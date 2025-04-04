# AmazonRedshiftConnectionCreateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** | Redshift database name | 
**host** | **str** | Redshift host | 
**password** | **str** | Redshift password | 
**port** | **int** | Redshift port | [optional] 
**type** | **str** |  | 
**user** | **str** | Redshift user name | 

## Example

```python
from felt_api.models.amazon_redshift_connection_create_params import AmazonRedshiftConnectionCreateParams

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonRedshiftConnectionCreateParams from a JSON string
amazon_redshift_connection_create_params_instance = AmazonRedshiftConnectionCreateParams.from_json(json)
# print the JSON string representation of the object
print(AmazonRedshiftConnectionCreateParams.to_json())

# convert the object into a dict
amazon_redshift_connection_create_params_dict = amazon_redshift_connection_create_params_instance.to_dict()
# create an instance of AmazonRedshiftConnectionCreateParams from a dict
amazon_redshift_connection_create_params_from_dict = AmazonRedshiftConnectionCreateParams.from_dict(amazon_redshift_connection_create_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


