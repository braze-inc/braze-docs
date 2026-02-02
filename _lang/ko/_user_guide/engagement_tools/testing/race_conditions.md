---
nav_title: 경합 조건
article_title: 경합 조건
alias: /race_conditions/
page_order: 9
page_type: reference
description: "이 문서에서는 경합 조건이 메시징 캠페인에 영향을 미치지 않도록 하는 모범 사례를 다룹니다."
toc_headers: h2
---

# 경합 조건

> A race condition occurs when an outcome depends on the sequence or timing of multiple events. For example, if the desired sequence of events is “Event A” then “Event B”, but sometimes “Event A” comes first, and other times “Event B” comes first—that is known as a race condition. This can lead to unexpected results or errors because these events compete to access shared resources or data.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

In Braze, race conditions can occur when multiple actions are triggered at the same time based on user data or events. For example, if a user triggers multiple campaigns (like signing up for a newsletter or making a purchase), they may not receive the messages in the correct order.

## Types of race conditions

The most common types of race conditions may occur when you’re doing the following:

- 신규 사용자 타겟팅
- 여러 API 엔드포인트 사용
- Matching action-based trigger and audience filters. 

Consider the following scenarios and implement best practices to avoid these race conditions.

## Scenario 1: 신규 사용자 타겟팅

Braze에서 가장 일반적인 경합 조건 중 하나는 새로 생성된 사용자를 대상으로 하는 메시지에서 발생합니다. The expected order of events is:

1. 사용자가 생성됩니다;
2. 동일한 사용자가 즉시 메시지 타겟팅, 커스텀 이벤트 수행 또는 커스텀 속성 로깅을 수행합니다.

그러나 경우에 따라 두 번째 이벤트가 먼저 트리거되기도 합니다. This means a message is attempting to be sent to a user that doesn’t exist yet. As a result, the user never receives it. This also applies to events or attributes, where the event or attribute attempts to be logged to a user profile that hasn’t been created yet.

### Best practices

#### Introduce delays

After a new user is created, you can add a delay before sending any targeted campaigns or Canvases. This timing delay allows the user profile to be created and for any relevant attributes to be updated that may determine their eligibility for receiving the message.

For example, after a user registers for your app, you can send a promotional offer after 24 hours. Or, if you're creating a user or logging a custom attribute, you can add a one-minute delay before proceeding in your process to avoid this race condition.

새 사용자가 캔버스에 입장하도록 트리거하는 특정 사용자 지정 이벤트에 대해 [Braze SDK에서]({{site.baseurl}}/developer_guide/sdk_integration) 이 지연 시간을 추가할 수도 있습니다. 

## Scenario 2: 여러 API 엔드포인트 사용

{% alert important %}
비동기 처리를 사용하여 속도와 유연성을 극대화합니다. 즉, API 호출이 개별적으로 전송될 경우 전송된 순서대로 처리된다는 보장을 할 수 없습니다.
{% endalert %}

다음과 같이 여러 API 엔드포인트에서 이 경합 조건이 발생할 수 있는 몇 가지 시나리오가 있습니다.

- 별도의 API 엔드포인트를 사용하여 사용자 생성 및 캔버스 또는 캠페인 트리거하기
- 커스텀 속성, 이벤트 또는 구매를 업데이트하기 위해 `/users/track` 엔드포인트를 여러 번 개별적으로 호출하기

When user information is sent to Braze using the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track), it may occasionally take a few seconds to process. 즉, `/users/track` 와 `/campaign/trigger/send` 과 같은 메시징 엔드포인트에 동시에 요청이 이루어질 경우 메시지가 전송되기 전에 사용자 정보가 업데이트된다는 보장이 없습니다.

{% alert note %}
사용자 속성과 이벤트가 동일한 요청( `/users/track` 또는 소프트웨어 개발 키트에서)으로 전송되는 경우, Braze는 이벤트 또는 메시지 전송을 시도하기 전에 속성을 먼저 처리합니다.
{% endalert %}

### Best practices

#### When using multiple endpoints, send your requests one at a time

If you’re using multiple endpoints, you can try staggering your requests so that each request is completed before the next one starts. This can reduce the chance of a race condition. For example, if you need to update user attributes and send a message, first wait for the user profile to be updated completely before sending a message using an endpoint.

If you're sending a scheduled message API request, these requests must be separate, and a user must be created before sending the scheduled API request.

#### Include key data with the trigger

Instead of using multiple endpoints, you can include the [user attributes]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) and [trigger properties]({{site.baseurl}}/api/objects_filters/trigger_properties_object) in a single API call using the [`campaign/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). 

이러한 객체가 트리거에 포함되면 메시지가 트리거되기 전에 속성이 먼저 처리되어 잠재적인 경합 조건이 제거됩니다. Note that trigger properties don't update the user profile, but are used in the context of the message only.

#### Use the POST: Track users (sync) endpoint

Use the [`/users/track/sync/` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous) to record custom events and purchases and update user profile attributes synchronously. Using this endpoint to update user profiles at the same time and in a single call can help prevent potential race conditions.

{% alert important %}
This endpoint is currently in beta. Contact your Braze account manager if you’re interested in participating in the beta.
{% endalert %}

## Scenario 3: 액션 기반 트리거와 대상 필터 매칭하기

또 다른 일반적인 경쟁 조건은 오디언스 필터와 동일한 트리거(예: 변경된 속성 또는 사용자 지정 이벤트 수행)로 액션 기반 캠페인 또는 캔버스를 구성하는 경우 발생할 수 있습니다. The user may not be in the audience at the time they perform the trigger event, which means they won’t receive the campaign or enter the Canvas.

### Best practices

#### Check your audience after a delay

To avoid using audience filters that contain the trigger criteria, we recommend checking your audience before delivery. For example, you can [use delivery validations]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#edit-delivery-settings) in Canvas Message steps as an additional check to confirm your audience meets the delivery criteria at message send. You can also leverage exit criteria for Canvas to exit any users at any point during the user journey if they meet your criteria.

For campaigns, you can use exit events to allow campaigns with a trigger event to abort messages to users who perform the exit event while in the delay.

#### Use unique filters with the trigger event

As you configure your filters, you may want to add a redundant filter “just in case”. However, this redundancy may lead to more issues. Instead, avoid using any filter that contains the trigger when possible. This is the safest route to avoid a race condition.

For example, if your campaign trigger is “Has made a purchase” and your audience filter is “Has made any purchase”, this redundancy can cause a race condition. 

#### Avoid audience filters that assume the trigger event has been updated

This best practice is similar to avoiding redundant filters with the trigger event. 일반적으로 트리거 이벤트가 고객 프로필에 업데이트된다고 가정하는 필터는 실패합니다.

#### Use Liquid aborts (attributes only)

In campaigns and Canvas steps, use Liquid aborts to avoid using audience filters that contain the trigger attributes at the entry schedule. For example, let’s say you have an array attribute “favorite colors” and want to target any user who updates the attribute array with any value, and also has the color “blue” in the array after the update has completed. If you use the audience filters in this example, you’ll encounter a race condition and miss users adding “blue” in the array for the first time.

In this case, you can implement a trigger delay in a campaign or use a Delay step in Canvas to allow the user profile to update for a period of time, then use the following Liquid abort logic:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### 사용자 데이터 관리 방법 확인

캔버스 응모 평가 중 경합 조건이 있는 경우, 사용자가 응모하지 않아야 할 캔버스에 응모할 수 있습니다. 예를 들어, 사용자의 프로필을 오디언스에 포함되도록 설정한 다음 캔버스에서 사용자가 더 이상 오디언스에 포함되지 않도록 대기열에 추가한 후에 업데이트할 수 있습니다. 

사용자가 같은 초 내에 캔버스 입력 이벤트를 여러 번 트리거하는 경우, Braze는 해당 초에 한 번의 입력만 허용합니다(재입력이 인에이블먼트된 경우에도). 이렇게 하면 중복 항목을 방지할 수 있으므로 총 캔버스 항목 수가 총 트리거 이벤트 수보다 적을 수 있습니다.

사용자 데이터가 어떻게 관리되고 업데이트되는지, 특히 특정 속성이 언제 어떻게 업데이트되는지(예: 소프트웨어 개발 키트, API, 배치 API 및 기타 방법)를 확인하는 것이 좋습니다. 이를 통해 사용자가 캠페인이나 캔버스에 들어온 이유와 사용자 프로필이 업데이트된 시점을 식별하고 명확하게 파악할 수 있습니다.
