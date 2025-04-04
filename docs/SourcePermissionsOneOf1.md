# SourcePermissionsOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[ProjectReference]**](ProjectReference.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from felt_api.models.source_permissions_one_of1 import SourcePermissionsOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of SourcePermissionsOneOf1 from a JSON string
source_permissions_one_of1_instance = SourcePermissionsOneOf1.from_json(json)
# print the JSON string representation of the object
print(SourcePermissionsOneOf1.to_json())

# convert the object into a dict
source_permissions_one_of1_dict = source_permissions_one_of1_instance.to_dict()
# create an instance of SourcePermissionsOneOf1 from a dict
source_permissions_one_of1_from_dict = SourcePermissionsOneOf1.from_dict(source_permissions_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


