import felt_api

import typing
import urllib.request
import uuid
import io
import os


def client(api_key: str):
    configuration = felt_api.Configuration(host="https://felt.com")
    configuration.api_key["bearerAuth"] = api_key
    configuration.api_key_prefix["bearerAuth"] = "Bearer"
    api_client = felt_api.ApiClient(configuration)
    return felt_api.DefaultApi(api_client)


def upload_file(client, map_id: str, file_name: str, layer_name: str):
    map_upload_layer_request = felt_api.MapUploadLayerRequest.from_dict(
        {"name": layer_name}
    )
    result = client.map_upload_layer(
        map_id, map_upload_layer_request=map_upload_layer_request
    )
    with open(file_name, "rb") as file_obj:
        request = _multipart_request(result.url, result.presigned_attributes, file_obj)
        urllib.request.urlopen(request)
    return result


def _multipart_request(
    url: str, presigned_attributes: dict[str, str], file_obj: typing.IO[bytes]
) -> urllib.request.Request:
    """Make a multipart/form-data request with the given file"""
    boundary = "-" * 20 + str(uuid.uuid4())
    headers = {"Content-Type": f'multipart/form-data; boundary="{boundary}"'}
    fname = os.path.basename(file_obj.name)
    data = io.BytesIO()
    text = io.TextIOWrapper(data, encoding="latin-1")
    for key, value in presigned_attributes.items():
        text.write(f"--{boundary}\r\n")
        text.write(f'Content-Disposition: form-data; name="{key}"\r\n\r\n')
        text.write(f"{value}\r\n")
    text.write(f"--{boundary}\r\n")
    text.write(f'Content-Disposition: form-data; name="file"; filename="{fname}"\r\n')
    text.write("Content-Type: application/octet-stream\r\n\r\n")
    text.flush()
    data.write(file_obj.read())
    data.write(f"\r\n--{boundary}".encode("latin-1"))
    body = data.getvalue()
    return urllib.request.Request(url, data=body, headers=headers, method="POST")
