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

사용자 검색에서 중복 프로필이 반환되는 경우, Braze 대시보드의 사용자 프로필에서 각 프로필을 개별적으로 병합할 수 있습니다.

### 1단계: 중복 프로필 검색

Braze에서 **오디언스** > **사용자 검색**을 선택합니다.

![The "User Search" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

중복 프로필에 대해 이메일 주소나 휴대폰 번호와 같은 고유 식별자를 입력한 다음 **검색**을 선택합니다.

![The "User Search" page in the Braze dashboard.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### 2단계: 병합이 중복됨

병합 프로세스를 시작하려면 **중복 항목 병합**을 선택합니다.

![One of the duplicate user's profiles.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

유지할 고객 프로필과 병합할 고객 프로필을 선택한 다음 **프로필 병합**을 선택합니다. 중복된 프로필을 모두 병합할 때까지 이 과정을 반복합니다.

![The individual merge page for a duplicate profile.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
병합 후에는 중복된 사용자 프로필을 복구할 수 없습니다.
{% endalert %}

## 대량 병합

중복 사용자를 일괄 병합하면 Braze는 이메일 주소와 같은 식별자가 일치하는 프로필을 찾아 모든 데이터를 가장 최근에 업데이트된 프로필에 `external_id`로 병합합니다. `external_id` 이 있는 프로필이 없는 경우 `external_id` 이 없는 가장 최근에 업데이트된 프로필이 대신 사용됩니다.

### 1단계: 오디언스 관리로 이동

Braze 대시보드에서 **오디언스** > **오디언스 관리**를 선택합니다.

![The "Manage Audience" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### 2단계: 결과 미리보기(선택 사항)

중복 항목 병합하기 전에 결과를 미리 보려면 **중복 항목 목록 생성**을 선택합니다.

!["중복 목록 생성"이 강조 표시된 "오디언스 관리" 페이지]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze에서 미리보기를 생성하여 이메일 주소로 CSV 파일로 전송합니다.

![생성된 CSV 파일 링크가 포함된 Braze의 이메일.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

다음 예제에서 Braze는 사용자의 외부 ID를 사용하여 중복 프로필에 플래그를 지정하고 어떤 프로필을 유지할지 식별합니다. 이러한 프로필이 일괄 병합되면 Braze는 외부 ID가 있는 프로필을 사용자의 새 기본 프로필로 사용합니다.

{% tabs local %}
{% tab 예제 CSV 파일 %}
| Email Address    | External ID | Phone Number   | Braze ID              | Identifier for rule | Profile to keep | Profile to merge |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### 병합 동작

브레이즈는 유지된 프로필의 빈 필드를 병합된 프로필의 값으로 채울 것입니다. 필드가 채워질 목록은 병합 동작을 참조하십시오.

### 3단계: 중복된 항목 병합

미리 보기 결과가 만족스럽다면 **모든 중복 항목 병합**을 선택합니다.

{% alert warning %}
병합 후에는 중복된 사용자 프로필을 복구할 수 없습니다.
{% endalert %}

!["모든 중복 항목 병합"이 강조 표시된 "오디언스 관리" 페이지]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## 규칙 기반 병합

병합을 실행할 때 가장 관련성이 높은 사용자 프로필이 유지되도록 규칙을 사용하여 중복 프로필이 해결되는 방식을 제어할 수 있습니다. 규칙이 설정되면 Braze는 기준과 일치하는 프로필을 유지합니다.

### 1단계: 규칙 정의

1. **대상** > **대상 관리** > **규칙 편집으로** 이동합니다.
2. **규칙 수정** 패널의 **유지할 프로필** 섹션에서 중복을 병합할 때 유지할 프로필의 **식별자를** 선택합니다. 이메일 주소나 전화번호가 될 수 있습니다.
3. **동점 해결** 섹션에서 **유지할 프로필**에서 일치하는 기준이 있는 프로필 간의 동점 해결 방법을 결정할 기준을 선택합니다. 다음을 선택할 수 있습니다:<br>
- **다음을 사용하여 동점을 해결합니다**: 생성 날짜, 업데이트 날짜, 마지막 세션
- **우선순위 지정**: 최신, 오래된

![The "Edit rules" panel with sections to select options for "Profile to keep" and "Resolving ties".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

예를 들어 전화번호가 있는 프로필을 유지할 수 있습니다. 여러 사용자가 동일한 전화번호를 사용하는 경우 **업데이트된 날짜** 필드를 사용하여 동점자를 해결하고 가장 최근에 업데이트된 사용자에게 우선순위를 지정할 수 있습니다.

### 2단계: 결과 미리보기(선택 사항)

규칙을 저장한 후 **중복 목록 생성**을 선택하여 규칙이 어떻게 작동할지 미리 볼 수 있습니다. Braze는 미리보기를 생성하여 규칙이 적용될 경우 어떤 사용자가 유지되고 병합되는지 보여주는 CSV 파일로 이메일 주소로 전송합니다. 

### 3단계: 병합이 중복됨

미리 보기 결과가 만족스럽다면 **오디언스 관리** 페이지로 돌아가서 **모든 중복 항목 병합**을 선택합니다.

{% alert warning %}
병합 후에는 중복된 사용자 프로필을 복구할 수 없습니다.
{% endalert %}

## Scheduled merging

Similar to rules-based merging, scheduled merging allows you to automate the merging of user profiles on a daily basis using preconfigured rules.

![The "Manage Audience" page with "schedule" button.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

After the feature is turned on, Braze will automatically assign a timeslot to perform the merge process daily at approximately 12 am in the user's company time zone. You can turn off scheduled merging at any time. Braze will notify the admins of your workspace 24 hours before the scheduled merge occurs, providing a reminder and time to review the configuration.

{% alert warning %}
병합 후에는 중복된 사용자 프로필을 복구할 수 없습니다.
{% endalert %}
