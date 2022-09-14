# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from ...operations._content_key_policies_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_policy_properties_with_secrets_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ContentKeyPoliciesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.media.aio.AzureMediaServices`'s
        :attr:`content_key_policies` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        account_name: str,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.ContentKeyPolicy"]:
        """List Content Key Policies.

        Lists the Content Key Policies in the account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param filter: Restricts the set of items returned. Default value is None.
        :type filter: str
        :param top: Specifies a non-negative integer n that limits the number of items returned from a
         collection. The service returns the number of available items up to but not greater than the
         specified value n. Default value is None.
        :type top: int
        :param orderby: Specifies the key by which the result collection should be ordered. Default
         value is None.
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ContentKeyPolicy or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.media.models.ContentKeyPolicy]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ContentKeyPolicyCollection]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    top=top,
                    orderby=orderby,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ContentKeyPolicyCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies"}  # type: ignore

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, account_name: str, content_key_policy_name: str, **kwargs: Any
    ) -> _models.ContentKeyPolicy:
        """Get a Content Key Policy.

        Get the details of a Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentKeyPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ContentKeyPolicy]

        request = build_get_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            content_key_policy_name=content_key_policy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ContentKeyPolicy", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}"}  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        account_name: str,
        content_key_policy_name: str,
        parameters: _models.ContentKeyPolicy,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ContentKeyPolicy:
        """Create or update an Content Key Policy.

        Create or update a Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :param parameters: The request parameters. Required.
        :type parameters: ~azure.mgmt.media.models.ContentKeyPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentKeyPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        account_name: str,
        content_key_policy_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ContentKeyPolicy:
        """Create or update an Content Key Policy.

        Create or update a Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :param parameters: The request parameters. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentKeyPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        account_name: str,
        content_key_policy_name: str,
        parameters: Union[_models.ContentKeyPolicy, IO],
        **kwargs: Any
    ) -> _models.ContentKeyPolicy:
        """Create or update an Content Key Policy.

        Create or update a Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :param parameters: The request parameters. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.media.models.ContentKeyPolicy or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentKeyPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ContentKeyPolicy]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ContentKeyPolicy")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            content_key_policy_name=content_key_policy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ContentKeyPolicy", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("ContentKeyPolicy", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}"}  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, account_name: str, content_key_policy_name: str, **kwargs: Any
    ) -> None:
        """Delete a Content Key Policy.

        Deletes a Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            content_key_policy_name=content_key_policy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}"}  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        content_key_policy_name: str,
        parameters: _models.ContentKeyPolicy,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ContentKeyPolicy:
        """Update a Content Key Policy.

        Updates an existing Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :param parameters: The request parameters. Required.
        :type parameters: ~azure.mgmt.media.models.ContentKeyPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentKeyPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        content_key_policy_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ContentKeyPolicy:
        """Update a Content Key Policy.

        Updates an existing Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :param parameters: The request parameters. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentKeyPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        content_key_policy_name: str,
        parameters: Union[_models.ContentKeyPolicy, IO],
        **kwargs: Any
    ) -> _models.ContentKeyPolicy:
        """Update a Content Key Policy.

        Updates an existing Content Key Policy in the Media Services account.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :param parameters: The request parameters. Is either a model type or a IO type. Required.
        :type parameters: ~azure.mgmt.media.models.ContentKeyPolicy or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentKeyPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicy
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ContentKeyPolicy]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ContentKeyPolicy")

        request = build_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            content_key_policy_name=content_key_policy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ContentKeyPolicy", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}"}  # type: ignore

    @distributed_trace_async
    async def get_policy_properties_with_secrets(
        self, resource_group_name: str, account_name: str, content_key_policy_name: str, **kwargs: Any
    ) -> _models.ContentKeyPolicyProperties:
        """Get a Content Key Policy with secrets.

        Get a Content Key Policy including secret values.

        :param resource_group_name: The name of the resource group within the Azure subscription.
         Required.
        :type resource_group_name: str
        :param account_name: The Media Services account name. Required.
        :type account_name: str
        :param content_key_policy_name: The Content Key Policy name. Required.
        :type content_key_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ContentKeyPolicyProperties or the result of cls(response)
        :rtype: ~azure.mgmt.media.models.ContentKeyPolicyProperties
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ContentKeyPolicyProperties]

        request = build_get_policy_properties_with_secrets_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            content_key_policy_name=content_key_policy_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_policy_properties_with_secrets.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ContentKeyPolicyProperties", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_policy_properties_with_secrets.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}/getPolicyPropertiesWithSecrets"}  # type: ignore
