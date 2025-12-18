## Braze Vega SDKについて

Braze Vega SDKを使用すると、ユーザーに対して分析を収集したり、リッチなアプリ内メッセージを表示したりすることができる。Braze Vega SDKのほとんどのメソッドは非同期で、待機または解決すべき約束を返す。

## Braze Vega SDKの統合

### ステップ 1: Brazeライブラリをインストールする

お好みのパッケージマネージャーを使用してBraze Vega SDKをインストールする。

{% tabs local %}
{% tab npm %}
プロジェクトでNPMを使用している場合は、Braze Vega SDKを依存関係として追加できる。

```bash
npm install @braze/vega-sdk --save
```

インストール後、必要なメソッドをインポートすることができる：

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
プロジェクトがYarnを使用している場合、Braze Vega SDKを依存関係として追加できる。

```bash
yarn add @braze/vega-sdk
```

インストール後、必要なメソッドをインポートすることができる：

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### ステップ2:SDK の初期化

プロジェクトにBraze Vega SDKを追加したら、Brazeダッシュボード内の**設定** **>アプリ設定に**あるAPIキーと[SDKエンドポイントURLを使って]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)、ライブラリを初期化する。

{% alert important %}
他のBrazeメソッドを呼び出す前に、`changeUser` プロミスを待ち受けるか解決しなければならない。さもないと、イベントやアトリビューションが正しくないユーザーに設定される可能性がある。
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
匿名ユーザーは[MAUに]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users)カウントされる可能性がある。その結果、これらのユーザーをMAUカウントから除外するために、条件付きでSDKをロードするか、初期化したい場合があります。
{% endalert %}

## オプション構成

### ロギング

SDKロギングをイネーブルメントにすることで、デバッグやトラブルシューティングに役立てることができる。ロギングをイネーブルメントにする方法は複数ある。

#### 初期化中のロギングをイネーブルメントにする

デバッグ・メッセージをコンソールに記録するには、`initialize()` に`enableLogging: true` を渡す：

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
基本的なログはすべてのユーザーが見ることができるので、コードを本番環境にリリースする前に、ロギングを無効にすることを検討しよう。
{% endalert %}

#### 初期化後のロギングをイネーブルメントにする

初期化後にSDKロギングをイネーブルまたはディスエーブルにするには、`toggleLogging()` を使用する：

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### カスタムロギング

`setLogger()` 、SDKログの処理方法をよりコントロールするためのカスタムロガー関数を提供する：

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### 設定オプション

SDKの行動をカスタマイズするために、`initialize()` に追加のコンフィギュレーション・オプションを渡すことができる：

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## SDKをアップグレードする

NPMまたはYarnからBraze Vega SDKを参照する場合、パッケージ依存関係を更新することで最新バージョンにアップグレードできる：

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## 統合をテストする

SDKインテグレーションが正しく機能していることを確認する：

1. コンソールでデバッグメッセージを見るために、`enableLogging: true` で SDK を初期化する。
2. 他のSDKメソッドを呼び出す前に、`await changeUser()` 。
3. `await openSession()` 、セッションを開始する。
4. Brazeダッシュボードの「**概要**」を確認し、セッションデータが記録されていることを確認する。
5. カスタムイベントのログをテストし、ダッシュボードに表示されることを確認する。


