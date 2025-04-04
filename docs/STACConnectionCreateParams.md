# STACConnectionCreateParams

SpatioTemporal Asset Catalogs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | STAC token | [optional] 
**type** | **str** |  | 
**url** | **str** | STAC server / asset URL | 

## Example

```python
from felt_api.models.stac_connection_create_params import STACConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of STACConnectionCreateParams from a JSON string
stac_connection_create_params_instance = STACConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(STACConnectionCreateParams.to_json())

# convert the object into a dict
stac_connection_create_params_dict = stac_connection_create_params_instance.to_dict()
# create an instance of STACConnectionCreateParams from a dict
stac_connection_create_params_from_dict = STACConnectionCreateParams.from_dict(stac_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


