{% multi_lang_include inapp_message_troubleshooting.md sdk="iOS" %}

### アセット読み込みのトラブルシューティング (`NSURLError` コード `-1008`)

Braze とサードパーティのネットワークロギングライブラリを統合する場合、開発者はドメインコード `-1008` の `NSURLError` に遭遇することがよくあります。このエラーは、画像やフォントなどのアセットが取得できなかったか、キャッシュできなかったことを示しています。このようなケースを回避するには、Braze CDNのURLを、これらのライブラリーによって無視されるべきドメインのリストに登録する必要がある。

#### ドメイン

CDNドメインの全リストは以下の通り：

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### 例

以下は、Brazeのアセットキャッシュと競合することが知られているライブラリーと、その問題を回避するためのサンプルコードである。使用できないリソース・エラーを引き起こすライブラリを使用しているプロジェクトで、以下にリストアップされていない場合は、そのライブラリのドキュメントを参照して、同様の使用APIを確認してほしい。

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


