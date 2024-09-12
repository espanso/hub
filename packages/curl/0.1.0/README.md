---
package_name: "curl"
package_title: "curl Package"
package_desc: "A package to get curl code snippets"
package_version: "0.1.0"
package_author: "yanming zhang"
package_repo: "https://github.com/zhangymPerson/espanso-package-curl"
---
An package to get curl command code snippets 

For more information about espanso packages, read the [documentation](https://espanso.org/docs/).

## Usage

Available replacements:

| replacement      | description                                | output                                                                                                      |
| ---------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `:curl:`         | Get curl command example                   | `curl --request GET http://example.com`                                                                     |
| `:curlget:`      | Get curl command example with query string | `curl --request GET http://example.com?key=value`                                                           |
| `:curlpost:`     | Get curl command example with post         | `curl --request POST http://example.com`                                                                    |
| `:curlput:`      | Get curl command example with put          | `curl --request PUT http://example.com`                                                                     |
| `:curldelete:`   | Get curl command example with delete       | `curl --request DELETE http://example.com`                                                                  |
| `:curlpatch:`    | Get curl command example with patch        | `curl --request PATCH http://example.com`                                                                   |
| `:curlxml:`      | Get curl command example with xml          | `curl --request POST --header 'Content-Type: application/xml' --data '<key>value</key>' http://example.com` |
| `:curljson:`     | Get curl command example with json         | `curl --request POST --header 'Content-Type: application/json' --data '{"key":"value"}' http://example.com` |
| `:curldata:`     | Get curl command example with data         | `curl --request POST --header 'Content-Type: multipart/form-data' --form 'key=value' http://example.com`    |
| `:curldownload:` | Get curl command example with download     | `curl --request GET --output file.txt http://example.com`                                                   |
| `:curlupload:`   | Get curl command example with upload       | `curl --request POST --form 'file=@/path/to/file' http://example.com`                                       |
| `:curlheader:`   | Get curl command example with header       | `curl --request GET --header 'X-My-Header: 123' http://example.com`                                         |
| `:curlcookie:`   | Get curl command example with cookie       | `curl --request GET --cookie 'key=value' http://example.com`                                                |
| `:curlbasic:`    | Get curl command example with basic auth   | `curl --request GET --user 'username:password' http://example.com`                                          |
| `:curlproxy:`    | Get curl command example with proxy        | `curl --request GET --proxy http://proxy.example.com:8080 http://example.com`                               |
| `:curlbearer:`   | Get curl command example with bearer auth  | `curl --request GET --header 'Authorization: Bearer token' http://example.com`                              |
