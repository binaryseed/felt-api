# AmazonRedshiftConnectionUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** | Redshift database name | [optional] 
**host** | **str** | Redshift host | [optional] 
**password** | **str** | Redshift password | [optional] 
**port** | **int** | Redshift port | [optional] 
**type** | **str** |  | 
**user** | **str** | Redshift user name | [optional] 

## Example

```python
from felt_api.models.amazon_redshift_connection_update_params import AmazonRedshiftConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonRedshiftConnectionUpdateParams from a JSON string
amazon_redshift_connection_update_params_instance = AmazonRedshiftConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(AmazonRedshiftConnectionUpdateParams.to_json())

# convert the object into a dict
amazon_redshift_connection_update_params_dict = amazon_redshift_connection_update_params_instance.to_dict()
# create an instance of AmazonRedshiftConnectionUpdateParams from a dict
amazon_redshift_connection_update_params_from_dict = AmazonRedshiftConnectionUpdateParams.from_dict(amazon_redshift_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


