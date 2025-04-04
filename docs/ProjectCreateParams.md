# ProjectCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to be used for the Project | 
**visibility** | **str** | Either viewable by all members of the workspace, or private to users who are invited. | 

## Example

```python
from felt_api.models.project_create_params import ProjectCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCreateParams from a JSON string
project_create_params_instance = ProjectCreateParams.from_json(json)
# print the JSON string representation of the object
print(ProjectCreateParams.to_json())

# convert the object into a dict
project_create_params_dict = project_create_params_instance.to_dict()
# create an instance of ProjectCreateParams from a dict
project_create_params_from_dict = ProjectCreateParams.from_dict(project_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


