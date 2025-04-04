# Source


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic_sync** | **str** |  | [optional] 
**connection** | [**SourceConnection**](SourceConnection.md) |  | [optional] 
**created_at** | **int** |  | [optional] 
**datasets** | [**List[SourceDataset]**](SourceDataset.md) |  | [optional] 
**id** | **str** |  | [optional] 
**last_synced_at** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**permissions** | [**SourcePermissions**](SourcePermissions.md) |  | [optional] 
**sync_status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from felt_api.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print(Source.to_json())

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_from_dict = Source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


