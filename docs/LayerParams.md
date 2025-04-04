# LayerParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional] [default to 'not_provided']
**id** | **str** |  | 
**layer_group_id** | **str** |  | [optional] [default to 'not_provided']
**metadata** | [**LayerMetadata**](LayerMetadata.md) |  | [optional] 
**name** | **str** |  | [optional] [default to 'not_provided']
**ordering_key** | **int** |  | [optional] 
**refresh_period** | **str** |  | [optional] 
**subtitle** | **str** | Deprecated: use &#x60;caption&#x60; instead. | [optional] 

## Example

```python
from felt_api.models.layer_params import LayerParams

# TODO update the JSON string below
json = "{}"
# create an instance of LayerParams from a JSON string
layer_params_instance = LayerParams.from_json(json)
# print the JSON string representation of the object
print(LayerParams.to_json())

# convert the object into a dict
layer_params_dict = layer_params_instance.to_dict()
# create an instance of LayerParams from a dict
layer_params_from_dict = LayerParams.from_dict(layer_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


