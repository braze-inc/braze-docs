---
nav_title: "푸시 실행 버튼"
article_title: 푸시 실행 버튼
page_order: 1
page_type: reference
description: "이 참고 문서에서는 푸시 실행 버튼의 정의와 iOS 및 Android 플랫폼 간의 차이점에 대해 설명합니다."
channel:
  - Push

---

# 푸시 실행 버튼

푸시 실행 버튼이 두 개 있는 iOS 푸시 알림입니다: 수락 및 거부.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> 푸시 실행 버튼을 사용하면 Braze iOS 및 Android 푸시 알림을 사용할 때 버튼의 콘텐츠와 동작을 설정할 수 있습니다. 실행 버튼을 사용하면 사용자가 앱 경험을 클릭할 필요 없이 알림에서 앱과 직접 상호 작용할 수 있습니다.

## 실행 버튼 만들기

각 대화형 버튼은 웹 페이지 또는 딥링크로 연결되거나 앱을 열 수 있습니다. 

- 표준 푸시 캠페인의 경우 대시보드의 푸시 메시지 작성기의 **온클릭 동작** 섹션에서 푸시 실행 버튼을 지정할 수 있습니다.
- [빠른 푸시 캠페인의]({{site.baseurl}}/quick_push) 경우 **설정** 탭에서 각 플랫폼별로 실행 버튼을 별도로 구성할 수 있습니다.

{% tabs %}
{% tab iOS %}
### iOS {#ios}

iOS 푸시 메시지에서 실행 버튼을 사용하려면 다음과 같이 하세요:

1. 표준 캠페인의 경우 **작성** 탭에서, 빠른 푸시의 경우 **설정** 탭에서 실행 버튼을 켭니다.
2. 사용 가능한 다음 버튼 조합에서 **iOS 알림 카테고리를** 선택합니다:
 - 수락/거절
 - 예 / 아니요
 - 확인/취소
 - 자세히 보기
 - 사전 등록된 커스텀 iOS 카테고리

iOS 알림 카테고리 드롭다운 메뉴.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
iOS의 버튼 처리 방식으로 인해 푸시 실행 버튼을 설정할 때 추가적인 통합 단계를 수행해야 하며, 이는 [개발자 설명서에]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories) 설명되어 있습니다. 특히 iOS 카테고리를 구성하거나 특정 기본값 버튼 옵션 중에서 선택해야 합니다. Android 통합의 경우 이러한 버튼이 자동으로 작동합니다.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

Android 푸시 메시지에서 실행 버튼을 사용하려면 다음과 같이 하세요:

1. 표준 캠페인의 경우 **작성** 탭에서, 빠른 푸시의 경우 **설정** 탭에서 실행 버튼을 켭니다.
2. <i class="fas fa-plus-circle"></i> **버튼 추가를** 선택하고 버튼 텍스트와 **클릭 시 동작을** 지정합니다. 다음 사용 가능한 작업 중에서 선택할 수 있습니다:
  - 앱 열기
  - 웹 URL로 리디렉션
  - 애플리케이션으로 [딥링크하기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) 

알림 버튼의 클릭 동작으로 '앱 열기'를 선택합니다.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

푸시 버튼은 최대 3개까지 추가할 수 있습니다.

#### Android 글자 수 제한

겹겹이 쌓여 있는 iOS 버튼과 달리 Android 버튼은 나란히 나란히 표시됩니다. 즉, 버튼을 더 많이 추가할수록(최대 3개까지) 버튼 복사 공간이 줄어듭니다. 

\![잘린 텍스트가 있는 Android 푸시 실행 버튼.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

다음 표는 버튼 수에 따라 버튼 사본이 잘리기 전에 추가할 수 있는 문자 수를 간략하게 설명합니다:

| 버튼 수 | 버튼당 최대 글자 수 |
| --- | --- |
| 1 | 46자 |
| 2 | 20자 |
| 3 | 11자 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

