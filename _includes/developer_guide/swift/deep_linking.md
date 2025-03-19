{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Handling deep links

### Step 1: Register a scheme {#register-a-scheme}

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

### Step 2: Add a scheme allowlist

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

For more information, refer to [Apple's documentation](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14) on the `LSApplicationQueriesSchemes` key.

### Step 3: Implement a handler

After activating your app, iOS will call the method [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc). The important argument is the [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL) object.

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  let query = url.query
  // Insert your code here to take some action based upon the path and query.
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *path  = [url path];
  NSString *query = [url query];
  // Insert your code here to take some action based upon the path and query.
  return YES;
}
```

{% endtab %}
{% endtabs %}

## App Transport Security (ATS)

As defined by [Apple](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14), "App Transport Security is a feature that improves the security of connections between an app and web services. The feature consists of default connection requirements that conform to best practices for secure connections. Apps can override this default behavior and turn off transport security."

ATS is applied by default. It requires that all connections use HTTPS and are encrypted using TLS 1.2 with forward secrecy. Refer to [Requirements for Connecting Using ATS](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35) for more information. All images served by Braze to end devices are handled by a content delivery network ("CDN") that supports TLS 1.2 and is compatible with ATS.

Unless they are specified as exceptions in your application's `Info.plist`, connections that do not follow these requirements will fail with errors that are similar to the following.

**Example Error 1:**

```bash
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

**Example Error 2:**

```bash
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

ATS compliance is enforced for links opened within the mobile app (our default handling of clicked links) and does not apply to sites opened externally via a web browser.

### Working with ATS

You can handle ATS in either of the following ways, but we recommend **complying with ATS requirements**.

{% tabs local %}
{% tab Comply %}
Your Braze integration can satisfy ATS requirements by ensuring that any existing links you drive users to (for example, though in-app message and push campaigns) satisfy ATS requirements. While there are ways to bypass ATS restrictions, our recommendation is to ensure that all linked URLs are ATS-compliant. Given Apple's increasing emphasis on application security, the following approaches to allowing ATS exceptions are not guaranteed to be supported by Apple.
{% endtab %}

{% tab Partially disable %}
You can allow a subset of links with certain domains or schemes to be treated as exceptions to the ATS rules. Your Braze integration will satisfy ATS requirements if every link you use in a Braze messaging channel is either ATS compliant or handled by an exception.

To add a domain as an exception of the ATS, add following to your app's `Info.plist` file:

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

Refer to Apple's article on [app transport security keys](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33) for more information.
{% endtab %}

{% tab Fully disable %}
You can turn off ATS entirely. Note that this is not recommended practice, due to both lost security protections and future iOS compatibility. To disable ATS, insert the following in your app's `Info.plist` file:

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```
{% endtab %}
{% endtabs %}

## Decoding URLs

The SDK percent-encodes links to create valid `URL`s. All link characters that are not allowed in a properly formed URL, such as Unicode characters, will be percent escaped.

To decode an encoded link, use the `String` property [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding). You must also return `true` in the `BrazeDelegate.braze(_:shouldOpenURL:)`. A call to action is required to trigger the handling of the URL by your app. For example:

{% tabs %}
{% tab swift %}

```swift
  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let urlString = url.absoluteString.removingPercentEncoding
    // Handle urlString
    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url options:(NSDictionary<NSString *, id> *)options {
  NSString *urlString = [url.absoluteString stringByRemovingPercentEncoding];
  // Handle urlString
  return YES;
}
```

{% endtab %}
{% endtabs %}

## Deep linking to app settings

You can take advantage of `UIApplicationOpenSettingsURLString` to deep link users to your app's settings from Braze push notifications, in-app messages, and the News Feed.

To take users from your app into the iOS settings:
1. First, make sure your application is set up for either [scheme-based deep links](#swift_register-a-scheme) or [universal links](#swift_universal-links).
2. Decide on a URI for deep linking to the **Settings** page (for example, `myapp://settings` or `https://www.braze.com/settings`).
3. If you are using custom scheme-based deep links, add the following code to your `application:openURL:options:` method:

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let path = url.path
  if (path == "settings") {
    UIApplication.shared.openURL(URL(string:UIApplication.openSettingsURLString)!)
  }
  return true
}
```

{% endtab %}
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
{% endtabs %}

## Customization options {#customization-options}

### Default WebView customization

The `Braze.WebViewController` class displays web URLs opened by the SDK, typically when "Open Web URL Inside App" is selected for a web deep link.

You can customize the `Braze.WebViewController` via the [`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/) delegate method.

### Linking handling customization

The `BrazeDelegate` protocol can be used to customize the handling of URLs such as deep links, web URLs, and universal links. To set the delegate during Braze initialization, set a delegate object on the `Braze` instance. Braze will then call your delegate's implementation of `shouldOpenURL` before handling any URIs.

#### Universal links {#universal-links}

Braze supports universal links in push notifications, in-app messages, and Content Cards. To enable universal link support, [`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) must be set to `true`.

When enabled, Braze will forward universal links to your app's `AppDelegate` via the [`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) method. 

Your application also needs to be set up to handle universal links. Refer to [Apple's documentation](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) to ensure your application is configured correctly for universal links.

{% alert warning %}
Universal link forwarding requires access to the application entitlements. When running the application in a simulator, these entitlements are not directly available and universal links are not forwarded to the system handlers.
To add support to simulator builds, you can add the application `.entitlements` file to the _Copy Bundle Resources_ build phase. See [`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) documentation for more details.
{% endalert %}

{% alert note %}
The SDK does not query your domains' `apple-app-site-association` file. It performs the differentiation between universal links and regular URLs by looking at the domain name only. As a result, the SDK does not respect any exclusion rule defined in the `apple-app-site-association` per [Supporting associated domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains).
{% endalert %}

## Examples

### BrazeDelegate

Here's an example using `BrazeDelegate`. For more information, see [Braze Swift SDK reference](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate).

{% tabs %}
{% tab swift %}

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if context.url.host == "MY-DOMAIN.com" {
    // Custom handle link here
    return false
  }
  // Let Braze handle links otherwise
  return true
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)braze:(Braze *)braze shouldOpenURL:(BRZURLContext *)context {
  if ([[context.url.host lowercaseString] isEqualToString:@"MY-DOMAIN.com"]) {
    // Custom handle link here
    return NO;
  }
  // Let Braze handle links otherwise
  return YES;
}
```

{% endtab %}
{% endtabs %}
