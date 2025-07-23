## 앱 내 메시지 구독

수신 인앱 메시지에 대한 알림을 받도록 Unity 게임 오브젝트를 등록할 수 있습니다. Braze 설정 에디터에서 게임 오브젝트 리스너를 설정하는 것을 권장합니다. 구성 편집기에서 Android 및 iOS용 리스너를 별도로 설정해야 합니다.

런타임에 게임 오브젝트 리스너를 구성해야 하는 경우 `AppboyBinding.ConfigureListener()`를 사용하고 `BrazeUnityMessageType.IN_APP_MESSAGE`를 지정합니다.

## 메시지 파싱

인앱 메시지 게임 오브젝트 콜백에서 수신되는 `string` 메시지는 편의를 위해 미리 제공된 모델 오브젝트로 구문 분석할 수 있습니다.

`InAppMessageFactory.BuildInAppMessage()` 을 사용하여 인앱 메시지를 파싱합니다. 결과 오브젝트는 해당 유형에 따라 [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) 또는 [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs)의 인스턴스가 됩니다.

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

## 메시지 데이터 로깅

Braze가 직접 표시하지 않는 인앱 메시지의 경우 클릭 수와 노출 수를 수동으로 기록해야 합니다.

[`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs)에서 `LogClicked()` 및 `LogImpression()`을 사용하여 메시지의 클릭 및 노출 횟수를 기록합니다.

[`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs)에서 `LogButtonClicked(int buttonID)`를 사용하여 버튼 클릭을 기록합니다. 버튼은 [`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) 인스턴스의 목록으로 표시되며, 각각 `ButtonID`를 포함합니다.
