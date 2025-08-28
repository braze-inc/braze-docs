---
nav_title: 휴면 사용자
article_title: 휴면 사용자
page_order: 4
page_type: reference
description: "이 기사는 사용자가 과거 참여를 기반으로 한 인센티브로 앱으로 돌아오게 하는 Braze Canvas 템플릿을 사용하는 방법을 설명합니다."
tool: Canvas
---

# 사용자 이탈

> 사용자가 브랜드가 제공하는 가치를 상기시키고, 과거의 참여를 기반으로 한 흥미로운 제안과 인센티브로 그들의 복귀를 장려하기 위해 소멸된 사용자 템플릿을 사용하세요.

이 기사는 사용 사례를 통해 사용자의 생애 주기에서 유지 및 로열티 단계에 맞게 설계된 Lapsed User 템플릿을 안내합니다. 완료되면 사용자가 프로모션에 따라 앱으로 돌아오도록 유도하는 캔버스를 생성하게 됩니다. 프로모션은 사용자가 프로모션 메시지를 받은 후 앱에서 세션을 시작했는지 여부와 같은 행동에 따라 달라집니다.

## 필수 조건

To successfully use the lapsed user template, you need to configure [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) with the partners and audiences you use.

## 귀하의 필요에 맞게 템플릿을 조정하기

영화와 쇼에 대한 독점 콘텐츠를 제공하는 스트리밍 서비스인 MovieCanon을 위해 일하고 있다고 가정해 보겠습니다. 우리는 30일 동안 우리 앱을 방문하지 않은 사용자에게 혜택과 프리미엄 콘텐츠를 홍보하기 위해 이탈 사용자 템플릿을 사용할 수 있습니다.

Before creating the Canvas, we set up the [Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) integration so that we can add user data from Braze to Google Audiences to send advertisements based on behavioral triggers, segmentation, and more.

새 캔버스를 만들 때, 만료되는 사용자 템플릿에 접근하려면 캔버스 템플릿 사용 > 브레이즈 템플릿을 선택하세요. 그런 다음, Lapsing User 옆에서 Apply Template을 선택합니다. 이제 우리는 템플릿을 살펴보고 우리의 필요에 맞게 조정할 수 있습니다.

### 1단계: 세부 사항 설정 

목표를 반영하기 위해 캔버스 세부정보를 조정합시다.

1. 템플릿 이름 옆의 편집을 선택하세요.

현재 캔버스의 제목과 설명.

{:start="2"}
2\. 캔버스 이름을 업데이트하여 이 캔버스가 프로모션으로 사용자에게 메시지를 보내고 세션을 시작하는 사람들과 오디언스 동기화를 수행할 것임을 명시합니다.
3\. 설명을 업데이트하여 이 캔버스에 특전과 프로모션이 포함되어 있음을 설명합니다.
4\. Lapsing/Retention 태그를 추가하여 캔버스 홈 페이지에서 이 캔버스를 필터링할 수 있도록 하세요.

!["Set Up Canvas Details" step with Canvas name of "Lapsed User - Visit App" and a brief Canvas description]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### 2단계: 전환 이벤트를 할당하세요

**주요 전환 이벤트 - A**를 우리 앱(MovieCanon)의 사용자 대상으로 업데이트하고, **주요 전환 이벤트 - B**는 기본값인 모든 구매로 남겨둡니다.

!["Assign Conversion Events" section with a primary conversion even of a user starting a session in a specific app.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### 3단계: 입회 일정을 조정하다

입장 일정을 예정된 대로 유지하고 기본값 시간 기반 옵션을 설정하여 캔버스가 매일 사용자의 경과를 확인하도록 합시다.

이 단계에 두 가지 조정을 하겠습니다: 

1. 시작 날짜와 시간을 선택하세요.
2. 특정 날짜와 두 달 후의 날짜의 종료 매개변수를 선택하십시오. 다른 이탈 사용자 캔버스가 있다고 가정해 보겠습니다. 이 캔버스가 끝난 후 시작하고 싶습니다.

!["Entry Schedule" step for a scheduled Canvas that enters users at a designated time.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### 4단계: 우리의 목표 오디언스를 선택하세요

우리는 30일 이상 우리 앱을 사용하지 않은 사용자로 설정된 기본값 설정을 유지할 것입니다. 우리는 또한 사용자가 4주 후에 캔버스에 다시 들어갈 수 있도록 기본값 입력 제어를 유지할 것입니다. 이것은 사용자가 30일 이상 연속으로 우리 앱을 방문하지 않을 때마다 그들이 캔버스에 들어간다는 것을 의미합니다.

!["Target Audience" step targeting users who last used the apps in 30 days.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### 5단계: 전송 설정을 선택하세요

기본값 구독 설정의 대부분을 유지할 것입니다:

- 구독하거나 메시지 또는 알림 수신에 동의한 사용자에게만 전송하십시오.
- 우리의 최대 게재빈도 설정 규칙을 적용하여 오디언스가 받는 메시지의 수에 압도되지 않도록 하십시오. 이 경우, 우리는 사용자가 매주 두 개의 "Lapsing/Retention"으로 태그된 캠페인 또는 캔버스 단계를 받을 수 있도록 최대 게재빈도를 설정합니다.
- 사용자의 현지 시간(오전 12시부터 오전 8시까지) 동안 방해금지 시간에 메시지를 보내지 마십시오.

우리가 변경할 유일한 설정은 방해금지 시간 동안 메시지가 발생할 때 무엇을 할지입니다. 메시지를 취소하는 대신, 다음 가능한 시간에 보내기를 선택하여 우리 사용자들이 어떤 프로모션도 놓치지 않도록 하세요.

!["Quiet Hours" section with a start time of 12 am and end time of 8 am.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### 6단계: 당신의 캔버스를 사용자 정의하세요

이제 템플릿 단계들을 사용자 정의하여 우리의 캔버스를 구축할 것입니다:

1. 모든 사용자가 30일 이상 우리 앱을 방문하지 않은 경우에 보낼 첫 번째 이메일을 사용자 정의하세요. 우리의 사용 사례를 위해, 우리는 사용자에게 오늘 우리 앱을 방문하면 새로운 혜택을 잠금 해제할 것이라는 내용을 담은 이메일을 맞춤 설정할 것입니다. 

![Canvas Message step for an email that tells users to unlock new perks when they visit today.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2\. "Start Session?"라는 행동 경로 구성 요소를 시작된 세션 경로에 대해 우리의 앱을 선택하여 사용자 정의하십시오. 

![Action path for sessions that are started in a specific app.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3\. "Sessions?"라는 결정 분할 단계의 기본값을 유지하세요. 이는 지난 캘린더 일에 우리 앱을 한 번 이상 사용한 사용자들을 ">1 Session" 그룹으로 정의합니다.
4\. 사용자가 “>1 세션” 그룹에 속하는 경우 메시지 단계를 사용자 정의하십시오. 우리의 사용 사례에서, 우리는 사용자에게 우리의 앱을 방문해 주셔서 감사하고 그들이 잠금 해제한 혜택을 강조할 것입니다.
5\. Google 오디언스 동기화가 광고 오디언스 업데이트 단계에서 설정되어 있는지 확인하여, 첫 번째 이메일을 받은 후 여러 세션을 가진 사용자들의 사용자 데이터를 업데이트하고 동기화합니다.
6\. "A/B Test"라는 실험 경로 구성 요소의 기본값을 유지하십시오. 이것은 두 개의 프로모션 중 하나(다음 단계에서 사용자 정의할 예정)를 세션이 두 개 미만인 사용자에게 무작위로 전송합니다.
7\. 사용자에게 실험 경로의 일환으로 전송될 두 가지 프로모션을 사용자 정의하십시오. 우리의 사용 사례에서, 우리는 하나는 3개월 구독에 대한 20% 프로모션으로 만들고, 다른 하나는 1개월 구독에 대한 10% 프로모션으로 만들 것입니다.

![Canvas steps with branching paths based on how many sessions a user had.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### 7단계: 테스트하고 캔버스를 시작하세요.

캔버스를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **캔버스 시작을** 선택하여 캔버스를 실행합니다. 이제 30일 이상 우리 앱을 방문하지 않은 사용자와 메시징 채널에 가입한 사용자에게 돌아오도록 권장하는 이메일이 발송됩니다!

{% alert tip %}
캔버스 출시 전후에 고려해야 할 사항에 대한 체크리스트를 확인하세요.
{% endalert %}

