# AddSourceLayerSTACParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**source_id** | **str** |  | 
**stac_asset_url** | **str** |  | 

## Example

```python
from felt_api.models.add_source_layer_stac_params import AddSourceLayerSTACParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddSourceLayerSTACParams from a JSON string
add_source_layer_stac_params_instance = AddSourceLayerSTACParams.from_json(json)
# print the JSON string representation of the object
print(AddSourceLayerSTACParams.to_json())

# convert the object into a dict
add_source_layer_stac_params_dict = add_source_layer_stac_params_instance.to_dict()
# create an instance of AddSourceLayerSTACParams from a dict
add_source_layer_stac_params_from_dict = AddSourceLayerSTACParams.from_dict(add_source_layer_stac_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


