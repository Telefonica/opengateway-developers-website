---
title: Device Location API
excerpt: The Device Location API from Open Gateway allows to check if a mobile phone is in a determined location.
category: 66aa4f941e51e7000fa353ce
---


The Device Location API is a software interface that allows applications to confirm if a user's device is in its intended location. The network must track a device's location at all times to effectively provide telecommunications services. This capability is utilized to offer device location as a service.

The Device Location API enhances security by verifying that a device is in the expected location during transactions, which helps prevent fraud and unauthorized activities. This verification process also streamlines authentication, leading to faster and smoother transactions, ultimately improving the user experience. 

Additionally, the API is a valuable tool for fraud prevention, as it can quickly detect and mitigate potential threats by identifying discrepancies between the claimed and actual device locations. It also helps businesses comply with regulatory requirements in industries where location verification is essential, such as finance and gaming. 
 
Furthermore, by knowing a user's location, businesses can offer more personalized and context-aware services, increasing customer engagement and satisfaction. The API's versatility makes it applicable across various industries, including retail, telecom, and logistics. For merchants, it also contributes to reducing chargebacks by verifying the location of a device during transactions.


## Overview of the SIM Swap CAMARA API

### High level definition

The Device Location CAMARA API is a software interface that allows applications to confirm if a user’s device is in the expected location. For the network to deliver its telecommunications services effectively, it must be able to locate a device at any time. This capability is thus utilized to provide device location as a service.

### API Operations

The Device Location Camara API specifies one operation:

- **POST /verify**: answers the question ‘is the device in the circle determined by a center (latitude and longitude) and an accuracy (given in km as the radius of the circle)?’

[Check the API Reference](/reference/retrievedevicelocation)

