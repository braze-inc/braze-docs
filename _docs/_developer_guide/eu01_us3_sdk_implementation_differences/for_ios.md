---
nav_title: For iOS
page_order: 5
---

# For iOS

To update the default endpoint in your integration of the Braze SDKs please add the following code:

Starting with Braze iOS SDK v3.0.2, you can set a custom endpoint using the `Info.plist` file. Add the `Appboy` dictionary to your Info.plist file. Inside the `Appboy` dictionary, add the `Endpoint` string subentry and set the value to your custom endpoint url’s authority (for example, `sdk.iad-01.braze.com`, not `https://sdk.iad-01.braze.com`).
