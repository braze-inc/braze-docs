---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
alias: /teams/
description: "이 참조 문서에서는 대시보드에서 Braze Teams를 사용하는 방법을 다룹니다. Teams를 생성하고, 역할을 할당하고, 태그와 필터를 할당하는 방법을 알아볼 수 있습니다."

---

# Teams

> Braze 관리자는 다양한 사용자 역할과 권한을 가진 Teams로 회사 사용자를 그룹화할 수 있습니다. 이를 통해 편집할 수 있는 콘텐츠 유형을 분리하여 하나의 워크스페이스에서 여러 개의 관련 없는 회사 사용자 그룹이 함께 작업할 수 있습니다.

Teams는 고객 기반 위치, 언어, 커스텀 속성에 따라 설정할 수 있으므로 Teams 멤버와 비멤버가 메시징 기능과 고객 데이터에 대해 서로 다른 접근 권한을 가질 수 있습니다. 다양한 참여 툴에서 Teams 필터와 태그를 할당할 수 있습니다. 워크스페이스에서 생성할 수 있는 Teams 수에는 제한이 없습니다.

모든 Braze 계약에서 Teams를 사용할 수 있는 것은 아닙니다. 이 기능에 접근하려면 Braze 계정 매니저에게 문의하거나 [저희에게 연락하세요](mailto:success@braze.com).

## Teams는 권한 세트 및 역할과 어떻게 다른가요?

{% multi_lang_include permissions.md content="Differences" %}

## Teams 생성 {#creating-teams}

**설정** > **내부 Teams**로 이동하여 <i class="fas fa-plus"></i> **Teams 추가**를 선택합니다.

![새 Teams를 추가하는 창.]({% image_buster /assets/img_archive/adding_a_team.png %})

**Teams 이름**을 입력합니다. 원하는 경우 **Teams 정의(선택 사항)** 필드를 사용하여 커스텀 속성, 위치 또는 언어를 선택하여 Teams가 접근할 수 있는 사용자 데이터를 추가로 정의할 수 있습니다. 예를 들어, 가능한 사용 사례는 커스텀 속성으로 식별되는 테스트 사용자에게만 접근할 수 있는 개발 Teams를 생성하여 [Teams로 테스트](#test-with-teams)를 수행하는 것입니다. 또 다른 사용 사례는 제품에 따라 사용자와의 커뮤니케이션을 제한하는 것입니다.

Teams가 커스텀 속성, 언어 또는 국가로 정의된 경우, 해당 Teams를 사용하여 캠페인, 캔버스, 콘텐츠 카드, 세그먼트 등의 기능에 대해 최종 사용자를 필터링할 수 있습니다. 자세한 내용은 [Teams 태그 할당](#tags-and-filters)을 참조하세요.

## 사용자를 Teams에 할당하기

Braze 관리자와 "회사 설정 관리 가능"이라는 회사 수준 권한이 있는 제한된 사용자는 제한된 접근 권한이 있는 회사 사용자에게 Teams 수준 권한을 할당할 수 있습니다. Teams에 할당되면, 회사 사용자는 Teams 생성 시 정의된 사용자 언어, 위치 또는 커스텀 속성과 같은 특정 Teams에서 사용 가능한 데이터만 읽거나 쓸 수 있습니다.

사용자를 Teams에 할당하려면 **설정** > **회사 사용자**로 이동하여 Teams에 추가할 사용자를 선택합니다.

그런 다음 다음 단계를 수행합니다:

1. **워크스페이스 수준 권한** 섹션에서 사용자가 아직 포함되어 있지 않은 경우 적절한 워크스페이스에 추가하세요.

![배너 템플릿 권한 세트가 설정된 워크스페이스 수준 권한.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. **+ Teams 수준 권한 추가**를 선택한 다음, 이 사용자를 추가할 **Teams**를 선택하세요.
3. **Teams** 권한 섹션에서 특정 권한을 할당하세요.

![Teams 수준 랜딩 페이지 템플릿 권한.]({% image_buster /assets/img/teams.png %})

### 사용 가능한 Teams 수준 권한

다음은 Teams 수준에서 할당할 수 있는 모든 권한입니다. 여기에 나열되지 않은 권한은 워크스페이스 수준에서만 부여되며, 이러한 권한은 **Teams** 권한 열에 "--"으로 표시됩니다.

{% tabs %}
{% tab 세분화된 권한 %}

{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

- 캠페인 보기
- 캠페인 편집
- 캠페인 아카이브
- 캔버스 보기
- 캔버스 편집
- 캔버스 아카이브
- 콘텐츠 블록 보기
- 콘텐츠 블록 편집
- 콘텐츠 블록 아카이브
- 콘텐츠 블록 시작
- 기능 플래그 보기
- 기능 플래그 편집
- 기능 플래그 아카이브
- 세그먼트 보기
- 세그먼트 편집
- 이메일 템플릿 보기
- 이메일 템플릿 편집
- 이메일 템플릿 아카이브
- 웹훅 템플릿 보기
- 웹훅 템플릿 편집
- 웹훅 템플릿 아카이브
- 이메일 링크 템플릿 보기
- 이메일 링크 템플릿 편집
- 미디어 라이브러리 자산 보기
- 미디어 라이브러리 자산 편집
- 미디어 라이브러리 자산 삭제
- 캠페인 시작
- 캔버스 시작
- 사용자 데이터 내보내기
- 고객 프로필 보기(PII 수정됨)
- 대시보드 사용자 편집
- 캠페인 승인
- 캔버스 승인
- 캔버스 템플릿 편집
- 캔버스 템플릿 보기
- 캔버스 템플릿 아카이브
- 대시보드 보고서 보기
- 대시보드 보고서 편집
- 대시보드 보고서 삭제
- PII 보기

{% endtab %}
{% tab 레거시 권한 %}

- 캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경설정 센터에 접근
- 캠페인, 캔버스 발송
- 콘텐츠 카드 시작 및 관리
- 세그먼트 편집
- 사용자 데이터 내보내기
- 고객 프로필 PII 준수 보기
- 대시보드 사용자 관리
- 미디어 라이브러리 자산 관리
- 캠페인 승인 및 거부
- 캔버스 승인 및 거부
- 캔버스 템플릿 생성 및 편집
- 캔버스 템플릿 보기
- 캔버스 템플릿 아카이브
- 랜딩 페이지 템플릿 편집
- 랜딩 페이지 템플릿 보기
- 랜딩 페이지 템플릿 아카이브

{% endtab %}
{% endtabs %}

각 사용자 권한에 포함된 항목과 사용 방법에 대한 설명을 보려면 [사용자 권한]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions) 섹션을 참조하세요.

## Teams 태그 할당 {#tags-and-filters}

**Teams 추가** 필터를 사용하여 캔버스, 캠페인, 콘텐츠 카드, 세그먼트, 이메일 템플릿, 웹훅 템플릿, 콘텐츠 블록 및 미디어 라이브러리 자산에 Teams를 할당할 수 있습니다.
 
![캠페인에 Teams 태그 추가하기.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Teams 생성 시 적용된 *정의*에 따라, Teams 필터가 할당되면 해당 참여 툴의 오디언스는 정의와 일치하는 고객 프로필로 제한됩니다.
- 할당된 *권한*에 따라, Teams 멤버는 자신의 Teams 필터가 설정된 대시보드 참여 툴에만 접근할 수 있습니다. 워크스페이스 권한이 제한적이거나 없는 경우, 특정 오브젝트를 저장하거나 시작하기 전에 Teams 필터를 추가해야 합니다. Teams 멤버는 또한 캔버스, 캠페인, 콘텐츠 카드 및 세그먼트를 Teams별로 필터링하여 관련 콘텐츠를 식별할 수 있습니다.

### 활용 사례

다음 두 가지 시나리오는 Braze의 마케터 미셸의 경우를 가정한 것입니다. 미셸은 "Development"라는 Teams의 멤버입니다. 그녀는 Development Teams의 모든 Teams 수준 권한에 접근할 수 있습니다.

{% tabs %}
{% tab 시나리오 1 - Teams 권한만 %}

이 시나리오에서 미셸은 워크스페이스 수준 권한이 없는 제한된 사용자입니다. 그녀의 권한은 다음과 같습니다:

![워크스페이스 수준 권한이 없고 16개의 Teams 기반 권한이 있는 커스텀 권한.]({% image_buster /assets/img_archive/scenario1.png %})

미셸에게 할당된 권한에 따라, 캠페인을 생성할 때마다 해당 캠페인에 "Development" Teams만 할당할 수 있습니다. Teams가 할당되지 않으면 캠페인을 시작할 수 없으며, 다른 Teams 태그를 보거나 접근할 수 없습니다.

!["Development" Teams 태그만 표시되는 캠페인 Teams 태그 드롭다운.]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab 시나리오 2 - Teams 권한과 워크스페이스 권한 %}

이 시나리오에서 미셸은 여전히 Development Teams의 멤버이지만, 추가적인 워크스페이스 수준 권한도 가지고 있습니다.

![하나의 워크스페이스 수준 권한과 15개의 Teams 기반 권한이 있는 커스텀 권한.]({% image_buster /assets/img_archive/scenario2.png %})

미셸이 "캠페인, 캔버스, 카드, 콘텐츠 블록, 기능 플래그, 세그먼트, 미디어 라이브러리 및 환경설정 센터에 접근"이라는 워크스페이스 수준 권한을 가지고 있기 때문에, 생성하는 캠페인에 다른 Teams 필터를 보고 할당할 수 있습니다.

![여러 Teams 태그가 있는 캠페인 Teams 태그 드롭다운]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

첫 번째 시나리오와 마찬가지로, 미셸은 캠페인을 시작하기 전에 Development Teams 태그를 캠페인에 추가해야 합니다.

{% endtab %}
{% endtabs %}

## Teams로 테스트하기 {#test-with-teams}

Teams의 가능한 활용 사례 중 하나는 프로덕션 환경에서 콘텐츠를 테스트하고 시작하기 위한 Teams 기반 승인 시스템을 만드는 것입니다.

이를 위해 테스트 사용자에게만 접근할 수 있는 "Development" Teams를 생성합니다. 테스트 사용자가 커스텀 속성으로 식별 가능한 경우 Teams를 테스트 사용자에게만 접근하도록 제한할 수 있습니다. 그런 다음 Teams를 생성하거나 편집할 때 커스텀 속성을 정의로 추가합니다(앞의 [Teams 생성](#creating-Teams) 섹션 참조). 승인자는 모든 사용자에 대한 접근 권한이 있어야 합니다.

일반적인 프로세스는 다음과 같습니다:

1. Development Teams가 캠페인을 생성하고 "Development" Teams 태그를 추가합니다.
2. Development Teams가 테스트 사용자에게 캠페인을 시작합니다.
3. 승인 Teams가 로컬 캠페인 디자인을 검증하고, 승격하고, 시작합니다. 시작하려면 승인 Teams가 Teams 태그를 "Development"에서 "[All Teams]"로 변경하고 캠페인을 다시 시작합니다.

활성 캠페인에 대한 변경 사항:

1. Development Teams가 실행 중인 캠페인을 복제하고, "Development" Teams 태그를 추가하고, 저장합니다.
2. Development Teams가 편집을 수행하고 승인 Teams와 공유합니다.
3. 승인 Teams가 "Development" Teams 태그를 제거하고, 이전 캠페인을 일시 중지하고, 새 캠페인을 시작합니다.

## 기존 Teams 아카이브하기

**내부 Teams** 페이지에서 Teams를 아카이브할 수 있습니다.

아카이브할 하나 이상의 Teams를 선택합니다. Teams가 Braze 내의 어떤 오브젝트와도 연결되어 있지 않으면 즉시 아카이브됩니다. Teams가 오브젝트와 연결되어 있는 경우, 아카이브 프로세스 후 Teams를 제거하거나 교체하는 옵션이 표시됩니다.

![Braze에서 오브젝트에 연결된 Teams 아카이브하기]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Braze 관리자는 아카이브된 Teams를 선택하고 **아카이브 해제**를 선택하여 Teams의 아카이브를 해제할 수 있습니다.