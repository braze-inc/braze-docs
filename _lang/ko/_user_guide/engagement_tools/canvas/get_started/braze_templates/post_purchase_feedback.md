---
nav_title: 구매 후 피드백
article_title: 구매 후 피드백
page_order: 6
page_type: reference
description: "이 문서에서는 Braze 캔버스 템플릿을 사용하여 피드백에 응답하고 사용자와의 관계를 구축할 수 있는 개인화된 경험을 조율하는 방법에 대해 설명합니다."
tool: Canvas
---

# 구매 후 피드백

> 구매 후 피드백 템플릿을 사용하여 고객이 브랜드와 상호 작용하는 방식에 대한 중요한 인사이트를 확보하고 긍정적인 경험을 지속할 수 있도록 하세요. 개인화된 커뮤니케이션과 구조화된 메시지를 활용하면 고객 관계를 지속적으로 구축하고 육성할 수 있습니다.

이 문서에서는 사용자 라이프사이클의 전환 단계를 위해 설계된 **구매 후 피드백** 템플릿의 사용 사례를 안내합니다. 작업을 마치면 사용자가 앱에 대한 피드백을 제공할 수 있는 캔버스를 만들 수 있습니다.

## 필수 조건

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 피드백 설문조사 결과에 참조할 [사용자 지정 속성입니다]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).
- A configured [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) with the partners and audiences you use.

## 필요에 맞게 템플릿 조정하기

모바일 비디오 게임 개발사인 데코룸소프트에서 일한다고 가정해 보겠습니다. 구매 후 피드백 템플릿을 사용하여 최신 비디오 게임 출시작인 프록시 워 3에 대한 피드백을 측정할 것입니다: 갈증의 전쟁. 이 피드백을 바탕으로 확장팩인 Liquid Mirage의 개발 계획에 반영할 예정입니다.

Before creating the Canvas, we set up the [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) integration so that we can add user data from Braze to Google Audiences to send advertisements based on behavioral triggers, segmentation, and more.

구매 후 피드백 템플릿에 액세스하려면 새 캔버스를 만들 때 **캔버스 템플릿 사용** > **브레이즈 템플릿을** 선택합니다. 그런 다음 **구매 후 피드백** 옆의 **템플릿 적용을** 선택합니다. 이제 템플릿을 검토하여 필요에 맞게 조정할 수 있습니다.

### 1단계: 캔버스 세부 정보 설정

목표를 반영하도록 캔버스 세부 사항을 조정해 보겠습니다.

1. 템플릿 이름 옆의 **편집을** 선택합니다.

![캔버스의 현재 제목과 설명입니다.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2\. 캔버스 이름을 업데이트하여 캔버스가 최근 사용자를 타겟팅하도록 지정합니다.
3\. 설명을 업데이트하여 캔버스가 사용자의 피드백 제출을 장려하는 용도로 사용된다는 점을 명시합니다.
4\. Canvas 홈 페이지에서 **피드백** 태그를 추가하여 필터링합니다.

![캔버스의 새 이름과 설명입니다. 새 설명에는 다음과 같이 명시되어 있습니다: '곧 출시될 PWD3 확장팩인 Liquid Mirage에 대한 관심을 측정하기 위한 구매 후 피드백 캔버스입니다.']({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### 2단계: 전환 이벤트 할당

다음으로 전환 이벤트를 할당해 보겠습니다. **기본 전환 이벤트 - A를** **특정 구매로** 업데이트하고 **대리전을** 선택합니다.

!["전환 이벤트 할당" 섹션에서 프록시 전쟁 게임 상품 구매 시 전환 이벤트 유형을 지정할 수 있습니다.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

가장 최근 사용자를 타겟팅하기 위해 템플릿의 전환 기한을 3일로 유지하겠습니다.

### 3단계: 참가 일정 설정

1. 입력 일정 유형을 **작업 기반으로** 유지합니다.
2. 참가 기간의 **시작 시간을** 게임 시작 날짜로 설정합니다.

### 4단계: 캔버스에 참가할 사람 결정

피드백 대상은 최근 프록시 워 3를 구매한 유저입니다.

1. 게임을 구매한 사용자로 구성된 타겟 세그먼트인 '구매한 대리전 3'을 선택합니다.
2. "프록시 워 3"를 "0" 회 이상 구매한 사용자를 포함하려면 필터를 선택합니다.

![게임을 구매한 사용자를 세분화하는 '구매한 대리전 3'이라는 세그먼트.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3\. 캔버스의 최대 지속 시간 이후에는 사용자가 캔버스에 다시 들어갈 수 없도록 항목 컨트롤을 업데이트합니다.

### 5단계: 전송 설정을 선택하세요

기본 구독 설정을 유지하여 구독을 신청했거나 메시지 또는 알림 수신에 동의한 사용자에게만 전송합니다. 

전송에 신중을 기하기 위해 **조용한 시간 사용을** 선택하여 사용자의 시간대인 오후 11시부터 오전 10시 사이에는 피드백을 요청하지 않고 다음 사용 가능한 시간에만 전송합니다.

!['설정 보내기' 단계는 구독 또는 옵트인한 사용자를 대상으로 합니다. 콰이어트 아워가 켜져 있습니다.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

이 예에서는 다른 설정(주파수 제한 및 시드 그룹)은 생략하겠습니다.

### 6단계: 캔버스 사용자 지정

다음으로 사용자에게 전송할 메시지 채널과 콘텐츠를 사용자 지정하여 캔버스를 구축합니다. 이메일, 인앱 메시지 및 웹훅 채널을 통해서만 피드백을 받고 있으므로 템플릿을 살펴보고 메시지 단계에서 SMS 변형을 제거하겠습니다.

각 메시징 구성 요소를 살펴보고 콘텐츠를 업데이트하는 것으로 사용자 지정 작업을 시작하겠습니다. 참조할 사용자 지정 속성은 `Experience Feedback` 입니다.

1. 캔버스 빌더에서 사용자 여정의 첫 번째 메시지 단계를 선택합니다.
2. **이메일** 변형을 선택합니다.
3. 사용자 피드백을 유도할 수 있는 제목으로 **정보 전송을** 작성합니다. 
4. 템플릿의 이메일 메시지를 피드백 설문조사 메시지로 바꾸려면 **메시지 수정을** 선택합니다. 여기에는 사용자 여정의 행동 경로 단계에서 참조할 각 콜투액션의 링크를 교체하여 어떤 옵션이 선택되었는지 캡처하는 것이 포함됩니다.

{% alert tip %}
[캔버스 항목 속성을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) 사용하여 참조하는 제품에 따라 캔버스의 메시지를 사용자 지정할 수 있습니다.
{% endalert %}

#### 피드백 설문조사 설정

다음으로 **인앱 메시지** 변형에 대한 세부 정보를 입력해야 합니다. 여기에서 사용자 피드백의 감성을 나타내는 `Experience Feedback` 사용자 지정 속성을 지정해야 합니다. (이후의 작업 경로 단계에서도 이를 참조할 것입니다.)

1. 동일한 첫 번째 메시지 단계에서 **인앱 메시지** 변형을 선택합니다. 메시지 컨트롤은 그대로 유지합니다. 
2. 헤더와 본문에는 사용자가 프록시 워 3를 사용한 경험에 대해 솔직하게 표현하도록 유도하는 언어를 사용할 것입니다.
3. 설문조사 응답이 프로필과 함께 기록되기를 원하므로 **제출 시** 설문조사를 객관식 **선택** 및 로그 속성으로 유지합니다.
4. 세 가지 설문조사 선택 항목 각각에 대해 사용자 지정 속성으로 **경험 피드백을** 선택합니다. 
5. 사용자 프로필의 속성 값은 사용자 지정 속성과 일치하므로 그대로 유지하겠습니다.

![최근 구매한 프록시 워 3에 대한 만족도를 묻는 설문조사로, 세 가지 옵션이 제공됩니다: "좋았어요", "괜찮았어요", "저한테는 안 맞아요"]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### 액션 경로 구축

사용자 지정 속성 `Experience Feedback` 과 이전 섹션의 속성 값을 사용하여 템플릿의 액션 경로를 속성 및 값과 일치하도록 업데이트합니다.

![설문조사에 '좋아요'라고 응답한 사용자를 포함하는 행동 경로 단계의 '좋은 피드백' 그룹.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### 광고 리타겟팅 설정

**광고 리타겟팅** 단계에서 Google 오디언스 동기화가 설정되어 있는지 확인합니다. 여기에는 광고 계정, 기존 타겟, 타겟에 사용자를 추가하는 옵션을 선택하는 것이 포함됩니다.

### 웹훅 지원 사례 설정하기

다음으로 잠재적인 지원 사례를 트리거하도록 웹훅을 설정해 보겠습니다. 이는 사용자 피드백 분석과 함께 사용하면 특히 유용한 인사이트를 얻을 수 있습니다.

**지원 사례 생성이라는** 이름의 메시지 단계에서는 구매에 불만족하여 환불을 원하는 사용자를 위한 웹훅을 작성하도록 템플릿을 업데이트합니다.

![프록시 워 3 구매에 대해 부정적인 감정을 가지고 환불을 원하는 고객을 위한 지원 사례를 생성하는 웹훅입니다.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### 6단계: 캔버스 테스트 및 실행

캔버스를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 캔버스 **시작을** 선택하여 캔버스를 실행합니다. 이제 개인화된 사용자 여정으로 사용자를 세심하게 타겟팅하여 최근 프록시 워 3 구매를 기반으로 한 피드백 설문조사에 응답하도록 유도할 수 있습니다!

{% alert tip %}
캔버스 출시 전후에 고려해야 할 사항은 [출시 전/후 체크리스트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) 확인하세요.
{% endalert %}
