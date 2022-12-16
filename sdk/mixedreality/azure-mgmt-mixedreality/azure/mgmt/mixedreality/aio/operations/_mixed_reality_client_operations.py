# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._mixed_reality_client_operations import build_check_name_availability_local_request
from .._vendor import MixedRealityClientMixinABC

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MixedRealityClientOperationsMixin(MixedRealityClientMixinABC):
    @overload
    async def check_name_availability_local(
        self,
        location: str,
        check_name_availability: _models.CheckNameAvailabilityRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Check Name Availability for local uniqueness.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability: Check Name Availability Request. Required.
        :type check_name_availability: ~azure.mgmt.mixedreality.models.CheckNameAvailabilityRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResponse or the result of cls(response)
        :rtype: ~azure.mgmt.mixedreality.models.CheckNameAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def check_name_availability_local(
        self, location: str, check_name_availability: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Check Name Availability for local uniqueness.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability: Check Name Availability Request. Required.
        :type check_name_availability: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResponse or the result of cls(response)
        :rtype: ~azure.mgmt.mixedreality.models.CheckNameAvailabilityResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def check_name_availability_local(
        self, location: str, check_name_availability: Union[_models.CheckNameAvailabilityRequest, IO], **kwargs: Any
    ) -> _models.CheckNameAvailabilityResponse:
        """Check Name Availability for local uniqueness.

        :param location: The location in which uniqueness will be verified. Required.
        :type location: str
        :param check_name_availability: Check Name Availability Request. Is either a model type or a IO
         type. Required.
        :type check_name_availability: ~azure.mgmt.mixedreality.models.CheckNameAvailabilityRequest or
         IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameAvailabilityResponse or the result of cls(response)
        :rtype: ~azure.mgmt.mixedreality.models.CheckNameAvailabilityResponse
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

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2021-03-01-preview"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.CheckNameAvailabilityResponse]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(check_name_availability, (IO, bytes)):
            _content = check_name_availability
        else:
            _json = self._serialize.body(check_name_availability, "CheckNameAvailabilityRequest")

        request = build_check_name_availability_local_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_name_availability_local.metadata["url"],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameAvailabilityResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability_local.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/locations/{location}/checkNameAvailability"}  # type: ignore
