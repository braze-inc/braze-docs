---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "이 참조 문서에서는 모바일 고객을 유치하고 리타겟팅하는 데 사용되는 성과 마케팅 플랫폼인 Jampp와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/)는 모바일 고객을 확보하고 리타겟팅하는 데 사용되는 성과 마케팅 플랫폼입니다. Jampp는 행동 데이터를 예측 및 프로그래매틱 기술과 결합하여 소비자의 최초 구매 또는 더 빈번한 구매를 촉진하는 개인적이고 관련성 있는 광고를 보여줌으로써 광고주 측에서 매출을 창출합니다.

_This integration is maintained by Jampp._

## 통합 정보

Braze와 Jampp 통합을 통해 Braze 사용자는 Braze 웹훅 이벤트를 통해 이벤트를 Jampp에 동기화할 수 있습니다. 그 결과, 고객은 모바일 광고 생태계 내에서 리타겟팅 이니셔티브에 더 풍부한 데이터 세트를 추가할 수 있습니다.

광고로 고객을 리타겟하고 싶은 몇 가지 예제:
- 고객의 이메일 또는 푸시 구독 상태가 변경될 때.
- 고객이 Braze 메시징 캠페인과 상호 작용한 방법.
- 고객이 특정 지오펜스를 트리거한 경우.

## 필수 조건

이 통합은 iOS 및 Android 앱을 지원합니다.

| 요구 사항 | 설명 |
|---|---|
| Jampp 계정 | 이 파트너십을 활용하려면 [Jampp 계정](https://www.jampp.com/)이 필요합니다. |
| Android 앱 ID | Android용 고유 Braze 애플리케이션 식별자(예: "com.example"). |
| iOS 앱 ID | iOS용 고유 Braze 애플리케이션 식별자(예: "012345678"). |
| Braze SDK에서 IDFA 수집 활성화 | IDFA 수집은 Braze SDK 내에서 선택 사항이며 기본적으로 비활성화되어 있습니다. | 
| 커스텀 속성을 통한 Google 광고 ID 수집 | Google 광고 ID 수집은 고객에게 선택 사항이며 [커스텀 속성][5]으로 수집할 수 있습니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

### 1단계: Braze에서 웹훅 템플릿 만들기

향후 캠페인 또는 캔버스에서 사용할 Jampp 웹훅 템플릿을 만들려면 Braze 플랫폼에서 **템플릿** > **웹훅 템플릿**으로 이동하십시오.

새 캠페인을 만들 때 Braze에서 **웹훅**을 선택하여 일회성 Jampp 웹훅 캠페인을 만들거나 기존 템플릿을 사용할 수 있습니다.

새 웹훅 템플릿에서 다음 필드를 작성하세요:
- **요청 본문**: 원시 텍스트
- **웹훅 URL**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

웹훅 URL에서 다음을 수행해야 합니다:
- 이벤트 이름을 설정하십시오. 이 이름은 Jampp 대시보드에 표시됩니다.
- Android용 앱의 고유한 애플리케이션 식별자(예: 'com.example') 및 iOS용 앱의 고유한 애플리케이션 식별자(예: '012345678')를 전달합니다.
- 적절한 커스텀 속성에 대해 추적 중인 Google 광고 ID로 [Liquid][1]을 삽입하십시오. Google 광고 ID는 이 예제에서 `aaid`로 나열되지만, 개발자가 설정한 커스텀 속성 이름으로 바꿔야 합니다.

![Braze 웹훅 빌더에 표시된 웹훅 URL 및 메시지 미리보기.][2]

{% alert important %}
Braze는 디바이스 IDFA/AAID를 자동으로 수집하지 않으므로 이러한 값은 사용자가 직접 저장해야 합니다. 이 데이터를 수집하려면 사용자 동의가 필요할 수 있습니다.
{% endalert %}

#### 요청 헤더 및 메서드

Jampp 웹훅에는 HTTP 메서드와 요청 헤더가 필요합니다.

- **HTTP 메서드**: GET
- **요청 헤더**:
  - **Content-Type**: application/json

![Braze 웹훅 빌더에 표시되는 요청 헤더, HTTP 메서드 및 메시지 미리보기.][3]

#### 요청 본문

이 웹훅에 대한 요청 본문은 정의할 필요가 없습니다.

### 2단계: 요청 미리보기

메시지를 미리 보고 요청이 다른 사용자에게 맞게 렌더링되는지 확인합니다. Android 및 iOS 사용자 모두에 대한 테스트 요청을 미리 보고 전송하는 것이 좋습니다. 요청이 성공하면 API는 `HTTP 204` 로 응답합니다.

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid
[2]: {% image_buster /assets/img/jampp_webhook.png %}
[3]: {% image_buster /assets/img/jampp_method.png %}
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
