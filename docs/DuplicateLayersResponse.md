# DuplicateLayersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layer_groups** | [**List[LayerGroup2]**](LayerGroup2.md) |  | 
**layers** | [**List[Layer2]**](Layer2.md) |  | 

## Example

```python
from felt_api.models.duplicate_layers_response import DuplicateLayersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateLayersResponse from a JSON string
duplicate_layers_response_instance = DuplicateLayersResponse.from_json(json)
# print the JSON string representation of the object
print(DuplicateLayersResponse.to_json())

# convert the object into a dict
duplicate_layers_response_dict = duplicate_layers_response_instance.to_dict()
# create an instance of DuplicateLayersResponse from a dict
duplicate_layers_response_from_dict = DuplicateLayersResponse.from_dict(duplicate_layers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


