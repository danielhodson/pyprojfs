#!/usr/bin/python

import os
import sys
import ctypes
import ProjectedFS

# HRESULT
S_OK                    = 0x00000000
E_OUTOFMEMORY           = 0x8007000E
E_INVALIDARG            = 0x80070057

# HRESULT_FROM_WIN32()
ERROR_FILE_NOT_FOUND    = 0x80070002
ERROR_INVALID_PARAMETER = 0x80070057

# virtual/projected paths
virt_root = "C:\\vfs"
virt_file = "testing.txt"

# file metadata
fileBasicInfo = ProjectedFS.PRJ_FILE_BASIC_INFO()
fileBasicInfo.IsDirectory = False
fileBasicInfo.FileSize = 0x1000

sessions = dict()

@ProjectedFS.PRJ_START_DIRECTORY_ENUMERATION_CB
def startdir_enum_cb(callbackData, enumerationId):
    sessions[enumerationId.contents] = dict()
    return S_OK

@ProjectedFS.PRJ_END_DIRECTORY_ENUMERATION_CB
def enddir_enum_cb(callbackData, enumerationId):
    try:
        del sessions[enumerationId.contents]
        return S_OK
    except:
        pass

# just fill out a dummy entry for virt_file
@ProjectedFS.PRJ_GET_DIRECTORY_ENUMERATION_CB
def getdir_enum_cb(callbackData, enumerationId, searchExpression, dirEntryBufferHandle):
    try:
        if (("COMPLETED" not in sessions[enumerationId.contents]) or (callbackData.Flags & ProjectedFS.PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN)):
            if ProjectedFS.PrjFileNameMatch(virt_file, searchExpression):
                ProjectedFS.PrjFillDirEntryBuffer(virt_file, fileBasicInfo, dirEntryBufferHandle)
                sessions[enumerationId.contents]["COMPLETED"] = True
            else:
                return ERROR_FILE_NOT_FOUND
        return S_OK
    except:
        return ERROR_INVALID_PARAMETER

@ProjectedFS.PRJ_GET_PLACEHOLDER_INFO_CB
def getplaceholder_info_cb(callbackData):
    if ProjectedFS.PrjFileNameMatch(virt_file, callbackData.contents.FilePathName):
        PlaceholderInfo = ProjectedFS.PRJ_PLACEHOLDER_INFO()
        PlaceholderInfo.FileBasicInfo = fileBasicInfo
        ProjectedFS.PrjWritePlaceholderInfo(callbackData.contents.NamespaceVirtualizationContext, virt_file, PlaceholderInfo, ctypes.sizeof(PlaceholderInfo))
        return S_OK
    else:
        return ERROR_FILE_NOT_FOUND

@ProjectedFS.PRJ_GET_FILE_DATA_CB
def getfiledata_cb(callbackData, byteOffset, length):
    if length > fileBasicInfo.FileSize:
        return E_INVALIDARG

    writeBuffer = ProjectedFS.PrjAllocateAlignedBuffer(callbackData.contents.NamespaceVirtualizationContext,length)
    if not writeBuffer:
        return E_OUTOFMEMORY

    ctypes.memmove(ctypes.c_void_p(writeBuffer), "A" * length, length)
    ProjectedFS.PrjWriteFileData(callbackData.contents.NamespaceVirtualizationContext, callbackData.contents.DataStreamId,writeBuffer,byteOffset,length)
    ProjectedFS.PrjFreeAlignedBuffer(writeBuffer)
    return S_OK

# Hard coding our instance GUID for now
instanceId = ProjectedFS.GUID()
instanceId.Data1 = 0xD137C01A
instanceId.Data2 = 0xBAAD
instanceId.Data3 = 0xCAA7

if not os.path.exists(virt_root):
    print "%s does not exist yet, creating.." % (virt_root)
    os.mkdir(virt_root)

if not os.path.isdir(virt_root):
    print "%s is not a directory, exiting.." % (virt_root)
    sys.exit(1)

if ProjectedFS.PrjMarkDirectoryAsPlaceholder(virt_root, None, None, instanceId) != S_OK:
    print "Error marking %s directory as placeholder. Exiting.." % (virt_root)
    sys.exit(1)

# Populate the *required* provider callback routines
# QueryFileNameCallback, NotificationCallback, and CancelCommandCallback are optional
callbackTable = ProjectedFS.PRJ_CALLBACKS()
callbackTable.StartDirectoryEnumerationCallback = startdir_enum_cb
callbackTable.EndDirectoryEnumerationCallback = enddir_enum_cb
callbackTable.GetDirectoryEnumerationCallback = getdir_enum_cb
callbackTable.GetPlaceholderInfoCallback = getplaceholder_info_cb
callbackTable.GetFileDataCallback = getfiledata_cb

print "Starting virtualization instance"

# Start Provider
instanceHandle = ProjectedFS.PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT()
if ProjectedFS.PrjStartVirtualizing(virt_root, callbackTable, None, None, instanceHandle) != S_OK:
    print "Error starting virtualization. Exiting.."
    sys.exit(1)

# virt file exists from previous run? delete it
if os.path.isfile(virt_root + os.path.sep + virt_file):
    ProjectedFS.PrjDeleteFile(instanceHandle, virt_file, ProjectedFS.PRJ_UPDATE_ALLOW_DIRTY_METADATA | ProjectedFS.PRJ_UPDATE_ALLOW_DIRTY_DATA | ProjectedFS.PRJ_UPDATE_ALLOW_TOMBSTONE)

raw_input("Press any key to exit...")

# Stop Provider. MSDN says it returns an HRESULT, but the func prototype is void.
ProjectedFS.PrjStopVirtualizing(instanceHandle)
print "Stopped virtualization instance"
