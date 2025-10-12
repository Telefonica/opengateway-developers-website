---
title: Tenure API
excerpt: The Tenure API enables businesses to verify the length of customer tenure with mobile network operators, establishing trust and reliability scores for network subscription identifiers based on account history and longevity.
category: 681879c3afc1a0003709c745
---

The Tenure API provides businesses with the ability to verify and assess the length of tenure of mobile network subscribers, offering valuable insights into customer reliability and account stability. By leveraging verified data from mobile network operators, this API enables informed decision-making for fraud prevention, risk assessment, and customer onboarding processes.

This API is particularly valuable for financial services, digital platforms, and any business requiring additional verification layers to establish customer trustworthiness based on their mobile subscription history and account longevity.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.



## Overview of the Tenure API

### High level definition

The Tenure CAMARA API is a software interface that enables businesses to verify a specified length of tenure for a network subscriber based on a provided date, establishing a level of trust for the network subscription identifier through historical account data validation.

### API Operations

The Tenure CAMARA API specifies one operation:

- **POST /check-tenure**: Verifies continuous tenure of an identified mobile subscriber from a specified date, returning boolean confirmation and optional contract type information (PAYG, PAYM, or Business).

[Check the API Reference](https://developers.opengateway.telefonica.com/reference/checktenure)

## Why Tenure?

The Tenure API helps businesses assess customer reliability and establish trust levels by leveraging mobile network operator data about subscription longevity and account stability. This enables more informed decision-making in various business processes while maintaining privacy and compliance.

### Enhanced Risk Assessment

Tenure information provides valuable insights into customer stability and reliability. Longer tenure periods generally indicate more established and trustworthy customers, enabling businesses to make informed decisions about credit scoring, fraud prevention, and customer segmentation strategies.

### Fraud Prevention

Account tenure serves as a powerful indicator in fraud detection systems. New or recently activated accounts often present higher fraud risks, while established accounts with long tenure histories demonstrate legitimacy and reduced fraud probability, helping businesses implement more effective security measures.

### Customer Onboarding Optimization

Streamline customer onboarding processes by using tenure data to determine appropriate verification levels and service offerings. Established customers with proven tenure may qualify for expedited processes, while newer accounts can receive additional verification steps as needed.

### Financial Services Applications

Essential for financial institutions and fintech companies requiring customer reliability assessments. Tenure data supports:

- **Credit Risk Evaluation**: Incorporate subscription longevity into credit scoring models
- **Account Opening Decisions**: Make informed decisions about new account approvals
- **Loan Underwriting**: Use tenure as an additional factor in lending decisions
- **Insurance Assessments**: Factor account stability into risk calculations

### Contract Type Intelligence

The API provides optional contract type information when available:

- **PAYG (Pay-As-You-Go)**: Prepaid account holders
- **PAYM (Pay Monthly)**: Contract account customers  
- **Business**: Enterprise or business account types

This information enables more nuanced customer profiling and targeted service offerings based on account characteristics and payment preferences.

### Privacy-Compliant Verification

Delivers tenure verification while maintaining strict privacy standards. The API provides only essential information (tenure confirmation and contract type) without exposing sensitive personal details, ensuring compliance with data protection regulations.

### Standardized Integration

Built on CAMARA standards, the Tenure API offers consistent integration across multiple mobile network operators worldwide. This standardization reduces development complexity and enables broad market coverage through a single API implementation.

### Real-time Verification

Provides instant tenure verification results that can be seamlessly integrated into existing business workflows, transaction processing systems, and customer onboarding platforms without introducing delays or friction.

### Trust Scoring Enhancement

Tenure data can be incorporated into comprehensive trust scoring systems alongside other verification APIs such as:

- **Number Verification**: Confirm device ownership
- **Age Verification**: Verify age requirements  
- **KYC Match**: Validate customer identity data
- **Device Location**: Confirm geographic presence

### Compliance and Regulatory Support

Helps businesses meet regulatory requirements for customer due diligence and know-your-customer (KYC) processes by providing verified data from authoritative sources. Particularly valuable in regulated industries requiring enhanced customer verification.
