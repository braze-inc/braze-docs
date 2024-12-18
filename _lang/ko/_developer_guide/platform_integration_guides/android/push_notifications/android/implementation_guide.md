---
nav_title: 고급 구현 가이드 (선택 사항)
article_title: Android용 고급 푸시 알림 구현 (선택 사항)
platform: Android
page_order: 29
description: "이 고급 구현 가이드에서는 사용자별 정보가 메시지에 표시되도록 푸시 알림의 레이아웃을 사용자 지정하는 방법을 다룹니다. 저희 팀이 구축한 사용 사례 예제와 함께 코드 스니펫 및 로깅 분석에 대한 지침도 포함되어 있습니다."
channel:
  - push
---

<br>
{% alert important %}
기본 푸시 알림 개발자 통합 가이드를 찾고 계신가요? 여기에서 확인하세요[참조: ]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).
{% endalert %}

# 고급 구현 가이드

> 이 선택적이고 고급 구현 가이드는 푸시 메시지를 최대한 활용하기 위해 커스텀 FirebaseMessagingService 하위 클래스를 활용하는 방법을 다룹니다. 저희 팀이 구축한 커스텀 사용 사례와 함께 제공되는 코드 스니펫, 로깅 분석에 대한 안내가 포함되어 있습니다. Braze 데모 저장소 [여기](https://github.com/braze-inc/braze-growth-shares-android-demo-app)를 방문하세요! 이 구현 가이드는 Kotlin 구현을 중심으로 하지만 관심 있는 사람을 위해 Java 스니펫도 제공됩니다.

## 커스텀 알림 레이아웃

Braze 알림은 [데이터 메시지](https://firebase.google.com/docs/cloud-messaging/concept-options)로 발송되므로, 애플리케이션이 백그라운드에서도 항상 적절하게 동작을 수행하고 응답할 기회가 있음을 의미합니다(앱이 백그라운드에 있을 때 시스템에서 자동으로 처리할 수 있는 알림 메시지와는 반대됨). 이와 같이 애플리케이션은 예를 들어 알림 트레이에 전달된 알림 내에서 개인화된 UI 요소를 표시하여 경험을 사용자 지정할 수 있습니다. 이 방식으로 푸시를 구현하는 것이 일부에게는 낯설 수 있지만, Braze의 잘 알려진 기능 중 하나인 [푸시 스토리]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)는 커스텀 뷰 컴포넌트를 사용하여 몰입감 있는 경험을 만드는 좋은 예입니다!

#### 요구 사항

Android는 커스텀 알림 보기를 구현하는 데 사용할 수 있는 구성요소에 몇 가지 제한을 둡니다. 알림 보기 레이아웃은 _오직_ [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) 프레임워크와 호환되는 View 객체만 포함해야 합니다.

### 개인화된 푸시 알림

푸시 알림은 사용자 지정 보기 계층 구조 내에 사용자별 정보를 표시할 수 있습니다. 다음 예는 사용자가 특정 작업(Braze 학습 과정)을 완료한 후 푸시 알림을 표시하고 이제 이 알림을 확장하여 진행 상황을 확인하도록 권장하는 예입니다. 여기에 제공된 정보는 사용자에 따라 다르며, API 트리거를 활용하여 특정 사용자 작업을 수행하거나 세션을 완료할 때 발송될 수 있습니다. 

![개인화된 푸시 대시보드 예시]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

#### 대시보드 구성

대시보드에서 개인화된 푸시를 설정하려면 표시하려는 특정 카테고리를 등록해야 합니다. 표준 Liquid를 사용하여 키-값 쌍 내에서 메시지를 표시하려는 적절한 사용자 속성을 설정하십시오. 이러한 보기는 특정 고객 프로필의 특정 사용자 속성을 기반으로 개인화될 수 있습니다.

![개인화된 푸시 대시보드 예시]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

##### 분석을 기록할 준비가 되셨습니까?
데이터 흐름의 진행 방식을 더 잘 이해하려면 [다음 섹션](#logging-analytics)을 참조하세요.

## 로그 분석

### Braze API를 사용한 로깅(권장)

로깅 분석은 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에 접속한 고객 서버를 통해 실시간으로만 수행할 수 있습니다. 분석을 기록하려면 다음 스크린샷과 같이 키-값 페어 필드에 `braze_id` 값을 보내 업데이트할 고객 프로필을 식별합니다.

![개인화된 푸시 대시보드 예시]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:80%;"}

### 수동으로 로깅하기 

`FirebaseMessagingService.onMessageReceived` 구현 내에서 또는 페이로드에 있는 추가 항목을 기반으로 시작 활동 내에서 원하는 모든 요소를 기록함으로써 수동 로깅을 수행할 수 있습니다. 하지만 명심할 중요한 사항은 Android 시스템에 의해 [플래그가 지정되거나 종료](https://firebase.google.com/docs/cloud-messaging/android/receive)되지 않으려면 `FirebaseMessagingService` 서브클래스는 호출 후 10초 이내에 실행을 완료_해야_ 한다는 점입니다. 


