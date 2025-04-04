# OGCConnection

Open Geospatial Consortium

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from felt_api.models.ogc_connection import OGCConnection

# TODO update the JSON string below
json = "{}"
# create an instance of OGCConnection from a JSON string
ogc_connection_instance = OGCConnection.from_json(json)
# print the JSON string representation of the object
print(OGCConnection.to_json())

# convert the object into a dict
ogc_connection_dict = ogc_connection_instance.to_dict()
# create an instance of OGCConnection from a dict
ogc_connection_from_dict = OGCConnection.from_dict(ogc_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


