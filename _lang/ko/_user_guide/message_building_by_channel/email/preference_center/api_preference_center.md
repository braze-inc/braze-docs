---
nav_title: API 이메일 환경설정 센터
article_title: API 이메일 환경설정 센터
page_order: 1
description: "이 문서에서는 API 이메일 환경설정 센터와 이를 커스텀하는 방법에 대해 설명합니다."
channel:
  - email
---

# API 이메일 환경설정 센터

> 환경설정 센터를 설정하면 사용자가 [이메일 메시징]({{site.baseurl}}/user_guide/message_building_by_channel/email/)에 대한 알림 환경설정을 한 곳에서 편집하고 관리할 수 있습니다. 이 문서에서는 API로 생성하는 환경설정 센터를 구축하는 단계를 안내하지만, [드래그 앤 드롭 편집기]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/)를 사용하여 환경설정 센터를 구축할 수도 있습니다.

Braze 대시보드에서 **오디언스** > **이메일 환경설정 센터**로 이동합니다.

여기에서 각 구독 그룹을 관리하고 확인할 수 있습니다. 생성하는 각 구독 그룹은 이 환경설정 센터 목록에 추가됩니다. 여러 개의 환경설정 센터를 만들 수 있습니다.

{% alert important %}
환경설정 센터는 Braze 이메일 채널 내에서 사용하도록 설계되었습니다. 환경설정 센터 링크는 각 사용자에 따라 동적으로 생성되며 외부에서 호스팅할 수 없습니다.
{% endalert %}

## API로 환경설정 센터 만들기

[Preference Center Braze 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center)를 사용하면 사용자의 구독 상태 및 구독 그룹 상태를 표시할 수 있는 Braze 호스팅 웹사이트인 환경설정 센터를 만들 수 있습니다. HTML과 CSS를 사용하여 개발자 팀이 환경설정 센터를 구축하면 페이지 스타일을 브랜드 가이드라인에 맞출 수 있습니다.

Liquid을 사용하면 구독 그룹의 이름과 각 사용자의 상태를 가져올 수 있습니다. 이를 통해 Braze는 페이지가 로드될 때 이 데이터를 저장하고 검색합니다.

### 필수 조건

| 요구 사항 | 설명 |
|---|---|
| 활성화된 환경설정 센터 | Braze 대시보드에 환경설정 센터 기능을 사용할 수 있는 권한이 있어야 합니다. |
| 이메일, SMS 또는 WhatsApp 구독 그룹이 있는 유효한 워크스페이스 | 유효한 사용자와 이메일, SMS 또는 WhatsApp 구독 그룹이 있는 워크스페이스. |
| 유효한 사용자 | 이메일 주소와 외부 ID를 가진 사용자. |
| 환경설정 센터 권한이 있는 API 키 | Braze 대시보드에서 **설정** > **API 키**로 이동하여 환경설정 센터 권한이 있는 API 키에 액세스할 수 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 1단계: 환경설정 센터 생성 엔드포인트 사용

[환경설정 센터 생성 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)를 사용하여 환경설정 센터 구축을 시작해 보겠습니다. 환경설정 센터를 커스텀하려면 `preference_center_page_html` 필드와 `confirmation_page_html` 필드에 브랜딩에 맞는 HTML을 포함할 수 있습니다.

[환경설정 센터 URL 생성 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)를 사용하면 Braze를 통해 발송된 이메일 외부에서 특정 사용자의 환경설정 센터 URL을 가져올 수 있습니다.

### 2단계: 이메일 캠페인에 포함

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

이메일에 환경설정 센터 링크를 삽입하려면, 탈퇴 URL을 삽입하는 방식과 마찬가지로 이메일의 원하는 위치에 다음 Liquid 태그를 사용하세요.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Liquid을 포함하는 HTML을 조합하여 사용할 수도 있습니다. 예를 들어, HTML 편집기나 드래그 앤 드롭 편집기에서 다음을 URL로 붙여넣을 수 있습니다. 이렇게 하면 모든 이메일 구독 그룹을 자동으로 나열하는 기본 환경설정 센터 레이아웃이 표시됩니다. [링크 별칭 지정]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/)을 사용하는 경우, Braze가 추적 매개변수를 추가할 수 있도록 Liquid 태그 뒤에 물음표(`?`)를 추가하세요.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

환경설정 센터에는 사용자가 모든 이메일에서 탈퇴할 수 있는 체크박스가 있습니다. 테스트 메시지로 발송하면 이 환경설정을 저장할 수 없다는 점에 유의하세요.

{% alert important %}
위의 Liquid 태그는 캠페인 또는 캔버스를 시작할 때만 작동합니다. 테스트 이메일을 보내면 유효한 링크가 생성되지 않습니다. 환경설정 센터 링크를 확인하려면 테스트 프로필만 타겟팅하는 캠페인에서 메시지를 시작하세요.
{% endalert %}

#### 환경설정 센터 편집

[환경설정 센터 업데이트 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)를 사용하여 환경설정 센터를 편집하고 업데이트할 수 있습니다. 

#### 환경설정 센터 및 세부 정보 식별

환경설정 센터를 식별하려면 [환경설정 센터 세부 정보 보기 엔드포인트]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)를 사용하여 마지막 업데이트 타임스탬프, 환경설정 센터 ID 등 관련 정보를 반환할 수 있습니다.

## 커스텀

Braze는 환경설정 센터의 구독 상태 업데이트를 관리하여 환경설정 센터를 동기화 상태로 유지합니다. 그러나 다음 옵션과 함께 [구독 그룹 API]({{site.baseurl}}/api/endpoints/subscription_groups/)를 사용하여 자체 환경설정 센터를 만들고 호스팅할 수도 있습니다.

### 옵션 1: 문자열 쿼리 매개변수를 사용한 링크

URL 본문에 쿼리 문자열 필드-값 쌍을 사용하여 사용자의 ID와 이메일 카테고리를 페이지에 전달하면 사용자는 탈퇴 선택을 확인하기만 하면 됩니다. 이 옵션은 사용자 식별자를 해시 형식으로 저장하고 아직 구독 센터가 없는 경우에 적합합니다.

이 옵션의 경우 각 이메일 카테고리에 고유한 탈퇴 링크가 필요합니다:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
발송 시점에 Liquid 필터를 사용하여 사용자의 외부 ID를 해시할 수도 있습니다. 이렇게 하면 `user_id`가 MD5 해시 값으로 변환됩니다. 예를 들어:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### 옵션 2: JSON 웹 토큰으로 인증

[JSON 웹 토큰](https://auth0.com/learn/json-web-tokens/)을 사용하여 웹 서버의 일부(예: 계정 환경설정)에 사용자를 인증할 수 있습니다. 이 영역은 일반적으로 사용자 이름 및 비밀번호 로그인과 같은 인증 계층 뒤에 있습니다. 

이 접근 방식은 URL에 쿼리 문자열 값 쌍을 포함할 필요가 없습니다. 이러한 값들은 JSON 웹 토큰의 페이로드에 전달할 수 있습니다. 예를 들어:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": "offers"
}
```

## 자주 묻는 질문

### 환경설정 센터를 만들지 않았는데 대시보드에 "PreferenceCenterBrazeDefault"가 표시되는 이유는 무엇인가요?

이는 레거시 Liquid {%raw%}`${preference_center_url}`{%endraw%}가 사용될 때 환경설정 센터를 렌더링하는 데 사용됩니다. 즉, {%raw%}`${preference_center_url}` 또는 `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%}를 참조하는 캔버스 단계나 템플릿은 작동하지 않습니다. 이는 레거시 Liquid 또는 "PreferenceCenterBrazeDefault"를 메시지의 일부로 포함한 이전에 발송된 메시지에도 적용됩니다. 

새 메시지에서 {%raw%}`${preference_center_url}`{%endraw%}를 다시 참조하면 "PreferenceCenterBrazeDefault"라는 이름의 환경설정 센터가 다시 생성됩니다.

### 환경설정 센터는 여러 언어를 지원하나요?

아니요. 그러나 커스텀 옵트인 및 옵트아웃 페이지의 HTML을 작성할 때 Liquid을 활용할 수 있습니다. 동적 링크를 사용하여 탈퇴를 관리하는 경우 이는 단일 링크입니다. 

예를 들어 스페인어를 사용하는 사용자의 탈퇴율을 추적하는 경우, 별도의 캠페인을 사용하거나 커런츠 관련 분석을 활용해야 합니다(예: 사용자가 탈퇴하는 시점을 확인하고 해당 사용자의 선호 언어를 확인).

다른 예로, 스페인어를 사용하는 사용자의 탈퇴율을 추적하려면 사용자의 언어가 스페인어인 경우 `?Spanish=true` 같은 쿼리 매개변수 문자열을 탈퇴 URL에 추가하고, 그렇지 않은 경우 일반 탈퇴 링크를 사용할 수 있습니다:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

그런 다음 커런츠를 통해 스페인어를 사용하는 사용자와 해당 탈퇴 링크에 대한 클릭 이벤트 수를 파악할 수 있습니다.

### 탈퇴 링크와 이메일 환경설정 센터가 모두 발송에 필요한가요?

아니요. 이메일 캠페인을 작성할 때 "이메일 본문에 탈퇴 링크가 포함되어 있지 않습니다"라는 메시지가 표시되는 경우, 탈퇴 링크가 콘텐츠 블록에 있으면 이 경고가 표시될 수 있습니다.

### 기본 브라우저 아이콘을 어떻게 업데이트하나요?

기본적으로 브라우저 탭 이름 옆의 아이콘(파비콘)은 Braze 로고를 사용합니다. 커스텀 파비콘을 추가하려면 생성 또는 업데이트 [환경설정 센터 API 호출]({{site.baseurl}}/api/endpoints/preference_center)에서 `links-tags` 속성을 통해 설정합니다. 그러면 Braze가 호스팅된 페이지에 {% raw %}`<link rel="icon" ...>`{% endraw %} 태그를 삽입합니다.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}