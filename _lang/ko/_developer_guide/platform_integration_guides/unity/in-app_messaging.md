---
nav_title: 인앱 메시징
article_title: Unity용 인앱 메시징
channel: in-app messaging
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "이 참조 문서에서는 Unity 플랫폼용 인앱 메시징 구성 지침을 다룹니다."

---

# 인앱 메시징 통합

> 이 참조 문서에서는 Unity 플랫폼용 인앱 메시징 구성 지침을 다룹니다.

## 기본 인앱 메시지 동작 구성

{% tabs %}
{% tab Android %}

Android에서는 Braze의 인앱 메시지가 기본적으로 자동으로 표시됩니다. 이 기능을 비활성화하려면 Braze 구성 편집기에서 **인앱 메시지 자동 표시**를 선택 해제합니다.

또는 Unity 프로젝트의 `braze.xml`에서 `com_braze_inapp_show_inapp_messages_automatically`를 `false`로 설정할 수 있습니다.

초기 인앱 메시지 표시 작업은 Braze 설정에서 '인앱 메시지 매니저 초기 표시 작업'을 통해 설정할 수 있습니다.

{% endtab %}
{% tab iOS %}

iOS에서는 Braze의 인앱 메시지가 기본적으로 자동으로 표시됩니다. 이 기능을 비활성화하려면 Braze 구성 편집기에서 게임 오브젝트 리스너를 설정하고 **Braze 표시 인앱 메시지**가 선택되어 있지 않은지 확인하세요.

초기 인앱 메시지 표시 작업은 Braze 설정에서 '인앱 메시지 매니저 초기 표시 작업'을 통해 설정할 수 있습니다.

{% endtab %}
{% endtabs %}

## 인앱 메시지 표시 동작 구성

다음을 통해 런타임에 인앱 메시지의 표시 동작을 선택적으로 변경할 수 있습니다.

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## 온디맨드 인앱 메시지 표시

`DisplayNextInAppMessage()` 메서드를 통해 스택에서 사용 가능한 다음 인앱 메시지를 표시할 수 있습니다. `DISPLAY_LATER` 또는 `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER`를 인앱 메시지 표시 동작으로 선택하면 이 저장된 메시지 스택에 메시지가 추가됩니다.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```

## Unity에서 인앱 메시지 데이터 수신하기

수신 인앱 메시지에 대한 알림을 받도록 Unity 게임 오브젝트를 등록할 수 있습니다. Braze 설정 에디터에서 게임 오브젝트 리스너를 설정하는 것을 권장합니다. 구성 편집기에서 Android 및 iOS용 리스너를 별도로 설정해야 합니다.

런타임에 게임 오브젝트 리스너를 구성해야 하는 경우 `AppboyBinding.ConfigureListener()`를 사용하고 `BrazeUnityMessageType.IN_APP_MESSAGE`를 지정합니다.

## 인앱 메시지 구문 분석

인앱 메시지 게임 오브젝트 콜백에서 수신되는 `string` 메시지는 편의를 위해 미리 제공된 모델 오브젝트로 구문 분석할 수 있습니다.

`InAppMessageFactory.BuildInAppMessage()` 을 사용하여 인앱 메시지를 파싱합니다. 결과 오브젝트는 해당 유형에 따라 [`IInAppMessage.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs) 또는 [`IInAppMessageImmersive.cs`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs)의 인스턴스가 됩니다.

### 인앱 메시지 콜백 예시

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

## GIF 지원

{% multi_lang_include wrappers/gif_support/in_app_messaging.md %}

## 분석

Braze가 직접 표시하지 않는 인앱 메시지의 경우 클릭 수와 노출 수를 수동으로 기록해야 합니다.

[`IInAppMessage`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessage.cs)에서 `LogClicked()` 및 `LogImpression()`을 사용하여 메시지의 클릭 및 노출 횟수를 기록합니다.

[`IInAppMessageImmersive`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/IInAppMessageImmersive.cs)에서 `LogButtonClicked(int buttonID)`를 사용하여 버튼 클릭을 기록합니다. 버튼은 [`InAppMessageButton`](https://github.com/braze-inc/braze-unity-sdk/blob/18cb8ee89f1841c576eb954793edb6e06f9130b4/Assets/Plugins/Appboy/Models/InAppMessage/InAppMessageButton.cs) 인스턴스의 목록으로 표시되며, 각각 `ButtonID`를 포함합니다.

## 사용자 지정 액션 리스너

사용자가 인앱 메시지와 상호 작용하는 방식을 더 잘 제어해야 하는 경우 `BrazeInAppMessageListener`를 사용하여 `Appboy.AppboyBinding.inAppMessageListener`에 할당합니다. 사용하지 않으려는 위임의 경우 `null`로 남겨두면 됩니다.

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

