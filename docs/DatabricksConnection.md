# DatabricksConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **str** |  | [optional] 
**http_path** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**server_hostname** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from felt_api.models.databricks_connection import DatabricksConnection

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksConnection from a JSON string
databricks_connection_instance = DatabricksConnection.from_json(json)
# print the JSON string representation of the object
print(DatabricksConnection.to_json())

# convert the object into a dict
databricks_connection_dict = databricks_connection_instance.to_dict()
# create an instance of DatabricksConnection from a dict
databricks_connection_from_dict = DatabricksConnection.from_dict(databricks_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


