---
nav_title: 클릭 추적
article_title: 추적 클릭
page_order: 3
description: "이 참조 문서에서는 WhatsApp 메시지에서 클릭 추적을 켜고, 단축 링크를 테스트하고, 추적 링크에 커스텀 도메인을 사용하는 방법 등에 대해 설명합니다."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# 클릭 추적

> 이 페이지에서는 WhatsApp 메시지에서 클릭 추적을 켜고, 단축 링크를 테스트하고, 추적 링크에 커스텀 도메인을 사용하는 방법 등에 대해 설명합니다.

클릭 추적을 통해 누군가가 WhatsApp 메시징의 링크를 탭하는 시점을 측정하여 어떤 콘텐츠가 참여를 유도하는지 명확하게 파악할 수 있습니다. Braze는 URL을 단축하고, 백그라운드 추적을 추가하며, 클릭 이벤트가 발생하면 이를 기록합니다.

응답 및 템플릿 메시지 모두에서 클릭 추적을 사용 설정할 수 있습니다. 버튼과 본문 텍스트의 링크와 함께 작동하며 개인화된 URL과 커스텀 도메인을 지원합니다. 이 기능을 켜면 WhatsApp 성능/성과 보고서에서 클릭 데이터를 볼 수 있으며, 누가 무엇을 클릭했는지에 따라 사용자를 기반으로 세그먼트화할 수 있습니다.

{% alert note %}
딥링크에서는 클릭 추적이 작동하지 않습니다. Branch 또는 Appsflyer와 같은 제공업체의 유니버설 링크를 단축할 수 있지만, 이 과정에서 발생할 수 있는 문제(기여도가 깨지거나 리디렉션이 발생하는 등)는 Braze가 해결할 수 없습니다.
{% endalert %}

## 작동 방식

### 응답 메시지 

응답 메시지에 대한 클릭 추적을 설정하려면 다음과 같이 하세요:
1. 웹사이트 URL이 포함된 클릭 유도 문안(CTA) 버튼이 포함된 응답 메시지를 작성합니다.
2. 인터페이스에서 지정된 버튼을 클릭하여 클릭 추적을 인에이블먼트합니다.

링크는 Braze 도메인 또는 구독 그룹에 지정된 커스텀 도메인으로 단축되고 사용자에 맞게 개인화됩니다.

`http://` 또는 `https://` 로 시작하는 모든 정적 URL은 단축됩니다. Liquid 개인화(예: 사용자 수준 추적 타겟팅)가 포함된 단축 URL은 2개월 동안 유효합니다.

콘텐츠 본문과 버튼이 있는 WhatsApp 메시지 작성기.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### 템플릿 메시지 

템플릿 메시징의 경우 클릭 추적을 사용하려면 템플릿을 만들 때 기본 URL을 올바르게 제출해야 합니다.

#### 1단계: WhatsApp에서 클릭 추적 지원 템플릿 구축하기

1. WhatsApp 매니저에서 커스텀 도메인 또는 `brz.ai` 으로 기본 URL을 만듭니다.
2. 템플릿에 포함된 링크가 클릭 추적과 호환되는지 확인하세요.
3. Braze에서 캠페인으로 설정한 후에는 템플릿 변수를 변경하지 마세요. 다운스트림 변경 사항은 통합할 수 없습니다.
4. CTA 버튼 링크의 경우 **동적을** 선택한 다음 기본 URL(`brz.ai` 또는 커스텀 도메인)을 입력합니다.<br><br>\![클릭 유도 문안을 만드는 섹션입니다.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. 본문 텍스트의 링크의 경우, WhatsApp 매니저에서 템플릿을 작성할 때 추적하려는 링크가 본문에 포함된 경우 삽입된 공백을 모두 제거하세요.<br><br>\![텍스트 상자에 클릭 유도 문안의 콘텐츠 본문을 입력합니다.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### 2단계: Braze에서 템플릿 완성하기

작성 시 Braze는 본문 텍스트와 CTA 버튼 모두에서 지원 가능한 URL 도메인이 있는 템플릿을 자동으로 감지합니다. 상태는 템플릿 하단에 표시됩니다. 

클릭 추적을 위한 활성 상태를 보여주는 '링크 상태' 섹션.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **지원되는 링크:** 일치하는 기본 URL로 제출된 링크에는 클릭 추적이 인에이블먼트됩니다.
- **부분적으로 지원되는 링크:** 템플릿의 일부 링크가 전체 URL로 제출된 경우 해당 링크에는 클릭 추적이 **적용되지** 않습니다.
- **지원되지 않는 링크:** 승인된 기본 URL이 없는 **링크에는** 클릭 추적 기능이 없습니다.

대상 URL은 `brz.ai` 또는 커스텀 도메인과 일치하는 기본 URL이 있는 모든 링크에 대해 제공해야 합니다. 

버튼 이름, 웹사이트 URL, 클릭 추적 URL을 입력할 수 있는 필드가 있는 '버튼' 섹션입니다.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## URL의 Liquid 개인화

Braze 컴포저 내에서 직접 URL을 동적으로 구성할 수 있으므로 URL에 동적 UTM 매개변수를 추가하거나 사용자에게 고유한 링크를 보낼 수 있습니다(예: 사용자를 유기한 장바구니 또는 재고가 있는 특정 제품으로 연결).
URL은 지원되는 모든 Liquid 개인화 태그를 사용하여 동적으로 생성할 수 있습니다.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

또한 이 예시와 같이 커스텀 정의된 Liquid 변수를 단축하는 기능도 지원합니다:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid 변수에 의해 렌더링되는 URL 단축

Braze는 API 트리거 프로퍼티에 포함된 URL을 포함하여 Liquid에서 렌더링되는 URL을 단축합니다. 예를 들어 {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} 이 유효한 URL을 담당하는 경우, WhatsApp 메시지를 보내기 전에 해당 URL을 단축하여 추적합니다.

## 테스트

캠페인이나 캔버스를 시작하기 전에 먼저 메시지를 미리 보고 테스트하는 것이 가장 좋습니다. 이렇게 하려면 **테스트** 탭으로 이동하여 미리 보고 콘텐츠 테스트 그룹 또는 개별 사용자에게 WhatsApp을 전송합니다.

이 미리보기는 관련 개인화 및 단축 URL로 업데이트됩니다. 

{% alert important %}
활성 캔버스 내에서 초안을 만들면 단축 URL이 생성되지 않습니다. 실제 단축 URL은 캔버스 초안이 활성화되면 생성됩니다.
{% endalert %}

## 보고

클릭 추적이 켜져 있거나 지원되는 템플릿과 함께 사용되는 경우, WhatsApp 성능/성과 표에는 배리언트별 클릭 이벤트 수와 관련 클릭률을 보여주는 **총 클릭** 수 열이 포함됩니다. WhatsApp 측정기준에 대한 자세한 내용은 [WhatsApp 메시지 성능을]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics) 참조하세요.

\![WhatsApp 메시지 캔버스 단계.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

클릭 데이터는 분석 대시보드에 자동으로 보고됩니다.

\![WhatsApp 메시지 성능/성과 테이블.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## 사용자 리타겟팅하기 

`Clicked/Opened Step` 필터 및 `clicked tracked WhatsApp link` 상호 작용을 사용하여 링크와의 상호 작용을 기반으로 사용자를 세그먼트화할 수 있습니다.

!!! "클릭한 추적된 WhatsApp 링크"에 대한 필터를 사용하여 그룹을 필터링합니다.]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### 어떤 개별 사용자가 URL을 클릭하는지 알 수 있나요?

예. 클릭 추적이 켜져 있거나 템플릿 구성에 따라 인에이블먼트된 경우, WhatsApp 리타겟팅 필터 또는 커런츠에서 전송한 WhatsApp 클릭 이벤트(`users.messages.whatsapp.Click`)를 활용하여 URL을 클릭한 사용자를 리타겟팅할 수 있습니다.

### WhatsApp 기기에서 미리 보기를 클릭으로 계산하나요? 

아니요, 이들은 WhatsApp 메시징의 클릭률에 영향을 미치지 않습니다. 

