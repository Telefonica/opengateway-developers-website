---
title: Frontend authorization flow
excerpt: If your application offers a human interface to provide your users with features enabled by Open Gateway, this is its frontend component, running on the end-user's device, that will trigger the API calling flow. This guide will show you how to authorize your application by identifying the end-user from their network connected devices.
category: 66d57750d3f60b0011576376
---

From a developer perspective, the frontend authorization flow consists of two sequential steps implemented by performing HTTP requests to the following Open Gateway Channel Partner's API gateway endpoints, compliant with the OIDC standard **Authorization Code Flow**.

## Frontend authorization flow steps

1. **Authorization request**: The flow triggers as a GET request for an authorization from the end-user connected device, so they can be identified by their operator by its IP address, and get an **authorization code** as a result, which will be passed in the query string to the application backend's **redirect URI** as a callback.

	Your application's frontend needs to include the following parameters in the request's query string:
	- `response_type=code`: The response type must be set to `code` to get an authorization code.
	- `client_id`: The client ID of your application, as registered in the Channel Partner's developer portal.
	- `purpose`: The purpose of the API call, according to the Open Gateway API product subscribed. It actually includes both the value for the W3C standard DPV purpose and a value for the scope in the following format `dpv:<w3c_purpose>#<scope>`. You can find the proper value for this parameter, for each API, in the API Reference section.
	- `redirect_uri`: The URI where the authorization code will be sent back to your application backend. This URI must be registered in the Channel Partner's developer portal as part of the application configuration.
	- `state`: This is an optional parameter according to the OIDC standard, but you will want to pass an end-user device identifier here, commonly the phone number, if you need to include this value in the request body when calling the service API from the backend once the authorization flow completes and an access token is retrieved.

	Your redirect URI (you will need to implement a server-side endpoint to handle the callback) will receive the following parameters in the query string:
	- `code`: The authorization code to be used in the next step.

	In case the API called (the request's scope) and the purpose, the combination of both, require the end-user's explicit consent, a redirect (HTTP status 302) will be responded with a consent capture web page from the operator as location, previously to the final redirect to your redirect URI. Once the user grants the consent, or rejects it, the flow will resume to your redirect URI with the result, this being the authorization code if the consent was granted.

	The following restrictions apply:
	- The request must be performed from the end-user's device who, at the same time, is the operator subscriber
	- Such device must be connected to operator's mobile network. WiFi connections or tethering from other devices will help operator from identifying your user as a subscriber
	- Your frontend application must be able to follow HTTP redirects (status 302 with an URL in the `Location` to redirect the request to), since both the consent capture and the final redirect to your redirect URI will be done this way. If this frontend is a web application, the web browser will handle it for you. For other technologies, please refer to the specific documentation regarding following HTTP redirects.

	[Check the API reference](/reference/authorize)

2. **Access token retrieval**: The authorization code received in the previous step will be used to get an access token from the Channel Partner's API gateway, by performing a POST request to the token endpoint.

	Your application's backend needs to include the following parameters in the request body:
	- `grant_type=authorization_code`: The grant type must be set to `authorization_code` to get an access token from an authorization code.
	- `code`: The authorization code received in the previous step.
	- `redirect_uri`: The URI where the authorization code was sent back to your application backend in the previous step.

	This request must be authorized with the following values as basic authentication:
	- `client_id`: The client ID of your application, as registered in the Channel Partner's developer portal.
	- `client_secret`: The client secret of your application, as registered in the Channel Partner's developer portal.

	The response will include the following parameters:
	- `access_token`: The access token to be used in the service API call.
	- `token_type`: The type of the token, usually `Bearer`.
	- `expires_in`: The time in seconds the token will be valid.

	[Check the API reference](/reference/token)

	Once you get the access token, you can use it to authorize you HTTP request to the Open Gateway service API accordingly with the `purpose` passed as a value in the authorization request above.
	
## Frontend authorization flow sequence diagram

![Frontend Authorization Flow Sequence Diagram](https://github.com/Telefonica/opengateway-developers-website/raw/main/callflows/authorization/diagrams/frontend.svg?autoSizes=true)

## References

In this portal, you can find the following references:
- [Authorization request reference](/reference/authorize)
- [Access token retrieval reference](/reference/token)
- [Guide on Privacy](/docs/privacy)
- [Postman collection](/docs/postman)
- [Sample code for Number Verification](/docs/samplecode_numberverification)

External references:
- [CAMARA APIs Access and User Consent Management](https://github.com/camaraproject/IdentityAndConsentManagement/blob/r0.2.0/documentation/CAMARA-API-access-and-user-consent.md)
- [OIDC Authorization Code flow specification](https://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth)