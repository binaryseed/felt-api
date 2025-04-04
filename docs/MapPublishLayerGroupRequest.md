# MapPublishLayerGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to publish the layer group under | [optional] [default to 'not_provided']

## Example

```python
from felt_api.models.map_publish_layer_group_request import MapPublishLayerGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapPublishLayerGroupRequest from a JSON string
map_publish_layer_group_request_instance = MapPublishLayerGroupRequest.from_json(json)
# print the JSON string representation of the object
print(MapPublishLayerGroupRequest.to_json())

# convert the object into a dict
map_publish_layer_group_request_dict = map_publish_layer_group_request_instance.to_dict()
# create an instance of MapPublishLayerGroupRequest from a dict
map_publish_layer_group_request_from_dict = MapPublishLayerGroupRequest.from_dict(map_publish_layer_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


