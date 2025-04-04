# DatabricksConnectionCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Databricks access token | 
**catalog** | **str** | Databricks catalog | [optional] 
**http_path** | **str** | Databricks server HTTP path | 
**var_schema** | **str** | Databricks schema | [optional] 
**server_hostname** | **str** | Databricks server hostname | 
**type** | **str** |  | 

## Example

```python
from felt_api.models.databricks_connection_create_params import DatabricksConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksConnectionCreateParams from a JSON string
databricks_connection_create_params_instance = DatabricksConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(DatabricksConnectionCreateParams.to_json())

# convert the object into a dict
databricks_connection_create_params_dict = databricks_connection_create_params_instance.to_dict()
# create an instance of DatabricksConnectionCreateParams from a dict
databricks_connection_create_params_from_dict = DatabricksConnectionCreateParams.from_dict(databricks_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


