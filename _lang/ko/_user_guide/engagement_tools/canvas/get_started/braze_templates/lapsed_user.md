---
nav_title: 이탈한 사용자
article_title: 휴면 사용자
page_order: 4
page_type: reference
description: "이 문서에서는 사용자가 과거의 참여를 기반으로 한 인센티브로 앱으로 돌아오도록 유도하기 위해 Braze Canvas 템플릿을 사용하는 방법을 설명합니다."
tool: Canvas
---

# 이탈한 사용자

> 이탈한 사용자 템플릿을 사용하여 사용자에게 브랜드가 제공하는 가치를 상기시키고, 과거의 참여를 기반으로 한 흥미로운 제안과 인센티브로 그들의 복귀를 유도합니다.

이 문서는 사용자 생애 주기의 유지 및 로열티 단계에 맞춰 설계된 **이탈한 사용자** 템플릿의 사용 사례를 안내합니다. 작업이 완료되면, 사용자의 행동에 따라 프로모션을 통해 앱으로 돌아오도록 유도하는 Canvas를 생성하게 됩니다. 예를 들어, 사용자가 프로모션 메시지를 받은 후 앱에서 세션을 시작했는지 여부에 따라 다릅니다.

## 필수 조건

To successfully use the lapsed user template, you need to configure [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) with the partners and audiences you use.

## 필요에 맞게 템플릿 조정하기

영화와 쇼에 대한 독점 콘텐츠를 제공하는 스트리밍 서비스인 MovieCanon을 위해 작업하고 있다고 가정해 보겠습니다. 30일 동안 우리 앱을 방문하지 않은 사용자에게 혜택과 프리미엄 콘텐츠를 홍보하기 위해 이탈한 사용자 템플릿을 사용할 수 있습니다.

Before creating the Canvas, we set up the [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) integration so that we can add user data from Braze to Google Audiences to send advertisements based on behavioral triggers, segmentation, and more.

이탈한 사용자 템플릿에 접근하려면, 새 Canvas를 만들 때 **Canvas 템플릿 사용** > **Braze 템플릿**을 선택합니다. 그런 다음, **이탈한 사용자** 옆에서 **템플릿 적용**을 선택합니다. 이제 템플릿을 검토하여 필요에 맞게 조정할 수 있습니다.

### 1단계: 세부 정보 설정 

목표를 반영하도록 캔버스 세부 사항을 조정해 보겠습니다.

1. 템플릿 이름 옆의 **편집을** 선택합니다.

![Canvas의 현재 제목과 설명입니다.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Canvas 이름을 업데이트하여 이 Canvas가 프로모션으로 사용자에게 메시지를 보내고 세션을 시작하는 사용자에 대한 오디언스 동기화를 수행할 것임을 명시합니다.
3\. 이 Canvas가 혜택과 프로모션을 포함하고 있음을 설명하기 위해 설명을 업데이트합니다.
4\. 이 Canvas를 Canvas 홈 페이지에서 필터링할 수 있도록 **이탈/유지** 태그를 추가합니다.

!["Canvas 세부정보 설정" 단계에서 Canvas 이름을 "이탈한 사용자 - 앱 방문"으로 하고 간단한 Canvas 설명을 추가합니다.]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### 2단계: 전환 이벤트를 할당합니다.

**주요 전환 이벤트 - A**를 우리 앱(MovieCanon)의 사용자 대상으로 업데이트하고, **주요 전환 이벤트 - B**는 기본값인 모든 구매로 남겨둡니다.

!["전환 이벤트 할당" 섹션에서 특정 앱에서 사용자가 세션을 시작하는 주요 전환 이벤트를 설정합니다.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### 3단계: 참가 일정 맞춤 설정

입력 일정을 **예약됨**으로 유지하고 기본 시간 기반 옵션을 유지하여 Canvas가 매일 이탈한 사용자를 확인하도록 합니다.

이 단계에서 두 가지 조정을 하겠습니다: 

1. 시작 날짜와 시간을 선택합니다.
2. **특정 날짜에** 종료 매개변수를 선택하고 두 달 후의 날짜를 선택합니다. 다른 이탈 사용자 캔버스를 시작한다고 가정해 보겠습니다.

!["입장 일정" 단계는 지정된 시간에 사용자를 초대하는 예약된 캔버스입니다.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### 4단계: 대상 청중을 선택합니다.

입장 청중에 대한 기본 설정을 유지하겠습니다. 이는 30일 이상 우리 앱을 사용하지 않은 사용자로 설정되어 있습니다. 사용자가 4주 후에 캔버스에 다시 들어올 수 있도록 기본 입장 제어도 유지하겠습니다. 이는 사용자가 30일 이상 우리 앱을 방문하지 않을 때마다 캔버스에 들어간다는 것을 의미합니다.

!["대상 청중" 단계는 마지막으로 앱을 사용한 지 30일이 지난 사용자를 대상으로 합니다.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### 5단계: 전송 설정을 선택하세요

대부분의 기본 구독 설정을 유지하겠습니다:

- 메시지나 알림을 수신하기 위해 구독하거나 선택한 사용자에게만 전송합니다.
- 우리 청중이 받는 메시지 수에 압도되지 않도록 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) 규칙을 적용합니다. 이 경우, 사용자가 받을 수 있는 "이탈/유지"로 태그된 캠페인이나 캔버스 단계의 수를 매주 두 개로 제한하도록 최대 게재빈도 설정을 합니다.
- 사용자의 현지 시간(오전 12시부터 오전 8시까지) 동안 방해금지 시간에 메시지를 전송하지 마십시오.

우리가 변경할 유일한 설정은 방해금지 시간 동안 메시지가 트리거될 때의 처리 방법입니다. 메시지를 취소하는 대신, 사용자가 프로모션을 놓치지 않도록 **다음 가능한 시간에 전송**을 선택합니다.

!["방해금지 시간" 섹션은 시작 시간이 오전 12시이고 종료 시간이 오전 8시입니다.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### 6단계: 캔버스 사용자 지정

이제 템플릿 단계를 사용자 정의하여 캔버스를 구축하겠습니다:

1. 30일 이상 우리 앱을 방문하지 않은 모든 사용자에게 전송될 첫 번째 이메일을 사용자 정의합니다. 우리 사용 사례에 맞춰, 오늘 우리 앱을 방문하면 새로운 혜택을 잠금 해제할 것이라는 내용을 담은 이메일을 사용자 정의합니다. 

![오늘 방문하면 새로운 혜택을 잠금 해제하라는 내용을 담은 이메일의 캔버스 메시지 단계입니다.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2\. 우리 앱을 선택하여 "세션 시작?"라는 행동 경로 구성 요소를 사용자 정의합니다. 

![특정 앱에서 시작된 세션에 대한 행동 경로입니다.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3\. “세션?”이라는 이름의 결정 분할 단계에 대한 기본값을 유지하세요. 이는 지난 캘린더 하루 동안 우리 앱을 한 번 이상 사용한 사용자들을 “>1 세션” 그룹으로 정의합니다.
4\. “>1 세션” 그룹에 속하는 사용자들을 위해 메시지 단계를 사용자화하세요. 우리의 사용 사례에서는, 사용자들에게 우리 앱을 방문해 주셔서 감사하다고 전하고 그들이 잠금 해제한 혜택을 강조할 것입니다.
5\. 첫 번째 이메일을 받은 후 여러 세션을 가진 사용자들의 사용자 데이터를 업데이트하고 동기화할 수 있도록 광고 오디언스 업데이트 단계에서 Google 오디언스 동기화가 설정되어 있는지 확인하세요.
6\. “A/B 테스트”라는 이름의 [실험 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) 구성 요소에 대한 기본값을 유지하세요. 이것은 두 세션 미만을 가진 사용자들에게 (다음 단계에서 사용자화할) 두 가지 프로모션 중 하나를 무작위로 전송할 것입니다.
7\. 실험 경로의 일환으로 사용자에게 전송될 두 가지 프로모션을 사용자화하세요. 우리의 사용 사례에서는, 하나는 3개월 구독에 대한 20% 프로모션이고 다른 하나는 1개월 구독에 대한 10% 프로모션으로 만들 것입니다.

![사용자가 가진 세션 수에 따라 분기 경로가 있는 캔버스 단계입니다.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### 7단계: 캔버스를 테스트하고 출시하세요.

캔버스를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **캔버스 시작을** 선택하여 캔버스를 실행합니다. 이제 30일 이상 우리 앱을 방문하지 않았고 메시징 채널에 구독한 사용자들은 돌아오도록 유도하는 이메일을 받을 것입니다!

{% alert tip %}
캔버스 출시 전후에 고려해야 할 사항은 [출시 전/후 체크리스트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) 확인하세요.
{% endalert %}

