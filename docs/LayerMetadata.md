# LayerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_text** | **str** |  | [optional] [default to 'not_provided']
**attribution_url** | **str** |  | [optional] [default to 'not_provided']
**description** | **str** |  | [optional] [default to 'not_provided']
**license** | **str** |  | [optional] [default to 'not_provided']
**source_abbreviation** | **str** |  | [optional] [default to 'not_provided']
**source_name** | **str** |  | [optional] [default to 'not_provided']
**source_url** | **str** |  | [optional] [default to 'not_provided']
**updated_at** | **date** |  | [optional] 

## Example

```python
from felt_api.models.layer_metadata import LayerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LayerMetadata from a JSON string
layer_metadata_instance = LayerMetadata.from_json(json)
# print the JSON string representation of the object
print(LayerMetadata.to_json())

# convert the object into a dict
layer_metadata_dict = layer_metadata_instance.to_dict()
# create an instance of LayerMetadata from a dict
layer_metadata_from_dict = LayerMetadata.from_dict(layer_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


