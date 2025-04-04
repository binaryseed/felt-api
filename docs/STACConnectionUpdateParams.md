# STACConnectionUpdateParams

SpatioTemporal Asset Catalogs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | STAC token | [optional] 
**type** | **str** |  | 
**url** | **str** | STAC server / asset URL | [optional] 

## Example

```python
from felt_api.models.stac_connection_update_params import STACConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of STACConnectionUpdateParams from a JSON string
stac_connection_update_params_instance = STACConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(STACConnectionUpdateParams.to_json())

# convert the object into a dict
stac_connection_update_params_dict = stac_connection_update_params_instance.to_dict()
# create an instance of STACConnectionUpdateParams from a dict
stac_connection_update_params_from_dict = STACConnectionUpdateParams.from_dict(stac_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


