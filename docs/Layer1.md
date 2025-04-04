# Layer1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | 
**geometry_type** | **str** |  | 
**hide_from_legend** | **bool** |  | 
**id** | **str** |  | 
**is_spreadsheet** | **bool** |  | [optional] 
**links** | [**Layer1Links**](Layer1Links.md) |  | [optional] 
**metadata** | [**LayerMetadata**](LayerMetadata.md) |  | [optional] 
**name** | **str** |  | 
**ordering_key** | **int** | A sort order key used for ordering layers and layer groups in the legend | [optional] 
**progress** | **float** |  | 
**refresh_period** | **str** |  | [optional] 
**status** | **str** |  | 
**style** | **object** | The Felt Style Language style for the layer | 
**subtitle** | **str** | Deprecated: use &#x60;caption&#x60; instead. | [optional] 
**tile_url** | **str** | The tile URL for this layer | [optional] 
**type** | **str** |  | 

## Example

```python
from felt_api.models.layer1 import Layer1

# TODO update the JSON string below
json = "{}"
# create an instance of Layer1 from a JSON string
layer1_instance = Layer1.from_json(json)
# print the JSON string representation of the object
print(Layer1.to_json())

# convert the object into a dict
layer1_dict = layer1_instance.to_dict()
# create an instance of Layer1 from a dict
layer1_from_dict = Layer1.from_dict(layer1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


