# MapUpdateStyleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**style** | **object** | The new layer style, specified in Felt Style Language format | 

## Example

```python
from felt_api.models.map_update_style_request import MapUpdateStyleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapUpdateStyleRequest from a JSON string
map_update_style_request_instance = MapUpdateStyleRequest.from_json(json)
# print the JSON string representation of the object
print(MapUpdateStyleRequest.to_json())

# convert the object into a dict
map_update_style_request_dict = map_update_style_request_instance.to_dict()
# create an instance of MapUpdateStyleRequest from a dict
map_update_style_request_from_dict = MapUpdateStyleRequest.from_dict(map_update_style_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


