---
nav_title: 전면
article_title: 전면
description: "Front와 Braze를 통합하는 방법 알아보기"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# 전면

> Front의 통합을 통해 각 플랫폼의 웹훅 및 Braze 데이터 변환을 활용하여 양방향 대화형 SMS 파이프라인을 설정할 수 있습니다.

Front에서 들어오는 웹훅에는 실시간 에이전트가 보내는 메시지가 포함된 페이로드가 들어 있습니다. The request will need to be reformatted before it can be accepted by Braze endpoints. Front 데이터 변환 템플릿은 페이로드를 다시 포맷하고 **아웃바운드 SMS 전송**이라는 제목의 고객 프로필에 커스텀 이벤트를 작성합니다. 이때 메시지 본문은 이벤트 속성정보로 전달됩니다.

Braze에서 새 변환을 설정하기 전에 [데이터 변환]({{site.baseurl}}/user_guide/data/data_transformation/overview/) 설명서에서 각 티어에 대한 지원 매트릭스를 검토하는 것이 좋습니다. 무료 및 프로 등급은 매월 다른 수의 활성 변환 및 수신 요청을 제공합니다. 현재 사용 중인 요금제가 사용 사례를 지원할 수 있는지 확인하세요.

## 전제 조건

시작하기 전에 다음이 필요합니다:

| 전제 조건             | 설명                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 프런트 계정            | 이 파트너십을 이용하려면 Front 계정이 필요합니다.|
| Braze 데이터 변환 웹훅 URL | [Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview/) will be used to reformat the incoming webhook from Front so it can be accepted by the Braze /users/track endpoint.|
| 전면 REST API 키         | Front REST API 키는 Braze에서 Front로 아웃바운드 웹훅 요청을 수행하는 데 사용됩니다. |

## 사용 사례

- Streamline your lead generation process using Braze automated SMS messaging to identify user preferences and enable live sales agents to follow up and close sales.
- 자동화된 SMS 응답과 실시간 채팅 지원을 통해 구매 전환을 유도하여 장바구니를 떠난 고객의 재참여를 유도하세요.

## Front 통합

### 1단계: 데이터 변환 만들기

먼저 Braze에서 새로운 데이터 변환을 생성합니다. 다음은 간소화된 단계입니다. 전체 안내는 [변환 생성]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/)을 참조하세요.

1. Braze에서 **데이터 설정** > **데이터 변환**으로 이동한 다음, **변환 생성**을 선택합니다.
2. **환경 편집에서** **처음부터 시작을** 선택합니다.
3. **대상 선택에서** **POST를 선택합니다: 사용자 추적**.
4. 다음 변환 템플릿을 복사하여 붙여넣은 다음 엔드포인트를 저장하고 활성화합니다.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    변환은 다음과 유사합니다.

    ![데이터 변환 예시.]({% image_buster /assets/img/front/data_transformation.png %})

{% alert tip %}
특정 요구 사항에 맞게 이 템플릿을 수정할 수 있습니다. 예를 들어 미리 설정된 사용자 지정 이벤트 이름을 사용자 지정할 수 있습니다. 자세한 내용은 [데이터 변환 개요]({{site.baseurl}}/user_guide/data/data_transformation/overview/)를 참조하세요.
{% endalert %}

### 2단계: 아웃바운드 SMS 캠페인 만들기

다음으로, Front에서 웹훅을 수신 대기하는 SMS 캠페인과 고객에 대한 커스텀 SMS 응답을 생성합니다.

#### 2.1단계: 메시지 작성

**메시지** 텍스트 상자에 옵트아웃 언어 또는 기타 정적 콘텐츠와 함께 다음 Liquid 코드를 추가합니다.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

메시지는 다음과 비슷해야 합니다:

![Liquid 코드를 사용한 메시지 예시.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 배송 예약하기

배달 유형에서 **작업 기반 배달을** 선택한 다음 사용자 지정 이벤트 트리거에서 **아웃바운드 SMS 전송을** 선택합니다.

!['배송 예약' 페이지]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
이 사용자 지정 이벤트는 사용자 프로필에 기록하는 데이터 변환입니다. 에이전트 메시지는 이 이벤트의 이벤트 속성정보로 저장됩니다.
{% endalert %}

마지막으로, **전달 제어**에서 재적격성을 활성화합니다.

!['전달 제어'에서 활성화된 재적격성.]({% image_buster /assets/img/front/braze_reeligibility.png %})

### 3단계: 사용자 지정 채널 만들기

전면 대시보드에서 **설정** > **채널** > **채널 추가로** 이동한 다음 **사용자 지정 채널을** 선택하고 새 Braze 채널의 이름을 입력합니다.

![전면 대시보드의 Braze용 맞춤 채널.]({% image_buster /assets/img/front/front_custom_channel.png %})

### 4단계: 설정 구성

아웃바운드 API 엔드포인트 필드에 [앞서 생성한](#step-1-set-up-a-data-transformation-in-braze) 데이터 변환 웹훅 URL을 입력합니다. 새 Braze 채널에서 실시간 상담원이 보내는 모든 아웃바운드 메시지는 여기로 전송됩니다. 또한 이 채널은 **수신 URL** 필드에 Braze가 SMS 메시지를 전달할 수 있는 엔드포인트 URL을 제공합니다.

나중에 필요할 수 있으니 이 URL을 메모해 두세요.

![전면에 새로 생성된 Braze 채널의 채널 설정]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### 5단계: 인바운드-SMS 전달 설정

다음으로, 고객의 인바운드 SMS를 Front의 받은 편지함으로 전달할 수 있도록 Braze에서 두 개의 새 웹훅 캠페인을 생성합니다.

|숫자|목적|
|---|---|
|웹훅 캠페인 1|프론트에 라이브 채팅 대화가 요청되고 있다는 신호를 보냅니다.|
|웹훅 캠페인 2|고객의 인바운드에서 보낸 모든 대화형 SMS 응답을 Front의 받은 편지함으로 전달합니다.|
{: .reset-td-br-1 .reset-td-br-2 }

#### 5.1단계: SMS 키워드 카테고리 만들기

Braze 대시보드에서 **오디언스**로 이동하고 **SMS 구독 그룹**을 선택한 다음, **커스텀 키워드 추가**를 선택합니다. Front에 대한 전용 SMS 키워드 카테고리를 만들려면 다음 필드를 입력합니다.

|필드|설명|
|---|---|
|키워드 카테고리|키워드 카테고리의 이름(예: `FrontSMS1`).|
|키워드|사용자 지정 키워드(예: `TIMETOMOW`. 우발적인 트리거를 방지하기 위해 자주 사용하는 단어는 피하세요. 키워드는 대소문자를 구분하지 않으므로 `lawn` 은 `LAWN` 과 일치합니다.|
|회신 메시지|'조경사가 곧 연락을 드릴 것입니다.'와 같이 키워드가 감지되면 전송되는 메시지.|
{: .reset-td-br-1 .reset-td-br-2 }

![Braze의 SMS 키워드 카테고리 예시]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### 5.2단계: 첫 번째 웹훅 캠페인 만들기

Braze 대시보드에서 [이전에 생성](#step-3-configure-the-settings-for-your-new-custom-braze-channel)한 URL을 사용하여 첫 번째 웹훅 캠페인을 생성합니다.

![Braze에서 생성해야 하는 첫 번째 웹훅 캠페인의 예시입니다.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

요청 본문에 다음을 추가합니다:

{% raw %}
```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

설정 탭에서 `Authorization`, `content-type`, `accept` 요청 헤더를 구성합니다.

![세 가지 필수 헤더가 포함된 요청 예시.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### 5.3단계: 첫 번째 배송 예약하기

**예약 전달**의 경우 **실행 기반 전달**을 선택한 다음, 트리거 유형으로 **SMS 인바운드 메시지 전송**을 선택합니다. 또한 [이전에 설정한](#step-51-create-an-sms-keyword-category) SMS 구독 그룹 및 키워드 카테고리를 추가합니다.

![첫 번째 웹훅 캠페인의 '전송 예약' 페이지]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

**배달 관리에서** 재적격성을 활성화합니다.

![첫 번째 웹훅 캠페인의 '전달 제어'에서 선택한 재적격성.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### 5.4단계: 두 번째 웹훅 캠페인 만들기

두 번째 웹훅 캠페인은 첫 번째 캠페인과 일치하므로 [첫 번째 캠페인을 복제하고 이름을 변경]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns)할 수 있습니다. 지금 이 작업을 수행합니다.

#### 5.5단계: 두 번째 배송 예약하기

**예약 전달**의 경우 **실행 기반 트리거** 및 **SMS 구독 그룹**을 [첫 번째 전달](#step-53-schedule-the-first-delivery)과 동일하게 설정합니다. 그러나 **키워드 카테고리**의 경우 **기타**를 선택합니다.

!['기타'를 키워드 카테고리로 선택한 두 번째 웹훅 캠페인의 '예약 배송' 페이지.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### 5.6단계: 대상 필터 추가

이제 웹훅 캠페인에서 고객의 인바운드 SMS 응답을 전달할 수 있습니다. 실시간 채팅에 대한 메시지만 전달되도록 SMS 응답을 필터링하려면 **특정 캠페인에서 마지막으로 수신한 메시지** 세분화 필터를 **타겟 오디언스 단계**에 추가합니다

!['특정 캠페인에서 마지막으로 수신한 메시지'가 선택된 오디언스 필터]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

그런 다음, 필터를 구성합니다.

1. **캠페인에서** [이전에 생성한](#step-2-create-an-outbound-sms-campaign) SMS 캠페인을 선택합니다.
2. **연산자**에서 **미만**을 선택합니다.
3. **기간**에서 고객의 응답 없이 채팅이 열려 있어야 하는 시간을 선택합니다.

![선택한 대상 필터의 구성 설정입니다.]({% image_buster /assets/img/front/front_target_audience.png %})

## 고려 사항

### 청구 가능한 세그먼트

- Braze의 SMS 메시지는 메시지 세그먼트당 요금이 부과됩니다. 메시지 요금 청구 방식을 이해하려면 세그먼트를 정의하는 요소와 이러한 메시지가 분할되는 방식을 이해해야 합니다. 자세한 내용은 [설명서를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments) 참조하세요.
- 상담원 응답 시간이 길어지면 청구 가능한 세그먼트가 더 많이 소모됩니다.

### 데이터 포인트 소비

현재 이 통합을 사용하려면 실시간 에이전트가 Front에서 SMS를 보낼 때마다 고객 프로필에 커스텀 이벤트를 기록해야 합니다. 몇 개의 메시지만 주고받는 짧은 대화에 적합할 수 있지만, 대화가 길어질수록 데이터 포인트에 미치는 영향도 커집니다. 데이터 포인트는 Braze에 기록된 각 사용자 지정 이벤트에 대해 소비됩니다.

### SMS 메시지에 링크 포함

프론트 라이브 채팅에서 링크를 보내면 추가 HTML 태그와 함께 렌더링됩니다.

### 전면에서 이미지 파일 첨부

앞쪽의 이미지 파일은 Braze에서 보낸 SMS 메시지에서 렌더링되지 않습니다.

### 옵트아웃 

대화형 메시지에는 모호한 옵트아웃으로 간주할 수 있는 '중지' 또는 이와 유사한 어휘가 포함될 위험이 높습니다.
