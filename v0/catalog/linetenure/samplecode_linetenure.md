---
title: Sample code for Tenure
excerpt: The following samples show how to use the [Open Gateway Tenure API](https://opengateway.telefonica.com/en/apis/tenure) to check whether a mobile subscription has been active since a given date, enabling fraud prevention and trust verification use cases.
category: 681879c3afc1a0003709c745
---

The API consumption flow for Tenure follows the [OIDC Authorization Code Flow](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#authorization-code-flow-frontend-flow). That means the request is triggered from the **frontend** (end-user device) but must be **completed on the backend**, where the access token is obtained and the API is called.

> 📘 Want to try it before coding?
> Check the [API reference and live console](https://developers.opengateway.telefonica.com/reference/checktenure)

## Table of contents
- [Frontend](#frontend)
  - [Requesting the authorization code](#requesting-the-authorization-code)
- [Backend](#backend)
  - [Getting the access token](#getting-the-access-token)
  - [Calling the Tenure API](#calling-the-tenure-api)

---

## Frontend

The API flow starts from the **end-user's device**, such as a mobile phone:
- Your application requests user authorization with a `redirect_uri` to receive the `code`.
- After successful login/consent, the telco redirects back to your callback with the authorization `code`.

### Requesting the authorization code
```javascript
let clientId = "my-app-id";
let redirectUri = "https://my-backend.com/tenure-callback";
let scope = "dpv:FraudPreventionAndDetection#kyc-tenure";

const params = new URLSearchParams({
  response_type: "code",
  client_id: clientId,
  redirect_uri: redirectUri,
  scope: scope
});

window.location.href = `https://opengateway.aggregator.com/authorize?${params.toString()}`;
```

Or using an HTML form:
```html
<form action="https://opengateway.aggregator.com/authorize" method="GET">
  <input type="hidden" name="client_id" value="my-app-id">
  <input type="hidden" name="response_type" value="code">
  <input type="hidden" name="scope" value="dpv:FraudPreventionAndDetection#kyc-tenure">
  <input type="hidden" name="redirect_uri" value="https://my-backend.com/tenure-callback">
  <button type="submit">Check Tenure</button>
</form>
```

---

## Backend

After the frontend redirects to your `redirect_uri`, your backend receives the `code`, uses it to obtain an `access_token`, and then calls the API.

### Getting the access token
#### Python
```python
import requests

client_id = "my-app-id"
client_secret = "my-app-secret"
redirect_uri = "https://my-backend.com/tenure-callback"
code = "received-from-redirect"

token = requests.post(
  "https://opengateway.aggregator.com/token",
  auth=(client_id, client_secret),
  data={
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": redirect_uri
  }
)

access_token = token.json()["access_token"]
```

#### Node.js
```javascript
const fetch = require('node-fetch');
const btoa = require('btoa');

const clientId = "my-app-id";
const clientSecret = "my-app-secret";
const redirectUri = "https://my-backend.com/tenure-callback";
const code = "received-from-redirect";

const credentials = btoa(`${clientId}:${clientSecret}`);

fetch("https://opengateway.aggregator.com/token", {
  method: "POST",
  headers: {
    "Authorization": `Basic ${credentials}`,
    "Content-Type": "application/x-www-form-urlencoded"
  },
  body: new URLSearchParams({
    grant_type: "authorization_code",
    code: code,
    redirect_uri: redirectUri
  })
})
.then(res => res.json())
.then(data => console.log(data.access_token));
```

#### cURL
```bash
curl -X POST https://opengateway.aggregator.com/token \
  -u "my-app-id:my-app-secret" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code&code=received-from-redirect&redirect_uri=https://my-backend.com/tenure-callback"
```

---

### Calling the Tenure API
#### Python
```python
headers = {
  "Authorization": f"Bearer {access_token}",
  "Content-Type": "application/json"
}

data = {
  "tenureDate": "2023-07-03"
}

response = requests.post(
  "https://sandbox.opengateway.telefonica.com/apigateway/kyc-tenure/v0.1/check-tenure",
  headers=headers,
  json=data
)

print(response.json())
```

#### Node.js
```javascript
const headers = {
  "Authorization": `Bearer ${access_token}`,
  "Content-Type": "application/json"
};

const body = JSON.stringify({
  tenureDate: "2023-07-03"
});

fetch("https://sandbox.opengateway.telefonica.com/apigateway/kyc-tenure/v0.1/check-tenure", {
  method: "POST",
  headers,
  body
})
  .then(res => res.json())
  .then(result => console.log(result));
```

#### cURL
```bash
curl -X POST https://sandbox.opengateway.telefonica.com/apigateway/kyc-tenure/v0.1/check-tenure \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"tenureDate": "2023-07-03"}'
```

---

## Notes
- Replace `my-app-id` and `my-app-secret` with your own credentials.
- Register and manage your apps at the [Open Gateway Sandbox](https://sandbox.opengateway.telefonica.com/my-apps).
- You can use `mock_sandbox_access_token` for testing.