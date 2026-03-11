## Braze Vega SDKについて

Braze Vega SDKを使えば、ユーザー向けの分析データを収集し、アプリ内でリッチなアプリ内メッセージを表示できる。Braze Vega SDK のメソッドの大半は非同期であり、await または resolve すべき Promise を返す。

## Braze Vega SDKの統合

### ステップ 1: Brazeライブラリをインストールする

お好みのパッケージマネージャーを使って、Braze Vega SDKをインストールする。

{% tabs local %}
{% tab npm %}
プロジェクトでNPMを使用している場合、Braze Vega SDKを依存関係として追加できる。

```bash
npm install @braze/vega-sdk --save
```

インストール後、必要なメソッドをインポートできる：

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
プロジェクトでYarnを使用している場合、Braze Vega SDKを依存関係として追加できる。

```bash
yarn add @braze/vega-sdk
```

インストール後、必要なメソッドをインポートできる：

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### ステップ2:SDK の初期化

プロジェクトにBraze Vega SDKを追加した後、ライブラリーを初期化する。その際、Brazeダッシュボードの「**設定**」＞「**アプリ設定」**にあるAPI キーと[SDKエンドポイントURL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)を使用する。

{% alert important %}
他のBrazeメソッドを呼び出す前に、プロミ`changeUser`スを待機または解決しなければならない。さもなければ、イベントや属性が誤ったユーザーに設定される可能性がある。
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");
      
      // Start a session
      await openSession();
      
      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };
    
    initBraze();
  }, []);
  
  return (
    // Your app components
  );
};
```

{% alert important %}
匿名ユーザーは[MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users)にカウントされる可能性がある。その結果、これらのユーザーをMAUカウントから除外するために、条件付きでSDKをロードするか、初期化したい場合があります。
{% endalert %}

## オプション設定

### ロギング

SDKのログ記録のイネーブルメントを有効にすれば、デバッグやトラブルシューティングに役立つ。ログ記録のイネーブルメントは複数ある。

#### 初期化中にログ記録をイネーブルメントする

デバッグメッセージをコンソールに記録するには`initialize()`、`enableLogging: true`以下を実行する:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
基本ログは全てのユーザーに公開されるため、本番環境にコードをリリースする前にログ記録を無効にすることを検討せよ。
{% endalert %}

#### 初期化後にログ記録をイネーブルメントする

初期化後にSDKのログ出力をイネーブルメントまたは無効`toggleLogging()`にするには、以下を使用する：

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### カスタムロギング

SDKのログ処理をより細かくコントロールするために、カスタムロガー関数を`setLogger()`指定するには``を使用する。

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### 設定オプション

SDKの動作をカスタマイズするために`initialize()`、追加の設定オプションを渡すことができる：

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## SDKをアップグレードする

NPMやYarnからBraze Vega SDKを参照している場合、パッケージ依存関係を更新することで最新版にアップグレードできる：

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## 統合のテスト

SDKの統合が正しく動作しているか確認するには：

1. コンソールにデバッグメッセージを表示するには`enableLogging: true`、SDKを初期化する。
2. 他のSDKメソッドを呼び出す前に`await changeUser()`必ず確認すること
3. セッションを開始するには`await openSession()`電話をかけろ
4. Brazeダッシュボードの**「概要」**で、セッションデータが記録されていることを確認せよ。
5. カスタムイベントのテスト記録を行い、それがダッシュボードに表示されることを確認する


