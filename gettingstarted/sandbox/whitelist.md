---
title: Sandbox line whitelist
excerpt: Get familiar with our Sandbox's whitelist and how it's meant to guard our operators' customers' privacy.
category: 66d5624a492663000f4ed527
---

## On privacy

Having actual operator's mobile lines in you whitelist is mandatory for testing the APIs in the production mode. This way, you as a tester can make real calls to the operators' APIs and get real responses without compromising anyone else's privacy by accessing just your own line's data.

Check the [Privacy](/docs/privacy) guide for more information on why Open Gateway is Privacy by Design.

## Adding your mobile lines to the whitelist

In order to add your lines to the whitelist, just visit the Sandbox web console's section "My phone numbers", add your line's number and follow the Sandbox directions.

You will find a QR code to scan with your mobile device. Be sure to use the device in which the line's SIM card is installed. Since the goal is to verify the line is yours, you need to be connected by using the line's data. If your device is connected to a WiFi or your device is dual SIM and it is using the other line's data, the operator won't be able to verify it. Check your device mobile settings in that case.

![Verify a new line capturing a QR code](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/sandbox/images/whitelist-qr.png?autoSizes=true)

Your mobile device will be redirected to a web page which will use the Number Verification API itself to verify the line. Once the verification is done, your line will be added to the whitelist, and you will find it as verified on the "My phone numbers" section in the Sandbox web console.

![Complete verification on your mobile device](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/sandbox/images/whitelist-mobile.png?autoSizes=true)

In case you get your line added but you didn't get the verification done, you can try again by clicking the QR icon next to your line in the "My phone numbers" section to trigger the verification process again.

![Resume verification from the white list](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/sandbox/images/whitelist-verify.png?autoSizes=true)