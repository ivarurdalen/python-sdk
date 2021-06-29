# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exabel/api/data/v1/time_series_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from exabel_data_sdk.stubs.exabel.api.data.v1 import (
    time_series_messages_pb2 as exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2,
)
from exabel_data_sdk.stubs.exabel.api.time import (
    time_range_pb2 as exabel_dot_api_dot_time_dot_time__range__pb2,
)
from exabel_data_sdk.stubs.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="exabel/api/data/v1/time_series_service.proto",
    package="exabel.api.data.v1",
    syntax="proto3",
    serialized_options=b"\n\026com.exabel.api.data.v1B\026TimeSeriesServiceProtoP\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n,exabel/api/data/v1/time_series_service.proto\x12\x12\x65xabel.api.data.v1\x1a-exabel/api/data/v1/time_series_messages.proto\x1a exabel/api/time/time_range.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto"N\n\x15ListTimeSeriesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"z\n\x16ListTimeSeriesResponse\x12\x33\n\x0btime_series\x18\x01 \x03(\x0b\x32\x1e.exabel.api.data.v1.TimeSeries\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"V\n\x14GetTimeSeriesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x04view\x18\x02 \x01(\x0b\x32".exabel.api.data.v1.TimeSeriesView"\xd2\x01\n\x17\x43reateTimeSeriesRequest\x12\x33\n\x0btime_series\x18\x01 \x01(\x0b\x32\x1e.exabel.api.data.v1.TimeSeries\x12\x30\n\x04view\x18\x02 \x01(\x0b\x32".exabel.api.data.v1.TimeSeriesView\x12@\n\x12\x64\x65\x66\x61ult_known_time\x18\x03 \x01(\x0b\x32$.exabel.api.data.v1.DefaultKnownTime\x12\x0e\n\x06no_tag\x18\x04 \x01(\x08"\xc2\x01\n\x17UpdateTimeSeriesRequest\x12\x33\n\x0btime_series\x18\x01 \x01(\x0b\x32\x1e.exabel.api.data.v1.TimeSeries\x12\x30\n\x04view\x18\x02 \x01(\x0b\x32".exabel.api.data.v1.TimeSeriesView\x12@\n\x12\x64\x65\x66\x61ult_known_time\x18\x03 \x01(\x0b\x32$.exabel.api.data.v1.DefaultKnownTime"\'\n\x17\x44\x65leteTimeSeriesRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"c\n"BatchDeleteTimeSeriesPointsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x0btime_ranges\x18\x02 \x03(\x0b\x32\x1a.exabel.api.time.TimeRange2\xec\x0b\n\x11TimeSeriesService\x12\xc6\x01\n\x0eListTimeSeries\x12).exabel.api.data.v1.ListTimeSeriesRequest\x1a*.exabel.api.data.v1.ListTimeSeriesResponse"]\x82\xd3\xe4\x93\x02W\x12\x30/v1/{parent=entityTypes/*/entities/*}/timeSeriesZ#\x12!/v1/{parent=signals/*}/timeSeries\x12\xc9\x02\n\rGetTimeSeries\x12(.exabel.api.data.v1.GetTimeSeriesRequest\x1a\x1e.exabel.api.data.v1.TimeSeries"\xed\x01\x82\xd3\xe4\x93\x02\xe6\x01\x12?/v1/{name=entityTypes/*/entities/*/signals/*}/{view.known_time}ZA\x12?/v1/{name=signals/*/entityTypes/*/entities/*}/{view.known_time}Z/\x12-/v1/{name=entityTypes/*/entities/*/signals/*}Z/\x12-/v1/{name=signals/*/entityTypes/*/entities/*}\x12\xfb\x01\n\x10\x43reateTimeSeries\x12+.exabel.api.data.v1.CreateTimeSeriesRequest\x1a\x1e.exabel.api.data.v1.TimeSeries"\x99\x01\x82\xd3\xe4\x93\x02\x92\x01"9/v1/{time_series.name=entityTypes/*/entities/*/signals/*}:\x0btime_seriesZH"9/v1/{time_series.name=signals/*/entityTypes/*/entities/*}:\x0btime_series\x12\xfb\x01\n\x10UpdateTimeSeries\x12+.exabel.api.data.v1.UpdateTimeSeriesRequest\x1a\x1e.exabel.api.data.v1.TimeSeries"\x99\x01\x82\xd3\xe4\x93\x02\x92\x01\x32\x39/v1/{time_series.name=entityTypes/*/entities/*/signals/*}:\x0btime_seriesZH"9/v1/{time_series.name=signals/*/entityTypes/*/entities/*}:\x0btime_series\x12\xbf\x01\n\x10\x44\x65leteTimeSeries\x12+.exabel.api.data.v1.DeleteTimeSeriesRequest\x1a\x16.google.protobuf.Empty"f\x82\xd3\xe4\x93\x02`*-/v1/{name=entityTypes/*/entities/*/signals/*}Z/*-/v1/{name=signals/*/entityTypes/*/entities/*}\x12\x83\x02\n\x1b\x42\x61tchDeleteTimeSeriesPoints\x12\x36.exabel.api.data.v1.BatchDeleteTimeSeriesPointsRequest\x1a\x16.google.protobuf.Empty"\x93\x01\x82\xd3\xe4\x93\x02\x8c\x01"@/v1/{name=entityTypes/*/entities/*/signals/*}/points:batchDelete:\x01*ZE"@/v1/{name=signals/*/entityTypes/*/entities/*}/points:batchDelete:\x01*B2\n\x16\x63om.exabel.api.data.v1B\x16TimeSeriesServiceProtoP\x01\x62\x06proto3',
    dependencies=[
        exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2.DESCRIPTOR,
        exabel_dot_api_dot_time_dot_time__range__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
    ],
)


_LISTTIMESERIESREQUEST = _descriptor.Descriptor(
    name="ListTimeSeriesRequest",
    full_name="exabel.api.data.v1.ListTimeSeriesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="exabel.api.data.v1.ListTimeSeriesRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="exabel.api.data.v1.ListTimeSeriesRequest.page_size",
            index=1,
            number=2,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="exabel.api.data.v1.ListTimeSeriesRequest.page_token",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=208,
    serialized_end=286,
)


_LISTTIMESERIESRESPONSE = _descriptor.Descriptor(
    name="ListTimeSeriesResponse",
    full_name="exabel.api.data.v1.ListTimeSeriesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="time_series",
            full_name="exabel.api.data.v1.ListTimeSeriesResponse.time_series",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="next_page_token",
            full_name="exabel.api.data.v1.ListTimeSeriesResponse.next_page_token",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="total_size",
            full_name="exabel.api.data.v1.ListTimeSeriesResponse.total_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=288,
    serialized_end=410,
)


_GETTIMESERIESREQUEST = _descriptor.Descriptor(
    name="GetTimeSeriesRequest",
    full_name="exabel.api.data.v1.GetTimeSeriesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="exabel.api.data.v1.GetTimeSeriesRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="view",
            full_name="exabel.api.data.v1.GetTimeSeriesRequest.view",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=412,
    serialized_end=498,
)


_CREATETIMESERIESREQUEST = _descriptor.Descriptor(
    name="CreateTimeSeriesRequest",
    full_name="exabel.api.data.v1.CreateTimeSeriesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="time_series",
            full_name="exabel.api.data.v1.CreateTimeSeriesRequest.time_series",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="view",
            full_name="exabel.api.data.v1.CreateTimeSeriesRequest.view",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="default_known_time",
            full_name="exabel.api.data.v1.CreateTimeSeriesRequest.default_known_time",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="no_tag",
            full_name="exabel.api.data.v1.CreateTimeSeriesRequest.no_tag",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=501,
    serialized_end=711,
)


_UPDATETIMESERIESREQUEST = _descriptor.Descriptor(
    name="UpdateTimeSeriesRequest",
    full_name="exabel.api.data.v1.UpdateTimeSeriesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="time_series",
            full_name="exabel.api.data.v1.UpdateTimeSeriesRequest.time_series",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="view",
            full_name="exabel.api.data.v1.UpdateTimeSeriesRequest.view",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="default_known_time",
            full_name="exabel.api.data.v1.UpdateTimeSeriesRequest.default_known_time",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=714,
    serialized_end=908,
)


_DELETETIMESERIESREQUEST = _descriptor.Descriptor(
    name="DeleteTimeSeriesRequest",
    full_name="exabel.api.data.v1.DeleteTimeSeriesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="exabel.api.data.v1.DeleteTimeSeriesRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=910,
    serialized_end=949,
)


_BATCHDELETETIMESERIESPOINTSREQUEST = _descriptor.Descriptor(
    name="BatchDeleteTimeSeriesPointsRequest",
    full_name="exabel.api.data.v1.BatchDeleteTimeSeriesPointsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="exabel.api.data.v1.BatchDeleteTimeSeriesPointsRequest.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="time_ranges",
            full_name="exabel.api.data.v1.BatchDeleteTimeSeriesPointsRequest.time_ranges",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=951,
    serialized_end=1050,
)

_LISTTIMESERIESRESPONSE.fields_by_name[
    "time_series"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIES
_GETTIMESERIESREQUEST.fields_by_name[
    "view"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIESVIEW
_CREATETIMESERIESREQUEST.fields_by_name[
    "time_series"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIES
_CREATETIMESERIESREQUEST.fields_by_name[
    "view"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIESVIEW
_CREATETIMESERIESREQUEST.fields_by_name[
    "default_known_time"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._DEFAULTKNOWNTIME
_UPDATETIMESERIESREQUEST.fields_by_name[
    "time_series"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIES
_UPDATETIMESERIESREQUEST.fields_by_name[
    "view"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIESVIEW
_UPDATETIMESERIESREQUEST.fields_by_name[
    "default_known_time"
].message_type = exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._DEFAULTKNOWNTIME
_BATCHDELETETIMESERIESPOINTSREQUEST.fields_by_name[
    "time_ranges"
].message_type = exabel_dot_api_dot_time_dot_time__range__pb2._TIMERANGE
DESCRIPTOR.message_types_by_name["ListTimeSeriesRequest"] = _LISTTIMESERIESREQUEST
DESCRIPTOR.message_types_by_name["ListTimeSeriesResponse"] = _LISTTIMESERIESRESPONSE
DESCRIPTOR.message_types_by_name["GetTimeSeriesRequest"] = _GETTIMESERIESREQUEST
DESCRIPTOR.message_types_by_name["CreateTimeSeriesRequest"] = _CREATETIMESERIESREQUEST
DESCRIPTOR.message_types_by_name["UpdateTimeSeriesRequest"] = _UPDATETIMESERIESREQUEST
DESCRIPTOR.message_types_by_name["DeleteTimeSeriesRequest"] = _DELETETIMESERIESREQUEST
DESCRIPTOR.message_types_by_name[
    "BatchDeleteTimeSeriesPointsRequest"
] = _BATCHDELETETIMESERIESPOINTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListTimeSeriesRequest = _reflection.GeneratedProtocolMessageType(
    "ListTimeSeriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTTIMESERIESREQUEST,
        "__module__": "exabel.api.data.v1.time_series_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.ListTimeSeriesRequest)
    },
)
_sym_db.RegisterMessage(ListTimeSeriesRequest)

ListTimeSeriesResponse = _reflection.GeneratedProtocolMessageType(
    "ListTimeSeriesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTTIMESERIESRESPONSE,
        "__module__": "exabel.api.data.v1.time_series_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.ListTimeSeriesResponse)
    },
)
_sym_db.RegisterMessage(ListTimeSeriesResponse)

GetTimeSeriesRequest = _reflection.GeneratedProtocolMessageType(
    "GetTimeSeriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETTIMESERIESREQUEST,
        "__module__": "exabel.api.data.v1.time_series_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.GetTimeSeriesRequest)
    },
)
_sym_db.RegisterMessage(GetTimeSeriesRequest)

CreateTimeSeriesRequest = _reflection.GeneratedProtocolMessageType(
    "CreateTimeSeriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATETIMESERIESREQUEST,
        "__module__": "exabel.api.data.v1.time_series_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.CreateTimeSeriesRequest)
    },
)
_sym_db.RegisterMessage(CreateTimeSeriesRequest)

UpdateTimeSeriesRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateTimeSeriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATETIMESERIESREQUEST,
        "__module__": "exabel.api.data.v1.time_series_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.UpdateTimeSeriesRequest)
    },
)
_sym_db.RegisterMessage(UpdateTimeSeriesRequest)

DeleteTimeSeriesRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteTimeSeriesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETETIMESERIESREQUEST,
        "__module__": "exabel.api.data.v1.time_series_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.DeleteTimeSeriesRequest)
    },
)
_sym_db.RegisterMessage(DeleteTimeSeriesRequest)

BatchDeleteTimeSeriesPointsRequest = _reflection.GeneratedProtocolMessageType(
    "BatchDeleteTimeSeriesPointsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _BATCHDELETETIMESERIESPOINTSREQUEST,
        "__module__": "exabel.api.data.v1.time_series_service_pb2"
        # @@protoc_insertion_point(class_scope:exabel.api.data.v1.BatchDeleteTimeSeriesPointsRequest)
    },
)
_sym_db.RegisterMessage(BatchDeleteTimeSeriesPointsRequest)


DESCRIPTOR._options = None

_TIMESERIESSERVICE = _descriptor.ServiceDescriptor(
    name="TimeSeriesService",
    full_name="exabel.api.data.v1.TimeSeriesService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1053,
    serialized_end=2569,
    methods=[
        _descriptor.MethodDescriptor(
            name="ListTimeSeries",
            full_name="exabel.api.data.v1.TimeSeriesService.ListTimeSeries",
            index=0,
            containing_service=None,
            input_type=_LISTTIMESERIESREQUEST,
            output_type=_LISTTIMESERIESRESPONSE,
            serialized_options=b"\202\323\344\223\002W\0220/v1/{parent=entityTypes/*/entities/*}/timeSeriesZ#\022!/v1/{parent=signals/*}/timeSeries",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetTimeSeries",
            full_name="exabel.api.data.v1.TimeSeriesService.GetTimeSeries",
            index=1,
            containing_service=None,
            input_type=_GETTIMESERIESREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIES,
            serialized_options=b"\202\323\344\223\002\346\001\022?/v1/{name=entityTypes/*/entities/*/signals/*}/{view.known_time}ZA\022?/v1/{name=signals/*/entityTypes/*/entities/*}/{view.known_time}Z/\022-/v1/{name=entityTypes/*/entities/*/signals/*}Z/\022-/v1/{name=signals/*/entityTypes/*/entities/*}",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="CreateTimeSeries",
            full_name="exabel.api.data.v1.TimeSeriesService.CreateTimeSeries",
            index=2,
            containing_service=None,
            input_type=_CREATETIMESERIESREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIES,
            serialized_options=b'\202\323\344\223\002\222\001"9/v1/{time_series.name=entityTypes/*/entities/*/signals/*}:\013time_seriesZH"9/v1/{time_series.name=signals/*/entityTypes/*/entities/*}:\013time_series',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateTimeSeries",
            full_name="exabel.api.data.v1.TimeSeriesService.UpdateTimeSeries",
            index=3,
            containing_service=None,
            input_type=_UPDATETIMESERIESREQUEST,
            output_type=exabel_dot_api_dot_data_dot_v1_dot_time__series__messages__pb2._TIMESERIES,
            serialized_options=b'\202\323\344\223\002\222\00129/v1/{time_series.name=entityTypes/*/entities/*/signals/*}:\013time_seriesZH"9/v1/{time_series.name=signals/*/entityTypes/*/entities/*}:\013time_series',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DeleteTimeSeries",
            full_name="exabel.api.data.v1.TimeSeriesService.DeleteTimeSeries",
            index=4,
            containing_service=None,
            input_type=_DELETETIMESERIESREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b"\202\323\344\223\002`*-/v1/{name=entityTypes/*/entities/*/signals/*}Z/*-/v1/{name=signals/*/entityTypes/*/entities/*}",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="BatchDeleteTimeSeriesPoints",
            full_name="exabel.api.data.v1.TimeSeriesService.BatchDeleteTimeSeriesPoints",
            index=5,
            containing_service=None,
            input_type=_BATCHDELETETIMESERIESPOINTSREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b'\202\323\344\223\002\214\001"@/v1/{name=entityTypes/*/entities/*/signals/*}/points:batchDelete:\001*ZE"@/v1/{name=signals/*/entityTypes/*/entities/*}/points:batchDelete:\001*',
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_TIMESERIESSERVICE)

DESCRIPTOR.services_by_name["TimeSeriesService"] = _TIMESERIESSERVICE

# @@protoc_insertion_point(module_scope)
