---
nav_title: 웹훅 만들기
article_title: 웹훅 만들기
page_order: 1
channel:
  - webhooks
description: "이 참조 문서에서는 웹훅 캠페인을 만들고 구성하는 방법에 대해 설명합니다."
search_rank: 2
---

# 웹훅 캠페인 만들기

> 웹훅 캠페인을 만들거나 멀티채널 캠페인에 웹훅을 포함하면 다른 시스템과 애플리케이션에 실시간 정보를 제공하여 앱 이외의 동작을 트리거할 수 있습니다. 

웹훅을 사용하여 Salesforce 또는 Marketo와 같은 시스템이나 백엔드 시스템으로 정보를 보낼 수 있습니다. 예를 들어 고객이 특정 횟수만큼 커스텀 이벤트를 수행한 후 고객의 계정에 프로모션 크레딧을 적립하고 싶을 수 있습니다.

{% alert tip %}
계속 진행하기 전에 웹훅의 정의와 Braze에서 웹훅을 사용하는 방법에 대해 자세히 알아보려면 [웹훅 소개를]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) 참조하세요.
{% endalert %}

## 1단계: 메시지 구축 위치 선택하기

메시지를 캠페인으로 보내야 할지 캔버스로 보내야 할지 잘 모르시겠어요? 캠페인은 단일의 간단한 메시징 캠페인에 적합하며, 캔버스는 여러 단계의 사용자 여정에 적합합니다.

{% tabs %}
{% tab Campaign %}

**단계:**

1. **메시징** > **캠페인으로** 이동하여 **캠페인 만들기를** 선택합니다.
2. **웹훅을** 선택하거나 여러 채널을 타겟팅하는 캠페인의 경우 **멀티채널을** 선택합니다.
3. 캠페인 이름을 명확하고 의미 있는 것으로 정하세요.
4. (선택 사항) 이 캠페인의 사용 방법을 설명하는 설명을 추가합니다.
4. 필요에 따라 [팀과]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [태그를]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) 추가합니다.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 구축할 수 있습니다. 예를 들어 [보고서 빌더를]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 사용할 때 특정 태그를 기준으로 필터링할 수 있습니다.
5. 캠페인에 필요한 만큼 배리언트를 추가하고 이름을 지정하세요. 추가된 각 배리언트에 대해 서로 다른 웹훅 템플릿을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 참조하세요.

{% alert tip %}
캠페인의 모든 메시지가 비슷하거나 콘텐츠가 동일한 경우 배리언트를 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사를** 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**단계:**

1. 캔버스 작성기를 사용하여 캔버스를 [만듭니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
2. 캔버스를 설정한 후 캔버스 빌더에서 단계를 추가합니다. 단계에 명확하고 의미 있는 이름을 붙이세요.
3. [단계 일정을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) 선택하고 필요에 따라 지연을 지정합니다.
4. 필요에 따라 이 단계의 오디언스를 필터링합니다. 세그먼트를 지정하고 필터를 추가하여 이 단계의 수신자를 더욱 세분화할 수 있습니다. 오디언스 옵션은 메시징이 전송되는 시점에 지연이 발생한 후에 확인됩니다.
5. [진행 방식을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) 선택하세요.
6. 메시지와 페어링할 다른 메시징 채널을 선택합니다.

{% endtab %}
{% endtabs %}

## 2단계: 웹훅 구축하기

웹훅을 처음부터 새로 만들거나 기존 템플릿을 사용하거나 기존 템플릿 중 하나를 사용할 수 있습니다. 그런 다음 편집기의 **작성** 탭에서 웹훅을 구축합니다.

**작성** 탭은 다음 필드로 구성됩니다:

- 언어
- 웹훅 URL
- HTTP 메서드
- 요청 본문

웹훅 템플릿 예시가 있는 '작성' 탭입니다.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### 언어 {#internationalization}

URL과 요청 본문에서 [국제화가]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) 지원됩니다. 메시지를 국제화하려면 **언어 추가를** 선택하고 필수 입력란을 채우세요. 

콘텐츠를 작성하기 전에 언어를 선택하여 Liquid에서 원하는 위치에 텍스트를 채울 수 있도록 하는 것이 좋습니다. 사용 가능한 전체 언어 목록은 [지원되는 언어를]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported) 참조하세요.

오른쪽에서 왼쪽으로 쓰이는 언어로 문구를 추가하는 경우, 오른쪽에서 왼쪽으로 쓰이는 메시징의 최종 모양은 서비스 제공업체의 렌더링 방식에 따라 크게 달라질 수 있습니다. 최대한 정확하게 오른쪽에서 왼쪽으로 표시되는 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 메시지 만들기를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) 참조하세요.

#### 웹훅 URL

웹훅 URL 또는 HTTP URL은 엔드포인트를 지정합니다. 엔드포인트는 웹훅에서 캡처하는 정보를 전송하는 곳입니다. 

공급업체에 정보를 보내려면 공급업체가 API 설명서에 이 URL을 제공해야 합니다. 자체 시스템으로 정보를 전송하는 경우 개발자 또는 엔지니어링 팀에 문의하여 올바른 URL을 사용하고 있는지 확인하세요. 

Braze는 표준 포트 `80` (HTTP) 및 `443` (HTTPS)를 통해 통신하는 URL만 허용합니다.

##### Liquid 사용

[Liquid를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 사용하여 웹훅 URL을 개인화할 수 있습니다. 특정 엔드포인트에서는 사용자를 식별하거나 URL의 일부로 사용자별 정보를 제공해야 하는 경우가 있습니다. Liquid를 사용할 때는 URL에 사용하는 각 사용자별 정보에 대한 [기본값을]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) 포함해야 합니다.

#### HTTP 메서드

정보를 전송하는 엔드포인트에 따라 사용해야 하는 [HTTP 방식이]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) 달라집니다. 대부분의 경우 POST를 사용합니다.

#### 요청 본문

요청 본문은 지정한 URL로 전송될 정보입니다. 웹훅 요청의 본문은 JSON 키-값 페어 또는 원시 텍스트로 작성할 수 있습니다.

##### JSON 키-값 페어

JSON 키-값 페어를 사용하면 JSON 형식을 기대하는 엔드포인트에 대한 요청을 쉽게 작성할 수 있습니다. JSON 요청을 기대하는 엔드포인트에서만 사용할 수 있습니다. 예를 들어 키가 `message_body` 인 경우 해당 값은 `Your order just arrived!` 일 수 있습니다. 키-값 페어를 입력하면 작성기가 JSON 구문으로 요청을 구성하고 JSON 요청의 미리보기가 자동으로 채워집니다.

!!! 요청 본문이 JSON 키-값 페어로 설정되었습니다.]({% image_buster /assets/img/webhook_json_1.png %})

요청에 사용자 속성, [커스텀 속성]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices) 또는 [이벤트 속성정보를]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 포함하는 등 Liquid를 사용하여 키-값 페어를 개인화할 수 있습니다. 예를 들어 요청에 고객의 이름과 이메일을 포함할 수 있습니다. 각 속성에 대한 [기본값을]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) 포함해야 합니다.

##### 원시 텍스트

원시 텍스트 옵션을 사용하면 모든 형식의 본문을 예상하는 엔드포인트에 대한 요청을 유연하게 작성할 수 있습니다. 예를 들어, 요청이 XML 형식일 것으로 예상되는 엔드포인트에 대한 요청을 작성하는 데 이 기능을 사용할 수 있습니다. 

Liquid를 사용한 [개인화]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) 및 [국제화는]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) 모두 원시 텍스트에서 지원됩니다.

Liquid를 사용한 원시 텍스트가 포함된 요청 본문 예시입니다.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

`Content-Type` [요청 헤더를](#request-headers-optional) `application/x-www-form-url-encoded` 으로 설정한 경우 요청 본문은 URL 인코딩 문자열로 형식화해야 합니다. 예를 들어

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

!!! URL 인코딩 문자열이 포함된 요청 본문.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## 3단계: 추가 설정 구성

#### 요청 헤더(선택 사항)

특정 엔드포인트에서는 요청에 헤더를 포함해야 할 수도 있습니다. 작성기의 **작성** 섹션에서 필요한 만큼 헤더를 추가할 수 있습니다.

'권한 부여' 키와 '콘텐츠 유형' 키에 대한 요청 헤더 예시.]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

일반적인 요청 헤더는 `Content-Type` 사양(본문에서 예상되는 데이터 유형(예: XML 또는 JSON)을 설명)과 공급업체 또는 시스템에 대한 자격 증명을 포함하는 권한 부여 헤더입니다. 

콘텐츠 유형 사양은 `Content-Type` 키를 사용해야 합니다. 일반적인 값은 `application/json` 또는 `application/x-www-form-urlencoded` 입니다.

인증 헤더는 `Authorization` 키를 사용해야 합니다. 일반적인 값은 {% raw %} `Bearer {{YOUR_TOKEN}}` 또는 `Basic {{YOUR_TOKEN}}` {% endraw %} 이며, `YOUR_TOKEN` 은 공급업체 또는 시스템에서 제공한 자격 증명입니다.

## 4단계: 메시지 테스트 보내기

캠페인을 시작하기 전에 웹훅을 테스트하여 요청 형식이 제대로 지정되었는지 확인하는 것이 좋습니다.

**테스트** 탭으로 전환하여 테스트 웹훅을 전송합니다. 웹훅을 무작위 사용자, 특정 사용자(외부 사용자 ID의 이메일 주소 입력) 또는 원하는 속성을 가진 커스텀 사용자로 테스트할 수 있습니다.  

테스트 웹훅을 보내면 응답 메시지와 함께 대화 상자가 나타납니다. 웹훅 요청이 실패한 경우 오류 메시지를 참조하여 웹훅 문제 해결에 대한 도움을 받으세요. 다음 예제에서는 잘못된 웹훅 URL을 사용한 웹훅의 응답에 대해 자세히 설명합니다.

```json
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

## 5단계: 나머지 캠페인 또는 캔버스 구축하기

{% tabs %}
{% tab Campaign %}

그런 다음 나머지 캠페인을 구축합니다. 도구를 사용하여 웹훅을 구축하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

#### 전달 일정 또는 트리거 선택

웹훅은 예약된 시간, 동작 또는 API 트리거를 기반으로 전달될 수 있습니다. 자세한 내용은 [캠페인 예약하기를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) 참조하세요.

실행 기반 전달의 경우 캠페인 기간과 조용한 시간을 설정할 수도 있습니다.

이 단계에서는 사용자가 캠페인을 [다시]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) 수신할 수 있도록 허용하거나 [최대 게재빈도]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 설정 규칙을 인에이블하는 등 전달 제어를 지정할 수도 있습니다.

#### 타겟팅할 사용자 선택하기

다음으로 세그먼트 또는 필터를 선택하여 오디언스 범위를 좁혀 [사용자를 타겟팅해야]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) 합니다. 이 단계에서는 세그먼트에서 더 큰 오디언스를 선택하고, 원하는 경우 필터를 사용하여 해당 세그먼트를 더 좁힐 수 있습니다. 현재 대략적인 세그먼트 인구가 어떻게 보이는지 자동으로 미리 볼 수 있습니다. 정확한 세그먼트 멤버십은 항상 메시지 전송 직전에 계산된다는 점에 유의하세요.

{% multi_lang_include target_audiences.md %}

#### 전환 이벤트 선택하기

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 액션, [전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 전환이 카운트되는 기간을 최대 30일로 설정할 수 있습니다.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면 캔버스 단계의 나머지 섹션을 완료하세요. 나머지 캔버스를 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 캔버스 설명서의 캔버스 [구축]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) 단계를 참조하세요.

{% endtab %}
{% endtabs %}

## 6단계: 검토 및 배포

캠페인 또는 캔버스의 마지막 구축을 완료한 후에는 세부 사항을 검토하고 테스트한 다음 전송하세요!

## 알아두어야 할 사항

### 오류, 재시도 로직 및 시간 초과

웹훅은 외부 엔드포인트에 요청을 보내는 Braze 서버에 의존하므로 오류가 가끔 발생할 수 있습니다. 가장 일반적인 오류로는 구문 오류, 만료된 API 키, 요금 제한, 예기치 않은 서버 측 문제 등이 있습니다. 웹훅 캠페인을 보내기 전에:

- 웹훅에 구문 오류가 있는지 테스트하기
- 개인화된 변수에 기본값이 있는지 확인합니다.

웹훅이 전송에 실패하면 [메시지 활동 로그에]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) 오류 메시지가 기록되며 오류 타임스탬프, 앱 이름, 오류에 대한 세부 정보 등이 포함됩니다.

!"현재 사용자에 대한 정보를 쿼리하려면 활성 액세스 토큰을 사용해야 합니다"라는 메시지가 표시되는 웹훅 오류가 발생했습니다.]({% image_buster /assets/img_archive/webhook-error.png %})

오류 메시지에 오류의 원인이 명확하지 않은 경우 사용 중인 API 엔드포인트의 설명서를 확인해야 합니다. 여기에는 일반적으로 엔드포인트에서 사용하는 오류 코드와 일반적으로 발생하는 원인에 대한 설명이 제공됩니다.

#### 응답 코드 및 재시도 로직

웹훅 요청이 전송되면 수신 서버는 요청에 어떤 일이 발생했는지를 나타내는 응답 코드를 반환합니다. 다음 표에는 서버가 보낼 수 있는 다양한 응답, 이러한 응답이 캠페인 분석에 미치는 영향, 오류 발생 시 Braze가 캠페인을 재전송할지 여부가 요약되어 있습니다:

| 응답 코드 | 수신됨으로 표시되었나요? | 재시도? |
|---------------|-----------|----------|
| `20x` (성공)  | 예 |   N/A  |
| `30x` (리디렉션)  | 아니요 | 아니요 |
| `408` (요청 시간 초과)  | 아니요 | 예 |
| `429` (요금 제한)  | 아니요 | 예 |
| `Other 4XX` (클라이언트 오류)  | 아니요 | 아니요 |
| `5XX` (서버 오류)   | 아니요 | 예 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Braze는 지수 백오프를 사용하여 30분 이내에 위의 상태 코드를 최대 5회까지 재시도합니다. 엔드포인트에 연결할 수 없는 경우 24시간 동안 재시도가 분산될 수 있습니다.<br><br>각 웹훅은 시간 초과되기 90초 전까지 허용됩니다.
{% endalert %}

#### 문제 해결 및 추가 오류 세부 정보

특정 웹훅 오류 해결에 대한 자세한 설명, 문제 해결 단계 및 지침은 [웹훅 및 연결된 콘텐츠 요청 문제 해결을]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/) 참조하세요. 또한, 비정상 호스트 감지 시스템의 작동 방식과 자동화된 이메일 및 추가 로그인을 통해 오류 알림을 제공하는 Braze 커런츠에 대한 자세한 설명도 확인할 수 있습니다.

### IP 허용 목록 {#ip-allowlisting}

Braze에서 웹훅이 전송되면, Braze 서버는 고객 또는 타사 서버에 네트워크 요청을 보냅니다. IP 허용 목록을 사용하면 웹훅 요청이 Braze에서 오는지 확인할 수 있어 보안을 한층 강화할 수 있습니다.

Braze는 다음 IP에서 웹훅을 전송합니다. 나열된 IP는 허용 목록에 옵트인한 모든 API 키에 자동으로 동적으로 추가됩니다.

{% alert important %}
Braze 간 웹훅을 만들고 허용 목록을 사용하는 경우 `127.0.0.1` 을 포함하여 다음 IP를 모두 허용 목록에 추가해야 합니다.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='ips' %}

### Braze 파트너와 웹훅 사용하기 {#utilizing-webhooks}

웹훅을 사용하는 방법에는 여러 가지가 있으며, 기술 파트너(Alloys)와 함께 웹훅을 사용하여 고객 및 사용자와 직접 커뮤니케이션 수준을 높일 수 있습니다.

확인해보세요:
* [메신저]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)
* 그리고 더 많은 [기술 파트너가]({{site.baseurl}}/partners/home/) 있습니다!


