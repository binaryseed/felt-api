# AddSourceLayerDatasetParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_id** | **str** |  | 
**var_from** | **str** |  | 

## Example

```python
from felt_api.models.add_source_layer_dataset_params import AddSourceLayerDatasetParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddSourceLayerDatasetParams from a JSON string
add_source_layer_dataset_params_instance = AddSourceLayerDatasetParams.from_json(json)
# print the JSON string representation of the object
print(AddSourceLayerDatasetParams.to_json())

# convert the object into a dict
add_source_layer_dataset_params_dict = add_source_layer_dataset_params_instance.to_dict()
# create an instance of AddSourceLayerDatasetParams from a dict
add_source_layer_dataset_params_from_dict = AddSourceLayerDatasetParams.from_dict(add_source_layer_dataset_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


