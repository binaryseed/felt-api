# OGCConnectionUpdateParams

Open Geospatial Consortium

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | OGC token | [optional] 
**type** | **str** |  | 
**url** | **str** | OGC URL | [optional] 

## Example

```python
from felt_api.models.ogc_connection_update_params import OGCConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of OGCConnectionUpdateParams from a JSON string
ogc_connection_update_params_instance = OGCConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(OGCConnectionUpdateParams.to_json())

# convert the object into a dict
ogc_connection_update_params_dict = ogc_connection_update_params_instance.to_dict()
# create an instance of OGCConnectionUpdateParams from a dict
ogc_connection_update_params_from_dict = OGCConnectionUpdateParams.from_dict(ogc_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


