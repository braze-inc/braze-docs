---
page_order: 1.4
nav_title: 詳細なログ記録
article_title: 詳細なログ記録
description: "Braze SDKの詳細ログ記録のイネーブルメント方法、トラブルシューティング用のログ収集方法、そしてそれらをBrazeサポートと共有する方法を学ぶ。"
---

# 詳細なログ記録

> 詳細なログ出力は、Braze SDKからの詳細かつ低レベルな情報を提供する。これにより、SDKの初期化方法、サーバーとの通信方法、プッシュ通知、アプリ内メッセージ、コンテンツカードといったメッセージングチャネルの処理方法が可視化される。

何かが期待通りに動作しない場合——例えばプッシュ通知が届かない、アプリ内メッセージが表示されない、ユーザーデータが同期されない——詳細ログは根本原因の識別に役立つ。推測する代わりに、SDKが各ステップで何をしているかを正確に確認できる。

{% alert tip %}
手動で詳細ログのイネーブルメントをせずにデバッグしたい場合、[SDKデバッガー]({{site.baseurl}}/developer_guide/sdk_integration/debugging)を使ってBrazeダッシュボード内で直接デバッグセッションを作成できる。
{% endalert %}

## 詳細ログを記録するタイミング

必要な時に詳細ログを有効にしろ：

- **SDKの初期化を確認する**：SDKが正しいAPIキーとエンドポイントで正しく起動することを確認せよ。
- **メッセージ配信のトラブルシューティング**：プッシュトークンが登録されているか、アプリ内メッセージがトリガーされているか、コンテンツカードが同期されているかを確認する。
- **ディープリンクをデバッグする**：SDKがプッシュ通知、アプリ内メッセージ、またはコンテンツカードからのディープリンクを受信し、開封することを確認せよ。
- **セッショントラッキングを検証する**：セッションの開始と終了が予定通りであることを確認する。
- **接続の問題を診断する**：SDKとBrazeサーバー間のネットワークリクエストとレスポンスを検査する。

## 詳細ログ記録のイネーブルメント

{% alert important %}
詳細ログは開発者およびテスト環境でのみ使用することを意図している。本番環境へアプリを公開する前に詳細ログ記録を無効化し、機密情報が漏洩するのを防ぐこと。
{% endalert %}

{% tabs %}
{% tab Android %}

メソッド`Application.onCreate()`内で他のSDK呼び出しを行う前に詳細ログ記録をイネーブルにすると、最も完全な出力を取得できる。

**コードでは：**

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}

**In `braze.xml`:**

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```

詳細ログのイネーブルメントを確認するには、Logcat出力で\``V/Braze`verbose`を検索する。以下に例を示します。

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

詳細については、[Android SDKのロギングを]({{site.baseurl}}/developer_guide/sdk_integration#android_enabling-logs)参照せよ。

{% endtab %}
{% tab Swift %}

初期化時に、オブジェクト`Braze.Configuration`のログ`.debug`レベルを に設定する。

{% subtabs %}
{% subtab SWIFT %}
```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.logger.level = .debug
let braze = Braze(configuration: configuration)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
[configuration.logger setLevel:BRZLoggerLevelDebug];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endsubtab %}
{% endsubtabs %}

レベル`.debug`は最も詳細な出力を示すため、トラブルシューティングに推奨される。詳細については、[SWIFT SDKのロギングを]({{site.baseurl}}/developer_guide/sdk_integration#swift_log-levels)参照せよ。

{% endtab %}
{% tab Web %}

URLパラメータとして\`add`?brazeLogging=true``を追加するか、SDK初期化時にロギングのイネーブルメントを行う。

```javascript
braze.initialize('YOUR-API-KEY', {
    baseUrl: 'YOUR-SDK-ENDPOINT',
    enableLogging: true
});
```

初期化後にログ記録のオンオフを切り替えることもできる。

```javascript
braze.toggleLogging();
```

ログはブラウザの開発者の開発ツールのコンソールタブに表示される。詳細については、[Web SDKのログ記録を]({{site.baseurl}}/developer_guide/sdk_integration#web_logging)参照せよ。

{% endtab %}
{% tab Unity %}

1. [**Braze**] > [**Braze 構成**] の順に移動して、[Braze 構成設定] を開きます。
2. **「Show Braze Android 設定**」ドロップダウンを選択する。
3. **SDK**ログレベルフィールドに「.」と入力する`0`。

{% endtab %}
{% tab React Native %}

SDK設定時にログレベルを設定する：

```javascript
const configuration = new Braze.BrazeConfiguration('YOUR-API-KEY', 'YOUR-SDK-ENDPOINT');
configuration.logLevel = Braze.LogLevel.Verbose;
```

{% endtab %}
{% endtabs %}

## ログの収集

詳細ログ記録のイネーブルメント後、トラブルシューティング対象の問題を再現し、プラットフォームのコンソールまたはデバッグツールからログを収集する。

{% tabs %}
{% tab Android %}

Android Studioで**Logcat**を使ってログをキャプチャする：

1. デバイスを接続するか、エミュレータを起動する。
2. Android Studioで、下部のパネルから**Logcat**を開け。
3. または`V/Braze`でフィルターをかけて、`D/Braze`Braze SDKの出力を分離する。
4. 問題を再現する。
5. 関連するログをコピーして、テキストファイルに保存する。

{% endtab %}
{% tab iOS %}

MacOSの**コンソール**アプリを使ってログをキャプチャする：

1. 詳細ログ記録を有効にした状態で、アプリを端末にインストールせよ。
2. デバイスをMacに接続せよ。
3. **コンソール**アプリを開封し、**デバイスの**サイドバーから自分のデバイスを選ぶ。
4. 検索バーで  `BrazeKit`または  `Braze`でフィルターをかける。
5. 問題を再現する。
6. 関連するログをコピーして、テキストファイルに保存する。

{% endtab %}
{% tab Web %}

ブラウザの開発者ツールを使え：

1. ブラウザの開発者ツールを開封（通常は**F12**キーかCmd+Option+Iキーだ）。
2. **コンソール**タブに移動する。
3. 問題を再現する。
4. コンソールの出力をコピーして、テキストファイルに保存しろ。

{% endtab %}
{% endtabs %}

{% alert tip %}
Brazeサポート向けにログを収集する際は、アプリ起動前からログ記録を開始し、問題発生後も十分に経過するまで継続すること。これにより、一連の出来事の全容を把握できる。
{% endalert %}

## 冗長なログを読む

詳細ログは一貫した構造に従っているため、SDKの動作を追跡するのに役立つ。特定のチャネルのログ出力を学習する方法、具体的には確認すべきキーエントリや一般的なトラブルシューティングパターンについては、「[詳細ログの読み方]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)」を参照せよ。

## Brazeサポートとのログ共有

SDKに関する問題でBrazeサポートに連絡する際は、以下の情報を含めてください：

1. **詳細なログファイル**：アプリ起動前から問題発生までの完全なログ記録。
2. **再現ステップ**：問題をトリガーするアクションの明確な説明。
3. **期待される動作と実際の動作**：君が予想していたことと、実際に起きたこと。
4. **SDKバージョン**：使用しているBraze SDKのバージョン。
5. **プラットフォームとOSのバージョン**：例えば、iOS 18.0、Android 14、あるいはChrome 120といったものだ。