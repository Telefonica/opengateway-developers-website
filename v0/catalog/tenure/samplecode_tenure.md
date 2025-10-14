---
title: Sample code for Tenure
category:
  uri: API Catalog
content:
  excerpt: >-
    The following samples show how to use the [Open Gateway Tenure
    API](https://opengateway.telefonica.com/en/apis/tenure) to verify a
    specified length of tenure for a network subscriber to establish a level of
    trust for the network subscription identifier.
---

The following code shows, for didactic purposes, a hypothetical or sample SDK, in several programming languages, from a generic Open Gateway's channel partner, also known as aggregator.

The final implementation will depend on the channel partner's development tools offering. Sample code on how to consume the API without an SDK, directly with HTTP requests, is also provided.

> 📘 Want to try it before coding?
> Check the [API interactive reference](https://developers.opengateway.telefonica.com/reference/checktenure)

### Table of contents
- [Backend flow](#backend-flow)
  - [Authorization](#authorization)
  - [API usage](#api-usage)
- [Frontend flow](#frontend-flow)
  - [Authorization code request](#authorization-code-request)
  - [Callback handling](#callback-handling)

## Code samples

> 📘 Note
> These are code samples and not finalized ready-to-run code:
> - Remember to replace 'my-app-id' and 'my-app-secret' with the credentials of your app.
If you registered your test app on our Sandbox, you can retrieve its credentials [here](https://sandbox.opengateway.telefonica.com/my-apps). 
> - Remember also to replace "aggregator/opengateway-sdk" with the SDK from your aggregator.
If you are using our sandbox SDK, check info and installation of de Sandbox SDK [here](/docs/sdkreference)

## Backend flow

The authorization protocol used in Open Gateway for backend flows is the OIDC standard CIBA (Client-Initiated Backchannel Authentication). You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#ciba-flow-backend-flow).

### Authorization

```python Sample SDK for Python
from aggregator_opengateway_sdk import ClientCredentials, TenureVerifier

credentials = ClientCredentials(
    client_id='my-app-id',
    client_secret='my-app-secret'
)

tenure_client = TenureVerifier(credentials=credentials, phone_number='+34629255833')
```

```node Sample SDK for Node.js
import { ClientCredentials, TenureVerifier } from "aggregator/opengateway-sdk"

const credentials = new ClientCredentials({
    clientId: 'my-app-id',
    clientSecret: 'my-app-secret'
})

const customerPhoneNumber = '+34629255833'

const tenureClient = new TenureVerifier(credentials, undefined, customerPhoneNumber)
```

```java Sample SDK for Java
import aggregator.opengatewaysdk.ClientCredentials;
import aggregator.opengatewaysdk.TenureVerifier;

ClientCredentials credentials = new ClientCredentials(
    "my-app-id",
    "my-app-secret"
);

final String customerPhoneNumber = "+34629255833";

TenureVerifier tenureClient = new TenureVerifier(credentials, null, customerPhoneNumber);
```

```javascript HTTP using JavaScript (ES6)
let clientId = "my-app-id";
let clientSecret = "my-app-secret";
let appCredentials = btoa(`${clientId}:${clientSecret}`);
let scope = "dpv:FraudPreventionAndDetection#kyc-tenure";

const tokenRequest = await fetch("https://opengateway.aggregator.com/token", {
  method: "POST",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": `Basic ${appCredentials}`
  },
  body: new URLSearchParams({ scope })
});

const { access_token } = await tokenRequest.json();
```

### API usage

```python Sample SDK for Python
result = tenure_client.check_tenure({
    "tenureDate": "2022-01-15"
})

print("Tenure check passed?", result.tenureDateCheck)
if hasattr(result, 'contractType'):
    print("Contract type:", result.contractType)
```

```node Sample SDK for Node.js
const result = await tenureClient.checkTenure({
    tenureDate: "2022-01-15"
})

console.log("Tenure check passed?", result.tenureDateCheck)
if (result.contractType) {
    console.log("Contract type:", result.contractType)
}
```

```java Sample SDK for Java
Map<String, Object> tenureData = new HashMap<>();
tenureData.put("tenureDate", "2022-01-15");

TenureCheckResult result = tenureClient.checkTenure(tenureData);

System.out.println("Tenure check passed? " + result.getTenureDateCheck());
if (result.getContractType() != null) {
    System.out.println("Contract type: " + result.getContractType());
}
```

```javascript HTTP using JavaScript (ES6)
const headers = new Headers();
headers.append("Authorization", `Bearer ${access_token}`);
headers.append("Content-Type", "application/json");

const payload = JSON.stringify({
  tenureDate: "2022-01-15"
});

const response = await fetch("https://opengateway.aggregator.com/kyc-tenure/v0.1/check-tenure", {
  method: "POST",
  headers,
  body: payload
});

const result = await response.json();
console.log("Tenure check:", result.tenureDateCheck);
if (result.contractType) {
    console.log("Contract type:", result.contractType);
}
```

---

## Frontend flow

### Authorization code request

```javascript HTTP using JavaScript (ES6)
let clientId = "my-app-id";
let redirectUri = "https://myapp.com/tenure-callback";
let scope = "dpv:FraudPreventionAndDetection#kyc-tenure";

const params = new URLSearchParams({
  client_id: clientId,
  response_type: "code",
  scope,
  redirect_uri: redirectUri
});

window.location.href = `https://opengateway.aggregator.com/authorize?${params.toString()}`;
```

### Callback handling

```python HTTP using Python + Flask
from flask import Flask, request
import requests, base64

client_id = "my-app-id"
client_secret = "my-app-secret"

app = Flask(__name__)

@app.route('/tenure-callback', methods=['GET'])
def callback():
    code = request.args.get('code')
    credentials = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {credentials}"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "https://myapp.com/tenure-callback"
    }
    response = requests.post("https://opengateway.aggregator.com/token", headers=headers, data=data)
    access_token = response.json().get("access_token")
    return access_token

if __name__ == '__main__':
    app.run()
```
