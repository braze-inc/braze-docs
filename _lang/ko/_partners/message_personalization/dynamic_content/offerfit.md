---
nav_title: "OfferFit"
article_title: OfferFit
alias: /partners/offerfit/
description: "OfferFit은 수동 A/B 테스트를 인공지능 테스트로 대체합니다. 라이프사이클 마케터는 오퍼핏의 AI 테스트를 사용하여 각 고객에게 가장 적합한 1:1 결정을 내리고, 모든 변수를 동시에 테스트하며, 시장 변화를 감지하고 적응할 수 있습니다."
page_type: partner
search_tag: OfferFit

---


# OfferFit

> [OfferFit](https://www.offerfit.ai/)은 수동 A/B 테스트를 인공지능 테스트로 대체합니다. 라이프사이클 마케터는 오퍼핏의 AI 테스트를 사용하여 각 고객에게 가장 적합한 1:1 결정을 내리고, 모든 변수를 동시에 테스트하며, 시장 변화를 감지하고 적응할 수 있습니다.

OfferFit과 Braze의 통합을 통해 고객 데이터를 기반으로 모든 고객에게 적합한 메시지, 채널, 타이밍을 자동으로 찾아낼 수 있습니다. 교차 판매, 상향 판매, 재구매, 유지, 갱신, 추천, 윈백과 같은 비즈니스 목표에 따라 기존에 식별된 고객을 대상으로 캠페인을 최적화할 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
|-------------|-------------|
| OfferFit 라이선스 | 이 파트너십을 활용하려면 활성 OfferFit 라이선스가 필요합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키입니다: {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.create</code></li><li><code>templates.update</code></li><li><code>templates.info</code></li><li><code>templates.list</code></li></ul>{:/} 이는 Braze 대시보드의 **설정** > **API 키에서** 생성할 수 있습니다. |
| Braze REST API 엔드포인트 | [REST API 엔드포인트 URL][1]. 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **개발자 콘솔** > **API 설정**에서 API 키를 생성할 수 있습니다.
{% endalert %}

### Braze REST API 엔드포인트

OfferFit 라이선스 및 사용 사례에 따라 사용하는 Braze REST API 엔드포인트가 결정됩니다. 다음은 사용할 수 있는 다양한 API 엔드포인트입니다.

| Braze REST API 엔드포인트 | OfferFit 사용 |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | 캠페인 또는 캔버스에서 타겟팅할 고객 목록을 검색합니다. OfferFit은 PII 데이터를 허용하지 않으므로 `fields_to_export` 속성은 플랫폼 사용자와 함께 동의한 데이터 속성만 검색하는 데 사용됩니다. |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | 특정 세그먼트에 속한 모든 사용자를 검색합니다. OfferFit은 PII 데이터를 허용하지 않으므로 `fields_to_export` 속성은 플랫폼 사용자와 함께 동의한 PII 이외 필드만 검색하는 데 사용됩니다. |
| [POST /users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | 오퍼핏은 이 엔드포인트를 사용하여 메시징을 개인화하는 데 사용할 수 있는 사용자 지정 데이터 속성으로 사용자 프로필을 업데이트할 수 있습니다.                                                                                                                                            |
| [POST /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Braze에서 API 캠페인을 트리거합니다. |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | API 트리거 전달을 위해 구성된 캠페인에 대한 전송을 트리거합니다. |
| [GET /campaigns/list]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Braze에 구성된 모든 캠페인 목록과 관련 메타데이터를 검색합니다. |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | 특정 Braze 캠페인의 애널리틱스 데이터를 검색합니다. |
| [GET /campaigns/details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | 특정 Braze 캠페인의 세부 정보를 검색합니다. |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | API 트리거 전달을 위해 구성된 캔버스에 대한 전송을 트리거합니다. |
| [GET /canvas/list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Braze에 구성된 모든 캔버스 목록과 관련 메타데이터를 검색합니다. |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | 특정 캔버스의 분석 데이터를 검색합니다. |
| [GET /canvas/details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | 특정 캔버스의 세부 정보를 검색합니다. |
| [GET /segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Braze에 구성된 모든 세그먼트 목록과 관련 메타데이터를 검색합니다. |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Braze 세그먼트의 크기를 검색합니다. |
| [GET /segments/details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | 특정 Braze 세그먼트의 세부 정보를 검색합니다. |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | 새 Braze HTML 이메일 템플릿을 만듭니다. |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | 기존 Braze HTML 이메일 템플릿을 업데이트합니다. |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | 특정 Braze HTML 이메일 템플릿의 세부 정보를 검색합니다. |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Braze에 구성된 모든 Braze HTML 이메일 템플릿 목록과 `subject line` 및 `HTML content`를 검색합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

[OfferFit을 통합](#integration)한 후에는 다음을 수행하여 실험 프로세스를 자동화할 수 있습니다.

1. 매출, 전환, ARPU 등 극대화할 **성공 측정기준**을 선택합니다
고객 데이터에서 측정할 수 있는 KPI. OfferFit이 인공지능을 통해 극대화하고자 하는 측정기준입니다.
2. 테스트할 **차원**(예: 오퍼, 제목란, 크리에이티브, 채널, 시간, 요일, 빈도 등)을 선택합니다.
3. 각 차원에 사용할 수 있는 **옵션을** 선택합니다. 예를 들어 채널 차원에서 이메일, SMS, 푸시를 선택한 다음 빈도 차원에서 매일, 주 2회, 매주를 선택할 수 있습니다.

![OF_USE_CASE_EXAMPLE][2]


실험 프로세스가 자동화되면 OfferFit은 선택한 성공 측정기준을 극대화하는 것을 목표로 각 고객에 대한 일일 추천을 생성하기 시작합니다. 

오퍼핏 AI는 모든 고객 상호 작용을 통해 학습하고 이러한 인사이트를 다음날 추천에 적용합니다.


| 사용 사례 | 목표 | 사전 접근 방식 | OfferFit 접근 방식 |
|----------|------|----------------|-------------------|
| **교차 판매 또는 상향 판매** | 인터넷 구독에서 사용자당 평균 수익(ARPU)을 극대화하세요. | 모든 고객에게 차상위 티어 요금제를 제공하는 연간 캠페인을 실행합니다. | 각 고객에게 가장 적합한 메시지, 전송 시간, 할인, 요금제를 경험적으로 발견하여 급진적 오퍼에 민감한 고객, 업그레이드를 위해 할인이나 기타 인센티브가 필요한 고객을 파악합니다. |
| **갱신 및 유지** | 계약 기간과 순현재가치(NPV)를 모두 극대화하여 계약 갱신을 보장합니다. | 수동으로 A/B 테스트를 수행하고, 갱신을 보장하기 위해 상당한 할인을 제공합니다. | 자동화된 실험을 통해 각 고객에게 가장 적합한 갱신 제안을 찾고, 가격에 덜 민감하고 갱신 시 큰 할인이 필요하지 않은 고객을 파악하세요. |
| **반복 구매** | 구매 및 재구매율을 극대화하세요. | 모든 고객은 웹사이트 계정을 만든 후 동일한 여정(예: 동일한 이메일 시퀀스 등)을 수신합니다. | 실험을 자동화하여 각 고객에게 가장 적합한 메뉴 항목과 가장 효과적인 제목란, 전송 시간, 커뮤니케이션 빈도를 찾습니다. |
| **윈백** | 과거 가입자의 재가입을 유도하여 재활성화를 늘립니다. | 정교한 A/B 테스트 및 세분화. | 자동화된 실험을 활용하여 수천 개의 변수를 한 번에 테스트하여 각 개인에게 가장 적합한 크리에이티브, 메시지, 채널 및 케이던스를 발견하세요. |
| **추천** | 기존 고객의 비즈니스 신용카드 추천을 통해 신규 계좌 개설을 극대화하세요. | 광범위한 A/B 테스트를 통해 모든 고객에 대한 고정된 이메일 시퀀스를 사용하여 고객 집단에 가장 적합한 전송 시간, 주기 등을 결정합니다. | 실험을 자동화하여 특정 고객에게 제공할 이상적인 이메일, 크리에이티브, 전송 시간, 신용카드를 결정합니다. |
| **리드 육성 및 전환** | 매출 증대를 유도하고 각 고객에게 적절한 금액을 지불하세요. | Facebook 및 기타 플랫폼의 개인정보 보호정책이 변경됨에 따라 개인 맞춤형 유료 광고에 대한 이전의 접근 방식은 더 이상 유효하지 않습니다. | 강력한 퍼스트파티 데이터를 활용하여 고객 세그먼트, 입찰 방법, 입찰 수준 및 크리에이티브를 자동으로 실험합니다. |
| **로열티 및 인게이지먼트** | 고객 로열티 프로그램 신규 등록자의 구매를 극대화합니다. | 고객은 자신의 행동에 대한 응답으로 정해진 시퀀스의 고정된 이메일을 수신합니다. 예를 들어 로열티 프로그램의 새로운 모든 등록자는 동일한 여정을 수신합니다. | 다양한 이메일 오퍼, 크리에이티브, 전송 시간, 빈도를 자동으로 실험하여 각 고객의 구매 및 재구매를 극대화합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## 통합

### 1단계: Braze에서 타겟 오디언스 정의

Braze에서 세그먼트를 하나 이상 생성하여 타겟 오디언스를 정의합니다. 이 세그먼트는 캠페인 또는 캔버스를 적합한 사용자에게 보내는 데 사용됩니다.

### 2단계: API로 트리거되는 Braze 캠페인 또는 캔버스를 구성하고 캠페인 자산(예: HTML 템플릿, 이미지) 생성 {#step-2}

1. Braze에서 캠페인 또는 캔버스를 만듭니다. 오퍼핏은 이 캠페인 또는 캔버스를 사용하여 정의된 오디언스 중 적합한 사용자에게 1:1 맞춤 활성화 이벤트를 전송합니다. 
2. 캠페인이나 캔버스에 Braze [대조군]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)을 포함하지 마세요. 이렇게 하면 오퍼핏 컨트롤 그룹이 유일하게 활성화된 그룹이 될 수 있습니다.
3. 규모에 따라 크리에이티브 콘텐츠에 Liquid 태그를 구성하여 캠페인이나 캔버스에 오퍼핏 추천을 동적으로 채울 수 있습니다. OfferFit은 Braze API를 통해 템플릿의 Liquid 태그에 고객별 콘텐츠를 전달합니다.

### 3단계: 오퍼핏 사용 사례 구성을 업데이트하여 Braze 활성화 이벤트를 오케스트레이션하세요.

OfferFit의 Braze와 기본 활성화 통합 기능을 활용하여 타겟 오디언스를 위한 1:1 개인화된 추천을 오케스트레이션하고 예약할 수 있습니다.

## 사용자 지정

OfferFit은 Braze에서 활성화 이벤트를 오케스트레이션하는 것 외에도 사용 가능한 API 엔드포인트를 통해 Braze에서 고객 프로필(비PII) 및 인게이지먼트 데이터를 검색할 수 있는 데이터 통합 기능을 제공합니다.

## 이 통합 사용

OfferFit을 구성한 후 자동화된 실험 플랫폼에서 타겟 오디언스의 각 사용자에 대해 1:1 개인화된 활성화 이벤트를 Braze에 자동으로 전송합니다. 이러한 활성화 이벤트는 [2단계](#step-2)에서 구성한 Braze 캠페인 또는 캔버스를 통해 트리거됩니다.

브라즈에서 제공되는 분석 데이터 외에도, 오퍼핏은 마케터가 오퍼핏의 자가 학습 AI 기능을 통해 발견한 고객 인사이트를 탐색할 수 있는 포괄적인 리포팅 레이어를 제공합니다.




[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}

