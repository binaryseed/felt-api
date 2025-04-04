# MapUploadLayerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**List[UploadInterpretationHint]**](UploadInterpretationHint.md) | A list of hints for interpreting the data in the upload. | [optional] 
**import_url** | **str** | A public URL containing geodata to import, in place of uploading a file. | [optional] 
**lat** | **float** | (Image uploads only) The latitude of the image center. | [optional] 
**lng** | **float** | (Image uploads only) The longitude of the image center. | [optional] 
**metadata** | [**LayerMetadata**](LayerMetadata.md) |  | [optional] 
**name** | **str** | The display name for the new layer. | 
**zoom** | **float** | (Image uploads only) The zoom level of the image. | [optional] 

## Example

```python
from felt_api.models.map_upload_layer_request import MapUploadLayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapUploadLayerRequest from a JSON string
map_upload_layer_request_instance = MapUploadLayerRequest.from_json(json)
# print the JSON string representation of the object
print(MapUploadLayerRequest.to_json())

# convert the object into a dict
map_upload_layer_request_dict = map_upload_layer_request_instance.to_dict()
# create an instance of MapUploadLayerRequest from a dict
map_upload_layer_request_from_dict = MapUploadLayerRequest.from_dict(map_upload_layer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


