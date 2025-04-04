# SnowflakeConnectionCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Snowflake account ID | 
**database** | **str** | Snowflake database name | 
**password** | **str** | Snowflake password | 
**role** | **str** | Snowflake role | [optional] 
**var_schema** | **str** | Snowflake database schema | [optional] 
**type** | **str** |  | 
**user** | **str** | Snowflake user name | 
**warehouse** | **str** | Snowflake warehouse | [optional] 

## Example

```python
from felt_api.models.snowflake_connection_create_params import SnowflakeConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeConnectionCreateParams from a JSON string
snowflake_connection_create_params_instance = SnowflakeConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(SnowflakeConnectionCreateParams.to_json())

# convert the object into a dict
snowflake_connection_create_params_dict = snowflake_connection_create_params_instance.to_dict()
# create an instance of SnowflakeConnectionCreateParams from a dict
snowflake_connection_create_params_from_dict = SnowflakeConnectionCreateParams.from_dict(snowflake_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


