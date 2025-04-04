#!/bin/bash

# Errors
# components.schemas.LayerMetadata.default=`not_provided` is not of type `date`
#


# docker run --rm openapitools/openapi-generator-cli help generate

rm -rf felt_api

docker run --rm -v "/Users/vince/felt/felt_api:/local" -v "/Users/vince/felt/felt:/felt" openapitools/openapi-generator-cli generate \
          -i /felt/priv/felt_openapi_spec_v2.json \
          --skip-validate-spec \
          --package-name felt_api \
          -g python \
          -o /local

git add felt_api docs README.md requirements.txt setup.py
git clean -fd
