---
nav_title: API 이메일 기본 설정 센터
article_title: API 이메일 기본 설정 센터
page_order: 1
description: "이 문서에서는 API 이메일 환경설정 센터와 이를 커스텀하는 방법에 대해 설명합니다."
channel:
  - email
---

# API 이메일 기본 설정 센터

> 환경설정 센터를 설정하면 사용자가 [이메일 메시징에]({{site.baseurl}}/user_guide/message_building_by_channel/email/) 대한 알림 환경설정을 편집하고 관리할 수 있는 원스톱 상점을 제공합니다. 이 문서에는 API로 생성된 환경설정 센터를 구축하는 단계가 포함되어 있지만 [드래그 앤 드롭 편집기를]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/) 사용하여 환경설정 센터를 구축할 수도 있습니다.

Braze 대시보드에서 **오디언스** > **이메일 기본 설정 센터로** 이동합니다.

여기에서 각 구독 그룹을 관리하고 볼 수 있습니다. 생성하는 각 구독 그룹은 이 환경설정 센터 목록에 추가됩니다. 환경설정 센터를 여러 개 만들 수 있습니다.

{% alert important %}
환경설정 센터는 Braze 이메일 채널 내에서 사용하도록 되어 있습니다. 환경설정 센터 링크는 각 사용자에 따라 동적으로 작동하며 외부에서 호스팅할 수 없습니다.
{% endalert %}

## API를 사용하여 기본 설정 센터 만들기

기본 설정 [센터 Braze 엔드포인트를]({{site.baseurl}}/api/endpoints/preference_center) 사용하면 사용자의 구독 상태 및 구독 그룹 상태를 표시할 수 있는 Braze에서 호스팅하는 웹사이트인 기본 설정 센터를 만들 수 있습니다. 개발자 팀은 HTML과 CSS를 사용하여 페이지의 스타일이 브랜드 가이드라인과 일치하도록 환경설정 센터를 구축할 수 있습니다.

Liquid를 사용하면 구독 그룹의 이름과 각 사용자의 상태를 검색할 수 있습니다. 이렇게 하면 Braze는 페이지가 로드될 때 이 데이터를 저장하고 검색합니다.

### 전제 조건

| 요구 사항 | 설명 |
|---|---|
| 인에이블된 기본 설정 센터 | Braze 대시보드에는 환경설정 센터 기능을 사용할 수 있는 권한이 있습니다. |
| 이메일, SMS 또는 WhatsApp 구독 그룹이 있는 유효한 워크스페이스 | 유효한 사용자 및 이메일, SMS 또는 WhatsApp 구독 그룹이 있는 작업 공간입니다. |
| 유효한 사용자 | 이메일 주소와 외부 ID가 있는 사용자. |
| 환경 설정 센터 권한으로 생성된 API 키 | Braze 대시보드에서 **설정** > **API 키로** 이동하여 환경설정 센터 권한이 있는 API 키에 액세스할 수 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 1단계: 환경 설정 센터 만들기 엔드포인트 사용

기본 설정 [센터 만들기 엔드포인트를]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/) 사용하여 기본 설정 센터 구축을 시작해 보겠습니다. 환경설정 센터를 커스텀하려면 `preference_center_page_html` 필드와 `confirmation_page_html` 필드에 브랜딩과 일치하는 HTML을 포함할 수 있습니다.

[환경설정 센터 URL 생성 엔드포인트를]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) 사용하면 Braze를 통해 전송된 이메일 외부에서 특정 사용자의 환경설정 센터 URL을 가져올 수 있습니다.

### 2단계: 이메일 캠페인에 포함하기

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

이메일에 환경설정 센터 링크를 삽입하려면 탈퇴 URL을 삽입하는 방법과 유사하게 이메일의 원하는 위치에 다음 Liquid 태그를 사용합니다.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Liquid를 포함하는 HTML 조합을 사용할 수도 있습니다. 예를 들어 HTML 편집기 또는 드래그 앤 드롭 편집기에서 다음을 URL로 붙여넣을 수 있습니다. 그러면 모든 이메일 구독 그룹이 자동으로 나열되는 기본 환경설정 센터 레이아웃이 표시됩니다. 

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}">Edit your preferences</a>
```
{%endraw%}

환경설정 센터에는 사용자가 모든 이메일에서 탈퇴할 수 있는 확인란이 있습니다. 테스트 메시지로 전송된 경우에는 이러한 환경설정을 저장할 수 없습니다.

{% alert important %}
위의 Liquid 태그는 캠페인 또는 캔버스를 시작할 때만 작동합니다. 테스트 이메일을 보내도 유효한 링크가 생성되지 않습니다.
{% endalert %}

#### 환경설정 센터 편집하기

환경설정 [센터 업데이트 엔드포인트를]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) 사용하여 환경설정 센터를 편집하고 업데이트할 수 있습니다. 

#### 기본 설정 센터 및 세부 정보 식별자 지정

환경설정 센터를 식별하려면 환경설정 [센터 엔드포인트에 대한 세부정보 보기를]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) 사용하여 마지막으로 업데이트된 타임스탬프, 환경설정 센터 ID 등 관련 정보를 반환하세요.

## 커스터마이징

Braze는 환경설정 센터에서 구독 상태 업데이트를 관리하여 환경설정 센터를 동기화 상태로 유지합니다. 그러나 다음 옵션이 포함된 [구독 그룹 API를]({{site.baseurl}}/api/endpoints/subscription_groups/) 사용하여 자체 환경설정 센터를 만들고 호스팅할 수도 있습니다.

### 옵션 1: 문자열 쿼리 매개변수로 링크하기

URL 본문에 쿼리 문자열 필드-값 쌍을 사용하여 사용자 ID와 이메일 카테고리를 페이지에 전달하면 사용자가 탈퇴를 선택했는지 확인하기만 하면 됩니다. 이 옵션은 사용자 식별자를 해시 형식으로 저장하고 아직 가입 센터가 없는 사용자에게 적합합니다.

이 옵션의 경우 각 이메일 카테고리마다 고유한 수신 거부 링크가 필요합니다:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
또한 Liquid 필터를 사용하여 전송 시점에 사용자의 외부 ID를 해시할 수도 있습니다. 예를 들어 `user_id` 을 MD5 해시 값으로 변환합니다:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### 옵션 2: JSON 웹 토큰으로 인증하기

[JSON 웹 토큰을](https://auth0.com/learn/json-web-tokens/) 사용하여 사용자 이름 및 비밀번호 로그인과 같은 인증 계층 뒤에 있는 웹 서버의 일부(예: 계정 환경설정)에 사용자를 인증할 수 있습니다. 

이 접근 방식은 예를 들어 JSON 웹 토큰의 페이로드에 쿼리 문자열 값 쌍을 전달할 수 있으므로 URL에 쿼리 문자열 값 쌍을 포함할 필요가 없습니다:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

## 자주 묻는 질문

### 환경설정 센터를 만들지 않았습니다. 대시보드에 "PreferenceCenterBrazeDefault"가 표시되는 이유는 무엇인가요?

이는 레거시 Liquid {%raw%}`${preference_center_url}`{%endraw%} 를 사용할 때 환경 설정 센터를 렌더링하는 데 사용되므로 {%raw%}`${preference_center_url}` 또는 `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} 를 참조하는 캔버스 단계나 템플릿은 작동하지 않습니다. 이는 메시징의 일부로 레거시 Liquid 또는 "PreferenceCenterBrazeDefault"가 포함된 이전에 전송된 메시징에도 적용됩니다. 

새 메시지에서 {%raw%}`${preference_center_url}`{%endraw%} 을 다시 참조하면 "PreferenceCenterBrazeDefault"라는 이름의 기본 설정 센터가 다시 만들어집니다.

### 기본 설정 센터는 여러 언어를 지원하나요?

그러나 커스텀 옵트인 및 옵트아웃 페이지의 HTML을 작성할 때 Liquid를 활용할 수 있습니다. 동적 링크를 사용하여 탈퇴를 관리하는 경우 이 링크는 하나의 링크입니다. 

예를 들어 스페인어를 사용하는 사용자의 탈퇴율을 추적하는 경우 별도의 캠페인을 사용하거나 커런츠 관련 분석을 활용해야 합니다(예: 사용자가 구독을 취소하는 시점을 확인하고 해당 사용자가 선호하는 언어를 확인하는 등).

다른 예로 스페인어를 사용하는 사용자의 탈퇴율을 추적하려면 사용자의 언어가 독일어인 경우 `?Spanish=true` 같은 쿼리 파라미터 문자열을 탈퇴 URL에 추가하고 그렇지 않은 경우 일반 탈퇴 링크를 사용할 수 있습니다:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

그런 다음 커런츠를 통해 스페인어를 사용하는 사용자와 해당 탈퇴 링크에 대한 클릭 이벤트 수를 식별할 수 있습니다.

### 탈퇴 링크와 이메일 환경설정 센터 모두 전송에 필요한가요?

아니요. 이메일 캠페인을 작성할 때 "이메일 본문에 탈퇴 링크가 포함되어 있지 않습니다."라는 메시지가 표시되는 경우 콘텐츠 블록에 탈퇴 링크가 있는 경우 이 경고가 표시될 것으로 예상됩니다.
