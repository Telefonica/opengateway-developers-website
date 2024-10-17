---
title: Test the Sandbox with Postman
excerpt: Learn how to explore the functionality of the Sandbox environment using Postman, this guide will demonstrate how to effectively interact with APIs in a controlled setting.
category: 66d5624a492663000f4ed527
---

# Interact with the Open Gateway Sandbox using Postman

Here you can download the postman collection <a href="https://github.com/Telefonica/opengateway-postman/raw/main/postman_collection.json" download>Postman collection</a> and the <a href="https://github.com/Telefonica/opengateway-postman/raw/main/sandbox.postman_environment.json" download> Sandbox enviroment</a> with variables that you will have to configure to work with your sandbox credentials. 

To import a Postman collection, you will need to follow the steps below:  

1. Open Postman and click on the ‘Import’ button in the top left corner of the interface.
2. Select ‘File’ and browse for the collection file you wish to import into your system.
3. At this point, Postman will automatically detect the file type and import it. Once complete, you will see the imported collection in the left pane of the interface.

Open Gateway APIs access is granted to applications, not developers, so every application can have limited access to the scope and for the purpose it needs.

## Hands-on Postman 

### Import the Postman Collection

To use a Postmam collection: 

1. Click on the imported collection in the left pane to expand it and see all its API calls. You will find them organised in folders, indicating the order in which you should make them: 
	- Authenticate your app and its user (an alternative authentication method will soon be available for frontend use) > Authorization (OIDC) / CIBA (Backend) / 1st Authorization request.
	- Get an access token with which to make the service API call > Authorization (OIDC) / CIBA (Backend) / 2nd Get access token.
	- Make the call to the service API, among those available: Service APIs 
  


2. Service APIs / Select a specific call to view the details and configuration options.

![Available Services](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/sandbox/images/availableservice.png) 

3. You can send the request by clicking on the ‘Send’ button and view the response in the ‘Response’ tab. However, you will need to import the environment first.

![Send Request](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/sandbox/images/send.png) 

### Import the Postman Environment

On the other hand, Postman environments allow you to have a specific configuration for each of the projects you are working on. The environment we provide you with the necessary information to carry out your tests on the Open Gateway Sandbox. 

To import an environment into Postman, you will need to follow the steps below:  
1. Click on the gear icon in the top right corner and select ‘Manage Environments’.
2. Click ‘Import’ and select the environment file you wish to import.
3. Postman will import the environment and display it in the list of available environments.

![Import Environment](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/sandbox/images/importenvironment.png) 


To use an environment in Postmam:

1. Select the desired environment by clicking on the drop-down menu in the top right corner of the interface.
2. The variables defined in the environment will be available for use in collection requests. Collection requests already use the following environment variables in the format
{{variable_name}}. You simply need to edit the environment, after importing it, and modify
them according to your own test configuration:
   - **‘api-gateway-url** - Fixed. Should not be changed if you want to run your tests on the Sandbox. Its value is https://sandbox.opengateway.telefonica.com/apigateway
   - **‘application-client-id’** - Value that identifies each of the apps you have registered in the Sandbox. You can check it in the ‘My apps’ section.
   - **‘application-client-secret’** - Private key to authenticate each of your registered apps. You can check it in the section ‘My apps’. 
   - **‘mobile-phone-number’** - Mobile line number for mobile network API calls (e.g. SIM Swap). If it is more convenient for you. You can modify the calls in the collection to indicate this value in them instead of using the {{mobile-phone-number}} variable.
   - **‘device-local-ip’** - Local IPv4 of a device on the home WiFi network for calls to the home network APIs (e.g. Home Devices QoD). If this is more convenient for you. You can modify the calls in the collection to specify this value in them instead of using the {{device-local-ip}} variable.

![Sandbox Environment](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/sandbox/images/environments.png) 

For more information, you can consult the [Postman Getting Started](https://learning.postman.com/docs/getting-started/overview/) guide here.
