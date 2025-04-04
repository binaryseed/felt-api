# SourceCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | [**SourceCreateParamsConnection**](SourceCreateParamsConnection.md) |  | 
**name** | **str** |  | 
**permissions** | [**SourceCreateParamsPermissions**](SourceCreateParamsPermissions.md) |  | [optional] 

## Example

```python
from felt_api.models.source_create_params import SourceCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SourceCreateParams from a JSON string
source_create_params_instance = SourceCreateParams.from_json(json)
# print the JSON string representation of the object
print(SourceCreateParams.to_json())

# convert the object into a dict
source_create_params_dict = source_create_params_instance.to_dict()
# create an instance of SourceCreateParams from a dict
source_create_params_from_dict = SourceCreateParams.from_dict(source_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


