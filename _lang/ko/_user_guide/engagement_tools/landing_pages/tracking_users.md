---
nav\_title: 사용자 추적 글\_title: 양식 설명을 통해 사용자를 추적합니다: "메시지에 Liquid 태그를 추가하여 랜딩 페이지를 통해 양식을 제출하는 사용자를 식별하는 방법을 알아보세요." page\_order: 2
---

# 양식을 통한 사용자 추적

> 원시 %}`{% 랜딩{1> 페이지 URL %}`{%<1} 엔드드로우 %}를 추가하여 랜딩 페이지를 통해 양식을 제출한 사용자를 추적하는 방법을 알아보세요. Liquid 태그를 메시지에 추가하세요. 이 리퀴드 태그는 이메일, SMS, 인앱 메시지 등 모든 Braze 메시징 채널에서 지원됩니다. 추적 데이터에 대해 자세히 알아보려면 [랜딩 페이지 추적 데이터 정보를]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data) 참조하세요.

## 작동 방식

브레이즈에서 단일 또는 멀티채널 메시지에 랜딩 페이지 리퀴드 태그를 추가할 수 있습니다. 사용자가 해당 랜딩 페이지를 방문하여 양식을 제출하면 Braze는 해당 사용자에 대한 새 프로필을 생성하지 않고 해당 데이터를 기존 프로필에 자동으로 연결합니다.

{% 알림 팁 %} 외부 채널에 페이지 URL을 임베드하여 리드 생성을 위한 랜딩 페이지를 사용할 수도 있습니다. 랜딩 페이지를 만든 후 랜딩 **페이지 세부 정보로** 이동하여 랜딩 페이지의 고유 URL을 얻습니다. {% endalert %}

## 랜딩 페이지 리퀴드 태그 사용

### 필수 조건

시작하기 전에 [랜딩 페이지와]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) [캠페인을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/) 만들어야 합니다.

### 1단계: URL 핸들 확인

Braze는 랜딩 페이지의 URL 핸들을 사용하여 고유한 리퀴드 태그를 생성합니다. 현재 URL 핸들을 변경하려면 **메시징** > **랜딩 페이지**로 이동한 다음 랜딩 페이지를 엽니다. **URL 핸들에서** 새 URL 핸들을 입력할 수 있습니다.

{% 경고 경고 %} 메시지를 보낸 후 URL 핸들을 변경하면 이전 URL을 사용하여 랜딩 페이지를 방문하려고 하는 모든 사용자가 `404` 페이지로 전송됩니다. {% 끝알람 %}

브라즈 랜딩 페이지의 URL 핸들 예시\]({% image\_buster /assets/img/landing\_pages/url-handle-example.png %}){: style="max-width:80%;"}

### 2단계: 리퀴드 태그 생성

**메시징** > **캠페인으로** 이동한 다음 캠페인을 선택합니다. 메시지 편집기에서 **맞춤설정을** 선택합니다.

드래그 앤 드롭 편집기의 '개인화 추가' 버튼\]({% image\_buster /assets/img/랜딩\_페이지/select-personalization.png %}){:: style="max-width:75%;"}

Braze는 [랜딩 페이지의 URL 핸들을](#step-1-verify-your-url-handle) 사용하여 자동으로 리퀴드 태그를 생성합니다. 다음 표를 참조하여 태그를 생성하세요:

|**개인화 유형|** **랜딩 페이지를** 선택합니다.|**랜딩 페이지|** [이전에 만든](#prerequisites) 랜딩 페이지를 선택합니다.} {: .reset-td-br-1 .reset-td-br-2 role="프레젠테이션" }

Liquid 태그를 메시지에 추가하려면 **삽입을** 선택하거나 스니펫을 클립보드에 복사하여 수동으로 추가할 수 있습니다.

\![선택한 랜딩 페이지에 대해 자동 생성된 리퀴드 태그입니다.\]({% image\_buster /assets/img/랜딩\_페이지/get-snippet.png %}){:: style="max-width:40%;"}

스니펫은 다음과 유사합니다:

{원시 %} ```루비 {% 랜딩_페이지_URL 내-사용자 지정 URL 핸들 %} ``` {% endraw %}

### 3단계: 메시지 마무리 및 전송

Liquid 스니펫을 메시지에 삽입한 다음 나머지 메시지를 마무리합니다. 준비가 되면 랜딩 페이지를 통해 사용자 추적을 시작하라는 메시지를 보낼 수 있습니다.
