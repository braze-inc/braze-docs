---
nav_title: 사용자
article_title: Braze 사용자 관리
page_order: 0
page_type: reference
description: "이 참조 문서에서는 사용자 추가, 일시 중지 및 삭제를 포함하여 회사 계정에서 사용자를 관리하는 방법을 다룹니다."

---

# Braze 사용자 관리

> 회사 계정에서 사용자 추가, 일시 중지 및 삭제를 포함하여 사용자를 관리하는 방법을 배우세요.

{% alert note %}
이 페이지의 여러 섹션은 **회사 사용자** 페이지를 참조합니다. 만약 [이전 탐색]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)을 사용하고 있다면, **회사 사용자**는 **사용자 관리**라고 불리며 계정 아이콘 아래에 위치합니다.
{% endalert %}

## Braze 사용자 추가

사용자를 Braze 계정에 추가하려면 관리자 권한이 있어야 합니다. 

새 사용자를 추가하려면:

1. **설정** > **회사 사용자**.
2. **\+ 새 사용자 추가**를 클릭합니다.
3. 이메일, 부서, [사용자 역할]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role) 등 메시지가 표시되면 해당 사용자의 정보를 입력합니다.

{% alert tip %}
고객 프로필에 나열된 부서는 Braze로부터 수신하는 커뮤니케이션 유형을 결정합니다. 이것은 모든 사람이 Braze를 사용하는 방식과 관련된 커뮤니케이션 및 알림만 받도록 하기 위함입니다.
{% endalert %}

![User details fields.]({% image_buster /assets/img/add_new_user_2.png %}){: style="max-width:60%;"}

{:start="4"}

4. 관리자가 아닌 사용자의 경우, 이 사용자가 가질 [권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions)을(를) 회사 수준 및 작업 공간 수준에서 선택하십시오.

![Workspace-level permissions with a section for custom permissions fields.]({% image_buster /assets/img/add_new_user_3.png %})

### 이메일 주소 요구 사항

모든 이메일 주소는 [인스턴스]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)에서 고유해야 합니다. 이는 해당 인스턴스에서 회사 작업 공간에 접근한 적이 있거나 여전히 접근할 수 있는 사용자와 이미 연결된 이메일 주소를 추가하려고 하면 오류 메시지가 표시된다는 것을 의미합니다. 

팀에서 Gmail을 사용하고 있으며 이메일 주소 추가에 문제가 있는 경우 이메일 주소에 더하기 기호(+)를 추가하여 "+1" 또는 "+테스트"와 같은 별칭을 만들 수 있습니다. 예를 들어, `contractor@braze.com`은(는) `contractor+1@braze.com`의 별칭을 가질 수 있습니다. 이메일을 `contractor+1@braze.com`에게 보내면 여전히 `contractor@braze.com`에게 전달되지만, 별칭은 고유한 이메일 주소로 인식됩니다.

### Braze 계정의 이메일 주소를 변경할 수 있나요?

보안상의 이유로 사용자는 Braze 계정과 연결된 이메일 주소를 변경할 수 없습니다. 사용자가 이메일 주소를 업데이트하려는 경우 관리자는 사용자가 선호하는 이메일 주소로 [새 계정을 만들어야](#adding-braze-users) 합니다.

## Braze 사용자 일시 중지

사용자를 일시 중지하면 계정이 비활성 상태가 되어 더 이상 로그인할 수 없지만 계정과 관련된 데이터는 보존됩니다. 관리자만 Braze 사용자를 일시 중지하거나 일시 중지를 해제할 수 있습니다.

사용자를 일시 정지하려면 **설정** > **회사 사용자로** 이동하여 해당 사용자 아이디를 찾은 다음 <i class="fa-solid fa-user-lock"></i> **일시 정지를** 선택합니다.

![Option to suspend a user.]({% image_buster /assets/img_archive/suspend_user.png %})

관리자는 목록에서 사용자의 이름을 선택하고 하단의 **사용자 정지**을 클릭하여 사용자를 정지할 수도 있습니다.

![Suspend a user when editing the user details.]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## Assigning user access and responsibilities

{% multi_lang_include permissions.md content="Differences" %}

## Braze 사용자 삭제

사용자를 삭제하려면 **설정** > **회사 사용자**로 이동하여 사용자 이름을 찾고 <i class="fa fa-trash-can"></i> **사용자 삭제**를 선택하십시오.

![Delete a user]({% image_buster /assets/img_archive/delete_user_new.png %})

사용자가 삭제된 후 Braze는 다음 계정 데이터를 보관하지 않습니다:

- 사용자가 가지고 있던 모든 속성
- 이메일 주소
- 전화번호
- 외부 사용자 ID
- 성별
- 국가
- 언어
- 다른 유사한 데이터

Braze는 다음 계정 데이터를 보관합니다:

- 계정과 연결된 사용자 지정 속성 또는 테스트 데이터
- 사용자가 만든 캠페인 또는 캔버스(단, **마지막으로 편집한** 사람 열에 표시되는 등 사용자 이름이 표시되지 않음)

## 문제 해결

### 사용자를 추가하려고 할 때 "이메일이 이미 사용 중입니다."라는 메시지가 표시됩니다.

새 사용자를 추가하려고 하는데 이메일이 이미 사용되었지만 사용자 목록에서 찾을 수 없다는 오류가 표시되는 경우, 해당 사용자는 동일한 Braze 대시보드 클러스터의 다른 인스턴스 내에 존재할 가능성이 높습니다.

이 새 사용자를 만들려면 다음 중 하나를 수행하면 됩니다:

1. 다른 인스턴스에서 사용자를 삭제한 후에 새 인스턴스에서 사용자를 만들 수 있습니다.
2. 다른 이메일 문자열(예: `testing+01@braze.com`) 또는 다른 이메일 별칭을 사용하여 사용자를 만듭니다. 

`testing+01@braze.com` 을 사용할 때 받은 편지함에서 메시지 활성화가 표시되지 않으면 해당 이메일 주소의 메시지를 받을 수 있는지 IT 팀에 확인하세요. 일부 관리자는 `+` 로 시작하는 이메일 주소로 보낸 메시지를 필터링합니다.

