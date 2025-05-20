{% multi_lang_include developer_guide/prerequisites/android.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) 합니다.

## 커스텀 알림 레이아웃

Braze 알림은 [데이터 메시지로](https://firebase.google.com/docs/cloud-messaging/concept-options) 전송되므로 앱이 백그라운드에 있을 때 시스템에서 자동으로 처리할 수 있는 알림 메시지와 달리 백그라운드에서도 항상 응답하고 그에 따른 동작을 수행할 수 있습니다(앱이 백그라운드에 있을 때 알림 메시지와 달리). 이와 같이 애플리케이션은 예를 들어 알림 트레이에 전달된 알림 내에서 개인화된 UI 요소를 표시하여 경험을 사용자 지정할 수 있습니다. 이 방식으로 푸시를 구현하는 것이 일부에게는 낯설 수 있지만, Braze의 잘 알려진 기능 중 하나인 [푸시 스토리]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)는 커스텀 뷰 컴포넌트를 사용하여 몰입감 있는 경험을 만드는 좋은 예입니다!

{% alert important %}
Android는 커스텀 알림 보기를 구현하는 데 사용할 수 있는 구성요소에 몇 가지 제한을 둡니다. 알림 보기 레이아웃은 _오직_ [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) 프레임워크와 호환되는 View 객체만 포함해야 합니다.
{% endalert %}

## 개인화된 푸시 알림

푸시 알림은 사용자 지정 보기 계층 구조 내에 사용자별 정보를 표시할 수 있습니다. 다음 예에서는 API 트리거를 사용하여 앱에서 특정 작업을 완료한 후 현재 진행 상황을 추적할 수 있도록 사용자에게 개인화된 푸시 알림을 보냅니다.

![개인화된 푸시 대시보드 예시]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

대시보드에서 개인화된 푸시를 설정하려면 표시하려는 특정 카테고리를 등록한 다음 Liquid를 사용하여 표시하려는 관련 사용자 속성을 설정합니다.

![개인화된 푸시 대시보드 예시]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
