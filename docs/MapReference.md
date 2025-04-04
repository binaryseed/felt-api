# MapReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**folder_id** | **str** |  | 
**id** | **str** |  | 
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
from felt_api.models.map_reference import MapReference

# TODO update the JSON string below
json = "{}"
# create an instance of MapReference from a JSON string
map_reference_instance = MapReference.from_json(json)
# print the JSON string representation of the object
print(MapReference.to_json())

# convert the object into a dict
map_reference_dict = map_reference_instance.to_dict()
# create an instance of MapReference from a dict
map_reference_from_dict = MapReference.from_dict(map_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


