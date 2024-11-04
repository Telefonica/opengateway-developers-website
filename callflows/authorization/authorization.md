---
title: Authorization
excerpt: In this guide you will find a briefly introduction to authorization mechanisms and best practices for secure access to Open Gateway APIs
category: 66d57750d3f60b0011576376
---

> 📘 To try out our APIs, visit the [Sandbox](https://opengateway.telefonica.com/developer-hub/unirse).

## Authorization standards

As standardized by CAMARA, Open Gateway API access will be secured using [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) (OIDC) on top of OAuth 2.0 protocol. Operators are aligned in introducing the concept of **purpose** in order to fully comply with data protection regulations, such as the GDPR regulation in Europe, to protect user privacy. More on this in the [Privacy guide](/docs/privacy).

## Authentication on the Channel Partners

By using OIDC authorization flows, Open Gateway telcos provide an interoperable and secure way to access their APIs. When it comes to the Channel Partners, which provide the API gateways that developer applications will actually perform calls to (see [API Architecture](/docs/architecture)), they may also offer their own authentication mechanisms, always compliant with the OpenID Connect standard and aggregating and routing authorization to the end-user's operator.

This guide covers the CAMARA standard authorization flows. Please refer to your Channel Partner of choice for specific details on their implementation. Most likely they will abstract some concepts for you like access tokens, scopes or purposes, according to the specific API products you subscribe to in their platform.

Whether your Channel Partner provides you with the Open Gateway OIDC standard flows or its own, it will handle operator routing for you to authorize you application's call to the proper operator according to your end-user, so your application will get an only Channel Partner's 3-legged access token for each user, scope and purpose, and then use it without caring about what the operator is.

## Authorization flows

According to your application's use case, the API call flow will trigger from the frontend or the backend of your application. Your use case could even have no human interface nor involve a interaction with an operator subscriber's connected device. The authorization flow will be different in each case:

- If your application's feature leveraging Open Gateway APIs is triggered by a user action in the frontend, you will need to use the frontend authorization flow, following the OIDC **Authorization Code flow** standard.

	[Frontend authorization flow](/docs/frontend)

- If you want to use Open Gateway APIs from your backend without end-user interaction, or the connected devices involved in your use does not have a user interface (e.g. IoT, drones, autonomous driving, etc.), you will need to use the backend authorization flow, following the OIDC standard **CIBA** (Client-Initiated Backchannel Authentication Flow). 

	[Backend authorization flow](/docs/backend)

Your Channel Partner of choice may provide you with SDKs or implement these flows for you in your application. When using them, such SDKs abstract you from the details of this flows while they still occur under the hood.

More on this in the [API integration guide](/docs/apiintegration). Refer to your Channel Partner for available SDKs and their specifications and conditions.

## Consent capture

In case the lawful basis of the Open Gateway API and the purpose of your use case require the end-user's explicit consent, you will need to capture it during the authorization flow. The consent capture is a mandatory step in the authorization process, and it will be launched by the operator's authorization server during the flow. If your 3-legged access token, once gotten, refers to an scope and purpose not consent granted by the end-user, the operator, as the data controller, will reject the access to the data.

[More on this in the Privacy guide](/docs/privacy).

The frontend authorization flow, as per the OIDC standard, will redirect your request to the operator's consent capture URL if needed, and then resume all the way to your application's redirect URI according to the user event.

In case of implementing a backend authorization flow, there is no standard way to make the operator subscriber to get to a consent capture frontend, so you will have to implement a secondary flow, known as out-of-band, to capture the consent by other mean, so when your backend calls the Open Gateway API the user consent has been already granted. This secondary flow will usually be a registration, subscription or activation process on your customer journey, or similar.