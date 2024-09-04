---
title: 🕵🏽‍♀️ Privacy by Design
excerpt: Open Gateway as an industry initiative has been designed with end-user's privacy in mind, to provide developers with telco capabilities while ensuring user data privacy and security.
category: 66840b9dac745a002559ffad
---

# Privacy at Open Gateway

Several Open Gateway APIs allow developers or applications to access and utilize personal information or data. "Utilizing" personal data encompasses any form of handling or processing related to an identified or identifiable individual, including merely viewing the data. Consequently, the use of personal data must be justified and authorized.

To manage access to personal data, **consuming an Open Gateway API requires the use of an access token**. This mechanism ensures that the consuming application securely accesses the data exposed by the API and accurately identifies the specific data being accessed.

The access token allows to track the data consumption, ensure the proper privacy management (e.g., validating if the customer has rights to access) and gives the possibility to directly provide subscribers control over the access to their data, enabling consent capture/revoking mechanisms. 

That is why the developer/application shall first request a valid access token that identifies:
- Data (what) that is going to be accessed.
- Purpose (for what), reason why the data is going to be accessed.
- 3-legged identification of the parties interacting:
    - Data consumer: Application.
    - Data provider: Operator.
    - Data owner/origin: Network Subscriber

Legitimizing the access to personal data can imply multiple procedures, that shall be validated by the operator during the access token retrieval. There are two options: explicit consent and legitimate interest.

For the first one, **explicit consent**, the capture procedure of such consent may be launched during the token
creation, ensuring that the subscriber/user is identified and can clearly confirm or reject the access to the data

In the case **legitimate interest** applies to this API, this is a decision to be taken by the Telco Operator according to its legal/privacy assessment in the context of the country or region where it is operating. A Legitimate Interest lawful basis does not require explicit consent, but it may be necessary to inform the subscriber about the usage of their location information, and a way for the subscriber to revoke that usage may also be needed. Finally, the Telco Operator may have to implement the proper channels and procedures to manage the lawful basis by its subscribers.