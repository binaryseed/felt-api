# SourcePermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**projects** | [**List[ProjectReference]**](ProjectReference.md) |  | [optional] 

## Example

```python
from felt_api.models.source_permissions import SourcePermissions

# TODO update the JSON string below
json = "{}"
# create an instance of SourcePermissions from a JSON string
source_permissions_instance = SourcePermissions.from_json(json)
# print the JSON string representation of the object
print(SourcePermissions.to_json())

# convert the object into a dict
source_permissions_dict = source_permissions_instance.to_dict()
# create an instance of SourcePermissions from a dict
source_permissions_from_dict = SourcePermissions.from_dict(source_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


