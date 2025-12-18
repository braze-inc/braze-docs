---
nav_title: LINE 클릭 추적
article_title: LINE 클릭 추적
page_order: 2
description: "이 페이지에서는 LINE 메시지에서 클릭 추적을 켜고, 단축 링크를 테스트하고, 추적 링크에 커스텀 도메인을 사용하는 방법 등에 대해 설명합니다."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# LINE 클릭 추적

> 이 페이지에서는 LINE 메시지에서 클릭 추적을 켜고, 단축 링크를 테스트하고, 추적 링크에 커스텀 도메인을 사용하는 방법 등에 대해 설명합니다.


LINE 클릭 추적을 켜면 Braze는 자동으로 URL을 단축하고 추적 메커니즘을 추가하며 클릭 수를 실시간으로 기록합니다. LINE은 총체적인 클릭 데이터를 제공하는 반면, Braze는 시의적절하고 실행 가능한 세분화된 사용자 정보를 제공합니다. 이 데이터를 통해 클릭 행동에 따라 사용자를 세분화하고 특정 클릭에 대한 반응으로 메시지를 트리거하는 등 보다 타겟화된 세분화 및 리타겟팅 전략을 수립할 수 있습니다.

LINE 클릭 추적은 텍스트, 리치, 카드 기반 메시징에 사용할 수 있습니다. 클릭 시 동작으로 URL이 있는 버튼 및 이미지 매핑 영역 내의 링크를 지원합니다. Liquid 및 커스텀 도메인을 사용하여 URL을 개인화할 수도 있습니다.

## 작동 방식

메시지 작성 중 **설정** 탭에서 LINE 클릭 추적 설정을 관리할 수 있습니다. 이 기능을 켜면 기본값인 Braze 도메인(`https://brz.ai`) 또는 구독 그룹에 지정된 커스텀 도메인을 사용하여 URL이 단축되고 사용자에 맞게 개인화됩니다.

`http://` 또는 `https://` 로 시작하는 모든 URL은 단축됩니다. 메시징에는 최대 25개의 URL을 포함할 수 있습니다. Liquid 개인화(예: 사용자 수준 추적 또는 UTM 매개변수)가 포함된 단축 URL은 2개월 동안 유효합니다.

## 클릭 추적 설정하기

### 문자 메시지

문자 메시지에 대한 클릭 추적을 설정하려면 다음과 같이 하세요:

1. **문자** 메시지를 작성기로 드래그하고 텍스트 필드에 URL을 추가합니다.

\![긴 URL이 포함된 문자 메시지가 있는 LINE 메시지 작성기: https://braze.com/docs/user_guide/message_building_by_channel/line/create/]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2\. **설정** 탭으로 이동하여 **클릭 추적이** 켜져 있는지 확인합니다. 클릭 추적은 모든 새 메시징에 대해 기본값으로 켜져 있습니다.

{% alert note %}
**설정** 또는 **미리보기 & 테스트** 탭에서 단축 링크의 미리 보기를 볼 수 있습니다. 메시지를 구축하는 동안 작성기에 전체 링크가 표시됩니다.
{% endalert %}

LINE 메시지 작성기의 "설정" 탭에서 "클릭 추적"이 켜져 있고 단축 URL이 포함된 미리보기 문자 메시지: https://olaf.brz.ai/p/9rcfdqdD.]({% image_buster /assets/img/line/click_tracking_settings.png %})

### 풍부한 메시지

리치 메시지에 대한 클릭 추적을 설정하려면 다음과 같이 하세요:

1. **리치 메시지를** 작성기로 드래그하고 템플릿을 선택합니다.
2. 해당 탭 가능한 영역의 **클릭 시 동작에** 대한 **URI를** 선택합니다.
3. **URL 열기** 필드에 URL을 입력합니다.

탭 가능한 두 개의 영역에 각각 URL이 있는 리치 메시지가 있는 LINE 메시지 작성기.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4\. **설정** 탭으로 이동하여 **클릭 추적이** 켜져 있는지 확인합니다. 클릭 추적은 모든 새 메시징에 대해 기본값으로 켜져 있습니다.

### 카드 기반 메시지

카드 기반 메시징에 대한 클릭 추적을 설정하려면 다음과 같이 하세요:

1. **카드 기반 메시지를** 작성기로 드래그합니다.
2. 해당 카드 또는 버튼 영역의 **클릭 시 동작에** 대한 **URI를** 선택합니다.

각각 URL이 있는 두 개의 버튼이 있는 카드 기반 메시지가 있는 LINE 메시지 작성기.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3\. **설정** 탭으로 이동하여 **클릭 추적이** 켜져 있는지 확인합니다. 클릭 추적은 모든 새 메시징에 대해 기본값으로 켜져 있습니다.

{% alert note %}
**제목** 또는 **설명** 필드의 URL은 LINE 내에서 클릭할 수 없으므로 단축되지 않습니다.
{% endalert %}

## 커스텀 도메인

LINE 클릭 추적을 사용하면 자체 도메인을 사용하여 단축 URL의 모양과 느낌을 개인화할 수 있어 일관된 브랜드 이미지를 전달할 수 있습니다. 자세한 내용은 [커스텀 도메인을]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains) 참조하세요.

## URL의 Liquid 개인화

Braze 컴포저 내에서 직접 URL을 동적으로 구성할 수 있으므로 URL에 동적 UTM 매개변수를 추가하거나 사용자에게 고유한 링크를 보낼 수 있습니다(예: 사용자를 유기한 장바구니 또는 재고가 있는 특정 제품으로 연결).
URL은 지원되는 모든 Liquid 개인화 태그를 사용하여 동적으로 생성할 수 있습니다.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

다음 예시와 같이 커스텀 정의된 Liquid 변수를 단축할 수도 있습니다:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Liquid 변수에 의해 렌더링되는 URL 단축

Braze는 API 트리거 프로퍼티에 포함된 URL을 포함하여 Liquid에서 렌더링되는 URL을 단축합니다. 예를 들어 {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} 이 유효한 URL을 담당하는 경우, 해당 URL을 단축하여 추적한 후 LINE 메시지를 전송합니다.

## 테스트

캠페인이나 캔버스를 시작하기 전에 먼저 메시지를 미리 보고 테스트하는 것이 가장 좋습니다. **테스트** 탭으로 이동하여 콘텐츠 테스트 그룹 또는 개별 사용자에게 LINE 메시지를 미리 보고 전송할 수 있습니다.

이 미리보기는 관련 개인화 및 단축 URL로 업데이트됩니다. 

{% alert important %}
활성 캔버스 내에서 초안을 만들면 단축 URL이 생성되지 않습니다. 실제 단축 URL은 캔버스 초안이 활성화되면 생성됩니다.
{% endalert %}

## 보고

LINE 성능/성과 표에는 배리언트별 클릭 이벤트 수와 관련 클릭률을 보여주는 **총 클릭** 수 열이 포함되어 있습니다. LINE 측정기준에 대한 자세한 내용은 [LINE 메시지 성능/성과를]({{site.baseurl}}/user_guide/message_building_by_channel/line/reporting) 참조하세요.

!\![LINE 캔버스 단계의 성능/성과.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

클릭 데이터는 분석 대시보드에 자동으로 보고됩니다. 

LINE 성능/성과 분석 대시보드.]({% image_buster /assets/img/line/line_performance.png %})

## 사용자 리타겟팅하기

다음 세분화 필터와 트리거를 사용하여 LINE 메시지에서 URL을 클릭한 사용자를 리타겟팅할 수 있습니다:

- 동작 기반 트리거
    - 캠페인과 상호 작용하기
    - Step과 상호 작용

\![LINE 실행 기반 전달 트리거.]({% image_buster /assets/img/line/line_action_based.png %})

- 세분화 필터
    - 클릭/열린 캠페인
    - 클릭/열린 캠페인 또는 태그가 있는 캔버스 
    - 클릭/열기 단계

\![세 가지 세분화 필터를 모두 표시하는 필터 그룹: "클릭/열린 캠페인", "클릭/열린 캠페인 또는 태그가 있는 캔버스", "클릭/열린 단계".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## 자주 묻는 질문

### 테스트 전송 시 받은 링크가 실제 URL인가요?

예, 테스트 전송 시 실제 URL이 생성됩니다. 그러나 론칭된 캠페인에서 전송된 정확한 URL은 테스트 전송에서 전송된 URL과 다를 수 있습니다.

### URL을 단축하기 전에 UTM 매개변수를 추가할 수 있나요?

예, 정적 및 동적 매개변수를 모두 추가할 수 있습니다.

### 단축 URL은 얼마 동안 유효하나요?

개인화된 URL은 URL 등록 시점부터 2개월 동안 유효합니다.

### URL을 단축하려면 Braze 소프트웨어 개발 키트를 설치해야 하나요?

아니요, 클릭 추적은 SDK 통합 없이도 작동합니다.

### 어떤 개별 사용자가 URL을 클릭하는지 알 수 있나요?

예. 클릭 추적이 켜져 있으면 [LINE 리타겟팅 필터를](#retargeting-users) 사용하여 URL을 클릭한 사용자를 리타겟팅할 수 있습니다.

### 클릭 추적은 딥링크 또는 유니버설 링크에서 작동하나요?

딥링크에서는 클릭 추적이 작동하지 않습니다. Branch 또는 Appsflyer와 같은 제공업체의 유니버설 링크를 단축할 수 있지만, 이 과정에서 발생할 수 있는 문제(기여도가 깨지거나 리디렉션에 실패하는 등)는 Braze가 해결할 수 없습니다.

### LINE 앱의 미리보기도 클릭 수에 포함되나요?

아니요, LINE 메시징의 클릭률에 영향을 미치지 않습니다.