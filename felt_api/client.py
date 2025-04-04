
def client(api_key: str):
    configuration = Configuration(host = "https://felt.com")
    configuration.api_key['bearerAuth'] = api_key
    configuration.api_key_prefix['bearerAuth'] = 'Bearer'
    api_client = ApiClient(configuration)
    return DefaultApi(api_client)
