---
nav_title: "푸시 실행 버튼"
article_title: 푸시 실행 버튼
page_order: 1
page_type: reference
description: "이 참조 문서에서는 푸시 액션 버튼의 정의와 iOS 및 Android 플랫폼 간의 차이점에 대해 설명합니다."
channel:
  - Push

---

# 푸시 액션 버튼

![두 개의 푸시 동작 버튼이 있는 iOS 푸시 알림입니다: 수락 및 거부.][1]{: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> 푸시 액션 버튼을 사용하면 Braze iOS 및 Android 푸시 알림을 사용할 때 버튼의 콘텐츠와 액션을 설정할 수 있습니다. 액션 버튼을 사용하면 사용자가 앱 환경을 클릭할 필요 없이 알림에서 앱과 직접 상호 작용할 수 있습니다.

## 액션 버튼 만들기

각 대화형 버튼은 웹 페이지 또는 딥링크로 연결되거나 앱을 열 수 있습니다. 대시보드의 푸시 메시지 작성기의 **클릭 시 동작** 섹션에서 푸시 동작 버튼을 지정할 수 있습니다.

{% alert important %}
단일 캠페인에서 iOS와 Android를 모두 타겟팅하려면 멀티채널 캠페인을 만드세요. [퀵 푸시 캠페인]({{site.baseurl}}/quick_push)을 사용하여 iOS 및 Android를 모두 타겟팅하는 경우 푸시 실행 버튼은 지원되지 않습니다.
{% endalert %}

### iOS {#ios}

iOS 푸시 메시지에서 액션 버튼을 사용하려면 다음과 같이 하세요:

1. iOS [푸시 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)을 생성하고 **작성** 탭에서 실행 버튼을 활성화합니다.
2. 사용 가능한 다음 버튼 조합에서 **iOS 알림 카테고리를** 선택합니다:
 - 수락/거부
 - 예/아니요
 - 확인/취소
 - 더 보기
 - 사전 등록된 사용자 지정 iOS 카테고리

![iOS 알림 카테고리 드롭다운 메뉴]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Due to iOS's handling of buttons, you need to perform additional integration steps when setting up push action buttons, which are outlined in our [developer documentation]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). 특히 iOS 카테고리를 구성하거나 특정 기본 버튼 옵션 중에서 선택해야 합니다. Android 통합의 경우 이러한 버튼은 자동으로 작동합니다.
{% endalert %}

### Android {#android}

Android 푸시 메시지에서 액션 버튼을 사용하려면 다음과 같이 하세요:

1. Android [푸시 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/)을 만들고 **작성** 탭에서 알림 버튼을 활성화합니다.
2. <i class="fas fa-plus-circle"></i> **버튼 추가를** 선택하고 버튼 텍스트와 **클릭 시 동작을** 지정합니다. 다음 사용 가능한 작업 중에서 선택할 수 있습니다:
  - 앱 열기
  - 웹 URL로 리디렉션
  - 애플리케이션으로의 [딥링크]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)

![알림 버튼의 클릭 동작으로 '앱 열기'를 선택합니다.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

푸시 버튼은 최대 3개까지 추가할 수 있습니다.

#### Android 문자 수 제한

쌓아 올리는 iOS 버튼과 달리 Android 버튼은 일렬로 나란히 표시됩니다. 즉, 버튼을 더 많이 추가할수록(최대 3개까지) 버튼 복사 공간이 줄어듭니다. 

![텍스트가 잘린 Android 푸시 동작 버튼]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

다음 표에는 버튼 복사본이 잘리기 전에 추가할 수 있는 문자 수가 버튼 수에 따라 간략하게 나와 있습니다.

| 버튼 개수 | 버튼당 최대 글자 수 |
| --- | --- |
| 1 | 46자 |
| 2 | 20자 |
| 3 | 11자 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


[1]: {% image_buster /assets/img_archive/push_action_example.png %}
