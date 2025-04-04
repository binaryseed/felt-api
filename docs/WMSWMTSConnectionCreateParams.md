# WMSWMTSConnectionCreateParams

Web Map Service / Web Map Tile Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** | WMS/WMTS URL | 

## Example

```python
from felt_api.models.wmswmts_connection_create_params import WMSWMTSConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WMSWMTSConnectionCreateParams from a JSON string
wmswmts_connection_create_params_instance = WMSWMTSConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(WMSWMTSConnectionCreateParams.to_json())

# convert the object into a dict
wmswmts_connection_create_params_dict = wmswmts_connection_create_params_instance.to_dict()
# create an instance of WMSWMTSConnectionCreateParams from a dict
wmswmts_connection_create_params_from_dict = WMSWMTSConnectionCreateParams.from_dict(wmswmts_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


