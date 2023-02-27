#!/bin/sh

OPEN_AI_API_KEY=$(head -1 "$CONFIG"/openai_api_key)
KEY_HEADER="Authorization: Bearer $OPEN_AI_API_KEY"

curl=`cat <<EOS
curl https://api.openai.com/v1/completions \
  -H 'Content-Type: application/json' \
  -H "$KEY_HEADER" \
  -d '{
  "model": "text-davinci-003",
  "prompt": "$1",
  "max_tokens": 4000,
  "temperature": $2

}' \
--insecure | jq -r '.choices[]'.text
EOS`

eval ${curl}