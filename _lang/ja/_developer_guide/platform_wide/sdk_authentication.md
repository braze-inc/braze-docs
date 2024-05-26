---
nav_title: SDK 認証
article_title: SDK 認証
page_order: 2
description: "このリファレンス記事では、SDK認証と、Braze SDKでこの機能を有効にする方法について説明します。"
platform:
  - iOS
  - Android
  - Web
  
---

# SDK 認証

> SDK 認証を使用すると、ログイン ユーザーに代わって行われた SDK 要求に暗号化証明 (サーバー側で生成) を提供できます。

アプリでこの機能を有効にすると、JSON Web Token(JWT)署名が無効または欠落しているリクエストを拒否するようにBrazeダッシュボードを設定できます。

- カスタムイベント、属性、購入、セッションデータの送信
- Brazeワークスペースで新しいユーザーを作成する
- 標準ユーザー・プロファイル属性の更新
- メッセージの受信またはトリガー

認証されていないログインユーザーがアプリの SDK API キーを使用して、他のユーザーになりすますなどの悪意のあるアクションを実行するのを防ぐことができるようになりました。

## 開始:

開始するには、次の 4 つの大まかな手順があります。

1. [サーバー側の統合][1] \- 公開キーと秘密キーのペアを生成し、秘密キーを使用して現在ログインしているユーザーの JWT を作成します。<br><br>
2. [SDK統合][2] \- Braze SDKでこの機能を有効にし、サーバーから生成されたJWTをリクエストします。<br><br>
3. [公開鍵の追加][3] \- Brazeダッシュボードの「**設定管理**」ページに_公開鍵_を追加します。<br><br>
4. [Brazeダッシュボード内での適用の切り替え][4] \- Brazeダッシュボード内でこの機能の適用をアプリごとに切り替えます。

## サーバー側の統合 {#server-side-integration}

### 公開鍵と秘密鍵のペアを生成する {#generate-keys}

RSA256公開鍵と秘密鍵のペアを生成します。公開鍵は最終的にBrazeダッシュボードに追加され、秘密鍵はサーバーに安全に保管する必要があります。

RS256 JWT アルゴリズムで使用できるように、2048 ビットの RSA キーが推奨されます。

{% alert warning %}
秘密鍵は _秘密_にしておくことを忘れないでください。アプリやウェブサイトで秘密鍵を公開したり、ハードコードしたりしないでください。秘密キーを知っているユーザーは誰でも、アプリケーションの代わりにユーザーを偽装したり、ユーザーを作成したりできます。
{% endalert %}

### 現在のユーザーの JSON Web トークンを作成する {#create-jwt}

秘密鍵を取得したら、サーバー側のアプリケーションはそれを使用して、現在ログインしているユーザーのアプリまたはWebサイトにJWTを返す必要があります。

通常、このロジックは、アプリが現在のユーザーのプロファイルを通常要求する場所であればどこにでも配置できます。たとえば、ログイン エンドポイントや、アプリが現在のユーザーのプロファイルを更新する場所などです。

JWT を生成する場合、次のフィールドが必要です。

**JWT ヘッダー**

|分野 |必須項目 |説明 |
| ----- | -------- | ----------------------------------- |
| `alg` |はい |サポートされているアルゴリズムは です `RS256`。 |
| `typ` |はい |型は と等しく `JWT`なければなりません。       |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**JWT ペイロード**

|分野 |必須項目 |説明 |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` |はい |「件名」は、Braze SDKを呼び出すときに `changeUser`  指定したユーザーIDと等しくなければなりません。
| `exp` |はい |このトークンの有効期限の「有効期限」。                               |
| `aud` |いいえ |"audience" 要求は省略可能であり、設定 `braze`                      する場合は |
| `iss` |いいえ |"issuer" 要求は省略可能であり、設定する場合は SDK API キーと等しくなります。             |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### JWT ライブラリ

JSON Web Tokenの詳細や、この署名プロセスを簡素化する多くのオープンソースライブラリを参照するには、 [https://jwt.io](https://jwt.io) をご覧ください。

## SDK統合 {#sdk-integration}

この機能は、次の [SDK バージョン\]({{ site.baseurl }} 以降で使用できます。/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
iOS統合の場合、このページではBraze Swift SDKの手順を詳しく説明します。従来のAppboyKit iOS SDKでの使用例については、 [このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) と [このファイル](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)を参照してください。
{% endalert %}

### Braze SDKでこの機能を有効にします。

この機能を有効にすると、Braze SDKは、Braze Serverへのネットワークリクエストに、現在のユーザーの最後に認識されたJWTを追加します。

{% alert note %}
このオプションのみで初期化しても、Brazeダッシュボード内で [認証の適用](#braze-dashboard) を開始するまで、データ収集にはまったく影響しませんのでご安心ください。
{% endalert %}

{% tabs %}
{% tab JavaScript %}
を呼び出す `initialize`ときは、省略可能な `enableSdkAuthentication` プロパティ `true`を に設定します。
```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab Java %}
Appboy インスタンスを設定するときは、`setIsSdkAuthenticationEnabled`.`true`
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

または、braze.xmlに追加する `<bool name="com_braze_sdk_authentication_enabled">true</bool>` こともできます。
{% endtab %}
{% tab KOTLIN %}
Appboy インスタンスを設定するときは、`setIsSdkAuthenticationEnabled`.`true`
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

または、braze.xmlに追加する `<bool name="com_braze_sdk_authentication_enabled">true</bool>` こともできます。
{% endtab %}
{% tab Objective-C %}
SDK認証を有効にするには、Brazeインスタンスを初期化する前に、オブジェクトのプロパティ`BRZConfiguration`を`configuration.api.sdkAuthentication`に設定します`YES`。

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
SDK 認証を有効にするには、SDK の初期化時にオブジェクトのプロパティ`Braze.Configuration`を次のように`true`設定`configuration.api.sdkAuthentication`します。

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
現在、SDK 認証は、ネイティブ iOS および Android コードで SDK を初期化する一環として有効にする必要があります。Flutter SDKでSDK認証を有効にするには、他のタブからiOSとAndroidの統合に従ってください。SDK認証を有効にすると、残りの機能をDartに統合できます。
{% endtab %}
{% endtabs %}

### 現在のユーザーの JWT トークンを設定する

アプリが Braze `changeUser` メソッドを呼び出すたびに、 [サーバー側で生成された][4] JWT トークンも指定します。

また、現在のユーザーのセッションの途中で更新するようにトークンを構成することもできます。

{% alert note %}
これは `changeUser` 、ユーザーID _が実際に変更_された場合にのみ呼び出す必要があることに注意してください。このメソッドは、ユーザー ID が変更されていない場合に署名を更新する方法として使用しないでください。
{% endalert %}

{% tabs %}
{% tab JavaScript %}
以下を呼び出す [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
)ときに JWT トークンを指定します。

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンを更新した場合は、次のようになります。

```javascript
import * as braze from"@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

以下を呼び出す [`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)ときに JWT トークンを指定します。

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

または、セッションの途中でユーザーのトークンを更新した場合は、次のようになります。

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

以下を呼び出す [`appboy.changeUser`](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)ときに JWT トークンを指定します。

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER")
```

または、セッションの途中でユーザーのトークンを更新した場合は、次のようになります。

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

以下を呼び出す [`changeUser`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69)ときに JWT トークンを指定します。

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"signature"];
```

または、セッションの途中でユーザーのトークンを更新した場合は、次のようになります。

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"signature"];
```
{% endtab %}
{% tab Swift %}

以下を呼び出す [`changeUser`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69)ときに JWT トークンを指定します。

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "signature")
```
または、セッションの途中でユーザーのトークンを更新した場合は、次のようになります。

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "signature")
```
{% endtab %}
{% tab Dart %}

以下を呼び出す [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)ときに JWT トークンを指定します。

```dart
braze.changeUser("userId", sdkAuthSignature: "signature")
```
または、セッションの途中でユーザーのトークンを更新した場合は、次のようになります。

```dart
braze.setSdkAuthenticationSignature("signature")
```

{% endtab %}
{% endtabs %}

### 無効なトークンのコールバック関数を登録する {#sdk-callback}

この機能を [必須](#enforcement-options)に設定すると、次のシナリオで SDK リクエストが Braze によって拒否されます。
\- Braze APIが受信するまでにJWTの有効期限が切れている
\- JWTが空または欠落している
\- JWTは、Brazeダッシュボードにアップロードした公開鍵の検証に失敗しました。

サブ `subscribeToSdkAuthenticationFailures` スクライブを使用すると、これらの理由のいずれかで SDK 要求が失敗したときに通知を受け取ることができます。コールバック関数には、エラー`userId`に関連する ['errorCode'][9] `reason` を持つオブジェクト、要求の (ユーザーが匿名でない場合)、およびエラーの原因となった認証`signature`が含まれます。 

失敗した要求は、アプリが新しい有効な JWT を提供するまで定期的に再試行されます。そのユーザーがまだログインしている場合は、このコールバックを機会にサーバーに新しいJWTをリクエストし、Braze SDKにこの新しい有効なトークンを提供することができます。

{% alert tip %}
これらのコールバックメソッドは、独自の監視サービスやエラーログサービスを追加して、Brazeリクエストが拒否される頻度を追跡するのに最適な場所です。
{% endalert %}

{% tabs %}
{% tab JavaScript %}
```javascript
import * as braze from"@braze/web-sdk";
braze.subscribeToSdkAuthenticationFailures((error) => {
  // TODO: Optionally log to your error-reporting service
  // TODO: Check if the `user_id` within the `error` matches the currently logged-in user
  const updated_jwt = await getNewTokenSomehow(error);
  appboy.setSdkAuthenticationSignature(updated_jwt);
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

{% alert important %}
Braze Swift SDKのバージョン`5.14.0`から、SDK認証デリゲートメソッドは`BrazeDelegate``BrazeSDKAuthDelegate`、
{% endalert %}

\`\`\`objc
Braze \*braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = デリゲート;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
// TODO: Optionally log to your error-reporting service
藤堂:within`error`が現在ログインしているユーザーと一致するかどうかを確認します`user_id`
  NSLog(@"Invalid SDK Authentication signature.");
  NSString \*newSignature = getNewSignatureSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
  ()
  \`\`\`
{% endtab %}
{% tab Swift %}

{% alert important %}
Braze Swift SDKのバージョン`5.14.0`から、SDK認証デリゲートメソッドがプロトコルから`BrazeSDKAuthDelegate`分離`BrazeDelegate`されました。これより前のバージョンを使用している場合は、 に準拠し `BrazeDelegate`ている任意の場所に SDK 認証デリゲート メソッドを実装する必要があります。
{% endalert %}

\`\`\`swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = デリゲート
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
// TODO: Optionally log to your error-reporting service
藤堂:within`error`が現在ログインしているユーザーと一致するかどうかを確認します`user_id`
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
  ()
  ```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
// TODO: Optionally log to your error-reporting service
// TODO: Check if the `user_id` within は `error` 、現在ログインしているユーザーと一致します
print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(error)
  braze.setSdkAuthenticationSignature(newSignature);
  });
  \`\`\`
  {% endtab %}
{% endtabs %}

## 公開鍵の追加 {#key-management}

ダッシュボードの「 **設定の管理** 」ページで、Brazeダッシュボードの特定のアプリに公開鍵を追加します。各アプリは、最大 3 つの公開キーをサポートします。複数のアプリで同じ公開鍵と秘密鍵が使用される可能性があることに注意してください。

公開鍵を追加するには、次のようにします。

1. 利用可能なアプリの一覧からアプリを選択します。
2. 「 **SDK認証**」で、「 **公開鍵の追加**」をクリックします。
3. 公開鍵を貼り付け、オプションの説明を追加します。
4. 変更を保存すると、公開キーの一覧にキーが表示されます。

キーを削除したり、キーを主キーに昇格したりするには、各キーの横にあるオーバーフローメニューで対応するアクションを選択します。

## Brazeダッシュボードで有効化する {#braze-dashboard}

[サーバーサイド統合][1]と[SDK統合][2]が完了したら、これらの特定のアプリに対してこの機能を有効にし始めることができます。

BrazeダッシュボードでアプリのSDK認証設定が **[必須** ]に設定されていない限り、SDKリクエストは認証なしで通常どおり流れ続けることに注意してください。

統合に問題が発生した場合(たとえば、アプリが誤ってトークンをSDKに渡している、サーバーが無効なトークンを生成しているなど)、Brazeダッシュボードでこの機能を無効にすると、検証なしでデータの流れが通常どおり再開されます。

### 適用オプション {#enforcement-options}

ダッシュボードの **[Manage Settings** ] ページには、Braze がリクエストを検証する方法を制御する 3 つの SDK 認証状態があります。

|設定|説明|
| ------ | ---------- |
| **無効** |Brazeは、ユーザーに提供されたJWTを検証しません。(デフォルト設定)|
| **オプション** |Brazeはログインユーザーのリクエストを検証しますが、無効なリクエストは拒否しません。|
| **必須項目** |Brazeは、ログインしたユーザーのリクエストを検証し、無効なJWTを拒否します。
{: .reset-td-br-1 .reset-td-br-2}

![][8]

**[省略可能**] 設定は、この機能がアプリの SDK トラフィックに及ぼす潜在的な影響を監視するのに便利な方法です。

無効な JWT 署名は **Optional** 状態と **Required** 状態の両方で報告されますが、SDK 要求が拒否されるのは **Required** 状態のみで、アプリは再試行して新しい署名を要求します。

## 分析 {#analytics}

各アプリには、この機能が **[オプション** ] と **[必須** ] の状態の間に収集された SDK 認証エラーの内訳が表示されます。

データはリアルタイムで利用でき、グラフ内のポイントにカーソルを合わせると、特定の日付のエラーの内訳を確認できます。

![認証エラーのインスタンス数を示すグラフ。また、エラーの合計数、エラーの種類、および調整可能な日付範囲も表示されます。[10]{: style="max-width:80%"}

## エラーコード {#error-codes}

|エラーコード|エラーの理由 |説明 |
| --------  | ------------ | ---------  |
|10 | `EXPIRATION_REQUIRED` |有効期限は、Brazeの使用に必要なフィールドです。|
|20 | `DECODING_ERROR` |一致しない公開キーまたは一般的なキャッチされないエラー。|
|21 | `SUBJECT_MISMATCH` |想定される科目と実際の科目は同じではありません。|
|22 | `EXPIRED` |指定されたトークンの有効期限が切れています。|
|23 | `INVALID_PAYLOAD` |トークンペイロードが無効です。|
|24 | `INCORRECT_ALGORITHM` |トークンのアルゴリズムはサポートされていません。|
|25 | `PUBLIC_KEY_ERROR` |公開鍵を適切な形式に変換できませんでした。|
|26 | `MISSING_TOKEN` |要求でトークンが指定されていません。|
|27 | `NO_MATCHING_PUBLIC_KEYS` |指定されたトークンと一致する公開キーがありませんでした。|
|28 | `PAYLOAD_USER_ID_MISMATCH` |要求ペイロード内のすべてのユーザー ID が必要に応じて一致するわけではありません。|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## よくある質問 {#faq}

#### この機能は、すべてのアプリで同時に有効にする必要がありますか? {#faq-app-by-app}

いいえ、この機能は特定のアプリに対して有効にすることができ、すべてのアプリで一度に使用する必要はありません。

#### 古いバージョンのアプリをまだ使用しているユーザーはどうなりますか? {#faq-sdk-backward-compatibility}

この機能の適用を開始すると、古いバージョンのアプリによるリクエストはBrazeによって拒否され、SDKによって再試行されます。ユーザーがサポートされているバージョンにアプリをアップグレードすると、エンキューされた要求が再び受け入れられるようになります。

可能であれば、他の必須アップグレードの場合と同様に、ユーザーにアップグレードを促す必要があります。または、許容できる割合のユーザーがアップグレードされたことを確認するまで、この機能を [オプション][6] のままにしておくこともできます。

#### JWTトークンを生成するときは、どの有効期限を使用する必要がありますか? {#faq-expiration}

平均セッション時間、セッション Cookie/トークンの有効期限、またはアプリケーションが現在のユーザーのプロファイルを更新する頻度の値を大きくすることをお勧めします。

#### ユーザーのセッションの途中で JWT の有効期限が切れた場合はどうなりますか? {#faq-jwt-expiration}

ユーザーのトークンがセッションの途中で期限切れになった場合、SDK [は呼び出して][7] 、Brazeにデータを送信し続けるために新しいJWTトークンが必要であることをアプリに知らせるために呼び出します。

#### サーバー側の統合が中断され、JWT を作成できなくなった場合はどうなりますか? {#faq-server-downtime}

サーバーがJWTトークンを提供できない場合、または統合の問題に気付いた場合は、Brazeダッシュボードでいつでもこの機能を無効にすることができます。

無効にすると、保留中の失敗したSDKリクエストは最終的にSDKによって再試行され、Brazeによって受け入れられます。

#### この機能が共有シークレットの代わりに公開キー/秘密キーを使用するのはなぜですか? {#faq-shared-secrets}

共有シークレットを使用すると、Brazeダッシュボードページなど、その共有シークレットにアクセスできる人なら誰でもトークンを生成し、エンドユーザーになりすますことができます。

代わりに、公開鍵/秘密鍵を使用しているため、Brazeの従業員(ダッシュボードユーザーは言うまでもなく)でさえ、秘密鍵にアクセスできません。

#### 拒否された要求はどのように再試行されますか? {#faq-retry-logic}

認証エラーが原因でリクエストが拒否されると、SDKはユーザーのJWT署名の更新に使用されるコールバックを呼び出します。 

要求は、エクスポネンシャル バックオフ アプローチを使用して定期的に再試行されます。50回連続して失敗すると、次のセッションが開始されるまで再試行が一時停止されます。各 SDK には、データ フラッシュを手動で要求する方法もあります。

[1]: #server-side-integration
[2]: #sdk-integration
[3]: #key-management
[4]: #braze-dashboard
[5]: #create-jwt
[6]: #enforcement-options
[7]: #sdk-callback
[8]: {% image_buster /assets/img/sdk-auth-settings.png %}
[9]: #error-codes
[10]: {% image_buster /assets/img/sdk-auth-analytics.png %}
[11]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser
