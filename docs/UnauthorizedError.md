# UnauthorizedError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[UnauthorizedErrorErrorsInner]**](UnauthorizedErrorErrorsInner.md) |  | [optional] 

## Example

```python
from felt_api.models.unauthorized_error import UnauthorizedError

# TODO update the JSON string below
json = "{}"
# create an instance of UnauthorizedError from a JSON string
unauthorized_error_instance = UnauthorizedError.from_json(json)
# print the JSON string representation of the object
print(UnauthorizedError.to_json())

# convert the object into a dict
unauthorized_error_dict = unauthorized_error_instance.to_dict()
# create an instance of UnauthorizedError from a dict
unauthorized_error_from_dict = UnauthorizedError.from_dict(unauthorized_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


