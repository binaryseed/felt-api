# EmbedToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from felt_api.models.embed_token import EmbedToken

# TODO update the JSON string below
json = "{}"
# create an instance of EmbedToken from a JSON string
embed_token_instance = EmbedToken.from_json(json)
# print the JSON string representation of the object
print(EmbedToken.to_json())

# convert the object into a dict
embed_token_dict = embed_token_instance.to_dict()
# create an instance of EmbedToken from a dict
embed_token_from_dict = EmbedToken.from_dict(embed_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


