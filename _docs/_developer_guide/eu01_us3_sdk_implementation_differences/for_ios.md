---
nav_title: For iOS
page_order: 1
---

# For iOS

To update the default endpoint in your integration of the Braze SDKs please add the following code:

## Compile-time Endpoint Configuration (Recommended)

{% alert note %}
Note that as of December 2019, custom endpoints are no longer given out, if you have a pre-existing custom endpoint, you may continue to use it. For a list of our available endpoints, <a href="{{site.baseurl}}/api/basics/#endpoints">click here</a>.
{% endalert %}

If given a pre-exisiting custom endpoint by Braze...
- Starting with Braze iOS SDK v3.0.2, you can set a custom secure endpoint using the `Info.plist` file. Add the `Braze` dictionary to your Info.plist file. Inside the `Braze` dictionary, add the `Endpoint` string subentry and set the value to your custom endpoint url’s authority (for example, `sdk.iad-01.braze.com`, not `https://sdk.iad-01.braze.com`). Note that prior to Braze iOS SDK INSERT_VERSION_HERE, the dictionary key `Appboy` must be used in place of `Braze`.

## Runtime Endpoint Configuration

If given a pre-existing custom endpoint by Braze...
- Starting with Braze iOS SDK v3.17.0+, you can override set your secure endpoint via the `ABKEndpointKey` inside the `appboyOptions` parameter passed to `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Set the value to your custom endpoint url’s authority (for example, `sdk.iad-01.braze.com`, not `https://sdk.iad-01.braze.com`).

{% alert note %}
Support for setting endpoints at runtime using `ABKAppboyEndpointDelegate` has been removed in Braze iOS SDK v3.17.0. If you already use `ABKAppboyEndpointDelegate`, note that in Braze iOS SDK versions v3.14.1 to v3.16.0, any reference to `dev.appboy.com` in your `getApiEndpoint()` method must be replaced with a reference to `sdk.iad-01.braze.com`.
{% endalert %}
