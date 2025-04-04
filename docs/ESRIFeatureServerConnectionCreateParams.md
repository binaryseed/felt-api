# ESRIFeatureServerConnectionCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Feature Server token | [optional] 
**type** | **str** |  | 
**url** | **str** | Feature Server URL | 

## Example

```python
from felt_api.models.esri_feature_server_connection_create_params import ESRIFeatureServerConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of ESRIFeatureServerConnectionCreateParams from a JSON string
esri_feature_server_connection_create_params_instance = ESRIFeatureServerConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(ESRIFeatureServerConnectionCreateParams.to_json())

# convert the object into a dict
esri_feature_server_connection_create_params_dict = esri_feature_server_connection_create_params_instance.to_dict()
# create an instance of ESRIFeatureServerConnectionCreateParams from a dict
esri_feature_server_connection_create_params_from_dict = ESRIFeatureServerConnectionCreateParams.from_dict(esri_feature_server_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


