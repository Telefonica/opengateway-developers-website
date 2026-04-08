---
title: Age Verification API
category:
  uri: API Catalog
content:
  excerpt: >-
    The Age Verification API lets businesses determine whether a user is above
    the required age threshold for regulated services using mobile
    operator-verified data.
---

<div style={{display: 'flex', gap: '8px', marginBottom: '15px'}}>
  <span style={{backgroundColor: '#f0f0f0', border: '1px solid #ccc', borderRadius: '15px', padding: '4px 12px', fontSize: '12px', fontWeight: 'bold', color: '#666'}}>Under CAMARA project</span>
  <span style={{backgroundColor: '#8a8a8a', color: 'white', borderRadius: '15px', padding: '4px 12px', fontSize: '12px', fontWeight: 'bold'}}>GSMA Certified API</span>
</div>

The standardized Age Verification API allows you to determine whether a user is over the age required to access subscriptions that require it by regulation, using data verified by the mobile operator.

It is essential in regulated sectors such as online gambling, alcohol sales, or age-restricted digital media to block unauthorized access and eliminate fake accounts. The Age Verification API helps to do this privately and in real time.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.



## Overview of the Age Verification API

### High level definition

The Age Verification CAMARA API enables businesses to verify whether a user meets a specified age threshold by relying on verified data collected and maintained by mobile network operators during SIM registration or customer account setup.

### API Operations

Check the API reference to explore Age Verification integration details.

[Check the API reference](https://developers.opengateway.telefonica.com/reference/verifyage)

## Why Age Verification?

The Age Verification API helps businesses identify age thresholds of mobile line users in real-time, ensuring compliance with regulatory requirements while maintaining user privacy and streamlining verification processes.

### Process Simplification

Eliminates the need for users to submit identification photos or undergo biometric controls during initial interactions by leveraging verified data from mobile operators to confirm age instantly. This reduces friction in user onboarding while maintaining security and compliance.

### Trust and Traceability

Leverages data collected and verified by mobile operators during SIM card registration or customer account setup. This ensures age confirmation is based on a reliable, law-compliant source rather than user-provided data, reducing the risk of fraud and false information.

### Real-time Verification

Ideal for user verification, access control, and handling large transaction volumes without the common problems associated with document or image verification. Provides instant results that can be integrated into existing workflows seamlessly.

### Configurable Thresholds

The API allows adjustment of minimum age requirements (such as 18 or 21 years) according to business needs, industry requirements, or local laws. Verifications adapt to each market and include user-defined filters to improve accuracy and avoid incorrect results.

### Standardized Access

The CAMARA-standardized Age Verification API enables single integration to work with operators worldwide, without the need for custom agreements. This standardization simplifies development and reduces integration complexity across multiple markets.

### Privacy by Design

Uses only necessary data: indicates whether a person meets the minimum age requirement (e.g., 18 years) without sharing their birth date, documents, or other personal data. This better protects confidential information while ensuring compliance with privacy regulations.

### Enhanced Security Features

The API can optionally provide additional security information including:

- **Identity Match Score**: Indicates confidence level in the verification result
- **Verified Status**: Shows if information has been verified against legally accepted identification documents  
- **Content Lock**: Indicates if the subscription has content filtering enabled
- **Parental Control**: Shows if parental control features are activated

### Fraud Prevention

By utilizing verified operator data rather than user-submitted information, the API significantly reduces the risk of identity fraud, synthetic identities, and account manipulation commonly associated with traditional age verification methods.
