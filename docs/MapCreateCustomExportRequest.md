# MapCreateCustomExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_on_completion** | **bool** | Send an email to the requesting user when the export completes. Defaults to &#x60;true&#x60; | [optional] 
**filters** | **List[object]** | Filters for the layer in specified in Felt Style Language filter format | [optional] 
**output_format** | **str** |  | 

## Example

```python
from felt_api.models.map_create_custom_export_request import MapCreateCustomExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapCreateCustomExportRequest from a JSON string
map_create_custom_export_request_instance = MapCreateCustomExportRequest.from_json(json)
# print the JSON string representation of the object
print(MapCreateCustomExportRequest.to_json())

# convert the object into a dict
map_create_custom_export_request_dict = map_create_custom_export_request_instance.to_dict()
# create an instance of MapCreateCustomExportRequest from a dict
map_create_custom_export_request_from_dict = MapCreateCustomExportRequest.from_dict(map_create_custom_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


