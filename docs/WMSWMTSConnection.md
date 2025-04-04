# WMSWMTSConnection

Web Map Service / Web Map Tile Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from felt_api.models.wmswmts_connection import WMSWMTSConnection

# TODO update the JSON string below
json = "{}"
# create an instance of WMSWMTSConnection from a JSON string
wmswmts_connection_instance = WMSWMTSConnection.from_json(json)
# print the JSON string representation of the object
print(WMSWMTSConnection.to_json())

# convert the object into a dict
wmswmts_connection_dict = wmswmts_connection_instance.to_dict()
# create an instance of WMSWMTSConnection from a dict
wmswmts_connection_from_dict = WMSWMTSConnection.from_dict(wmswmts_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


