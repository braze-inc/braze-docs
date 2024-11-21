---
nav_title: 이메일 가입 양식
article_title: 이메일 가입 양식
alias: "/email_capture/"
description: "이 참조 페이지에서는 앱 내 메시지 드래그 앤 드롭 편집기를 사용하여 이메일 가입 양식을 만드는 방법을 설명합니다."
---

# 이메일 가입 양식

> 드래그 앤 드롭 이메일 가입 인앱 메시지 템플릿을 사용하여 사용자의 이메일 주소를 수집하고 구독 그룹을 늘릴 수 있습니다.

## SDK 요구 사항

### 최소 SDK 버전

드래그 앤 드롭 편집기를 사용하여 만든 메시지는 다음 최소 SDK 버전을 사용하는 사용자에게만 보낼 수 있습니다. 자세한 내용과 주의해야 할 뉘앙스는 [드래그 앤 드롭으로 인앱 메시지 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) 도움말의 [전제 조건][1] 섹션을 참조하세요.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### 텍스트 링크용 소프트웨어 개발 키트 버전

메시지를 해제하지 않는 텍스트 링크를 포함하려면 사용자가 다음 최소 SDK 버전을 사용해야 합니다.

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
인앱 메시지에 URL로 리디렉션되는 링크를 포함했는데 사용자가 지정된 최소 SDK 버전을 사용하지 않는 경우 링크를 클릭하면 메시지가 닫히고 사용자가 메시지로 돌아가 양식을 제출할 수 없습니다.
{% endalert %}

## 이메일 가입 양식 만들기

드래그 앤 드롭 인앱 메시지를 만들 때 템플릿에 대한 **이메일 가입을** 선택하고 **메시지 작성을** 선택합니다. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

### 1단계: 메시지 스타일을 설정하세요

템플릿을 사용자 정의하기 전에 사이드 메뉴를 사용하여 전체 메시지에 대한 메시지 수준 스타일을 설정할 수 있습니다. 예를 들어, 메시지에 포함된 모든 텍스트의 글꼴이나 모든 링크의 색상을 사용자 정의할 수 있습니다. 메시지를 모달 또는 전체 화면 표시 유형으로 만들 수도 있습니다.

### 2단계: 이메일 가입 구성 요소 사용자 지정

이메일 가입 양식 작성을 시작하려면 편집기에서 이메일 캡처 요소를 선택합니다. 기본적으로 수집된 이메일 주소에는 글로벌 구독 그룹이 **구독됨**으로 설정됩니다. 특정 구독 그룹에 사용자를 옵트인하려면 [이메일 구독 상태 업데이트하기]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)를 참조하세요.

이메일 캡처 요소의 플레이스홀더 텍스트와 레이블 텍스트를 사용자 지정할 수 있습니다.

#### 이메일 유효성 검사

사용자가 허용되지 않는 특수 문자가 포함된 이메일 주소를 입력하면 일반 오류 표시기가 표시되며 양식을 제출할 수 없습니다. 이 오류 메시지는 사용자 지정할 수 없습니다. **미리보기 및 테스트** 탭과 테스트 기기에서 오류 동작을 확인할 수 있습니다. [이메일 유효성 검사]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)에서 Braze가 이메일 주소 형식을 지정하는 방법에 대해 자세히 알아보세요.

### 3단계: 고지 사항 언어 추가(선택 사항)

브랜드 개인정보처리방침 및 이용약관에 대한 옵트인 문구와 링크를 메시지에 포함할 것을 권장합니다. 템플릿에 입력 안내 면책 조항을 예시로만 제공했지만 규정 준수 목적으로만 사용해서는 안 됩니다. 법무팀과 협력하여 특정 브랜드에 맞는 언어를 개발해야 합니다.

{% alert note %}
전달 가능성 모범 사례는 법적 요건을 초과하는 경우가 많으므로 항상 이메일 전송에 대한 명시적인 동의를 받고 사용자가 쉽게 거부할 수 있도록 하는 것이 좋습니다.
{% endalert %}

### 4단계: 메시지를 스타일링하세요

드래그 앤 드롭 [인앱 메시지 구성 요소][3]를 사용하여 메시지의 모양과 느낌을 사용자 정의할 수 있습니다.

## 보고

캠페인이 시작된 후에는 실시간으로 결과를 분석하여 얼마나 많은 사용자가 캠페인에 참여했는지 확인할 수 있습니다. 얼마나 많은 사용자가 구독 그룹에 옵트인했는지 확인하려면 인앱 메시지를 수신하고 양식을 제출한 사용자를 필터링하여 구독 그룹에 가입한 사용자 [세그먼트를 만들][5] 수 있습니다.

## 모범 사례

### 이중 옵트인 인증

회원님의 리스트에 가입한 사람이 정말로 회원님의 리스트에 가입할 의사가 있고 정확한 이메일 주소를 제공했는지 확인하려면 이메일 가입 양식을 통해 가입한 사람에게 [이중 옵트인](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in) 플로우를 보내 두 번째 확인을 받는 것이 좋습니다.

이를 설정하는 방법 중 하나는 캔버스 플로우를 사용하는 것입니다.

1. 액션 기반 캔버스를 만들고 사용자가 Braze에 이메일 주소를 추가할 때 트리거되도록 설정하세요. 플랫폼을 처음 사용하는 사용자를 타겟팅할 수 있도록 허용해야 합니다(예: 캔버스에서 필터가 없는 세그먼트를 사용하는 등).
2. {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquid 태그로 연결되는 하이퍼링크가 있는 CTA가 포함된 이메일 메시지 단계를 만듭니다. 버튼을 클릭하면 사용자의 이메일 구독 상태가 `opted_in`으로 변경됩니다.
3. [작업 경로 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths)를 추가합니다.
4. 첫 번째 경로의 경우 사용자가 이메일 구독 상태를 `opted_in`으로 변경할 때 이메일을 트리거합니다. 이 이메일은 사용자에게 이메일이 확인되었음을 알려야 합니다.
5. 창이 만료된 후 캔버스를 종료하는 다른 경로를 설정합니다.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
