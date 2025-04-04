# DuplicateLayersParamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_map_id** | **str** |  | 
**source_layer_id** | **str** |  | 
**source_layer_group_id** | **str** |  | 

## Example

```python
from felt_api.models.duplicate_layers_params_inner import DuplicateLayersParamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateLayersParamsInner from a JSON string
duplicate_layers_params_inner_instance = DuplicateLayersParamsInner.from_json(json)
# print the JSON string representation of the object
print(DuplicateLayersParamsInner.to_json())

# convert the object into a dict
duplicate_layers_params_inner_dict = duplicate_layers_params_inner_instance.to_dict()
# create an instance of DuplicateLayersParamsInner from a dict
duplicate_layers_params_inner_from_dict = DuplicateLayersParamsInner.from_dict(duplicate_layers_params_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


