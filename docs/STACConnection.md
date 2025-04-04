# STACConnection

SpatioTemporal Asset Catalogs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from felt_api.models.stac_connection import STACConnection

# TODO update the JSON string below
json = "{}"
# create an instance of STACConnection from a JSON string
stac_connection_instance = STACConnection.from_json(json)
# print the JSON string representation of the object
print(STACConnection.to_json())

# convert the object into a dict
stac_connection_dict = stac_connection_instance.to_dict()
# create an instance of STACConnection from a dict
stac_connection_from_dict = STACConnection.from_dict(stac_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


