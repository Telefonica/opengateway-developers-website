---
title: SIM Swap API
excerpt: The SIM Swap API from Open Gateway allows to check for SIM card swaps for fraud prevention purposes
category: 66aa4f941e51e7000fa353ce
---

The standardized SIM Swap API enables seamless integration of SIM swap detection and management functionality into your applications. This API enhances security by identifying potentially fraudulent activity and providing an additional layer of protection against unauthorized access.

Additionally, the SIM Swap's Unified API Access feature ensures access to network capabilities of various carriers through a single, standardized interface. This simplifies integration and improves efficiency for developers by consolidating access to multiple carrier networks.

## SIM Swap and Account Takeover Fraud

### Understanding SIM Swap Fraud

SIM Swap is a serious form of account takeover fraud. Your mobile phone is the most common device used to manage a wide range of products and services – from food delivery or gym accounts to car insurance or bank accounts. Each of these services requires a personal account to perform various transactions.

Account takeover fraud is one of the most impactful types of cybercrime. When a fraudster gains control of a user's account, they can exploit all the functionalities associated with that account. The quickest way to monetize this fraud is by transferring money or making purchases. However, other severe consequences can occur, such as implicating the real customer in criminal activities.

### How SIM Cards are Used by Telecom Operators

A SIM card is a small card inside your mobile phone, identified by a unique number. Telecom operators maintain a link between this number and your phone number. If your phone number is linked to a different SIM card, phone calls and SMS messages intended for you will be redirected to another mobile phone.

This is where SIM swap fraud becomes dangerous. The "new" mobile phone can be used to reset passwords and validate fraudulent transactions. Essentially, this allows the fraudster to take over your accounts and misuse them for malicious purposes.

### Protecting Against SIM Swap Fraud

To safeguard against SIM swap fraud, it is crucial to be aware of how your personal and financial information is used and protected. Use strong, unique passwords for your accounts, enable two-factor authentication, and monitor your accounts for any suspicious activity. Always be cautious of unsolicited requests for personal information, whether over the phone, via SMS, or through email.

By understanding the mechanics of SIM swap fraud and taking proactive steps to protect your accounts, you can significantly reduce the risk of falling victim to this type of cybercrime.


# Overview of the SIM Swap CAMARA API

## High level definition of the SIM Swap CAMARA API

The SIM Swap CAMARA API is a software interface that enables applications to request the last date of a SIM swap performed on a mobile line or to check whether a SIM swap has been performed during a specified period. This functionality is provided in an easy and secure manner, allowing real-time verification of the activation date of a SIM card on the mobile network.

### API Operations

The SIM Swap CAMARA API specifies the following two operations:

- **POST retrieve-date:** Answers the question ‘when did the last SIM swap occur?’. This operation requires the phone number to be checked (parameter `phoneNumber`).

- **POST check:** Checks whether a SIM swap occurred during the last N hours. This operation requires the following inputs:
  - `phoneNumber`: The phone number to be checked.
  - `maxAge`: The period in hours to be checked for a SIM swap (minimum 1 hour, maximum 2400 hours, default 240 hours).

With the SIM Swap CAMARA API, any digital service provider can integrate the functionality of checking changes in SIM renewals directly into their software. This can be done both alone and in combination with other external inputs. Additionally, they can combine other Open Gateway APIs related to anti-fraud measures that may be of interest.

Aggregators play a crucial role in the anti-fraud industry. They can integrate this functionality into their software and build more sophisticated algorithms by combining other security checks, such as location verification, phone number verification, matching of contact information, external data sources, AI algorithms, etc. To achieve this, aggregators can use other Open Gateway APIs like Device Location Verification, Number Verification, or KYC-Match.

## Advantages and Benefits of Using SIM Swap CAMARA API

The CAMARA SIM Swap API offers numerous advantages and benefits for the industry focused on enforcing identity protection. Here are some key arguments highlighting the advantages of using the CAMARA API:

1. **Two-Factor Authentication Reinforcement:** The SIM Swap API enhances the security of procedures involving two-factor authentication based on SMS. Verifying whether the mobile device used in the second factor has been compromised by a SIM swap protects your customer’s account and your business.

2. **Secure Account Creation:** The SIM Swap API allows for the detection of potentially fraudulent actions before creating new user accounts. This prevents unauthorized modifications of personal information, such as addresses or initiating password resets. This feature is crucial in sectors like banking transactions, e-commerce, and in-app purchases.

3. **Anti-Fraud Suite:** The SIM Swap API is part of a suite of Open Gateway APIs designed to protect customer identities in mobile digital services. Other APIs, such as Number Verification, Device Location Verification, and Know Your Customer - Match, can be used to enhance this protection in various scenarios.

4. **Usability:** The CAMARA API is developer-friendly, easy to set up, and use. It simplifies the integration process for telcos and clients of all kinds, allowing them to offer SIM Swap as an option to check SIM renewals.

5. **Footprint:** The standardization of SIM Swap through CAMARA guarantees common access to functionality across telco operators and countries.

6. **Security:** CAMARA guidelines ensure a common privacy and security framework that addresses the needs of service providers while preserving the rights of customers.

By using the SIM Swap CAMARA API, developers can significantly enhance the security and reliability of their applications, providing a robust defense against SIM swap fraud.
