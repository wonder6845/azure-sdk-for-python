# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._afd_profiles_operations import (
    build_check_host_name_availability_request,
    build_list_resource_usage_request,
)
from .._vendor import MixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AFDProfilesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.cdn.aio.CdnManagementClient`'s
        :attr:`afd_profiles` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_resource_usage(
        self, resource_group_name: str, profile_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.Usage"]:
        """Checks the quota and actual usage of AzureFrontDoor endpoints under the given CDN profile.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium or CDN
         profile which is unique within the resource group. Required.
        :type profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Usage or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.cdn.models.Usage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.UsagesListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_resource_usage_request(
                    resource_group_name=resource_group_name,
                    profile_name=profile_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_resource_usage.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("UsagesListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.AfdErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_resource_usage.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/usages"}  # type: ignore

    @overload
    async def check_host_name_availability(
        self,
        resource_group_name: str,
        profile_name: str,
        check_host_name_availability_input: _models.CheckHostNameAvailabilityInput,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the name availability of a host name.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium or CDN
         profile which is unique within the resource group. Required.
        :type profile_name: str
        :param check_host_name_availability_input: Custom domain to be validated. Required.
        :type check_host_name_availability_input: ~azure.mgmt.cdn.models.CheckHostNameAvailabilityInput
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def check_host_name_availability(
        self,
        resource_group_name: str,
        profile_name: str,
        check_host_name_availability_input: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the name availability of a host name.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium or CDN
         profile which is unique within the resource group. Required.
        :type profile_name: str
        :param check_host_name_availability_input: Custom domain to be validated. Required.
        :type check_host_name_availability_input: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def check_host_name_availability(
        self,
        resource_group_name: str,
        profile_name: str,
        check_host_name_availability_input: Union[_models.CheckHostNameAvailabilityInput, IO],
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityOutput:
        """Check the name availability of a host name.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium or CDN
         profile which is unique within the resource group. Required.
        :type profile_name: str
        :param check_host_name_availability_input: Custom domain to be validated. Is either a model
         type or a IO type. Required.
        :type check_host_name_availability_input: ~azure.mgmt.cdn.models.CheckHostNameAvailabilityInput
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityOutput or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.CheckNameAvailabilityOutput
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CheckNameAvailabilityOutput]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_host_name_availability_input, (IO, bytes)):
            _content = check_host_name_availability_input
        else:
            _json = self._serialize.body(check_host_name_availability_input, "CheckHostNameAvailabilityInput")

        request = build_check_host_name_availability_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_host_name_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AfdErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameAvailabilityOutput", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_host_name_availability.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/checkHostNameAvailability"}  # type: ignore
