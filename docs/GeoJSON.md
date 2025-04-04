# GeoJSON


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | [**List[GeoJSONFeaturesInner]**](GeoJSONFeaturesInner.md) |  | 
**type** | **str** |  | 

## Example

```python
from felt_api.models.geo_json import GeoJSON

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSON from a JSON string
geo_json_instance = GeoJSON.from_json(json)
# print the JSON string representation of the object
print(GeoJSON.to_json())

# convert the object into a dict
geo_json_dict = geo_json_instance.to_dict()
# create an instance of GeoJSON from a dict
geo_json_from_dict = GeoJSON.from_dict(geo_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


