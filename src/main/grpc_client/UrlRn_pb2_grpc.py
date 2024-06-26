# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import UrlRn_pb2 as UrlRn__pb2


class UrlRnStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getUrlByUsuario = channel.unary_unary(
                '/urlRn.UrlRn/getUrlByUsuario',
                request_serializer=UrlRn__pb2.UrlByUsuarioRequest.SerializeToString,
                response_deserializer=UrlRn__pb2.UrlByUsuarioResponse.FromString,
                )
        self.crearUrlByUsuario = channel.unary_unary(
                '/urlRn.UrlRn/crearUrlByUsuario',
                request_serializer=UrlRn__pb2.crearUrlRequest.SerializeToString,
                response_deserializer=UrlRn__pb2.UrlByUsuarioResponse.FromString,
                )


class UrlRnServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getUrlByUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def crearUrlByUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UrlRnServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getUrlByUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.getUrlByUsuario,
                    request_deserializer=UrlRn__pb2.UrlByUsuarioRequest.FromString,
                    response_serializer=UrlRn__pb2.UrlByUsuarioResponse.SerializeToString,
            ),
            'crearUrlByUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.crearUrlByUsuario,
                    request_deserializer=UrlRn__pb2.crearUrlRequest.FromString,
                    response_serializer=UrlRn__pb2.UrlByUsuarioResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'urlRn.UrlRn', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UrlRn(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getUrlByUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/urlRn.UrlRn/getUrlByUsuario',
            UrlRn__pb2.UrlByUsuarioRequest.SerializeToString,
            UrlRn__pb2.UrlByUsuarioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def crearUrlByUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/urlRn.UrlRn/crearUrlByUsuario',
            UrlRn__pb2.crearUrlRequest.SerializeToString,
            UrlRn__pb2.UrlByUsuarioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
