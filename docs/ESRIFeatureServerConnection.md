# ESRIFeatureServerConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from felt_api.models.esri_feature_server_connection import ESRIFeatureServerConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ESRIFeatureServerConnection from a JSON string
esri_feature_server_connection_instance = ESRIFeatureServerConnection.from_json(json)
# print the JSON string representation of the object
print(ESRIFeatureServerConnection.to_json())

# convert the object into a dict
esri_feature_server_connection_dict = esri_feature_server_connection_instance.to_dict()
# create an instance of ESRIFeatureServerConnection from a dict
esri_feature_server_connection_from_dict = ESRIFeatureServerConnection.from_dict(esri_feature_server_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


