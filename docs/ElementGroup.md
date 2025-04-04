# ElementGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | The color of the element group symbol. | 
**elements** | [**GeoJSON**](GeoJSON.md) |  | 
**id** | **str** | The ID of the element group. | 
**name** | **str** | The name of the element group. | 
**symbol** | **str** | The symbol used to represent the element group. | 

## Example

```python
from felt_api.models.element_group import ElementGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ElementGroup from a JSON string
element_group_instance = ElementGroup.from_json(json)
# print the JSON string representation of the object
print(ElementGroup.to_json())

# convert the object into a dict
element_group_dict = element_group_instance.to_dict()
# create an instance of ElementGroup from a dict
element_group_from_dict = ElementGroup.from_dict(element_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


