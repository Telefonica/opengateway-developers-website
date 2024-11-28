---
title: Know Your Customer API
excerpt: The Know Your Customer API makes it possible to validates users info with MNO (Mobile Network Operator) data, ensuring compliance and preventing identity fraud.
category: 66aa4f941e51e7000fa353ce
---

The standardised Know Your Customer API allows you to validate user contact information against data from Mobile Network Operators (MNOs), ensuring accuracy and improving both conversion rates and the quality of user onboarding for new services.

This API provides a quick and efficient method to verify customer contact details, helping you prevent identity fraud, including synthetic identities and identity theft. Additionally, by utilizing this standardized API, you can expand your user reach across multiple MNOs.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub) and gain access to our Sandbox.

## Overview of the Know Your Customer API

### High level definition

The Know Your Customer CAMARA API is a software interface that enables a requester to check if an user data is correct or not making a check with the mobile network operator records. 

### API Operations

The Know Your Customer Camara API specifies one operation:

- **POST /match**: answers the question 'is this informacion true?'

[Check the API Reference](/reference/kyc_match)

## Why Know Your Customer?

This API provides a streamlined solution for accessing network capabilities across various operators. By offering a single, standardized interface, it simplifies the integration process and reduces the complexity associated with managing multiple operator-specific APIs. This unified access not only saves development time and resources but also ensures consistent performance and reliability across different network environments. As a result, businesses can focus on delivering high-quality services without worrying about the underlying network intricacies.

### Fraud prevention

Utilizing the KYC-Match API helps mitigate risks associated with your customers’ identities, including synthetic identity fraud and fraudulent transactions stemming from identity theft.

###  Conversion rate and ​high-quality users

The API enhances the conversion rate quality during customer onboarding. The API cross-references user-provided contact information with data from their respective Mobile Network Operators (MNOs), ensuring a highly reliable source of verification. Additionally, it strictly adheres to privacy regulations.

### Simplified Integration

By using a standardized API, you can effortlessly incorporate the KYC-Match process into your onboarding system without requiring custom implementations for each telecom operator. This streamlines development and accelerates your time-to-market.

### Footprint for your Identify Service​

The standardized API provides uniform access to multiple telecom companies, broadening your business reach and ensuring consistent and flexible operations across different providers.



## General Informations

> ⚙️ Problem Solved ? 
>
> Check if the user data is true or false.


> ⚙️ Parameters sent in the request 
>
> - idDocumentMatch (Indicates whether the ID number associated with the customer's ID document matches the one in the OB systems. Possible values: true, false, not_available)
> - nameMatch (Indicates whether the customer's full name matches the one in the OB systems. Possible values: true, false, not_available)
> - givenNameMatch (Indicates whether the customer's first name matches the one in the OB systems. Possible values: true, false, not_available)
> - familyNameMatch (Indicates whether the customer's last name matches the one in the OB systems. Possible values: true, false, not_available)
> - nameKanaHankakuMatch (Indicates whether the customer's full name in Hankaku-Kana format (name reading) for Japan matches the one in the OB systems. Possible values: true, false, not_available)
> - nameKanaZenkakuMatch (Indicates whether the customer's full name in Zenkaku-Kana format (name reading) for Japan matches the one in the OB systems. Possible values: true, false, not_available)
> - middleNamesMatch (Indicates whether the customer's middle names match the ones in the OB systems. Possible values: true, false, not_available)
> - familyNameAtBirthMatch (Indicates whether the customer's family name at birth matches the one in the OB systems. Possible values: true, false, not_available)
> - addressMatch (Indicates whether the customer's complete address matches the one in the OB systems. Possible values: true, false, not_available)
> - streetNameMatch (Indicates whether the customer's street name matches the one in the OB systems. Possible values: true, false, not_available)
> - streetNumberMatch (Indicates whether the customer's street number matches the one in the OB systems. Possible values: true, false, not_available)
> - postalCodeMatch (Indicates whether the customer's postal code matches the one in the OB systems. Possible values: true, false, not_available)
> - regionMatch (Indicates whether the region of the customer's address matches the one in the OB systems. Possible values: true, false, not_available)
> - localityMatch (Indicates whether the locality of the customer's address matches the one in the OB systems. Possible values: true, false, not_available)
> - countryMatch (Indicates whether the country of the customer's address matches the one in the OB systems. Possible values: true, false, not_available)
> - houseNumberExtensionMatch (Indicates whether the house number extension of the customer's address matches the one in the OB systems. Possible values: true, false, not_available)
> - birthdateMatch (Indicates whether the customer's birthdate matches the one in the OB systems. Possible values: true, false, not_available)
> - emailMatch (Indicates whether the customer's email address matches the one in the OB systems. Possible values: true, false, not_available)
> - genderMatch (Indicates whether the customer's gender matches the one in the OB systems. Possible values: true, false, not_available)



> ⚙️ Data received in the response
>
> - If the ID number associated with the customer's ID document matches the one in the OB systems, it returns "idDocumentMatch": true;
> - If the ID number does not match, it returns "idDocumentMatch": false;
> - If the ID number is not available, it returns "idDocumentMatch": not_available.

> - If the customer's full name matches the one in the OB systems, it returns "nameMatch": true;
> - If the full name does not match, it returns "nameMatch": false;
> - If the full name is not available, it returns "nameMatch": not_available.

> - If the customer's first name matches the one in the OB systems, it returns "givenNameMatch": true;
> - If the first name does not match, it returns "givenNameMatch": false;
> - If the first name is not available, it returns "givenNameMatch": not_available.

> - If the customer's last name matches the one in the OB systems, it returns "familyNameMatch": true;
> - If the last name does not match, it returns "familyNameMatch": false;
> - If the last name is not available, it returns "familyNameMatch": not_available.

> - If the customer's full name in Hankaku-Kana format (name reading) for Japan matches the one in the OB systems, it returns "nameKanaHankakuMatch": true;
> - If the full name in Hankaku-Kana format does not match, it returns "nameKanaHankakuMatch": false;
> - If the full name in Hankaku-Kana format is not available, it returns "nameKanaHankakuMatch": not_available.

> - If the customer's full name in Zenkaku-Kana format (name reading) for Japan matches the one in the OB systems, it returns "nameKanaZenkakuMatch": true;
> - If the full name in Zenkaku-Kana format does not match, it returns "nameKanaZenkakuMatch": false;
> - If the full name in Zenkaku-Kana format is not available, it returns "nameKanaZenkakuMatch": not_available.

> - If the customer's middle names match the ones in the OB systems, it returns "middleNamesMatch": true;
> - If the middle names do not match, it returns "middleNamesMatch": false;
> - If the middle names are not available, it returns "middleNamesMatch": not_available.

> - If the customer's family name at birth matches the one in the OB systems, it returns "familyNameAtBirthMatch": true;
> - If the family name at birth does not match, it returns "familyNameAtBirthMatch": false;
> - If the family name at birth is not available, it returns "familyNameAtBirthMatch": not_available.

> - If the customer's complete address matches the one in the OB systems, it returns "addressMatch": true;
> - If the complete address does not match, it returns "addressMatch": false;
> - If the complete address is not available, it returns "addressMatch": not_available.

> - If the customer's street name matches the one in the OB systems, it returns "streetNameMatch": true;
> - If the street name does not match, it returns "streetNameMatch": false;
> - If the street name is not available, it returns "streetNameMatch": not_available.

> - If the customer's street number matches the one in the OB systems, it returns "streetNumberMatch": true;
> - If the street number does not match, it returns "streetNumberMatch": false;
> - If the street number is not available, it returns "streetNumberMatch": not_available.

> - If the customer's postal code matches the one in the OB systems, it returns "postalCodeMatch": true;
> - If the postal code does not match, it returns "postalCodeMatch": false;
> - If the postal code is not available, it returns "postalCodeMatch": not_available.

> - If the region of the customer's address matches the one in the OB systems, it returns "regionMatch": true;
> - If the region does not match, it returns "regionMatch": false;
> - If the region is not available, it returns "regionMatch": not_available.

> - If the locality of the customer's address matches the one in the OB systems, it returns "localityMatch": true;
> - If the locality does not match, it returns "localityMatch": false;
> - If the locality is not available, it returns "localityMatch": not_available.

> - If the country of the customer's address matches the one in the OB systems, it returns "countryMatch": true;
> - If the country does not match, it returns "countryMatch": false;
> - If the country is not available, it returns "countryMatch": not_available.

> - If the house number extension of the customer's address matches the one in the OB systems, it returns "houseNumberExtensionMatch": true;
> - If the house number extension does not match, it returns "houseNumberExtensionMatch": false;
> - If the house number extension is not available, it returns "houseNumberExtensionMatch": not_available.

> - If the customer's birthdate matches the one in the OB systems, it returns "birthdateMatch": true;
> - If the birthdate does not match, it returns "birthdateMatch": false;
> - If the birthdate is not available, it returns "birthdateMatch": not_available.

> - If the customer's email address matches the one in the OB systems, it returns "emailMatch": true;
> - If the email address does not match, it returns "emailMatch": false;
> - If the email address is not available, it returns "emailMatch": not_available.

> - If the customer's gender matches the one in the OB systems, it returns "genderMatch": true;
> - If the gender does not match, it returns "genderMatch": false;
> - If the gender is not available, it returns "genderMatch": not_available.


