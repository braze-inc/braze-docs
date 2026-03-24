---
nav_title: 컨텍스트 
article_title: 컨텍스트 
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "이 참조 문서에서는 캔버스에서 컨텍스트 단계를 만들고 사용하는 방법에 대해 설명합니다."
tool: Canvas

---

# 컨텍스트

> 컨텍스트 단계를 사용하면 사용자가 캔버스를 이동할 때 하나 이상의 변수를 생성하고 업데이트할 수 있습니다. 예를 들어, 시즌별 할인을 관리하는 캔버스가 있는 경우 컨텍스트 변수를 사용하여 사용자가 캔버스에 진입할 때마다 다른 할인 코드를 저장할 수 있습니다.

## 작동 방식

![캔버스의 첫 번째 단계인 컨텍스트 단계입니다.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

컨텍스트 단계를 사용하면 사용자가 특정 캔버스를 이동하는 동안 임시 데이터를 생성하고 사용할 수 있습니다. 이 데이터는 해당 캔버스 여정 내에서만 존재하며 다른 캔버스나 세션 외부에서는 유지되지 않습니다.

컨텍스트 변수는 해당 특정 캔버스 여정에서만 존재합니다. 사용자 프로필을 영구적으로 변경하지 않으며 다른 캔버스에는 표시되지 않습니다. 따라서 특정 캠페인이나 워크플로에만 관련된 임시 정보에 이상적입니다.

{% alert tip %}
컨텍스트 변수에 대한 전체 참조(데이터 유형, 사용법 및 모범 사례 포함)는 [컨텍스트 변수 참조]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/)를 확인하세요.
{% endalert %}

컨텍스트 단계 내에서 최대 10개의 컨텍스트 변수를 정의하거나 업데이트할 수 있습니다. 이러한 변수를 활용하여 지연 시간을 개인화하고, 사용자를 동적으로 세그먼트하며, 캔버스 전반에 걸쳐 메시징을 풍부하게 할 수 있습니다. 예를 들어, 사용자의 예약된 비행 시간에 대한 컨텍스트 변수를 생성한 다음, 이를 활용하여 개인화된 지연 시간을 설정하고 알림을 보낼 수 있습니다.

컨텍스트 변수는 두 가지 방법으로 설정할 수 있습니다:

- **캔버스 진입 시:** 이벤트 또는 API 트리거의 데이터가 컨텍스트 변수를 자동으로 채울 수 있습니다.
- **컨텍스트 단계에서:** 컨텍스트 단계를 추가하여 컨텍스트 변수를 수동으로 정의하거나 업데이트합니다.

각 컨텍스트 변수에는 이름, 데이터 유형 및 값(Liquid 또는 개인화 추가 도구를 사용하여 설정)이 필요합니다. 정의된 후에는 {% raw %}`{{context.${flight_time}}}`{% endraw %}와 같이 Liquid를 사용하여 캔버스 전체에서 컨텍스트 변수를 참조할 수 있습니다. **컨텍스트 변수 이름** 필드에서 컨텍스트 변수 이름을 직접 입력하거나 단계 편집기의 드롭다운에서 선택할 수도 있습니다. 자세한 내용은 [컨텍스트 변수 참조]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/)를 확인하세요.

각 캔버스 진입은 최신 진입 데이터와 캔버스 설정을 기반으로 컨텍스트 변수를 재정의하여, 사용자가 각자 고유한 컨텍스트를 가진 여러 활성 여정을 동시에 진행할 수 있도록 합니다. 예를 들어, 고객에게 두 개의 예정된 항공편이 있다면, 두 개의 별도 여정 상태가 동시에 실행됩니다&#8212;각 상태는 출발 시간 및 목적지와 같은 항공편별 컨텍스트 변수를 각각 보유합니다. 이를 통해 고객의 뉴욕행 오후 2시 비행편에 대한 개인화된 알림을 보내는 동시에, 내일 로스앤젤레스행 오전 8시 비행편에 대한 별도의 업데이트를 전송할 수 있어 각 메시지가 특정 예약 내용과 관련성을 유지합니다.

### 사용자 처리 및 일괄 처리

컨텍스트 단계는 성능 최적화를 위해 사용자를 배치 단위로 처리합니다. 사용자가 컨텍스트 단계에 진입하면 Braze는 기본적으로 1,000명 단위로 배치 처리합니다. 이 배치들은 병렬로 처리되지만, 각 배치 내에서는 사용자가 순차적으로 처리됩니다.

구체적으로 다음과 같습니다:

**예시**: 3,500명의 사용자가 사용자당 650ms가 소요되는 연결된 콘텐츠가 포함된 컨텍스트 단계에 진입할 경우:
- Braze는 4개의 사용자 배치(이 예시에서는 1,000명, 1,000명, 1,000명, 500명)를 생성합니다.
- 각 배치는 사용자를 순차적으로 처리하므로, 1,000명의 사용자 배치는 약 10.8분(650초; 1,000 × 650ms)이 소요됩니다.
- 배치는 각기 다른 시간에 완료되므로, 사용자는 자신의 배치가 완료되는 대로 다음 단계로 조금씩 이동합니다.
- 배치 크기 및 연결된 콘텐츠 응답 시간에 따라 초기 사용자는 마지막 사용자보다 몇 분 먼저 다음 단계에 도달할 수 있습니다.

연결된 콘텐츠가 없으면 외부 API 호출을 기다릴 필요가 없기 때문에 컨텍스트 단계 처리가 훨씬 빠르게 진행됩니다.

## 고려 사항

- 각 컨텍스트 단계당 최대 10개의 컨텍스트 변수를 정의할 수 있습니다.
- 각 변수에는 고유한 이름이 필요합니다(문자, 숫자, 밑줄만 사용 가능, 최대 100자).
- 한 단계 내 모든 변수의 총 크기는 50KB를 초과할 수 없습니다.
- API 트리거를 통해 전달된 변수는 컨텍스트 단계에서 생성된 변수와 동일한 네임스페이스를 공유합니다. 컨텍스트 단계에서 변수를 재정의하면 API 값이 덮어쓰기됩니다.

자세한 내용과 고급 사용법은 [컨텍스트 변수 참조]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/)를 확인하세요.

## 컨텍스트 단계 만들기

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### 1단계: 단계 추가

캔버스에 단계를 추가한 다음 사이드바에서 구성요소를 끌어다 놓거나 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택하고 **컨텍스트**를 선택합니다.

### 2단계: 변수 정의

{% alert note %}
각 컨텍스트 단계에 대해 최대 10개의 컨텍스트 변수를 정의할 수 있습니다.
{% endalert %}

컨텍스트 변수를 정의하려면:

1. 컨텍스트 변수에 **이름**을 지정합니다.
2. [데이터 유형]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types)을 선택합니다.
3. Liquid 표현식을 수동으로 작성하거나 **개인화 추가**를 사용하여 기존 속성에서 Liquid 스니펫을 만듭니다.
4. **미리보기**를 선택하여 컨텍스트 변수 값을 확인합니다.
5. (선택 사항) 추가 변수를 추가하려면 **컨텍스트 변수 추가**를 선택하고 1~4단계를 반복합니다.
6. 완료했으면 **완료**를 선택합니다.

이제 메시지 및 사용자 업데이트 단계 등 Liquid를 사용하는 모든 곳에서 **개인화 추가**를 선택하여 컨텍스트 변수를 사용할 수 있습니다. **컨텍스트 변수 이름** 필드에서 컨텍스트 변수 이름을 직접 입력하거나 단계 편집기의 드롭다운에서 선택할 수도 있습니다. 전체 사용법은 [컨텍스트 변수 참조]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/)를 확인하세요.

{% alert important %}
컨텍스트 변수를 참조할 때는 항상 {% raw %}`{{context.${variable_name}}}`{% endraw %} 형식을 사용하세요.
{% endalert %}

### 컨텍스트 변수 필터

[오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) 및 [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) 단계에서 컨텍스트 변수를 사용하여 필터를 생성할 수 있습니다. 필터 설정, 비교 로직 및 고급 예제에 대해서는 [컨텍스트 변수 참조]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters)를 확인하세요.

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## 사용자 경로 미리보기

메시지가 올바른 오디언스에게 전송되고 컨텍스트 변수가 예상된 결과로 평가되는지 확인하기 위해 [사용자 경로를 미리보기]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths)하고 테스트하는 것을 권장합니다.

{% alert note %}
편집기의 **미리보기 및 테스트 발송** 섹션에서 캔버스를 미리 보는 경우, 테스트 메시지 미리보기의 타임스탬프는 UTC로 표준화되지 **않습니다**. 이 패널은 미리보기를 문자열로 생성하기 때문입니다. 이는 캔버스가 `time` 오브젝트를 수신하도록 설정된 경우, 메시지 미리보기가 캔버스가 실제로 실행될 때의 결과를 정확히 보여주지 않음을 의미합니다. 캔버스를 가장 정확하게 테스트하려면 사용자 경로 미리보기를 사용하는 것을 권장합니다.
{% endalert %}

잘못된 컨텍스트 변수를 생성하는 일반적인 시나리오를 반드시 확인하세요. 사용자 경로를 미리 볼 때 컨텍스트 변수를 사용한 개인화된 지연 단계의 결과와, 사용자를 컨텍스트 변수와 매칭하는 모든 오디언스 또는 결정 단계 비교를 확인할 수 있습니다.

컨텍스트 변수가 유효하면 캔버스 전체에서 해당 변수를 참조할 수 있습니다. 그러나 컨텍스트 변수가 올바르게 생성되지 않았다면, 캔버스의 이후 단계들도 제대로 수행되지 않습니다. 예를 들어, 사용자에게 약속 시간을 할당하는 컨텍스트 단계를 생성하고 약속 시간 값을 과거 날짜로 설정하면, 메시지 단계의 리마인더 이메일이 발송되지 않습니다.

## 연결된 콘텐츠 문자열을 JSON으로 변환하기

컨텍스트 단계에서 [연결된 콘텐츠 호출]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call)을 수행할 때, 호출에서 반환된 JSON은 일관성 유지 및 오류 방지를 위해 문자열 데이터 유형으로 평가됩니다. 이 문자열을 JSON으로 변환하려면 `as_json_string`을 사용합니다. 예를 들어:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## 문제 해결

### 잘못된 컨텍스트 변수

컨텍스트 변수는 다음과 같은 경우 유효하지 않은 것으로 간주됩니다:

- 임베디드 연결된 콘텐츠에 대한 호출이 실패한 경우
- 런타임에 Liquid 표현식이 데이터 유형과 일치하지 않거나 비어 있는(null) 값을 반환하는 경우

예를 들어 컨텍스트 변수 데이터 유형이 **숫자**이지만 Liquid 표현식이 문자열을 반환하는 경우 유효하지 않습니다.

이런 상황에서는:
- 사용자는 다음 단계로 진행합니다.
- 캔버스 단계 분석에서 이를 _업데이트되지 않음_으로 집계합니다.

문제를 해결할 때 _업데이트되지 않음_ 측정기준을 모니터링하여 컨텍스트 변수가 올바르게 업데이트되고 있는지 확인하세요. 컨텍스트 변수가 유효하지 않은 경우 사용자는 컨텍스트 단계를 지나 캔버스에서 계속 진행할 수 있지만, 이후 단계에서는 자격을 얻지 못할 수 있습니다.

각 데이터 유형에 대한 예제 설정은 [데이터 유형]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types)을 참조하세요.

### 연결된 콘텐츠 발송 지연

배치 내 모든 사용자가 처리된 후에야 사용자가 다음 단계로 진행됩니다. 배치 처리가 완료되면 성공한 사용자는 다음 단계로 진행하고, 실패한 사용자는 별도로 재시도됩니다—성공한 사용자는 재시도가 완료될 때까지 기다리지 않고 바로 다음 단계로 넘어갑니다.

**재시도 동작**: 컨텍스트 단계(및 모든 캔버스 단계)는 표준 연결된 콘텐츠 재시도 동작이 아닌 캔버스 전용 재시도 메커니즘을 사용합니다. 연결된 콘텐츠 호출이 실패할 경우, Braze는 지수 백오프 방식으로 해당 단계를 약 13회 재시도합니다. 모든 재시도가 실패하면 사용자는 캔버스를 종료합니다.

{% alert note %}
표준 연결된 콘텐츠에서 사용되는 `:retry` 태그는 캔버스 단계 내에서 수행되는 연결된 콘텐츠 호출에는 적용되지 않습니다. 캔버스 단계는 캔버스 워크플로에 최적화된 자체 재시도 로직을 갖추고 있습니다.
{% endalert %}

**처리 시간**: 컨텍스트 단계를 통해 모든 사용자를 처리하는 데 걸리는 시간은 다음에 따라 달라집니다:
- 단계에 진입하는 사용자 수
- 연결된 콘텐츠 사용 여부(및 응답 시간)
- 배치 크기(기본값: 배치당 1,000명)

연결된 콘텐츠 엔드포인트에 사용량 제한이 있는 경우, 컨텍스트 단계가 각 배치 내에서 사용자를 순차적으로 처리하므로 사용량 제한을 자연스럽게 준수하는 데 도움이 됩니다. 그러나 여러 배치가 병렬로 처리되므로, 엔드포인트가 여러 배치에서 동시에 발생하는 요청을 처리할 수 있는지 확인해야 합니다.

## 시간대 일관성 표준화

캔버스 컨텍스트가 정식 출시됨에 따라, 액션 기반 캔버스의 모든 기본 타임스탬프 이벤트 등록정보가 UTC로 설정됩니다. 이 변경 사항은 캔버스 단계 및 메시지 편집 시 보다 예측 가능하고 일관된 경험을 보장하기 위한 광범위한 노력의 일환입니다. 이 변경 사항은 특정 캔버스가 컨텍스트 단계를 사용하든 그렇지 않든, 모든 액션 기반 캔버스에 영향을 미칩니다.

{% alert important %}
모든 상황에서, 원하는 시간대로 타임스탬프를 표시하려면 [Liquid time_zone 필터]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)를 사용하는 것을 강력히 권장합니다. 예시는 이 [자주 묻는 질문](#faq-example)을 참고하세요.
{% endalert %}

## 자주 묻는 질문

### 캔버스 컨텍스트가 정식 출시된 이후 무엇이 바뀌었나요?

캔버스 컨텍스트가 정식 출시됨에 따라 다음 세부 사항이 적용됩니다:

- 액션 기반 캔버스의 [트리거 이벤트 등록정보]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)에 있는 [datetime 유형]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties)의 모든 타임스탬프는 [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) 기준입니다.
- 이 변경 사항은 특정 캔버스가 컨텍스트 단계를 사용하든 그렇지 않든, 모든 액션 기반 캔버스에 영향을 미칩니다.

#### 이러한 변경의 이유는 무엇인가요?

이 변경 사항은 캔버스 단계 및 메시지 편집 시 보다 예측 가능하고 일관된 경험을 제공하기 위한 광범위한 노력의 일환입니다.

#### API로 트리거되거나 스케줄된 캔버스는 이 변경 사항의 영향을 받나요?

아니요.

#### 이 변경 사항이 캔버스 진입 등록정보에 영향을 미치나요?

예, `canvas_entry_property`가 액션 기반 캔버스에서 사용 중이며 등록정보 유형이 `time`인 경우 `canvas_entry_properties`에 영향을 미칩니다. 모든 상황에서, 원하는 시간대로 타임스탬프를 표시하려면 Liquid `time_zone` 필터를 사용하는 것을 권장합니다.

다음은 이를 수행하는 방법의 예시입니다:

| 메시지 단계의 Liquid | 출력 | Liquid에서 시간대를 올바르게 표현하는 방법인가요? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | 아니요 |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | 아니요
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | 예 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 새로운 타임스탬프 동작이 메시지에 어떤 영향을 미칠 수 있는지에 대한 실제 사례는 무엇인가요? {#faq-example}

메시지 단계에 다음과 같은 내용이 포함된 액션 기반 캔버스가 있다고 가정해 보겠습니다:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

다음과 같은 메시지가 표시됩니다: 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Liquid를 사용해 시간대를 지정하지 않았으므로, 여기서의 타임스탬프는 UTC 기준입니다. 

시간대를 명확하게 지정하려면 다음과 같이 Liquid `time_zone` 필터를 사용할 수 있습니다: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

다음과 같은 메시지가 표시됩니다: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

America/Los Angeles 시간대가 Liquid를 사용하여 지정되었으므로, 여기서의 타임스탬프는 PST입니다.

선호하는 시간대는 이벤트 등록정보 페이로드로 전송하여 Liquid 로직에서 사용할 수도 있습니다:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### 컨텍스트 변수는 캔버스 진입 등록정보와 어떻게 다른가요?

캔버스 진입 등록정보는 캔버스 컨텍스트 변수로 포함됩니다. 즉, Braze API를 사용하여 캔버스 진입 등록정보를 전송하고 다른 단계에서 참조할 수 있으며, 이는 Liquid 스니펫으로 컨텍스트 변수를 사용하는 것과 유사합니다.

### 단일 컨텍스트 단계에서 변수가 서로를 참조할 수 있나요?

예. 컨텍스트 단계의 모든 변수는 순차적으로 평가되므로, 다음과 같은 컨텍스트 변수를 설정할 수 있습니다:

| 컨텍스트 변수 | 값 | 설명 |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | 사용자가 가장 좋아하는 요리 유형입니다. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | 사용자에게 제공되는 할인 코드입니다. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | 이전 변수를 결합한 개인화된 메시지입니다. 메시지 단계에서 Liquid 스니펫 {% raw %}`{{context.${personalized_message}}}`{% endraw %}을 사용하여 컨텍스트 변수를 참조하여 각 사용자에게 개인화된 메시지를 전달할 수 있습니다. 컨텍스트 단계를 사용하여 [프로모션 코드]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) 값을 저장하고, 캔버스 내 다른 단계에서 이를 템플릿으로 활용할 수도 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

이는 여러 컨텍스트 단계에도 적용됩니다. 예를 들어 다음 시퀀스를 생각해 보세요:

1. 초기 컨텍스트 단계에서 `job_title` 값으로 `JobInfo`라는 변수를 만듭니다.
2. 메시지 단계에서 {% raw %}`{{context.${JobInfo}}}`{% endraw %}를 참조하고 사용자에게 `job_title`을 표시합니다.
3. 이후 컨텍스트 단계에서 컨텍스트 변수를 업데이트하여 `JobInfo`의 값을 `job_description`으로 변경합니다.
4. `JobInfo`를 참조하는 모든 후속 단계는 이제 업데이트된 값 `job_description`을 사용합니다.

컨텍스트 변수는 캔버스 전체에서 가장 최근 값을 사용하며, 업데이트할 때마다 해당 변수를 참조하는 모든 이후 단계에 영향을 줍니다.