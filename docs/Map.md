# Map


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**element_groups** | [**List[MapElementGroupsInner]**](MapElementGroupsInner.md) |  | 
**elements** | [**GeoJSON**](GeoJSON.md) |  | 
**folder_id** | **str** |  | [optional] 
**id** | **str** |  | 
**layer_groups** | [**List[LayerGroup1]**](LayerGroup1.md) |  | 
**layers** | [**List[Layer1]**](Layer1.md) |  | 
**links** | [**MapLinks**](MapLinks.md) |  | [optional] 
**project_id** | **str** |  | 
**public_access** | **str** |  | 
**thumbnail_url** | **str** | A static thumbnail image of the map | 
**title** | **str** |  | 
**type** | **str** |  | 
**url** | **str** |  | 
**visited_at** | **str** |  | 

## Example

```python
from felt_api.models.map import Map

# TODO update the JSON string below
json = "{}"
# create an instance of Map from a JSON string
map_instance = Map.from_json(json)
# print the JSON string representation of the object
print(Map.to_json())

# convert the object into a dict
map_dict = map_instance.to_dict()
# create an instance of Map from a dict
map_from_dict = Map.from_dict(map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


