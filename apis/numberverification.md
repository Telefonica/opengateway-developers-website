# Open Gateway's Number Verification API

Discover the **Number Verification API**, a pivotal tool for bolstering security and reliability in your applications. In today's digital landscape, verifying the authenticity of phone numbers is paramount for safeguarding against fraud and ensuring seamless user interactions. The Number Verification API offers a streamlined **solution to validate phone numbers in real-time**, empowering developers to implement robust identity verification mechanisms with ease.

Built as part of the **Open Gateway** initiative, the Number Verification API provides developers universal access to essential network functionalities. Whether you're enhancing user registration processes, securing transactions, or optimizing user engagement strategies, integrating the Number Verification API enriches your application's security posture while ensuring a seamless user experience.

##  Why Number Verification?

In today's digital landscape, verifying phone number ownership is critical to prevent identity fraud and secure online transactions. The Number Verification CAMARA API offers a reliable solution to **authenticate users by confirming their phone numbers**. This ensures that only legitimate users gain access to digital services, bolstering security measures and building trust among customers.

### Digital Identity and Authentication

Digital identity refers to the electronic representation of an individual or organization, encompassing digitally stored identifying characteristics exchanged during electronic transactions. These characteristics uniquely and specifically identify a person or legal entity. Unlike physical IDs such as passports, digital identities enable remote authentication over digital channels. They track activities, collect personal data, and validate individuals accessing services. Trust between parties—services, application providers, or users—is crucial in digital identity and electronic transactions, underpinned by authenticity and reliability.

### Multi-Factor Authentication

To access digital services, users must authenticate themselves on the provider’s website/app using credentials. Authentication factors are categories of evidence proving identity, such as usernames/passwords, national IDs, or phone numbers. The three main authentication factors are:

- **Knowledge Factor:** Information known to the user (e.g., username/password).
- **Possession Factor:** Physical possession of something (e.g., mobile phone).
- **Inherence Factor:** Inherent physical characteristics (e.g., fingerprint).

While individual authentication factors may have vulnerabilities, using multiple factors enhances security. Knowledge-based factors like passwords can be weak due to user habits or technology limitations. Biometric and possession-based factors offer stronger security against unauthorized access. Combining these factors in multi-factor authentication processes significantly reduces the risk of hacking attempts.


### Seamless and Transparent Authentication Using Network Connection

Smartphones have become indispensable for accessing digital services, managing everything from food delivery to banking. Leveraging smartphones as a possession factor in authentication systems is convenient for users accustomed to multi-factor authentication.

Currently, SMS One-time Passwords (OTPs) are widely used for possession authentication due to their simplicity and integration with existing SMS delivery systems. However, SMS OTPs rely on the assumption that users can receive and manually input the code, which introduces several challenges:

- **Number Verification Process:** Users confirm ownership of their registered phone number by receiving and entering an SMS OTP.
- **Possession Factor Validation:** Users demonstrate possession of the registered phone number by inputting the SMS OTP.

Despite its widespread use, SMS OTPs pose security risks such as SIM Swapping and lack of encryption for transmitted codes. These factors contribute to a non-transparent user experience and potential security vulnerabilities.

To address these issues, new solutions leverage carrier network-based technology for robust authentication. When users power on their phones, devices and SIM cards automatically connect to and authenticate through the carrier network without user intervention. This approach ensures secure, frictionless authentication, leveraging mobile network capabilities for enhanced security and user experience compared to traditional methods.

### How does the Number Verification API help to facilitate authentication? 

The Number Verification API utilizes telco mechanisms to authenticate users seamlessly based on their device's connection to the network. This method contrasts with traditional authentication solutions by enhancing user convenience and security. Unlike manual processes or plain-text codes, network-based validation requires no user interaction, bolstering protection against unauthorized access.

This API verifies that the provided mobile phone number (MSISDN) matches the device initiating data communication, ensuring users interact with digital services from authenticated devices.

# Overview of the Number Verification CAMARA API

## High level definition of the Number Verification CAMARA API

The Number Verification CAMARA API validates user identity by confirming ownership of the phone number being registered, matching it with the number identified by the operator through the user’s device connection. It facilitates two primary operations:

- **POST verify:** Determines if the provided phone number matches the one currently in use by the user (parameter `phoneNumber`). This operation is ideal for user authentication.
  
- **GET device-phone-number:** Identifies the phone number currently associated with the user's device without requiring input, providing a straightforward way to retrieve this information.

The Number Verification CAMARA API enables developers to seamlessly integrate authentication mechanisms into their applications, enhancing the user experience and security. It can also be combined with other Open Gateway APIs focused on anti-fraud measures to further bolster security.

Integration with channel partners and service aggregators streamlines the incorporation of telco functionalities with additional security algorithms, backup authentication methods, or external data sources. This collaboration enhances service reliability and security, leveraging APIs like Device Location Verification or SIM SWAP within the Open Gateway framework.


## Advantages of the CAMARA Number Verification API

The CAMARA Number Verification API offers significant advantages for industries focused on enhancing identity protection. Here are key benefits that highlight why the CAMARA API is essential:

1. **Secure Authentication and Identity Validation:** Utilizes network mechanisms instead of less secure Over the Top (OTT) methods or hardware tokens. It operates on any internet-enabled mobile device connected to a carrier's mobile data network, including during roaming and temporary Wi-Fi transitions.

2. **Improved User Experience:** Eliminates the need to copy, paste, or remember one-time passwords sent via SMS, thereby enhancing both security and user convenience during validation processes.

3. **Anti-Fraud Suite:** Number Verification is part of the broader suite of Open Gateway APIs dedicated to protecting customer identities in mobile digital services. APIs like SIM SWAP, Device Location Verification, and Know Your Customer - Match complement Number Verification to strengthen security across different scenarios.

4. **Usability:** CAMARA APIs are designed with developer-friendliness in mind, simplifying integration for telcos and various clients. This streamlined integration enables service providers to offer Number Verification seamlessly as an authentication option for users.

5. **Footprint:** CAMARA's standardized approach to Number Verification ensures universal access to this functionality across telco operators and countries, promoting consistency and reliability.

6. **Security:** CAMARA guidelines establish a common privacy and security framework that addresses service providers' needs while safeguarding customer rights.

By leveraging the CAMARA Number Verification API, industries can enhance security, improve user experiences, and mitigate identity fraud risks effectively.
