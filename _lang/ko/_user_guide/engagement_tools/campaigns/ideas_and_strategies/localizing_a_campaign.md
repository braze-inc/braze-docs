---
nav_title: 현지화
page_order: 3
page_type: reference
description: "이 문서에서는 캠페인과 캔버스 전반에 걸쳐 다양한 오케스트레이션 접근 방식의 이점을 간략하게 설명하고 사용자가 메시징에서 개인화를 처리할 수 있는 다양한 방법을 나열합니다."
tool:
  - Campaigns
  - Canvas

---

# 현지화

> Braze는 SDK를 통합한 후 사용자 기기에서 로캘 정보를 자동으로 수집합니다. 로캘에는 언어와 지역 식별자가 포함되어 있습니다. 이 정보는 **국가** 및 **언어** 아래의 Braze 세분화 도구에서 확인할 수 있습니다.

플랫폼에 따라 로캘이 수신되는 방식에 대한 기술적 세부 사항은 다음 [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) 및 [Android/FireOS](http://developer.android.com/reference/java/util/Locale.html) 리소스를 참조하세요.

여러 국가에 고객을 보유한 기업의 경우, Braze 여정 초기에 현지화를 처리하면 시간과 리소스를 절약할 수 있습니다. 다음 문서에서는 캠페인과 캔버스 전반에 걸쳐 다양한 오케스트레이션 접근 방식의 이점을 나열하고 사용자가 메시징에서 개인화를 처리할 수 있는 다양한 방법을 소개합니다.

- **오케스트레이션 옵션**
  - [캠페인](#campaign) (전체 템플릿 1개와 국가별 템플릿 1개)
  - [캔버스](#canvas) (모두를위한 하나의 여정 대 국가당 하나의 여정)<br><br>
- **개인화 옵션**
  - [수동 입력](#option-1-manual-entry)
  - [콘텐츠 블록](#option-2-content-blocks)
  - [카탈로그](#option-3-catalogs)
  - [현지화 파트너](#option-4-localization-partners)
  - [공개 Google 스프레드시트에서 번역](#option-5-translations-in-a-public-google-sheet)
  - [SheetDB를 통해 Google 스프레드시트를 JSON API로 변환하기](#option-6-google-spreadsheet-into-a-json-api-via-sheetdb)

## 오케스트레이션

### 캠페인

{% tabs local %}
{% tab 모두를 위한 하나의 템플릿 %}

"하나의 템플릿으로 모든 것을 처리하는" 접근 방식에서는 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)를 사용하여 Braze의 단일 템플릿에 현지화를 적용합니다. 전송 후 대시보드에서 집계된 캠페인 분석 정보를 제공합니다. 예를 들어 **국가** 및 **수신된 캠페인** 필터를 결합하여 사용자 지정 세그먼트 퍼널을 사용하여 사용자 수준 참여도를 측정할 수 있습니다.

| 장점 | 고려사항 |
| --- | --- |
| \- 중앙 집중식 접근 방식<br>\- 이메일 작성 시간 단축, 이메일을 여러 번 작성할 필요 없음 | \- 수동 보고서 작성<br>\- 캠페인 보고서에는 국가별 지표가 아닌 집계된 지표가 표시됩니다.<br>\- Liquid가 예상대로 채워지는지 철저히 테스트해야 합니다<br>\- 국가 값을 가져오는 방법이나 설정한 카운티 수에 따라 각 국가를 테스트하는 것이 까다로울 수 있습니다.<br>\- 여러 시간대에 걸쳐 특정 시간대에 전송 예약하기 어려움<br>\- 국가별로 별도의 콘텐츠를 보내려는 경우 사용하기가 더 어렵습니다. |
| \--- | \--- | \--- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 국가당 하나의 템플릿 %}

"국가당 하나의 템플릿" 접근 방식은 템플릿을 여러 전송 로캘로 분리합니다. 전송 후에는 대시보드에서 각 국가별로 전송 분석을 개별적으로 보고하며, 모든 다운스트림 사용자 수준의 [커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) 이벤트도 특정 캠페인에 연결됩니다.

- 템플릿은 유지 관리 및 추적 목적으로 [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) 구현하면 유용합니다.
- Campaigns can inherit the configurations from the same [Braze template]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) and [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (such as [email templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) that contain Liquid).
- 기존 캠페인과 템플릿을 [복제하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/) 가치 창출 시간을 단축할 수 있습니다.

| 장점 | 고려사항 |
| --- | --- |
| \- 여러 위치로 확장 가능<br>\- Braze 내 국가별 수익 보고(예: 캠페인별)<br>\- 국가별로 콘텐츠가 크게 다른 경우 유연성 확보 | \- 전략적 구조화 필요<br>\- 더 많은 빌드 노력 필요(예: 국가별 별도 캠페인) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### 캔버스

{% tabs local %}
{% tab 모두를 위한 하나의 여정 %}

"모두를 위한 하나의 여정" 접근 방식에서는 현지화가 [캔버스 여정]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey)과 Liquid 내에서 처리되어 각 사용자에 대한 메시징을 정의합니다. 

캔버스가 전송된 후 대시보드는 집계된 [캔버스 분석]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)을 제공하며, 사용자 수준 인게이지먼트는 [**국가**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) 및 [**수신된 캔버스 단계**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step) 필터를 결합하는 등의 커스텀 [세그먼트 퍼널]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_funnels/)을 통해 측정할 수 있습니다.

| 장점 | 고려사항 |
| --- | --- |
| \- 중앙 집중식 접근 방식<br>\- 이메일 작성 시간 단축 - 이메일을 여러 번 작성할 필요가 없습니다. | \- 수동 보고서 작성<br>\- 캔버스 보고서에는 국가별 지표가 아닌 집계된 지표가 표시됩니다.<br>\- Liquid가 예상대로 채워지는지 철저히 테스트해야 합니다<br>\- 국가 값을 가져오는 방법이나 설정한 카운티 수에 따라 각 국가를 테스트하는 것이 까다로울 수 있습니다.<br>\- 여러 시간대에 걸쳐 특정 시간대에 전송 예약하기 어려움<br>\- 국가별로 별도의 콘텐츠를 보내려는 경우 사용하기가 더 어렵습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 국가당 하나의 여정 %}

In the "one journey per country" approach, the [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) journey builder provides the flexibility of creating user journeys via multiple [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). 이러한 구성 요소는 구성 요소 및 전체 여정 수준에서 [복제]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-canvases)할 수 있습니다.

현지화는 다음 방법을 통해 수행할 수 있습니다:
- 국가별로 캔버스를 분리하여 오디언스 필터를 사용하여 복잡한 사용자 여정을 퍼널 상단에서 정의할 수 있습니다.
- 국가별 맞춤형 사용자 여정, 단일 캔버스에서 각 국가별로 별도의 메시지 스레드를 생성하여 각 여정에 대해 대규모로 사용자를 직관적으로 분류할 수 있는 [오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) 구현

전송된 대시보드는 고객의 현재 위치를 기반으로 국가별 및 사용자 수준별 [커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) 이벤트에 대한 동적 분석을 제공합니다.

| 장점 | 고려사항 |
| --- | --- |
| \- Braze 내 국가별 수익 보고(예: 캔버스, 이형 상품 또는 단계별)<br>\- 국가별로 콘텐츠가 크게 다른 경우 유연성 확보<br>\- 향후 여정의 일부로 다른 채널을 추가할 수 있습니다. | \- 전략적 구조화 필요<br>\- 더 많은 빌드 작업 필요(예: 각 국가별로 별도의 메시지 단계)<br>\- 하나의 캔버스에 국가별로 복잡한 맞춤형 여정을 넣으면 캔버스가 커지고 읽기 어려워질 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## 개인화

### 옵션 1: 수동 입력

수동 입력은 메시지 본문에 콘텐츠를 수동으로 붙여넣고 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/)를 사용하여 수신자에게 올바른 언어를 [조건부]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic)로 표시해야 합니다.

{% raw %}
```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This will go to anyone who does not match the other specified languages!
{% endif %}
```
{% endraw %}

위의 형식을 사용하거나 Braze 대시보드를 통해 이 작업을 수행할 수 있습니다: 
1. 메시지를 작성할 때 **언어** 버튼을 선택하여 선택한 각 언어에 대한 리퀴드 조건부 로직을 생성합니다.
2. 템플릿 텍스트를 메시지에 삽입한 후 각 언어별로 다른 변형을 입력합니다. 서식 지정이 있는 각 필드에 대해 괄호로 묶은 서식 지정 세그먼트 뒤에 변형을 입력해야 합니다. 변형은 그 앞의 괄호 안에 참조된 언어 코드와 일치해야 합니다.
3. 메시지를 보내기 전에 사용자의 ID 또는 이메일을 입력하여 메시지를 테스트하여 언어에 따라 메시지가 개인에게 어떻게 표시되는지 확인합니다. 

{% alert tip %}
항상 메시지에 {% raw %}`{% else %}`{% endraw %} 문구를 포함할 것을 권장합니다. 대부분의 사용자에게는 특정 언어에 대한 메시지가 표시되지만, 텍스트는 해당 언어를 사용하는 사용자에게만 표시됩니다:
- 선택한 언어가 없습니다.
- Braze가 지원하지 않는 언어 사용
- 언어가 감지되지 않는 디바이스를 사용하세요.
{% endalert %}

### 옵션 2: 콘텐츠 블록

Braze [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks)은 재사용 가능한 콘텐츠 블록입니다. 블록이 변경되면 해당 블록에 대한 모든 참조가 변경됩니다. 예를 들어 이메일 헤더 또는 바닥글에 대한 업데이트는 모든 이메일 또는 하우스 번역에 반영됩니다. 이러한 블록은 REST API를 사용하여 [생성]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) 및 [업데이트할]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) 수도 있으며, 사용자가 프로그래밍 방식으로 번역을 업로드할 수도 있습니다. 

대시보드에서 캠페인을 구축할 때 콘텐츠 블록은 {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %} 태그를 사용하여 참조할 수 있습니다. 이러한 블록에는 옵션 1과 같이 각 언어에 대한 조건부 로직에 포함된 모든 번역을 포함하거나 각 언어에 대해 별도의 블록을 사용할 수 있습니다.

콘텐츠 블록은 번역이 필요한 콘텐츠를 콘텐츠 블록 내에 보관하고, 가져오고, 번역한 다음 업데이트하는 번역 관리 프로세스로도 활용할 수 있습니다:
1. 대시보드에서 '번역 필요' 태그를 사용하여 콘텐츠 블록을 수동으로 생성합니다.
2. 서비스는 [`/content_blocks/list` 엔드포인트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)를 사용하여 모든 콘텐츠 블록의 야간 가져오기를 수행합니다.
3. 서비스에서 [`/content_blocks/info` 엔드포인트를]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) 통해 각 콘텐츠 블록에 대한 세부 정보를 가져와 번역할 태그가 지정된 블록을 확인합니다.
4. 번역 서비스는 모든 "번역 필요" 콘텐츠 블록의 본문을 번역합니다.
5. 서비스가 [`/content_block/update` 엔드포인트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)에 도달하여 번역된 콘텐츠를 업데이트하고 태그를 "번역 완료"로 업데이트합니다.

### 옵션 3: 카탈로그

[카탈로그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/)를 사용하면 API 및 CSV 파일을 통해 가져온 JSON 객체의 데이터에 액세스하여 Liquid를 통해 커스텀 속성이나 커스텀 이벤트 속성과 유사하게 메시지를 보강할 수 있습니다. 예를 들어, 다음과 같습니다.

{% tabs local %}
{% tab API %}

다음 API 호출을 통해 카탈로그를 만듭니다:
```json
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```
다음 API 호출을 통해 항목을 추가합니다:
```json
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endtab%}
{% tab CSV %}
다음 형식의 CSV를 만듭니다:

| ID | 컨텍스트 | 언어 | body |
| --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | 안녕하세요 |
| 5 | 2 | en | Hey |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | 안녕하세요 |
| 9 | 3 | en | Hey |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | 안녕하세요 |

{% endtab %}
{% endtabs %}

이러한 카탈로그 항목은 아래 표시된 [개인화]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-catalogs-in-a-message)를 사용하여 참조하거나 데이터 그룹을 만들 수 있는 [선택]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections) 항목을 사용하여 참조할 수 있습니다. 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 

//returns “Hey”
```
{% endraw %}

### 옵션 4: 로캘 추가

[메시지에 로캘]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales)을 추가하고 사용하여 단일 이메일 캠페인 또는 캔버스 내에서 다양한 언어의 사용자를 타겟팅할 수 있습니다. 

{% alert important %}
이 기능은 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}


### 옵션 5: 현지화 파트너

[트랜시펙스와]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) [크라우딘을](https://crowdin.com/) 비롯한 많은 Braze 파트너가 현지화 솔루션을 제공합니다. 일반적으로 사용자는 내부 팀 및 번역 에이전시와 함께 플랫폼을 사용합니다. 그런 다음 이러한 번역을 업로드한 다음 REST API를 통해 액세스할 수 있습니다. 또한 이러한 서비스는 종종 [커넥티드 콘텐츠를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 활용하여 사용자가 API를 통해 번역을 가져올 수 있도록 합니다.

예를 들어, 다음 커넥티드 콘텐츠 호출은 번역을 가져오기 위해 Transifex 및 Crowdin을 호출하고 {% raw %}`{{${language}}}`{% endraw %} 을 활용하여 특정 사용자에 대한 올바른 번역을 식별합니다. 그런 다음 이 번역은 JSON 블록 "문자열"에 저장되고 참조됩니다.

{% tabs local %}
{% tab 트랜시펙스 예시 %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endtab %}
{% tab Crowdin 예시 %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 옵션 6: 공개 Google 스프레드시트에서 번역 

또 다른 번역 옵션으로는 Google 스프레드시트의 주택 번역이 있으며, 번역 에이전시와 협력하여 처리하는 경우가 많습니다. 여기에 저장된 번역은 커넥티드 콘텐츠를 사용하여 쿼리할 수 있습니다. 그러면 사용자의 언어를 기반으로 한 관련 번역이 전송 시 캠페인 본문으로 가져옵니다. 

{% alert note %}
Google 스프레드시트 API는 프로젝트당 100초당 500건의 요청으로 제한되어 있습니다. 연결된 콘텐츠 호출은 캐시할 수 있지만 이 솔루션은 트래픽이 많은 캠페인에는 확장할 수 없습니다.
{% endalert %}

### 옵션 7: SheetDB를 통해 Google 스프레드시트를 JSON API로 변환하기  

이 옵션은 Google 스프레드시트를 연결된 콘텐츠를 통해 쿼리된 JSON 객체로 변환하는 대체 방법을 제공합니다. SheetDB를 통해 스프레드시트를 JSON API로 전환하면 API 호출의 주기에 따라 [여러 구독 티어](https://sheetdb.io/pricing) 중에서 선택할 수 있습니다.

스프레드시트 구조는 옵션 4의 단계를 따르지만 SheetDB는 개체를 쿼리할 수 있는 [추가 필터](https://docs.sheetdb.io/#sheetdb-api)도 제공합니다.

일부 사용자는 대규모 조건부 블록을 구축하는 대신 단일 언어에 대한 결과를 자동으로 반환하는 {% raw %}`{{${language}}}`{% endraw %} Liquid 태그를 기반으로 JSON 개체를 필터링하기 위해 GET 요청 호출에서 SheetDB의 [검색 방법](https://docs.sheetdb.io/#get-search-in-document)을 구현하여 Liquid 및 연결된 블록 종속성이 적은 SheetDB를 구현하는 것을 선호할 수 있습니다.

#### 1단계: Google 시트 서식 지정

먼저, 언어가 서로 다른 개체가 되도록 Google 시트를 작성합니다:

| 언어 | 제목1 | 본문1 | 제목2 | 본문2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| 드 | 안녕하세요 | 4 | 안녕하세요2 | 8 |

#### 2단계: 연결된 콘텐츠 호출에서 언어 Liquid 태그 사용

다음으로, 연결된 콘텐츠 호출 내에 {% raw %}`{{${language}}}`{% endraw %} Liquid 태그를 구현합니다. 스프레드시트를 만들면 SheetDB가 `sheet_id`를 자동으로 생성합니다.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### 3단계: 메시지 템플릿

마지막으로 Liquid를 사용하여 메시지를 템플릿화하세요:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### 고려사항

- {% raw %}`{{${language}}}`{% endraw %} 필드는 모든 사용자에 대해 정의되어야 하며, 그렇지 않으면 언어가 없는 사용자를 위해 Liquid 조건부 블록을 대체 핸들러로 제공해야 합니다.
- Google 스프레드시트 내의 데이터 모델링은 메시지 개체를 사용하는 것과는 다른 언어 중심의 수직적 방식을 따라야 합니다.
- SheetDB는 제한된 무료 계정과 캠페인 전략에 따라 고려해야 하는 여러 가지 유료 옵션을 제공합니다. 
- 연결된 콘텐츠 호출을 캐시할 수 있습니다. API 호출의 예상 케이던스를 측정하고 검색 방법을 사용하는 대신 기본 SheetDB 엔드포인트를 호출하는 대체 접근 방식을 조사하는 것이 좋습니다.