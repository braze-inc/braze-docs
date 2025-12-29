---
nav_title: ディープリンク
article_title: iOS のディープリンク
platform: iOS
page_order: 0
description: "この記事では、iOS アプリにユニバーサルディープリンクデリゲートを実装する方法と、アプリ設定にディープリンクする方法の例を紹介します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOS のディープリンク

ディープリンクの基本情報については、[ユーザーガイドの記事]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)を参照してください。Braze アプリにディープリンクを初めて実装する場合は、以下の手順で開始できます。

## ステップ1:スキームを登録する

`Info.plist` ファイルでカスタムスキームを記述する必要があります。ナビゲーション構造はディクショナリの配列によって定義されます。これらの各ディクショナリには、文字列の配列が含まれています。

Xcode を使用して `Info.plist` ファイルを編集します。

1. 新しいキー `URL types` を追加します。Xcode では、これが自動的に `Item 0` というディクショナリを含む配列になります。
2. `Item 0` 内に、キー `URL identifier` を追加します。カスタムスキームに値を設定します。
3. `Item 0` 内に、キー `URL Schemes` を追加します。これは、自動的に `Item 0` 文字列を含む配列になります。
4. `URL Schemes` >> `Item 0` をカスタムスキームに設定します。

また、`Info.plist` ファイルを直接編集する場合は、次の仕様に従うこともできます。

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

## ステップ2:カスタムスキームを許可リストに登録する (iOS 9 以降)

iOS 9 以降では、アプリが開くことを許可されているカスタムスキームの許可リストが必要です。このリストに含まれないスキームを呼び出そうとすると、デバイスのログにエラーが記録され、ディープリンクは開かれません。以下はこのエラーの例です。

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

たとえば、アプリ内メッセージをタップしたときに Facebook アプリが開かれるようにするには、アプリの許可リストに Facebook カスタムスキーム (`fb`) が含まれている必要があります。含まれていないと、ディープリンクが拒否されます。自分のアプリ内のページやビューに誘導するディープリンクでも、アプリのカスタムスキームがアプリの `Info.plist` に含まれている必要があります。

アプリの `Info.plist` がディープリンクする必要があるすべてのスキームを、キー `LSApplicationQueriesSchemes` を使用してアプリの許可リストに追加する必要があります。以下に例を示します。

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>facebook</string>
    <string>twitter</string>
</array>
```

詳細については、`LSApplicationQueriesSchemes` キーに関する [Apple のドキュメント](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14)を参照してください。

## ステップ3: ハンドラの実装

アプリをアクティブにすると、iOS でメソッド [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc) が呼び出されます。重要な引数は [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL) オブジェクトです。

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

![]({% image_buster /assets/img_archive/deep_link.png %})

# ユニバーサルリンク

ユニバーサルリンクを使用するには、登録済みのドメインがアプリの機能に追加され、`apple-app-site-association` ファイルがアップロードされていることを確認してください。その後で、メソッド `application:continueUserActivity:restorationHandler:` を `AppDelegate` に実装します。以下に例を示します。

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

詳細については、[Apple](https://developer.apple.com/library/content/documentation/General/Conceptual/AppSearch/UniversalLinks.html)を参照してください。

{% alert note %}
デフォルトのユニバーサルリンク統合は、Braze プッシュ通知、アプリ内メッセージドと互換性がありません。アプリケーション内のユニバーサルリンクを処理するには、「[リンクのカスタマイズを](#linking-handling-customization)」を参照してください。または、プッシュ通知、アプリ内メッセージで[スキームベースのディープリンク](#step-1-registering-a-scheme)を使用することをお勧めします。
{% endalert%}

## アプリトランスポートセキュリティ (ATS)
iOS 9では、アプリ内メッセージやプッシュ通知に埋め込まれたWeb URLに影響を与える変更が導入された。

### ATS の要件
[Apple のドキュメント](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14)から:「アプリトランスポートセキュリティは、アプリと Web サービス間の接続のセキュリティを向上させる機能です。この機能は、安全な接続のベストプラクティスに準拠したデフォルトの接続要件で構成されています。アプリでこのデフォルト動作を無効にして、トランスポートセキュリティを無効にできます。」

ATS は iOS 9 以降にデフォルトで適用されます。すべての接続が HTTPS を使用し、TLS 1.2を使用して暗号化され、前方秘匿性が確保される必要があります。詳細については、[ATS を使用して接続するための要件](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35)を参照してください。Braze によりエンドデバイスに提供されるすべての画像は、TLS 1.2をサポートし、ATS と互換性のあるコンテンツ配信ネットワーク (「CDN」) によって処理されます。

アプリケーションの `Info.plist` で例外として指定されていない限り、これらの要件に従わない接続は次のようなエラーにより失敗します。

```
CFNetwork SSLHandshake failed (-9801)
Error Domain=NSURLErrorDomain Code=-1200 "An SSL error has occurred, and a secure connection to the server cannot be made."
```

```
NSURLSession/NSURLConnection HTTP load failed (kCFStreamErrorDomainSSL, -9802)
```

ATS コンプライアンスは、モバイルアプリ内で開かれたリンク (クリックされたリンクのデフォルト処理) に適用され、Web ブラウザーから外部で開かれたサイトには適用されません。

### ATS 要件の処理

ATS は、次の 3 つの方法のいずれかで処理できます。

#### すべてのリンクが ATS に準拠していることを確認する (推奨)
(アプリ内メッセージやプッシュキャンペーンから) ユーザーを誘導する既存のリンクが ATS の要件を満たすようにすることで、Braze 統合が ATS 要件を満たすことができます。ATS の制限を回避する方法はありますが、リンクされたすべての URL が ATS に準拠するようにすることをお勧めします。Apple がアプリケーションのセキュリティをこれまで以上に重視していることを考えると、ATS の例外を許可する以下のアプローチが Apple によってサポートされる保証はありません。

SSL ツールにより、Web サーバーのセキュリティの問題を正確に特定できます。このQualys, Inc. の[SSL サーバーテスト](https://www.ssllabs.com/ssltest/index.html) は、Apple ATS 9 およびiOS 9 への準拠に特化したラインアイテムを提供します。

#### ATS を一部無効にする
特定のドメインやスキームのリンクのサブセットを ATS ルールの例外として処理することを許可できます。Braze メッセージングチャネルで使用するすべてのリンクが ATS に準拠しているか、例外として処理されている場合、Braze 統合は ATS 要件を満たします。

ATS の例外としてドメインを追加するには、アプリの `Info.plist` ファイルに以下を追加します。

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

詳細については、[アプリトランスポートセキュリティのキー](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW33)に関する Apple の記事を参照してください。

#### ATS を完全に無効にする

ATS を完全に無効にできます。ただし、セキュリティ保護が失われることと、将来の iOS との互換性の両方を考慮して、この処理は推奨されないことに注意してください。ATS を無効にするには、アプリの `Info.plist` ファイルに以下を挿入します。

```html
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

ATS エラーをデバッグする方法の詳細については、[[アプリトランスポートセキュリティを使用したアプリの配布]](http://timekl.com/blog/2015/08/21/shipping-an-app-with-app-transport-security/?utm_campaign=iOS+Dev+Weekly&utm_medium=email&utm_source=iOS_Dev_Weekly_Issue_213) を参照してください。

## URL エンコーディング

Braze iOS SDK v2.21.0 以降、SDK はリンクをパーセントエンコードして有効な `NSURL` を作成します。適切な形式の URL で使用できないリンク文字 (ユニコード文字など) は、すべてパーセントエスケープされます。

エンコードされたリンクをデコードするには、`NSString` メソッド [`stringByRemovingPercentEncoding`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSString_Class/index.html#//apple_ref/occ/instm/NSString/stringByRemovingPercentEncoding) を使用します。また、`ABKURLDelegate` の `YES` を返す必要があり、アプリによる URL の処理を​​トリガーするには、CTA が必要です。以下に例を示します。

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

## カスタマイズ {#linking-customization}

### デフォルト WebView のカスタマイズ

一般的に Web ディープリンクに対して [アプリ内で Web URL を開く] が選択されている場合、カスタマイズ可能な `ABKModalWebViewController` クラスには SDK によって開かれる Web URL が表示されます。

`ABKModalWebViewController` クラスのカテゴリを宣言するか、直接変更して、Web ビューにカスタマイズを適用できます。詳細については、このクラスの [.h ファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKModalWebViewController.h)と [.m ファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/ABKModalWebViewController.m)をご確認ください。

### リンク処理のカスタマイズ

`ABKURLDelegate` プロトコルを使用して、ディープリンク、Web URL、ユニバーサルリンクなどの URL の処理をカスタマイズできます。Braze の初期化中にデリゲートを設定するには、[[`startWithApiKey:inApplication:withAppboyOptions:`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) の `appboyOptions` の `ABKURLDelegateKey` にデリゲートオブジェクトを渡します。その後、URI を処理する前に Braze で `handleAppboyURL:fromChannel:withExtras:` のデリゲートの実装が呼び出されます。

#### 統合の例:ABKURLDelegate

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

詳細については、[`ABKURLDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKURLDelegate.h) を参照してください。

## よくあるユースケース

### アプリ設定へのディープリンク

iOS は、アプリから iOS 設定アプリケーションのページにユーザーを誘導できます。`UIApplicationOpenSettingsURLString` を利用して、プッシュ通知、アプリ内メッセージから設定にユーザーをディープリンクできます。

1. まず、アプリケーションが[スキームベースのディープリンク](#deep-links)または[ユニバーサルリンク](#universal-links)用に設定されていることを確認します。
2. [**設定**] ページへのディープリンクの URI (`myapp://settings` や `https://www.braze.com/settings` など) を決定します。
3. カスタムスキームベースのディープリンクを使用している場合は、`application:openURL:options:` メソッドに次のコードを追加します。

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

