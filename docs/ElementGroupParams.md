# ElementGroupParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] [default to '#C93535']
**id** | **str** |  | [optional] [default to 'not_provided']
**name** | **str** |  | 
**symbol** | **str** |  | [optional] [default to 'dot']

## Example

```python
from felt_api.models.element_group_params import ElementGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of ElementGroupParams from a JSON string
element_group_params_instance = ElementGroupParams.from_json(json)
# print the JSON string representation of the object
print(ElementGroupParams.to_json())

# convert the object into a dict
element_group_params_dict = element_group_params_instance.to_dict()
# create an instance of ElementGroupParams from a dict
element_group_params_from_dict = ElementGroupParams.from_dict(element_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


