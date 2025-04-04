# AddSourceLayerSQLParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **str** |  | 
**query** | **str** |  | 
**source_id** | **str** |  | 

## Example

```python
from felt_api.models.add_source_layer_sql_params import AddSourceLayerSQLParams

# TODO update the JSON string below
json = "{}"
# create an instance of AddSourceLayerSQLParams from a JSON string
add_source_layer_sql_params_instance = AddSourceLayerSQLParams.from_json(json)
# print the JSON string representation of the object
print(AddSourceLayerSQLParams.to_json())

# convert the object into a dict
add_source_layer_sql_params_dict = add_source_layer_sql_params_instance.to_dict()
# create an instance of AddSourceLayerSQLParams from a dict
add_source_layer_sql_params_from_dict = AddSourceLayerSQLParams.from_dict(add_source_layer_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


