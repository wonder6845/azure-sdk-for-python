# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    resource_group_name: str,
    search_service_name: str,
    subscription_id: str,
    *,
    client_request_id: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-03-13"))  # type: Literal["2020-03-13"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/listAdminKeys",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "searchServiceName": _SERIALIZER.url("search_service_name", search_service_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_regenerate_request(
    resource_group_name: str,
    search_service_name: str,
    key_kind: Union[str, _models.AdminKeyKind],
    subscription_id: str,
    *,
    client_request_id: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-03-13"))  # type: Literal["2020-03-13"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/regenerateAdminKey/{keyKind}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "searchServiceName": _SERIALIZER.url("search_service_name", search_service_name, "str"),
        "keyKind": _SERIALIZER.url("key_kind", key_kind, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if client_request_id is not None:
        _headers["x-ms-client-request-id"] = _SERIALIZER.header("client_request_id", client_request_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class AdminKeysOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.search.SearchManagementClient`'s
        :attr:`admin_keys` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        search_service_name: str,
        search_management_request_options: Optional[_models.SearchManagementRequestOptions] = None,
        **kwargs: Any
    ) -> _models.AdminKeyResult:
        """Gets the primary and secondary admin API keys for the specified Azure Cognitive Search service.

        :param resource_group_name: The name of the resource group within the current subscription. You
         can obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Cognitive Search service associated with the
         specified resource group. Required.
        :type search_service_name: str
        :param search_management_request_options: Parameter group. Default value is None.
        :type search_management_request_options:
         ~azure.mgmt.search.models.SearchManagementRequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdminKeyResult or the result of cls(response)
        :rtype: ~azure.mgmt.search.models.AdminKeyResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-03-13"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AdminKeyResult]

        _client_request_id = None
        if search_management_request_options is not None:
            _client_request_id = search_management_request_options.client_request_id

        request = build_get_request(
            resource_group_name=resource_group_name,
            search_service_name=search_service_name,
            subscription_id=self._config.subscription_id,
            client_request_id=_client_request_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdminKeyResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/listAdminKeys"}  # type: ignore

    @distributed_trace
    def regenerate(
        self,
        resource_group_name: str,
        search_service_name: str,
        key_kind: Union[str, _models.AdminKeyKind],
        search_management_request_options: Optional[_models.SearchManagementRequestOptions] = None,
        **kwargs: Any
    ) -> _models.AdminKeyResult:
        """Regenerates either the primary or secondary admin API key. You can only regenerate one key at a
        time.

        :param resource_group_name: The name of the resource group within the current subscription. You
         can obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param search_service_name: The name of the Azure Cognitive Search service associated with the
         specified resource group. Required.
        :type search_service_name: str
        :param key_kind: Specifies which key to regenerate. Valid values include 'primary' and
         'secondary'. Known values are: "primary" and "secondary". Required.
        :type key_kind: str or ~azure.mgmt.search.models.AdminKeyKind
        :param search_management_request_options: Parameter group. Default value is None.
        :type search_management_request_options:
         ~azure.mgmt.search.models.SearchManagementRequestOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AdminKeyResult or the result of cls(response)
        :rtype: ~azure.mgmt.search.models.AdminKeyResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2020-03-13"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.AdminKeyResult]

        _client_request_id = None
        if search_management_request_options is not None:
            _client_request_id = search_management_request_options.client_request_id

        request = build_regenerate_request(
            resource_group_name=resource_group_name,
            search_service_name=search_service_name,
            key_kind=key_kind,
            subscription_id=self._config.subscription_id,
            client_request_id=_client_request_id,
            api_version=api_version,
            template_url=self.regenerate.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AdminKeyResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    regenerate.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Search/searchServices/{searchServiceName}/regenerateAdminKey/{keyKind}"}  # type: ignore
