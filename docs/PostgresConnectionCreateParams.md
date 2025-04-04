# PostgresConnectionCreateParams

Postgres / PostGIS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** | Postgres database name | 
**host** | **str** | Postgres host | 
**password** | **str** | Postgres password | 
**port** | **int** | Postgres port | [optional] 
**type** | **str** |  | 
**user** | **str** | Postgres user name | 

## Example

```python
from felt_api.models.postgres_connection_create_params import PostgresConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresConnectionCreateParams from a JSON string
postgres_connection_create_params_instance = PostgresConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(PostgresConnectionCreateParams.to_json())

# convert the object into a dict
postgres_connection_create_params_dict = postgres_connection_create_params_instance.to_dict()
# create an instance of PostgresConnectionCreateParams from a dict
postgres_connection_create_params_from_dict = PostgresConnectionCreateParams.from_dict(postgres_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


