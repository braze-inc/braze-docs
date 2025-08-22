---
nav_title: 워크스페이스
article_title: "시작하기: 워크스페이스"
page_order: 3
page_type: reference
description: "Braze 플랫폼에서 하는 모든 작업은 작업 공간 내에서 이루어집니다. 이 문서에서는 이러한 기능의 작동 방식과 Braze에서 워크스페이스를 계획할 때 염두에 두어야 할 중요한 고려 사항에 대해 설명합니다."
---

# 시작하기: 워크스페이스

Braze 플랫폼에서 하는 모든 작업은 작업 공간 내에서 이루어집니다. 워크스페이스는 별도의 데이터 사일로 역할을 하며, 서로 다른 브랜드나 활동을 분리하여 보관할 수 있습니다. 웹사이트 또는 모바일 앱의 여러 버전에서 동일한 워크스페이스로 데이터를 전송할 수 있습니다. 워크스페이스 내에서 수집되는 다양한 사이트와 앱을 "앱 인스턴스"라고 합니다.

## 작업 공간 이해

작업 공간은 두 가지 주요 용도로 사용됩니다:

- **사용자 데이터 통합:** 여러 앱 인스턴스가 하나의 워크스페이스에 있는 경우 iOS, Android, 웹 등 다양한 버전의 앱에서 사용자 데이터를 원활하게 수집하고 타겟팅할 수 있습니다. 이렇게 하면 사용 중인 플랫폼에 관계없이 각 사용자에 대한 최신 정보를 항상 확보할 수 있습니다.
- **별개의 활동을 분리합니다.** 또한 워크스페이스는 브랜드나 활동을 분리할 수 있는 수단을 제공합니다. 예를 들어 사용자 기반이 다른 여러 개의 하위 브랜드가 있는 경우 각각에 대해 별도의 워크스페이스를 만드는 것이 좋습니다.

{% alert tip %}
This approach is particularly useful for companies like mobile gaming firms that can manage individual workspaces for each of their games or eCommerce sites that want separate workspaces for each region they operate in.
{% endalert %}

## 워크스페이스 계획

각 플랫폼에서 앱의 각 버전에 대해 별도의 앱 인스턴스를 생성해야 합니다. 워크스페이스에 포함할 앱 인스턴스를 결정할 때는 타겟팅하려는 사용자를 생각하고 그에 따라 그룹화하세요.

하나의 워크스페이스에서 여러 앱 인스턴스를 사용할 수 있다는 점은 전체 앱 포트폴리오에 대한 메시징 제한을 평가할 수 있다는 점에서 매력적일 수 있습니다. 하지만 하나의 워크스페이스에 서로 다른 버전의 동일한(또는 매우 유사한) 앱만 함께 배치하는 것이 가장 좋습니다.

### 공유 워크스페이스

동일한 워크스페이스에 여러 앱 인스턴스를 포함하려는 경우의 일반적인 예:

- 여러 플랫폼에 걸쳐 거의 동일한 앱이 여러 개 있는 경우
- 앱의 주요 수정 사항이 다르지만 업그레이드할 때 동일한 사용자를 계속 참여시키려는 경우
- 동일한 사용자가 다른 버전의 앱으로 이동하거나 이동할 수 있는 경우(예: 무료에서 프리미엄으로 전환)

#### 세분화 필터에 미치는 영향

하나의 워크스페이스에 어떤 앱을 선택하든 해당 앱의 데이터가 집계됩니다. 이는 Braze의 다음 세분화 필터에 주목할 만한 영향을 미칩니다(전체 목록은 아닙니다).

- 마지막으로 사용한 앱
- 처음 사용한 앱
- 세션 수
- 앱 내에서 지출한 금액
- 푸시 구독(사용자가 한 앱에서 구독을 취소하면 워크스페이스의 모든 앱에서 구독이 취소되는 올 오어 논 상황이 됩니다.)
- 이메일 구독(이는 전부 아니면 올 오어 논이 되어 규정 준수 문제에 노출될 수 있습니다.)

{% alert note %}
이러한 필터에서 앱 인스턴스 전반의 데이터를 집계하기 때문에 동일한 워크스페이스 내에 상당히 다른 앱을 배치하는 것은 권장하지 않습니다. 타겟팅이 까다로워질 수 있습니다!
{% endalert %}

### 별도의 작업 공간

다른 경우에는 여러 개의 개별 워크스페이스를 사용하고 싶을 수도 있습니다. 일반적인 예는 다음과 같습니다:

- 동일한 앱의 개발 환경과 프로덕션 환경을 위한 별도의 작업 공간 분리
- 여러 하위 브랜드, 예를 들어 여러 게임을 제공하는 모바일 게임 회사의 경우
- 동일한 앱 또는 웹사이트를 다른 국가에서 운영하거나 다른 언어를 대상으로 하는 다른 로컬라이제이션

### 중요 고려 사항

워크스페이스는 별도의 데이터 사일로 역할을 한다는 점을 기억하세요. 사용자 데이터든 마케팅 자산이든 모든 데이터는 워크스페이스 내에 저장됩니다. 이 데이터는 해당 작업 공간 외부에서 쉽게 공유할 수 없습니다. 

다음은 워크스페이스 내에서 구성되는 모든 주요 요소입니다:

- [앱 인스턴스](#app-instances)
- [Teams](#teams)
- [Braze 사용자 권한](#braze-user-permissions) (Braze 사용자 제외)
- [전류 커넥터](#currents-connectors)
- [사용자 프로필](#user-profiles) 및 관련 사용자 데이터
- [세그먼트, 캠페인 및 캔버스](#segments-campaigns-and-canvases)

#### 앱 인스턴스

각 플랫폼에서 앱의 각 버전에 대해 별도의 앱 인스턴스를 생성해야 합니다. 예를 들어 iOS와 Android 모두에 무료 및 프로 버전의 앱이 있는 경우 워크스페이스 내에 4개의 앱 인스턴스(무료 iOS 앱, 무료 Android 앱, 프로 iOS 앱, 프로 Android 앱)를 생성합니다. 이렇게 하면 각 앱 인스턴스에 대해 하나씩 사용할 수 있는 4개의 API 키가 제공됩니다.

#### Teams

[Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) can be set up across customer base location, language, and custom attributes so that team members and non-team members have different access to messaging features and customer data.

#### Braze 사용자 권한

워크스페이스에는 독립적인 액세스 및 사용자 권한 정의가 있습니다. [User permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) allow you to create granular controls regarding what an individual dashboard user or team has access to within a single workspace.

#### 전류 커넥터

The [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) tool is a real-time data stream of your engagement events that is the most robust yet granular export out of the Braze platform. 커런츠 커넥터는 특정 Braze 패키지에 포함되어 있으며, 단일 워크스페이스를 가정할 때 처음에 받았을 수도 있습니다.

별도의 워크스페이스를 만들지 아니면 결합된 워크스페이스를 만들지 결정할 때는 커런츠 커넥터는 워크스페이스 간에 공유되지 않으므로 보유하고 있는 커런츠 커넥터의 수를 고려하는 것이 중요합니다. 

예를 들어 동일한 앱의 개발 환경과 프로덕션 환경을 위한 별도의 작업 공간이 있는 경우 프로덕션 작업 공간에서 커런츠 커넥터를 활성화하세요. 두 워크스페이스 모두에서 커런츠를 사용하려면 커런트 커넥터를 추가로 구매해야 합니다.

#### 사용자 프로필

All persistent data associated with a user is stored in their [user profile]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). 그러나 사용자 프로필은 사용자의 참여 기록, 세그먼트 멤버십, 디바이스 및 운영 체제에 대한 정보에 쉽게 액세스할 수 있으므로 문제 해결 및 테스트에 유용한 리소스이기도 합니다.

#### 세그먼트, 캠페인 및 캔버스

세그먼트, 캠페인 또는 캔버스는 다른 워크스페이스에 저장된 데이터를 참조하거나 액세스할 수 없습니다. 반대로 여러 앱이 동일한 워크스페이스에 있는 경우 모든 앱의 데이터가 집계됩니다. 이는 [Braze의 필터에 영향을](#impact-on-segmentation-filters) 미칩니다.

### 각 접근 방식에 대한 개요

다음 표에서는 워크스페이스 계획에 대한 이 두 가지 접근 방식의 장점과 단점을 설명합니다:

- **작업 공간과 사용자 프로필을 분리하세요:** 하나의 워크스페이스에는 하나의 앱 인스턴스가 있고 한 사람은 해당 앱 인스턴스에 대해 하나의 고객 프로필을 갖습니다.
- **공유 작업 공간 및 사용자 프로필:** 하나의 워크스페이스에 여러 개의 앱 인스턴스가 있고 한 사람이 모든 앱 인스턴스에 대해 하나의 고객 프로필을 갖습니다.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
</style>

<table>
    <tr>
        <th></th>
        <th colspan="2">별도의 작업 공간</th>
        <th colspan="2">공유 워크스페이스</th>
    </tr>
    <tr>
        <th></th>
        <th>혜택</th>
        <th>단점</th>
        <th>혜택</th>
        <th>단점</th>
    </tr>
    <tr>
        <td>타겟팅</td>
        <td>커뮤니케이션을 분리하는 가장 안전한 방법. 캠페인은 특정 고객 프로필만 타겟팅하도록 보장됩니다.</td>
        <td>사용자가 다른 워크스페이스에 다른 고객 프로필을 가지고 있는 것을 알고 있어도 교차 프로모션 메시징을 보낼 수 없습니다.</td>
        <td>사용자가 워크스페이스에 여러 개의 앱을 가지고 있는 것을 알고 있는 경우 교차 프로모션 메시징을 보낼 수 있습니다.<br><br>여러 앱에서 사용자 데이터를 참조할 수 있습니다. 예를 들어, 존은 앱 1과 관련된 X 속성과 앱 2와 관련된 Y 속성을 가지고 있으며, 두 속성 모두 하나의 캠페인에서 참조할 수 있습니다.</td>
        <td>실수로 여러 앱 인스턴스에 걸쳐 사용자를 타겟팅할 수 있는 인적 오류의 여지가 더 커집니다.<br><br>인앱 메시지를 보내려면 하나의 캠페인이 실수로 다른 앱에 표시되지 않도록 앱별 맞춤 이벤트가 있어야 합니다. 예를 들어 <code>app_1_action</code> 대 <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <td>사용자 지정 이벤트 및 속성</td>
        <td>커스텀 속성 및 이벤트는 앱 인스턴스에만 적용되도록 보장됩니다.</td>
        <td>워크스페이스 전반에서 사용자 행동을 추적할 수 없습니다.<br><br><b>팁:</b> 이를 위해 여러 개의 커런츠 커넥터를 활용할 수 있습니다.</td>
        <td>워크스페이스의 모든 앱 인스턴스에서 사용자 행동을 추적할 수 있습니다.</td>
        <td>사용자 지정 속성 및 이벤트는 모든 앱 인스턴스에 적용되므로 사용자 프로필의 어떤 데이터가 어떤 앱 인스턴스와 관련이 있는지 구분하기 어려울 수 있습니다. 예를 들어, "date_of_parking"이 앱 1과 관련이 있나요, 아니면 앱 2와 관련이 있나요? 이를 방지하려면 체계적인 이름 지정 규칙을 사용해야 합니다.</td>
    </tr>
    <tr>
        <td>주파수 제한</td>
        <td>최대 게재빈도 설정은 각 앱 인스턴스에 대해 개별적으로 정의할 수 있습니다(워크스페이스 기준).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>빈도 제한은 앱 단위가 아닌 모든 캠페인에 적용되므로 고객에게 과도한 메시지를 보내는 것을 방지하기가 더 어렵습니다.</td>
    </tr>
    <tr>
        <td>Subscription status for user profiles</td>
        <td>Each user profile's subscription status is unique to each app instance.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>A user profile's subscription statuses are combined across app instances.<br><br><b>팁:</b> You could use <a href='/docs/user_guide/data/custom_data/custom_attributes'>custom attributes</a> to manage your users' subscriptions instead.</td>
    </tr>
    <tr>
        <td>Braze 사용자 권한</td>
        <td>N/A</td>
        <td>Updating <a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>user permissions</a> for a dashboard user must be done separately for each workspace the user needs access to.</td>
        <td><a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>User permissions</a> can be set once for a dashboard user, and they will have the same permissions for all app instances in the workspace.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>콘텐츠 복제</td>
        <td>N/A</td>
        <td>Cannot duplicate segments, push or Content Card campaigns, or Canvases across workspaces.</td>
        <td>Can [duplicate campaigns across workspaces]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/copying_across_workspaces/) for the following supported channels: SMS, in-app messages, email, email templates, and Content Blocks. <br><br>세그먼트, 캠페인 및 캔버스를 복제하여 한 앱 인스턴스에서 다른 앱 인스턴스로 콘텐츠를 재사용할 수 있습니다.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>분석</td>
        <td>글로벌 통계는 홈 페이지에서 정확하게 확인할 수 있습니다.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>홈 페이지의 워크스페이스에 있는 모든 앱 인스턴스에 대한 글로벌 통계가 집계됩니다.</td>
    </tr>
</table>

## 모범 사례

### 테스트 작업 공간 설정

프로덕션 워크스페이스(실제 사용자에게 메시지를 보낼 워크스페이스)를 설정하려는 경우에는 테스트 워크스페이스도 함께 설정하는 것이 좋습니다. 테스트 작업 공간은 실제 사용자 데이터가 없는 프로덕션 작업 공간의 복제본입니다. 

이는 여러 가지 이유로 모범 사례로 간주됩니다:

- **변경 사항 격리:** 라이브 프로덕션 환경에 영향을 주지 않고 격리된 환경에서 새로운 기능, 구성 또는 업데이트를 테스트할 수 있습니다. 이렇게 하면 테스트 중에 문제가 발생하더라도 프로덕션 환경에는 영향을 미치지 않습니다.
- **정확한 테스트:** 실제 데이터에 대한 걱정 없이 테스트 환경의 데이터를 제어하고 조작할 수 있으므로 보다 정확한 테스트가 가능합니다.
- **디버깅:** 프로덕션 환경에 영향을 미칠 걱정 없이 환경을 자유롭게 조작할 수 있으므로 테스트 환경에서 문제를 디버깅하기가 더 쉽습니다.
- **교육:** 새로운 팀원들은 실수가 실제적인 결과를 초래하지 않는 안전한 환경에서 업무 공간에 익숙해질 수 있습니다.

{% alert tip %}
테스트 워크스페이스와 프로덕션 워크스페이스를 설정하는 순서는 특정 요구 사항과 상황에 따라 달라질 수 있습니다. 하지만 일반적으로 테스트 워크스페이스를 먼저 설정하는 것이 좋습니다. 이를 통해 프로덕션 워크스페이스에 구현하기 전에 기능, 구성 및 업데이트를 테스트할 수 있습니다. 테스트와 결과에 만족하면 프로덕션 워크스페이스를 설정할 수 있습니다.
{% endalert %}

### 관리자 추가

단일 워크스페이스에 대한 관리자 권한이 있는 Braze 사용자가 두 명 이상 있어야 합니다. 이렇게 하면 조직에 다른 사용자의 권한을 관리할 수 있는 충분한 인원이 확보됩니다.

## 다음 단계

워크스페이스 계획을 결정했으면 이제 워크스페이스를 만들고 앱 인스턴스를 추가할 차례입니다. For steps, check out [Creating and managing workspaces]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/).

