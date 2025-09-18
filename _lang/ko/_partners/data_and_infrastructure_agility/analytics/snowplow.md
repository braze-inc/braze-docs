---
nav_title: Snowplow
article_title: Snowplow
description: "이 참조 문서에서는 Google Tag Manager 서버 측 태그 지정을 통해 Snowplow 이벤트를 Braze에 전달할 수 있는 오픈소스 데이터 수집 플랫폼인 Snowplow와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow][1]는 풍부한 고품질의 지연 시간이 짧은 데이터 수집을 위한 확장 가능한 오픈 소스 플랫폼입니다. 엔터프라이즈 비즈니스를 위한 고품질의 완전한 행동 데이터를 수집하도록 설계되었습니다.

_This integration is maintained by Snowplow._

## 통합 정보

Braze와 Snowplow의 통합을 통해 사용자는 Google Tag Manager 서버 측 태그 지정을 통해 Snowplow 이벤트를 Braze에 전달할 수 있습니다. Snowplow Braze 태그를 사용하면 추가적인 유연성과 제어 기능을 제공하면서 이벤트를 Braze로 보낼 수 있습니다.
- 데이터의 모든 변환에 대한 완전한 가시성 확보
- 시간이 지남에 따라 정교함을 발전시키는 능력
- 모든 데이터는 전달을 선택할 때까지 개인 클라우드에 남아 있음
- 풍부한 태그 라이브러리와 친숙한 Google 태그 관리자 UI로 설정이 간편합니다.

Snowplow의 풍부한 행동 데이터를 활용하여 Braze에서 강력한 고객 중심 상호작용을 유도하고 실시간으로 개인화된 메시지를 전달하세요.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Snowplow 파이프라인 | Snowplow 파이프라인이 가동 및 실행 중이어야 합니다. |
| Google Tag Manager 서버 측 | GTM-SS를 배포하고 [GTM-SS용 스노우플로우 클라이언트를][2] 설정해야 합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][3]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

### 개인화된 실행 기반 전달
Snowplow에서 기본적으로 수집하는 많은 리치 이벤트 중 하나를 사용하거나 커스텀 이벤트를 정의하여 비즈니스에 적합한 더욱 세분화된 고객 여정을 구성할 수 있습니다. Snowplow의 풍부한 행동 데이터를 활용하여 고객 퍼널을 설계하고 마케팅 및 제품 팀의 가치를 창출하여 Braze를 통해 전환율과 제품 사용을 극대화할 수 있습니다.

### 동적 세분화
Snowplow의 고품질 행동 데이터를 기반으로 Braze에서 동적 오디언스를 생성합니다. 사용자가 제품, 앱 또는 웹사이트에서 작업을 수행하면, Snowplow가 수집하는 실시간 행동 데이터를 활용하여 Braze의 관련 세그먼트에서 사용자를 자동으로 추가하거나 제거할 수 있습니다.

## 통합

### 1단계: 템플릿 설치

#### 수동 설치

1. 템플릿 파일을 다운로드하세요. [`template.tpl`][7] 템플릿 파일을 다운로드합니다.
2. Google 태그 관리자 서버 컨테이너의 **템플릿** 섹션에서 새 태그를 만듭니다.
3. 오른쪽 상단의 **추가 작업** 메뉴를 클릭하고 **가져오기를** 선택합니다.
4. 다운로드한 템플릿 파일을 가져와서 저장합니다.

#### Tag Manager 갤러리

곧 출시됩니다! 이 태그는 GTM 갤러리에 포함하기 위해 승인 대기 중입니다.

### 2단계: 브레이즈 태그 설정

템플릿을 설치한 후 GTM-SS 컨테이너에 Braze 태그를 추가합니다.

1. **태그** 탭에서 **새로** 만들기를 선택한 다음 **브레이즈 태그를** 태그 구성으로 선택합니다.
2. Braze에 전달할 이벤트에 대해 원하는 트리거를 선택합니다.
3. 필요한 매개변수를 입력하고 태그를 구성합니다(자세한 내용은 다음 사용자 지정 섹션에서 확인할 수 있습니다).
4. **저장**을 클릭합니다.

## 사용자 지정

### 필수 태그 매개변수

다음 표에는 Braze 태그 설정에 포함해야 하는 필수 태그 매개변수가 나와 있습니다.

| 매개변수 | 설명 |
| --------- | ----------- |
| Braze REST API 엔드포인트 | 이를 Braze REST [엔드포인트][3]의 URL로 설정합니다. |
| Braze API 키 | 이를 각 요청에 포함할 Braze [API 키][4]로 설정합니다. |
| Braze `external_id` | 이 키를 사용자의 `external_id` 에 해당하는 클라이언트 이벤트 속성으로 설정하면 [Braze 사용자 식별자로][5] 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 이벤트 매핑

다음 표에는 [Snowplow 클라이언트][2]가 클레임하는 Snowplow 이벤트와 관련된 이벤트 매핑 옵션이 나와 있습니다.

| 매핑 옵션 | 설명 |
| --------- | ----------- |
| 자기 설명 이벤트 포함 | 기본적으로 켜져 있습니다. Braze로 전송되는 이벤트의 속성정보 오브젝트에 Snowplow 자체 설명 이벤트 데이터를 포함할지 여부를 나타냅니다. |
| 제설기 이벤트 컨텍스트 규칙 | Braze 태그가 Snowplow 이벤트에 연결된 컨텍스트 엔티티를 사용하는 방법을 설명합니다. |
| 단일 요소인 경우 배열에서 엔티티 추출 | 동일한 엔티티를 여러 개 이벤트에 연결할 수 있으므로 Snowplow 엔티티는 항상 배열로 구성됩니다. 이 옵션은 배열에 단일 요소만 포함된 경우 배열에서 단일 요소를 선택합니다. |
| 이벤트 객체에 모든 엔티티 포함 | 기본적으로 켜져 있습니다. Braze 이벤트의 속성정보 오브젝트에 있는 이벤트의 모든 엔티티를 포함합니다. 포함할 개별 엔티티를 선택하려면 이 옵션을 비활성화합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 고급 이벤트 매핑

#### 이벤트 속성 규칙

클라이언트 이벤트의 다른 속성을 포함시키고 이를 Braze 이벤트에 매핑하려면 다음 표의 규칙을 참조하세요: 

| 이벤트 속성 규칙 | 설명 |
| --------- | ----------- |
| 공통 이벤트 속성 포함 | 이 옵션은 기본적으로 활성화됩니다. 이 옵션은 [공통 이벤트 정의][6]의 이벤트 속성정보를 Braze 이벤트의 속성정보에 자동으로 포함할지 여부를 설정합니다. |
| 추가 사용자 속성 및 이벤트 속성 매핑 규칙 | 클라이언트 이벤트의 속성 키와 이를 매핑하려는 속성의 개체 키를 지정합니다(또는 동일한 이름을 유지하려면 매핑된 키를 비워 두세요). 여기서 키 경로 표기법을 사용하거나(예: Snowplow 이벤트 플랫폼의 경우 `x-sp-tp2.p`, Snowplow 이벤트 페이지 보기 ID의 경우 `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id`(배열 인덱스: 0)) 대체 클라이언트를 사용하는 경우 Snowplow 이외의 속성정보를 선택할 수 있습니다.<br><br>이벤트 속성 매핑 규칙은 Braze 이벤트 속성 개체를 채웁니다.|
| 공통 사용자 속성 포함| 이 옵션은 기본적으로 활성화됩니다. 이 옵션은 공통 이벤트 정의의 `user_data` 속성정보를 Braze 사용자 속성 오브젝트에 포함할지 여부를 설정합니다.|
| 이벤트 시간 속성 | 이 옵션을 사용하면 클라이언트 이벤트 속성정보를 지정하여 이벤트 시간(ISO-8601 형식)을 채우거나 비워 두어 현재 시간을 사용할 수 있습니다(기본 동작). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 엔티티 매핑

Snowplow 엔티티 매핑 표를 사용하여 엔티티를 Braze에서 다른 이름을 사용하도록 다시 매핑하고 이벤트 속성정보 또는 사용자 속성 오브젝트에 포함시킬 수 있습니다. 

엔티티는 두 가지 형식으로 지정할 수 있습니다:
- 주요 버전 일치: `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1`. 여기서 `com_snowplowanalytics_snowplow`는 이벤트 공급업체, `web_page`는 스키마 이름, `1`은 주요 버전 번호입니다. 원하는 경우 `x-sp-`를 생략할 수도 있습니다.
- 전체 스키마 일치: `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| 엔티티 매핑 옵션 | 설명 |
| --------- | ----------- |
| 이벤트에 매핑되지 않은 엔티티 포함 | 이전 사용자 지정으로 일부 엔티티를 사용자 속성으로 다시 매핑하거나 이동할 때 이 옵션을 사용하면 매핑되지 않은 모든 엔티티(예: [이벤트 속성정보 규칙](#event-property-rules)에서 찾을 수 없는 엔티티)가 Braze 이벤트의 속성정보 오브젝트에 포함되도록 할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


[1]: https://snowplowanalytics.com
[2]: https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[5]: {{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation
[6]: https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data
[7]: https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl
