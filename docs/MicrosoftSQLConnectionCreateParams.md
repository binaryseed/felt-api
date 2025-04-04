# MicrosoftSQLConnectionCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** | MSSQL database name | 
**host** | **str** | MSSQL host | 
**password** | **str** | MSSQL password | 
**port** | **int** | MSSQL port | [optional] 
**type** | **str** |  | 
**user** | **str** | MSSQL user name | 

## Example

```python
from felt_api.models.microsoft_sql_connection_create_params import MicrosoftSQLConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftSQLConnectionCreateParams from a JSON string
microsoft_sql_connection_create_params_instance = MicrosoftSQLConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(MicrosoftSQLConnectionCreateParams.to_json())

# convert the object into a dict
microsoft_sql_connection_create_params_dict = microsoft_sql_connection_create_params_instance.to_dict()
# create an instance of MicrosoftSQLConnectionCreateParams from a dict
microsoft_sql_connection_create_params_from_dict = MicrosoftSQLConnectionCreateParams.from_dict(microsoft_sql_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


