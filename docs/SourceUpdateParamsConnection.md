# SourceUpdateParamsConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Snowflake account ID | [optional] 
**database** | **str** | Redshift database name | [optional] 
**password** | **str** | Redshift password | [optional] 
**role** | **str** | Snowflake role | [optional] 
**var_schema** | **str** | Databricks schema | [optional] 
**type** | **str** |  | 
**user** | **str** | Redshift user name | [optional] 
**warehouse** | **str** | Snowflake warehouse | [optional] 
**host** | **str** | Redshift host | [optional] 
**port** | **int** | Redshift port | [optional] 
**credentials** | **str** | BigQuery credentials - Base 64 encoded Service account JSON | [optional] 
**dataset** | **str** | BigQuery dataset | [optional] 
**project** | **str** | BigQuery project | [optional] 
**access_token** | **str** | Databricks access token | [optional] 
**catalog** | **str** | Databricks catalog | [optional] 
**http_path** | **str** | Databricks server HTTP path | [optional] 
**server_hostname** | **str** | Databricks server hostname | [optional] 
**token** | **str** | STAC token | [optional] 
**url** | **str** | WMS/WMTS URL | [optional] 

## Example

```python
from felt_api.models.source_update_params_connection import SourceUpdateParamsConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SourceUpdateParamsConnection from a JSON string
source_update_params_connection_instance = SourceUpdateParamsConnection.from_json(json)
# print the JSON string representation of the object
print(SourceUpdateParamsConnection.to_json())

# convert the object into a dict
source_update_params_connection_dict = source_update_params_connection_instance.to_dict()
# create an instance of SourceUpdateParamsConnection from a dict
source_update_params_connection_from_dict = SourceUpdateParamsConnection.from_dict(source_update_params_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


