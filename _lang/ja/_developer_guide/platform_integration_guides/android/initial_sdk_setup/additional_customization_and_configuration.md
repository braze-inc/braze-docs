---
nav_title: その他の SDK カスタマイズ
article_title: AndroidおよびFireOS向けのその他のSDKカスタマイズ
page_order: 3
platform: 
  - Android
  - FireOS
description: "このリファレンス記事では、詳細ログ、ログ記録の抑制、複数の API キーの実装方法など、追加のカスタマイズオプションと設定オプションについて説明します。"

---

# AndroidおよびFireOS向けのその他のSDKカスタマイズ

> このリファレンス記事では、詳細ログ、ログ記録の抑制、複数の API キーの実装方法など、追加のカスタマイズオプションと設定オプションについて説明します。

## Braze での R8/ProGuard の使用

[コード圧縮](https://developer.android.com/studio/build/shrink-code)設定は、Braze 統合に自動的に含まれます。

Braze コードを難読化するクライアントアプリでは、Braze がスタックトレースを解釈するためのリリースマッピングファイルを保存する必要があります。すべての Braze コードを引き続き保持する場合は、ProGuard ファイルに以下を追加します。

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## ロギング

デフォルトでは、Braze Android SDK のログレベルは `INFO` に設定されています。[これらのログを抑制](#suppressing-logs)したり、[別のログレベルを設定](#enabling-logs) (`VERBOSE`、`DEBUG`、または `WARN` など) したりすることができます。

### ログの有効化 {#enabling-logs}

アプリの問題のトラブルシューティングや、Braze サポートでの所要時間の短縮に役立つように、SDK の詳細ログを有効にします。Brazeサポートに冗長ログを送信する場合は、アプリケーションを起動したらすぐにログを開始し、問題が発生してからずっと後にログを終了するようにする。

詳細なログは開発環境のみを対象としているため、アプリをリリースする前に無効にする必要があります。

{% alert important %}
`Application.onCreate()` で他の呼び出しを行う前に詳細ログを有効にして、ログが可能な限り完全になるようにします。
{% endalert %}

{% tabs %}
{% tab アプリケーション %}
アプリで直接ログを有効にするには、他のメソッドの前に、以下をアプリケーションの `onCreate()` メソッドに追加します。

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

`MIN_LOG_LEVEL` を、最小ログレベルとして設定するログレベルの**定数**に置き換えます。設定した`MIN_LOG_LEVEL` のレベル`>=` のログはすべて、Androidのデフォルトの [`Log`](https://developer.android.com/reference/android/util/Log)メソッドに転送される。設定した `MIN_LOG_LEVEL` 未満の (`<`) すべてのログは破棄されます。

| コンスタント    | 値          | 説明                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | デバッグや開発のために最も詳細なメッセージをログに記録する。            |
| `DEBUG`     | 3              | デバッグや開発のために、説明的なメッセージをログに記録する。                  |
| `INFO`      | 4              | 一般的なハイライトのための情報メッセージを記録する。                       |
| `WARN`      | 5              | 潜在的に有害な状況を特定するための警告メッセージをログに記録する。     |
| `ERROR`     | 6              | アプリケーションの失敗や深刻な問題を示すエラーメッセージを記録する。 |
| `ASSERT`    | 7              | 開発中に条件が偽の場合にアサーションメッセージをログに記録する。     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

たとえば、以下のコードはログレベル`2`、`3`、`4`、`5`、`6`、`7`を `Log` メソッドに転送します。

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
{% endtab %}

{% tab braze.xml %}
`braze.xml` でログを有効にするには、ファイルに以下を追加する：

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

`MIN_LOG_LEVEL` を、最小ログレベルとして設定するログレベルの**値**に置き換えます。設定した`MIN_LOG_LEVEL` のレベル`>=` のログはすべて、Androidのデフォルトの [`Log`](https://developer.android.com/reference/android/util/Log)メソッドに転送される。設定した `MIN_LOG_LEVEL` 未満の (`<`) すべてのログは破棄されます。

| コンスタント    | 値          | 説明                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | デバッグや開発のために最も詳細なメッセージをログに記録する。            |
| `DEBUG`     | 3              | デバッグや開発のために、説明的なメッセージをログに記録する。                  |
| `INFO`      | 4              | 一般的なハイライトのための情報メッセージを記録する。                       |
| `WARN`      | 5              | 潜在的に有害な状況を特定するための警告メッセージをログに記録する。     |
| `ERROR`     | 6              | アプリケーションの失敗や深刻な問題を示すエラーメッセージを記録する。 |
| `ASSERT`    | 7              | 開発中に条件が偽の場合にアサーションメッセージをログに記録する。     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

たとえば、以下のコードはログレベル`2`、`3`、`4`、`5`、`6`、`7`を `Log` メソッドに転送します。

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

### 冗長ログを検証する

ログが `VERBOSE` に設定されていることを確認するには、`V/Braze` がログのどこかで発生するかどうかを確認します。もしそうなら、冗長ログは正常に有効になっている。以下に例を示します。

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

### ログの抑制

Braze Android SDK のデフォルトのログレベルは `INFO` です。Braze Android SDK のすべてのログを抑制するには、他のメソッドの_前_にアプリケーションの `onCreate()` メソッドで `BrazeLogger.SUPPRESS` を呼び出します。

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

## 複数の API キー

複数の API キーの最も一般的なユースケースは、デバッグおよびリリースビルドバリアントの API キーを分離することです。

ビルド内の複数の API キーを簡単に切り替えられるように、関連する[ビルドバリアント](https://developer.android.com/studio/build/build-variants.html)ごとに個別の `braze.xml` ファイルを作成することをお勧めします。ビルドバリアントは、ビルドタイプと製品フレーバーの組み合わせです。デフォルトでは、[新しい Android プロジェクトは `debug` および `release` ビルドタイプで構成され](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types)、製品フレーバーは設定されません。

関連するビルドバリアントごとに、新しい `braze.xml` を `src/<build variant name>/res/values/` で作成します。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

ビルドバリアントがコンパイルされると、新しい API キーが使用されます。

コードでの API キーの設定については、[ランタイム構成]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/)のドキュメントを参照してください。
