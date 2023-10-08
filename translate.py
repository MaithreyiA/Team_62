import requests

endpoint = 'https://vidyaapi.cognitiveservices.azure.com/'
key =  '32147b15d7144737b463eaa740c22687'
path = 'translator/text/batch/v1.1/batches'
constructed_url = endpoint + path

sourceSASUrl = 'https://storageps18.blob.core.windows.net/inputdocs?sp=rl&st=2023-10-08T06:48:52Z&se=2023-10-08T14:48:52Z&sv=2022-11-02&sr=c&sig=FaW0Yl8L76MU6%2FV2wnXiP0%2BpDdsYvA8wQmUdaL1W3vE%3D'

targetSASUrl = 'https://storageps18.blob.core.windows.net/translateddocs?sp=wl&st=2023-10-08T06:50:14Z&se=2023-10-08T14:50:14Z&sv=2022-11-02&sr=c&sig=0Apa%2FY%2BWcCNoBBIsc0NAsyU0FKzLOdvxy%2B3j2ml0FNM%3D'

body= {
    "inputs": [
        {
            "source": {
                "sourceUrl": sourceSASUrl,
                "storageSource": "AzureBlob",
                "language": "en"
            },
            "targets": [
                {
                    "targetUrl": targetSASUrl,
                    "storageSource": "AzureBlob",
                    "category": "general",
                    "language": "te"
                }
            ]
        }
    ]
}
headers = {
  'Ocp-Apim-Subscription-Key': key,
  'Content-Type': 'application/json',
}

response = requests.post(constructed_url, headers=headers, json=body)
response_headers = response.headers

print(f'response status code: {response.status_code}\nresponse status: {response.reason}\n\nresponse headers:\n')

for key, value in response_headers.items():
    print(key, ":", value)
