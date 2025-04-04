# USZipCode2022AttributeHint

A hint that the data contains US Zip Code (2022) attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**USZipCode2022AttributeHintAttribute**](USZipCode2022AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.us_zip_code2022_attribute_hint import USZipCode2022AttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of USZipCode2022AttributeHint from a JSON string
us_zip_code2022_attribute_hint_instance = USZipCode2022AttributeHint.from_json(json)
# print the JSON string representation of the object
print(USZipCode2022AttributeHint.to_json())

# convert the object into a dict
us_zip_code2022_attribute_hint_dict = us_zip_code2022_attribute_hint_instance.to_dict()
# create an instance of USZipCode2022AttributeHint from a dict
us_zip_code2022_attribute_hint_from_dict = USZipCode2022AttributeHint.from_dict(us_zip_code2022_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


