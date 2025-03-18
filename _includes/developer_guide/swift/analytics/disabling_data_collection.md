## Disabling data tracking

To disable data-tracking activity on the Swift SDK, set the [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) property to `false` on your Braze instance. When `enabled` is set to `false`, the Braze SDK ignores any calls to the public API. The SDK also cancels all in-flight actions, such as network requests, event processing, etc. 

## Wiping previously-stored data

You can use the [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) method to fully clear locally-stored SDK data on a user's device.

For Braze Swift versions 7.0.0 and later, the SDK and the `wipeData()` method randomly generates a UUID for their device ID. However, if your `useUUIDAsDeviceId` is set to `false` _or_ you're using Swift SDK version 5.7.0 or earlier, you'll also need to make a post request to [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) since your Identifier for Vendors (IDFV) will automatically be used as that user's device ID.

## Resuming data tracking

To resume data collection, set [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) to `true`. Keep in mind, this will not restore any previously wiped data.

## IDFV collection

In previous versions of the Braze iOS SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user's device ID. Beginning in Swift SDK `v5.7.0`, the IDFV field was optionally disabled, and instead, Braze would set a random UUID as the device ID. Starting in Swift SDK `v7.0.0`, the IDFV field will not be collected by default, and a UUID will be set as the device ID instead.

The `useUUIDAsDeviceId` feature configures the [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) to set the device ID as a UUID. Traditionally, the iOS SDK would assign the device ID equal to the Apple-generated IDFV value. With this feature enabled by default on your iOS app, all new users created via the SDK would be assigned a device ID equal to a UUID.

If you still want to collect IDFV separately, you can use [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

### Considerations

#### SDK Version

In Swift SDK `v7.0.0+`, when `useUUIDAsDeviceId` is enabled (default), all new users created will be assigned a random device ID. All previously existing users will maintain their same device ID value, which may have been IDFV.

When this feature is not enabled, devices will continue to be assigned IDFV upon creation.

#### Downstream 

**Technology partners**: When this feature is enabled, any technology partners that derive the IDFV value from the Braze device ID will no longer have access to this data. If the IDFV value derived from the device is needed for your partner integration, we recommend that you set this feature to `false`.

**Currents**: `useUUIDAsDeviceId` set to true means the device ID sent in Currents will no longer equal the IDFV value.

### Frequently asked questions

#### Will this change impact my existing users in Braze?

No. When enabled, this feature will not overwrite any user data in Braze. New UUID device IDs will only be created for new devices or when `wipedata()` is called.

#### Can I turn this feature off after turning it on?

Yes, this feature can be toggled on and off at your discretion. Previously stored device IDs will never be overwritten.

#### Can I still capture the IDFV value via Braze elsewhere?

Yes, you can still optionally collect the IDFV via the Swift SDK (collection is disabled by default). 
