# felt_api.DefaultApi

All URIs are relative to *https://felt.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](DefaultApi.md#create_project) | **POST** /api/v2/projects | 
[**create_source**](DefaultApi.md#create_source) | **POST** /api/v2/sources | 
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /api/v2/projects/{project_id} | 
[**delete_source**](DefaultApi.md#delete_source) | **DELETE** /api/v2/sources/{source_id} | 
[**get_user**](DefaultApi.md#get_user) | **GET** /api/v2/user | 
[**library_list**](DefaultApi.md#library_list) | **GET** /api/v2/library | 
[**list_projects**](DefaultApi.md#list_projects) | **GET** /api/v2/projects | 
[**list_sources**](DefaultApi.md#list_sources) | **GET** /api/v2/sources | 
[**map_add_source_layer**](DefaultApi.md#map_add_source_layer) | **POST** /api/v2/maps/{map_id}/add_source_layer | 
[**map_create**](DefaultApi.md#map_create) | **POST** /api/v2/maps | 
[**map_create_custom_export**](DefaultApi.md#map_create_custom_export) | **POST** /api/v2/maps/{map_id}/layers/{layer_id}/custom_export | 
[**map_create_embed_token**](DefaultApi.md#map_create_embed_token) | **POST** /api/v2/maps/{map_id}/embed_token | 
[**map_delete**](DefaultApi.md#map_delete) | **DELETE** /api/v2/maps/{map_id} | 
[**map_delete_comment**](DefaultApi.md#map_delete_comment) | **DELETE** /api/v2/maps/{map_id}/comments/{comment_id} | 
[**map_delete_element**](DefaultApi.md#map_delete_element) | **DELETE** /api/v2/maps/{map_id}/elements/{element_id} | 
[**map_delete_layer**](DefaultApi.md#map_delete_layer) | **DELETE** /api/v2/maps/{map_id}/layers/{layer_id} | 
[**map_delete_layer_group**](DefaultApi.md#map_delete_layer_group) | **DELETE** /api/v2/maps/{map_id}/layer_groups/{layer_group_id} | 
[**map_duplicate_layers**](DefaultApi.md#map_duplicate_layers) | **POST** /api/v2/duplicate_layers | 
[**map_export_comments**](DefaultApi.md#map_export_comments) | **GET** /api/v2/maps/{map_id}/comments/export | 
[**map_get_custom_export**](DefaultApi.md#map_get_custom_export) | **GET** /api/v2/maps/{map_id}/layers/{layer_id}/custom_exports/{export_id} | 
[**map_get_export_link**](DefaultApi.md#map_get_export_link) | **GET** /api/v2/maps/{map_id}/layers/{layer_id}/get_export_link | 
[**map_list_element_groups**](DefaultApi.md#map_list_element_groups) | **GET** /api/v2/maps/{map_id}/element_groups | 
[**map_list_elements**](DefaultApi.md#map_list_elements) | **GET** /api/v2/maps/{map_id}/elements | 
[**map_list_layer_groups**](DefaultApi.md#map_list_layer_groups) | **GET** /api/v2/maps/{map_id}/layer_groups | 
[**map_list_layers**](DefaultApi.md#map_list_layers) | **GET** /api/v2/maps/{map_id}/layers | 
[**map_move**](DefaultApi.md#map_move) | **POST** /api/v2/maps/{map_id}/move | 
[**map_publish_layer**](DefaultApi.md#map_publish_layer) | **POST** /api/v2/maps/{map_id}/layers/{layer_id}/publish | 
[**map_publish_layer_group**](DefaultApi.md#map_publish_layer_group) | **POST** /api/v2/maps/{map_id}/layer_groups/{layer_group_id}/publish | 
[**map_refresh_layer**](DefaultApi.md#map_refresh_layer) | **POST** /api/v2/maps/{map_id}/layers/{layer_id}/refresh | 
[**map_resolve_comment**](DefaultApi.md#map_resolve_comment) | **POST** /api/v2/maps/{map_id}/comments/{comment_id}/resolve | 
[**map_show**](DefaultApi.md#map_show) | **GET** /api/v2/maps/{map_id} | 
[**map_show_element_groups**](DefaultApi.md#map_show_element_groups) | **GET** /api/v2/maps/{map_id}/element_groups/{group_id} | 
[**map_show_layer**](DefaultApi.md#map_show_layer) | **GET** /api/v2/maps/{map_id}/layers/{layer_id} | 
[**map_show_layer_group**](DefaultApi.md#map_show_layer_group) | **GET** /api/v2/maps/{map_id}/layer_groups/{layer_group_id} | 
[**map_update**](DefaultApi.md#map_update) | **POST** /api/v2/maps/{map_id}/update | 
[**map_update_layer**](DefaultApi.md#map_update_layer) | **POST** /api/v2/maps/{map_id}/layers | 
[**map_update_layer_groups**](DefaultApi.md#map_update_layer_groups) | **POST** /api/v2/maps/{map_id}/layer_groups | 
[**map_update_style**](DefaultApi.md#map_update_style) | **POST** /api/v2/maps/{map_id}/layers/{layer_id}/update_style | 
[**map_upload_layer**](DefaultApi.md#map_upload_layer) | **POST** /api/v2/maps/{map_id}/upload | 
[**map_upsert_element_groups**](DefaultApi.md#map_upsert_element_groups) | **POST** /api/v2/maps/{map_id}/element_groups | 
[**map_upsert_elements**](DefaultApi.md#map_upsert_elements) | **POST** /api/v2/maps/{map_id}/elements | 
[**show_project**](DefaultApi.md#show_project) | **GET** /api/v2/projects/{project_id} | 
[**show_source**](DefaultApi.md#show_source) | **GET** /api/v2/sources/{source_id} | 
[**sync_source**](DefaultApi.md#sync_source) | **POST** /api/v2/sources/{source_id}/sync | 
[**update_project**](DefaultApi.md#update_project) | **POST** /api/v2/projects/{project_id}/update | 
[**update_source**](DefaultApi.md#update_source) | **POST** /api/v2/sources/{source_id}/update | 


# **create_project**
> Project create_project(project_create_params=project_create_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.project import Project
from felt_api.models.project_create_params import ProjectCreateParams
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    project_create_params = felt_api.ProjectCreateParams() # ProjectCreateParams | Project create params (optional)

    try:
        api_response = api_instance.create_project(project_create_params=project_create_params)
        print("The response of DefaultApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create_params** | [**ProjectCreateParams**](ProjectCreateParams.md)| Project create params | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source**
> SourceReference create_source(source_create_params=source_create_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.source_create_params import SourceCreateParams
from felt_api.models.source_reference import SourceReference
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    source_create_params = felt_api.SourceCreateParams() # SourceCreateParams | Source create params (optional)

    try:
        api_response = api_instance.create_source(source_create_params=source_create_params)
        print("The response of DefaultApi->create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_create_params** | [**SourceCreateParams**](SourceCreateParams.md)| Source create params | [optional] 

### Return type

[**SourceReference**](SourceReference.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | SourceReference |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    project_id = 'project_id_example' # str | The ID of the Project to delete. Note: This will delete all Folders and Maps inside the project!

    try:
        api_instance.delete_project(project_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the Project to delete. Note: This will delete all Folders and Maps inside the project! | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source**
> delete_source(source_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    source_id = 'source_id_example' # str | The ID of the source to delete

    try:
        api_instance.delete_source(source_id)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source to delete | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user()

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.user import User
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)

    try:
        api_response = api_instance.get_user()
        print("The response of DefaultApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **library_list**
> LayerLibrary library_list(source=source)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer_library import LayerLibrary
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    source = workspace # str |  (optional) (default to workspace)

    try:
        api_response = api_instance.library_list(source=source)
        print("The response of DefaultApi->library_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->library_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  | [optional] [default to workspace]

### Return type

[**LayerLibrary**](LayerLibrary.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerLibrary |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> List[ProjectReference] list_projects(workspace_id=workspace_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.project_reference import ProjectReference
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    workspace_id = 'workspace_id_example' # str | Only needed when using the API as part of a plugin (optional)

    try:
        api_response = api_instance.list_projects(workspace_id=workspace_id)
        print("The response of DefaultApi->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_projects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Only needed when using the API as part of a plugin | [optional] 

### Return type

[**List[ProjectReference]**](ProjectReference.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Projects |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sources**
> List[SourceReference] list_sources(workspace_id=workspace_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.source_reference import SourceReference
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    workspace_id = 'workspace_id_example' # str | Only needed when using the API as part of a plugin (optional)

    try:
        api_response = api_instance.list_sources(workspace_id=workspace_id)
        print("The response of DefaultApi->list_sources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_sources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Only needed when using the API as part of a plugin | [optional] 

### Return type

[**List[SourceReference]**](SourceReference.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SourceReferences |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_add_source_layer**
> AddSourceLayerAccepted map_add_source_layer(map_id, add_source_layer_params=add_source_layer_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.add_source_layer_accepted import AddSourceLayerAccepted
from felt_api.models.add_source_layer_params import AddSourceLayerParams
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 
    add_source_layer_params = felt_api.AddSourceLayerParams() # AddSourceLayerParams | AddSourceLayerParams (optional)

    try:
        api_response = api_instance.map_add_source_layer(map_id, add_source_layer_params=add_source_layer_params)
        print("The response of DefaultApi->map_add_source_layer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_add_source_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **add_source_layer_params** | [**AddSourceLayerParams**](AddSourceLayerParams.md)| AddSourceLayerParams | [optional] 

### Return type

[**AddSourceLayerAccepted**](AddSourceLayerAccepted.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | AddSourceLayerAccepted |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_create**
> Map map_create(map_create_request=map_create_request)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.map import Map
from felt_api.models.map_create_request import MapCreateRequest
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_create_request = felt_api.MapCreateRequest() # MapCreateRequest | Map params (optional)

    try:
        api_response = api_instance.map_create(map_create_request=map_create_request)
        print("The response of DefaultApi->map_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_create_request** | [**MapCreateRequest**](MapCreateRequest.md)| Map params | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Map |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_create_custom_export**
> ExportRequestResponse map_create_custom_export(map_id, layer_id, map_create_custom_export_request=map_create_custom_export_request)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.export_request_response import ExportRequestResponse
from felt_api.models.map_create_custom_export_request import MapCreateCustomExportRequest
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map where the layer is located
    layer_id = 'layer_id_example' # str | The ID of the layer to export
    map_create_custom_export_request = felt_api.MapCreateCustomExportRequest() # MapCreateCustomExportRequest | Create custom export params (optional)

    try:
        api_response = api_instance.map_create_custom_export(map_id, layer_id, map_create_custom_export_request=map_create_custom_export_request)
        print("The response of DefaultApi->map_create_custom_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_create_custom_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map where the layer is located | 
 **layer_id** | **str**| The ID of the layer to export | 
 **map_create_custom_export_request** | [**MapCreateCustomExportRequest**](MapCreateCustomExportRequest.md)| Create custom export params | [optional] 

### Return type

[**ExportRequestResponse**](ExportRequestResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export request |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |
**503** | ServiceUnavailableError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_create_embed_token**
> EmbedToken map_create_embed_token(map_id, user_email=user_email)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.embed_token import EmbedToken
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 
    user_email = 'user_email_example' # str | Optionally assign the token to a user email address. Providing an email will enable the viewer to export data if the Map allows it. (optional)

    try:
        api_response = api_instance.map_create_embed_token(map_id, user_email=user_email)
        print("The response of DefaultApi->map_create_embed_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_create_embed_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **user_email** | **str**| Optionally assign the token to a user email address. Providing an email will enable the viewer to export data if the Map allows it. | [optional] 

### Return type

[**EmbedToken**](EmbedToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmbedToken |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete**
> map_delete(map_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to delete

    try:
        api_instance.map_delete(map_id)
    except Exception as e:
        print("Exception when calling DefaultApi->map_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to delete | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_comment**
> map_delete_comment(map_id, comment_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map that contains the comment.
    comment_id = 'comment_id_example' # str | The ID of the comment to delete.

    try:
        api_instance.map_delete_comment(map_id, comment_id)
    except Exception as e:
        print("Exception when calling DefaultApi->map_delete_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map that contains the comment. | 
 **comment_id** | **str**| The ID of the comment to delete. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_element**
> map_delete_element(map_id, element_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to delete the element from.
    element_id = 'element_id_example' # str | The ID of the element to delete.

    try:
        api_instance.map_delete_element(map_id, element_id)
    except Exception as e:
        print("Exception when calling DefaultApi->map_delete_element: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to delete the element from. | 
 **element_id** | **str**| The ID of the element to delete. | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_layer**
> map_delete_layer(map_id, layer_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to delete the layer from
    layer_id = 'layer_id_example' # str | The ID of the layer to delete

    try:
        api_instance.map_delete_layer(map_id, layer_id)
    except Exception as e:
        print("Exception when calling DefaultApi->map_delete_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to delete the layer from | 
 **layer_id** | **str**| The ID of the layer to delete | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_delete_layer_group**
> map_delete_layer_group(map_id, layer_group_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to delete the layer group from
    layer_group_id = 'layer_group_id_example' # str | The ID of the layer group to delete

    try:
        api_instance.map_delete_layer_group(map_id, layer_group_id)
    except Exception as e:
        print("Exception when calling DefaultApi->map_delete_layer_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to delete the layer group from | 
 **layer_group_id** | **str**| The ID of the layer group to delete | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_duplicate_layers**
> DuplicateLayersResponse map_duplicate_layers(duplicate_layers_params_inner=duplicate_layers_params_inner)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.duplicate_layers_params_inner import DuplicateLayersParamsInner
from felt_api.models.duplicate_layers_response import DuplicateLayersResponse
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    duplicate_layers_params_inner = [felt_api.DuplicateLayersParamsInner()] # List[DuplicateLayersParamsInner] | Duplicate Layers Params (optional)

    try:
        api_response = api_instance.map_duplicate_layers(duplicate_layers_params_inner=duplicate_layers_params_inner)
        print("The response of DefaultApi->map_duplicate_layers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_duplicate_layers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duplicate_layers_params_inner** | [**List[DuplicateLayersParamsInner]**](DuplicateLayersParamsInner.md)| Duplicate Layers Params | [optional] 

### Return type

[**DuplicateLayersResponse**](DuplicateLayersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Duplicate Layers Response |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_export_comments**
> List[object] map_export_comments(map_id, format=format)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to export comments from.
    format = 'format_example' # str | The format to export the comments in, either 'csv' or 'json' (default) (optional)

    try:
        api_response = api_instance.map_export_comments(map_id, format=format)
        print("The response of DefaultApi->map_export_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_export_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to export comments from. | 
 **format** | **str**| The format to export the comments in, either &#39;csv&#39; or &#39;json&#39; (default) | [optional] 

### Return type

**List[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommentExport |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_custom_export**
> MapGetCustomExport200Response map_get_custom_export(map_id, layer_id, export_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.map_get_custom_export200_response import MapGetCustomExport200Response
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map where the layer is located
    layer_id = 'layer_id_example' # str | The ID of the layer to export
    export_id = 'export_id_example' # str | The ID of the export

    try:
        api_response = api_instance.map_get_custom_export(map_id, layer_id, export_id)
        print("The response of DefaultApi->map_get_custom_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_get_custom_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map where the layer is located | 
 **layer_id** | **str**| The ID of the layer to export | 
 **export_id** | **str**| The ID of the export | 

### Return type

[**MapGetCustomExport200Response**](MapGetCustomExport200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export request |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_get_export_link**
> MapGetExportLink200Response map_get_export_link(map_id, layer_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.map_get_export_link200_response import MapGetExportLink200Response
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map where the layer is located
    layer_id = 'layer_id_example' # str | The ID of the layer to export

    try:
        api_response = api_instance.map_get_export_link(map_id, layer_id)
        print("The response of DefaultApi->map_get_export_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_get_export_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map where the layer is located | 
 **layer_id** | **str**| The ID of the layer to export | 

### Return type

[**MapGetExportLink200Response**](MapGetExportLink200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export link |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |
**503** | ServiceUnavailableError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_list_element_groups**
> List[ElementGroup] map_list_element_groups(map_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.element_group import ElementGroup
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to list groups from.

    try:
        api_response = api_instance.map_list_element_groups(map_id)
        print("The response of DefaultApi->map_list_element_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_list_element_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to list groups from. | 

### Return type

[**List[ElementGroup]**](ElementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GroupList |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_list_elements**
> GeoJSON map_list_elements(map_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.geo_json import GeoJSON
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to list elements from.

    try:
        api_response = api_instance.map_list_elements(map_id)
        print("The response of DefaultApi->map_list_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_list_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to list elements from. | 

### Return type

[**GeoJSON**](GeoJSON.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GeoJSON |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_list_layer_groups**
> List[LayerGroup] map_list_layer_groups(map_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer_group import LayerGroup
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 

    try:
        api_response = api_instance.map_list_layer_groups(map_id)
        print("The response of DefaultApi->map_list_layer_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_list_layer_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 

### Return type

[**List[LayerGroup]**](LayerGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Layers Groups |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_list_layers**
> List[Layer] map_list_layers(map_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer import Layer
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 

    try:
        api_response = api_instance.map_list_layers(map_id)
        print("The response of DefaultApi->map_list_layers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_list_layers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 

### Return type

[**List[Layer]**](Layer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Layers |  -  |
**401** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_move**
> Map map_move(map_id, move_map_params=move_map_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.map import Map
from felt_api.models.move_map_params import MoveMapParams
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 
    move_map_params = felt_api.MoveMapParams() # MoveMapParams | Move map params (optional)

    try:
        api_response = api_instance.map_move(map_id, move_map_params=move_map_params)
        print("The response of DefaultApi->map_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **move_map_params** | [**MoveMapParams**](MoveMapParams.md)| Move map params | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Map |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_publish_layer**
> Layer map_publish_layer(map_id, layer_id, map_publish_layer_request=map_publish_layer_request)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer import Layer
from felt_api.models.map_publish_layer_request import MapPublishLayerRequest
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map where the layer is located
    layer_id = 'layer_id_example' # str | The ID of the layer to publish
    map_publish_layer_request = felt_api.MapPublishLayerRequest() # MapPublishLayerRequest | Publish layer params (optional)

    try:
        api_response = api_instance.map_publish_layer(map_id, layer_id, map_publish_layer_request=map_publish_layer_request)
        print("The response of DefaultApi->map_publish_layer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_publish_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map where the layer is located | 
 **layer_id** | **str**| The ID of the layer to publish | 
 **map_publish_layer_request** | [**MapPublishLayerRequest**](MapPublishLayerRequest.md)| Publish layer params | [optional] 

### Return type

[**Layer**](Layer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Publish layer response |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_publish_layer_group**
> LayerGroup map_publish_layer_group(map_id, layer_group_id, map_publish_layer_group_request=map_publish_layer_group_request)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer_group import LayerGroup
from felt_api.models.map_publish_layer_group_request import MapPublishLayerGroupRequest
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map where the layer group is located
    layer_group_id = 'layer_group_id_example' # str | The ID of the layer group to publish
    map_publish_layer_group_request = felt_api.MapPublishLayerGroupRequest() # MapPublishLayerGroupRequest | Publish layer group params (optional)

    try:
        api_response = api_instance.map_publish_layer_group(map_id, layer_group_id, map_publish_layer_group_request=map_publish_layer_group_request)
        print("The response of DefaultApi->map_publish_layer_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_publish_layer_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map where the layer group is located | 
 **layer_group_id** | **str**| The ID of the layer group to publish | 
 **map_publish_layer_group_request** | [**MapPublishLayerGroupRequest**](MapPublishLayerGroupRequest.md)| Publish layer group params | [optional] 

### Return type

[**LayerGroup**](LayerGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Publish layer group response |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_refresh_layer**
> UploadResponse map_refresh_layer(map_id, layer_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.upload_response import UploadResponse
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map hosting the layer to refresh
    layer_id = 'layer_id_example' # str | The ID of the layer to refresh

    try:
        api_response = api_instance.map_refresh_layer(map_id, layer_id)
        print("The response of DefaultApi->map_refresh_layer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_refresh_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map hosting the layer to refresh | 
 **layer_id** | **str**| The ID of the layer to refresh | 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UploadResponse |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_resolve_comment**
> CommentResolved map_resolve_comment(map_id, comment_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.comment_resolved import CommentResolved
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map that contains the comment.
    comment_id = 'comment_id_example' # str | The ID of the comment to resolve.

    try:
        api_response = api_instance.map_resolve_comment(map_id, comment_id)
        print("The response of DefaultApi->map_resolve_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_resolve_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map that contains the comment. | 
 **comment_id** | **str**| The ID of the comment to resolve. | 

### Return type

[**CommentResolved**](CommentResolved.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CommentResolved |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_show**
> Map map_show(map_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.map import Map
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 

    try:
        api_response = api_instance.map_show(map_id)
        print("The response of DefaultApi->map_show:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_show: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 

### Return type

[**Map**](Map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Map |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_show_element_groups**
> GeoJSON map_show_element_groups(map_id, group_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.geo_json import GeoJSON
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map.
    group_id = 'group_id_example' # str | The ID of the element group.

    try:
        api_response = api_instance.map_show_element_groups(map_id, group_id)
        print("The response of DefaultApi->map_show_element_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_show_element_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map. | 
 **group_id** | **str**| The ID of the element group. | 

### Return type

[**GeoJSON**](GeoJSON.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GeoJSON |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_show_layer**
> Layer map_show_layer(map_id, layer_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer import Layer
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 
    layer_id = 'layer_id_example' # str | 

    try:
        api_response = api_instance.map_show_layer(map_id, layer_id)
        print("The response of DefaultApi->map_show_layer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_show_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **layer_id** | **str**|  | 

### Return type

[**Layer**](Layer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Layer |  -  |
**401** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_show_layer_group**
> LayerGroup map_show_layer_group(map_id, layer_group_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer_group import LayerGroup
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 
    layer_group_id = 'layer_group_id_example' # str | 

    try:
        api_response = api_instance.map_show_layer_group(map_id, layer_group_id)
        print("The response of DefaultApi->map_show_layer_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_show_layer_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **layer_group_id** | **str**|  | 

### Return type

[**LayerGroup**](LayerGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Layer Group |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update**
> Map map_update(map_id, map_update_request=map_update_request)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.map import Map
from felt_api.models.map_update_request import MapUpdateRequest
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to update
    map_update_request = felt_api.MapUpdateRequest() # MapUpdateRequest | Map update params (optional)

    try:
        api_response = api_instance.map_update(map_id, map_update_request=map_update_request)
        print("The response of DefaultApi->map_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to update | 
 **map_update_request** | [**MapUpdateRequest**](MapUpdateRequest.md)| Map update params | [optional] 

### Return type

[**Map**](Map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Map |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_layer**
> List[Layer] map_update_layer(map_id, layer_params=layer_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer import Layer
from felt_api.models.layer_params import LayerParams
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 
    layer_params = [felt_api.LayerParams()] # List[LayerParams] | Layer params (optional)

    try:
        api_response = api_instance.map_update_layer(map_id, layer_params=layer_params)
        print("The response of DefaultApi->map_update_layer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_update_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **layer_params** | [**List[LayerParams]**](LayerParams.md)| Layer params | [optional] 

### Return type

[**List[Layer]**](Layer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Layer |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_layer_groups**
> List[LayerGroup] map_update_layer_groups(map_id, layer_group_params=layer_group_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer_group import LayerGroup
from felt_api.models.layer_group_params import LayerGroupParams
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | 
    layer_group_params = [felt_api.LayerGroupParams()] # List[LayerGroupParams] | Update LayerGroup params (optional)

    try:
        api_response = api_instance.map_update_layer_groups(map_id, layer_group_params=layer_group_params)
        print("The response of DefaultApi->map_update_layer_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_update_layer_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**|  | 
 **layer_group_params** | [**List[LayerGroupParams]**](LayerGroupParams.md)| Update LayerGroup params | [optional] 

### Return type

[**List[LayerGroup]**](LayerGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LayerGroup |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_update_style**
> Layer map_update_style(map_id, layer_id, map_update_style_request=map_update_style_request)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.layer import Layer
from felt_api.models.map_update_style_request import MapUpdateStyleRequest
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map where the layer is located
    layer_id = 'layer_id_example' # str | The ID of the layer to update the style of
    map_update_style_request = felt_api.MapUpdateStyleRequest() # MapUpdateStyleRequest | LayerStyleParams (optional)

    try:
        api_response = api_instance.map_update_style(map_id, layer_id, map_update_style_request=map_update_style_request)
        print("The response of DefaultApi->map_update_style:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_update_style: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map where the layer is located | 
 **layer_id** | **str**| The ID of the layer to update the style of | 
 **map_update_style_request** | [**MapUpdateStyleRequest**](MapUpdateStyleRequest.md)| LayerStyleParams | [optional] 

### Return type

[**Layer**](Layer.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_upload_layer**
> UploadResponse map_upload_layer(map_id, map_upload_layer_request=map_upload_layer_request)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.map_upload_layer_request import MapUploadLayerRequest
from felt_api.models.upload_response import UploadResponse
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to upload the layer to.
    map_upload_layer_request = felt_api.MapUploadLayerRequest() # MapUploadLayerRequest | LayerFileParams (optional)

    try:
        api_response = api_instance.map_upload_layer(map_id, map_upload_layer_request=map_upload_layer_request)
        print("The response of DefaultApi->map_upload_layer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_upload_layer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to upload the layer to. | 
 **map_upload_layer_request** | [**MapUploadLayerRequest**](MapUploadLayerRequest.md)| LayerFileParams | [optional] 

### Return type

[**UploadResponse**](UploadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UploadResponse |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_upsert_element_groups**
> List[ElementGroup] map_upsert_element_groups(map_id, element_group_params=element_group_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.element_group import ElementGroup
from felt_api.models.element_group_params import ElementGroupParams
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to create the group in
    element_group_params = [felt_api.ElementGroupParams()] # List[ElementGroupParams] | Element group params (optional)

    try:
        api_response = api_instance.map_upsert_element_groups(map_id, element_group_params=element_group_params)
        print("The response of DefaultApi->map_upsert_element_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_upsert_element_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to create the group in | 
 **element_group_params** | [**List[ElementGroupParams]**](ElementGroupParams.md)| Element group params | [optional] 

### Return type

[**List[ElementGroup]**](ElementGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GeoJSON |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_upsert_elements**
> GeoJSON map_upsert_elements(map_id, geo_json=geo_json)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.geo_json import GeoJSON
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    map_id = 'map_id_example' # str | The ID of the map to create the element in
    geo_json = felt_api.GeoJSON() # GeoJSON | Element params (optional)

    try:
        api_response = api_instance.map_upsert_elements(map_id, geo_json=geo_json)
        print("The response of DefaultApi->map_upsert_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->map_upsert_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_id** | **str**| The ID of the map to create the element in | 
 **geo_json** | [**GeoJSON**](GeoJSON.md)| Element params | [optional] 

### Return type

[**GeoJSON**](GeoJSON.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GeoJSON |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_project**
> Project show_project(project_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.project import Project
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_response = api_instance.show_project(project_id)
        print("The response of DefaultApi->show_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->show_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_source**
> Source show_source(source_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.source import Source
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    source_id = 'source_id_example' # str | The ID of the source to show

    try:
        api_response = api_instance.show_source(source_id)
        print("The response of DefaultApi->show_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->show_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source to show | 

### Return type

[**Source**](Source.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_source**
> SourceReference sync_source(source_id)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.source_reference import SourceReference
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    source_id = 'source_id_example' # str | The ID of the source to sync

    try:
        api_response = api_instance.sync_source(source_id)
        print("The response of DefaultApi->sync_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->sync_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source to sync | 

### Return type

[**SourceReference**](SourceReference.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | SourceReference |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(project_id, project_update_params=project_update_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.project import Project
from felt_api.models.project_update_params import ProjectUpdateParams
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    project_id = 'project_id_example' # str | The ID of the project to update
    project_update_params = felt_api.ProjectUpdateParams() # ProjectUpdateParams | Project update params (optional)

    try:
        api_response = api_instance.update_project(project_id, project_update_params=project_update_params)
        print("The response of DefaultApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The ID of the project to update | 
 **project_update_params** | [**ProjectUpdateParams**](ProjectUpdateParams.md)| Project update params | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_source**
> SourceReference update_source(source_id, source_update_params=source_update_params)

### Example

* Api Key Authentication (bearerAuth):

```python
import felt_api
from felt_api.models.source_reference import SourceReference
from felt_api.models.source_update_params import SourceUpdateParams
from felt_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://felt.com
# See configuration.py for a list of all supported configuration parameters.
configuration = felt_api.Configuration(
    host = "https://felt.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: bearerAuth
configuration.api_key['bearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['bearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with felt_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = felt_api.DefaultApi(api_client)
    source_id = 'source_id_example' # str | The ID of the source to update
    source_update_params = felt_api.SourceUpdateParams() # SourceUpdateParams | Source update params (optional)

    try:
        api_response = api_instance.update_source(source_id, source_update_params=source_update_params)
        print("The response of DefaultApi->update_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**| The ID of the source to update | 
 **source_update_params** | [**SourceUpdateParams**](SourceUpdateParams.md)| Source update params | [optional] 

### Return type

[**SourceReference**](SourceReference.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | SourceReference |  -  |
**401** | UnauthorizedError |  -  |
**403** | UnauthorizedError |  -  |
**404** | NotFoundError |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Unprocessable Entity |  -  |
**500** | InternalServerError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

