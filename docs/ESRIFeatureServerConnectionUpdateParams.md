# ESRIFeatureServerConnectionUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Feature Server token | [optional] 
**type** | **str** |  | 
**url** | **str** | Feature Server URL | [optional] 

## Example

```python
from felt_api.models.esri_feature_server_connection_update_params import ESRIFeatureServerConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ESRIFeatureServerConnectionUpdateParams from a JSON string
esri_feature_server_connection_update_params_instance = ESRIFeatureServerConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(ESRIFeatureServerConnectionUpdateParams.to_json())

# convert the object into a dict
esri_feature_server_connection_update_params_dict = esri_feature_server_connection_update_params_instance.to_dict()
# create an instance of ESRIFeatureServerConnectionUpdateParams from a dict
esri_feature_server_connection_update_params_from_dict = ESRIFeatureServerConnectionUpdateParams.from_dict(esri_feature_server_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


