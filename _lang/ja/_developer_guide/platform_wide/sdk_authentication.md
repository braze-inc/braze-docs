---
nav_title: SDK認証
article_title: SDK認証
page_order: 2
description: "この参考記事では、SDK 認証と、Braze SDK でこの機能を有効にする方法について説明します。"
platform:
  - iOS
  - Android
  - Web
  
---

# SDK認証

> SDK 認証を使用すると、ログインしているユーザーの代わりに行われた SDK リクエストに対して (サーバー側で生成された) 暗号証明を提供できます。

アプリでこの機能を有効にすると、次のような JSON Web トークン (JWT) 署名が無効または存在しないリクエストを拒否するように Braze ダッシュボードを設定できます。

- カスタムイベント、属性、購入、セッションデータを送信する
- Brazeワークスペースに新しいユーザーを作成する
- 標準ユーザープロファイル属性を更新する
- メッセージを受信またはトリガーする

これで、認証されていないログインユーザーが、アプリの SDK API キーを使って、他のユーザーになりすますなどの悪意のあるアクションを実行するのを防ぐことができます。

## はじめに

始めるには4つのハイレベルなステップがある：

1. [サーバー・サイドの統合][1]\- 公開鍵と秘密鍵のペアを生成し、秘密鍵を使って現在ログインしているユーザーのJWTを作成する。<br><br>
2. [SDK 統合][2]\- Braze SDK でこの機能を有効にし、サーバーから生成された JWT をリクエストします。<br><br>
3. [公開鍵の追加][3]-**管理設定**ページのBrazeダッシュボードに_公開鍵を_追加する。<br><br>
4. [Braze ダッシュボード内で適用を切り替える][4]\- Braze ダッシュボード内でアプリごとにこの機能の適用を切り替えます。

## サーバーサイドの統合 {#server-side-integration}

### 公開鍵と秘密鍵のペアを生成する。 {#generate-keys}

RSA256公開鍵/秘密鍵ペアを生成する。公開キーは最終的に Braze のダッシュボードに追加されますが、秘密キーはサーバーに安全に保管する必要があります。

RS256 JWTアルゴリズムで使用する2048ビットのRSA鍵を推奨する。

{% alert warning %}
秘密キーは_非公開_にしておくことを忘れないでください。アプリやウェブサイトに秘密鍵を公開したり、ハードコードしたりしてはならない。あなたの秘密キーを知っている人なら誰でも、あなたのアプリケーションに代わってユーザーになりすましたり、ユーザーを作成したりすることができます。
{% endalert %}

### 現在のユーザーのJSONウェブトークンを作成する {#create-jwt}

秘密キーが手に入ったら、サーバー側のアプリケーションはそれを使って、現在ログインしているユーザーのアプリまたは Web サイトに JWT を返す必要があります。

通常、このロジックは、アプリが通常現在のユーザーのプロファイルをリクエストする任意の場所に移動できます。たとえば、ログインエンドポイントや、アプリが現在のユーザープロファイルを更新する場所などです。

JWTを生成する際には、以下のフィールドが期待される：

**JWT ヘッダー**

| フィールド | 必須 | 説明                         |
| ----- | -------- | ----------------------------------- |
| `alg` | はい  | サポートされているアルゴリズムは`RS256` である。 |
| `typ` | はい  | タイプは `JWT` と同じでなければなりません。        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**JWT ペイロード**

| フィールド | 必須 | 説明                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | はい  | 「subject」は、`changeUser` の呼び出し時に Braze SDK に指定したユーザー ID と同じである必要があります。  |
| `exp` | はい | このトークンをいつ期限切れにするかの「有効期限」。                                |
| `aud` | いいえ       | 「オーディエンス」の指定は任意であり、設定する場合は `braze` と等しくなければなりません。                      |
| `iss` | いいえ       | 「発行者」はオプションで、設定する場合は SDK API キーと等しくなければなりません。              |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### JWTライブラリ

JSONウェブトークンについての詳細や、この署名プロセスを簡素化する多くのオープンソースライブラリを参照するには、[https://jwt.io](https://jwt.io) をチェックしてほしい。

## SDKの統合 {#sdk-integration}

この機能は、以下の \[SDKバージョン]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions): で利用可能です。

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
iOS 統合については、このページで Braze Swift SDK のステップを詳しく説明します。レガシー AppboyKit iOS SDK での使用例については、[このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m)と[このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)を参照してください。
{% endalert %}

### Braze SDKでこの機能を有効にする。

この機能が有効な場合、Braze SDK は、Braze サーバーに対して行われたネットワークリクエストに、現在のユーザーの最新の既知の JWT を追加します。

{% alert note %}
このオプションだけで初期化しても、Brazeダッシュボード内で[認証の適用を](#braze-dashboard)開始するまでは、データ収集には何の影響もないのでご心配なく。
{% endalert %}

{% tabs %}
{% tab JavaScript %}
`initialize` を呼び出す際には、オプションの `enableSdkAuthentication` プロパティを `true` に設定します。
```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab Java %}
Appboy インスタンスを構成する場合は、`setIsSdkAuthenticationEnabled` を呼び出して `true` に設定してください。
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

あるいは、braze.xml に`<bool name="com_braze_sdk_authentication_enabled">true</bool>` を追加することもできます。
{% endtab %}
{% tab KOTLIN %}
Appboy インスタンスを構成する場合は、`setIsSdkAuthenticationEnabled` を呼び出して `true` に設定してください。
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

あるいは、braze.xml に`<bool name="com_braze_sdk_authentication_enabled">true</bool>` を追加することもできます。
{% endtab %}
{% tab Objective-C %}
SDK 認証を有効にするには、Braze インスタンスを初期化する前に、`BRZConfiguration` オブジェクトの `configuration.api.sdkAuthentication` プロパティを `YES` に設定します。

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab SWIFT %}
SDK認証を有効にするには、SDKを初期化する際に、`Braze.Configuration` オブジェクトの`configuration.api.sdkAuthentication` プロパティを`true` に設定する：

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
現在、SDK 認証は、iOS と Android のネイティブコードで SDK を初期化する際に有効にする必要があります。Flutter SDK で SDK 認証を有効にするには、他のタブの iOS と Android の統合に従ってください。SDK 認証を有効にした後、残りの機能を Dart に統合することができます。
{% endtab %}
{% endtabs %}

### 現在のユーザーのJWTトークンを設定する

アプリが Braze `changeUser` メソッドを呼び出すたびに、[サーバー側で生成された][4] JWT トークンも指定します。

また、トークンが現在のユーザーのセッションの途中でリフレッシュされるように設定することもできる。

{% alert note %}
`changeUser` は、ユーザー ID が_実際に変更された_場合にのみ呼び出す必要があることに注意してください。ユーザーIDが変更されていない場合、署名を更新する方法としてこのメソッドを使用してはならない。
{% endalert %}

{% tabs %}
{% tab JavaScript %}
[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
) の呼び出し時に JWT トークンを指定する：

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
{% tab Java %}

[`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-) の呼び出し時に JWT トークンを指定する：

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

[`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-) の呼び出し時に JWT トークンを指定する：

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER")
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

[`changeUser`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69) の呼び出し時に JWT トークンを指定する：

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"signature"];
```

あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"signature"];
```
{% endtab %}
{% tab SWIFT %}

[`changeUser`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69) の呼び出し時に JWT トークンを指定する：

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "signature")
```
あるいは、セッションの途中でユーザーのトークンをリフレッシュした場合である：

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "signature")
```
{% endtab %}
{% tab Dart %}

[`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) の呼び出し時に JWT トークンを指定する：

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

`subscribeToSdkAuthenticationFailures` を使用して、これらのいずれかの理由で SDK リクエストが失敗したときに通知を受け取るようにサブスクライブできます。コールバック関数には、関連する \[`errorCode`][9]、エラーの `reason`、リクエストの `userId` (ユーザーが匿名でない場合)、およびエラーの原因となった認証 `signature` を備えたオブジェクトが含まれます。 

失敗したリクエストは、アプリが新しい有効な JWT を提供するまで、定期的に再試行されます。そのユーザーがまだログインしている場合、このコールバックをサーバーに新しいJWTを要求する機会として使用し、この新しい有効なトークンをBraze SDKに供給することができる。

{% alert tip %}
これらのコールバックメソッドは、独自の監視サービスやエラーログサービスを追加して、Brazeリクエストが拒否される頻度を追跡するのに最適な場所である。
{% endalert %}

{% tabs %}
{% tab JavaScript %}
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
{% tab Java %}
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
{% tab SWIFT %}

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
{% tab Dart %}
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

アプリごとに、1次、2次、3次の最大3つの公開キーを追加できます。必要に応じて、同じキーを複数のアプリに追加することもできます。公開鍵を追加する：

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択する。
2. 利用可能なアプリのリストからアプリを選ぶ。
3. \[**SDK 認証**] で、\[**公開キーを追加**] を選択します。
4. オプションの説明を入力し、公開キーを貼り付け、\[**公開キーを追加**] を選択します。

### 新しい1次キーを割り当てる

2次キーまたは3次キーを新しい1次キーとして割り当てるには以下の操作を行います。

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択する。
2. 利用可能なアプリのリストからアプリを選ぶ。
3. \[**SDK 認証**] でキーを選択し、\[**管理**] > \[**1次キーを作成**] を選択します。

### キーを削除する

1次キーを削除するには、まず[新たな1次キーを割り当て](#assign-a-new-primary-key)、それからキーを削除します。非プライマリキーを削除するには

1. Brazeのダッシュボードに行き、**「設定」**>「**アプリ設定**」を選択する。
2. 利用可能なアプリのリストからアプリを選ぶ。
3. \[**SDK 認証**] で1次キー以外のキーを選択し、\[**管理**] > \[**公開キーを削除**] を選択します。

## Brazeのダッシュボードで有効にする {#braze-dashboard}

[サーバー側の統合][1]と [SDK 統合][2]が完了したら、それらの特定のアプリに対してのこの機能の有効化を開始できます。

Braze ダッシュボードでアプリの SDK 認証設定が「**必須**」に設定されていない限り、SDK リクエストは認証なしで通常どおり処理され続けることに注意してください。

統合に何か問題が発生した場合（例えば、アプリがSDKにトークンを不正に渡している、またはサーバーが無効なトークンを生成している）、Brazeダッシュボードでこの機能を無効にすると、データは検証なしで通常通り流れるようになる。

### 適用オプション {#enforcement-options}

ダッシュボードの**管理設定**ページでは、各アプリに3つのSDK認証ステートがあり、Brazeがどのようにリクエストを検証するかを制御する。

| セッティング| 説明|
| ------ | ---------- |
| **無効** | Brazeは、ユーザーに提供されたJWTを検証しない。(デフォルト設定）|
| **オプション** | Brazeは、ログインしているユーザーのリクエストを確認するが、無効なリクエストは拒否しない。 |
| **必須** | Brazeは、ログインしているユーザーのリクエストを検証し、無効なJWTは拒否する。|
{: .reset-td-br-1 .reset-td-br-2}

![][8]

**Optional**設定は、この機能がアプリのSDKトラフィックに与える潜在的な影響を監視するのに便利な方法である。

無効な JWT 署名は**オプション**と**必須**の両方の状態で報告されますが、**必須**状態でのみ SDK リクエストが拒否され、アプリは再試行して新しい署名をリクエストします。

## 分析 {#analytics}

各アプリには、この機能が**オプション**状態と**必須**状態にある間に収集された SDK 認証エラーの内訳が表示されます。

データはリアルタイムで入手でき、チャート上のポイントにカーソルを合わせると、指定した日付のエラーの内訳を見ることができる。

![認証エラーの発生件数を示すグラフ。また、エラーの総数、エラーの種類、調整可能な日付範囲も表示される。][10]{: style="max-width:80%"}

## エラーコード {#error-codes}

| エラーコード| エラー理由 | 説明 |
| --------  | ------------ | ---------  |
| 10 | `EXPIRATION_REQUIRED` | Braze を使用する場合、有効期限は必須フィールドです。|
| 20 | `DECODING_ERROR` | 公開鍵が一致しないか、一般的な捕捉不能エラーが発生した。|
| 21 | `SUBJECT_MISMATCH` | 期待されるサブジェクトと実際のサブジェクトは同じではありません。|
| 22 | `EXPIRED` | 提供されたトークンの有効期限が切れた。|
| 23 | `INVALID_PAYLOAD` | トークンのペイロードが無効である。|
| 24 | `INCORRECT_ALGORITHM` | トークンのアルゴリズムはサポートされていない。|
| 25 | `PUBLIC_KEY_ERROR` | 公開鍵が適切な形式に変換できなかった。|
| 26 | `MISSING_TOKEN` | リクエストにトークンが指定されていない。|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | 提供されたトークンに一致する公開鍵がなかった。|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | リクエストのペイロードに含まれるすべてのユーザーIDが、要求されたものと一致するわけではない。|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## よくある質問 {#faq}

#### この機能はすべてのアプリで同時に有効にする必要がありますか？{#faq-app-by-app}

いいえ、この機能は特定のアプリに対して有効にすることができ、すべてのアプリで一度に使用する必要はありません。

#### 私のアプリの古いバージョンを使っているユーザーはどうなりますか？{#faq-sdk-backward-compatibility}

この機能を適用し始めると、古いバージョンのアプリによるリクエストは Braze によって拒否され、SDK によって再試行されます。ユーザーがアプリをサポートされたバージョンにアップグレードすると、キューに入れられたリクエストは再び受け入れられるようになる。

可能であれば、他の必須アップグレードと同様に、ユーザーにアップグレードを勧めてください。あるいは、許容できる割合のユーザーがアップグレードしたことを確認するまで、この機能を[オプショナルにして][6]おくこともできる。

#### JWT トークンを生成する際、どのような有効期限を使用すべきか？{#faq-expiration}

平均セッション期間、セッション Cookie/トークンの有効期限、またはアプリケーションが現在のユーザープロファイルをそれ以外の方法で更新する頻度のうち、高い方の値を使用することをお勧めします。

#### ユーザーのセッションの途中でJWTの有効期限が切れた場合はどうなるのか？ {#faq-jwt-expiration}

ユーザーのトークンがセッションの途中で期限切れになった場合、SDK には[コールバック関数][7]があり、この関数を呼び出して、 Braze にデータを送信し続けるには新しい JWT トークンが必要であることをアプリに通知します。

#### サーバー側の統合が壊れ、JWT を作成できなくなった場合はどうなりますか？{#faq-server-downtime}

サーバーがJWTトークンを提供できない場合、または統合に問題がある場合は、Brazeのダッシュボードでいつでも機能を無効にできる。

一度無効にすると、保留中の失敗したSDKリクエストは最終的にSDKによって再試行され、Brazeによって受け入れられる。

#### なぜこの機能では、共有シークレットではなく公開キー/秘密キーを使うのでしょうか？ {#faq-shared-secrets}

共有秘密を使う場合、Brazeのダッシュボードページなど、その共有秘密にアクセスできる人なら誰でも、トークンを生成してエンドユーザーになりすますことができる。

その代わり、公開鍵/秘密鍵を使用することで、Brazeの従業員でさえ（ダッシュボードのユーザーはもちろん）秘密鍵にアクセスできないようにしている。

#### 拒否されたリクエストはどのように再試行されるのか？ {#faq-retry-logic}

認証エラーが原因でリクエストが拒否されると、SDK はユーザーの JWT 署名の更新に使用されるコールバックを呼び出します。 

リクエストは指数バックオフアプローチを使用して定期的に再試行される。50回連続で失敗すると、次のセッション開始まで再試行は一時停止される。各 SDK には、手動でデータフラッシュをリクエストするメソッドもあります。

[1]: #server-side-integration
[2]: #sdk-integration
[3]: #key-management
[4]: #braze-dashboard
[5]: #create-jwt
[6]: #enforcement-options
[7]: #sdk-callback
[8]: {% image_buster /assets/img/sdk-auth-settings.png %}
[9]: \#error-codes
[10]: {% image_buster /assets/img/sdk-auth-analytics.png %}
 https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
