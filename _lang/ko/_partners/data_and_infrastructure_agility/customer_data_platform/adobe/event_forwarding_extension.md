---
nav_title: 이벤트 전달 확장
article_title: Adobe
description: "이 참조 문서에서는 Adobe Experience Platform Edge 네트워크에서 캡처한 데이터를 활용하여 서버 측 이벤트의 형태로 Braze로 전송할 수 있는 Braze 이벤트 전달 확장을 다룹니다."
page_type: partner
page_order: 2
search_tag: Partner

---

# 이벤트 추적 API 이벤트 전달 확장 기능

> Braze 이벤트 추적 API [이벤트 전달](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) 확장을 통해 Adobe Experience Platform Edge 네트워크에서 캡처한 데이터를 활용하고 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) API를 사용하여 서버 측 이벤트의 형태로 Braze로 전송할 수 있습니다.

이 문서에서는 확장의 사용 사례, 이벤트 전달 라이브러리에 확장을 설치하는 방법, 이벤트 전달 [규칙](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)에서 확장 기능을 사용하는 방법을 다룹니다.

{% alert note %}
속성을 Braze로 전송하면 Braze 데이터 포인트 소비가 증가할 수 있습니다. 속성을 보내기 전에 Braze 계정 관리자와 상담하세요. 자세한 내용은 [청구 가능한 데이터 포인트]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points)에 대한 Braze 설명서를 참조하세요.
{% endalert %}

## 사용 사례

이 확장은 Braze의 엣지 네트워크 데이터를 사용하여 고객 분석 및 타겟팅 기능을 활용해야 합니다.

예를 들어, 멀티채널(웹사이트 및 모바일)을 운영하고 웹사이트 및 모바일 플랫폼에서 거래 또는 대화 입력을 이벤트 데이터로 캡처하는 소매 조직을 생각해 보겠습니다. 

이 데이터는 다양한 [태그](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en) 규칙을 사용하여 실시간으로 엣지 네트워크로 전송됩니다. 여기에서 Braze 이벤트 전달 확장은 관련 이벤트를 서버 측에서 Braze로 자동 전송합니다.

## 요금 제한

| API | 요금 한도 |
| --- | --- |
| 사용자 추적 | 분당 50,000건의 요청.<br><br>자세한 내용은 [사용자 추적 API 설명서를]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit) 참조하세요.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 필요한 구성 세부 정보 수집

엣지 네트워크를 Braze에 연결하려면 다음이 필요합니다.

| 키 유형 | 설명 |
| --- | --- |
| 브레이즈 인스턴스 | 귀하의 Braze 인스턴스는 Braze 온보딩 매니저에게서 얻을 수 있거나 [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints)에서 찾을 수 있습니다. |
| Braze REST API 키 | 모든 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 2단계: 비밀 만들기

새 [이벤트 전달 비밀번호를](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) 생성하고 값을 [Braze API 키로](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details) 설정합니다. 이 값은 계정에 대한 연결을 인증하는 동시에 값을 안전하게 유지하는 데 사용됩니다.

### 3단계: Braze 확장 프로그램 설치 및 구성

1. 확장을 설치하려면 [이벤트 전달 속성정보를 생성](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties)하거나 기존 속성정보를 선택하여 대신 편집합니다.
2. 다음으로 왼쪽 탐색에서 **확장** 프로그램을 선택합니다. **카탈로그** 탭의 Braze 확장 카드에서 **설치**를 선택합니다.
3. 다음 화면에서 REST 인스턴스와 API 키를 입력하고 완료되면 **저장**을 선택합니다.

### 4단계: 이벤트 전송 규칙 생성

확장을 설치한 후 새 이벤트 전달 [규칙](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)을 생성하고 원하는 대로 조건을 구성합니다. 규칙에 대한 작업을 구성할 때 **Braze** 확장을 선택한 다음 작업 유형으로 **이벤트 보내기를** 선택합니다.

![][1]

{% tabs 로컬 %}
{% tab 사용자 식별 %}

| 입력 | 설명 |
| --- | --- |
| 외부 사용자 ID | 길고 무작위이며 잘 분산된 UUID 또는 GUID입니다. 사용자 아이디의 이름을 다른 방법으로 지정하는 경우에도 길고 무작위이며 잘 분산된 이름을 사용해야 합니다. [제안된 사용자 ID 명명 규칙]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention)에 대해 자세히 알아보세요. |
| Braze 사용자 ID | Braze 사용자 식별자. |
| 사용자 별칭 | 별칭은 대체 고유 사용자 식별자 역할을 합니다. 별칭을 사용하여 핵심 사용자 ID와 다른 차원에서 사용자를 식별할 수 있습니다.<br><br>사용자 별칭 객체는 식별자 자체에 대한 `alias_name` 및 별칭 유형을 나타내는 `alias_label` 등 두 부분으로 구성됩니다. 사용자는 레이블이 다른 여러 개의 별칭을 가질 수 있지만 `alias_label`당 `alias_name` 하나만 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
이벤트를 사용자에게 연결하려면 `External User ID` 필드, `Braze User Identifier` 필드 또는 `User Alias` 섹션을 입력해야 합니다.
{% endalert %}

{% endtab %}
{% tab 이벤트 데이터 %}

| 입력 | 설명 | 필수 |
| --- | --- | --- |
| 이벤트 이름 | 이벤트 이름. | 예 |
| 이벤트 시간 | ISO 8601 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 문자열 형식의 날짜-시간. | 예 |
| 앱 식별자 | 앱 식별자 또는 `app_id`는 활동을 워크스페이스의 특정 앱과 연결하는 매개변수입니다. 워크스페이스 내에서 상호 작용하고 있는 앱을 지정합니다. | 아니요 |
| 이벤트 등록정보 | 이벤트의 사용자 지정 속성이 포함된 JSON 객체입니다. | 아니요 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
**Braze 이벤트 전송** 작업에서는 **이벤트 이름** 및 **이벤트 시간**만 지정하면 되지만, 커스텀 속성정보 필드에 가능한 한 많은 정보를 포함해야 합니다. 자세한 내용은 [이벤트 객체를]({{site.baseurl}}/api/objects_filters/event_object/) 참조하세요.
{% endalert %}

{% endtab %}
{% tab 사용자 속성 %}

사용자 속성은 지정된 사용자 프로필에 제공된 이름과 값으로 속성을 만들거나 업데이트하는 필드가 포함된 JSON 객체일 수 있습니다. 지원되는 속성은 다음과 같습니다:

| 사용자 속성 | 설명 |
| --- | --- |
| 이름 | 사용자의 이름. |
| 성 | 사용자의 성(이름). |
| 전화 | 사용자의 전화번호입니다. |
| 이메일 | 사용자의 이메일 주소입니다. |
| 성별 | 다음 문자열 중 하나입니다: 'M', 'F', 'O'(기타), 'N'(해당 없음), 'P'(말하지 않음). |
| 도시 | 사용자의 도시입니다. |
| 국가 | [ISO-3166-1 알파-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 형식의 문자열로 사용자 국가를 입력합니다. |
| 언어 | [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 형식의 문자열로 된 사용자 언어입니다. |
| 생년월일 | 사용자의 생년월일 데이터는 "YYYY-MM-DD" 형식의 문자열입니다(예: 1980-12-21). |
| 시간대 | [IANA 표준 시간대](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) 데이터베이스의 표준 시간대 이름(예: 'America/New_York' 또는 '동부 표준시(미국 및 캐나다)'). |
| Facebook | `id`(문자열), `likes`(문자열 배열), `num_friends`(정수) 중 하나를 포함하는 해시입니다. |
| Twitter | id(정수), `screen_name`(문자열, X(이전의 트위터) 핸들), `followers_count`(정수), `friends_count`(정수), `statuses_count`(정수) 중 하나를 포함하는 해시. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
구성 내 추가된 모든 속성은 속성 값의 변경 여부에 관계없이 이벤트가 Braze로 전송될 때마다 전송됩니다. 사용자 속성을 구성할 때 데이터 포인트 소비에 어떤 영향을 미치는지 파악해야 합니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 5단계: 구매 이벤트 보내기 규칙 만들기

확장을 설치한 후 새 이벤트 전달 [규칙](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)을 생성하고 원하는 대로 조건을 구성합니다. 규칙에 대한 작업을 구성할 때 **Braze** 확장을 선택한 다음 작업 유형으로 **구매 이벤트 보내기를** 선택합니다.

![][3]

{% tabs 로컬 %}
{% tab 사용자 식별 %}

| 입력 | 설명 |
| --- | --- |
| 외부 사용자 ID | 길고 무작위이며 잘 분산된 UUID 또는 GUID입니다. 사용자 아이디의 이름을 다른 방법으로 지정하는 경우에도 길고 무작위이며 잘 분산된 이름을 사용해야 합니다. [제안된 사용자 ID 명명 규칙]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention)에 대해 자세히 알아보세요. |
| Braze 사용자 ID | Braze 사용자 식별자. |
| 사용자 별칭 | 별칭은 대체 고유 사용자 식별자 역할을 합니다. 별칭을 사용하여 핵심 사용자 ID와 다른 차원에서 사용자를 식별할 수 있습니다.<br><br>사용자 별칭 객체는 식별자 자체에 대한 `alias_name` 및 별칭 유형을 나타내는 `alias_label` 등 두 부분으로 구성됩니다. 사용자는 레이블이 다른 여러 개의 별칭을 가질 수 있지만 `alias_label`당 `alias_name` 하나만 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
이벤트를 사용자에게 연결하려면 `External User ID` 필드, `Braze User Identifier` 필드 또는 `User Alias` 섹션을 입력해야 합니다.
{% endalert %}

{% endtab %}
{% tab 구매 데이터 %}

| 입력 | 설명 | 필수 |
| --- | --- | --- |
| 제품 ID | 구매 식별자. (예: 제품 이름 또는 제품 카테고리) | 예 |
| 구매 시간 | ISO 8601 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 문자열 형식의 날짜-시간. | 예 |
| 통화 | [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) 영숫자 통화 코드 형식의 문자열로 통화를 입력합니다. | 예 |
| 가격 | 개체의 가격입니다. | 예 |
| 수량 | 구매한 수량입니다. 제공하지 않으면 기본값은 1이 됩니다. 최대값은 100보다 작아야 합니다. | 아니요 |
| 앱 식별자 | 앱 식별자 또는 `app_id`는 활동을 워크스페이스의 특정 앱과 연결하는 매개변수입니다. 워크스페이스 내에서 상호 작용하고 있는 앱을 지정합니다. | 아니요 |
| 구매 등록정보 | 구매의 사용자 지정 속성이 포함된 JSON 객체입니다. | 아니요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
**구매 이벤트 전송** 작업에서는 , `Product ID`, `Purchase Time`, `Currency`, `Price`만 지정하면 되지만, 구매 속성정보 필드에 가능한 한 많은 정보를 포함해야 합니다. 자세한 내용은 [구매 개체를]({{site.baseurl}}/api/objects_filters/purchase_object/) 참조하세요.
{% endalert %}

{% endtab %}
{% tab 사용자 속성 %}

구성 보기에서 각 이벤트와 함께 속성을 전송할지 여부를 선택할 수 있습니다.

사용자 속성은 지정된 사용자 프로필에 제공된 이름과 값으로 속성을 만들거나 업데이트하는 필드가 포함된 JSON 객체일 수 있습니다. 지원되는 속성은 다음과 같습니다:

| 사용자 속성 | 설명 |
| --- | --- |
| 이름 | 사용자의 이름. |
| 성 | 사용자의 성(이름). |
| 전화 | 사용자의 전화번호입니다. |
| 이메일 | 사용자의 이메일 주소입니다. |
| 성별 | 다음 문자열 중 하나입니다: 'M', 'F', 'O'(기타), 'N'(해당 없음), 'P'(말하지 않음). |
| 도시 | 사용자의 도시입니다. |
| 국가 | [ISO-3166-1 알파-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) 형식의 문자열로 사용자 국가를 입력합니다. |
| 언어 | [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) 형식의 문자열로 된 사용자 언어입니다. |
| 생년월일 | 사용자의 생년월일 데이터는 "YYYY-MM-DD" 형식의 문자열입니다(예: 1980-12-21). |
| 시간대 | [IANA 표준 시간대](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) 데이터베이스의 표준 시간대 이름(예: 'America/New_York' 또는 '동부 표준시(미국 및 캐나다)'). |
| Facebook | `id`(문자열), `likes`(문자열 배열), `num_friends`(정수) 중 하나를 포함하는 해시입니다. |
| Twitter | id(정수), `screen_name`(문자열, X(이전의 트위터) 핸들), `followers_count`(정수), `friends_count`(정수), `statuses_count`(정수) 중 하나를 포함하는 해시. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
구성 내 추가된 모든 속성은 속성 값의 변경 여부에 관계없이 이벤트가 Braze로 전송될 때마다 전송됩니다. 사용자 속성을 구성할 때 데이터 포인트 소비에 어떤 영향을 미치는지 파악해야 합니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 6단계: Braze 내에서 데이터 검증

이벤트 수집과 Adobe Experience Platform 통합이 성공적으로 완료되면 [고객 프로필을 조회]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)할 때 Braze 콘솔에 이벤트가 표시됩니다. 특히, Braze로 전송된 새로운 이벤트 데이터는 특정 사용자의 [개요 탭의]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab) **구매** 또는 **사용자 지정 이벤트** 섹션에 반영됩니다.

[1]: {% image_buster /assets/img/efe.png %}
[3]: {% image_buster /assets/img/efe2.png %}