---
title: Backend authorization flow
excerpt: If your use case does not involve end-user's interaction you will want to integrate with Open Gateway APIs from the backend. This guide will help you understand the flows to get your application authorized to call the APIs from your server or any other environment without a human interface.
category: 66d57750d3f60b0011576376
---

> 📘 Note
>
> To try out our APIs, visit the [Sandbox](https://opengateway.telefonica.com/developer-hub/unirse).

From a developer perspective, the backend authorization flow consists of two sequential steps implemented by performing HTTP requests to the following Open Gateway Channel Partner's API gateway endpoints, compliant with the ODIC standard **CIBA** (Client-Initiated Backchannel Authentication Flow).

## Backend authorization flow steps

### Authorization request
The flow triggers as a POST request for an authorization from your application's backend, identifying the end-user as an operator subscriber, and get an **authorization request identification** as a result, which will be using in the next step.

Your application's backend needs to include the following parameters in the request body:
- `login_hint`: The login hint to be used by the operator to identify the end-user, in the following format `<identifier_type>:<identifier>`, those being:
	- `tel` for phone numbers. The `login_hint` must be a tel URI as defined in [RFC 3966](https://www.rfc-editor.org/info/rfc3966) for global phone numbers without visual separators in [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I/en) format. For example, `tel:+34666666666`.
	- `ipport` for IPv4 and IPv6 addresses, that can optionally include a port. For example, `ipport:80.90.34.2:16790`, `ipport:80.90.34.2`, `ipport:[2001:db8::1]:8080` or `ipport:[2001:db8::1]`
- `purpose`: The purpose of the API call, according to the Open Gateway API product subscribed. It actually includes both the value for the W3C standard DPV purpose and a value for the scope in the following format `dpv:<w3c_purpose>#<scope>`. You can find the proper value for this parameter, for each API, in the API Reference section.

This request must be authorized with the following values as basic authentication:
- `client_id`: The client ID of your application, as registered in the Channel Partner's developer portal.
- `client_secret`: The client secret of your application, as registered in the Channel Partner's developer portal.

In case the API called (the request's scope) and the purpose, the combination of both, require the end-user's explicit consent, this authorization request won't succeed until such consent is gathered by other mean, also know as out-of-band. More context on this in the [Authorization](/docs/authorization) and [Privacy](/docs/privacy) guides.

```curl Sample request
curl --request POST \
     --url https://sandbox.opengateway.telefonica.com/apigateway/bc-authorize \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data 'login_hint=tel:+34655555555' \
     --data 'purpose=dpv:FraudPreventionAndDetection#sim-swap' \
     -u "your_app_client_id:your_app_client_secret"
```

[Check the API reference](/reference/bcauthorize)

### Access token retrieval
The authorization request id received in the previous step will be used to get an access token from the Channel Partner's API gateway, by performing a POST request to the token endpoint.

Your application's backend needs to include the following parameters in the request body:
- `grant_type=urn:openid:params:grant-type:ciba`: The grant type must be set to `urn:openid:params:grant-type:ciba` to get an access token in a CIBA flow.
- `auth_req_id`: The authorization request id received in the previous step.

This request must be authorized with the following values as basic authentication:
- `client_id`: The client ID of your application, as registered in the Channel Partner's developer portal.
- `client_secret`: The client secret of your application, as registered in the Channel Partner's developer portal.

The response will include the following parameters:
- `access_token`: The access token to be used in the service API call.
- `token_type`: The type of the token, usually `Bearer`.
- `expires_in`: The time in seconds the token will be valid.

```curl Sample request
curl --request POST \
     --url https://sandbox.opengateway.telefonica.com/apigateway/token \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data grant_type=urn:openid:params:grant-type:ciba \
     --data auth_req_id=obtained_auth_req_idt \
     -u "your_app_client_id:your_app_client_secret"
```

[Check the API reference](/reference/token)

Once you get the access token, you can use it to authorize you HTTP request to the Open Gateway service API accordingly with the `purpose` passed as a value in the authorization request above.
	
## Backend authorization flow sequence diagram

![Backend Authorization Flow Sequence Diagram](https://github.com/Telefonica/opengateway-developers-website/raw/main/callflows/authorization/diagrams/backend.svg?autoSizes=true)

## References

In this portal, you can find the following references:
- [Authorization request reference](/reference/bcauthorize)
- [Access token retrieval reference](/reference/token)
- [Guide on Privacy](/docs/privacy)
- [Postman interaction](/docs/postmaninteraction)
- [Sample code for SIM Swap](/docs/samplecode_simswap)

External references:
- [CAMARA APIs Access and User Consent Management](https://github.com/camaraproject/IdentityAndConsentManagement/blob/r0.2.0/documentation/CAMARA-API-access-and-user-consent.md)
- [OIDC Client-Initiated Backchannel Authentication Flow](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html)