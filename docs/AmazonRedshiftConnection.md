# AmazonRedshiftConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from felt_api.models.amazon_redshift_connection import AmazonRedshiftConnection

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonRedshiftConnection from a JSON string
amazon_redshift_connection_instance = AmazonRedshiftConnection.from_json(json)
# print the JSON string representation of the object
print(AmazonRedshiftConnection.to_json())

# convert the object into a dict
amazon_redshift_connection_dict = amazon_redshift_connection_instance.to_dict()
# create an instance of AmazonRedshiftConnection from a dict
amazon_redshift_connection_from_dict = AmazonRedshiftConnection.from_dict(amazon_redshift_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


