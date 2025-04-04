# TimezoneAttributeHint

A hint that the data contains a Timezone attribute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | [**TimezoneAttributeHintAttribute**](TimezoneAttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.timezone_attribute_hint import TimezoneAttributeHint

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneAttributeHint from a JSON string
timezone_attribute_hint_instance = TimezoneAttributeHint.from_json(json)
# print the JSON string representation of the object
print(TimezoneAttributeHint.to_json())

# convert the object into a dict
timezone_attribute_hint_dict = timezone_attribute_hint_instance.to_dict()
# create an instance of TimezoneAttributeHint from a dict
timezone_attribute_hint_from_dict = TimezoneAttributeHint.from_dict(timezone_attribute_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


