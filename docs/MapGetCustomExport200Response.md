# MapGetCustomExport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** |  | 
**export_id** | **str** |  | 
**filters** | **List[object]** |  | 
**status** | **str** |  | 

## Example

```python
from felt_api.models.map_get_custom_export200_response import MapGetCustomExport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of MapGetCustomExport200Response from a JSON string
map_get_custom_export200_response_instance = MapGetCustomExport200Response.from_json(json)
# print the JSON string representation of the object
print(MapGetCustomExport200Response.to_json())

# convert the object into a dict
map_get_custom_export200_response_dict = map_get_custom_export200_response_instance.to_dict()
# create an instance of MapGetCustomExport200Response from a dict
map_get_custom_export200_response_from_dict = MapGetCustomExport200Response.from_dict(map_get_custom_export200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


