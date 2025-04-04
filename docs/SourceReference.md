# SourceReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic_sync** | **str** |  | [optional] 
**connection_type** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**last_synced_at** | **int** |  | [optional] 
**links** | [**SourceReferenceLinks**](SourceReferenceLinks.md) |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**permissions** | [**SourcePermissions**](SourcePermissions.md) |  | [optional] 
**sync_status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from felt_api.models.source_reference import SourceReference

# TODO update the JSON string below
json = "{}"
# create an instance of SourceReference from a JSON string
source_reference_instance = SourceReference.from_json(json)
# print the JSON string representation of the object
print(SourceReference.to_json())

# convert the object into a dict
source_reference_dict = source_reference_instance.to_dict()
# create an instance of SourceReference from a dict
source_reference_from_dict = SourceReference.from_dict(source_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


