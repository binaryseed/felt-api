# WFSConnectionParams

Web Feature Server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**url** | **str** | WFS URL | 

## Example

```python
from felt_api.models.wfs_connection_params import WFSConnectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of WFSConnectionParams from a JSON string
wfs_connection_params_instance = WFSConnectionParams.from_json(json)
# print the JSON string representation of the object
print(WFSConnectionParams.to_json())

# convert the object into a dict
wfs_connection_params_dict = wfs_connection_params_instance.to_dict()
# create an instance of WFSConnectionParams from a dict
wfs_connection_params_from_dict = WFSConnectionParams.from_dict(wfs_connection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


