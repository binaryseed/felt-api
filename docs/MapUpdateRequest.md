# MapUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description to display in the map legend | [optional] 
**public_access** | **str** | The level of access to grant to the map. Defaults to \&quot;view_only\&quot;. | [optional] 
**title** | **str** | The new title for the map | [optional] 

## Example

```python
from felt_api.models.map_update_request import MapUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapUpdateRequest from a JSON string
map_update_request_instance = MapUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MapUpdateRequest.to_json())

# convert the object into a dict
map_update_request_dict = map_update_request_instance.to_dict()
# create an instance of MapUpdateRequest from a dict
map_update_request_from_dict = MapUpdateRequest.from_dict(map_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


