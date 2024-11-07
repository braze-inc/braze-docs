---
nav_title: ディープリンク
article_title: iOS のディープリンク
platform: Swift
page_order: 1
description: "この記事では、iOS アプリにユニバーサルディープリンクデリゲートを実装する方法と、Swift SDK のアプリ設定にディープリンクする方法の例を紹介します。"

---

# ディープリンク

> ディープリンクは、ネイティブアプリを起動したり、特定のコンテンツを表示したり、特定のアクションを実行したりするリンクを提供する手段です。iOS アプリにディープリンクを初めて実装する場合は、次のステップに従ってください。

ディープリンクに関する一般情報については、[よくある質問の記事]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking)を参照してください。 

## ステップ 1:スキームの登録

ディープリンクを処理するには、`Info.plist` ファイルにカスタムスキームを記述する必要があります。ナビゲーション構造はディクショナリの配列によって定義されます。これらの各ディクショナリには、文字列の配列が含まれています。

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
        <string>YOUR.SCHEME</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>YOUR.SCHEME</string>
        </array>
    </dict>
</array>
```

## ステップ2:スキーム許可リストの追加

`LSApplicationQueriesSchemes` キーをアプリの Info.plist ファイルに追加して、`canOpenURL(_:)` に渡す URL スキームを宣言する必要があります。この許可リストに含まれないスキームを呼び出そうとすると、デバイスのログにエラーが記録され、ディープリンクは開かれません。以下はこのエラーの例です。

```
<Warning>: -canOpenURL: failed for URL: "yourapp://deeplink" – error: "This app is not allowed to query for scheme yourapp"
```

たとえば、アプリ内メッセージをタップしたときに Facebook アプリが開かれるようにするには、アプリの許可リストに Facebook カスタムスキーム (`fb`) が含まれている必要があります。含まれていないと、ディープリンクが拒否されます。自分のアプリ内のページやビューに誘導するディープリンクでも、アプリのカスタムスキームがアプリの `Info.plist` に含まれている必要があります。

以下は許可リストの例です。

```html
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>myapp</string>
    <string>fb</string>
    <string>twitter</string>
</array>
```

詳細については、`LSApplicationQueriesSchemes` キーに関する [Apple のドキュメント](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14)を参照してください。

## ステップ 3: ハンドラの実装

アプリをアクティブにすると、iOS でメソッド [`application:openURL:options:`](https://developer.apple.com/reference/uikit/uiapplicationdelegate/1623112-application?language=objc) が呼び出されます。重要な引数は [NSURL](https://developer.apple.com/library/ios/DOCUMENTATION/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSURL) オブジェクトです。

{% tabs %}
{% tab SWIFT %}

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

## アプリトランスポートセキュリティ (ATS)

### ATS の要件
[Apple のドキュメント](https://developer.apple.com/library/prerelease/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS9.html#//apple_ref/doc/uid/TP40016198-SW14)から:「アプリトランスポートセキュリティは、アプリと Web サービス間の接続のセキュリティを向上させる機能です。この機能は、安全な接続のベストプラクティスに準拠したデフォルトの接続要件で構成されています。アプリでこのデフォルト動作を無効にして、トランスポートセキュリティを無効にできます。」

ATS はデフォルトで適用されます。すべての接続が HTTPS を使用し、TLS 1.2を使用して暗号化され、前方秘匿性が確保される必要があります。詳細については、[ATS を使用して接続するための要件](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35)を参照してください。Braze によりエンドデバイスに提供されるすべての画像は、TLS 1.2をサポートし、ATS と互換性のあるコンテンツ配信ネットワーク (「CDN」) によって処理されます。

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

ATS は、次の3つの方法のいずれかで処理できます。

#### すべてのリンクが ATS に準拠するようにする (推奨)
(アプリ内メッセージやプッシュキャンペーンなどから) ユーザーを誘導する既存のリンクが ATS の要件を満たすようにすることで、Braze 統合が ATS 要件を満たすことができます。ATS の制限を回避する方法はありますが、リンクされたすべての URL が ATS に準拠するようにすることをお勧めします。Apple がアプリケーションのセキュリティをこれまで以上に重視していることを考えると、ATS の例外を許可する以下のアプローチが Apple によってサポートされる保証はありません。

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

## URL エンコーディング

SDK では、有効な `URL` を作成するためにリンクをパーセントエンコードします。適切な形式の URL で使用できないリンク文字 (ユニコード文字など) は、すべてパーセントエスケープされます。

エンコードされたリンクをデコードするには、`String` プロパティ [`removingPercentEncoding`](https://developer.apple.com/documentation/swift/stringprotocol/removingpercentencoding) を使用します。また、`BrazeDelegate.braze(_:shouldOpenURL:)` で `true` を返す必要があります。アプリによる URL の処理をトリガーするには、アクションの呼び出しが必要です。 

以下はその例です。

{% tabs %}
{% tab SWIFT %}

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


## アプリ設定へのディープリンク

`UIApplicationOpenSettingsURLString` を利用して、Braze のプッシュ通知、アプリ内メッセージ、ニュースフィードからアプリの設定にユーザーをディープリンクできます。

ユーザーをアプリから iOS 設定に移動させる手順は以下のとおりです。
1. まず、アプリケーションが[スキームベースのディープリンク](##step-1-registering-a-scheme)または[ユニバーサルリンク](#universal-links)用に設定されていることを確認します。
2. [**設定**] ページへのディープリンクの URI (`myapp://settings` や `https://www.braze.com/settings` など) を決定します。
3. カスタムスキームベースのディープリンクを使用している場合は、`application:openURL:options:` メソッドに次のコードを追加します。

{% tabs %}
{% tab SWIFT %}

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

## カスタマイズ {#linking-customization}

### デフォルト WebView のカスタマイズ

一般的に Web ディープリンクに対して [アプリ内で Web URL を開く] が選択されている場合、`Braze.WebViewController` クラスには SDK によって開かれる Web URL が表示されます。

`Braze.WebViewController` は、[`BrazeDelegate.braze(_:willPresentModalWithContext:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:willpresentmodalwithcontext:)-12sqy/) デリゲートメソッドを使用してカスタマイズできます。

### リンク処理のカスタマイズ

`BrazeDelegate` プロトコルを使用して、ディープリンク、Web URL、ユニバーサルリンクなどの URL の処理をカスタマイズできます。Braze の初期化中にデリゲートを設定するには、`Braze` インスタンスでデリゲートオブジェクトを設定します。その後、URI を処理する前に Braze で `shouldOpenURL` のデリゲートの実装が呼び出されます。

#### ユニバーサルリンク

Braze では、プッシュ通知、アプリ内メッセージ、コンテンツカードでユニバーサルリンクがサポートされています。ユニバーサルリンクのサポートを有効にするには、[`configuration.forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) を `true` に設定する必要があります。

有効にすると、[`application:continueUserActivity:restorationHandler:`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623072-application) メソッドを使用して Braze からアプリの`AppDelegate` にユニバーサルリンクが転送されます。 

また、ユニバーサルリンクを処理するようアプリケーションを設定する必要があります。[Apple のドキュメント](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app)を参照し、アプリケーションがユニバーサルリンクに関して正しく設定されていることを確認してください。

{% alert warning %}
ユニバーサルリンクを転送するには、アプリケーション権限にアクセスできる必要があります。アプリケーションをシミュレーターで実行している場合、これらの権限を直接使用できず、ユニバーサルリンクはシステムハンドラに転送されません。
シミュレータービルドのサポートを追加するには、`.entitlements` アプリケーションファイルを _Copy Bundle Resources_ ビルドフェーズに追加できます。詳細については、[`forwardUniversalLinks`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks) のドキュメントを参照してください。
{% endalert %}

{% alert note %}
SDK では、ドメインの `apple-app-site-association` ファイルに対してクエリが実行されません。ドメイン名のみを確認することで、ユニバーサルリンクと通常の URL が区別されます。そのため、SDK では[サポート関連ドメイン](https://developer.apple.com/documentation/xcode/supporting-associated-domains)ごとに `apple-app-site-association` で定義される除外ルールが考慮されません。
{% endalert %}

### 統合の例: BrazeDelegate

{% tabs %}
{% tab SWIFT %}

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

詳細については、[`BrazeDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate) を参照してください。


