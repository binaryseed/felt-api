# UnauthorizedErrorErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | [optional] 
**source** | [**UnauthorizedErrorErrorsInnerSource**](UnauthorizedErrorErrorsInnerSource.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from felt_api.models.unauthorized_error_errors_inner import UnauthorizedErrorErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedErrorErrorsInner from a JSON string
unauthorized_error_errors_inner_instance = UnauthorizedErrorErrorsInner.from_json(json)
# print the JSON string representation of the object
print(UnauthorizedErrorErrorsInner.to_json())

# convert the object into a dict
unauthorized_error_errors_inner_dict = unauthorized_error_errors_inner_instance.to_dict()
# create an instance of UnauthorizedErrorErrorsInner from a dict
unauthorized_error_errors_inner_from_dict = UnauthorizedErrorErrorsInner.from_dict(unauthorized_error_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


