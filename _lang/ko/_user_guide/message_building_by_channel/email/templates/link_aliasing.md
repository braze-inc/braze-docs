---
nav_title: 링크 별칭 지정
article_title: 링크 별칭 지정
alias: /link_aliasing/
page_order: 3
description: "이 글은 링크 별칭 지정이 어떻게 작동하는지 설명하고, 링크가 어떻게 표시될지에 대한 예시를 제공합니다."
channel:
  - email

---

# [![Braze Learning ](https://learning.braze.com/link-aliasing)과정 []({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}링크 별칭 지정
 
> 링크 별칭 지정을 사용하여 Braze에서 이메일 메시지로 보낸 링크를 식별할 수 있는 인식 가능한 사용자 생성 이름을 만드십시오. 이 링크는 세분화 리타겟팅, 행동 기반 트리거링 및 링크 분석에 사용할 수 있습니다.

## 링크 별칭 지정에 관하여

링크 별칭 지정을 사용하면 이메일로 전송된 링크를 식별자(identifier)로 사용하고 추적하기 위한 사용자 생성 이름을 만들 수 있습니다. 이렇게 하면 이메일에서 이러한 식별 가능한 링크 별칭을 효율적으로 활용하여 참여도를 추적하고 캠페인 성능을 분석할 수 있으며, 전체 링크를 참조할 필요가 없습니다.

링크 별칭 지정을 사용하면 다음과 같은 작업을 수행할 수 있습니다:

- **특정 링크를 클릭한 사용자를 대상으로 리타겟팅:** 링크를 클릭한 사용자를 식별하고 타겟팅하십시오.
- **작업 기반 트리거 생성:** 사용자가 링크를 클릭할 때 이메일을 발송합니다.
- **측정기준 분석:** 링크 A와 링크 B를 클릭한 사용자 수를 비교하십시오.

### 작동 방식

Braze는 모든 링크 URL에  (링크 `lid`식별자라고도 함)이라는 추가 매개변수를 부착하여 이메일 내 링크를 고유하게 식별합니다. 이`lid`값을 통해 Braze는 URL의 나머지 매개변수가 달라질 수 있더라도 링크와의 사용자 상호작용을 추적, 모니터링 및 집계할 수 있습니다. 이는 사용자가 이메일 캠페인 콘텐츠에 어떻게 참여하는지에 대한 인사이트를 제공하는 데 도움이 됩니다.

이메일 캠페인, 이메일 메시지가 포함된 캔버스 또는 콘텐츠 블록이 복제될 경우 링크 식별자도 업데이트됩니다.

## 링크 별칭 만들기

링크 별칭을 만들려면 다음 단계를 따르세요: 

1. 캠페인 또는 캔버스 구성 요소에서 이메일 본문을 확인하세요.
2. **링크 관리** 탭을 선택하십시오.
3. Braze는 각 링크에 대해 고유한 기본값 링크 별칭을 자동으로 생성합니다.
4. 별칭에 이름을 지정하십시오. 별칭은 이메일 캠페인 배리언트 또는 캔버스 구성 요소마다 고유하게 명명되어야 합니다. 

보고 또는 세분화를 다룰 때 특정 링크를 참조하는 데 사용할 별칭을 설정할 수도 있습니다. 

![링크 관리 페이지에 네 개의 링크 별칭이 있습니다.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
링크 별칭 지정은 쿼리 매개변수를 추가하는 것이 안전한 HTML 앵커 태그의 `href` 속성 내에서만 지원됩니다. 링크 끝에 물음표(?)를 포함하는 것이 권장되는 방법입니다. 이렇게 하면 Braze가 값을`lid` 쉽게 추가할 수 있습니다. `lid` 값을 추가하지 않으면 Braze는 링크 별칭 지정을 위한 URL을 인식하지 못합니다.
{% endalert %}

## 링크 별칭 관리

추적 중인 모든 링크 별칭을 보려면 다음을 수행하세요:

1. **설정** > **이메일 환경설정** 아래 **작업 공간 설정**으로 이동합니다.
2. **링크 별칭 지정** 탭을 선택하십시오.

{% alert important %}
[이전 탐색]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)을 사용하는 경우 이러한 설정은 **설정 관리** 아래에 있습니다.
{% endalert %}

여기서 링크 별칭을 정렬하고, 검색하고, 추적을 해제할 수 있습니다.

![추적 링크 별칭 페이지로, 다양한 캠페인과 연결된 활성 및 비활성 링크 별칭을 표시합니다.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
[캠페인의 경우 목록 링크 별칭]({{site.baseurl}}/get_campaign_link_alias/) 및 [캔버스 엔드포인트의 경우 목록 링크 별칭을]({{site.baseurl}}/get_canvas_link_alias/) 사용하여 캠페인 또는 이메일별 캔버스 구성 요소의 각 메시지 변형에 설정된 `alias` 을 추출합니다.
{% endalert %}

Braze는 이메일 내 링크를 평가하고 링크 템플릿을 추가하며 세분화 및 보고 목적으로 작동하는 명명 규칙을 제공할 것을 권장합니다. 이것은 모든 링크를 추적하는 데 도움이 됩니다.

링크 별칭 지정이 활성화된 경우, 메시지, 콘텐츠 블록 및 링크 템플릿은 수정되지 않습니다. 링크 템플릿이나 콘텐츠 블록을 사용하는 기존 메시지는 동일합니다. 그러나 메시지를 업데이트할 때 링크 별칭 마크업이 모든 링크에 적용되므로 링크가 보이도록 링크 템플릿을 다시 적용해야 합니다.

## 링크 별칭 지정을 통한 링크 업데이트 방식

다음 표는 이메일 본문 내 링크 예시, 링크 별칭 지정 결과, 그리고 링크 별칭 지정을 통해 원본 링크가 어떻게 업데이트되는지에 대한 설명을 제공합니다.

### 퍼머링크

**논리:** Braze는 물음표(?)를 삽입하고 URL에 첫 번째 쿼리 매개변수를 추가합니다.

| 이메일 본문의 링크    | 링크 별칭 지정                     |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 추가 쿼리 매개변수가 포함된 링크

**논리:** Braze는 다른 쿼리 매개변수를 감지하고 URL 끝에 `lid=`를 추가합니다.

| 이메일 본문의 링크                                            | 링크 별칭 지정                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML 링크

**논리:** Braze는 링크가 URL임을 인식하며 이미 물음표(?)가 존재하므로, 쿼리 `lid`매개변수는 물음표 뒤에 추가됩니다.

| 이메일 본문의 링크                                                | 링크 별칭 지정                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 앵커와 연결

**논리:** Braze는 URL이 물음표(?) 뒤에 앵커(#)가 있는 표준 구조를 사용할 것으로 예상합니다. Braze는 왼쪽에서 오른쪽으로 읽기 때문에 물음표와`lid`값이 앵커 앞에 추가됩니다.

| 이메일 본문의 링크                               | 링크 별칭 지정                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 앵커 및 캡처 태그와 연결

**논리:** URL에 앵커(#)가 포함된 상태에서 링크 별칭 지정을 사용할 경우, Braze는 앵커가 쿼리 매개변수 뒤에 위치해야 한다고 가정합니다. 이는 정확한 추적을 위해 값이 앵커 **앞에** 추가되어야 함을 의미하며, Braze가 `lid`URL을 왼쪽에서 오른쪽으로 읽기 때문에 물음표(?)와 값은 앵커`lid` 앞에 위치해야 합니다.

| 이메일 본문의 링크                                                                        | 링크 별칭 지정                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 추적 링크 별칭

**링크 관리** 탭에서 세분화 목적으로 "추적"할 별칭과 세분화 필터에 표시할 별칭을 선택합니다. 추적된 별칭은 세분화 목적으로만 사용되며 보고 목적으로 링크가 추적되는 데에는 영향을 미치지 않습니다.

{% alert tip %}
링크 참여 측정기준을 추적하려면 링크가 HTTP 또는 HTTPS로 시작하는지 확인하세요. 특정 링크에 대한 클릭 추적을 끄려면 [유니버설 링크 및 앱 링크를]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis) 참조하세요.
{% endalert %}

Braze는 추적할 수 있는 무제한 링크를 선택할 수 있지만, 사용자가 최근에 연 링크에서만 리타겟할 수 있습니다. 고객 프로필에는 최근에 클릭한 링크 100개가 포함됩니다. 예를 들어, 500개의 링크를 추적하고 사용자가 그 중 500개를 모두 클릭하면, 리타겟하거나 가장 최근에 클릭된 100개의 링크를 기준으로 세그먼트를 만들 수 있습니다.

![두 개의 링크가 선택된 링크 관리 탭.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
Braze는 프로필 수준에서 마지막으로 클릭된 100개의 링크 별칭만 추적합니다.
{% endalert %}

### 액션 기반 필터
 
모든 링크(추적 또는 미추적)를 타겟팅하는 액션 기반 메시지를 만들거나 이메일 캠페인 또는 캔버스 구성 요소에서 별칭을 클릭했는지 여부에 따라 사용자를 리타겟팅할 수 있습니다.

![캔버스 구성 요소에서 별칭을 클릭했거나 캠페인과 상호작용한 사용자를 대상으로 하는 액션 기반 옵션]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### 세분화 필터

Braze에서 이메일 내 링크 별칭이 있고 사용자가 이를 클릭하면, 해당 이벤트가 별칭과 함께 고객 프로필에 기록됩니다.

"캠페인 또는 캔버스 단계에서 클릭된 별칭" 세분화 필터를 사용한 후 해당 링크 별칭의 이름을 변경하기로 결정하면, 고객 프로필의 기존 클릭 데이터는 업데이트되지 **않습니다**. 즉, 여전히 이전 링크 별칭으로 표시됩니다. 따라서 새 링크 별칭을 기준으로 사용자를 타겟팅하는 경우 이전 링크 별칭의 데이터는 포함되지 않습니다.

"캠페인에서 클릭한 별칭" 또는 "캔버스에서 클릭한 별칭" 세분화 필터를 사용하면, 특정 캠페인 또는 캔버스에서 특정 별칭을 클릭했는지 여부에 따라 사용자를 필터링합니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우 링크 별칭을 클릭하면, 해당 이메일 주소를 공유하는 다른 모든 사용자의 고객 프로필이 업데이트됩니다. 

다음 세분화 필터는 이벤트 처리 시점에 추적되는 클릭 이벤트에 적용됩니다. 즉, 추적되지 않은 링크는 기존 데이터를 제거하지 않으며 링크를 추적해도 데이터를 다시 채우지 않습니다. 자세한 내용은 [세분화 필터를]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) 참조하십시오.

#### 링크 추적 해제

링크 추적을 해제해도 필터가 적용된 기존 세그먼트를 추적되지 않는 별칭으로 재배정하지 않습니다. 기존 데이터는 새로운 데이터로 대체될 때까지 고객 프로필에 그대로 유지됩니다. 

보관된 메시지의 링크는 자동으로 추적되지 않습니다. 그러나 보관된 메시지가 보관 해제되면 링크를 다시 추적해야 합니다. 링크 별칭이 추적되면 링크 보고는 최상위 도메인이나 전체 URL 대신 별칭으로 색인됩니다.

이메일 캠페인 내 모든 링크와 해당 링크별 총 클릭 수를 확인하려면 **메시지 분석** > **이메일 성능/성과** > **히트맵 &미리**보기로 이동한 후 **히트맵 표시** 토글을 선택하세요.

![링크 테이블(총 클릭 수) 패널에 링크 별칭과 해당 총 클릭 수를 표시합니다.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### 이메일 클릭 이벤트

커런츠로 참여 데이터를 내보낼 때 링크 별칭 지정이 활성화되어 있으면 이메일 클릭 이벤트가 약간 다르게 처리됩니다. 링크 별칭 지정이 활성화된 경우 [이메일 클릭 ]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/)이벤트에 두 개의 추가 필드가 포함됩니다:`link_id`  와 `link_alias`.

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
캔버스와 캠페인 간의 `dispatch_id` 동작은 다릅니다. Braze는 캔버스 단계(예약할 수 있는 항목 단계 제외)를 "예약"된 경우에도 트리거된 이벤트로 처리하기 때문입니다. 캔버스 및 캠페인에서 [`dispatch_id` 동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)에 대해 자세히 알아보세요.

_2019년 8월에 업데이트가 기록되었습니다._
{% endalert %}

## 콘텐츠 블록의 링크 별칭 지정

새로운 콘텐츠 블록은 링크가 수정되어 Braze가 적용 가능한 경우 각 링크에 `lid={{placeholder}}`를 추가합니다. 이 입력 안내 값은 이메일 메시지 배리언트에 삽입될 때 해결됩니다.

Braze에서 링크 별칭 지정을 활성화하기 전에 생성된 기존 콘텐츠 블록 내의 링크를 수정하려면 기존 콘텐츠 블록을 복제한 다음 복제된 콘텐츠 블록 내의 링크를 수정하십시오.

콘텐츠 블록에 `lid` 값이 없는 경우 새 메시지에 삽입되면 해당 콘텐츠 블록의 링크는 별칭으로 추적되지 않습니다. 새 콘텐츠 블록이 "이전" 메시지 배리언트에 삽입되면, 해당 메시지 배리언트의 링크는 링크 별칭 지정에 의해 인식됩니다. 콘텐츠 블록에서의 링크도 인식됩니다. 그러나 "old" 콘텐츠 블록은 "new" 콘텐츠 블록을 중첩할 수 없습니다.

{% alert tip %}
콘텐츠 블록의 경우 Braze는 새 메시지에서 사용할 기존 콘텐츠 블록의 복사본을 만드는 것을 권장합니다. 이것은 새 메시지에서 링크 별칭 지정이 활성화되지 않은 콘텐츠 블록을 참조할 수 있는 시나리오를 방지하기 위해 대량 복제를 통해 수행할 수 있습니다.
{% endalert %}

## Link aliasing for URLs generated by Liquid

HTML 또는 콘텐츠 블록의 `assign` 문과 같이 Liquid에서 생성한 URL의 경우 Liquid 태그에 물음표(`?`)를 추가해야 합니다. This allows Braze to append query parameters (`lid = somevalue`) so that link aliasing can work properly. Without identifying where to append query parameters, link aliasing will not recognize these URLs and link templates won't apply.

### 예시

권장되는 링크 서식은 이 링크 앨리어싱 예시를 확인하세요:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

링크에 물음표(`?`)가 포함된 매개변수가 있는 경우 앵커 태그에 앰퍼샌드(`&`)로 바꿀 수 있습니다. 다음 예와 같이:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}


