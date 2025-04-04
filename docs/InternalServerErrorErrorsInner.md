# InternalServerErrorErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | [optional] 
**source** | [**InternalServerErrorErrorsInnerSource**](InternalServerErrorErrorsInnerSource.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from felt_api.models.internal_server_error_errors_inner import InternalServerErrorErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of InternalServerErrorErrorsInner from a JSON string
internal_server_error_errors_inner_instance = InternalServerErrorErrorsInner.from_json(json)
# print the JSON string representation of the object
print(InternalServerErrorErrorsInner.to_json())

# convert the object into a dict
internal_server_error_errors_inner_dict = internal_server_error_errors_inner_instance.to_dict()
# create an instance of InternalServerErrorErrorsInner from a dict
internal_server_error_errors_inner_from_dict = InternalServerErrorErrorsInner.from_dict(internal_server_error_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


