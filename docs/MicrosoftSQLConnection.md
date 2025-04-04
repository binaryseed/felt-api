# MicrosoftSQLConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from felt_api.models.microsoft_sql_connection import MicrosoftSQLConnection

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftSQLConnection from a JSON string
microsoft_sql_connection_instance = MicrosoftSQLConnection.from_json(json)
# print the JSON string representation of the object
print(MicrosoftSQLConnection.to_json())

# convert the object into a dict
microsoft_sql_connection_dict = microsoft_sql_connection_instance.to_dict()
# create an instance of MicrosoftSQLConnection from a dict
microsoft_sql_connection_from_dict = MicrosoftSQLConnection.from_dict(microsoft_sql_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


