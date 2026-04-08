---
title: SIM Swap API
category:
  uri: API Catalog
content:
  excerpt: >-
    The SIM Swap API lets you detect SIM exchange events for fraud prevention
    and stronger account protection.
---

<div style={{display: 'flex', gap: '8px', marginBottom: '15px'}}>
  <span style={{backgroundColor: '#f0f0f0', border: '1px solid #ccc', borderRadius: '15px', padding: '4px 12px', fontSize: '12px', fontWeight: 'bold', color: '#666'}}>Under CAMARA project</span>
  <span style={{backgroundColor: '#8a8a8a', color: 'white', borderRadius: '15px', padding: '4px 12px', fontSize: '12px', fontWeight: 'bold'}}>GSMA Certified API</span>
</div>

The standardised SIM Swap API allows you to integrate SIM swap detection and management functionality into your applications, enhancing security by identifying potentially fraudulent activity and providing an additional layer of protection.

This solution leverages data from the carrier's network, allowing the protocols and security measures of any service to be adjusted quickly and proportionately.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

### Getting started on the Telefónica Open Gateway Sandbox

<iframe  
  width="560"  
  height="315"  
  src="https://www.youtube.com/embed/Pdo-HnTyQ_E?si=8ikNlfQqz36U_vJ8"  
  title="YouTube video player"  
  frameborder="0"  
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  
  referrerpolicy="strict-origin-when-cross-origin"  
  allowfullscreen>
</iframe>

## Overview of the SIM Swap CAMARA API

### High level definition

The SIM Swap CAMARA API enables applications to check whether a SIM swap occurred recently on a mobile line, allowing real-time verification of suspicious SIM exchange events.

### API Operations

Check the API reference to explore SIM Swap integration details.

[Check the API reference](https://developers.opengateway.telefonica.com/reference/checksimswap)

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
