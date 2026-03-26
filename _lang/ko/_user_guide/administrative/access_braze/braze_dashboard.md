---
nav_title: 대시보드
article_title: Braze 대시보드
page_order: 5
page_type: reference
description: "Braze 대시보드는 고객 참여를 구축, 관리 및 분석하기 위한 중앙 작업 공간입니다. 메시징 도구, 오디언스 통찰력, 세분화 및 실시간 성능 데이터를 한 곳에 모아 제공합니다."

---

# Braze 대시보드

> Braze 대시보드는 고객 참여를 구축, 관리 및 분석하기 위한 중앙 작업 공간입니다. [dashboard.braze.com](https://dashboard.braze.com/) 또는 [dashboard.braze.eu](https://dashboard.braze.eu/)에서 액세스하세요.

Braze 대시보드를 사용하여 캠페인을 계획하고, 메시지를 시작 및 관리하며, 오디언스 통찰력을 탐색하고, 세분화를 조정하고, 단일 인터페이스에서 실시간 성과 및 참여 측정기준을 검토하세요.

## 대시보드 개요

로그인하면 대시보드는 귀하의 참여 도구 및 데이터에 대한 중앙 집중식 보기를 제공합니다:

- **홈 페이지:** 최근 편집된 [콘텐츠](#pick-up-where-you-left-off) 및 주요 성과 측정기준을 한눈에 보여줍니다.
- **왼쪽 탐색:** 기능별로 도구를 정리합니다 (메시징, 오디언스, 분석, 설정)
- **글로벌 헤더:** 검색, 지원, 언어 설정, 알림 및 귀하의 계정에 빠르게 액세스할 수 있습니다.

귀하의 대시보드 경험은 [작업 공간]({{site.baseurl}}/user_guide/getting_started/workspaces)에 의해 조직되어 있으며, 이는 다양한 브랜드, 지역 또는 팀을 위한 콘텐츠를 관리하는 데 도움이 됩니다. 측면 탐색에서 언제든지 [작업 공간 간 전환](#workspace-switcher)할 수 있습니다.

## 대시보드에 액세스하세요

시작하려면 [Braze 계정에 로그인]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account)하세요. 대시보드 내 페이지에 대한 액세스 및 특정 작업을 수행할 수 있는 권한은 귀하에게 할당된 [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions)에 따라 다릅니다. 권한에 대한 도움이 필요하면 Braze 관리자에게 문의하세요.

## Braze로 이동

브레이즈 탐색은 기기 전반에 걸쳐 기능과 콘텐츠에 효율적으로 접근할 수 있도록 설계되었습니다. Braze 대시보드에는 두 가지 탐색 수준이 있습니다: 전역 헤더와 사이드 탐색입니다.

전역 헤더는 화면 상단에서 거의 항상 표시됩니다. 필수 도구 및 설정에 빠르게 접근할 수 있습니다. 포함된 항목은 다음과 같습니다:

- 검색
- 지원 및 커뮤니티 링크
- [대시보드 언어]({{site.baseurl}}/user_guide/administrative/access_braze/language/)
- Notifications
- 계정 설정
- [BrazeAI 운영자™]({{site.baseurl}}/user_guide/brazeai/operator/)

### 사이드 탐색 사용

왼쪽의 수직 메뉴는 Braze 도구를 기능별로 정리하고 가장 많이 사용하는 항목을 손이 닿는 곳에 유지합니다. 주 메뉴 항목을 선택하여 쌓인 수직 레이아웃으로 옵션을 표시합니다. 

![Braze 대시보드의 작업 공간 전환기]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### 작업 공간 전환기

사이드 탐색 상단에 위치한 작업 공간 전환기를 사용하면 Braze 인스턴스의 서로 다른 작업 공간 간에 이동할 수 있습니다. 활성 작업 공간이 강조 표시됩니다.

[작업 공간]({{site.baseurl}}/user_guide/getting_started/workspaces)은 브랜드, 지역, 제품 라인 또는 팀별로 콘텐츠를 정리하는 데 도움을 줍니다. 각 작업 공간에는 고유한 데이터, 캠페인 및 설정이 포함됩니다. 작업 공간 간에 접근 권한이 다를 수 있습니다. 예를 들어, 한 작업 공간에서는 편집 권한이 있고 다른 작업 공간에서는 보기 전용 권한이 있을 수 있습니다.

작업 공간을 전환하려면 사이드 탐색 상단의 작업 공간 드롭다운을 선택하고 접근하려는 작업 공간을 선택하세요. 가장 자주 사용하는 작업 공간에 빠르게 접근할 수 있도록 [즐겨찾기 작업 공간 추가](#adding-favorite-workspaces)할 수도 있습니다.

#### 사이드 내비게이션 최소화

비주얼 혼잡을 줄이기 위해, 특히 캔버스를 디자인하는 작업 중에는 사이드 내비게이션 패널을 최소화할 수 있습니다. **메뉴 최소화**를 눌러서 축소하세요. 최소화된 상태에서도 아이콘 위에 마우스를 올리면 메뉴 항목 이름이 포함된 툴팁을 볼 수 있습니다. 이것은 작업 공간을 깔끔하게 유지하면서 도구 간에 빠르게 이동하는 데 도움이 됩니다.

![메뉴 아이콘 최소화 및 최대화]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### 반응형 탐색

내비게이션은 다양한 화면 크기에 원활하게 적응합니다. 작은 화면에서는 측면 탐색이 자동으로 축소됩니다. 필요할 때 <i class="fa-solid fa-bars" aria-label="탐색 메뉴 열기"></i>를 눌러 메뉴를 엽니다. 

![작은 화면에서는 측면 탐색이 자동으로 축소됩니다. 메뉴 아이콘을 탭하면 내비게이션 옵션이 열립니다.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## 대시보드 검색

헤더에 위치한 글로벌 검색 바는 Braze 대시보드에서 콘텐츠를 찾는 가장 빠른 방법입니다. 검색 인터페이스를 열고 필요한 항목으로 바로 이동하려면 선택하세요. 

![검색어가 입력되지 않은 상태에서 글로벌 검색이 열리며, 최근에 열린 페이지가 표시됩니다.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

최근에 열린 콘텐츠는 검색 바 아래에 나타납니다. 여기에는 최근에 상호작용한 캠페인, 캔버스, 템플릿 또는 페이지가 포함되어 있어 작업으로 쉽게 돌아갈 수 있습니다.

### 무엇을 검색할 수 있습니까?

다음 항목 및 작업을 검색할 수 있습니다:

- 캠페인 이름
- 캔버스 names
- 콘텐츠 블록
- 세그먼트 이름
- 이메일 템플릿 이름
- Braze 내의 페이지 (동의어 포함)

{% alert tip %}
정확한 텍스트를 검색하려면 검색어를 따옴표("")로 묶으세요. 예를 들어, [“모든 사용자”]를 검색하면 이름에 정확한 구문 “모든 사용자”가 포함된 모든 항목이 반환됩니다.
{% endalert %}

### 콘텐츠 유형 및 상태 태그

각 결과는 콘텐츠 유형을 나타내는 태그로 레이블이 지정됩니다—예: 캠페인, 캔버스 또는 세그먼트—및 상태(활성, 보관, 중지).

### 활성 및 초안 콘텐츠에 대한 필터

기본적으로 검색에는 활성, 초안 및 보관된 항목이 포함됩니다. 결과를 좁히려면 **활성 및 초안만 표시** 토글을 사용하세요.

!["활성 및 초안만 표시" 토글.]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### 키보드 단축키

키보드를 사용하여 검색 결과를 이동할 수 있습니다.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Action                      | 키보드 단축키                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| 검색 메뉴 열기        | {::nomarkdown} <ul> <li> 맥: <kbd>⌘</kbd> + <kbd>K</kbd> </li> <li>윈도우: <kbd>Ctrl</kbd> + <kbd>K</kbd> </li> </ul> {:/}  |
| 검색 결과 간 이동 | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| 검색 결과 선택      | <kbd>진입</kbd>    |
| 검색 메뉴 닫기       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tips

Braze 대시보드는 작업을 보다 효율적으로 수행하고 가장 많이 사용하는 도구와 콘텐츠에 빠르게 접근할 수 있도록 여러 기능을 포함합니다.

### 중지한 위치에서 재개

**홈** 페이지에서 대시보드는 최근에 편집하거나 생성한 캠페인, 캔버스 및 세그먼트를 표시합니다. 이렇게 하면 검색하지 않고도 진행 중인 작업으로 쉽게 돌아갈 수 있습니다. 각 항목에는 콘텐츠 유형 및 상태(예: 초안, 활성 또는 중지됨)를 보여주는 태그가 포함되어 있습니다.

![캔버스 초안, 활성 세그먼트 및 '중단한 부분 이어받기' 섹션의 캠페인 초안입니다.]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

자세한 내용은 [홈 대시보드]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off)를 참조하세요.

### 즐겨찾는 작업 공간 추가

여러 작업 공간에서 작업하는 경우 가장 자주 사용하는 작업 공간을 즐겨찾기로 표시하여 더 빠르게 접근할 수 있습니다. 즐겨찾는 작업 공간을 추가하려면 [프로필 설정에 접근](#accessing-your-profile-settings)하고, **즐겨찾는 작업 공간** 필드를 **계정 프로필** 섹션에서 찾아서 즐겨찾기로 추가할 작업 공간을 선택하세요. 즐겨찾는 작업 공간은 작업 공간 전환기 상단에 표시되어 빠르게 접근할 수 있습니다.

### 프로필 설정에 접근

계정 설정, 알림 기본 설정 및 개인 정보를 관리하려면:

1. 전역 헤더에서 프로필 아이콘을 선택하세요.
2. **계정 관리**를 선택하여 프로필 페이지에 접근하세요.

프로필 페이지에서 이메일 설정을 업데이트하고, 2단계 인증을 구성하고, API 키를 확인하고, 기타 계정 세부 정보를 관리할 수 있습니다.

## 대시보드의 접근성

Braze 대시보드는 색상 대비에 대한 WCAG AA 기준을 충족하는 브랜드 색상을 사용합니다. 이는 모든 사용자에게 포괄적인 경험을 지원하며 접근성 모범 사례에 부합합니다.

## 피드백 공유

당신의 생각을 들려주고 싶으신가요? 내비게이션, 접근성, 사용성, 시각적 디자인 등에 대한 피드백을 공유할 수 있습니다. 전역 헤더에서 **지원** 메뉴를 열고 **피드백 공유**를 선택하세요. 우리는 모든 피드백을 검토하여 귀하의 Braze 경험을 개선하는 데 도움을 줍니다.

## 관련 리소스

### 관리 작업

- [작업 공간 만들기 및 관리]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)
- [Braze 사용자 관리]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)
- [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)

### 주요 작업 및 다음 단계

- **캠페인 구축**: [캠페인을 생성하세요]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)
- **여정 만들기**: [캔버스 구축]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- **대상 정의**: [세그먼트를 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)
- **성능 검토**: [애널리틱스 개요]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/)
- **설정 구성**: [앱 설정]({{site.baseurl}}/user_guide/administrative/app_settings/)


