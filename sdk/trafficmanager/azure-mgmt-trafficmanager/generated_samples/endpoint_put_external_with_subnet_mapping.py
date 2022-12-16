# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.trafficmanager import TrafficManagerManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-trafficmanager
# USAGE
    python endpoint_put_external_with_subnet_mapping.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = TrafficManagerManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.endpoints.create_or_update(
        resource_group_name="azuresdkfornetautoresttrafficmanager2191",
        profile_name="azuresdkfornetautoresttrafficmanager8224",
        endpoint_type="ExternalEndpoints",
        endpoint_name="My%20external%20endpoint",
        parameters={
            "name": "My external endpoint",
            "properties": {
                "endpointStatus": "Enabled",
                "subnets": [{"first": "1.2.3.0", "scope": 24}, {"first": "25.26.27.28", "last": "29.30.31.32"}],
                "target": "foobar.contoso.com",
            },
            "type": "Microsoft.network/TrafficManagerProfiles/ExternalEndpoints",
        },
    )
    print(response)


# x-ms-original-file: specification/trafficmanager/resource-manager/Microsoft.Network/preview/2022-04-01-preview/examples/Endpoint-PUT-External-WithSubnetMapping.json
if __name__ == "__main__":
    main()
