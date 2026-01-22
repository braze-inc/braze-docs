---
nav_title: 사용자 관리
article_title: LINE 사용자 관리
page_order: 0
description: "이 문서에서는 LINE 사용자 ID와 설정 방법에 대해 설명합니다."
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINE 사용자 관리

> LINE 사용자 ID는 `native_line_id` 라는 고객 프로필 속성에 저장되며, 이 속성은 LINE 채널에서 사용자에게 메시지를 보낼 때 사용됩니다. 이 문서에서는 `native_line_id` 속성을 설정하고 찾는 방법에 대해 설명합니다.

고객 사용자 데이터는 [Braze 사용자 프로필에]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) 표시됩니다. 고객 프로필에는 이름, 이메일 주소 등 회사 사용자에 대한 정보와 속성이 저장됩니다. 

Braze를 통해 LINE 메시지를 보낼 때, Braze는 `native_line_id` 속성을 사용하여 메시지를 보낼 사용자를 식별합니다. 사용자가 채널을 팔로우하거나 메시지에 답장하는 등 LINE에서 Braze 간 웹훅 이벤트를 전송할 때, `native_line_id` 을 통해 해당 사용자 프로필을 조회합니다.

{% alert note %}
LINE 사용자 ID는 LINE 제공자별로 구분됩니다. 특정 사용자는 팔로우하는 각 서비스 제공자마다 다른 LINE 사용자 ID를 갖게 됩니다. 사용자는 이메일이나 전화번호와 달리 LINE ID는 팔로우하는 브랜드마다 변경되기 때문에 이를 모를 가능성이 높습니다.
{% endalert %}

## `native_line_id` 속성 설정

고객 프로필에 `native_line_id` 이 설정되는 시나리오는 다음과 같이 여러 가지가 있습니다.

| 시나리오 | 고객 프로필이 다음과 함께 존재하는지 여부 `native_line_id` | 결과 |
| --- | --- | --- |
|사용자가 LINE 채널을 팔로우하는 경우 | 아니요| 익명 사용자 프로필이 생성됩니다(병합이 필요합니다):<br> - `native_line_id` 은 사용자의 LINE ID로 설정됩니다. <br>- `line_id` 사용자 별칭 지정은 사용자의 LINE ID로 설정됩니다.<br>\- 사용자가 채널의 Braze 구독 그룹에 가입되어 있습니다. |
|사용자가 LINE 채널을 팔로우하는 경우| 예 | `native_line_id` 이 있는 모든 고객 프로필:<br>\- 채널의 Braze 구독 그룹에 가입한 경우|
|회사는 n`ative_line_id` 열이 있는 사용자 CSV 업로드를 사용합니다.| 아니요| 지정된 `external_id` 또는 사용자 별칭 지정에 대한 사용자 프로필이 없는 경우:<br>- `native_line_id` 은 지정된 값으로 설정됩니다.<br> \- CSV에 지정된 다른 모든 속성은 고객 프로필에 설정됩니다.|
|회사는 `native_line_id` 열과 함께 사용자 CSV 업로드를 사용합니다. | 예 | 지정된 `external_id` 또는 사용자 별칭에 대한 사용자 프로필이 있는 경우:<br>- `native_line_id` 은 지정된 값으로 설정됩니다.<br>\- CSV에 지정된 다른 모든 속성은 고객 프로필에 설정됩니다.<br>\- 여러 프로필에 동일한 `native_line_id` |
| 회사는 `/users/track` 엔드포인트를 사용하고 `native_line_id` 속성을 지정합니다. | 아니요 | 지정된 사용자[( `external_id`]({{site.baseurl}}/api/objects_filters/user_attributes_object/),[ `user_alias`,]({{site.baseurl}}/api/objects_filters/user_attributes_object/)[ `braze_id` 또는 `email` 에서 지정한]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 사용자[)]({{site.baseurl}}/api/objects_filters/user_attributes_object/)에 대한 고객 프로필이 없는 경우:<br>- `native_line_id` 은 지정된 값으로 설정됩니다.<br>\- 요청에 지정된 다른 모든 속성은 고객 프로필에 설정됩니다. |
| 회사는 `/users/track` 엔드포인트를 사용하고 `native_line_id` 속성을 지정합니다. | 예 | 지정된 사용자[( `external_id`]({{site.baseurl}}/api/objects_filters/user_attributes_object/),[ `user_alias`,]({{site.baseurl}}/api/objects_filters/user_attributes_object/)[ `braze_id` 또는 `email` 에서 지정)에]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 대한 고객 프로필이 있는 경우:<br>- `native_line_id` 은 지정된 값으로 설정됩니다.<br>\- 요청에 지정된 다른 모든 속성은 고객 프로필에 설정됩니다.<br>\- 여러 프로필에 동일한 `native_line_id` |
| 회사에서 Braze에 구독 상태 동기화 실행을 요청합니다. | 아니요 | Braze에 해당 사용자 프로필이 없는 LINE에서 사용자 LINE ID가 반환되면 익명 사용자 프로필이 생성됩니다:<br>- `native_line_id` 은 사용자의 LINE ID로 설정됩니다.<br>- `line_id` 사용자 별칭 지정은 사용자의 LINE ID로 설정됩니다.<br>\- 사용자가 채널의 Braze 구독 그룹에 가입되어 있습니다.<br><br>나중에 동일한 LINE ID를 가진 사용자가 생성되면 중복 사용자가 발생하지만, 두 사용자 모두 올바른 LINE 가입 상태를 유지합니다. 이러한 경우 사용자 병합을 통해 사용자 기반을 정리할 수 있습니다. |
| 회사에서 Braze에 구독 상태 동기화 실행을 요청합니다. | 예 | LINE에서 해당 고객 프로필이 있는 사용자 LINE ID가 Braze에 반환된 경우:<br>\- 사용자가 채널의 Braze 구독 그룹에 가입되어 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## 찾기 `native_line_id`

Braze 대시보드에서 고객 프로필을 볼 때, **참여** 탭 > **연락처 설정** 섹션 > **LINE** 섹션으로 이동하여 `native_line_id` 속성이 설정되어 있는지 확인할 수 있습니다.

`native_line_id` 을 설정한 경우 **LINE 사용자 ID** 아래에 표시됩니다. 그렇지 않으면 표시되지 않습니다.

참여 탭에서 회선 연락처 설정을 클릭합니다.]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}

