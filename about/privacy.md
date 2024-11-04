---
title: Privacy by Design
excerpt: Open Gateway as an industry initiative has been designed with end-user's privacy in mind, to provide developers with telco capabilities while ensuring user data privacy and security.
category: 66840b9dac745a002559ffad
---

> 📘 To try out our APIs, visit the [Sandbox](https://opengateway.telefonica.com/developer-hub/unirse).

Open Gateway APIs allow applications to access and utilize end-users' personal information or data. "Utilizing" personal data encompasses any form of handling or processing related to an identified or identifiable individual, including merely viewing the data or having it accesible from the application's code and thus to its developer. Consequently, **the use of personal data must be justified and authorized**.

Open Gateway as an initiative from the telco companies has been designed with their subscribers, the applications’ end-users, privacy in mind.

To manage access to personal data, consuming an Open Gateway API requires the use of a **3-legged access token** for every purpose. The authorization mechanism for providing it ensures that the consuming application securely accesses the data exposed by the API and accurately identifies the specific data being accessed and the reason to do so, so the user can have full control over their personal information.

The access token allows to track the data consumption, ensure the proper privacy management (e.g., validating if the consumer has rights to access) and gives the possibility to directly provide operators' subscribers with tools for checking what the access to their data is and consent or revoke it.

That is why each developer's application shall first request a valid access token that identifies:
- **Scope** (what) that is going to be accessed.
- **Purpose** (for what), reason why the data is going to be accessed.
- **3-legged identification** of the parties interacting:
    - Data consumer: the application
    - Data controller: the operator
    - Data owner: the end-user and operator subscriber

Legitimizing the access to personal data can imply multiple procedures, that shall be validated by the operator during the access token retrieval.

These are the main, but not only, lawful bases than can apply:

- **Explicit Consent** from the end user, the capture of which must be launched during the token creation, ensuring that the user is identified and can clearly confirm or reject the access to the data. Once the consent is granted by the user, it applies to the specific application, scope and purpose for which it was requested for a period, during which it is not necessary to launch the capture again. If the use case of the application does not involve an end-user interface, the consent must be captured by the operator through other means, also known as out-of-band, previous to API consumption.

- **Legitimate Interest** of the operator, which is determined by the operator according to its legal and privacy assessment in the context of the country or region where it is operating. A Legitimate Interest lawful basis does not require explicit consent from the user, but it is necessary to inform the subscriber about the scope and purpose of the usage of their personal information.

No matter what the lawful basis is, operators must implement the proper channels and procedures for their subscribers to be able to check and revoke their consent for every application, scope or purpose.
