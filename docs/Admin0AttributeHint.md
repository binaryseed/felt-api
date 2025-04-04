# Admin0AttributeHint

A hint that the data contains an Administrative Level 0 (Country) attribute. https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**Admin0AttributeHintAttribute**](Admin0AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.admin0_attribute_hint import Admin0AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of Admin0AttributeHint from a JSON string
admin0_attribute_hint_instance = Admin0AttributeHint.from_json(json)
# print the JSON string representation of the object
print(Admin0AttributeHint.to_json())

# convert the object into a dict
admin0_attribute_hint_dict = admin0_attribute_hint_instance.to_dict()
# create an instance of Admin0AttributeHint from a dict
admin0_attribute_hint_from_dict = Admin0AttributeHint.from_dict(admin0_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


