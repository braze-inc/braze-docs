---
nav_title: SDK認証
article_title: SDK認証
page_order: 2
description: "この参考記事では、SDK認証と、Braze SDKでこの機能を有効にする方法について説明する。"
platform:
  - iOS
  - Android
  - Web
  
---

# SDK認証

> SDK認証では、ログインしたユーザーの代わりに行われたSDKリクエストに対して、暗号化証明（サーバーサイドで生成）を提供することができる。

アプリでこの機能を有効にすると、BrazeダッシュボードでJSON Web Token (JWT)署名が無効または見つからないリクエストを拒否するように設定できる：

- カスタムイベント、属性、購入、セッションデータを送信する
- Brazeワークスペースに新しいユーザーを作成する
- 標準ユーザープロファイル属性を更新する
- メッセージを受信またはトリガーする

これで、認証されていないログイン・ユーザーが、アプリのSDK APIキーを使って、他のユーザーになりすますなどの悪意のあるアクションを実行するのを防ぐことができる。

## はじめに

始めるには4つのハイレベルなステップがある：

1. [サーバー・サイドの統合][1]\- 公開鍵と秘密鍵のペアを生成し、秘密鍵を使って現在ログインしているユーザーのJWTを作成する。<br><br>
2. [SDKインテグレーション][2]\- Braze SDKでこの機能を有効にし、サーバーから生成されたJWTをリクエストする。<br><br>
3. [公開鍵の追加][3]-**管理設定**ページのBrazeダッシュボードに_公開鍵を_追加する。<br><br>
4. [Brazeダッシュボード内で強制を切り替える][4]\- アプリごとにBrazeダッシュボード内でこの機能の強制を切り替える。

## サーバーサイドの統合 {#server-side-integration}

### 公開鍵と秘密鍵のペアを生成する。 {#generate-keys}

RSA256公開鍵/秘密鍵ペアを生成する。公開鍵は最終的にBrazeのダッシュボードに追加されるが、秘密鍵はサーバーに安全に保管する必要がある。

RS256 JWTアルゴリズムで使用する2048ビットのRSA鍵を推奨する。

{% alert warning %}
秘密鍵は_秘密にして_おくことを忘れないこと。アプリやウェブサイトに秘密鍵を公開したり、ハードコードしたりしてはならない。あなたの秘密鍵を知っている人なら誰でも、あなたのアプリケーションに代わってユーザーになりすましたり、ユーザーを作成したりすることができる。
{% endalert %}

### 現在のユーザーのJSONウェブトークンを作成する {#create-jwt}

秘密鍵が手に入ったら、サーバー側のアプリケーションはそれを使って、現在ログインしているユーザーのJWTをアプリやウェブサイトに返さなければならない。

典型的には、このロジックは、ログインエンドポイントやアプリが現在のユーザーのプロファイルをリフレッシュする場所など、アプリが現在のユーザーのプロファイルを通常リクエストする場所に置くことができる。

JWTを生成する際には、以下のフィールドが期待される：

**JWTヘッダー**

| フィールド | required | 説明                         |
| ----- | -------- | ----------------------------------- |
| `alg` | はい  | サポートされているアルゴリズムは`RS256` である。 |
| `typ` | はい  | 型は`JWT` と等しくなければならない。        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**JWTペイロード**

| フィールド | required | 説明                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | はい  | subject "は、Braze SDKを呼び出すときに指定したユーザーIDと同じでなければならない。 `changeUser`  |
| `exp` | はい | このトークンの有効期限を指定する。                                |
| `aud` | いいえ       | audience "の指定は任意であり、指定された場合、以下のようになる。 `braze`                      |
| `iss` | いいえ       | issuer "は省略可能で、設定する場合はSDK API Keyと等しくなければならない。              |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### JWTライブラリ

JSONウェブトークンについての詳細や、この署名プロセスを簡素化する多くのオープンソースライブラリを参照するには、[https://jwt.io](https://jwt.io) をチェックしてほしい。

## SDKの統合 {#sdk-integration}

この機能は、以下の\[SDKバージョン]({{ site.baseurl }}/user_guide/engagement_)で利用可能である。tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
iOSインテグレーションについては、このページでBraze Swift SDKの手順を詳しく説明する。レガシーAppboyKit iOS SDKでの使用例については、[この](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m)ファイルと[このファイルを](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)参照。
{% endalert %}

### Braze SDKでこの機能を有効にする。

この機能が有効な場合、Braze SDKは、Brazeサーバーへのネットワークリクエストに、現在のユーザーの最後の既知のJWTを追加する。

{% alert note %}
このオプションだけで初期化しても、Brazeダッシュボード内で[認証の適用を](#braze-dashboard)開始するまでは、データ収集には何の影響もないのでご心配なく。
{% endalert %}

{% tabs %}
{% tab ジャバスクリプト %}
`initialize` を呼び出す際には、オプションの`enableSdkAuthentication` プロパティを`true` に設定する。
```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab ジャワ %}
Appboyインスタンスをコンフィギュレーションする際、`setIsSdkAuthenticationEnabled` を`true` にコールする。
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

あるいは、braze.xml に`<bool name="com_braze_sdk_authentication_enabled">true</bool>` を追加することもできる。
{% endtab %}
{% tab KOTLIN %}
Appboyインスタンスをコンフィギュレーションする際、`setIsSdkAuthenticationEnabled` を`true` にコールする。
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

あるいは、braze.xml に`<bool name="com_braze_sdk_authentication_enabled">true</bool>` を追加することもできる。
{% endtab %}
{% tab Objective-C %}
SDK認証を有効にするには、Brazeインスタンスを初期化する前に、`BRZConfiguration` オブジェクトの`configuration.api.sdkAuthentication` プロパティを`YES` ：

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab スウィフト %}
SDK認証を有効にするには、SDKを初期化する際に、`Braze.Configuration` オブジェクトの`configuration.api.sdkAuthentication` プロパティを`true` に設定する：

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab ダート %}
現在、SDK認証は、iOSとAndroidのネイティブ・コードでSDKを初期化する一環として有効にする必要がある。Flutter SDKでSDK Authenticationを有効にするには、他のタブからiOSとAndroidのインテグレーションに従う。SDK認証を有効にした後、残りの機能をDartに統合することができる。
{% endtab %}
{% endtabs %}

### 現在のユーザーのJWTトークンを設定する

アプリがBrazeの`changeUser` メソッドを呼び出すときは常に、[サーバーサイドで生成さ][4]れたJWTトークンも供給する。

また、トークンが現在のユーザーのセッションの途中でリフレッシュされるように設定することもできる。

{% alert note %}
`changeUser` 、ユーザーIDが_実際に変更さ_れたときのみコールされるべきであることに留意されたい。ユーザーIDが変更されていない場合、署名を更新する方法としてこのメソッドを使用してはならない。
{% endalert %}

{% tabs %}
{% tab ジャバスクリプト %}
を呼び出す際にJWTトークンを提供する。 [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
):

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```javascript
import * as braze from"@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab ジャワ %}

を呼び出す際にJWTトークンを提供する。 [`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-):

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

を呼び出す際にJWTトークンを提供する。 [`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-):

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER")
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

を呼び出す際にJWTトークンを提供する。 [`changeUser`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69):

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"signature"];
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"signature"];
```
{% endtab %}
{% tab スウィフト %}

を呼び出す際にJWTトークンを提供する。 [`changeUser`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69):

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "signature")
```
あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "signature")
```
{% endtab %}
{% tab ダート %}

を呼び出す際にJWTトークンを提供する。 [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```dart
braze.changeUser("userId", sdkAuthSignature: "signature")
```
あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```dart
braze.setSdkAuthenticationSignature("signature")
```

{% endtab %}
{% endtabs %}

### 無効なトークンのコールバック関数を登録する {#sdk-callback}

この機能が[Requiredに](#enforcement-options)設定されている場合、以下のシナリオでSDKリクエストがBrazeによって拒否される：
- Braze APIが受信した時点でJWTの有効期限が切れていた。
- JWTが空か行方不明だった
- Brazeダッシュボードにアップロードした公開鍵のJWT検証に失敗した。

`subscribeToSdkAuthenticationFailures` を使って、SDKリクエストがこれらの理由で失敗したときに通知されるようにサブスクライブすることができる。コールバック関数は、エラーに関連する \[`errorCode`][9],`reason` ]、リクエストの`userId` （ユーザーが匿名でない場合）、およびエラーの原因となった認証`signature` を含むオブジェクトを含む。 

失敗したリクエストは、アプリが新しい有効なJWTを提供するまで、定期的に再試行される。そのユーザーがまだログインしている場合、このコールバックをサーバーに新しいJWTを要求する機会として使用し、この新しい有効なトークンをBraze SDKに供給することができる。

{% alert tip %}
これらのコールバックメソッドは、独自の監視サービスやエラーログサービスを追加して、Brazeリクエストが拒否される頻度を追跡するのに最適な場所である。
{% endalert %}

{% tabs %}
{% tab ジャバスクリプト %}
```javascript
import * as braze from"@braze/web-sdk";
braze.subscribeToSdkAuthenticationFailures((error) => {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  const updated_jwt = await getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(updated_jwt);
});
```
{% endtab %}
{% tab ジャワ %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the error user matches the currently logged-in user
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    // TODO: Optionally log to your error-reporting service
    // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  NSLog(@"Invalid SDK Authentication signature.");
  NSString *newSignature = getNewSignatureSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab スウィフト %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab ダート %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(error)
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% endtabs %}

## 公開鍵を管理する {#key-management}

### 公開鍵を追加する

アプリごとに、プライマリ、セカンダリ、ターシャリの3つまで公開鍵を追加できる。必要に応じて、同じキーを複数のアプリに追加することもできる。公開鍵を追加する：

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択する。
2. 利用可能なアプリのリストからアプリを選ぶ。
3. **SDK Authenticationで**、**Add Public Keyを**選択する。
4. オプションの説明を入力し、公開鍵を貼り付け、**Add Public Keyを**選択する。

### 新しい主キーを割り当てる

セカンダリ・キーまたはターシャリ・キーを新しいプライマリ・キーとして割り当てる：

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択する。
2. 利用可能なアプリのリストからアプリを選ぶ。
3. **SDK Authenticationで**キーを選択し、**Manage**>**Make Primary Keyを**選択する。

### キーを削除する

プライマリ・キーを削除するには、まず[新しいプライマリを割り当て](#assign-a-new-primary-key)、それからキーを削除する。非プライマリキーを削除するには

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択する。
2. 利用可能なアプリのリストからアプリを選ぶ。
3. **SDK Authenticationで**プライマリ・キー以外のキーを選択し、**Manage**>**Delete Public Keyを**選択する。

## Brazeのダッシュボードで有効にする {#braze-dashboard}

[サーバーサイド・インテグレーションと][1] [SDKインテグレーションが][2]完了したら、特定のアプリに対してこの機能を有効にし始めることができる。

アプリのSDK認証設定がBrazeダッシュボードで**Requiredに**設定されていない限り、SDKリクエストは認証なしで通常通り流れ続けることに留意すること。

統合に何か問題が発生した場合（例えば、アプリがSDKにトークンを不正に渡している、またはサーバーが無効なトークンを生成している）、Brazeダッシュボードでこの機能を無効にすると、データは検証なしで通常通り流れるようになる。

### 執行オプション {#enforcement-options}

ダッシュボードの**管理設定**ページでは、各アプリに3つのSDK認証ステートがあり、Brazeがどのようにリクエストを検証するかを制御する。

| セッティング| 説明|
| ------ | ---------- |
| **無効** | Brazeは、ユーザーに提供されたJWTを検証しない。(デフォルト設定）|
| **オプション** | Brazeは、ログインしているユーザーのリクエストを確認するが、無効なリクエストは拒否しない。 |
| **required** | Brazeは、ログインしているユーザーのリクエストを検証し、無効なJWTは拒否する。|
{: .reset-td-br-1 .reset-td-br-2}

![][8]

**Optional**設定は、この機能がアプリのSDKトラフィックに与える潜在的な影響を監視するのに便利な方法である。

無効なJWT署名は**Optionalと** **Requiredの**両方の状態で報告されるが、**Requiredの**状態だけがSDK要求を拒否し、アプリが再試行して新しい署名を要求する原因となる。

## 分析 {#analytics}

各アプリは、この機能が**Optionalと** **Requiredの**状態で収集されたSDK認証エラーの内訳を表示する。

データはリアルタイムで入手でき、チャート上のポイントにカーソルを合わせると、指定した日付のエラーの内訳を見ることができる。

![認証エラーの発生件数を示すグラフ。また、エラーの総数、エラーの種類、調整可能な日付範囲も表示される。][10]{: style="max-width:80%"}

## エラーコード {#error-codes}

| エラーコード| エラー理由 | 説明 |
| --------  | ------------ | ---------  |
| 10 | `EXPIRATION_REQUIRED` | 有効期限はBrazeを使用するための必須項目である。|
| 20 | `DECODING_ERROR` | 公開鍵が一致しないか、一般的な捕捉不能エラーが発生した。|
| 21 | `SUBJECT_MISMATCH` | 期待される対象者と実際の対象者は同じではない。|
| 22 | `EXPIRED` | 提供されたトークンの有効期限が切れた。|
| 23 | `INVALID_PAYLOAD` | トークンのペイロードが無効である。|
| 24 | `INCORRECT_ALGORITHM` | トークンのアルゴリズムはサポートされていない。|
| 25 | `PUBLIC_KEY_ERROR` | 公開鍵が適切な形式に変換できなかった。|
| 26 | `MISSING_TOKEN` | リクエストにトークンが指定されていない。|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | 提供されたトークンに一致する公開鍵がなかった。|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | リクエストのペイロードに含まれるすべてのユーザーIDが、要求されたものと一致するわけではない。|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## よくある質問 {#faq}

#### この機能はすべてのアプリで同時に有効にする必要があるのか？ {#faq-app-by-app}

いや、この機能は特定のアプリで有効にすることができ、すべてのアプリで一度に使う必要はない。

#### 私のアプリの古いバージョンを使っているユーザーはどうなるのか？ {#faq-sdk-backward-compatibility}

この機能を実行し始めると、古いバージョンのアプリによるリクエストはBrazeによって拒否され、SDKによって再試行される。ユーザーがアプリをサポートされたバージョンにアップグレードすると、キューに入れられたリクエストは再び受け入れられるようになる。

可能であれば、他の必須アップグレードと同様に、ユーザーにアップグレードを促すべきである。あるいは、許容できる割合のユーザーがアップグレードしたことを確認するまで、この機能を[オプショナルにして][6]おくこともできる。

#### JWTトークンを生成する際、どのような期限を使用すべきか？ {#faq-expiration}

平均セッション時間、セッションクッキー/トークンの有効期限、またはアプリケーションが現在のユーザーのプロファイルを更新する頻度のうち、高い方の値を使用することを推奨する。

#### ユーザーのセッションの途中でJWTの有効期限が切れた場合はどうなるのか？ {#faq-jwt-expiration}

ユーザーのトークンがセッションの途中で期限切れになった場合、SDKは[コールバック関数を][7]呼び出し、Brazeにデータを送信し続けるには新しいJWTトークンが必要であることをアプリに知らせる。

#### サーバーサイドの統合が壊れ、JWTを作成できなくなった場合はどうなるのか？ {#faq-server-downtime}

サーバーがJWTトークンを提供できない場合、または統合に問題がある場合は、Brazeのダッシュボードでいつでも機能を無効にできる。

一度無効にすると、保留中の失敗したSDKリクエストは最終的にSDKによって再試行され、Brazeによって受け入れられる。

#### なぜこの機能では、共有秘密鍵の代わりに公開鍵/秘密鍵を使うのか？ {#faq-shared-secrets}

共有秘密を使う場合、Brazeのダッシュボードページなど、その共有秘密にアクセスできる人なら誰でも、トークンを生成してエンドユーザーになりすますことができる。

その代わり、公開鍵/秘密鍵を使用することで、Brazeの従業員でさえ（ダッシュボードのユーザーはもちろん）秘密鍵にアクセスできないようにしている。

#### 拒否されたリクエストはどのように再試行されるのか？ {#faq-retry-logic}

認証エラーのためにリクエストが拒否されると、SDKはユーザーのJWT署名をリフレッシュするために使用されるコールバックを呼び出す。 

リクエストは指数バックオフアプローチを使用して定期的に再試行される。50回連続で失敗すると、次のセッション開始まで再試行は一時停止される。各SDKには、手動でデータフラッシュを要求するメソッドもある。

[1]: #server-side-integration
[2]: #sdk-integration
[3]: #key-management
[4]: #braze-dashboard
[5]: #create-jwt
[6]: #enforcement-options
[7]: #sdk-callback
[8]: {% image_buster /assets/img/sdk-auth-settings.png %}
[9]: \#エラーコード
[10]: {% image_buster /assets/img/sdk-auth-analytics.png %}
[11]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
