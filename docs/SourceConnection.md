# SourceConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**warehouse** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**dataset** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**catalog** | **str** |  | [optional] 
**http_path** | **str** |  | [optional] 
**server_hostname** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from felt_api.models.source_connection import SourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SourceConnection from a JSON string
source_connection_instance = SourceConnection.from_json(json)
# print the JSON string representation of the object
print(SourceConnection.to_json())

# convert the object into a dict
source_connection_dict = source_connection_instance.to_dict()
# create an instance of SourceConnection from a dict
source_connection_from_dict = SourceConnection.from_dict(source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


