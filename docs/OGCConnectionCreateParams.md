# OGCConnectionCreateParams

Open Geospatial Consortium

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | OGC token | [optional] 
**type** | **str** |  | 
**url** | **str** | OGC URL | 

## Example

```python
from felt_api.models.ogc_connection_create_params import OGCConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of OGCConnectionCreateParams from a JSON string
ogc_connection_create_params_instance = OGCConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(OGCConnectionCreateParams.to_json())

# convert the object into a dict
ogc_connection_create_params_dict = ogc_connection_create_params_instance.to_dict()
# create an instance of OGCConnectionCreateParams from a dict
ogc_connection_create_params_from_dict = OGCConnectionCreateParams.from_dict(ogc_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


