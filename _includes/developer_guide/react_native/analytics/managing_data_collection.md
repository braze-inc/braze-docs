{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Disabling data tracking

To disable data collection, use the `disableSDK` method. After calling this method, the Braze SDK stops sending data to Braze servers.

```javascript
Braze.disableSDK();
```

## Resuming data tracking

To resume data collection after disabling it, use the `enableSDK` method.

```javascript
Braze.enableSDK();
```

## Wiping data

To delete all locally stored Braze SDK data on the device, use the `wipeData` method. After calling this method, the SDK is disabled and must be re-enabled with `enableSDK`.

```javascript
Braze.wipeData();
```

## Flushing data

To request an immediate flush of any pending data to Braze servers, use `requestImmediateDataFlush`.

```javascript
Braze.requestImmediateDataFlush();
```

## Setting ad-tracking enabled

To inform Braze whether ad-tracking is enabled for this device, use the `setAdTrackingEnabled` method. The SDK does not automatically collect this data.

```javascript
Braze.setAdTrackingEnabled(true, "GOOGLE_ADVERTISING_ID");
```

The second parameter is the Google Advertising ID and is only used on Android.

## Updating the tracking property allow list (iOS only)

To update the list of data types declared for tracking, use `updateTrackingPropertyAllowList`. This is a no-op on Android.

```javascript
Braze.updateTrackingPropertyAllowList({
  adding: [Braze.TrackingProperty.EMAIL, Braze.TrackingProperty.FIRST_NAME],
  removing: [],
  addingCustomEvents: ["my_custom_event"],
  removingCustomEvents: [],
  addingCustomAttributes: ["my_custom_attribute"],
  removingCustomAttributes: []
});
```

For more information, refer to [Privacy Manifest]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/).
