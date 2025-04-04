# UploadInterpretationHint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**LocalityAttributeHintAttributes**](LocalityAttributeHintAttributes.md) |  | 
**attribute** | [**H3AttributeHintAttribute**](H3AttributeHintAttribute.md) |  | 

## Example

```python
from felt_api.models.upload_interpretation_hint import UploadInterpretationHint

# TODO update the JSON string below
json = "{}"
# create an instance of UploadInterpretationHint from a JSON string
upload_interpretation_hint_instance = UploadInterpretationHint.from_json(json)
# print the JSON string representation of the object
print(UploadInterpretationHint.to_json())

# convert the object into a dict
upload_interpretation_hint_dict = upload_interpretation_hint_instance.to_dict()
# create an instance of UploadInterpretationHint from a dict
upload_interpretation_hint_from_dict = UploadInterpretationHint.from_dict(upload_interpretation_hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


