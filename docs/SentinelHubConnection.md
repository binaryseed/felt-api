# SentinelHubConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from felt_api.models.sentinel_hub_connection import SentinelHubConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SentinelHubConnection from a JSON string
sentinel_hub_connection_instance = SentinelHubConnection.from_json(json)
# print the JSON string representation of the object
print(SentinelHubConnection.to_json())

# convert the object into a dict
sentinel_hub_connection_dict = sentinel_hub_connection_instance.to_dict()
# create an instance of SentinelHubConnection from a dict
sentinel_hub_connection_from_dict = SentinelHubConnection.from_dict(sentinel_hub_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


