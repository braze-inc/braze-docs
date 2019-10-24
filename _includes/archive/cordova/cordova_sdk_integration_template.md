# Push Notifications

If you use the Cordova SDK default setup you won't have to make any new changes client-side. For modified integrations, see [the {{ include.platform }} integration instructions][1].

# In-App Messaging

By default the Cordova SDK supports in-app messages with no changes. See [the {{ include.platform }} integration instructions][11] for information on customizing in-app messages. Furthermore, you can look at the [sample Cordova application][3] or the [sample {{ include.platform }} application][3] for implementation samples.



# Analytics

### Setting User IDs

See [the {{ include.platform }} integration instructions][6] for an in depth discussion of when to set and change a user ID.

```javascript
AppboyPlugin.changeUser("YOUR_USER_ID");
```

### Logging Custom Events

See [the {{ include.platform }} integration instructions][7] for in depth discussion of event tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "Val1";
AppboyPlugin.logCustomEvent("cordovaCustomEventWithProperties", properties);
```

### Setting Custom Attributes

See [the {{ include.platform }} integration instructions][8] for in depth discussion of attribute tracking best practices and interfaces.

```javascript
AppboyPlugin.setFirstName("firstName");
```

### Logging Purchases

See [the {{ include.platform }} integration instructions][9] for in depth discussion of revenue tracking best practices and interfaces.

```javascript
var properties = {};
properties["KeyOne"] = "ValueOne";
AppboyPlugin.logPurchase("testPurchaseWithNullCurrency", 10, null, 5, properties);
```

# News Feed

See [the {{ include.platform }} integration instructions][5] for information on how to integrate the news feed into your Cordova app. Alternatively, our Cordova plugin provides a method, `launchNewsFeed`, that will launch a modal news feed without further integration.

The Braze Cordova SDK has several methods to get the number of read/unread News Feed cards for different categories. See our [sample project implementation][4] for an example.

You can look at the [sample {{ include.platform }} application][3] and [sample Cordova application][3] implementation samples.

# Setting a Custom API Endpoint

A custom API endpoint can be configured via the `config.xml`. For example, to use the EU endpoint, see the following:

```
<platform name="{{ include.config_platform }}">
    ...
    <preference name="{{ include.endpoint_preference_key }}" value="sdk.fra-01.braze.eu" />
</platform>
```
