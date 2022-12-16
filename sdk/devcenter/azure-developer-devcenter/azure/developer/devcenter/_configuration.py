# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from ._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class DevCenterClientConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for DevCenterClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param tenant_id: The tenant to operate on. Required.
    :type tenant_id: str
    :param dev_center: The DevCenter to operate on. Required.
    :type dev_center: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param dev_center_dns_suffix: The DNS suffix used as the base for all devcenter requests.
     Default value is "devcenter.azure.com".
    :type dev_center_dns_suffix: str
    :keyword api_version: Api Version. Default value is "2022-03-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        tenant_id: str,
        dev_center: str,
        credential: "TokenCredential",
        dev_center_dns_suffix: str = "devcenter.azure.com",
        **kwargs: Any
    ) -> None:
        super(DevCenterClientConfiguration, self).__init__(**kwargs)
        api_version = kwargs.pop("api_version", "2022-03-01-preview")  # type: str

        if tenant_id is None:
            raise ValueError("Parameter 'tenant_id' must not be None.")
        if dev_center is None:
            raise ValueError("Parameter 'dev_center' must not be None.")
        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if dev_center_dns_suffix is None:
            raise ValueError("Parameter 'dev_center_dns_suffix' must not be None.")

        self.tenant_id = tenant_id
        self.dev_center = dev_center
        self.credential = credential
        self.dev_center_dns_suffix = dev_center_dns_suffix
        self.api_version = api_version
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://devcenter.azure.com/.default"])
        kwargs.setdefault("sdk_moniker", "developer-devcenter/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = policies.BearerTokenCredentialPolicy(
                self.credential, *self.credential_scopes, **kwargs
            )
