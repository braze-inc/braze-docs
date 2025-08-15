---
nav_title: 링크 단축
article_title: 링크 단축
page_order: 5
description: "이 참고 문서에서는 SMS 메시지에서 링크 단축을 켜는 방법과 자주 묻는 질문에 대해 설명합니다."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# 링크 단축

> 이 페이지에서는 SMS 메시지에서 링크 단축을 켜고, 단축 링크를 테스트하고, 단축 링크에 사용자 지정 도메인을 사용하는 방법 등에 대해 설명합니다.

링크 단축 및 클릭 추적을 사용하면 SMS 메시지에 포함된 URL을 자동으로 단축하고 클릭률 분석을 수집하여 사용자가 SMS 캠페인에 어떻게 참여하는지 파악하는 데 도움이 되는 추가 참여 지표를 제공할 수 있습니다.

링크 단축 및 클릭 추적은 캠페인과 캔버스 모두에서 [메시지 변형 수준에서]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) 설정할 수 있습니다. 

URL의 길이는 켜져 있는 추적 유형에 따라 결정됩니다:
- **기본 추적**은 캠페인 수준의 클릭 추적을 가능하게 합니다. 정적 URL의 길이는 20자, 동적 URL의 길이는 25자입니다.
- **고급 추적을** 통해 캠페인 수준 및 사용자 수준의 클릭 추적이 가능합니다. Clicks will also generate an [SMS click event]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) sent through Currents. 고급 추적 기능이 있는 정적 URL의 길이는 27~28자로, URL을 클릭한 사용자 세그먼트를 생성할 수 있습니다. 동적 URL의 경우 32~33자의 길이를 갖습니다.

링크는 공유 쇼트 도메인(`brz.ai`)을 사용하여 단축됩니다. 예시 URL은 `https://brz.ai/8jshX`(기본, 정적) 또는 `https://brz.ai/8jshX/2dj8d`(고급, 동적)와 같이 보일 수 있습니다. 자세한 내용은 [테스트](#testing)를 참조하세요.

`http://` 또는 `https://` 로 시작하는 모든 정적 URL은 단축됩니다. 정적 단축 URL은 생성된 날로부터 1년간 유효합니다. Liquid 맞춤 설정이 포함된 단축 URL은 2개월 동안 유효합니다.

{% alert note %}
<sup>BrazeAITM</sup> [지능형 채널 필터를]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) 사용하고 SMS 채널을 선택할 수 있도록 하려면 고급 추적 및 [클릭 추적을]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking) 통해 SMS 링크 단축을 사용 설정하세요.
{% endalert %}

## 링크 단축 사용

링크 단축을 사용하려면 메시지 작성기의 링크 단축 토글이 켜져 있는지 확인하세요. 그런 다음 기본 또는 고급 추적 중 하나를 선택합니다.

![링크 단축을 위한 토글이 있는 메시지 작성기.][1]

Braze는 `http://` 또는 `https://` 로 시작하는 URL만 인식합니다. URL이 인식되면 **미리 보기** 섹션이 자리 표시자 URL로 업데이트됩니다. Braze는 단축 후 URL의 길이를 추정하지만, 보다 정확한 추정을 위해 테스트 사용자를 선택하고 메시지를 초안으로 저장하라는 경고 메시지가 표시됩니다.

![메시지 작성기에서 '메시지' 상자에 긴 URL을 입력하고 미리 보기에 단축 링크를 생성합니다.][3]

### UTM 매개변수 추가

{% multi_lang_include click_tracking.md section='UTM parameters' %}

## URL의 유동적 개인화

Braze 컴포저 내에서 직접 URL을 동적으로 구성하여 URL에 동적 UTM 매개변수를 추가하거나 사용자에게 고유한 링크를 보낼 수 있습니다(예: 사용자가 버린 장바구니로 이동하거나 재고가 있는 특정 제품으로 이동하는 등).

### 지원되는 Liquid 개인화 태그를 사용하여 URL 만들기

URL은 [지원되는 모든 Liquid 개인화 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)를 사용하여 동적으로 생성할 수 있습니다.

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

또한 사용자 정의 리퀴드 변수의 단축을 지원합니다. 몇 가지 예가 아래에 나와 있습니다.

### Liquid 변수를 사용하여 URL 만들기

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Liquid 변수에 의해 렌더링되는 URL 단축

Liquid에서 렌더링하는 URL은 API 트리거 프로퍼티에 포함된 URL도 단축합니다. 예를 들어 {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}이 유효한 URL을 나타내는 경우, SMS 메시지를 발송하기 전에 해당 URL을 단축하여 추적합니다. 

### 메시징/보내기 엔드포인트에서 URL 단축하기

링크 단축은 [`/messages/send` 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) 통한 API 전용 메시지에 대해서도 사용 설정되어 있습니다. 기본 또는 고급 추적을 사용 설정하려면 `link_shortening_enabled` 또는 `user_click_tracking_enabled` 요청 매개변수를 사용하세요.

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| 선택 사항 | 부울 | 링크 단축 및 캠페인 수준 클릭 추적을 사용하려면 `link_shortening_enabled` 을 `true` 으로 설정합니다. 추적을 사용하려면 `campaign_id` 및 `message_variation_id` 주소가 있어야 합니다.|
|`user_click_tracking_enabled`| 선택 사항 | 부울 | `user_click_tracking_enabled`를 `true`로 설정하여 링크 단축, 캠페인 수준 및 사용자 수준 클릭 추적을 사용 설정합니다. 추적된 데이터를 사용하여 URL을 클릭한 사용자 세그먼트를 만들 수 있습니다.<br><br> 이 매개 변수를 사용하려면 `link_shortening_enabled` 는 `true` 여야 하며 `campaign_id` 및 `message_variation_id` 이 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

요청 매개변수의 전체 목록을 보려면 [요청 매개변수로]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters) 이동하세요.

## 테스트

캠페인이나 Canvas를 시작하기 전에 먼저 메시지를 미리 보고 테스트하는 것이 가장 좋습니다. 이렇게 하려면 **테스트** 탭으로 이동하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) 또는 개별 사용자에게 미리 보고 SMS를 보냅니다. 

이 미리보기는 관련 개인화 및 단축 URL로 업데이트됩니다. 렌더링된 개인화 및 단축된 URL을 반영하여 문자 수와 [청구 가능한 세그먼트도]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) 업데이트됩니다. 

테스트 메시지를 보내기 전에 캠페인 또는 캔버스를 저장하여 메시지에 전송될 단축 URL의 표시를 받아보세요. 테스트 전송 전에 캠페인 또는 캔버스가 저장되지 않은 경우, 테스트 전송에는 플레이스홀더 URL이 포함됩니다.

{% alert important %}
활성 캔버스 내에서 초안을 만들면 단축 URL이 생성되지 않습니다. 실제 단축 URL은 캔버스 초안이 활성화되면 생성됩니다.
{% endalert %}

![메시지 "테스트" 탭에 테스트 수신자를 선택할 수 있는 필드가 있습니다.][2]

{% alert note %}
사용자를 선택한 후 **테스트** 탭에서 리퀴드 개인화 및 단축 URL이 템플릿으로 제공됩니다. 정확한 문자 수를 받으려면 사용자가 선택되어 있는지 확인하세요.
{% endalert %}

## 클릭 추적

링크 단축이 켜져 있으면 SMS 및 MMS 실적 표에 이형 상품별 클릭 이벤트 수와 관련 클릭률을 표시하는 **총 클릭** 수라는 열이 포함됩니다. SMS 측정기준에 대한 자세한 내용은 [SMS 메시지 성능]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance)을 참조하세요.

![SMS 및 MMS 성능 지표 표입니다.][4]

**과거 실적** 및 **SMS/MMS 실적** 차트에는 **총 클릭 수** 옵션도 포함되어 있으며 클릭 이벤트의 일일 시계열을 표시합니다. 클릭 수는 리디렉션 시(예: 사용자가 링크를 방문할 때) 증가하며, 사용자당 한 번 이상 증가될 수 있습니다.

## 사용자 리타겟팅

리타겟팅에 대한 안내는 [SMS 리타겟팅을]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links) 참조하세요.

{% multi_lang_include click_tracking.md section='Custom Domains' %}

{% multi_lang_include click_tracking.md section='Frequently Asked Questions' %}

### 어떤 개별 사용자가 URL을 클릭하는지 알 수 있나요?

예. **고급 추적이** 켜져 있는 경우, [SMS 리타겟팅 필터]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) 또는 커런츠에서 전송한 SMS 클릭 이벤트(`users.messages.sms.ShortLinkClick`)를 활용하여 URL을 클릭한 사용자를 리타겟팅할 수 있습니다.

### 링크 단축은 딥링크 또는 유니버설 링크에서 작동하나요?

링크 단축은 딥링크에서는 작동하지 않습니다. Branch나 앱스플라이어와 같은 제공업체의 유니버설 링크를 단축할 수는 있지만, 이 과정에서 발생할 수 있는 문제(어트리뷰션이 깨지거나 리디렉션이 발생하는 등의 문제)는 Braze가 해결해드릴 수 없습니다.

[1]: {% image_buster /assets/img/link_shortening/shortening1.png %}
[2]: {% image_buster /assets/img/link_shortening/shortening2.png %}
[3]: {% image_buster /assets/img/link_shortening/shortening3.png %}
[4]: {% image_buster /assets/img/link_shortening/shortening4.png %}
[5]: {% image_buster /assets/img/sms/retargeting5.png %}
[6]: {% image_buster /assets/img/sms/retargeting4.png %}
[7]: {% image_buster /assets/img/custom_domain.png %}
[8]: {% image_buster /assets/img/custom_domain2.png %}
[11]: {% image_buster /assets/img/sms/link_shortening10.png %}
[13]: {% image_buster /assets/img/link_shortening/shortening3.png %}   

