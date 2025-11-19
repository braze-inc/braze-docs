---
nav_title: 중복 사용자
article_title: 중복 사용자
description: "Braze 대시보드에서 중복 사용자를 찾아 병합하는 방법을 알아보세요."
page_order: 0
---

# 중복 사용자

> 중복 사용자를 찾아 병합하여 캠페인과 캔버스의 효과를 극대화하는 방법을 알아보세요.

{% alert tip %}
Braze REST API를 사용하여 중복 사용자를 병합하려면 [POST를 참조하세요: 사용자 병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

## 개별 병합

사용자 검색에서 중복된 프로필이 반환되는 경우 Braze 대시보드의 사용자 프로필에서 각 프로필을 개별적으로 병합할 수 있습니다.

### 1단계: 중복 프로필 검색하기

Braze에서 **오디언스** > **사용자 검색을** 선택합니다.

탐색 메뉴에 강조 표시된 '사용자 검색' 타일.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

중복 프로필에 대해 이메일 주소나 휴대폰 번호 등의 고유 식별자를 입력한 다음 **검색을** 선택합니다.

Braze 대시보드의 "사용자 검색" 페이지.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### 2단계: 중복 항목 병합

병합 프로세스를 시작하려면 **중복 항목 병합을** 선택합니다.

중복된 고객 프로필 중 하나입니다.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

유지할 고객 프로필과 병합할 고객 프로필을 선택한 다음 **프로필 병합을** 선택합니다. 중복된 프로필을 모두 병합할 때까지 이 과정을 반복합니다.

중복 프로필에 대한 개별 병합 페이지입니다.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
병합 후에는 중복된 고객 프로필을 복구할 수 없습니다.
{% endalert %}

## 대량 병합

중복 사용자를 일괄 병합하면 Braze는 이메일 주소와 같은 식별자가 일치하는 프로필을 찾아 모든 데이터를 가장 최근에 업데이트된 프로필에 `external_id` 으로 병합합니다. `external_id` 이 있는 프로필이 없는 경우 `external_id` 이 없는 가장 최근에 업데이트된 프로필이 대신 사용됩니다.

### 1단계: 오디언스 관리로 이동하기

Braze 대시보드에서 **오디언스** > **오디언스 관리를** 선택합니다.

탐색 메뉴에 강조 표시된 '오디언스 관리' 타일을 클릭합니다.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### 2단계: 결과 미리보기(선택 사항)

중복 항목을 병합하기 전에 결과를 미리 보려면 **중복 항목 목록 생성을** 선택합니다.

'중복 목록 생성'이 강조 표시된 '오디언스 관리' 페이지가 나타납니다.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze에서 미리 보기를 생성하여 이메일 주소로 CSV 파일로 전송합니다.

생성된 CSV 파일에 대한 링크가 포함된 Braze의 이메일.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

다음 예제에서 Braze는 사용자의 외부 ID를 사용하여 중복 프로필에 플래그를 지정하고 어느 프로필을 유지할지 식별합니다. 이러한 프로필이 일괄 병합되면 Braze는 외부 ID가 있는 프로필을 사용자의 새 기본 프로필로 사용합니다.

{% tabs local %}
{% tab example csv file %}
| 이메일 주소 | 외부 ID | 전화번호 | Braze ID | 규칙 식별자 | 보관할 프로필 | 병합할 프로필
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99 | (555) 123-4567 | 65fcaa547f470494d1370 | 이메일 | TRUE | FALSE |
| alex@company.com | | (555) 987-6543 | 65fcaa547f47d004d1348 | 이메일 | 거짓 | 참 |
| alex@company.com | | (555) 321-0987 | 65fcaa547f47d0049135c | 이메일 | 거짓 | 참 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### 병합 동작

Braze는 보관된 프로필의 비어 있는 필드를 병합된 프로필의 값으로 채웁니다. 채워질 필드 목록은 [병합 동작을]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior) 참조하세요.

### 3단계: 중복된 항목 병합

미리 보기 결과가 만족스럽다면 **모든 중복 항목 병합을** 선택합니다.

{% alert warning %}
병합 후에는 중복된 고객 프로필을 복구할 수 없습니다.
{% endalert %}

'모든 중복 항목 병합'이 강조 표시된 '오디언스 관리' 페이지가 표시됩니다.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## 규칙 기반 병합

병합을 실행할 때 중복된 프로필을 해결하는 방법을 제어하는 규칙을 사용하여 가장 관련성이 높은 고객 프로필을 유지할 수 있습니다. 규칙이 설정되면 Braze는 기준과 일치하는 프로필을 유지합니다.

### 1단계: 규칙 정의

1. **오디언스** > **오디언스 관리** > **규칙 편집으로** 이동합니다.
2. **규칙 편집** 패널의 **유지할 프로필** 섹션에서 중복된 프로필을 병합할 때 유지할 프로필의 **식별자를** 선택합니다. 이메일 주소 또는 전화번호일 수 있습니다.
3. **동점 해소하기** 섹션에서 **유지할 프로필에서** 일치하는 기준을 가진 프로필 간의 동점 해소 방법을 결정할 기준을 선택합니다. 다음을 선택할 수 있습니다:<br>
- **다음을 사용하여 동점을 해결합니다**: 생성 날짜, 업데이트 날짜, 마지막 세션
- **우선순위** 지정: 최신, 오래된

'유지할 프로필' 및 '동점 해소' 옵션을 선택할 수 있는 섹션이 있는 '규칙 편집' 패널입니다.]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

예를 들어 전화번호가 있는 프로필을 유지할 수 있습니다. 여러 사용자가 동일한 전화번호를 사용하는 경우 **업데이트된 날짜** 필드를 사용하여 동점자를 해결하고 가장 최근에 업데이트된 사용자에게 우선순위를 지정할 수 있습니다.

### 2단계: 결과 미리보기(선택 사항)

규칙을 저장한 후 **중복 목록 생성을** 선택하여 규칙이 어떻게 작동할지 미리 볼 수 있습니다. Braze는 미리 보기를 생성하여 규칙이 적용될 경우 어떤 사용자가 유지되고 병합되는지 보여주는 CSV 파일로 이메일 주소로 전송합니다. 

### 3단계: 중복 항목 병합

미리 보기 결과가 만족스럽다면 **오디언스 관리** 페이지로 돌아가서 **모든 중복 항목 병합을** 선택합니다.

{% alert warning %}
병합 후에는 중복된 고객 프로필을 복구할 수 없습니다.
{% endalert %}

## 예약된 병합

규칙 기반 병합과 마찬가지로 예약 병합을 사용하면 미리 구성된 규칙을 사용하여 매일 고객 프로필을 병합하는 작업을 자동화할 수 있습니다.

'오디언스 관리' 페이지에서 '일정' 버튼을 클릭합니다.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

이 기능을 켜면 Braze는 사용자의 회사 시간대 기준 매일 오전 12시에 병합 프로세스를 수행하도록 자동으로 시간 슬롯을 할당합니다. 언제든지 예약 병합을 해제할 수 있습니다. 예정된 병합이 발생하기 24시간 전에 Braze가 워크스페이스 관리자에게 알림을 보내 구성을 검토할 수 있는 시간을 제공합니다.

{% alert warning %}
병합 후에는 중복된 고객 프로필을 복구할 수 없습니다.
{% endalert %}
