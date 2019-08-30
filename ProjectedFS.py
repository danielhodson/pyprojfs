#!/usr/bin/python

from ctypes import *
from ctypes.wintypes import *

_prjfs = windll.ProjectedFSLib

#### ~~~~~
####
#### Common structures
####
#### ~~~~~

from comtypes import GUID

# class GUID(Structure):
#   _fields_ = [('Data1', c_uint32),
#               ('Data2', c_short),
#               ('Data3', c_short),
#               ('Data4', c_ubyte * 8)]

#   def __init__(self):
#     oledll.ole32.CoCreateGuid(byref(self))

# typedef enum PRJ_NOTIFY_TYPES
# {
PRJ_NOTIFY_NONE                                 = 0x00000000
PRJ_NOTIFY_SUPPRESS_NOTIFICATIONS               = 0x00000001
PRJ_NOTIFY_FILE_OPENED                          = 0x00000002
PRJ_NOTIFY_NEW_FILE_CREATED                     = 0x00000004
PRJ_NOTIFY_FILE_OVERWRITTEN                     = 0x00000008
PRJ_NOTIFY_PRE_DELETE                           = 0x00000010
PRJ_NOTIFY_PRE_RENAME                           = 0x00000020
PRJ_NOTIFY_PRE_SET_HARDLINK                     = 0x00000040
PRJ_NOTIFY_FILE_RENAMED                         = 0x00000080
PRJ_NOTIFY_HARDLINK_CREATED                     = 0x00000100
PRJ_NOTIFY_FILE_HANDLE_CLOSED_NO_MODIFICATION   = 0x00000200
PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_MODIFIED     = 0x00000400
PRJ_NOTIFY_FILE_HANDLE_CLOSED_FILE_DELETED      = 0x00000800
PRJ_NOTIFY_FILE_PRE_CONVERT_TO_FULL             = 0x00001000
PRJ_NOTIFY_USE_EXISTING_MASK                    = 0xFFFFFFFF
# } PRJ_NOTIFY_TYPES;

# typedef enum PRJ_NOTIFICATION
# {
PRJ_NOTIFICATION_FILE_OPENED                        = 0x00000002
PRJ_NOTIFICATION_NEW_FILE_CREATED                   = 0x00000004
PRJ_NOTIFICATION_FILE_OVERWRITTEN                   = 0x00000008
PRJ_NOTIFICATION_PRE_DELETE                         = 0x00000010
PRJ_NOTIFICATION_PRE_RENAME                         = 0x00000020
PRJ_NOTIFICATION_PRE_SET_HARDLINK                   = 0x00000040
PRJ_NOTIFICATION_FILE_RENAMED                       = 0x00000080
PRJ_NOTIFICATION_HARDLINK_CREATED                   = 0x00000100
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_NO_MODIFICATION = 0x00000200
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_MODIFIED   = 0x00000400
PRJ_NOTIFICATION_FILE_HANDLE_CLOSED_FILE_DELETED    = 0x00000800
PRJ_NOTIFICATION_FILE_PRE_CONVERT_TO_FULL           = 0x00001000
# } PRJ_NOTIFICATION;

# DECLARE_HANDLE(PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT);
PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT = HANDLE
# DECLARE_HANDLE(PRJ_DIR_ENTRY_BUFFER_HANDLE);
PRJ_DIR_ENTRY_BUFFER_HANDLE = HANDLE

#### ~~~~~
####
#### Virtualization instance APIs
####
#### ~~~~~

# typedef struct PRJ_NOTIFICATION_MAPPING
class PRJ_NOTIFICATION_MAPPING(Structure):
  _fields = [('NotificationBitMask', c_int),
             ('NotificationRoot', LPCWSTR)]
# } PRJ_NOTIFICATION_MAPPING;

# typedef enum PRJ_STARTVIRTUALIZING_FLAGS
# {
PRJ_FLAG_NONE                       = 0x00000000
PRJ_FLAG_USE_NEGATIVE_PATH_CACHE    = 0x00000001
# } PRJ_STARTVIRTUALIZING_FLAGS;

# typedef struct PRJ_STARTVIRTUALIZING_OPTIONS
# {
class PRJ_STARTVIRTUALIZING_OPTIONS(Structure):
  _fields = [('Flags', c_int),
             ('PoolThreadCount', c_uint),
             ('ConcurrentThreadCount', c_uint),
             ('NotificationMappings', POINTER(PRJ_NOTIFICATION_MAPPING)),
             ('NotificationMappingsCount', c_uint)]
# } PRJ_STARTVIRTUALIZING_OPTIONS;

# STDAPI_(void)
# PrjStopVirtualizing(
#     _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext
#     );

__prototype = WINFUNCTYPE(None, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT)
__paramflags = ((1, "namespaceVirtualizationContext"),)
PrjStopVirtualizing = __prototype(("PrjStopVirtualizing", _prjfs), __paramflags)

# STDAPI
# PrjClearNegativePathCache(
#    _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext,
#    _Out_opt_ UINT32* totalEntryNumber
#    );


__prototype = WINFUNCTYPE(HRESULT, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, POINTER(c_uint32))
__paramflags = ((1, "namespaceVirtualizationContext"), (2, "totalEntryNumber"))
PrjClearNegativePathCache = __prototype(("PrjClearNegativePathCache", _prjfs), __paramflags)

# typedef struct PRJ_VIRTUALIZATION_INSTANCE_INFO
# {
class PRJ_VIRTUALIZATION_INSTANCE_INFO(Structure):
  _fields_ = [('InstanceID', GUID),
              ('WriteAlignment', c_uint32)]
# } PRJ_VIRTUALIZATION_INSTANCE_INFO;

# STDAPI
# PrjGetVirtualizationInstanceInfo(
#    _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext,
#    _Out_ PRJ_VIRTUALIZATION_INSTANCE_INFO* virtualizationInstanceInfo
#    );

__prototype = WINFUNCTYPE(HRESULT, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, POINTER(PRJ_VIRTUALIZATION_INSTANCE_INFO))
__paramflags = ((1, "namespaceVirtualizationContext"), (2, "virtualizationInstanceInfo"))
PrjGetVirtualizationInstanceInfo = __prototype(("PrjGetVirtualizationInstanceInfo", _prjfs), __paramflags)


#### ~~~~~
####
#### Placeholder and File APIs
####
#### ~~~~~

# typedef enum PRJ_PLACEHOLDER_ID
# {
PRJ_PLACEHOLDER_ID_LENGTH = 128
# } PRJ_PLACEHOLDER_ID;

# typedef struct PRJ_PLACEHOLDER_VERSION_INFO
# {
class PRJ_PLACEHOLDER_VERSION_INFO(Structure):
  _fields_ = [('ProviderID', c_ubyte * PRJ_PLACEHOLDER_ID_LENGTH),
              ('ContentID', c_ubyte * PRJ_PLACEHOLDER_ID_LENGTH)]
# } PRJ_PLACEHOLDER_VERSION_INFO;

# STDAPI
# PrjMarkDirectoryAsPlaceholder(
#     _In_ PCWSTR rootPathName,
#     _In_opt_ PCWSTR targetPathName,
#     _In_opt_ const PRJ_PLACEHOLDER_VERSION_INFO* versionInfo,
#     _In_ const GUID* virtualizationInstanceID
#     );
__prototype = WINFUNCTYPE(HRESULT, LPCWSTR, LPCWSTR, POINTER(PRJ_PLACEHOLDER_VERSION_INFO), POINTER(GUID))
__paramflags = ((1, "rootPathName"), (1, "targetPathName"), (1, "versionInfo"), (1, "virtualizationInstanceID"))
PrjMarkDirectoryAsPlaceholder = __prototype(("PrjMarkDirectoryAsPlaceholder", _prjfs), __paramflags)

# typedef struct PRJ_FILE_BASIC_INFO {
class PRJ_FILE_BASIC_INFO(Structure):
  _fields_ = [('IsDirectory', BOOLEAN),
              ('FileSize', c_longlong),
              ('CreationTime', LARGE_INTEGER),
              ('LastAccessTime', LARGE_INTEGER),
              ('LastWriteTime', LARGE_INTEGER),
              ('ChangeTime', LARGE_INTEGER),
              ('FileAttributes', c_uint32)]
# } PRJ_FILE_BASIC_INFO;

# typedef struct PRJ_PLACEHOLDER_INFO
# {
class EaInformation(Structure):
  _fields_ = [('EaBufferSize', c_uint32),
              ('OffsetToFirstEa', c_uint32)]

class SecurityInformation(Structure):
  _fields_ = [('SecurityBufferSize', c_uint32),
              ('OffsetToSecurityDescriptor', c_uint32)]

class StreamsInformation(Structure):
  _fields_ = [('StreamsInfoBufferSize', c_uint32),
              ('OffsetToFirstStreamInfo', c_uint32)]

class PRJ_PLACEHOLDER_INFO(Structure):
  _fields_ = [('FileBasicInfo', PRJ_FILE_BASIC_INFO),
              ('EaInformation', EaInformation),
              ('SecurityInformation', SecurityInformation),
              ('StreamsInformation', StreamsInformation),
              ('VersionInfo', PRJ_PLACEHOLDER_VERSION_INFO),
              ('VariableData', c_ubyte * 1)]
# } PRJ_PLACEHOLDER_INFO;

# STDAPI
# PrjWritePlaceholderInfo(
#     _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext,
#     _In_ PCWSTR destinationFileName,
#     _In_reads_bytes_(placeholderInfoSize) const PRJ_PLACEHOLDER_INFO* placeholderInfo,
#     _In_ UINT32 placeholderInfoSize
#     );
__prototype = WINFUNCTYPE(HRESULT, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, LPCWSTR, POINTER(PRJ_PLACEHOLDER_INFO), c_uint32)
__paramflags = ((1, "namespaceVirtualizationContext"), (1, "destinationFileName"), (1, "placeholderInfo"), (1, "placeholderInfoSize"))
PrjWritePlaceholderInfo = __prototype(("PrjWritePlaceholderInfo", _prjfs), __paramflags)

# typedef enum PRJ_UPDATE_TYPES
# {
PRJ_UPDATE_NONE                 = 0x00000000
PRJ_UPDATE_ALLOW_DIRTY_METADATA = 0x00000001
PRJ_UPDATE_ALLOW_DIRTY_DATA     = 0x00000002
PRJ_UPDATE_ALLOW_TOMBSTONE      = 0x00000004
PRJ_UPDATE_RESERVED1            = 0x00000008
PRJ_UPDATE_RESERVED2            = 0x00000010
PRJ_UPDATE_ALLOW_READ_ONLY      = 0x00000020
PRJ_UPDATE_MAX_VAL = (PRJ_UPDATE_ALLOW_READ_ONLY << 1)
# } PRJ_UPDATE_TYPES;

# DEFINE_ENUM_FLAG_OPERATORS(PRJ_UPDATE_TYPES);

# typedef enum PRJ_UPDATE_FAILURE_CAUSES
# {
PRJ_UPDATE_FAILURE_CAUSE_NONE           = 0x00000000
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_METADATA = 0x00000001
PRJ_UPDATE_FAILURE_CAUSE_DIRTY_DATA     = 0x00000002
PRJ_UPDATE_FAILURE_CAUSE_TOMBSTONE      = 0x00000004
PRJ_UPDATE_FAILURE_CAUSE_READ_ONLY      = 0x00000008
# } PRJ_UPDATE_FAILURE_CAUSES;

# DEFINE_ENUM_FLAG_OPERATORS(PRJ_UPDATE_FAILURE_CAUSES);

# STDAPI
# PrjUpdateFileIfNeeded(
#     _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext,
#     _In_ PCWSTR destinationFileName,
#     _In_reads_bytes_(placeholderInfoSize) const PRJ_PLACEHOLDER_INFO* placeholderInfo,
#     _In_ UINT32 placeholderInfoSize,
#     _In_opt_ PRJ_UPDATE_TYPES updateFlags,
#     _Out_opt_ PRJ_UPDATE_FAILURE_CAUSES* failureReason
#     );
__prototype = WINFUNCTYPE(HRESULT, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, LPCWSTR, POINTER(PRJ_PLACEHOLDER_INFO), c_uint32, c_uint32, POINTER(c_uint32))
__paramflags = ((1, "namespaceVirtualizationContext"), (1, "destinationFileName"), (1, "placeholderInfo"), (1, "placeholderInfoSize"), (1, "updateFlags"), (2, "failureReason"))
PrjUpdateFileIfNeeded = __prototype(("PrjUpdateFileIfNeeded", _prjfs), __paramflags)
 
# STDAPI
# PrjDeleteFile(
#     _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext,
#     _In_ PCWSTR destinationFileName,
#     _In_opt_ PRJ_UPDATE_TYPES updateFlags,
#     _Out_opt_ PRJ_UPDATE_FAILURE_CAUSES* failureReason
#    );
__prototype = WINFUNCTYPE(HRESULT, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, LPCWSTR, c_uint32, POINTER(c_uint32))
__paramflags = ((1, "namespaceVirtualizationContext"), (1, "destinationFileName"), (1, "updateFlags"), (2, "failureReason"))
PrjDeleteFile = __prototype(("PrjDeleteFile", _prjfs), __paramflags)
 
# STDAPI
# PrjWriteFileData(
#     _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext,
#     _In_ const GUID* dataStreamId,
#     _In_reads_bytes_(length) void* buffer,
#     _In_ UINT64 byteOffset,
#     _In_ UINT32 length
#     );
__prototype = WINFUNCTYPE(HRESULT, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, POINTER(GUID), c_void_p, c_ulonglong, c_uint32)
__paramflags = ((1, "namespaceVirtualizationContext"), (1, "dataStreamId"), (1, "buffer"), (1, "byteOffset"), (1, "length"))
PrjWriteFileData = __prototype(("PrjWriteFileData", _prjfs), __paramflags)
 
# typedef enum PRJ_FILE_STATE
# {
PRJ_FILE_STATE_PLACEHOLDER          = 0x00000001
PRJ_FILE_STATE_HYDRATED_PLACEHOLDER = 0x00000002
PRJ_FILE_STATE_DIRTY_PLACEHOLDER    = 0x00000004
PRJ_FILE_STATE_FULL                 = 0x00000008
PRJ_FILE_STATE_TOMBSTONE            = 0x00000010
# } PRJ_FILE_STATE;

# DEFINE_ENUM_FLAG_OPERATORS(PRJ_FILE_STATE);

# STDAPI
# PrjGetOnDiskFileState(
#     _In_ PCWSTR destinationFileName,
#     _Out_ PRJ_FILE_STATE* fileState
#     );
__prototype = WINFUNCTYPE(HRESULT, LPCWSTR, POINTER(c_uint32))
__paramflags = ((1, "destinationFileName"), (2, "fileState"))
PrjGetOnDiskFileState = __prototype(("PrjGetOnDiskFileState", _prjfs), __paramflags)
 
# STDAPI_(void*)
# PrjAllocateAlignedBuffer (
#     _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext,
#     _In_ size_t size
#     );
__prototype = WINFUNCTYPE(c_void_p, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, c_size_t)
__paramflags = ((1, "namespaceVirtualizationContext"), (1, "size"))
PrjAllocateAlignedBuffer = __prototype(("PrjAllocateAlignedBuffer", _prjfs), __paramflags)
 
# STDAPI_(void)
# PrjFreeAlignedBuffer (
#     _In_ void* buffer
#     );
__prototype = WINFUNCTYPE(None, c_void_p)
__paramflags = ((1, "buffer"),)
PrjFreeAlignedBuffer = __prototype(("PrjFreeAlignedBuffer", _prjfs), __paramflags)

#### ~~~~~
####
#### Callback support
####
#### ~~~~~

#  typedef enum PRJ_CALLBACK_DATA_FLAGS
#  {
PRJ_CB_DATA_FLAG_ENUM_RESTART_SCAN          = 0x00000001
PRJ_CB_DATA_FLAG_ENUM_RETURN_SINGLE_ENTRY   = 0x00000002
#  } PRJ_CALLBACK_DATA_FLAGS;
  
#  typedef struct PRJ_CALLBACK_DATA
#  {
class PRJ_CALLBACK_DATA(Structure):
  _fields_ = [('Size', c_uint32),
              ('Flags', c_uint32),
              ('NamespaceVirtualizationContext', PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT),
              ('CommandId', c_int32),
              ('FileId', GUID),
              ('DataStreamId', GUID),
              ('FilePathName', LPCWSTR),
              ('VersionInfo', POINTER(PRJ_PLACEHOLDER_VERSION_INFO)),
              ('TriggeringProcessId', c_uint32),
              ('TriggeringProcessImageFileName', LPCWSTR),
              ('InstanceContext', c_void_p)]
#  } PRJ_CALLBACK_DATA;

# typedef
# _Function_class_(PRJ_START_DIRECTORY_ENUMERATION_CB)
# HRESULT
# (CALLBACK PRJ_START_DIRECTORY_ENUMERATION_CB)(
#     _In_ const PRJ_CALLBACK_DATA* callbackData,
#     _In_ const GUID* enumerationId
#     );
PRJ_START_DIRECTORY_ENUMERATION_CB = WINFUNCTYPE(HRESULT, POINTER(PRJ_CALLBACK_DATA), POINTER(GUID))
 
# typedef
# _Function_class_(PRJ_GET_DIRECTORY_ENUMERATION_CB)
# HRESULT
# (CALLBACK PRJ_GET_DIRECTORY_ENUMERATION_CB)(
#     _In_ const PRJ_CALLBACK_DATA* callbackData,
#     _In_ const GUID* enumerationId,
#     _In_opt_ PCWSTR searchExpression,
#     _In_ PRJ_DIR_ENTRY_BUFFER_HANDLE dirEntryBufferHandle
#     );
PRJ_GET_DIRECTORY_ENUMERATION_CB = WINFUNCTYPE(HRESULT, POINTER(PRJ_CALLBACK_DATA), POINTER(GUID), LPCWSTR, PRJ_DIR_ENTRY_BUFFER_HANDLE)
 
# typedef
# _Function_class_(PRJ_END_DIRECTORY_ENUMERATION_CB)
# HRESULT
# (CALLBACK PRJ_END_DIRECTORY_ENUMERATION_CB)(
#     _In_ const PRJ_CALLBACK_DATA* callbackData,
#     _In_ const GUID* enumerationId
#     );
PRJ_END_DIRECTORY_ENUMERATION_CB = WINFUNCTYPE(HRESULT, POINTER(PRJ_CALLBACK_DATA), POINTER(GUID))
 
# typedef
# _Function_class_(PRJ_GET_PLACEHOLDER_INFO_CB)
# HRESULT
# (CALLBACK PRJ_GET_PLACEHOLDER_INFO_CB)(
#     _In_ const PRJ_CALLBACK_DATA* callbackData
#     );
PRJ_GET_PLACEHOLDER_INFO_CB = WINFUNCTYPE(HRESULT, POINTER(PRJ_CALLBACK_DATA))
 
# typedef
# _Function_class_(PRJ_GET_FILE_DATA_CB)
# HRESULT
# (CALLBACK PRJ_GET_FILE_DATA_CB)(
#     _In_ const PRJ_CALLBACK_DATA* callbackData,
#     _In_ UINT64 byteOffset,
#     _In_ UINT32 length
#     );
PRJ_GET_FILE_DATA_CB = WINFUNCTYPE(HRESULT, POINTER(PRJ_CALLBACK_DATA), c_ulonglong, c_uint32)
 
# typedef
# _Function_class_(PRJ_QUERY_FILE_NAME_CB)
# HRESULT
# (CALLBACK PRJ_QUERY_FILE_NAME_CB)(
#     _In_ const PRJ_CALLBACK_DATA* callbackData
#     );
PRJ_QUERY_FILE_NAME_CB = WINFUNCTYPE(HRESULT, POINTER(PRJ_CALLBACK_DATA))

# typedef union PRJ_NOTIFICATION_PARAMETERS
# {
class PostCreate(Structure):
  _fields_ = [('NotificationMask', c_uint32)]

class FileRenamed(Structure):
  _fields_ = [('Notificationmask', c_uint32)]

class FileDeletedOnHandleClose(Structure):
  _fields_ = [('IsFileModified', BOOLEAN)]

class PRJ_NOTIFICATION_PARAMETERS(Union):
  _fields_ = [('PostCreate', PostCreate),
              ('FileRenamed', FileRenamed),
              ('FileDeletedOnHandleClose', FileDeletedOnHandleClose)]
# } PRJ_NOTIFICATION_PARAMETERS;


# typedef
# _Function_class_(PRJ_NOTIFICATION_CB)
# HRESULT
# (CALLBACK PRJ_NOTIFICATION_CB)(
#     _In_ const PRJ_CALLBACK_DATA* callbackData,
#     _In_ BOOLEAN isDirectory,
#     _In_ PRJ_NOTIFICATION notification,
#     _In_opt_ PCWSTR destinationFileName,
#     _Inout_ PRJ_NOTIFICATION_PARAMETERS* operationParameters
#     );
PRJ_NOTIFICATION_CB = WINFUNCTYPE(HRESULT, POINTER(PRJ_CALLBACK_DATA), BOOLEAN, c_uint32, LPCWSTR, POINTER(PRJ_NOTIFICATION_PARAMETERS))
 
# typedef
# _Function_class_(PRJ_CANCEL_COMMAND_CB)
# VOID
# (CALLBACK PRJ_CANCEL_COMMAND_CB)(
#     _In_ const PRJ_CALLBACK_DATA* callbackData
#     );
PRJ_CANCEL_COMMAND_CB = WINFUNCTYPE(HRESULT, POINTER(PRJ_CALLBACK_DATA))
 
# typedef struct PRJ_CALLBACKS {
class PRJ_CALLBACKS(Structure):
  _fields_ = [('StartDirectoryEnumerationCallback', PRJ_START_DIRECTORY_ENUMERATION_CB),
              ('EndDirectoryEnumerationCallback', PRJ_END_DIRECTORY_ENUMERATION_CB),
              ('GetDirectoryEnumerationCallback', PRJ_GET_DIRECTORY_ENUMERATION_CB),
              ('GetPlaceholderInfoCallback', PRJ_GET_PLACEHOLDER_INFO_CB),
              ('GetFileDataCallback', PRJ_GET_FILE_DATA_CB),
              ('QueryFileNameCallback', PRJ_QUERY_FILE_NAME_CB),
              ('NotificationCallback', PRJ_NOTIFICATION_CB),
              ('CancelCommandCallback', PRJ_CANCEL_COMMAND_CB)]
# } PRJ_CALLBACKS;

# STDAPI
# PrjStartVirtualizing(
#    _In_ PCWSTR virtualizationRootPath,
#    _In_ const PRJ_CALLBACKS* callbacks,
#    _In_opt_ const void* instanceContext,
#    _In_opt_ const PRJ_STARTVIRTUALIZING_OPTIONS* options,
#    _Outptr_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT* namespaceVirtualizationContext
#    );
__prototype = WINFUNCTYPE(HRESULT, LPCWSTR, POINTER(PRJ_CALLBACKS), c_void_p, POINTER(PRJ_STARTVIRTUALIZING_OPTIONS), POINTER(PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT))
__paramflags = ((1, "virtualizationRootPath"), (1, "callbacks"), (1, "instanceContext"), (1, "options"), (2, "namespaceVirtualizationContext"))
PrjStartVirtualizing = __prototype(("PrjStartVirtualizing", _prjfs))
#PrjStartVirtualizing = __prototype(("PrjStartVirtualizing", _prjfs), __paramflags)
 
# typedef enum PRJ_COMPLETE_COMMAND_TYPE
# {
PRJ_COMPLETE_COMMAND_TYPE_NOTIFICATION = 1
PRJ_COMPLETE_COMMAND_TYPE_ENUMERATION = 2
# } PRJ_COMPLETE_COMMAND_TYPE;

# typedef struct PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS {
class Notification(Structure):
  _fields_ = [('NotificationMask', c_uint32)]

class Enumeration(Structure):
  _fields_ = [('DirEntryBufferHandle', PRJ_DIR_ENTRY_BUFFER_HANDLE)]

class DUMMYUNIONNAME(Union):
  _fields_ = [('Notification', Notification),
              ('Enumeration', Enumeration)]

class PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS(Structure):
  _fields_ = [('DUMMYUNIONNAME', DUMMYUNIONNAME)]
# } PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS;
 
# STDAPI
# PrjCompleteCommand(
#     _In_ PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT namespaceVirtualizationContext,
#     _In_ INT32 commandId,
#     _In_ HRESULT completionResult,
#     _In_opt_ PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS* extendedParameters
#     );
__prototype = WINFUNCTYPE(HRESULT, PRJ_NAMESPACE_VIRTUALIZATION_CONTEXT, c_int32, HRESULT, POINTER(PRJ_COMPLETE_COMMAND_EXTENDED_PARAMETERS))
__paramflags = ((1, "namespaceVirtualizationContext"), (1, "commandId"), (1, "completionResult"), (1, "extendedParameters"))
PrjCompleteCommand = __prototype(("PrjCompleteCommand", _prjfs), __paramflags)


#### ~~~~~
####
#### Enumeration apis
####
#### ~~~~~

# STDAPI
# PrjFillDirEntryBuffer(
#     _In_ PCWSTR fileName,
#     _In_opt_ PRJ_FILE_BASIC_INFO* fileBasicInfo,
#     _In_ PRJ_DIR_ENTRY_BUFFER_HANDLE dirEntryBufferHandle
#     );
__prototype = WINFUNCTYPE(HRESULT, LPCWSTR, POINTER(PRJ_FILE_BASIC_INFO), PRJ_DIR_ENTRY_BUFFER_HANDLE)
__paramflags = ((1, "fileName"), (1, "fileBasicInfo"), (1, "dirEntryBufferHandle"))
PrjFillDirEntryBuffer = __prototype(("PrjFillDirEntryBuffer", _prjfs), __paramflags)
 
# STDAPI_(BOOLEAN)
# PrjFileNameMatch (
#     _In_ PCWSTR fileNameToCheck,
#     _In_ PCWSTR pattern
#     );
__prototype = WINFUNCTYPE(HRESULT, LPCWSTR, LPCWSTR)
__paramflags = ((1, "fileNameToCheck"), (1, "pattern"))
PrjFileNameMatch = __prototype(("PrjFileNameMatch", _prjfs), __paramflags)
 
# STDAPI_(int)
# PrjFileNameCompare (
#     _In_ PCWSTR fileName1,
#     _In_ PCWSTR fileName2
#     );
__prototype = WINFUNCTYPE(HRESULT, LPCWSTR, LPCWSTR)
__paramflags = ((1, "fileName1"), (1, "fileName2"))
PrjFileNameCompare = __prototype(("PrjFileNameCompare", _prjfs), __paramflags)
 
# STDAPI_(BOOLEAN)
# PrjDoesNameContainWildCards (
#     _In_ LPCWSTR fileName
#     );
__prototype = WINFUNCTYPE(HRESULT, LPCWSTR) 
__paramflags = ((1, "fileName"),)
PrjDoesNameContainWildCards = __prototype(("PrjDoesNameContainWildCards", _prjfs), __paramflags)
