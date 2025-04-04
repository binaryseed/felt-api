# GoogleBigQueryConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from felt_api.models.google_big_query_connection import GoogleBigQueryConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleBigQueryConnection from a JSON string
google_big_query_connection_instance = GoogleBigQueryConnection.from_json(json)
# print the JSON string representation of the object
print(GoogleBigQueryConnection.to_json())

# convert the object into a dict
google_big_query_connection_dict = google_big_query_connection_instance.to_dict()
# create an instance of GoogleBigQueryConnection from a dict
google_big_query_connection_from_dict = GoogleBigQueryConnection.from_dict(google_big_query_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


