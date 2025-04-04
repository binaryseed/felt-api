# MapPublishLayerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to publish the layer under | [optional] [default to 'not_provided']

## Example

```python
from felt_api.models.map_publish_layer_request import MapPublishLayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapPublishLayerRequest from a JSON string
map_publish_layer_request_instance = MapPublishLayerRequest.from_json(json)
# print the JSON string representation of the object
print(MapPublishLayerRequest.to_json())

# convert the object into a dict
map_publish_layer_request_dict = map_publish_layer_request_instance.to_dict()
# create an instance of MapPublishLayerRequest from a dict
map_publish_layer_request_from_dict = MapPublishLayerRequest.from_dict(map_publish_layer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


