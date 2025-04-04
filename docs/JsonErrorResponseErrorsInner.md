# JsonErrorResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | 
**source** | [**JsonErrorResponseErrorsInnerSource**](JsonErrorResponseErrorsInnerSource.md) |  | 
**title** | **str** |  | 

## Example

```python
from felt_api.models.json_error_response_errors_inner import JsonErrorResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonErrorResponseErrorsInner from a JSON string
json_error_response_errors_inner_instance = JsonErrorResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(JsonErrorResponseErrorsInner.to_json())

# convert the object into a dict
json_error_response_errors_inner_dict = json_error_response_errors_inner_instance.to_dict()
# create an instance of JsonErrorResponseErrorsInner from a dict
json_error_response_errors_inner_from_dict = JsonErrorResponseErrorsInner.from_dict(json_error_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


