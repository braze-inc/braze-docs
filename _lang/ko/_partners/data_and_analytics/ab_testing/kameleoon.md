---
nav_title: 카멜레온
article_title: 카멜레온
description: "Kameleoon과 Braze를 통합하는 방법 알아보기"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# 카멜레온

>[Kameleoon은](https://www.kameleoon.com) 하나의 통합 플랫폼에서 실험, AI 기반 개인화 및 기능 관리 기능을 갖춘 최적화 솔루션입니다.

## 필수 조건

Before you start, you'll need the following:

| Requirement | 설명 |  
| --- | --- |  
| 카멜레온 계정 | 이 파트너십을 이용하려면 카멜레온 계정이 필요합니다.|  
| Braze account| An active Braze account with the [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrated on your webpage. 이벤트 속성정보 세분화도 인에이블먼트해야 합니다. 요청하려면 [고려 사항을](#considerations) 참조하세요.|  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## 사용 사례

Kameleoon은 실험 및 개인화 캠페인에 참여하는 사용자를 식별할 수 있는 커스텀 이벤트를 Braze에 전송하여 보다 정확한 타겟팅과 개인화된 메시징을 가능하게 합니다.

## 카멜레온 통합하기

이 통합은 카멜레온의 engine.js 을 통해 자바스크립트 트래커로 실행됩니다. 카멜레온 플랫폼 내에서 빠르게 인에이블먼트할 수 있습니다.

### 1단계: 카멜레온 통합 페이지로 이동하기

Kameleoon 앱의 사이드바에서 **관리자를** 선택한 다음 **통합을** 선택합니다.

![카멜레온 플랫폼의 관리자 패널입니다.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### 2단계: Braze 도구 설치하기

기본값으로 Braze 도구는 설치되어 있지 않습니다. Braze 아이콘을 찾은 다음 **도구 설치를** 선택합니다. ![아래쪽을 가리키는 화살표가 있는 회색 사각형입니다.]({% image_buster /assets/img/kameleoon/img_2.png %})

Braze 도구를 활성화할 프로젝트를 선택하면 Kameleoon 데이터가 Braze에 올바르게 보고됩니다.

![Kameloon의 Braze 도구 아이콘.]({% image_buster /assets/img/kameleoon/img_3.png %})

도구를 구성한 후 **유효성 검사를** 선택하면 구성 패널이 닫힙니다. 그러면 도구가 설정된 프로젝트 수와 함께 Braze 도구 아이콘 옆에 **켜짐** 토글이 표시됩니다.

![Braze 도구가 Kameleoon에서 "켜짐"으로 토글되었습니다.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}  
이 기능은 베타 버전입니다. [카멜레온 베타 프로그램에](https://help.kameleoon.com/account-and-team-management/join-beta-program/) 가입하여 이 통합 기능을 사용해 보세요.  
{% endalert %}  
    
### 3단계: Braze와 카멜레온 캠페인 연계하기

#### 그래픽/코드 편집기에서

실험을 완료하려면 **통합** 단계를 선택하여 추적 도구로 Braze를 구성한 다음 **Braze를** 선택합니다.

![Kameleoon의 통합 대시보드에는 활성 통합인 Braze를 포함하여 사용 가능한 모든 통합이 표시됩니다.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze는 라이브 시작 전 요약에 언급될 예정입니다. Kameleoon은 자동으로 데이터를 Braze로 전송하고, 사용자는 이를 Braze에서 바로 분석 및 세그먼트화에 사용할 수 있습니다.

##### 개인화 생성

**개인화 생성** 페이지에서 리포팅 도구 중 Braze를 선택하여 리포팅을 개인화할 수 있습니다.

![보고 도구 섹션에 Braze가 선택된 상태에서 Heap, Mixpanel, Clarity와 같은 통합 기능이 표시됩니다.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### 기능 플래그 생성

**통합** 섹션의 기능 플래그 환경에서 통합을 설정합니다. 활성화하려는 환경에 맞게 인에이블먼트하세요.

![카멜레온의 기능 플래그 페이지와 사용 가능한 통합 기능. 각 파트너에게는 '전달 규칙'과 '기능 실험'이라는 두 가지 스위치가 있습니다.]({% image_buster /assets/img/kameleoon/img_7.png %})

##### 결과 페이지

실험의 보고 도구로 Braze를 설정한 후에는 **실험 구성** 메뉴의 Kameleoon 결과 페이지에서 이를 선택(또는 선택 해제)할 수 있습니다.

{% alert note %}  
이 통합은 [하이브리드 구현이](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) 필요하며 웹 SDK와만 호환됩니다.
{% endalert %}

![카멜레온의 결과 페이지 측면 패널입니다.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

실험과 관련된 보고 도구가 표시됩니다. **편집을** 선택하여 이 선택 항목을 편집합니다.

### 4단계: Braze에서 카멜레온 데이터 분석 및 활용하기

통합이 설정되면 Kameleoon은 **실험 이름**, **실험 ID**, **변형 이름**, **변형 ID와** 같은 속성이 포함된 `kameleoon_exposure` 이라는 커스텀 이벤트를 Braze에 전송합니다.

![Braze의 커스텀 이벤트 사용자 로그, Kameleoon에서 받은 이벤트의 페이로드 예시를 보여줍니다.]({% image_buster /assets/img/kameleoon/img_9.png %})

그런 다음 커스텀 이벤트에서 이 데이터를 보고, 커스텀 이벤트 보고서를 생성하여 캠페인 노출을 식별하고, 이벤트 속성정보를 기반으로 세그먼트를 세분화할 수 있습니다. [행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [행동 기반 트리거를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) 통해 후속 또는 연결된 캠페인과 캔버스를 만들거나 [세그먼트를]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) 만들 때 커스텀 이벤트를 사용할 수 있습니다.

또한 이러한 이벤트는 [커런츠 커스텀 이벤트 오브젝트를]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) 통해 액세스하여 종합적인 보고 및 분석을 할 수 있습니다.

## 고려 사항

### Request event property segmentation

Before you can use event property segmentation, you'll need it enabled in Braze. Use the following template to contact your Braze CSM or the support team for access.

   <table>
   <thead>
      <tr>
         <th>Field</th>
         <th>Details</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Subject</strong></td>
         <td>카멜레온 통합을 위한 이벤트 속성정보 세분화 인에이블먼트 요청하기</td>
      </tr>
      <tr>
         <td><strong>Body</strong></td>
         <td>
         Hello Braze Team,<br><br>
         Kameleoon&lt;>Braze 통합에서 전송된 이벤트에 대해 이벤트 속성정보를 세분화할 수 있도록 하고 싶습니다. Here are the details:<br><br>
         - <strong>Event Name:</strong> 카멜레온<br>
         - <strong>Event Properties:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Braze data points

세분화를 위해 인에이블된 이벤트 속성정보를 포함하여 Kameleoon에서 Braze로 전송된 커스텀 이벤트는 Braze 인스턴스에 데이터 포인트를 기록합니다.