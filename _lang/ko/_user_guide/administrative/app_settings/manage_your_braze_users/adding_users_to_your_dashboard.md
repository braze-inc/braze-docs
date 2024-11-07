---
nav_title: 사용자
article_title: Braze 사용자 관리
page_order: 0
page_type: reference
description: "이 참조 문서에서는 사용자 추가, 일시 중지 및 삭제를 포함하여 회사 계정에서 사용자를 관리하는 방법을 다룹니다."

---

# Braze 사용자 관리

> 회사 계정에서 사용자 추가, 일시 중지 및 삭제를 포함하여 사용자를 관리하는 방법을 배우십시오.

{% alert note %}
이 페이지의 여러 섹션은 **회사 사용자** 페이지를 참조합니다. 만약 [이전 탐색]({{site.baseurl}}/navigation)을 사용하고 있다면, **회사 사용자**는 **사용자 관리**라고 불리며 계정 아이콘 아래에 위치합니다.
{% endalert %}

## Braze 사용자 추가

사용자를 Braze 계정에 추가하려면 관리자 권한이 있어야 합니다. 

새 사용자를 추가하려면:

1. **설정** > **회사 사용자**.
2. 클릭 **\+ Add New User**.
3. 프롬프트에 따라 이메일, 부서 및 \[사용자 역할]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role.을(를) 포함하여 정보를 입력하십시오.

{% alert tip %}
사용자의 프로필에 나열된 부서는 Braze로부터 수신하는 커뮤니케이션 유형을 결정합니다. 이것은 모든 사람이 Braze를 사용하는 방식과 관련된 커뮤니케이션 및 알림만 받도록 하기 위함입니다.
{% endalert %}

![][2]

{:start="4"}

4. 관리자가 아닌 사용자의 경우, 이 사용자가 가질 [권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions)을(를) 회사 수준 및 작업 공간 수준에서 선택하십시오.

![][3]

### 이메일 주소 요구 사항

모든 이메일 주소는 인스턴스에서 고유해야 합니다. 이는 해당 인스턴스에서 회사 작업 공간에 접근한 적이 있거나 여전히 접근할 수 있는 사용자와 이미 연결된 이메일 주소를 추가하려고 하면 오류 메시지가 표시된다는 것을 의미합니다. 

팀에서 Gmail을 사용하고 있으며 이메일 주소 추가에 문제가 있는 경우 이메일 주소에 더하기 기호(+)를 추가하여 "+1" 또는 "+test"와 같은 별칭을 만들 수 있습니다. 예를 들어, `contractor@braze.com`은(는) `contractor+1@braze.com`의 별칭을 가질 수 있습니다. 이메일을 `contractor+1@braze.com`에게 보내면 여전히 `contractor@braze.com`에게 전달되지만, 별칭은 고유한 이메일 주소로 인식됩니다.

## Braze 사용자 일시 중지

사용자를 일시 중지하면 계정이 비활성 상태가 되어 더 이상 로그인할 수 없지만 계정과 관련된 데이터는 보존됩니다. 관리자만 Braze 사용자를 일시 중지하거나 일시 중지를 해제할 수 있습니다.

사용자를 일시 중지하려면 **설정** > **회사 사용자**로 이동하여 사용자 이름을 찾고 <i class="fa-solid fa-user-lock"></i> **일시 중지**를 클릭하십시오.

![사용자 정지][4]

관리자는 목록에서 사용자의 이름을 선택하고 하단의 **사용자 정지**을 클릭하여 사용자를 정지할 수도 있습니다.

![사용자 세부 정보를 편집할 때 사용자를 일시 중지합니다.][5]

## Braze 사용자 삭제

사용자를 삭제하려면 **설정** > **회사 사용자**로 이동하여 사용자 이름을 찾고 <i class="fa fa-trash-can"></i> **사용자 삭제**를 선택하십시오.

![사용자 삭제][34]

사용자가 삭제된 후 Braze는 다음 데이터 중 어느 것도 보관하지 않습니다:

- 사용자가 가지고 있던 모든 속성
- 이메일 주소
- 전화번호
- 외부 사용자 ID
- 성별
- 국가
- 언어
- 다른 유사한 데이터

[1]: {% image_buster /assets/img/add_new_user_1.png %}
[2]: {% image_buster /assets/img/add_new_user_2.png %}
[3]: {% image_buster /assets/img/add_new_user_3.png %}
[4]: {% image_buster /assets/img_archive/suspend_user.png %}
[5]: {% image_buster /assets/img_archive/suspend_user2.png %}

[27]: {% image_buster /assets/img/add-user.gif %} "새 사용자 프로세스 추가"
[34]: {% image_buster /assets/img_archive/delete_user_new.png %}