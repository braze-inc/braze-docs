---
nav_title: アプリ内メッセージング
article_title: Unity のアプリ内メッセージング
channel: in-app messaging
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "このリファレンス記事では、Unity プラットフォームのアプリ内メッセージング構成ガイドラインについて説明します。"

---

# アプリ内メッセージング統合

> このリファレンス記事では、Unity プラットフォームのアプリ内メッセージング構成ガイドラインについて説明します。

## デフォルトのアプリ内メッセージの動作を構成する

{% tabs %}
{% tab Android %}

Android では、Braze からのアプリ内メッセージは自動的にネイティブに表示されます。この機能を無効にするには、Braze 構成エディタで **「アプリ内メッセージを自動的に表示する」の** 選択を解除します。

代わりに設定することもできます `com_braze_inapp_show_inapp_messages_automatically` に `false` Unityプロジェクトの `braze.xml`。

アプリ内メッセージの初期表示操作は、Braze 設定の「アプリ内メッセージ マネージャーの初期表示操作」で設定できます。

{% endtab %}
{% tab iOS %}

iOS では、Braze からのアプリ内メッセージは自動的にネイティブに表示されます。この機能を無効にするには、Braze 構成エディターでゲーム オブジェクト リスナーを設定し、**「Braze Displays In-App Messages」** が選択されていないことを確認します。

{% endtab %}
{% endtabs %}

## アプリ内メッセージの表示動作の設定

オプションで、実行時にアプリ内メッセージの表示動作を次のように変更できます。

\`\`\`csharp
// トリガーされたときにすぐに表示されるアプリ内メッセージを設定します。
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM\_DISPLAY\_NOW);

// アプリ内メッセージを後で表示し、スタックに保存するように設定します。
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM\_DISPLAY\_LATER);

// トリガーされた後に破棄されるアプリ内メッセージを設定します。
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM\_DISCARD);
\`\`\`

## オンデマンドでアプリ内メッセージを表示する

スタック内の次の利用可能なアプリ内メッセージを表示するには、 `DisplayNextInAppMessage()` 方法。メッセージは、次の場合にこの保存済みメッセージスタックに追加されます。 `DISPLAY_LATER` または `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` アプリ内メッセージ表示アクションとして選択されます。

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Unityでアプリ内メッセージデータを受信する

アプリ内メッセージの受信を通知するために Unity ゲーム オブジェクトを登録できます。ゲーム オブジェクト リスナーは、Braze 構成エディターから設定することをお勧めします。構成エディターでは、Android と iOS のリスナーを個別に設定する必要があります。

実行時にゲームオブジェクトリスナーを設定する必要がある場合は、 `AppboyBinding.ConfigureListener()` 指定する `BrazeUnityMessageType.IN_APP_MESSAGE`。

## アプリ内メッセージの解析

着信 `string` アプリ内メッセージ ゲーム オブジェクト コールバックで受信したメッセージは、便宜上、事前に用意されたモデル オブジェクトに解析できます。

使用 `InAppMessageFactory.BuildInAppMessage()` アプリ内メッセージを解析します。結果のオブジェクトは、 [`IInAppMessage.cs`][13] または [`IInAppMessageImmersive.cs`][12] 種類によって異なります。

### アプリ内メッセージコールバックの例

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

## 分析

Braze によって直接表示されないアプリ内メッセージのクリックとインプレッションは手動で記録する必要があります。

使用 `LogClicked()` そして `LogImpression()` の上 [`IInAppMessage`][13] メッセージのクリック数と表示回数を記録します。

使用 `LogButtonClicked(int buttonID)` の上 [`IInAppMessageImmersive`][12] ボタンのクリックを記録します。ボタンはリストとして表されることに注意してください。[`InAppMessageButton`][8] インスタンスにはそれぞれ `ButtonID`。

## カスタムアクションリスナー

ユーザーがアプリ内メッセージをどのように操作するかをより細かく制御する必要がある場合は、 `BrazeInAppMessageListener` そしてそれを割り当てる `Appboy.AppboyBinding.inAppMessageListener`。使用したくないデリゲートについては、そのままにしておくことができます。 `null`。

\`\`\`csharp
BrazeInAppMessageListener listener = new BrazeInAppMessageListener() {
  BeforeInAppMessageDisplayed = BeforeInAppMessageDisplayed、
  OnInAppMessageButtonClicked = OnInAppMessageButtonClicked、
  OnInAppMessageClicked = OnInAppMessageClicked、
  OnInAppMessageHTMLクリック = OnInAppMessageHTMLクリック、
  OnInAppMessageDismissed = OnInAppMessageDismissed、
()
Appboy.AppboyBinding.inAppMessageListener = リスナー;

public void BeforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // アプリ内メッセージが表示される前に実行されます。
()

public void OnInAppMessageButtonClicked(IInAppMessage inAppMessage, InAppMessageButton inAppMessageButton) {
  // アプリ内メッセージボタンがクリックされるたびに実行されます。
()

public void OnInAppMessageClicked(IInAppMessage inAppMessage) {
  // アプリ内メッセージがクリックされるたびに実行されます。
()

public void OnInAppMessageHTMLClicked(IInAppMessage inAppMessage, Uri uri) {
  // HTML アプリ内メッセージがクリックされるたびに実行されます。
()

public void OnInAppMessageDismissed(IInAppMessage inAppMessage) {
  // アプリ内メッセージがクリックされずに閉じられるたびに実行されます。
()
\`\`\`

[8]: https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs
[12]: https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs
[13]: https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs
