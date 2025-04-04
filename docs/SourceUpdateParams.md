# SourceUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection** | [**SourceUpdateParamsConnection**](SourceUpdateParamsConnection.md) |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | [**SourceCreateParamsPermissions**](SourceCreateParamsPermissions.md) |  | [optional] 

## Example

```python
from felt_api.models.source_update_params import SourceUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of SourceUpdateParams from a JSON string
source_update_params_instance = SourceUpdateParams.from_json(json)
# print the JSON string representation of the object
print(SourceUpdateParams.to_json())

# convert the object into a dict
source_update_params_dict = source_update_params_instance.to_dict()
# create an instance of SourceUpdateParams from a dict
source_update_params_from_dict = SourceUpdateParams.from_dict(source_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


