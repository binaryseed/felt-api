# MapCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basemap** | **str** | The basemap to use for the new map. Defaults to \&quot;default\&quot;. Valid values are \&quot;default\&quot;, \&quot;light\&quot;, \&quot;dark\&quot;, \&quot;satellite\&quot;, a valid raster tile URL with {x}, {y}, and {z} parameters, or a hex color string like #ff0000. | [optional] 
**description** | **str** | A description to display in the map legend | [optional] 
**lat** | **float** | If no data has been uploaded to the map, the initial latitude to center the map display on. | [optional] 
**layer_urls** | **List[str]** | An array of urls to use to create layers in the map. Only tile URLs for raster layers are supported at the moment. | [optional] 
**lon** | **float** | If no data has been uploaded to the map, the initial longitude to center the map display on. | [optional] 
**public_access** | **str** | The level of access to grant to the map. Defaults to \&quot;view_only\&quot;. | [optional] 
**title** | **str** | The title to be used for the map. Defaults to \&quot;Untitled Map\&quot; | [optional] 
**workspace_id** | **str** | The workspace to create the map in. Defaults to the latest used workspace | [optional] 
**zoom** | **float** | If no data has been uploaded to the map, the initial zoom level for the map to display. | [optional] 

## Example

```python
from felt_api.models.map_create_request import MapCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapCreateRequest from a JSON string
map_create_request_instance = MapCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MapCreateRequest.to_json())

# convert the object into a dict
map_create_request_dict = map_create_request_instance.to_dict()
# create an instance of MapCreateRequest from a dict
map_create_request_from_dict = MapCreateRequest.from_dict(map_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


