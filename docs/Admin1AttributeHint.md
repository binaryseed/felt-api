# Admin1AttributeHint

A hint that the data contains an Administrative Level 1 (Region) attribute. https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**Admin1AttributeHintAttribute**](Admin1AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.admin1_attribute_hint import Admin1AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of Admin1AttributeHint from a JSON string
admin1_attribute_hint_instance = Admin1AttributeHint.from_json(json)
# print the JSON string representation of the object
print(Admin1AttributeHint.to_json())

# convert the object into a dict
admin1_attribute_hint_dict = admin1_attribute_hint_instance.to_dict()
# create an instance of Admin1AttributeHint from a dict
admin1_attribute_hint_from_dict = Admin1AttributeHint.from_dict(admin1_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


