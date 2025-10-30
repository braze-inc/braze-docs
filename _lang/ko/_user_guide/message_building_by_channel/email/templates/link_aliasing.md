---
nav_title: 링크 별칭 지정
article_title: 링크 별칭 지정
alias: /link_aliasing/
page_order: 3
description: "이 문서에서는 링크 별칭 지정의 작동 원리를 설명하고 링크의 모양에 대한 예시를 제공합니다."
channel:
  - email

---

# [\![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"} 링크 별칭 지정
 
> 링크 별칭 지정을 사용하여 인식 가능한 사용자 생성 이름을 만들어 Braze에서 이메일 메시지로 전송된 링크를 식별할 수 있습니다. 이러한 링크는 세그먼트 리타겟팅, 액션 기반 트리거 동작 및 링크 분석에 사용할 수 있습니다.

## 링크 별칭 지정 정보

링크 별칭 지정 기능을 사용하면 사용자 생성 이름을 만들어 이메일에 전송된 링크를 식별하고 추적할 수 있습니다. 이렇게 하면 전체 링크를 참조하지 않고도 이메일에서 이러한 인식 가능한 링크 별칭 지정을 효율적으로 사용하여 참여도를 추적하고 캠페인 성과를 분석할 수 있습니다.

링크 별칭 지정을 사용하면 가능합니다:

- **특정 링크를 클릭한 사용자를 리타겟팅하세요:** 링크를 클릭한 사용자를 식별하고 타겟팅합니다.
- **동작 기반 트리거를 만듭니다:** 사용자가 링크를 클릭하면 이메일을 보냅니다.
- **측정기준을 분석합니다:** 링크 A를 클릭한 사용자 수와 링크 B를 클릭한 사용자 수를 비교합니다.

### 작동 방식

Braze는 모든 링크 URL에 `lid` (링크 식별자라고도 함)라는 추가 파라미터를 추가하여 이메일 내의 링크를 고유하게 식별합니다. 이 `lid` 값을 사용하면 나머지 URL 매개변수가 다르더라도 Braze는 링크에 대한 사용자 상호작용을 추적, 모니터링 및 집계할 수 있습니다. 이를 통해 사용자가 이메일 캠페인의 콘텐츠에 어떻게 참여하는지에 대한 인사이트를 얻을 수 있습니다.

이메일 캠페인, 이메일 메시지가 포함된 캔버스 또는 콘텐츠 블록이 중복되는 경우 링크 식별자도 업데이트됩니다.

## 링크 별칭 지정하기

링크 별칭을 지정하려면 다음 단계를 따르세요: 

1. 캠페인 또는 캔버스 컴포넌트에서 이메일 본문으로 이동합니다.
2. **링크 관리** 탭을 선택합니다.
3. Braze는 각 링크에 대해 고유한 기본값 링크 별칭을 자동으로 생성합니다.
4. 별칭에 이름을 지정합니다. 별칭은 이메일 캠페인 배리언트 또는 캔버스 컴포넌트별로 고유한 이름을 지정해야 합니다. 

보고 또는 세그먼트 세분화 시 특정 링크를 참조하는 데 사용할 별칭을 설정할 수도 있습니다. 

네 개의 링크 별칭 지정이 가능한 링크 관리 페이지.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
링크 별칭 지정은 쿼리 매개변수를 추가해도 안전한 HTML 앵커 태그 내의 `href` 속성에서만 지원됩니다. 링크 끝에 물음표(?)를 넣는 것이 가장 좋은 방법이며, 이를 통해 Braze가 `lid` 값을 쉽게 추가할 수 있습니다. `lid` 값을 추가하지 않으면 Braze는 링크 별칭 지정을 위한 URL을 인식하지 못합니다.
{% endalert %}

## 링크 별칭 지정 관리하기

추적된 링크 별칭 지정을 모두 보려면 다음과 같이 하세요:

1. **워크스페이스 설정에서** **설정** > **이메일 환경설정으로** 이동합니다.
2. **링크 별칭 지정 설정** 탭을 선택합니다.

{% alert important %}
[이전 탐색을]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) 사용하는 경우 이러한 설정은 **설정 관리** 아래에 있습니다.
{% endalert %}

여기에서 링크 별칭 지정을 정렬, 검색하고 추적을 해제할 수 있습니다.

\![ "Email_Survey".]({% image_buster /assets/img/tracked_aliases.png %}라는 캠페인과 연관된 "TechPartners" 및 "Help"라는 두 개의 링크 별칭 지정이 표시된 링크 별칭 지정 추적 페이지입니다.)

{% alert tip %}
캠페인의 [경우 목록 링크 별칭]({{site.baseurl}}/get_campaign_link_alias/) 지정 및 [캔버스]({{site.baseurl}}/get_canvas_link_alias/) 엔드포인트의 [경우 목록 링크 별칭]({{site.baseurl}}/get_canvas_link_alias/) 지정을 사용하여 캠페인 또는 이메일별 캔버스 컴포넌트의 각 메시지 배리언트에 설정된 `alias` 을 추출합니다.
{% endalert %}

Braze는 이메일 내의 링크를 평가하고, 링크 템플릿을 추가하고, 세분화 및 보고 목적에 맞는 명명 규칙을 제공할 것을 권장합니다. 이렇게 하면 모든 링크를 추적할 수 있습니다.

링크 별칭 지정이 켜져 있으면 메시지, 콘텐츠 블록 및 링크 템플릿은 수정되지 않습니다. 링크 템플릿 또는 콘텐츠 블록을 사용하는 기존 메시지는 모두 동일합니다. 그러나 메시지를 업데이트하면 링크 별칭 지정 마크업이 모든 링크에 적용되므로 링크가 표시되려면 링크 템플릿을 다시 적용해야 합니다.

## 링크 별칭 지정으로 링크가 업데이트되는 방법

다음 표에서는 이메일 본문에 있는 링크의 예, 링크 별칭 지정 결과, 링크 별칭 지정으로 원본 링크가 업데이트되는 방식에 대한 설명을 제공합니다.

### 영구 링크

**논리:** Braze는 물음표(?)를 삽입하고 첫 번째 쿼리 매개변수를 URL에 추가합니다.

| 이메일 본문에 링크    | 별칭 지정이 있는 링크                     |
|-----------------------|----------------------------------------|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 더 많은 쿼리 매개변수와 연결

**논리:** Braze는 다른 쿼리 매개변수를 감지하여 URL 끝에 `lid=` 을 추가합니다.

| 이메일 본문에 링크                                            | 별칭 지정이 있는 링크                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML 링크

**논리:** Braze는 링크가 URL이고 이미 물음표(?)가 있는 것으로 인식하여 물음표 뒤에 `lid` 쿼리 매개변수를 추가합니다.

| 이메일 본문에 링크                                                | 별칭 지정이 있는 링크                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 앵커 링크

**논리:** Braze는 URL이 물음표(?) 뒤에 앵커(#)가 있는 표준 구조를 사용할 것으로 예상합니다. Braze는 왼쪽에서 오른쪽으로 읽으므로 앵커 앞에 물음표와 `lid` 값이 추가됩니다.

| 이메일 본문에 링크                               | 별칭 지정이 있는 링크                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 앵커 및 캡처 태그와 링크하기

**논리:** 앵커(#)가 포함된 URL에 링크 별칭 지정을 사용하는 경우 Braze는 앵커가 쿼리 매개변수 뒤에 배치될 것으로 예상합니다. 즉, 제대로 추적하려면 앵커 앞에 `lid` 값을 추가해야 하며, Braze는 URL을 왼쪽에서 오른쪽으로 읽으므로 앵커 앞에 물음표(?)와 `lid` 이 와야 합니다.

| 이메일 본문에 링크                                                                        | 별칭 지정이 있는 링크                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions#special-offer?lid={{link_alias}}">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 링크 별칭 지정 추적하기

**링크 관리** 탭에서 세그먼트화 목적으로 "추적"하고 세그먼트화 필터에 표시할 별칭을 선택합니다. 링크 별칭 지정은 세분화 목적으로만 사용되며 보고 목적으로 추적되는 링크에는 영향을 미치지 않습니다.

{% alert tip %}
링크 참여 측정기준을 추적하려면 링크 앞에 HTTP 또는 HTTPS가 오는지 확인하세요. 특정 링크에 대한 클릭 추적을 해제하려면 [유니버설 링크 및 앱 링크를]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis) 참조하세요.
{% endalert %}

Braze에서는 추적할 링크를 무제한으로 선택할 수 있지만, 사용자가 가장 최근에 연 링크에 대해서만 리타겟팅할 수 있습니다. 고객 프로필에는 가장 최근에 클릭한 100개의 링크가 포함됩니다. 예를 들어 500개의 링크를 추적하고 사용자가 500개의 링크를 모두 클릭한 경우, 가장 최근에 클릭한 100개의 링크를 기반으로 리타겟팅하거나 세그먼트를 생성할 수 있습니다.

{% tabs local %}
{% tab Drag-And-Drop Editor %}

드래그 앤 드롭 이메일 편집기의 링크 관리 탭입니다.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab HTML editor %}

HTML 이메일 편집기의 링크 관리 탭을 클릭합니다.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Braze는 프로필 수준에서 최근 100회 클릭한 링크 별칭 지정까지만 추적합니다.
{% endalert %}

### 액션 기반 필터
 
모든 링크(추적 또는 미추적)를 타겟팅하는 액션 기반 메시지를 만들거나 이메일 캠페인 또는 캔버스 컴포넌트에서 별칭을 클릭했는지 여부에 따라 사용자를 리타겟팅할 수 있습니다.

캔버스 컴포넌트에서 사용자 별칭을 클릭하거나 캠페인과 상호 작용한 사용자를 타겟팅하는 액션 기반 옵션입니다.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### 세분화 필터

Braze에서는 이메일에 링크 별칭 지정이 있고 사용자가 이를 클릭하면 해당 이벤트가 해당 별칭과 함께 사용자 프로필에 기록됩니다.

"모든 캠페인 또는 캔버스 단계에서 클릭 별칭" 세분화 필터를 사용하고 나중에 이 링크 별칭의 이름을 변경하는 경우, 사용자 프로필의 이전 클릭 데이터는 **업데이트되지 않으므로** 여전히 이전 링크 별칭으로 표시됩니다. 따라서 새 링크 별칭 지정을 기반으로 사용자를 타겟팅하는 경우 이전 링크 별칭의 데이터는 포함되지 않습니다.

'캠페인에서 클릭한 별칭' 또는 '캔버스에서 클릭한 별칭' 세분화 필터를 사용하면 특정 캠페인 또는 캔버스에서 특정 별칭을 클릭했는지 여부에 따라 사용자를 필터링합니다. 여러 사용자가 동일한 이메일 주소를 공유하고 링크 별칭 지정을 클릭하면 해당 이메일 주소를 공유하는 다른 모든 사용자의 사용자 프로필이 업데이트됩니다. 

이벤트가 처리되는 시점에 추적되는 클릭 이벤트에는 다음 세분화 필터가 적용됩니다. 즉, 추적되지 않은 링크는 기존 데이터를 제거하지 않으며 링크를 추적해도 데이터를 다시 채우지 않습니다. 자세한 내용은 [세분화 필터를]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) 참조하세요.

#### 링크 추적 해제

링크를 추적 해제해도 필터가 있는 기존 세그먼트는 추적 해제된 별칭으로 재할당되지 않습니다. 이전 데이터는 최신 데이터로 교체될 때까지 사용자 프로필에 남아 있습니다. 

보관된 메시징의 링크는 자동으로 추적 해제됩니다. 그러나 보관된 메시징이 보관 해제된 경우에는 링크를 다시 추적해야 합니다. 링크 별칭 지정이 추적되면 링크 보고는 최상위 도메인이나 전체 URL이 아닌 별칭을 기준으로 색인화됩니다.

세 개의 링크 별칭 지정과 총 클릭 수를 표시하는 캠페인 분석 탭입니다.]({% image_buster /assets/img/link_aliasing_click_table.png %})

### 이메일 클릭 이벤트

커런츠에서 참여 데이터를 내보내는 경우 링크 별칭 지정이 활성화된 경우 이메일 클릭 이벤트가 약간 달라집니다. 링크 별칭 지정이 켜져 있는 경우 [이메일 클릭 이벤트에]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/) `link_id` 및 `link_alias` 이라는 두 개의 추가 필드가 생깁니다.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
`dispatch_id` 에 대한 동작은 캔버스와 캠페인 간에 다르며, 그 이유는 Braze는 캔버스 단계(예약 가능한 엔트리 단계 제외)가 "예약된" 경우에도 트리거된 이벤트로 취급하기 때문입니다. 캔버스 및 캠페인의 [`dispatch_id` 동작에]({{site.baseurl}}/help/help_articles/data/dispatch_id/) 대해 자세히 알아보세요.

_2019년 8월에 업데이트되었습니다._
{% endalert %}

## 콘텐츠 블록의 링크 별칭 지정

새로운 콘텐츠 블록은 링크가 수정되며, Braze는 해당되는 경우 각 링크에 `lid={{placeholder}}` 을 추가합니다. 이 입력 안내자 값은 이메일 메시지 배리언트에 삽입될 때 확인됩니다.

Brave에서 링크 별칭 지정을 인에이블먼트하기 전에 생성된 기존 콘텐츠 블록 내의 링크를 수정하려면 기존 콘텐츠 블록을 복제하고 복제된 콘텐츠 블록 내의 링크를 수정합니다.

`lid` 값이 없는 콘텐츠 블록을 새 메시지에 삽입하면 해당 콘텐츠 블록의 링크는 별칭으로 추적되지 않습니다. 새 콘텐츠 블록이 "이전" 메시지 배리언트에 삽입되면 해당 메시지 배리언트의 링크는 링크 별칭 지정을 통해 인식됩니다. 콘텐츠 블록의 링크도 인식됩니다. 그러나 "이전" 콘텐츠 블록은 "새" 콘텐츠 블록을 중첩할 수 없습니다.

{% alert tip %}
콘텐츠 블록의 경우 새 메시징에 사용할 기존 콘텐츠 블록의 사본을 만드는 것이 좋습니다. 대량 복제를 통해 새 메시지에서 링크 별칭 지정이 인에이블먼트되지 않은 콘텐츠 블록을 참조할 수 있는 시나리오를 방지할 수 있습니다.
{% endalert %}

## Liquid에서 생성한 URL에 대한 링크 별칭 지정

HTML 또는 콘텐츠 블록의 `assign` 문과 같이 Liquid에서 생성된 URL의 경우 Liquid 태그에 물음표(`?`)를 추가해야 합니다. 이를 통해 Braze는 링크 별칭 지정이 제대로 작동할 수 있도록 쿼리 매개변수(`lid = somevalue`)를 추가할 수 있습니다. 쿼리 매개변수를 추가할 위치를 식별하지 않으면 링크 별칭 지정이 이러한 URL을 인식하지 못하며 링크 템플릿이 적용되지 않습니다.

### 예

권장되는 링크 별칭 지정 형식은 이 링크 별칭 지정 예시를 확인하세요:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

링크에 물음표(`?`)가 포함된 매개변수가 있는 경우 이 예제에서처럼 앵커 태그에서 물음표를 앰퍼샌드(`&`)로 바꿀 수 있습니다:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}


