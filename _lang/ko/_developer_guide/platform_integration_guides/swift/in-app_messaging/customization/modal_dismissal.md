---
nav_title: 모달 해제
article_title: iOS용 인앱 메시지 모달 해제
platform: Swift
page_order: 7
description: "이 참조 문서에서는 Swift SDK의 인앱 메시징 Modal 해제를 다룹니다."
channel:
  - in-app messages
---

# Modal 해제

> 외부 탭 해제 기능을 활성화하려면 사용자 지정하려는 인앱 메시지 유형의 `Attributes` 구조에서 `dismissOnBackgroundTap` 속성정보를 수정하면 됩니다. 

예를 들어 Modal 이미지 인앱 메시지에 이 기능을 사용하려면 다음과 같이 구성할 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

`Attributes` 을 통한 사용자 지정은 Objective-C에서 사용할 수 없습니다.

{% endtab %}
{% endtabs %}

기본값은 `false` 입니다. 사용자가 인앱 메시지 외부를 클릭할 때 Modal 인앱 메시지의 해제 여부를 결정합니다.

| `DismissModalOnOutsideTap` | 설명 |
|----------|-------------|
| `true`         | Modal 인앱 메시지는 외부를 탭하면 해제됩니다.     |
| `false`        | 기본 Modal 인앱 메시지는 외부를 탭해도 해제되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

인앱 메시지 사용자 지정에 대한 자세한 내용은 이 [문서](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization)를 참조하세요.