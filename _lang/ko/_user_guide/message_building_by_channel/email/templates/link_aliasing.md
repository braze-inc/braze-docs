---
nav_title: 링크 별칭 지정
article_title: 링크 별칭 지정
alias: /link_aliasing/
page_order: 3
description: "이 문서는 링크 별칭 지정이 작동하는 방식과 링크가 어떻게 보일지 설명합니다."
channel:
  - email

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}링크 별칭 지정
 
> 링크 별칭 지정을 사용하여 Braze에서 이메일 메시지로 보낸 링크를 식별할 수 있는 인식 가능한 사용자 생성 이름을 만드십시오. 이 링크는 세분화 리타겟팅, 행동 기반 트리거링 및 링크 분석에 사용할 수 있습니다. 링크 별칭 지정은 특정 링크를 클릭한 사용자를 리타겟할 수 있는 기능을 제공하여, 사용자가 특정 별칭 링크를 클릭할 때 행동 기반 트리거를 생성할 수 있게 합니다.

## 링크 별칭 만들기

링크 별칭 지정은 이메일 채널의 링크에 Braze에서 생성된 쿼리 매개변수를 장식하여 작동합니다. 링크 별칭을 만들려면 다음 단계를 따르세요: 

1. 이메일 본문을 여세요.
2. {클릭} **링크 관리** {탭}
3. Braze는 각 링크에 대해 고유한 기본값 링크 별칭을 자동으로 생성합니다.
4. 별칭에 이름을 지정하십시오. 별칭은 이메일 캠페인 배리언트 또는 캔버스 구성 요소마다 고유하게 명명되어야 합니다. 

보고 또는 세분화를 다룰 때 특정 링크를 참조하는 데 사용할 별칭을 설정할 수도 있습니다. 

![][2]

링크 별칭 지정은 쿼리 매개변수를 추가하는 것이 안전한 HTML 앵커 태그의 `href` 속성 내에서만 지원됩니다. 링크 끝에 물음표(?)를 포함하는 것이 좋습니다. 그러면 Braze가 `lid` 값을 쉽게 추가할 수 있습니다. `lid` 값을 추가하지 않으면 Braze는 링크 별칭 지정을 위한 URL을 인식하지 못합니다.

### 링크 별칭 관리

다음 단계를 따라 모든 추적된 링크 별칭을 확인하세요:

1. **설정** > **이메일 환경설정** 아래 **작업 공간 설정**으로 이동합니다.
2. 클릭 **링크 별칭 지정 설정** 탭.

{% alert important %}
[이전 탐색<2>을 사용하는 경우 이러한 설정은 **설정 관리<3> 아래에 있습니다.
{% endalert %}

여기에서 모든 링크 별칭을 정렬하고 검색할 수도 있습니다.

![추적된 링크 별칭 페이지에는 "test"라는 링크 별칭이 표시되며, 이는 캔버스 단계의 활성 부분입니다.][8]

#### 링크 별칭 추적 해제

**링크 별칭 지정 설정** 탭에서 링크 별칭에 대한 추적을 끌 수 있습니다.

1. 링크 별칭을 선택하십시오.
2. 클릭 **추적 끄기**.  

#### 링크 별칭 및 고객 프로필 데이터

Braze에서 앱 또는 웹사이트에 링크 별칭이 있고 사용자가 이를 클릭하면 이벤트가 별칭과 함께 사용자의 프로필에 기록됩니다. 나중에 이 링크 별칭의 이름을 변경하기로 결정하면 고객 프로필의 이전 클릭 데이터가 업데이트되지 않으므로 여전히 이전 링크 별칭으로 표시됩니다. 따라서 새 링크 별칭을 기준으로 사용자를 타겟팅하면 이전 링크 별칭의 데이터를 포함하지 않습니다.

### 워크플로 확인

Braze는 이메일 내 링크를 평가하고 링크 템플릿을 추가하며 세분화 및 보고 목적으로 작동하는 명명 규칙을 제공할 것을 권장합니다. 이것은 모든 링크를 추적하는 데 도움이 됩니다.

링크 별칭 지정이 활성화되면 메시지, 콘텐츠 블록 및 링크 템플릿이 수정되지 않습니다. 링크 템플릿이나 콘텐츠 블록을 사용하는 기존 메시지는 동일합니다. 그러나 메시지를 업데이트할 때 링크 별칭 마크업이 모든 링크에 적용되므로 링크가 보이도록 링크 템플릿을 다시 적용해야 합니다.

### 데이터 추출

캠페인][3] 및 캔버스][4] 엔드포인트에 대한 \[목록 링크 별칭을 사용하여 캠페인 또는 이메일 특정 캔버스 구성 요소의 각 메시지 배리언트에 설정된 `alias`을(를) 추출합니다.

## 콘텐츠 블록에서 링크 별칭 지정

새로운 콘텐츠 블록은 링크가 수정되어 Braze가 적용 가능한 경우 각 링크에 `lid={{placeholder}}`을(를) 추가합니다. 이 입력 안내 값은 이메일 메시지 배리언트에 삽입될 때 해결됩니다.

Braze에서 링크 별칭 지정을 활성화하기 전에 생성된 기존 콘텐츠 블록 내의 링크를 수정하려면 기존 콘텐츠 블록을 복제한 다음 복제된 콘텐츠 블록 내의 링크를 수정하십시오.

콘텐츠 블록에 `lid` 값이 없는 경우 새 메시지에 삽입되면 해당 콘텐츠 블록의 링크는 별칭으로 추적되지 않습니다. 새 콘텐츠 블록이 "이전" 메시지 배리언트에 삽입되면, 해당 메시지 배리언트의 링크는 링크 별칭 지정에 의해 인식됩니다. 콘텐츠 블록에서의 링크도 인식됩니다. 그러나 "old" 콘텐츠 블록은 "new" 콘텐츠 블록을 중첩할 수 없습니다.

{% alert tip %}
콘텐츠 블록의 경우 Braze는 새 메시지에서 사용할 기존 콘텐츠 블록의 복사본을 만드는 것을 권장합니다. 이것은 새 메시지에서 링크 별칭 지정이 활성화되지 않은 콘텐츠 블록을 참조할 수 있는 시나리오를 방지하기 위해 대량 복제를 통해 수행할 수 있습니다.
{% endalert %}

## 예시

다음 표는 이메일 본문에 있는 링크의 예, 링크 별칭 지정 결과 및 원래 링크가 링크 별칭 지정으로 어떻게 업데이트되는지에 대한 설명을 제공합니다.

| 이메일 본문에 링크 | 별칭이 있는 링크 | 논리 |
|---|---|---|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk | Braze는 물음표(?)를 삽입하고 URL에 첫 번째 쿼리 매개변수를 추가합니다. |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Braze는 다른 쿼리 매개변수를 감지하고 URL 끝에 `lid=`을(를) 추가합니다. |
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} | Braze는 이것이 URL이며 이미 물음표(?)가 있음을 인식합니다. 그런 다음 물음표 뒤에 `lid` 쿼리 매개변수를 추가합니다. |
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email | Braze는 URL이 물음표(?) 뒤에 앵커(#)가 있는 표준 구조를 사용할 것으로 예상합니다. Braze는 왼쪽에서 오른쪽으로 읽기 때문에 물음표와 `lid` 값을 앵커 앞에 추가합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Liquid을 통해 생성된 URL에 대한 링크 별칭 지정

HTML 또는 콘텐츠 블록의 `assign` 문에 의해 생성된 URL의 경우 앵커 태그에 물음표(?)를 추가하는 것이 좋습니다. 이것은 Braze가 쿼리 매개변수(`lid = somevalue`)를 추가하여 링크 별칭 지정이 제대로 작동하도록 도와줍니다. 쿼리 매개변수를 추가할 위치를 식별하지 않으면 링크 별칭 지정이 이러한 URL을 인식하지 못합니다.

### 예시

이 링크 별칭 지정 예제를 확인하여 앵커 태그의 권장 형식을 확인하세요:

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

## 링크 템플릿

새 메시지 변형의 경우 기존 [링크 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/)을(를) **링크 관리** 탭에서 사용할 수 있습니다. 링크 템플릿으로 시작된 메시지의 경우 여전히 적용됩니다. 기존 메시지가 수정된 경우 링크 템플릿을 **링크 관리** 탭을 통해 다시 적용해야 합니다. 

{% alert note %}
링크 템플릿은 **링크 관리** 탭에서 볼 수 있는 링크에만 적용할 수 있습니다. 이것은 `lid` URL 매개변수가 없는 링크(예: "이전" 콘텐츠 블록 또는 마크업할 수 없는 링크)가 링크 템플릿에 적합하지 않음을 의미합니다. 이를 해결하려면 "old" 콘텐츠 블록을 복사하거나 URL의 `href` 속성에 물음표(?) 또는 앰퍼샌드(&)를 포함하는 것이 좋습니다.
{% endalert %}

## 링크 세분화

리타겟팅 필터를 사용하면 이메일 캠페인 또는 캔버스 구성 요소에서 특정 추적 별칭을 클릭한 고객을 기반으로 세분화 필터를 만들 수 있습니다. 이 필터는 추적된 별칭이 있는 캠페인 또는 캔버스에서만 사용할 수 있습니다.

### 추적 링크

**링크 관리** 탭에서 세분화 목적으로 "추적"할 별칭과 세분화 필터에 표시할 별칭을 선택합니다. 추적된 별칭은 세분화 목적으로만 사용되며 보고 목적으로 링크가 추적되는 데에는 영향을 미치지 않습니다.

{% alert tip %}
링크 참여 측정기준을 추적하려면 링크가 HTTP 또는 HTTPS로 시작하는지 확인하세요.
{% endalert %}

Braze는 추적할 수 있는 무제한 링크를 선택할 수 있지만, 사용자가 최근에 연 링크에서만 리타겟할 수 있습니다. 사용자 프로필에는 최근에 클릭한 링크 100개가 포함됩니다. 예를 들어, 500개의 링크를 추적하고 사용자가 그 중 500개를 모두 클릭하면, 리타겟하거나 가장 최근에 클릭된 100개의 링크를 기준으로 세그먼트를 만들 수 있습니다.

{% tabs 지역 %}
{% tab 드래그 앤 드롭 편집기 %}

![드래그 앤 드롭 이메일 편집기의 링크 관리 탭.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab HTML 편집기 %}

![HTML 이메일 편집기의 링크 관리 탭.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Braze는 프로필 수준에서 마지막으로 클릭된 100개의 링크 별칭만 추적합니다.
{% endalert %}

### 링크 추적 해제

링크 추적을 해제해도 필터가 있는 기존 세그먼트가 추적 해제된 별칭으로 재할당되지 않습니다. 이전 데이터는 새로운 데이터로 대체될 때까지 사용자 프로필에 남아 있을 것입니다. 다음 세분화 필터는 계속 존재하지만, 해당 필터로 새 세그먼트를 만들 수는 없습니다.

세분화 목적을 위해 기본적으로 작업 공간당 100개의 링크만 추적할 수 있습니다. 보관된 메시지의 링크는 자동으로 추적되지 않습니다. 그러나 보관된 메시지가 보관 해제되면 링크를 다시 추적해야 합니다. 링크 별칭이 추적되면 링크 보고는 최상위 도메인이나 전체 URL 대신 별칭으로 색인됩니다.

![][1]

### 세그먼트 필터

다음 세그먼트 필터는 이벤트가 처리될 때 추적되는 클릭 이벤트에 적용됩니다. 이는 링크 추적을 해제해도 기존 데이터가 제거되지 않으며, 링크를 추적해도 데이터를 백필하지 않는다는 것을 의미합니다.

#### 캠페인에서 별칭 클릭

리타겟 사용자를 클릭한 특정 별칭을 기준으로 캠페인에서 리타겟합니다. 여기에는 추적된 별칭이 있는 캠페인만 반영됩니다.

#### 캔버스 단계에서 별칭 클릭

리타겟 사용자를 특정 별칭을 기반으로 캔버스 구성 요소에서 클릭한 경우. 파이프로 구분된 필터 옵션은 캔버스 및 캔버스 구성 요소를 표시한 다음 캔버스 구성 요소 내의 별칭을 표시합니다. 여기에는 추적된 별칭이 있는 캔버스 단계만 표시됩니다.

#### 캠페인 또는 캔버스에서 별칭 클릭됨

리타겟 users based on any alias that was clicked in the 캠페인 or 캔버스 component. 별칭은 "전역"으로 간주되므로 모든 캠페인 및 캔버스 단계에서 링크 클릭을 대상으로 하는 모든 전역 별칭이 됩니다.

![][5]

### 액션 기반 필터
 
사용자는 추적된 링크든 추적되지 않은 링크든 상관없이 타겟팅하는 액션 기반 메시지를 생성하거나, 이메일 캠페인 또는 캔버스 구성 요소 전반에 걸쳐 별칭을 클릭했는지 여부에 따라 사용자를 리타겟할 수 있습니다. 

![][6]

### 이메일 클릭 이벤트

\[이메일 클릭 이벤트][7]는 사용자가 이메일을 클릭할 때 발생합니다. 사용자가 여러 번 클릭하거나 이메일 내의 다른 링크를 클릭하면 동일한 캠페인에 대해 여러 이벤트가 생성될 수 있습니다. 링크 별칭 지정이 활성화된 경우 이메일 클릭 이벤트에 대해 두 개의 추가 필드가 있습니다: `link_id` 및 `link_alias`.

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
Canvas와 캠페인 간의 `dispatch_id` 동작은 다릅니다. Braze는 Canvas 단계(예약할 수 있는 Entry Steps 제외)를 "예약"된 경우에도 트리거된 이벤트로 처리하기 때문입니다. 캔버스 및 캠페인에서 [`dispatch_id` 동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)에 대해 자세히 알아보세요.

_2019년 8월에 업데이트가 기록되었습니다._
{% endalert %}


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/
[8]: {% image_buster /assets/img/tracked_aliases.png %}