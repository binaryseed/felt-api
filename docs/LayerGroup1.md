# LayerGroup1


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
from felt_api.models.layer_group1 import LayerGroup1

# TODO update the JSON string below
json = "{}"
# create an instance of LayerGroup1 from a JSON string
layer_group1_instance = LayerGroup1.from_json(json)
# print the JSON string representation of the object
print(LayerGroup1.to_json())

# convert the object into a dict
layer_group1_dict = layer_group1_instance.to_dict()
# create an instance of LayerGroup1 from a dict
layer_group1_from_dict = LayerGroup1.from_dict(layer_group1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


