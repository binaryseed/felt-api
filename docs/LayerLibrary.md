# LayerLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layer_groups** | [**List[LayerGroup]**](LayerGroup.md) |  | 
**layers** | [**List[Layer]**](Layer.md) |  | 
**type** | **str** |  | 

## Example

```python
from felt_api.models.layer_library import LayerLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of LayerLibrary from a JSON string
layer_library_instance = LayerLibrary.from_json(json)
# print the JSON string representation of the object
print(LayerLibrary.to_json())

# convert the object into a dict
layer_library_dict = layer_library_instance.to_dict()
# create an instance of LayerLibrary from a dict
layer_library_from_dict = LayerLibrary.from_dict(layer_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


