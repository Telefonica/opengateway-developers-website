---
title: Glossary of Terms
excerpt: Reference guide to key terms and concepts used in the Open Gateway API documentation
category: 6810d600713e0a001a963871
version: 0
---

## Aggregator
Aggregator or ‘Channel Partners’ aggregate Operator’s CAMARA standardized APIs to build Open Gateway-based services and implement Operator end-point routing based on final user identification on the network.

## API Gateway
An intermediary platform that allows communication between different systems and APIs, providing a centralized and standardized approach for accessing and utilizing APIs. The Open Gateway operator platform is the API GW platform in the operator that exposes standardized APIs so third-party services can consume them in a secure and consistent way. Operator platform APIs are based on REST/HTTP. OAuth 2.0 and OpenID Connect are standard security mechanisms to control access to the APIs. APIs are reachable from the Internet and all traffic is encrypted with TLS.

## AuthCode
Authentication method to validate the user's identity during the authentication process.

## CAMARA
CAMARA is an open-source project within Linux Foundation to define, develop and test the APIs. CAMARA works in close collaboration with the GSMA Operator Platform Group to align API requirements and publish API definitions and APIs. Harmonization of APIs is achieved through fast and agile created working code with developer-friendly documentation. API definitions and reference implementations are free to use (Apache2.0 license). The tool to manage the work and outcomes of the APIs standardization at CAMARA is GitHub: [https://github.com/camaraproject](https://github.com/camaraproject)

## CIBA
CIBA (Client-Initiated Backchannel Authentication) is a type of authentication that allows applications to authenticate a user asynchronously, meaning the user does not need to directly interact with their credentials. In Open Gateway, it is used for backend authentication flows. For more details, you can refer to the [backend authentication guide](https://developers.opengateway.telefonica.com/docs/backend).

## SIM Swap
This refers to the act of asking a telco operator for a new SIM card arguing that the original one has been lost, damaged, or stolen. When the new SIM card begins to be in force, the old one becomes invalid, and it is said that a SIM swap has happened. This can be a legitimate action. But this API helps to detect whether it happens due to an illegitimate action or not.

## Consent
The explicit permission given by the user for the processing of their personal data, as required by privacy regulations such as GDPR (General Data Protection Regulation).

## IDP
Identity Provider, a service that authenticates and verifies the identity of users.

## Open Gateway
An industry initiative led by GSMA (Global System for Mobile Communications Association) that transforms telecom networks into future-ready platforms, enabling seamless integration and access to telco capabilities through standardized APIs.

## Open Code Repository
A platform or repository where developers can access and collaborate on open-source code and projects, such as GitHub.

## OAuth 2.0 / OpenID Connect
Standards and protocols for user authentication and authorization, allowing secure access to APIs and services.

## Privacy-by-Default
A principle that ensures privacy protection is integrated into systems and processes by default, requiring explicit user consent for the processing of personal data.

## SDK
Software Development Kit, a set of tools, libraries, and documentation that enables developers to build applications for a specific platform or system.

## User Identifier
A unique identifier associated with a user, such as an IP address or MSISDN, used for authentication, routing, and identification purposes.
