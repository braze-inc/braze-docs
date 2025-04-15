{% multi_lang_include inapp_message_troubleshooting.md sdk="iOS" %}

### Troubleshooting asset loading (`NSURLError` code `-1008`)

When integrating Braze alongside third-party network logging libraries, developers can commonly run into an `NSURLError` with the domain code `-1008`. This error indicates that assets like images and fonts could not be retrieved or failed to cache. To work around such cases, you will need to register Braze CDN URLs to the list of domains that should be ignored by these libraries.

#### Domains

The full list of CDN domains is as listed below:

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### Examples

Below are libraries that are known to conflict with Braze asset caching, along with example code to work around the issue. If your project uses a library that causes an unavailable resource error and is not listed below, consult the documentation of that library for similar usage APIs.

##### Netfox

{% tabs %}
{% tab Swift %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];
```
{% endtab %}
{% endtabs %}

##### NetGuard

{% tabs %}
{% tab Swift %}
```swift
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;
```
{% endtab %}
{% endtabs %}

##### XNLogger

{% tabs %}
{% tab Swift %}
```swift
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])
```
{% endtab %}
{% tab Objective-C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}


