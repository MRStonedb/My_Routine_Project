# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import kafka_push_pb2 as kafka__push__pb2


class KafkaProduceHandlerStub(object):
  """The KafkaProduceHandler service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.PushToKafka = channel.unary_unary(
        '/kafka_produce.KafkaProduceHandler/PushToKafka',
        request_serializer=kafka__push__pb2.KafkaProduceRequest.SerializeToString,
        response_deserializer=kafka__push__pb2.KafkaProduceReply.FromString,
        )


class KafkaProduceHandlerServicer(object):
  """The KafkaProduceHandler service definition.
  """

  def PushToKafka(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KafkaProduceHandlerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'PushToKafka': grpc.unary_unary_rpc_method_handler(
          servicer.PushToKafka,
          request_deserializer=kafka__push__pb2.KafkaProduceRequest.FromString,
          response_serializer=kafka__push__pb2.KafkaProduceReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'kafka_produce.KafkaProduceHandler', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
