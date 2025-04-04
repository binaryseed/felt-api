# WMSWMTSConnectionUpdateParams

Web Map Service / Web Map Tile Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** | WMS/WMTS URL | [optional] 

## Example

```python
from felt_api.models.wmswmts_connection_update_params import WMSWMTSConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WMSWMTSConnectionUpdateParams from a JSON string
wmswmts_connection_update_params_instance = WMSWMTSConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(WMSWMTSConnectionUpdateParams.to_json())

# convert the object into a dict
wmswmts_connection_update_params_dict = wmswmts_connection_update_params_instance.to_dict()
# create an instance of WMSWMTSConnectionUpdateParams from a dict
wmswmts_connection_update_params_from_dict = WMSWMTSConnectionUpdateParams.from_dict(wmswmts_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


