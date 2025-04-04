# ProjectUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to be used for the Project | [optional] 
**visibility** | **str** | Either viewable by all members of the workspace, or private to users who are invited. | [optional] 

## Example

```python
from felt_api.models.project_update_params import ProjectUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUpdateParams from a JSON string
project_update_params_instance = ProjectUpdateParams.from_json(json)
# print the JSON string representation of the object
print(ProjectUpdateParams.to_json())

# convert the object into a dict
project_update_params_dict = project_update_params_instance.to_dict()
# create an instance of ProjectUpdateParams from a dict
project_update_params_from_dict = ProjectUpdateParams.from_dict(project_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


