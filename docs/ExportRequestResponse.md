# ExportRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_request_id** | **str** |  | 
**poll_endpoint** | **str** |  | 

## Example

```python
from felt_api.models.export_request_response import ExportRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportRequestResponse from a JSON string
export_request_response_instance = ExportRequestResponse.from_json(json)
# print the JSON string representation of the object
print(ExportRequestResponse.to_json())

# convert the object into a dict
export_request_response_dict = export_request_response_instance.to_dict()
# create an instance of ExportRequestResponse from a dict
export_request_response_from_dict = ExportRequestResponse.from_dict(export_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


