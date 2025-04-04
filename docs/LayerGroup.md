# LayerGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | 
**id** | **str** |  | 
**layers** | [**List[Layer1]**](Layer1.md) |  | 
**links** | [**LayerGroup1Links**](LayerGroup1Links.md) |  | [optional] 
**name** | **str** |  | 
**ordering_key** | **int** | A sort order key used for ordering layers and layer groups in the legend | [optional] 
**subtitle** | **str** | Deprecated: use &#x60;caption&#x60; instead. | [optional] 
**type** | **str** |  | 

## Example

```python
from felt_api.models.layer_group import LayerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LayerGroup from a JSON string
layer_group_instance = LayerGroup.from_json(json)
# print the JSON string representation of the object
print(LayerGroup.to_json())

# convert the object into a dict
layer_group_dict = layer_group_instance.to_dict()
# create an instance of LayerGroup from a dict
layer_group_from_dict = LayerGroup.from_dict(layer_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


