---
nav_title: Collecting IDFV
article_title: Collecting IDFV
platform: iOS
page_type: reference
description: "This reference article describes how to collect the optional IDFV field"

---

# Collecting IDFV

## Background

In previous versions of the Braze iOS SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user's device ID. Beginning in Swift SDK v5.7.0, the IDFV field can optionally be disabled, and instead, Braze will set a random UUID as the device ID.

The optional `useUUIDAsDeviceId` feature configures the Swift SDK to set the device ID as a UUID. Traditionally, the iOS SDK would assign the device ID equal to the Apple-generated IDFV value. With this feature enabled on your iOS app, all new users created via the SDK would be assigned a device ID equal to a UUID.

## Collect IDFV with the UUID option enabled

If you still wish to collect IDFV with the UUID option enabled, you can still do so as outlined below:

In the `Braze.Configuration` instance of your iOS application, set `useUUIDAsDeviceId` to `true`.

## Considerations

### SDK Version

When enabling `useUUIDAsDeviceId`, all new users created will be assigned a random device ID. All previously existing users will maintain their same device ID value, which may have been IDFV.

When this feature is not enabled (by default), devices will continue to be assigned IDFV upon creation.

The diagram below describes when a UUID or IDFV will be assigned as the device ID. Note that the IDFV field can only be read from devices that support this feature (e.g., iOS, tvOS, macCatalyst)

![]({% image_buster /assets/img/swift_idfv.png %}){: style="max-width:80%"}

### Downstream 

**Technology partners**: If this feature is enabled, any technology partners that derive the IDFV value from the Braze device ID will no longer have access to this piece of data. If the IDFV value derived from the device IS is needed for your partner integration, we recommend that you do not enable this feature.

**Currents**: Enabling the `useUUIDAsDeviceId` option will mean the device ID sent in Currents will no longer equal IDFV.

## FAQs

#### Will this change impact my existing users in Braze?
No. When enabled, this feature will not overwrite any user data in Braze. Only newly created devices - or after `wipedata()` is called - will generate new UUID device IDs.

#### Can I turn this feature off after turning it on?
Yes, this feature can be toggled on and off at your discretion. Previously stored device IDs will never be overwritten.

#### Can I still capture the IDFV value via Braze elsewhere? 
Yes, you can still optionally collect the IDFV via the Swift SDK (collection is disabled by default). 
