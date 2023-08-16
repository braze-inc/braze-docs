---
nav_title: Deep Linking
article_title: Deep Linking for iOS
platform: iOS
page_order: 0
description: "This article covers how to implement the universal deep linking delegate for your iOS app and examples on how to deep link to app settings or a News Feed."

---

# Deep linking for iOS

For introductory information on deep links, refer to our [User Guide article][4]. If you're looking to implement deep links for the first time in your Braze app, the steps below will get you started.

{% alert note %}
This article includes information on News Feed, which is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

## Step 1: Register a scheme

You must state a custom scheme in the `Info.plist` file. The navigation structure is defined by an array of dictionaries. Each of those dictionaries contains an array of strings.

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
        <string>{YOUR.SCHEME}</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>{YOUR.SCHEME}</string>
        </array>
    </dict>
</array>
```

## Step 2: Whitelist the custom scheme (iOS 9+)

Starting with iOS 9, apps must have a whitelist of custom schemes that the app is allowed to open. Attempting to call schemes outside this list will cause the system to record an error in the device's logs, and the deep link will not open. An example of this error looks like this:

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

For example, if an in-app message should open the Facebook app when tapped, the app has to have the Facebook custom scheme (`fb`) in the whitelist. Otherwise, the system will reject the deep link. Deep links that direct to a page or view inside your own app still require that your app's custom scheme be listed in your app's `Info.plist`.

You should add all the schemes that the app needs to deep link to in a whitelist in your app's `Info.plist` with the key `LSApplicationQueriesSchemes`. For example:

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>facebook</string>
    <string>twitter</string>
</array>
```

For more information, refer to [Apple's documentation][12] on the `LSApplicationQueriesSchemes` key.

## Step 3: Implement a handler

After activating your app, iOS will call the method [`application:openURL:options:`][13]. The important argument is the [NSURL][2] object.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Here you should insert code to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Here you should insert code to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% endtabs %}

![][10]

# Universal links

To use universal links, make sure you have added a registered domain to your app's capabilities and have uploaded an `apple-app-site-association` file. Then implement the method `application:continueUserActivity:restorationHandler:` in your `AppDelegate`. For example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application
continueUserActivity:(NSUserActivity *)userActivity
  restorationHandler:(void (^)(NSArray *restorableObjects))restorationHandler {
  if ([userActivity.activityType isEqualToString:NSUserActivityTypeBrowsingWeb]) {
    NSURL *url = userActivity.webpageURL;
    // Handle url
  }
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  if (userActivity.activityType == NSUserActivityTypeBrowsingWeb) {
    let url = userActivity.webpageURL
    // Handle url
  }
  return true
}
```

{% endtab %}
{% endtabs %}

Refer to [Apple][11] for more information.

{% alert note %}
The default universal link integration is not compatible with Braze's push notifications, in-app messages, or News Feed. See [linking customization](#linking-handling-customization) to handle universal links within your application. Alternatively, we recommend using [scheme-based deep links](#step-1-registering-a-scheme) with push notifications, in-app messages, and the News Feed.
{% endalert%}

## App transport security (ATS)
iOS 9 introduced a breaking change affecting web URLs embedded in in-app messages, News Feed cards, and push notifications.

### ATS requirements
From [Apple's documentation][16]: "App Transport Security is a feature that improves the security of connections between an app and web services. The feature consists of default connection requirements that conform to best practices for secure connections. Apps can override this default behavior and turn off transport security."

ATS is applied by default on iOS 9+. It requires that all connections use HTTPS and are encrypted using TLS 1.2 with forward secrecy. Refer to [Requirements for Connecting Using ATS][14] for more information. All images served by Braze to end devices are handled by a content delivery network ("CDN") that supports TLS 1.2 and is compatible with ATS.

Unless they are specified as exceptions in your application's `Info.plist`, connections that do not follow these requirements will fail with errors that look something like this:

```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

ATS compliance is enforced for links opened within the mobile app (Braze's default handling of clicked links) and does not apply to sites opened externally via a web browser.

### Handling ATS requirements

You can handle ATS in one of the following three ways:

#### Confirm all links are ATS compliant (recommended)
Your Braze integration can satisfy ATS requirements by ensuring that any existing links you drive users to (through in-app message and push campaigns or News Feed cards) satisfy ATS requirements. While there are ways to bypass ATS restrictions, Braze's recommended best practice is to check that all linked URLs are ATS compliant. Given Apple's increasing emphasis on application security, the following approaches to allowing ATS exceptions are not guaranteed to be supported by Apple.

An SSL tool can help you pinpoint web server security issues. This [SSL server test][15] from Qualys, Inc. provides a line item specifically for Apple ATS 9 and iOS 9 compliance.

#### Partially disable ATS
You can allow a subset of links with certain domains or schemes to be treated as exceptions to the ATS rules. Your Braze integration will satisfy ATS requirements if every link you use in a Braze messaging channel is either ATS compliant or handled by an exception.

To add a domain as an exception of the ATS, add the following to your app's `Info.plist` file:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
    <key>NSExceptionDomains</key>
    <dict>
        <key>example.com</key>
        <dict>
            <key>NSExceptionAllowsInsecureHTTPLoads</key>
            <false/>
            <key>NSIncludesSubdomains</key>
            <true/>
        </dict>
    </dict>
</dict>
```

Refer to Apple's article on [app transport security keys][19] for more information.

#### Disable ATS entirely

You can turn off ATS entirely. Note that this is not recommended practice, due to both lost security protections and future iOS compatibility. To disable ATS, insert the following in your app's `Info.plist` file:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

Refer to [Shipping an App With App Transport Security][17] for more information on how to debug ATS failures.

## URL encoding

As of Braze iOS SDK v2.21.0, the SDK percent-encodes links to create valid `NSURL`s. All link characters that are not allowed in a properly formed URL, such as Unicode characters, will be percent escaped.

To decode an encoded link, use the `NSString` method [`stringByRemovingPercentEncoding`][8]. Note that you must also return `YES` in the `ABKURLDelegate` and that a call to action is required to trigger the handling of the URL by the app. For example:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% endtabs %}

## Customization {#linking-customization}

### Default WebView customization

The customizable `ABKModalWebViewController` class displays web URLs opened by the SDK, typically when "Open Web URL Inside App" is selected for a web deep link.

You can declare a category for, or directly modify, the `ABKModalWebViewController` class to apply customization to the web view. Check the class' [.h file][6] and [.m file][5] for more detail.

### Linking handling customization

The `ABKURLDelegate` protocol can be used to customize the handling of URLs such as deep links, web URLs, and universal links. To set the delegate during Braze initialization, pass a delegate object to the `ABKURLDelegateKey` in the `appboyOptions` of [`startWithApiKey:inApplication:withAppboyOptions:`][22]. Braze will then call your delegate's implementation of `handleAppboyURL:fromChannel:withExtras:` before handling any URIs.

#### Integration example: ABKURLDelegate

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)handleAppboyURL:(NSURL *)url fromChannel:(ABKChannel)channel withExtras:(NSDictionary *)extras {
  if ([[url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return YES;
  }
  // Let Braze handle links otherwise
  return NO;
}
```

{% endtab %}
{% tab swift %}

```swift
func handleAppboyURL(_ url: URL?, from channel: ABKChannel, withExtras extras: [AnyHashable : Any]?) -> Bool {
  if (url.host == "MY-DOMAIN.com") {
    // Custom handle link here
    return true;
  }
  // Let Braze handle links otherwise
  return false;
}
```

{% endtab %}
{% endtabs %}

For more information, see [`ABKURLDelegate.h`][23].

## Frequent use cases

### Deep linking to app settings

iOS can take users from your app into its page in the iOS settings application. You can take advantage of `UIApplicationOpenSettingsURLString` to deep link users to Settings from Braze's push notifications, in-app messages, and the News Feed.

1. First, make sure your application is set up for either [scheme-based deep links][25] or [universal links][27].
2. Decide on a URI for deep linking to the **Settings** page (e.g., `myapp://settings` or `https://www.braze.com/settings`).
3. If you are using custom scheme-based deep links, add the following code to your `application:openURL:options:` method:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app
            openURL:(NSURL *)url
            options:(NSDictionary<UIApplicationOpenURLOptionsKey,id> *)options {
  NSString *path  = [url path];
  if ([path isEqualToString:@"settings"]) {
    NSURL *settingsURL = [NSURL URLWithString:UIApplicationOpenSettingsURLString];
    [[UIApplication sharedApplication] openURL:settingsURL];
  }
  return YES;
}
```

{% endtab %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplicationOpenSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
{% endtabs %}

[2]: https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[5]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/ABKModalWebViewController.m
[6]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKModalWebViewController.h
[8]: https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/index.html#//apple_ref/occ/instm/NSString/stringByRemovingPercentEncoding
[10]: {% image_buster /assets/img_archive/deep_link.png %}
[11]: https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html
[12]: https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14
[13]: https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc
[14]: https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35
[15]: https://www.ssllabs.com/ssltest/index.html
[16]: https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14
[17]: http://timekl.com/blog/2015/08/21/shipping-an-app-with-app-transport-security/?utm_campaign=iOS+Dev+Weekly&utm_medium=email&utm_source=iOS_Dev_Weekly_Issue_213
[19]: https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33
[22]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24
[23]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKURLDelegate.h
[25]: #deep-links
[26]: #linking-customization
[27]: #universal-links
