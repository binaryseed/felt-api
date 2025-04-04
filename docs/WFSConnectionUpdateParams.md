# WFSConnectionUpdateParams

Web Feature Server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** | WFS URL | [optional] 

## Example

```python
from felt_api.models.wfs_connection_update_params import WFSConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of WFSConnectionUpdateParams from a JSON string
wfs_connection_update_params_instance = WFSConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(WFSConnectionUpdateParams.to_json())

# convert the object into a dict
wfs_connection_update_params_dict = wfs_connection_update_params_instance.to_dict()
# create an instance of WFSConnectionUpdateParams from a dict
wfs_connection_update_params_from_dict = WFSConnectionUpdateParams.from_dict(wfs_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


