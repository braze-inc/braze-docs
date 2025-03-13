## About IDFV collection

In previous versions of the Braze iOS SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user's device ID. Beginning in Swift SDK v5.7.0, the IDFV field was optionally disabled, and instead, Braze would set a random UUID as the device ID. Starting in Swift SDK v7.0.0, the IDFV field will not be collected by default, and a UUID will be set as the device ID instead.

The `useUUIDAsDeviceId` feature configures the [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) to set the device ID as a UUID. Traditionally, the iOS SDK would assign the device ID equal to the Apple-generated IDFV value. With this feature enabled by default on your iOS app, all new users created via the SDK would be assigned a device ID equal to a UUID.

If you still wish to collect IDFV separately, you can still do so via the Swift SDK as outlined [here](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

## Considerations

### SDK Version

In Swift SDK v7.0.0+, when `useUUIDAsDeviceId` is enabled (default), all new users created will be assigned a random device ID. All previously existing users will maintain their same device ID value, which may have been IDFV.

When this feature is not enabled, devices will continue to be assigned IDFV upon creation.

### Downstream 

**Technology partners**: When this feature is enabled, any technology partners that derive the IDFV value from the Braze device ID will no longer have access to this data. If the IDFV value derived from the device is needed for your partner integration, we recommend that you set this feature to `false`.

**Currents**: `useUUIDAsDeviceId` set to true means the device ID sent in Currents will no longer equal the IDFV value.

## Frequently asked questions

#### Will this change impact my existing users in Braze?
No. When enabled, this feature will not overwrite any user data in Braze. Only newly created devices - or after `wipedata()` is called - will generate new UUID device IDs.

#### Can I turn this feature off after turning it on?
Yes, this feature can be toggled on and off at your discretion. Previously stored device IDs will never be overwritten.

#### Can I still capture the IDFV value via Braze elsewhere?
Yes, you can still optionally collect the IDFV via the Swift SDK (collection is disabled by default). 
