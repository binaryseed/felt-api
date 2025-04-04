# LayerGroup2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | 
**id** | **str** |  | 
**layers** | [**List[Layer2]**](Layer2.md) |  | 
**links** | [**LayerGroup2Links**](LayerGroup2Links.md) |  | [optional] 
**name** | **str** |  | 
**ordering_key** | **int** | A sort order key used for ordering layers and layer groups in the legend | [optional] 
**subtitle** | **str** | Deprecated: use &#x60;caption&#x60; instead. | [optional] 
**type** | **str** |  | 

## Example

```python
from felt_api.models.layer_group2 import LayerGroup2

# TODO update the JSON string below
json = "{}"
# create an instance of LayerGroup2 from a JSON string
layer_group2_instance = LayerGroup2.from_json(json)
# print the JSON string representation of the object
print(LayerGroup2.to_json())

# convert the object into a dict
layer_group2_dict = layer_group2_instance.to_dict()
# create an instance of LayerGroup2 from a dict
layer_group2_from_dict = LayerGroup2.from_dict(layer_group2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


