---
nav_title: 다크 모드 테마
article_title: 인앱 메시지를 위한 다크 모드
page_order: 5
description: "이 참조 문서에서는 다크 모드 테마를 설정하는 방법과 호환성 고려 사항을 포함하여 Braze 인앱 메시지 다크 모드 지원에 대해 설명합니다."
channel:
  - in-app messages

---

# 다크 모드 테마

> 다크 모드에서는 사용자가 시스템 전체에 대한 색상 기본 설정을 지정할 수 있습니다( [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) 및 [iOS 13에](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/) 도입됨). '어두운' 테마는 배터리 수명을 절약하고 사용자의 눈의 피로를 줄이는 동시에 앱 개발자가 사용자가 선호하는 어두운 색상 테마를 더 쉽게 구현할 수 있도록 하기 위한 것입니다.

Braze 인앱 메시지는 대체 다크 테마를 추가하여 사용자의 선호도에 따라 적절한 색상 메시지를 전달할 수 있도록 지원하며, 앱 디자인과 일관성을 유지할 수 있도록 도와줍니다.

## 다크 모드 작동 방식

Android 10 또는 iOS 13 이상 버전을 사용하는 사용자는 기기 설정에서 다크 모드를 켜거나 끌 수 있습니다.

다크 모드가 인에이블먼트되면 기기의 기본 메뉴와 화면(푸시 알림, 기기 설정 등)이 짙은 회색으로 변경됩니다. 앱 코드에서 대체 테마를 지정하여 다크 모드를 지원하도록 선택할 수도 있습니다.

## 다크 모드 테마 설정하기

[인앱 메시지를 작성할]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) 때 스타일 탭에 있는 새로운 다크 모드 옵션을 사용하면 기기에서 다크 모드를 사용하는 사용자를 위해 대체 색상 테마를 쉽게 추가할 수 있습니다.

\![인앱 메시지를 만들 때 스타일 탭에서 라이트 모드 스타일과 다크 모드 스타일 간에 전환하는 사용자.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

이 옵션을 인에이블먼트하면 색상 선택기를 사용하여 인앱 메시지에 어두운 테마 색상을 선택하거나 기존 [색상 프로필을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) 선택하여 기존의 어두운 테마 또는 밝은 테마를 재사용할 수 있습니다.

{% alert note %}
앱에서 자체 어두운 테마를 제공하지 않더라도 이 기능을 사용할 수 있습니다. 그러나 다크 모드를 지원하지 않는 기기는 기본값으로 라이트 테마가 표시됩니다. 인앱 메시지가 표시되는 동안 Android에서 기기 테마를 변경해도 해당 인앱 메시지에 사용되는 테마는 변경되지 않습니다.
{% endalert %}

### 다크 모드를 지속적으로 사용하기

모든 인앱 메시지에 다크 모드를 사용하려면 **템플릿** > **인앱 메시지 템플릿으로** 이동하세요.

드롭다운에서 [색상 프로필 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) 선택합니다. 다크 모드 테마에 맞는 색상 프로필을 만듭니다. 그런 다음 인앱 메시지의 다크 모드 버전을 만들 때마다 해당 색상 프로필을 선택하여 인앱 메시지의 모양을 일관되게 유지할 수 있습니다.

## 호환성

- 사용자는 iOS 기기 버전 13 이상 또는 Android 기기 버전 10 이상이어야 합니다.
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+가 필요합니다.

{% alert note %}
다크 모드 앱은 Android 10 및 iOS 13에 도입되었습니다. 휴대폰을 이 버전 이상으로 업그레이드하지 않은 사용자에게는 라이트 테마만 표시됩니다. <br><br>캠페인은 사용자의 다크 모드 설정이나 OS 버전에 관계없이 선택한 오디언스에 해당하는 모든 사용자에게 계속 게재됩니다.
{% endalert %}

## HTML 인앱 메시지 사용

HTML 인앱 메시지에 대한 어둡고 밝은 테마를 만들려면 사용자의 선호도를 감지하는 [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS 미디어 기능을 사용하여 사용자의 선호도를 감지할 수 있습니다.

예를 들어

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

