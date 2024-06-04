---
nav_title: その他の SDK カスタマイズ
article_title: Android および FireOS 用のその他の SDK カスタマイズ
page_order: 3
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、詳細ログ、ログ記録の抑制、複数の API キーの実装方法など、追加のカスタマイズオプションと設定オプションについて説明します。"

---

# その他の SDK のカスタマイズ

> このリファレンス記事では、詳細ログ、ログ記録の抑制、複数の API キーの実装方法など、追加のカスタマイズオプションと設定オプションについて説明します。

## Braze での R8/ProGuard の使用
[コード圧縮][50]設定は、Braze 統合に自動的に含まれます。

Braze コードを難読化するクライアントアプリでは、Braze がスタックトレースを解釈するためのリリースマッピングファイルを保存する必要があります。すべての Braze コードを引き続き保持する場合は、ProGuard ファイルに以下を追加します。

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## 詳細ログ記録の有効化 {#android-verbose-logging}

Braze SDK の詳細ログは、サポートの問題を迅速に解決するために不可欠です。長いログファイルが望ましいため、これらのログをわかりやすくするために変更しないでください。詳細ログは開発環境のみを対象としており、リリースされたアプリケーションでは有効にしないでください。詳細なログ記録では、追加のユーザー情報や新しいユーザー情報が Braze に送信されることはありません。

サポートチームに送信するログは、アプリケーションの起動後すぐに開始され、観察された問題の発生後十分な時間を記録したものであることが必要です。

Braze Android SDK で詳細なログ記録を有効にするには:

{% tabs %}
{% tab JAVA %}

```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```

{% endtab %}
{% endtabs %}

`braze.xml` で詳細なログ記録を有効にするには:
```
<integer name="com_braze_logger_initial_log_level">2</integer>
```

Braze のログレベル整数定数は、[`android.util.log`][71] で定義されている Android のログレベル整数定数に対応しています。

{% alert important %}
詳細ログは、SDK への他の呼び出しの前に、`Application.onCreate()` でできるだけ早い段階で有効にして、可能な限り多くをログに記録できるようにする必要があります。
{% endalert %}

取得したログが詳細ログかどうかを知るには、ログに `V/Braze` があるかを調べます。以下に例を示します。

`2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started`

### Braze SDK ログ記録の抑制

Braze Android SDK のデフォルトのログレベルは `INFO` です。

Braze のログレベルを変更するには、[`android.util.Log`][54] 定数または `BrazeLogger.SUPPRESS` の 1 つを使用して [`BrazeLogger.setLogLevel()`][70] を呼び出します。以下に例を示します。

{% tabs %}
{% tab JAVA %}

```java
// Suppress all logs
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Suppress all logs
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```

{% endtab %}
{% endtabs %}

## 複数の API キー

複数の API キーの最も一般的なユースケースは、デバッグおよびリリースビルドバリアントの API キーを分離することです。

ビルド内の複数の API キーを簡単に切り替えられるように、関連する[ビルドバリアント][3]ごとに個別の `braze.xml` ファイルを作成することをお勧めします。ビルドバリアントは、ビルドタイプと製品フレーバーの組み合わせです。デフォルトでは、[新しい Android プロジェクトは `debug` および `release` ビルドタイプで構成され][8]、製品フレーバーは設定されません。

関連するビルドバリアントごとに、新しい `braze.xml` を `src/<build variant name>/res/values/` で作成します。

\`\`\`xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

ビルドバリアントがコンパイルされると、新しい API キーが使用されます。

コードでの API キーの設定については、[ランタイム構成][69]のドキュメントを参照してください。

[3]: https://developer.android.com/studio/build/build-variants.html
[8]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
[50]: https://developer.android.com/studio/build/shrink-code
[54]: https://developer.android.com/reference/android/util/Log.html
[69]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[70]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.support/-braze-logger/log-level.html
[71]: https://developer.android.com/reference/android/util/Log
