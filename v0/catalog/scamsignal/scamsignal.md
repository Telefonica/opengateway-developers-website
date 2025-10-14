---
title: Scam Signal API
category:
  uri: API Catalog
content:
  excerpt: >-
    The Scam Signal API provides advanced fraud detection capabilities
    leveraging telco network intelligence to identify and prevent fraudulent
    activities in real-time, protecting businesses and their customers from
    evolving threats.
---

The Scam Signal API leverages mobile network operator intelligence to detect and prevent Authorized Push Payment (APP) fraud in real-time. By analyzing network patterns during transaction attempts, this API enables financial institutions to identify when customers are under active social engineering pressure and intervene before fraud completion.

Specifically designed for the critical detection window between fraud initiation and payment completion, Scam Signal has demonstrated proven effectiveness with early deployments reporting up to **41% reduction in successful scams** and **44% decrease in fraud losses**.

> 📘 Want to learn more about implementation?
> [Contact our Expert Team](https://opengateway.telefonica.com/contactoexperto) to discuss technical implementation details and access requirements.

## Overview of the Scam Signal API

### High level definition

The Scam Signal CAMARA API provides real-time fraud detection by analyzing telco network signals to identify when customers are being manipulated during payment transactions. The API enables financial institutions to detect ongoing social engineering attacks and implement immediate protective measures.

### API Operations

The Scam Signal API delivers risk assessment capabilities through secure endpoints that analyze network metadata without accessing call content, ensuring privacy compliance while detecting fraud indicators.

**Available through expert consultation:**
- Real-time fraud scoring methodologies
- Integration patterns for existing fraud prevention systems
- Customization options for specific use cases and risk thresholds
- Performance benchmarks and accuracy metrics

## Why Scam Signal?

Traditional fraud detection systems struggle against Authorized Push Payment (APP) fraud because victims authorize legitimate transactions while under social engineering manipulation. Scam Signal addresses this critical gap by detecting the manipulation itself during the transaction window.

### Authorized Push Payment Fraud Targeting

APP fraud encompasses sophisticated social engineering attacks where criminals manipulate victims into authorizing payments to fraudulent accounts:

- **Bank Impersonation**: False security alerts requiring immediate fund transfers
- **CEO Fraud**: Business email compromise targeting corporate finance teams
- **Investment Scams**: Fake opportunities requiring urgent investment payments
- **Romance Fraud**: Manipulated relationships leading to financial requests
- **Vendor Impersonation**: Fake suppliers demanding payment redirections

### How APP Fraud Unfolds

Authorized Push Payment fraud operates through sophisticated social engineering where criminals manipulate victims during live interactions:

1. **Initial Contact**: Fraudsters impersonate trusted entities (banks, government agencies, family members) via phone, email, or messaging
2. **Psychological Pressure**: Create urgency through fake emergencies, security alerts, or time-sensitive investment opportunities  
3. **Transaction Coaching**: Guide victims through legitimate banking processes while maintaining psychological control
4. **Real-time Manipulation**: Continue coaching during payment execution to overcome security prompts and verification steps

**Critical Detection Window**: The period between fraud initiation and payment completion represents the optimal intervention opportunity.

### Real-time Detection Capabilities

**Live Fraud Identification**: Analyzes network signals to detect ongoing social engineering during payment attempts, enabling immediate intervention before transaction completion.

**Network Intelligence**: Leverages unique telco insights including call patterns, device behavior, and network metadata to identify manipulation indicators without accessing conversation content.

**Enhanced Fraud Models**: Integrates telco intelligence with existing fraud prevention systems, reducing false positives by **55%** while improving detection accuracy against sophisticated social engineering attacks.

**Adaptive Learning**: Continuously evolves to recognize new fraud patterns and criminal methodologies, staying ahead of emerging social engineering tactics.

**Privacy-Compliant Analysis**: Processes network metadata without accessing call content or personal communications, ensuring regulatory compliance while maintaining detection effectiveness.

### Implementation Scenarios

**Retail Banking Transaction Flow**:
When a customer initiates a high-value or unusual transfer, the bank's fraud system queries Scam Signal API to analyze concurrent network activity. If scam indicators are detected, the system can:
- Immediately pause the transaction pending verification
- Display targeted fraud awareness messages  
- Redirect customers to secure verification channels
- Trigger human agent intervention protocols

**Corporate Banking Protection**:
Wire transfer requests showing scam indicators automatically initiate enhanced verification procedures. For example, when a finance officer receives an "urgent CEO directive" for immediate payment, the system detects manipulation signals and suggests mandatory call-back verification using predetermined contact methods.

**Payment Platform Integration**:
Mobile payment apps, digital wallets, and peer-to-peer transfer services integrate real-time scam detection into existing fraud prevention workflows, enabling dynamic risk scoring adjustments based on social engineering indicators.

### Advanced Security Features

**Multi-Vector Analysis**: Combines network intelligence with transaction patterns, device behavior, and timing analysis to create comprehensive fraud risk profiles.

**Dynamic Risk Scoring**: Adjusts fraud confidence levels in real-time based on evolving network signals and behavioral indicators during transaction attempts.

**Intervention Flexibility**: Provides configurable response options from soft warnings to hard transaction blocks, allowing institutions to balance security with customer experience.

**Cross-Channel Protection**: Monitors fraud indicators across voice calls, SMS, messaging apps, and other communication channels used in social engineering attacks.

## Proven Business Impact

### Quantified Results
Early deployments in UK financial institutions demonstrate significant fraud reduction:
- **41% reduction** in successful scam completions
- **44% decrease** in financial fraud losses  
- **55% fewer false positives** improving operational efficiency

### Integration Benefits

**Real-time Protection**: Immediate intervention at the critical moment of fraud attempt, during the narrow window between manipulation and payment completion.

**Enhanced Accuracy**: Reduces false positives while improving genuine fraud detection through unique telco intelligence unavailable to traditional fraud prevention systems.

**Operational Efficiency**: Focuses human review resources on genuine threats rather than false alarms, improving fraud team productivity and response times.

**Customer Experience**: Protects legitimate customers from sophisticated manipulation while maintaining smooth transaction flows for authentic payments.

**Regulatory Compliance**: Supports PSD2 Strong Customer Authentication, AML requirements, and emerging APP fraud prevention regulations across multiple jurisdictions.

**Seamless Deployment**: RESTful API design enables integration with existing fraud prevention platforms, transaction monitoring systems, and decisioning engines without infrastructure changes.

### Target Industries

**Financial Services**: Banks, credit unions, and payment processors requiring enhanced APP fraud protection during money transfers and high-risk transactions.

**Fintech Platforms**: Mobile payment applications, digital wallets, and peer-to-peer services seeking advanced fraud detection capabilities.

**Corporate Banking**: Enterprise treasury management systems protecting against business email compromise and vendor impersonation fraud targeting corporate accounts and supplier payment processes.

### Fraud Prevention Ecosystem Integration

Scam Signal enhances existing fraud prevention capabilities by adding unique telco intelligence that complements traditional detection methods:

**Enhanced with Other Open Gateway APIs**:
- **SIM Swap Detection**: Identify recent SIM changes that may indicate account compromise
- **Number Verification**: Confirm device ownership during suspicious transaction attempts  
- **Device Location**: Validate geographic consistency with expected user patterns
- **KYC Match**: Cross-reference identity verification data for additional fraud indicators

**Traditional Fraud Tool Enhancement**:
- **Behavioral Analytics**: Add social engineering pressure indicators to user behavior models
- **Transaction Monitoring**: Enrich payment risk scoring with real-time communication analysis
- **Identity Verification**: Supplement know-your-customer processes with live manipulation detection
- **Risk Scoring Engines**: Integrate telco intelligence for more accurate fraud probability calculations

### Regulatory and Compliance Framework

**PSD2 Compliance**: Supports Strong Customer Authentication requirements by providing additional fraud risk indicators during payment initiation and authorization processes.

**AML Enhancement**: Contributes to Anti-Money Laundering programs by detecting social engineering patterns often associated with money mule recruitment and transaction layering schemes.

**Data Protection**: Operates within GDPR and other privacy frameworks by analyzing network metadata without accessing personal communications content or sensitive customer information.

**Industry Standards**: Built following GSMA Open Gateway standards and CAMARA API specifications, ensuring consistent implementation across global mobile network operators.

## Technical Implementation

Due to the sophisticated nature of fraud detection algorithms and the need to maintain effectiveness against evolving criminal tactics, technical implementation details are available exclusively through direct expert consultation.

> 💡 **Ready to enhance your fraud prevention capabilities?**
> [Schedule a Technical Consultation](https://opengateway.telefonica.com/contactoexperto) with our Open Gateway team to discuss implementation requirements, integration patterns, and performance metrics tailored to your specific use case.
