# UploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layer_group_id** | **str** |  | [optional] 
**layer_id** | **str** | The ID of the layer created by this upload. If multiple layers are included in the upload, this is the ID of the first layer in the layer group. | [optional] 
**presigned_attribues** | **object** | If provided, the presigned attributes to attach to the post request | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** | If provided, the URL to post the file to | [optional] 

## Example

```python
from felt_api.models.upload_response import UploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadResponse from a JSON string
upload_response_instance = UploadResponse.from_json(json)
# print the JSON string representation of the object
print(UploadResponse.to_json())

# convert the object into a dict
upload_response_dict = upload_response_instance.to_dict()
# create an instance of UploadResponse from a dict
upload_response_from_dict = UploadResponse.from_dict(upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


