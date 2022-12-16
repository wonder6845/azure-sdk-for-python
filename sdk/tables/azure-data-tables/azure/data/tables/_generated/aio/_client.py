# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable

from azure.core import AsyncPipelineClient
from azure.core.rest import AsyncHttpResponse, HttpRequest

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import AzureTableConfiguration
from .operations import ServiceOperations, TableOperations


class AzureTable:  # pylint: disable=client-accepts-api-version-keyword
    """AzureTable.

    :ivar table: TableOperations operations
    :vartype table: azure.table.aio.operations.TableOperations
    :ivar service: ServiceOperations operations
    :vartype service: azure.table.aio.operations.ServiceOperations
    :param url: The URL of the service account or table that is the target of the desired
     operation. Required.
    :type url: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2019-02-02". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, url: str, **kwargs: Any
    ) -> None:
        _endpoint = "{url}"
        self._config = AzureTableConfiguration(url=url, **kwargs)
        self._client = AsyncPipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.table = TableOperations(self._client, self._config, self._serialize, self._deserialize)
        self.service = ServiceOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "url": self._serialize.url("self._config.url", self._config.url, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AzureTable":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
