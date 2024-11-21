---
nav_title: アプリ内メッセージング
article_title: Unityのアプリ内メッセージ
channel: in-app messaging
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "このリファレンス記事では、Unityプラットフォームのアプリ内メッセージング構成ガイドラインについて説明する。"

---

# アプリ内メッセージング統合

> このリファレンス記事では、Unityプラットフォームのアプリ内メッセージング構成ガイドラインについて説明する。

## デフォルトのアプリ内メッセージの動作を設定する

{% tabs %}
{% tab Android %}

Androidでは、Brazeからのアプリ内メッセージが自動的にネイティブ表示される。この機能を無効にするには、Brazeコンフィギュレーションエディターで「**アプリ内メッセージを自動的に表示する**」の選択を解除する。

代わりに、Unity プロジェクトの `braze.xml` で `com_braze_inapp_show_inapp_messages_automatically` を`false` に設定することもできます。

アプリ内メッセージの初期表示動作は、Braze 設定の「アプリ内メッセージマネージャー初期表示動作」で設定できます。

{% endtab %}
{% tab iOS %}

iOSでは、Brazeからのアプリ内メッセージは自動的にネイティブ表示される。この機能を無効にするには、Braze 設定エディターでゲームオブジェクトリスナーを設定し、[**Braze でアプリ内メッセージを表示する**] が選択されていないことを確認します。

アプリ内メッセージの初期表示動作は、Braze 設定の「アプリ内メッセージマネージャー初期表示動作」で設定できます。

{% endtab %}
{% endtabs %}

## アプリ内メッセージの表示動作を設定する

オプションで、アプリ内メッセージの表示動作を実行時に以下の方法で変更することができます。

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## アプリ内メッセージをオンデマンドで表示する

`DisplayNextInAppMessage()` メソッドを使って、スタック内の次に利用可能なアプリ内メッセージを表示できます。アプリ内メッセージ表示アクションとして`DISPLAY_LATER` または`BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` が選択された場合、メッセージはこの保存されたメッセージのスタックに追加される。

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Unityでアプリ内メッセージデータを受信する

Unity ゲームオブジェクトを登録して、アプリ内メッセージの受信について通知を受けることができます。Brazeコンフィギュレーションエディターからゲームオブジェクトリスナーを設定することを推奨する。コンフィギュレーション・エディターでは、リスナーをAndroidとiOSで別々に設定する必要がある。

ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使用し、`BrazeUnityMessageType.IN_APP_MESSAGE` を指定します。

## アプリ内メッセージを解析する

アプリ内メッセージゲームオブジェクトのコールバックで受け取った受信 `string` メッセージは、便宜上、事前に提供されているモデルオブジェクトに解析できます。

`InAppMessageFactory.BuildInAppMessage()` を使ってアプリ内メッセージを解析しよう。結果として得られるオブジェクトはそのタイプに応じて [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) または [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) のインスタンスになります。

### アプリ内メッセージのコールバック例

```csharp
// Automatically logs a button click, if present.
void InAppMessageReceivedCallback(string message) {
  IInAppMessage inApp = InAppMessageFactory.BuildInAppMessage(message);
  if (inApp is IInAppMessageImmersive) {
    IInAppMessageImmersive inAppImmersive = inApp as IInAppMessageImmersive;
    if (inAppImmersive.Buttons != null && inAppImmersive.Buttons.Count > 0) {
      inAppImmersive.LogButtonClicked(inAppImmersive.Buttons[0].ButtonID);
    }
  }
}
```

## GIFサポート

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## 分析

Brazeが直接表示しないアプリ内メッセージについては、クリック数とインプレッション数を手動で記録する必要がある。

[`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) で `LogClicked()` と `LogImpression()` を使用して、メッセージのクリック数とインプレッション数をログに記録します。

[`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) で `LogButtonClicked(int buttonID)` を使用して、ボタンのクリック数をログに記録します。ボタンは [`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) インスタンスのリストとして表され、各インスタンスには `ButtonID` が含まれます。

## カスタム・アクション・リスナー

ユーザーがアプリ内メッセージを操作する方法をより細かくコントロールする必要がある場合は、`BrazeInAppMessageListener` を使用してそれを `Appboy.AppboyBinding.inAppMessageListener` に割り当てます。使用しないデリゲートについては、単に `null` のままにしておくことができます。

```csharp
BrazeInAppMessageListener listener = new BrazeInAppMessageListener() {
  BeforeInAppMessageDisplayed = BeforeInAppMessageDisplayed,
  OnInAppMessageButtonClicked = OnInAppMessageButtonClicked,
  OnInAppMessageClicked       = OnInAppMessageClicked,
  OnInAppMessageHTMLClicked   = OnInAppMessageHTMLClicked,
  OnInAppMessageDismissed     = OnInAppMessageDismissed,
};
Appboy.AppboyBinding.inAppMessageListener = listener;

public void BeforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Executed before an in-app message is displayed.
}

public void OnInAppMessageButtonClicked(IInAppMessage inAppMessage, InAppMessageButton inAppMessageButton) {
  // Executed whenever an in-app message button is clicked.
}

public void OnInAppMessageClicked(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is clicked.
}

public void OnInAppMessageHTMLClicked(IInAppMessage inAppMessage, Uri uri) {
  // Executed whenever an HTML in-app message is clicked.
}

public void OnInAppMessageDismissed(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is dismissed without a click.
}
```

