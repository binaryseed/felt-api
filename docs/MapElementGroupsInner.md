# MapElementGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | [**GeoJSON**](GeoJSON.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from felt_api.models.map_element_groups_inner import MapElementGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MapElementGroupsInner from a JSON string
map_element_groups_inner_instance = MapElementGroupsInner.from_json(json)
# print the JSON string representation of the object
print(MapElementGroupsInner.to_json())

# convert the object into a dict
map_element_groups_inner_dict = map_element_groups_inner_instance.to_dict()
# create an instance of MapElementGroupsInner from a dict
map_element_groups_inner_from_dict = MapElementGroupsInner.from_dict(map_element_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


