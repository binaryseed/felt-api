# WFSConnection

Web Feature Server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from felt_api.models.wfs_connection import WFSConnection

# TODO update the JSON string below
json = "{}"
# create an instance of WFSConnection from a JSON string
wfs_connection_instance = WFSConnection.from_json(json)
# print the JSON string representation of the object
print(WFSConnection.to_json())

# convert the object into a dict
wfs_connection_dict = wfs_connection_instance.to_dict()
# create an instance of WFSConnection from a dict
wfs_connection_from_dict = WFSConnection.from_dict(wfs_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


