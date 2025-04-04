# SourceCreateParamsPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**project_ids** | **List[str]** |  | 

## Example

```python
from felt_api.models.source_create_params_permissions import SourceCreateParamsPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCreateParamsPermissions from a JSON string
source_create_params_permissions_instance = SourceCreateParamsPermissions.from_json(json)
# print the JSON string representation of the object
print(SourceCreateParamsPermissions.to_json())

# convert the object into a dict
source_create_params_permissions_dict = source_create_params_permissions_instance.to_dict()
# create an instance of SourceCreateParamsPermissions from a dict
source_create_params_permissions_from_dict = SourceCreateParamsPermissions.from_dict(source_create_params_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


