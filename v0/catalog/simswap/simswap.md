---
title: SIM Swap API
category:
  uri: API Catalog
content:
  excerpt: >-
    The SIM Swap API from Open Gateway allows you to check for SIM card swaps for
    fraud prevention purposes
---

The standardized SIM Swap API enables seamless integration of SIM swap detection and management functionality into your applications. This API enhances security by identifying potentially fraudulent activity and providing an additional layer of protection against unauthorized access.

Additionally, the SIM Swap Unified API Access feature ensures access to network capabilities of various carriers through a single, standardized interface. This simplifies integration and improves efficiency for developers by consolidating access to multiple carrier networks.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

### Getting started on the Telefónica Open Gateway Sandbox

[![Digital Fraud Prevention with the SIM Swap API](https://i.ytimg.com/vi/Pdo-HnTyQ_E/hqdefault.jpg)](https://www.youtube.com/watch?v=Pdo-HnTyQ_E)

## Overview of the SIM Swap CAMARA API

### High level definition

The SIM Swap CAMARA API is a software interface that enables applications to request the last date of a SIM swap performed on a mobile line or to check whether a SIM swap has been performed during a specified period. This functionality is provided in an easy and secure manner, allowing real-time verification of the activation date of a SIM card on the mobile network.

### API Operations

The SIM Swap CAMARA API specifies the following two operations:

- **POST retrieve-date:** Answers the question ‘when did the last SIM swap occur?’. This operation requires the phone number to be checked (parameter `phoneNumber`).

  [Check the API Reference](/reference/retrievesimswapdate)

- **POST check:** Checks whether a SIM swap occurred during the last N hours. This operation requires the following inputs:
  - `phoneNumber`: The phone number to be checked.
  - `maxAge`: The period in hours to be checked for a SIM swap (minimum 1 hour, maximum 2400 hours, default 240 hours).

  [Check the API Reference](/reference/checksimswap)

## Why SIM Swap?

With the SIM Swap CAMARA API, any digital service provider can integrate the functionality of checking changes in SIM renewals directly into their software. This can be done independently or in combination with other external inputs. Additionally, they can combine other Open Gateway APIs related to anti-fraud measures that may be of interest.

Aggregators play a crucial role in the anti-fraud industry. They can integrate this functionality into their software and build more sophisticated algorithms by combining other security checks, such as location verification, phone number verification, matching of contact information, external data sources, AI algorithms, etc. To achieve this, aggregators can use other Open Gateway APIs like Device Location Verification, Number Verification, or KYC-Match.

By using the SIM Swap CAMARA API, developers can significantly enhance the security and reliability of their applications, providing a robust defense against SIM swap fraud.

![SIMSwap](https://github.com/Telefonica/opengateway-developers-website/raw/main/v0/catalog/simswap/images/SIMSwap.png)

### Understanding SIM Swap Fraud

SIM Swap is a serious form of account takeover fraud. Your mobile phone is the most common device used to manage a wide range of products and services – from food delivery or gym accounts to car insurance or bank accounts. Each of these services requires a personal account to perform various transactions.

Account takeover fraud is one of the most impactful types of cybercrime. When a fraudster gains control of a user's account, they can exploit all the functionalities associated with that account. The quickest way to monetize this fraud is by transferring money or making purchases. However, other severe consequences can occur, such as implicating the real customer in criminal activities.

### How SIM Cards are Used by Telecom Operators

A SIM card is a small card inside your mobile phone, identified by a unique number. Telecom operators maintain a link between this number and your phone number. If your phone number is linked to a different SIM card, phone calls and SMS messages intended for you will be redirected to another mobile phone.

This is where SIM swap fraud becomes dangerous. The "new" mobile phone can be used to reset passwords and validate fraudulent transactions. Essentially, this allows the fraudster to take over your accounts and misuse them for malicious purposes.

### Protecting Against SIM Swap Fraud

To safeguard against SIM swap fraud, it is crucial to be aware of how your personal and financial information is used and protected. Use strong, unique passwords for your accounts, enable two-factor authentication, and monitor your accounts for any suspicious activity. Always be cautious of unsolicited requests for personal information, whether over the phone, via SMS, or through email.

By understanding the mechanics of SIM swap fraud and taking proactive steps to protect your accounts, you can significantly reduce the risk of falling victim to this type of cybercrime.
