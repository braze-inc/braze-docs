---
nav_title: Deep Linking
article_title: Deep Linking for iOS
platform: Swift
page_order: 1
description: "This article covers how to implement the universal deep linking delegate for your iOS app and examples on how to deep link to app settings for the Swift SDK."

---

# Deep linking

> Deep linking is a way of providing a link that launches a native app, shows specific content, or takes some specific action. If you're looking to implement deep links in your iOS app for the first time, follow these steps.

{% tabs %}
{% tab web %}
THIS.
{% endtab %}

{% tab iOS %}
{% subtabs %}
{% subtab swift %}
## Step 1: Registering a scheme

To handle deep linking, a custom scheme must be stated in your `Info.plist` file. The navigation structure is defined by an array of dictionaries. Each of those dictionaries contains an array of strings.

Use Xcode to edit your `Info.plist` file:

1. Add a new key, `URL types`. Xcode will automatically make this an array containing a dictionary called `Item 0`.
2. Within `Item 0`, add a key `URL identifier`. Set the value to your custom scheme.
3. Within `Item 0`, add a key `URL Schemes`. This will automatically be an array containing a `Item 0` string.
4. Set `URL Schemes` >> `Item 0` to your custom scheme.

Alternatively, if you wish to edit your `Info.plist` file directly, you can follow this spec:

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

## Step 2: Adding a scheme allowlist

You must declare the URL schemes you wish to pass to `canOpenURL(_:)` by adding the `LSApplicationQueriesSchemes` key to your app's Info.plist file. Attempting to call schemes outside this allowlist will cause the system to record an error in the device's logs, and the deep link will not open. An example of this error will look like this:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

For example, if an in-app message should open the Facebook app when tapped, the app has to have the Facebook custom scheme (`fb`) in your allowlist. Otherwise, the system will reject the deep link. Deep links that direct to a page or view inside your own app still require that your app's custom scheme be listed in your app's `Info.plist`.

Your example allowlist might look something like:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

For more information, refer to [Apple's documentation][12] on the `LSApplicationQueriesSchemes` key.

## Step 3: Implement a handler

After activating your app, iOS will call the method [`application:openURL:options:`][13]. The important argument is the [NSURL][2] object.

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```
{% endsubtab %}

{% subtab objective-c %}
## Step 1: Registering a scheme

To handle deep linking, a custom scheme must be stated in your `Info.plist` file. The navigation structure is defined by an array of dictionaries. Each of those dictionaries contains an array of strings.

Use Xcode to edit your `Info.plist` file:

1. Add a new key, `URL types`. Xcode will automatically make this an array containing a dictionary called `Item 0`.
2. Within `Item 0`, add a key `URL identifier`. Set the value to your custom scheme.
3. Within `Item 0`, add a key `URL Schemes`. This will automatically be an array containing a `Item 0` string.
4. Set `URL Schemes` >> `Item 0` to your custom scheme.

Alternatively, if you wish to edit your `Info.plist` file directly, you can follow this spec:

```html
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

## Step 2: Adding a scheme allowlist

You must declare the URL schemes you wish to pass to `canOpenURL(_:)` by adding the `LSApplicationQueriesSchemes` key to your app's Info.plist file. Attempting to call schemes outside this allowlist will cause the system to record an error in the device's logs, and the deep link will not open. An example of this error will look like this:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

For example, if an in-app message should open the Facebook app when tapped, the app has to have the Facebook custom scheme (`fb`) in your allowlist. Otherwise, the system will reject the deep link. Deep links that direct to a page or view inside your own app still require that your app's custom scheme be listed in your app's `Info.plist`.

Your example allowlist might look something like:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

For more information, refer to [Apple's documentation][12] on the `LSApplicationQueriesSchemes` key.

## Step 3: Implement a handler

After activating your app, iOS will call the method [`application:openURL:options:`][13]. The important argument is the [NSURL][2] object.

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
  return YES;
}
```
{% endsubtab %}

{% subtab react native %}
## Step 1: Add `populateInitialUrlFromLaunchOptions`

For iOS, add `populateInitialUrlFromLaunchOptions` to your AppDelegate's `didFinishLaunchingWithOptions` method.

For example:

```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  self.moduleName = @"BrazeProject";
  self.initialProps = @{};

  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:apiKey endpoint:endpoint];
  configuration.triggerMinimumTimeInterval = 1;
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  [self registerForPushNotifications];
  [[BrazeReactUtils sharedInstance] populateInitialUrlFromLaunchOptions:launchOptions];

  return [super application:application didFinishLaunchingWithOptions:launchOptions];
}
```

## Step 2: Add `getInitialURL()`

Add the `Linking.getInitialURL()` method to handle when a deep link opens your app.

You should also call the `Braze.getInitialURL` method to handle deep links from iOS push notification clicks while your app is not running. Braze provides this workaround since React Native's Linking API does not support this scenario due to a race condition on app startup.

For example:

```javascript
Linking.getInitialURL()
  .then(url => {
    if (url) {
      console.log('Linking.getInitialURL is ' + url);
      showToast('Linking.getInitialURL is ' + url);
      handleOpenUrl({ url });
    }
  })
  .catch(err => console.error('Error getting initial URL', err));

// Handles deep links when an iOS app is launched from a hard close via push click.
Braze.getInitialURL(url => {
  if (url) {
    console.log('Braze.getInitialURL is ' + url);
    showToast('Braze.getInitialURL is ' + url);
    handleOpenUrl({ url });
  }
});
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab android %}
THIS.
{% endtab %}
{% endtabs %}

[2]: https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[6]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/webviewcontroller
[8]: https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding
[11]: https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app
[12]: https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14
[13]: https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc
[14]: https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35
[15]: https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application
[16]: https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14
[19]: https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33
[22]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24
[23]: https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate
[25]: ##step-1-registering-a-scheme
[26]: #linking-customization
[27]: #universal-links