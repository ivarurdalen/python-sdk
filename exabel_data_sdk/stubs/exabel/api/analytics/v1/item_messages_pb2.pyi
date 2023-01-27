"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ItemMetadata(google.protobuf.message.Message):
    """Metadata about an item."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CREATE_TIME_FIELD_NUMBER: builtins.int
    UPDATE_TIME_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    UPDATED_BY_FIELD_NUMBER: builtins.int
    WRITE_ACCESS_FIELD_NUMBER: builtins.int

    @property
    def create_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """When the item was created."""

    @property
    def update_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """When the item was last updated."""
    created_by: builtins.str
    'Resource name of the user who created the item.'
    updated_by: builtins.str
    'Resource name of the user who last updated the item.'
    write_access: builtins.bool
    'Whether the API caller has write access to the item.\n    May not always be populated.\n    '

    def __init__(self, *, create_time: google.protobuf.timestamp_pb2.Timestamp | None=..., update_time: google.protobuf.timestamp_pb2.Timestamp | None=..., created_by: builtins.str | None=..., updated_by: builtins.str | None=..., write_access: builtins.bool | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['_write_access', b'_write_access', 'create_time', b'create_time', 'update_time', b'update_time', 'write_access', b'write_access']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['_write_access', b'_write_access', 'create_time', b'create_time', 'created_by', b'created_by', 'update_time', b'update_time', 'updated_by', b'updated_by', 'write_access', b'write_access']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing_extensions.Literal['_write_access', b'_write_access']) -> typing_extensions.Literal['write_access'] | None:
        ...
global___ItemMetadata = ItemMetadata