# GoogleBigQueryConnectionUpdateParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **str** | BigQuery credentials - Base 64 encoded Service account JSON | [optional] 
**dataset** | **str** | BigQuery dataset | [optional] 
**project** | **str** | BigQuery project | [optional] 
**type** | **str** |  | 

## Example

```python
from felt_api.models.google_big_query_connection_update_params import GoogleBigQueryConnectionUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleBigQueryConnectionUpdateParams from a JSON string
google_big_query_connection_update_params_instance = GoogleBigQueryConnectionUpdateParams.from_json(json)
# print the JSON string representation of the object
print(GoogleBigQueryConnectionUpdateParams.to_json())

# convert the object into a dict
google_big_query_connection_update_params_dict = google_big_query_connection_update_params_instance.to_dict()
# create an instance of GoogleBigQueryConnectionUpdateParams from a dict
google_big_query_connection_update_params_from_dict = GoogleBigQueryConnectionUpdateParams.from_dict(google_big_query_connection_update_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


