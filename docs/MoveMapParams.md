# MoveMapParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**folder_id** | **str** |  | 

## Example

```python
from felt_api.models.move_map_params import MoveMapParams

# TODO update the JSON string below
json = "{}"
# create an instance of MoveMapParams from a JSON string
move_map_params_instance = MoveMapParams.from_json(json)
# print the JSON string representation of the object
print(MoveMapParams.to_json())

# convert the object into a dict
move_map_params_dict = move_map_params_instance.to_dict()
# create an instance of MoveMapParams from a dict
move_map_params_from_dict = MoveMapParams.from_dict(move_map_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


