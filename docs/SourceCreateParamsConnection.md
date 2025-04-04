# SourceCreateParamsConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Snowflake account ID | 
**database** | **str** | Redshift database name | 
**password** | **str** | Redshift password | 
**role** | **str** | Snowflake role | [optional] 
**var_schema** | **str** | Databricks schema | [optional] 
**type** | **str** |  | 
**user** | **str** | Redshift user name | 
**warehouse** | **str** | Snowflake warehouse | [optional] 
**host** | **str** | Redshift host | 
**port** | **int** | Redshift port | [optional] 
**credentials** | **str** | BigQuery credentials - Base 64 encoded Service account JSON | [optional] 
**dataset** | **str** | BigQuery dataset | [optional] 
**project** | **str** | BigQuery project | 
**access_token** | **str** | Databricks access token | 
**catalog** | **str** | Databricks catalog | [optional] 
**http_path** | **str** | Databricks server HTTP path | 
**server_hostname** | **str** | Databricks server hostname | 
**token** | **str** | STAC token | [optional] 
**url** | **str** | WMS/WMTS URL | 

## Example

```python
from felt_api.models.source_create_params_connection import SourceCreateParamsConnection

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCreateParamsConnection from a JSON string
source_create_params_connection_instance = SourceCreateParamsConnection.from_json(json)
# print the JSON string representation of the object
print(SourceCreateParamsConnection.to_json())

# convert the object into a dict
source_create_params_connection_dict = source_create_params_connection_instance.to_dict()
# create an instance of SourceCreateParamsConnection from a dict
source_create_params_connection_from_dict = SourceCreateParamsConnection.from_dict(source_create_params_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


