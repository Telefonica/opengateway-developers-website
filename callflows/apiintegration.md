---
title: API Integration
excerpt: In this guide we will go through the different ways to integrate with Open Gateway APIs so you can find the best fit for your use case and the offering from our Channel Partners.
category: 66d57750d3f60b0011576376
---

## RESTful by design 

Since Open Gateway APIs are RESTful, you will always be able to integrate them by performing HTTP requests from any programming language providing such capability. However, most Channel Partners will provide you with SDKs in several programming languages which, by performing such requests themselves under the hood, will make your life easier when it comes to accessing the telco features that Open Gateway offers to your application.

Apart from their commercial offer, check the offering of SDKs, our any other development tools, from your our Channel Partners to better suite to your use case and application needs.

These are some pros and cons you could get from the following two ways of integrating Open Gateway APIs:

### HTTP integration

#### Pros and cons
- Pros:
	- No dependencies on third-party libraries
	- No need to learn a new SDK
	- Portability across different Channel Partners (which provide their own SDKs each)
- Cons:
	- More low-level tasks to care about: encoding your credentials, calling authorization endpoints, handling tokens, etc.
	- More difficult to implement
	- More verbose code
	- More error-prone code

### Integration by SDKs

#### Pros and cons
- Pros:
	- Low-level tasks are abstracted: SDK's classes will take your application credentials as an input and will handle authentication and token management for you
	- Further features could be included by the Channel Partner in the SDK: for instance, frontend SDKs handling network interfaces to avoid authentication problems caused by end-user device being connected to Wi-Fi networks
	- Also...
		- Less code to write
		- Less error-prone code
		- Easier to implement integration
- Cons:
	- It is up to your Channel Partner to provide SDKs in different programming languages including your app's one
	- Depending on your Channel Partner and your use case, you could need to implement a frontend authorization flow and there could be a lack of frontend SDKs (e.g. for native mobile apps) which would lead you to integrate the frontend authorization by performing HTTP requests anyway
	- Once you have integrated the SDKs from a Channel Partner, you would need some re-engineering to switch to another Channel Partner's Open Gateway platform, since each one offer their owns and SDK interfaces are not standardized at CAMARA.
