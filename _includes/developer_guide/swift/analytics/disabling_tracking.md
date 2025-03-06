## Disabling tracking

To comply with data privacy regulations, data tracking activity on the iOS SDK can be stopped entirely by setting the [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) property to `false` on your Braze instance. 

When `enabled` is set to `false`, the Braze SDK ignores any calls to the public API. The SDK also cancels all in-flight actions, such as network requests, event processing, etc. To resume data collection, set [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) to `true`.

You can also use the [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) method to fully clear locally-stored SDK data on a user's device. If you're using Swift SDK version 5.7.0 or earlier, or `useUUIDAsDeviceId` is set to `false`, you'll also need to make a post request to [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) since your Identifier for Vendors (IDFV) will be used as their device ID. For Braze Swift versions 7.0.0 and later, the SDK and the `wipeData()` method randomly generates a UUID for their device ID instead.
