# AddSourceLayerParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | 
**var_from** | **str** |  | 
**query** | **str** |  | 
**source_id** | **str** |  | 
**stac_asset_url** | **str** |  | 

## Example

```python
from felt_api.models.add_source_layer_params import AddSourceLayerParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddSourceLayerParams from a JSON string
add_source_layer_params_instance = AddSourceLayerParams.from_json(json)
# print the JSON string representation of the object
print(AddSourceLayerParams.to_json())

# convert the object into a dict
add_source_layer_params_dict = add_source_layer_params_instance.to_dict()
# create an instance of AddSourceLayerParams from a dict
add_source_layer_params_from_dict = AddSourceLayerParams.from_dict(add_source_layer_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


