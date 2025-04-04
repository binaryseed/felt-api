# SourceDataset

A Dataset found when inspecting a Source, e.g. a database table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**geometry_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**inspection_status** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **int** |  | [optional] 

## Example

```python
from felt_api.models.source_dataset import SourceDataset

# TODO update the JSON string below
json = "{}"
# create an instance of SourceDataset from a JSON string
source_dataset_instance = SourceDataset.from_json(json)
# print the JSON string representation of the object
print(SourceDataset.to_json())

# convert the object into a dict
source_dataset_dict = source_dataset_instance.to_dict()
# create an instance of SourceDataset from a dict
source_dataset_from_dict = SourceDataset.from_dict(source_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


