---
nav_title: 보안 설정
article_title: 보안 설정
page_order: 2
page_type: reference
description: "이 참조 문서에서는 인증 규칙, IP 허용 목록, PII, 2단계 인증(2FA) 등 일반적인 회사 간 보안 설정에 대해 설명합니다."

---

# 보안 설정

> 관리자에게 보안은 가장 우선적으로 고려해야 할 사항입니다. **보안 설정** 페이지에서는 인증 규칙, IP 허용 목록, 2단계 인증 등 일반적인 회사 간 보안 설정을 관리할 수 있습니다.

이 페이지에 액세스하려면 **설정** > **관리자 설정** > **보안 설정으로** 이동합니다.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 계정 드롭다운을 선택하고 **회사 설정** > **보안 설정으로** 이동합니다.
{% endalert %}

## 인증 규칙

### 비밀번호 길이

이 필드를 사용하여 필요한 최소 비밀번호 길이를 변경할 수 있습니다. 기본 최소값은 8자입니다.

### 비밀번호 복잡도

**복잡한 비밀번호 적용을** 선택하여 비밀번호에 다음 중 하나 이상을 포함하도록 요구합니다: 
- 대문자
- 소문자
- 숫자
- 특수 문자

### 비밀번호 재사용 여부

사용자가 비밀번호를 재사용하기 전에 설정해야 하는 새 비밀번호의 최소 개수를 결정합니다. 기본값은 3개입니다.

### 비밀번호 만료 규칙

이 필드를 사용하여 Braze 계정 사용자가 비밀번호를 재설정할 시기를 설정할 수 있습니다.

### 세션 지속 시간 규칙

이 필드를 사용하여 Braze가 세션을 활성 상태로 유지할 기간을 정의할 수 있습니다. Braze에서 세션이 비활성 상태(정해진 시간 동안 활동이 없는 상태)로 간주되면 사용자는 로그아웃됩니다. 회사에 2단계 인증을 적용하는 경우 입력할 수 있는 최대 시간은 10,080분(1주일에 해당)이며, 그렇지 않은 경우 최대 세션 시간은 1,440분(24시간에 해당)입니다.

### 싱글 사인온(SSO) 인증

사용자가 비밀번호 또는 SSO를 사용하여 로그인하지 못하도록 제한할 수 있습니다.

[SAML SSO][15]의 경우, 고객은 적용하기 전에 SAML 설정을 설정해야 합니다. 고객이 Google SSO를 사용하는 경우 추가 리프트 없이 보안 설정 페이지만 적용하면 됩니다.

## 대시보드 IP 허용 목록

표시된 필드를 사용하여 사용자가 계정에 로그인할 수 있는 특정 IP 주소 및 서브넷(예: 회사 네트워크 또는 VPN)을 허용 목록에 추가할 수 있습니다. 쉼표로 구분된 목록에 IP 주소 및 서브넷을 CIDR 범위로 지정하세요. 이를 지정하지 않으면, 사용자는 모든 IP 주소에서 로그인할 수 있게 됩니다.

## 2단계 인증

모든 Braze 사용자에게는 2단계 인증이 필요합니다. 계정 로그에 두 번째 수준의 신원 확인을 추가하여 사용자 이름과 비밀번호보다 더 안전하게 보호합니다. 대시보드에서 2단계 인증을 지원할 수 없는 경우에는 고객 성공 관리자에게 문의하세요. 

2단계 인증이 켜져 있는 경우, 사용자는 비밀번호 입력 외에도 Braze 계정에 로그인할 때 인증 코드를 입력해야 합니다. 코드는 인증 앱, 이메일 또는 SMS를 통해 전송할 수 있습니다.

2단계 인증을 설정하지 않은 사용자는 Braze 계정에서 잠기게 됩니다. 또한, 관리자가 요구하지 않더라도 Braze 계정 사용자는 **계정 설정에서** 직접 2단계 인증을 설정할 수 있습니다.

### 기억해 주세요

![이 계정을 30일 동안 기억하기 확인란][04]{: style="float:right;max-width:40%;margin-left:15px;"}

회사에서 2단계 인증을 사용 설정하면 사용자가 **나를 기억하기** 확인란을 사용할 수 있게 됩니다. 이 기능은 기기에 쿠키를 저장하여 30일 동안 2단계 인증으로 한 번만 로그인하면 됩니다.

대시보드 회사에서 여러 개의 계정을 보유한 고객은 쿠키가 특정 기기에 연결되어 있어 이 기능을 사용하는 데 문제가 발생할 수 있습니다. 사용자가 동일한 기기를 사용하여 여러 계정에 로그인하는 경우, 해당 기기에서 이전에 인증된 계정에 대해 쿠키가 대체됩니다. Braze는 하나의 기기가 여러 계정에 연결되는 것이 아니라 하나의 기기만 계정에 연결될 것으로 예상합니다.

페이지에서 나가기 전에 변경 사항을 저장하세요!

### 사용자 인증 재설정하기

2단계 인증으로 로그인하는 데 문제가 있는 사용자는 회사 관리자에게 문의하여 2단계 인증을 재설정할 수 있습니다. 이렇게 하려면 관리자에게 다음 단계를 수행하도록 합니다:

1. **설정** > **회사 사용자**.
2. 제공된 목록에서 사용자를 선택합니다.
3. **2단계 인증에서** **재설정을** 선택합니다.

재설정을 통해 인증 앱 문제, 이메일 인증 미전송, SMS 중단 또는 사용자 오류로 인한 로그인 실패 등과 같은 일반적인 인증 문제를 해결할 수 있습니다.

## 향상된 액세스

향상된 액세스 권한은 Braze 대시보드의 민감한 작업에 대한 보안을 한층 더 강화합니다. 활성화된 경우, 사용자는 세그먼트를 내보내거나 API 키를 보기 전에 계정을 다시 인증해야 합니다. 상승된 액세스를 사용하려면 **설정** > **관리자 설정** > **보안 설정으로** 이동하여 이 기능을 켜세요. 

사용자가 다시 인증할 수 없으면 중단한 지점으로 리디렉션되어 민감한 작업을 계속할 수 없습니다. 재인증에 성공하면 먼저 로그아웃하지 않는 한 다음 한 시간 동안은 다시 인증할 필요가 없습니다.

![고급 액세스 토글.][5]

## 보안 이벤트 보고서 다운로드하기

보안 이벤트 보고서는 계정 초대, 계정 삭제, 로그인 시도 실패 및 성공, 기타 활동 등의 보안 이벤트에 대한 CSV 보고서입니다. 내부 감사를 수행하는 데 사용할 수 있습니다.

이 보고서를 다운로드하려면 다음과 같이 하세요:

1. **설정** > **관리자 설정으로** 이동합니다.
2. **보안 설정** 탭을 선택하고 **보안 이벤트 다운로드** 섹션으로 이동합니다.
2. **보고서 다운로드**를 선택합니다. 

이 보고서에는 계정에 대한 가장 최근 10,000건의 보안 이벤트만 포함되어 있습니다. 특정 이벤트 데이터가 필요한 경우 기술 지원팀에 문의하세요.

{% details 보고된 보안 이벤트 %}
### 로그인 및 계정 
- Removed Developer
- Added Additional Developer
- Signed In
- Failed Login
- Two-Factor Auth Setup Completed
- Two-Factor Auth Reset Completed
- Cleared Developer 2FA
- Developer Suspended
- Developer Unsuspended

### 향상된 액세스
- Started Elevated Access Flow
- Completed Elevated Access Flow
- Failed 2FA Verification For Elevated Access

### 캠페인
- Added Campaign
- Edited Campaign

### 캔버스
- Added Journey
- Edited Journey

### 세그먼트
- Added Segment
- Edited Segment
- Exported data to CSV
- Exported Segment via API

### REST API 키
- Added REST API key
- Removed REST API key

### 기본 인증 자격증명
- Added Basic Auth credential
- Updated Basic Auth credential
- Removed Basic Auth credential

### 권한
- Cleared Developer 2FA
- Updated Account Permission

### 회사 설정
- Added App Group
- Added App

### 이메일 템플릿
- Added Email Template
- Updated Email Template

### 푸시 자격증명
- Updated Push Credential
- Removed Push Credential

### SDK 디버거
- Started SDK Debugger Session
- Exported SDK Debugger Log
{% enddetails %}

## 개인 식별 정보(PII) 보기 {#view-pii}

**PII 보기** 권한은 엄선된 일부 Braze 사용자만 액세스할 수 있습니다. 기존 팀 권한 기능에 대해서는 [사용자 권한 설정하기를]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions) 참조하세요.

기본적으로 모든 관리자는 [사용자 권한에서]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions) **PII 보기** 권한이 켜져 있습니다. 즉, 대시보드 전체에서 다음과 같은 표준 및 커스텀 속성을 볼 수 있습니다. 사용자에 대해 이 권한을 해제하면 해당 사용자는 이 정보를 볼 수 없습니다.

### PII 정의

대시보드에서 어떤 필드를 PII로 지정할지 정의할 수 있습니다. 이렇게 하려면 **회사 설정** > **보안 설정으로** 이동합니다.

다음 필드는 **PII 보기** 권한이 없는 Braze 사용자로부터 숨길 수 있습니다.

| 표준 속성 | 사용자 지정 속성 |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>이메일 주소 </li> <li> 전화번호 </li> <li> 이름 </li> <li> 성 </li> <li> 성별 </li> <li> 생년월일 </li> <li> 기기 ID </li> <li> 가장 최근 위치 </li> </ul> {:/} | {::nomarkdown} <ul> <li> 모든 사용자 지정 속성<ul><li>모든 속성을 숨길 필요가 없는 경우 개별 사용자 지정 속성을 PII로 표시할 수 있습니다.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 제한된 영역

다음은 모든 필드가 PII로 설정되어 있고 언급된 사용자가 Braze 플랫폼을 사용하는 사용자라고 가정합니다.

| 대시보드 탐색 | 결과 | 참고 |
| -------------------- | ------ | ----- |
| 사용자 검색 | 로그인한 사용자는 이메일 주소, 전화번호, 이름 또는 성으로 검색할 수 없습니다({::nomarkdown}) <ul> <li> 사용자 프로필을 볼 때 앞의 표준 및 사용자 지정 속성이 표시되지 않습니다. </li> <li> Braze 대시보드에서 사용자 프로필의 이전 표준 속성을 편집할 수 없습니다. </li> </ul> {:/} | 이 섹션에 액세스하려면 여전히 고객 프로필을 볼 수 있는 액세스 권한이 필요합니다. |
| 사용자 가져오기 | 사용자는 **사용자 가져오기** 페이지에서 파일을 다운로드할 수 없습니다. | |
| {::nomarkdown} <ul> <li> 세그먼트 </li> <li> 캠페인 </li> <li> 캔버스 </li> </ul> {:/} | **사용자 데이터** 드롭다운에서: {::nomarkdown} <ul> <li> 사용자에게는 <b>CSV 이메일 주소 내보내기</b> 옵션이 없습니다. </li> <li> <b>CSV 사용자 데이터 내보내기</b>를 선택하면 CSV 파일에 앞의 표준 및 커스텀 속성이 제공되지 않습니다. </li> </ul> {:/} | |
| 내부 테스트 그룹 | 사용자는 내부 테스트 그룹에 추가된 모든 사용자의 이전 표준 속성에 액세스할 수 없습니다. | |
| 메시지 활동 로그 | 사용자는 메시지 활동 로그에서 식별된 모든 사용자에 대해 앞의 표준 속성에 액세스할 수 없습니다. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
메시지를 미리 볼 때 **PII 보기** 권한은 적용되지 않으므로 사용자는 Liquid를 통해 메시지에서 참조된 경우 이전 표준 속성을 볼 수 있습니다.
{% endalert %}

## 데이터 삭제 기본 설정 

이 설정을 사용하여 이벤트에 대한 사용자 삭제 프로세스 중에 특정 필드를 삭제할지 여부에 대한 기본 설정을 지정할 수 있습니다. 이러한 환경설정은 Braze에서 삭제된 사용자의 데이터에만 영향을 미칩니다. 

사용자가 삭제되면 Braze는 이벤트 데이터에서 모든 PII를 제거하지만 익명화된 데이터는 분석 목적으로 유지합니다. 최종 사용자 정보를 Braze에 전송하는 경우 일부 사용자 정의 필드에 PII가 포함될 수 있습니다. 이러한 필드에 PII가 포함된 경우 삭제된 사용자에 대한 이벤트 데이터가 익명화될 때 데이터를 삭제하도록 선택할 수 있으며, 필드에 PII가 포함되지 않은 경우 분석을 위해 해당 필드를 유지할 수 있습니다.

워크스페이스에 대한 올바른 환경설정을 결정하는 것은 회원님의 책임입니다. 적절한 설정을 결정하는 가장 좋은 방법은 이벤트 데이터를 Braze로 전송하는 내부 팀과 Braze에서 메시지 추가 기능을 사용하는 팀과 함께 검토하여 필드에 PII가 포함될 수 있는지 확인하는 것입니다.  

### 관련 필드  

| 이벤트 이름 또는 유형 | 필드 | 참고 |
| -------------------- | ------ | ----- |
| 사용자 지정 이벤트 | 등록정보 |  |
| 구매 이벤트 | 등록정보 |  |
| 메시지 보내기 | message_extras | 여러 이벤트 유형에 message_extras 필드가 포함되어 있습니다. 이 기본 설정은 향후 추가되는 이벤트 유형을 포함하여 message_extras를 지원하는 모든 메시지 보내기 이벤트 유형에 적용됩니다. |

{% alert warning %}
**삭제는 영구적입니다!** 삭제된 사용자에 대해 Snowflake에서 필드를 제거하도록 선택하면 이 설정은 워크스페이스의 모든 기록 데이터와 향후 삭제된 사용자에 대한 모든 이벤트에 적용됩니다. Braze가 삭제된 사용자의 과거 이벤트 데이터에 설정을 적용하는 프로세스를 실행한 후에는 데이터를 **복원할 수 없습니다**.
{% endalert %}

### 환경설정 구성

사용자가 삭제될 경우 제거해야 하는 필드의 확인란을 선택하여 기본 설정을 설정합니다. PII가 포함된 필드를 선택합니다. 이 환경설정은 워크스페이스를 환경설정 그룹에 명시적으로 추가하지 않는 한 현재 및 미래의 모든 워크스페이스에 적용됩니다.

작업 공간별로 환경설정을 사용자 지정하려면 기본 설정과 다른 설정으로 환경설정 그룹을 추가할 수 있습니다. 향후에 생성되는 워크스페이스를 포함하여 추가 환경설정 그룹에 추가되지 않은 모든 워크스페이스에는 기본 설정이 적용됩니다.  

![데이터 삭제 기본 설정 섹션에서 토글을 켜서 작업 공간별 데이터 삭제 기본 설정을 사용자 지정할 수 있습니다.]({% image_buster /assets/img/deletion_preferences_1.png %})


[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"
[5]: {% image_buster /assets/img/elevated_access.png %}
[04]: {% image_buster /assets/img/remember_me.png %}
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
