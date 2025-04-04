# PostgresConnectionUpdateParams

Postgres / PostGIS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** | Postgres database name | [optional] 
**host** | **str** | Postgres host | [optional] 
**password** | **str** | Postgres password | [optional] 
**port** | **int** | Postgres port | [optional] 
**type** | **str** |  | 
**user** | **str** | Postgres user name | [optional] 

## Example

```python
from felt_api.models.postgres_connection_update_params import PostgresConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresConnectionUpdateParams from a JSON string
postgres_connection_update_params_instance = PostgresConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(PostgresConnectionUpdateParams.to_json())

# convert the object into a dict
postgres_connection_update_params_dict = postgres_connection_update_params_instance.to_dict()
# create an instance of PostgresConnectionUpdateParams from a dict
postgres_connection_update_params_from_dict = PostgresConnectionUpdateParams.from_dict(postgres_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


