---
title: QoD Wifi
excerpt: The QoD API allows the developer to prioritize network traffic on certain devices on demand.
category: 66aa4f941e51e7000fa353ce
---

An example of an application that aims to enrich the public experience when attending a live sporting event, an advanced feature for your viewers may be watching replays of relevant games. 

To do this, the application must ensure that the end user has adequate connectivity to watch it, regardless of the
number of simultaneous users watching the sporting event in the same location. 

## Overview of the QoD Wifi CAMARA API

### High level definition

The QoD Wifi CAMARA API is a software interface that enable application developers to integrate network configuration and optimization functionalities into their software, without the need for the End Users to run complex processes on their devices.

This functionality easily allows applications to gain the ability to interact seamlessly with mobile network operator systems, so developers can focus on provide a better user experience.

### API Operations

The SIM Swap CAMARA API specifies the following two operations:

- **POST retrieve-date:** Answers the question ‘when did the last SIM swap occur?’. This operation requires the phone number to be checked (parameter `phoneNumber`).

  [Check the API Reference](/reference/retrievesimswapdate)

- **POST check:** Checks whether a SIM swap occurred during the last N hours. This operation requires the following inputs:
  - `phoneNumber`: The phone number to be checked.
  - `maxAge`: The period in hours to be checked for a SIM swap (minimum 1 hour, maximum 2400 hours, default 240 hours).

  [Check the API Reference](/reference/checksimswap)

With the SIM Swap CAMARA API, any digital service provider can integrate the functionality of checking changes in SIM renewals directly into their software. This can be done both alone and in combination with other external inputs. Additionally, they can combine other Open Gateway APIs related to anti-fraud measures that may be of interest.

Aggregators play a crucial role in the anti-fraud industry. They can integrate this functionality into their software and build more sophisticated algorithms by combining other security checks, such as location verification, phone number verification, matching of contact information, external data sources, AI algorithms, etc. To achieve this, aggregators can use other Open Gateway APIs like Device Location Verification, Number Verification, or KYC-Match.

By using the SIM Swap CAMARA API, developers can significantly enhance the security and reliability of their applications, providing a robust defense against SIM swap fraud.

## Why Sim Swap?

### Understanding SIM Swap Fraud

SIM Swap is a serious form of account takeover fraud. Your mobile phone is the most common device used to manage a wide range of products and services – from food delivery or gym accounts to car insurance or bank accounts. Each of these services requires a personal account to perform various transactions.

Account takeover fraud is one of the most impactful types of cybercrime. When a fraudster gains control of a user's account, they can exploit all the functionalities associated with that account. The quickest way to monetize this fraud is by transferring money or making purchases. However, other severe consequences can occur, such as implicating the real customer in criminal activities.

### How SIM Cards are Used by Telecom Operators

A SIM card is a small card inside your mobile phone, identified by a unique number. Telecom operators maintain a link between this number and your phone number. If your phone number is linked to a different SIM card, phone calls and SMS messages intended for you will be redirected to another mobile phone.

This is where SIM swap fraud becomes dangerous. The "new" mobile phone can be used to reset passwords and validate fraudulent transactions. Essentially, this allows the fraudster to take over your accounts and misuse them for malicious purposes.

### Protecting Against SIM Swap Fraud

To safeguard against SIM swap fraud, it is crucial to be aware of how your personal and financial information is used and protected. Use strong, unique passwords for your accounts, enable two-factor authentication, and monitor your accounts for any suspicious activity. Always be cautious of unsolicited requests for personal information, whether over the phone, via SMS, or through email.

By understanding the mechanics of SIM swap fraud and taking proactive steps to protect your accounts, you can significantly reduce the risk of falling victim to this type of cybercrime.

