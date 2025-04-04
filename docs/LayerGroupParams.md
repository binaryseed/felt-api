# LayerGroupParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional] [default to 'not_provided']
**id** | **str** |  | [optional] [default to 'not_provided']
**name** | **str** |  | 
**ordering_key** | **int** |  | [optional] 
**subtitle** | **str** | Deprecated: use &#x60;caption&#x60; instead. | [optional] 

## Example

```python
from felt_api.models.layer_group_params import LayerGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of LayerGroupParams from a JSON string
layer_group_params_instance = LayerGroupParams.from_json(json)
# print the JSON string representation of the object
print(LayerGroupParams.to_json())

# convert the object into a dict
layer_group_params_dict = layer_group_params_instance.to_dict()
# create an instance of LayerGroupParams from a dict
layer_group_params_from_dict = LayerGroupParams.from_dict(layer_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


