# PostgresConnection

Postgres / PostGIS

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
from felt_api.models.postgres_connection import PostgresConnection

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresConnection from a JSON string
postgres_connection_instance = PostgresConnection.from_json(json)
# print the JSON string representation of the object
print(PostgresConnection.to_json())

# convert the object into a dict
postgres_connection_dict = postgres_connection_instance.to_dict()
# create an instance of PostgresConnection from a dict
postgres_connection_from_dict = PostgresConnection.from_dict(postgres_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


