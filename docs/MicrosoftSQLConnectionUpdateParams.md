# MicrosoftSQLConnectionUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** | MSSQL database name | [optional] 
**host** | **str** | MSSQL host | [optional] 
**password** | **str** | MSSQL password | [optional] 
**port** | **int** | MSSQL port | [optional] 
**type** | **str** |  | 
**user** | **str** | MSSQL user name | [optional] 

## Example

```python
from felt_api.models.microsoft_sql_connection_update_params import MicrosoftSQLConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftSQLConnectionUpdateParams from a JSON string
microsoft_sql_connection_update_params_instance = MicrosoftSQLConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(MicrosoftSQLConnectionUpdateParams.to_json())

# convert the object into a dict
microsoft_sql_connection_update_params_dict = microsoft_sql_connection_update_params_instance.to_dict()
# create an instance of MicrosoftSQLConnectionUpdateParams from a dict
microsoft_sql_connection_update_params_from_dict = MicrosoftSQLConnectionUpdateParams.from_dict(microsoft_sql_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


