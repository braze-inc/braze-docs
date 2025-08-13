---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "이 참조 문서에서는 대규모 리타겟팅을 위해 특별히 빌드된 앱인 Remerge와 Braze 간 파트너십을 간략히 설명합니다. 이를 통해 앱 오디언스를 효율적으로 세분화하고 사용자를 리타겟팅할 수 있는 툴을 제공할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/)는 대규모 앱 리타겟팅을 위한 특별히 빌드된 솔루션으로, 효율적인 앱 오디언스 세분화와 사용자 리타겟팅을 위한 다양한 툴을 갖추고 있습니다.

_This integration is maintained by Remerge._

## 통합 정보

Braze와 Remerge의 통합은 모바일 수요 측 플랫폼을 통해 사용자를 리타겟팅할 수 있도록 웹훅 이벤트를 통해 사용자 데이터를 Remerge로 전송함으로써 강력한 크로스채널 생애주기 마케팅 캠페인을 개발할 수 있도록 도와줍니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Remerge 계정 | 이 파트너십을 활용하려면 Remerge 계정이 필요합니다. |
| Remerge 웹훅 키 | 이 키는 Remerge에서 제공합니다. |
| Android 앱 ID | Android용 고유 Braze 애플리케이션 식별자(예: "com.example"). |
| iOS 앱 ID | iOS용 고유 Braze 애플리케이션 식별자(예: "012345678"). |
| Braze SDK에서 IDFA 수집 활성화 | IDFA 수집은 Braze SDK 내에서 선택 사항이며 기본적으로 비활성화되어 있습니다. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Braze 웹훅 템플릿 만들기

향후 캠페인 또는 캔버스를 위한 리머지 웹훅 템플릿을 만들려면 Braze 플랫폼에서 **템플릿** > **웹훅 템플릿으로** 이동하세요. 

일회성 Remerge 웹훅 캠페인을 생성하거나 기존 템플릿을 사용하려면 새 캠페인을 생성할 때 Braze에서 **웹훅**을 선택합니다.

새 웹훅 템플릿에서 다음 필드를 입력합니다:
- **요청 본문**: 원시 텍스트
- **웹훅 URL**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %} 
{% assign android_app_id = 'your_android_app_id' %} 
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

웹훅 URL에 다음을 입력해야 합니다.
- `https://remerge.events/event` API를 사용하여 웹훅 이벤트를 전송하세요.
- 이벤트 이름을 설정합니다. 이 이름은 [remerge.io][65] 대시보드에 표시됩니다.
- Android용 앱의 고유한 애플리케이션 식별자(예: 'com.example') 및 iOS용 앱의 고유한 애플리케이션 식별자(예: '012345678')를 Remerge에 전달합니다.
- 키를 정의합니다. Remerge에서 제공합니다.

![Braze 웹훅 빌더에 표시되는 웹훅 URL 및 메시지 미리보기입니다.][67]

{% alert important %}
Braze는 디바이스 IDFA/AAID를 자동으로 수집하지 않으므로 이러한 값은 사용자가 직접 저장해야 합니다. 이 데이터를 수집하려면 사용자 동의가 필요할 수 있습니다.
{% endalert %}

#### 요청 헤더 및 메서드

Remerge 웹훅에는 HTTP 메서드와 요청 헤더가 필요합니다.

- **HTTP 메서드**: GET
- **요청 헤더**:
  - **Content-Type**: application/json

![Braze 웹훅 빌더에 표시되는 요청 헤더, HTTP 메서드 및 메시지 미리보기.][68]

#### 요청 본문

이 웹훅에 대한 요청 본문은 정의할 필요가 없습니다.

## 2단계: 요청 미리보기

메시지를 미리 보고 요청이 다른 사용자에게 맞게 렌더링되는지 확인합니다. Android 및 iOS 사용자 모두에 대한 테스트 요청을 미리 보고 전송하는 것이 좋습니다. 요청이 성공하면 API는 `HTTP 204` 로 응답합니다.

{% alert important %}
페이지에서 나가기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 만들 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}


[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %}
[68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}
