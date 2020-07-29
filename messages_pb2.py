# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages.proto',
  package='messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0emessages.proto\x12\x08messages\"%\n\x07Request\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"\x1b\n\x0cRandomNumber\x12\x0b\n\x03num\x18\x01 \x01(\x03\x32U\n\x15RandomNumberGenerator\x12<\n\x0fGetRandomNumber\x12\x11.messages.Request\x1a\x16.messages.RandomNumberb\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='messages.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='messages.Request.start', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='messages.Request.end', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=65,
)


_RANDOMNUMBER = _descriptor.Descriptor(
  name='RandomNumber',
  full_name='messages.RandomNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='messages.RandomNumber.num', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=94,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['RandomNumber'] = _RANDOMNUMBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messages.Request)
  })
_sym_db.RegisterMessage(Request)

RandomNumber = _reflection.GeneratedProtocolMessageType('RandomNumber', (_message.Message,), {
  'DESCRIPTOR' : _RANDOMNUMBER,
  '__module__' : 'messages_pb2'
  # @@protoc_insertion_point(class_scope:messages.RandomNumber)
  })
_sym_db.RegisterMessage(RandomNumber)



_RANDOMNUMBERGENERATOR = _descriptor.ServiceDescriptor(
  name='RandomNumberGenerator',
  full_name='messages.RandomNumberGenerator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=96,
  serialized_end=181,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRandomNumber',
    full_name='messages.RandomNumberGenerator.GetRandomNumber',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RANDOMNUMBER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RANDOMNUMBERGENERATOR)

DESCRIPTOR.services_by_name['RandomNumberGenerator'] = _RANDOMNUMBERGENERATOR

# @@protoc_insertion_point(module_scope)