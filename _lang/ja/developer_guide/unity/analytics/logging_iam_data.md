## アプリ内メッセージ s のサブスクライブ

Unity ゲームオブジェクトを登録して、アプリ内メッセージの受信について通知を受けることができます。Brazeコンフィギュレーションエディターからゲームオブジェクトリスナーを設定することを推奨する。コンフィギュレーション・エディターでは、リスナーをAndroidとiOSで別々に設定する必要がある。

ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使用し、`BrazeUnityMessageType.IN_APP_MESSAGE` を指定します。

## メッセージの解析

アプリ内メッセージゲームオブジェクトのコールバックで受け取った受信 `string` メッセージは、便宜上、事前に提供されているモデルオブジェクトに解析できます。

`InAppMessageFactory.BuildInAppMessage()` を使ってアプリ内メッセージを解析しよう。結果として得られるオブジェクトはそのタイプに応じて [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) または [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) のインスタンスになります。

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

## メッセージデータのロギング

Brazeが直接表示しないアプリ内メッセージについては、クリック数とインプレッション数を手動で記録する必要がある。

[`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) で `LogClicked()` と `LogImpression()` を使用して、メッセージのクリック数とインプレッション数をログに記録します。

[`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs) で `LogButtonClicked(int buttonID)` を使用して、ボタンのクリック数をログに記録します。ボタンは [`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) インスタンスのリストとして表され、各インスタンスには `ButtonID` が含まれます。
