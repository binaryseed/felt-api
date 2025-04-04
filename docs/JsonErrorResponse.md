# JsonErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[JsonErrorResponseErrorsInner]**](JsonErrorResponseErrorsInner.md) |  | 

## Example

```python
from felt_api.models.json_error_response import JsonErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JsonErrorResponse from a JSON string
json_error_response_instance = JsonErrorResponse.from_json(json)
# print the JSON string representation of the object
print(JsonErrorResponse.to_json())

# convert the object into a dict
json_error_response_dict = json_error_response_instance.to_dict()
# create an instance of JsonErrorResponse from a dict
json_error_response_from_dict = JsonErrorResponse.from_dict(json_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


