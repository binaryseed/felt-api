# SnowflakeConnection


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

## Example

```python
from felt_api.models.snowflake_connection import SnowflakeConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeConnection from a JSON string
snowflake_connection_instance = SnowflakeConnection.from_json(json)
# print the JSON string representation of the object
print(SnowflakeConnection.to_json())

# convert the object into a dict
snowflake_connection_dict = snowflake_connection_instance.to_dict()
# create an instance of SnowflakeConnection from a dict
snowflake_connection_from_dict = SnowflakeConnection.from_dict(snowflake_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


