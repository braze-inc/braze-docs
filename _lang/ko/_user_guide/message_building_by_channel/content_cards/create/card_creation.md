---
nav_title: 카드 생성
article_title: 카드 생성
alias: /card_creation/
description: "이 문서에서는 캠페인 시작 또는 캔버스 단계 진입 시 콘텐츠 카드를 만드는 것과 첫 노출 시 콘텐츠 카드를 만드는 것의 차이점에 대해 설명합니다."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# 카드 생성

> 카드가 생성되는 시점을 지정하여 새 콘텐츠 카드 캠페인 및 캔버스 단계에 대해 Braze가 오디언스 자격 및 개인화를 평가하는 시점을 선택할 수 있습니다.

## 전제 조건

이 기능을 이용하려면 다음 최소 소프트웨어 개발 키트 버전으로 업그레이드해야 합니다:

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

소프트웨어 개발 키트를 업그레이드한 후 모바일 사용자는 앱을 업그레이드해야 합니다. 캠페인 또는 캔버스 오디언스를 필터링하여 [이러한 최소 앱 버전의 사용자만 타겟팅할]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) 수 있습니다.

## 개요

{% tabs %}
{% tab Campaign %}

배달이 예약된 새 [콘텐츠 카드 캠페인을]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) 만들 때 **배달** 단계에서 Braze가 카드를 생성하는 시기를 선택할 수 있습니다.

예약된 콘텐츠 카드의 전달을 편집할 때 콘텐츠 카드 제어 섹션을 클릭합니다.]({% image_buster /assets/img_archive/card_creation.png %})

다음 옵션을 사용할 수 있습니다:

- **캠페인 시작 시:** 콘텐츠 카드의 이전 기본값입니다. Braze는 캠페인이 시작될 때 오디언스 자격과 개인화를 계산한 다음, 카드를 생성하고 사용자가 앱을 열 때까지 저장합니다. 
- **첫 노출 횟수(권장):** 사용자가 다음에 앱을 열면(즉, 새 [세션을](https://www.braze.com/resources/articles/whats-an-app-session-anyway) 시작하면) Braze는 사용자가 어떤 콘텐츠 카드를 받을 자격이 있는지 확인하고 Liquid 또는 연결된 콘텐츠와 같은 개인화를 템플릿화한 다음 카드를 생성합니다. 이 옵션은 일반적으로 카드 전달에서 더 나은 성능/성과를 제공합니다.

선택한 옵션에 관계없이 캠페인이 시작되면 콘텐츠 카드 만료일 카운트다운이 시작됩니다.

{% endtab %}
{% tab Canvas %}

콘텐츠 카드 [메시지 단계의]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) **메시징 채널** 탭에서 Braze가 카드를 생성하는 시기를 선택할 수 있습니다.

예약된 콘텐츠 카드의 전달을 편집할 때 콘텐츠 카드 제어 섹션을 클릭합니다.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

다음 옵션을 사용할 수 있습니다:

- **단계 입력 시:** 콘텐츠 카드의 이전 기본값입니다. 사용자가 캔버스 단계에 진입하면 Braze는 오디언스 자격을 계산한 다음 카드를 생성하고 사용자가 앱을 열 때까지 저장합니다.
- **첫 노출 횟수(권장):** Braze는 사용자가 캔버스 단계에 진입하면 오디언스 자격을 계산합니다. 사용자가 다음에 앱을 열면(즉, 새 [세션을](https://www.braze.com/resources/articles/whats-an-app-session-anyway) 시작하면) Braze는 Liquid 또는 연결된 콘텐츠와 같은 개인화를 템플릿화한 다음 카드를 생성합니다. 이 옵션을 사용하면 카드 전달 성능/성과가 향상되고 보다 최신의 개인화가 가능합니다.

선택한 옵션에 관계없이 사용자가 캔버스 단계에 들어가면 콘텐츠 카드 만료일 카운트다운이 시작됩니다.

{% alert tip %}
익명 사용자가 첫 세션에서 콘텐츠 카드를 보도록 하려면 캔버스 대신 캠페인을 사용하세요. 익명 사용자가 캔버스에 들어가면 이미 세션이 시작된 상태이므로 새 세션을 시작할 때까지 콘텐츠 카드를 받을 수 없기 때문입니다.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
두 옵션 모두, 카드가 생성된 후 Braze는 오디언스 자격 또는 개인화를 다시 계산하지 않습니다.
{% endalert %}

### 시작 또는 입장 시 카드 생성과 첫 노출 횟수의 차이점

이 섹션에서는 캠페인 시작 또는 단계 진입 시와 첫 노출 시 카드 생성의 주요 차이점에 대해 설명합니다.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">캠페인 시작 시 / 캔버스 단계 진입 시</th>
    <th class="tg-0pky">첫인상 노출 횟수</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">사용 시기</td>
    <td class="tg-0pky">특정 시간(시작 시간)에 콘텐츠를 스냅샷해야 하는 경우.</td>
    <td class="tg-0pky"><ul><li>출시 후 세그먼트에 입장할 수 있는 신규 또는 익명 사용자에게 카드를 표시해야 하는 경우<a href="#campaign_note">(캠페인에만 해당*</a>).</li><li>개인화를 사용 중이고 카드에서 최신 콘텐츠를 사용하려는 경우.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">오디언스</td>
    <td class="tg-0pky">Braze는 캠페인이 전송될 때 오디언스 멤버십을 평가합니다.<br><br>신규 사용자 또는 익명 사용자가 캠페인 전송 후 카드를 보려고 시도하는 경우 자격 여부를 평가하지 않습니다. 반복 캠페인의 경우 다음 반복 간격이 됩니다.</td>
    <td class="tg-0pky">Braze는 사용자가 다음에 앱을 열 때 멤버십을 평가합니다(세션 시작, <a href="#campaign_note">캠페인만 해당*</a>).<br><br> 이 설정은 신규 또는 익명 사용자가 카드를 보려고 할 때 항상 적격성 여부를 평가하므로 오디언스 범위가 더 넓어집니다. <br><br>또한, 첫 노출로 설정한 경우 비율 제한(카드를 받을 수 있는 사람 수 제한)은 적용되지 않습니다.</td>
  </tr>
  <tr>
    <td class="leftHeader">개인화</td>
    <td class="tg-0pky">Braze는 캠페인이 시작될 때 또는 사용자가 캔버스 단계에 진입할 때 Liquid, 연결된 콘텐츠, 콘텐츠 블록을 평가합니다. 반복 캠페인의 경우 다음 반복 간격이 됩니다.</td>
    <td class="tg-0pky">Braze는 첫 노출 시점 또는 다음 반복 간격 이후에 Liquid, 연결된 콘텐츠 및 콘텐츠 블록을 평가합니다.</td>
  </tr>
  <tr>
    <td class="leftHeader">분석</td>
    <td class="tg-0pky"><em>보낸 메시지는</em> 생성되어 볼 수 있는 카드의 수를 나타냅니다. 사용자가 카드를 조회했는지 여부는 포함되지 않습니다.</td>
    <td class="tg-0pky"><em>보낸 메시지는</em> 세션 시작 후 사용자에게 전송된 카드의 수를 나타냅니다. 캔버스에서는 세션을 시작하지 않고 단계에 진입하는 사용자에게는 카드가 전송되지 않으므로 이 측정기준이 단계에 진입하는 사용자 수와 일치하지 않을 수 있습니다.<br><br>도달 가능한 사용자와 노출 횟수는 변하지 않지만, 동일한 카드가 캠페인 시작 또는 캔버스 단계 진입 시 생성된 경우에 비해 첫 노출 시 생성된 카드의 전송량<em>(전송된 메시지 수)</em>이 감소하는 것을 확인할 수 있습니다.</td>
  </tr>
  <tr>
    <td class="leftHeader">처리 시간</td>
    <td class="tg-0pky">카드는 출시 시점에 세그먼트의 모든 적격 사용자에 대해 생성됩니다. <b>오디언스가</b> 많은 경우에는 출시 후 카드를 더 빨리 사용할 수 있으므로 <b>첫 노출을</b> 선택하는 것이 좋습니다.</td>
    <td class="tg-0pky">카드는 사용자가 처음 카드를 보려고 할 때 생성되므로 첫 노출 횟수에 표시되는 데 1~2초가 소요될 수 있습니다.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* 캔버스 오디언스는 단계 수준이 아닌 캔버스 항목에서 평가되므로 이 시나리오는 캠페인에만 적용됩니다.</sup></p>

## 고려 사항

### 출시 후 카드 생성 변경

Braze는 캠페인이 시작된 후에는 카드 생성 방식을 변경하지 않는 것을 권장합니다. 두 카드 생성 유형 간에 전송된 메시지 수 계산 방식이 다르기 때문에 캠페인이 시작된 후 카드 생성 방식을 변경하면 전송량의 정확성에 영향을 미칠 수 있습니다.

### 잠재적 처리 시간

캠페인 시작 후 카드를 훨씬 더 빨리 사용할 수 있으므로 오디언스가 많은 캠페인의 경우 첫 노출 시 카드 생성 옵션을 선택하는 것이 좋습니다. 세션 시작 시 트리거되는 캠페인은 첫 노출 시 카드 생성(예약 전달을 통해 사용 가능)으로 전환하여 성능/성과를 개선하는 것도 고려할 수 있습니다.

첫 노출 횟수에서 카드가 생성되면 카드가 처리되는 데 1~2초가 걸릴 수 있습니다. 이 처리 시간은 카드 크기와 메시지 템플릿 옵션의 복잡성 등 다양한 요인에 따라 달라집니다. 예를 들어 연결된 콘텐츠를 사용하는 카드의 처리 시간은 적어도 연결된 콘텐츠 응답 시간만큼 길어집니다.

### 이전 소프트웨어 개발 키트 버전

사용자의 앱이 이전 버전의 소프트웨어 개발 키트를 실행 중인 경우에도 지정된 카드 생성과 함께 전송된 콘텐츠 카드를 받게 됩니다. 그러나 이러한 사용자에게는 카드가 표시되는 데 시간이 오래 걸리며 다음 콘텐츠 카드 동기화 때까지 표시되지 않을 수 있습니다.

