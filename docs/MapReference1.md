# MapReference1


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
from felt_api.models.map_reference1 import MapReference1

# TODO update the JSON string below
json = "{}"
# create an instance of MapReference1 from a JSON string
map_reference1_instance = MapReference1.from_json(json)
# print the JSON string representation of the object
print(MapReference1.to_json())

# convert the object into a dict
map_reference1_dict = map_reference1_instance.to_dict()
# create an instance of MapReference1 from a dict
map_reference1_from_dict = MapReference1.from_dict(map_reference1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


