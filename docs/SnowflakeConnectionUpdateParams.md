# SnowflakeConnectionUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Snowflake account ID | [optional] 
**database** | **str** | Snowflake database name | [optional] 
**password** | **str** | Snowflake password | [optional] 
**role** | **str** | Snowflake role | [optional] 
**var_schema** | **str** | Snowflake database schema | [optional] 
**type** | **str** |  | 
**user** | **str** | Snowflake user name | [optional] 
**warehouse** | **str** | Snowflake warehouse | [optional] 

## Example

```python
from felt_api.models.snowflake_connection_update_params import SnowflakeConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeConnectionUpdateParams from a JSON string
snowflake_connection_update_params_instance = SnowflakeConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(SnowflakeConnectionUpdateParams.to_json())

# convert the object into a dict
snowflake_connection_update_params_dict = snowflake_connection_update_params_instance.to_dict()
# create an instance of SnowflakeConnectionUpdateParams from a dict
snowflake_connection_update_params_from_dict = SnowflakeConnectionUpdateParams.from_dict(snowflake_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


