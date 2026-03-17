---
nav_title: Security settings
article_title: 보안 설정
page_order: 2
toc_headers: h2
page_type: reference
description: "이 참조 문서에서는 인증 규칙, IP 허용 목록, PII, 2단계 인증(2FA) 등 일반적인 회사 간 보안 설정에 대해 설명합니다."

---

# Security settings

> 관리자로서 보안은 귀하의 우선 사항 목록에서 높은 우선 순위입니다. **보안 설정** 페이지는 인증 규칙, IP 허용 목록 및 2단계 인증을 포함한 일반적인 회사 간 보안 설정을 관리하는 데 도움이 될 수 있습니다.

이 페이지에 액세스하려면 **설정** > **관리자 설정** > **보안 설정으로** 이동합니다.

## 인증 규칙

### 비밀번호 길이

이 필드를 사용하여 요구되는 최소 비밀번호 길이를 변경하십시오. 기본 최소 길이는 8자입니다.

### 비밀번호 복잡도

**복잡한 비밀번호 강제 적용**을 선택하여 비밀번호에 다음 중 적어도 하나를 포함하도록 요구하십시오: 
- 대문자
- 소문자
- 숫자
- 특수 문자

### 비밀번호 재사용성

사용자가 비밀번호를 재사용하기 전에 설정해야 하는 새 비밀번호의 최소 개수를 결정합니다. 기본값은 3개입니다.

### 비밀번호 만료 규칙

이 필드를 사용하여 Braze 계정 사용자가 비밀번호를 재설정할 시기를 설정할 수 있습니다.

### 세션 지속 시간 규칙

이 필드를 사용하여 Braze가 세션을 활성 상태로 유지할 기간을 정의할 수 있습니다. Braze가 귀하의 세션을 비활성으로 간주한 후(정의된 분 수 동안 활동 없음), Braze는 사용자를 로그아웃합니다. 2단계 인증이 귀하의 회사에 대해 시행되는 경우 입력할 수 있는 최대 분 수는 10,080(1주와 동일)이며, 그렇지 않으면 최대 세션 기간은 1,440분(24시간과 동일)입니다.

### 싱글 사인온(SSO) 인증

사용자가 비밀번호 또는 SSO를 사용하여 로그인하지 못하도록 제한할 수 있습니다.

For [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/), customers need to set up their SAML settings before enforcing. 고객이 Google SSO를 사용하는 경우 추가 리프트 없이 보안 설정 페이지만 적용하면 됩니다.

## 대시보드 IP 허용 목록

표시된 필드를 사용하여 사용자가 계정에 로그인할 수 있는 특정 IP 주소 및 서브넷(예: 회사 네트워크 또는 VPN)을 허용 목록에 추가할 수 있습니다. 쉼표로 구분된 목록에 IP 주소 및 서브넷을 CIDR 범위로 지정하세요. 지정되지 않은 경우 사용자는 모든 IP 주소에서 로그인할 수 있습니다.

## 2단계 인증 (2FA)

모든 회사 사용자에게 2단계 인증이 필요합니다. 계정 로그에 두 번째 수준의 신원 확인을 추가하여 사용자 이름과 비밀번호보다 더 안전하게 보호합니다. 대시보드에서 2단계 인증을 지원할 수 없는 경우에는 고객 성공 관리자에게 문의하세요. 

When two-factor authentication is turned on:

- 비밀번호를 입력하는 것 외에도 사용자는 Braze 계정에 로그인할 때 인증 코드를 입력해야 합니다. The code can be sent through an authenticator app, email, or SMS. 
- The **Remember this account for 30 days** checkbox becomes available to users.

Braze는 2단계 인증을 설정하지 못한 사용자를 Braze 계정에서 잠급니다. 또한, 관리자가 요구하지 않더라도 Braze 계정 사용자는 **계정 설정에서** 직접 2단계 인증을 설정할 수 있습니다.

페이지에서 나가기 전에 변경 사항을 저장하세요!

### Remember this account for 30 days {#remember-me}

This feature is available when two-factor authentication is turned on.

When you select **Remember this account for 30 days**, a cookie is stored on your device, only requiring you to log in with two-factor authentication once over the course of 30 days. 

![이 계정을 30일 동안 기억하기 확인란]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

대시보드 회사에서 여러 개의 계정을 보유한 고객은 쿠키가 특정 기기에 연결되어 있어 이 기능을 사용하는 데 문제가 발생할 수 있습니다. 사용자가 동일한 기기를 사용하여 여러 계정에 로그인하는 경우, 해당 기기에서 이전에 인증된 계정에 대해 쿠키가 대체됩니다. Braze는 하나의 기기가 여러 계정에 연결되는 것이 아니라 하나의 기기만 계정에 연결될 것으로 예상합니다.

### 사용자 인증 재설정하기

If you're having issues logging in with two-factor authentication, contact your company administrators to reset your two-factor authentication. Administrators can perform the following steps:

1. **설정** > **회사 사용자**.
2. 제공된 목록에서 사용자를 선택합니다.
3. **2단계 인증에서** **재설정을** 선택합니다.

재설정을 통해 인증 앱 문제, 이메일 인증 미전송, SMS 중단 또는 사용자 오류로 인한 로그인 실패 등과 같은 일반적인 인증 문제를 해결할 수 있습니다.

### 회사 수준에서의 2FA 요구 사항

먼저, **회사 설정** > **보안 설정** > **2단계 인증**으로 이동하여 대시보드에 대해 2FA가 활성화되어 있는지 확인하십시오. 토글이 회색이면 2FA가 귀하의 회사에 대해 켜지지 않았으며 모든 회사 사용자에게 의무가 아닙니다.

#### 2FA가 의무가 아닐 때 사용자 옵션

회사의 차원에서 2FA가 시행되지 않는 경우, 개별 사용자는 자신의 계정 설정 페이지에서 2FA를 설정할 수 있습니다. 이 경우 사용자가 2FA를 설정하지 않더라도 계정에서 잠기지 않습니다. 사용자가 2FA를 활성화하기로 선택한 경우 관리 사용자 페이지를 확인하여 확인할 수 있습니다.

#### 2FA가 의무일 때의 요구 사항

회사의 차원에서 2단계 인증(2FA)이 시행되는 경우, 로그인 시 자신의 계정에서 이를 설정하지 않은 사용자는 대시보드에 접근할 수 없습니다. 사용자는 접근을 유지하기 위해 2FA 설정을 완료해야 합니다.

{% alert important %}
단일 로그인(SSO)이 활성화되지 않은 경우에만 모든 회사 사용자에게 2FA가 필요합니다. SSO가 사용 중인 경우, 회사 차원에서 2FA를 시행할 필요가 없습니다.
{% endalert %}

## 2단계 인증(2FA) 설정하기

### Authy로 2FA 설정하기

1. 기기 앱 스토어에서 Authy 앱을 다운로드하세요.
2. Braze에서 전화번호를 입력하세요.
3. 기기로 전송된 알림을 탭하여 Authy 앱을 열도록 하세요.
4. 기기에서 Authy 앱을 실행하여 코드를 가져오세요.
5. Braze에서 Authy로부터 받은 인증 코드를 입력하세요.

설정 과정 중 문제가 발생하고 Braze 홈페이지나 로그인 화면으로 리디렉션되는 경우, 다음을 시도하세요:

- 시크릿 모드 또는 개인 브라우징 모드 사용하기: 시크릿 모드 또는 개인 브라우징 창에서 다시 설정을 시도하세요. 이 방법은 브라우저 확장 프로그램이나 플러그인으로 인한 문제를 우회할 수 있습니다.
- 다른 브라우저 프로필 시도하기: 문제가 지속되면 설치된 플러그인과의 충돌을 제거하기 위해 다른 브라우저 프로필을 사용하는 것을 고려하세요.

### 2FA가 시행되지 않을 때 2FA 설정하기

2FA가 시행되지 않을 때 Braze 계정에서 2단계 인증(2FA)을 수동으로 활성화하려면 다음 단계를 따르세요:

1. App Store(iOS), Google Play Store(Android) 또는 웹에서 Authy, Google Authenticator, Okta Verify와 같은 2FA 앱을 다운로드하세요. 또는 이메일이나 SMS로 2FA를 설정하는 것을 선호하는 경우, 2단계로 건너뛰십시오.
2. Braze에서 계정 관리로 이동하여 **2단계 인증** 섹션으로 스크롤한 다음 **설정 시작**을 선택하십시오.
3. 로그인 모달에 비밀번호를 입력한 다음 **비밀번호 확인**을 선택하십시오.
4. **2단계 인증 설정** 모달에서 전화번호를 입력한 다음 **활성화**를 선택하십시오.
5. 2FA 앱, 이메일 또는 SMS 메시지에서 생성된 7자리 코드를 복사한 다음 Braze로 돌아가서 **2단계 인증 설정** 모달에 붙여넣으십시오. **확인**을 선택하십시오.
6. (선택 사항) 다음 30일 동안 2FA 입력을 피하려면 **이 계정을 30일 동안 기억** 옵션을 활성화하십시오.

## 향상된 액세스

향상된 액세스 권한은 Braze 대시보드의 민감한 작업에 대한 보안을 한층 더 강화합니다. 활성화된 경우, 사용자는 세그먼트를 내보내거나 API 키를 보기 전에 계정을 다시 인증해야 합니다. 상승된 액세스를 사용하려면 **설정** > **관리자 설정** > **보안 설정으로** 이동하여 이 기능을 켜세요. 

사용자가 다시 인증할 수 없으면 중단한 지점으로 리디렉션되어 민감한 작업을 계속할 수 없습니다. 재인증에 성공하면 먼저 로그아웃하지 않는 한 다음 한 시간 동안은 다시 인증할 필요가 없습니다.

![고급 액세스 토글.]({% image_buster /assets/img/elevated_access.png %})

## 보안 이벤트 보고서 다운로드 {#security-event-report}

보안 이벤트 보고서는 계정 초대, 계정 삭제, 로그인 시도 실패 및 성공, 기타 활동 등의 보안 이벤트에 대한 CSV 보고서입니다. 내부 감사를 수행하는 데 사용할 수 있습니다.

이 보고서를 다운로드하려면 다음과 같이 하세요:

1. **설정** > **관리자 설정으로** 이동합니다.
2. **보안 설정** 탭을 선택하고 **보안 이벤트 다운로드** 섹션으로 이동합니다.
3. **보고서 다운로드**를 선택합니다. 

이 수동 보고서 다운로드에는 귀하의 계정에 대한 가장 최근의 10,000개의 보안 이벤트만 포함되어 있습니다.

이 행 제한 없이 보안 이벤트를 Amazon S3로 내보내려면 [Amazon S3로 보안 이벤트 내보내기]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/)를 참조하십시오.

{% details Reported security events %}
### 로그인 및 계정
- Signed In
- Failed Login
- Two-Factor Auth Setup Completed
- Two-Factor Auth Reset Completed
- Cleared Developer 2FA
- Added Additional Developer
- 추가된 계정
- Developer Suspended
- Developer Unsuspended
- Developer Updated
- Removed Developer
- 제거된 계정
- User Subscription Status Updated
- User Updated
- 개발자 계정 업데이트됨

### 승격된 액세스
- Started Elevated Access Flow
- Completed Elevated Access Flow
- Failed 2FA Verification For Elevated Access
- 승격된 액세스 시행 활성화
- 승격된 액세스 시행 비활성화

캠페인
- Added Campaign
- Edited Campaign

Canvas
- Added Journey
- Edited Journey

### 세그먼트
- Added Segment
- Edited Segment
- Exported data to CSV
- Exported Segment via API
- 세그먼트 사용자 삭제됨
- 코호트 지워짐

### REST API key
- Added REST API key
- Removed REST API key

### 기본 인증 자격 증명
- Added Basic Auth credential
- Updated Basic Auth credential
- Removed Basic Auth credential

### 권한
- Cleared Developer 2FA
- Updated Account Permission
- 팀 추가됨
- 팀 편집됨
- 팀 보관됨
- 팀 보관 해제됨
- 앱 그룹 권한 세트 생성됨
- 앱 그룹 권한 세트 편집됨
- 앱 그룹 권한 세트 제거됨
- 커스텀 역할 생성됨
- 커스텀 역할 업데이트됨
- 커스텀 역할 삭제됨

### 회사 설정
- Added App Group
- Added App
- Company Settings Changed
- 회사 보안 설정 업데이트됨
- 보안 이벤트 클라우드 내보내기 업데이트됨
- 랜딩 페이지 커스텀 도메인 추가됨
- 랜딩 페이지 커스텀 도메인 제거됨
- 커스텀 도메인 생성됨
- 커스텀 도메인 삭제됨
- 글로벌 컨트롤 그룹 활성화됨
- 글로벌 컨트롤 그룹 비활성화됨
- 업데이트된 글로벌 컨트롤 제외 사항
- 업데이트된 구독 그룹 SMS 허용 목록

### 이메일 템플릿
- Added Email Template
- Updated Email Template

### 푸시 자격 증명
Updated Push Credential
Removed Push Credential

### SDK 디버거
- Started SDK Debugger Session
- Exported SDK Debugger Log

### Users
- 삭제된 사용자
- 조회된 사용자
- 사용자 가져오기 시작됨
- 사용자 구독 그룹 상태 업데이트됨
- 사용자가 삭제됨
- 단일 사용자 삭제 취소됨
- 대량 사용자 삭제 취소됨

### 카탈로그
- 카탈로그 생성됨
- 카탈로그 삭제됨

### Braze 에이전트
- 에이전트 생성됨
- 에이전트 편집됨

### BrazeAI 운영자 
- 요청된 BrazeAI 운영자 응답
- BrazeAI 운영자가 응답함
{% enddetails %}

## 개인 식별 정보(PII) 보기 {#view-pii}

**PII 보기** 권한은 몇몇 선택된 회사 사용자만 접근할 수 있습니다. By default, all admins have their **View PII** permission turned on in user permissions. 이는 그들이 대시보드 전반에 걸쳐 귀사가 PII로 정의한 모든 표준 및 커스텀 속성을 볼 수 있음을 의미합니다. 이 권한이 사용자에게 꺼져 있을 경우, 해당 사용자는 이러한 속성을 볼 수 없습니다.

{% alert note %}
**PII 보기** 권한이 필요합니다 [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/)를 사용하려면, 이는 일부 고객 데이터에 직접 접근할 수 있게 해줍니다.
{% endalert %}

For the existing team permission capabilities, refer to [Setting user permissions]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### PII 정의

{% alert important %}
특정 필드를 PII 필드로 선택하고 정의하는 것은 Braze 대시보드에서 사용자가 볼 수 있는 것에만 영향을 미치며, 그러한 PII 필드의 최종 사용자 데이터 처리 방식에는 영향을 미치지 않습니다.<br><br>귀사의 대시보드 설정을 귀사에 적용되는 모든 개인정보 보호 규정 및 정책, 특히 [데이터 보존]({{site.baseurl}}/data_retention/)과 관련된 규정 및 정책에 맞추기 위해 법무팀에 상담하십시오.
{% endalert %}

대시보드에서 귀사가 PII로 지정한 필드를 선택할 수 있습니다. 이를 위해 **회사 설정** > **관리자 설정** > **보안 설정**으로 이동하십시오.

다음 속성은 PII로 지정될 수 있으며 **PII 보기** 권한이 없는 회사 사용자에게 숨겨질 수 있습니다.

#### 잠재적 PII 속성

| Standard attributes | 사용자 지정 속성 |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>이메일 주소 </li> <li> 전화번호 </li> <li> 이름 </li> <li> 성 </li> <li> 성별 </li> <li> 생년월일 </li> <li> 기기 ID </li> <li> 가장 최근 위치 </li> </ul> {:/} | {::nomarkdown} <ul> <li> 모든 사용자 지정 속성<ul><li>모든 속성을 숨길 필요가 없는 경우 개별 사용자 지정 속성을 PII로 표시할 수 있습니다.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 제한된 영역

다음은 모든 필드가 PII로 설정되어 있다고 가정하며, 언급된 사용자는 Braze 플랫폼을 사용하는 회사 사용자입니다. 또한, "선행" 속성은 [잠재적 PII 속성](#potential-pii-attributes) 표에 있는 속성을 의미합니다. 사용자에게 PII 권한을 제거하면 나열된 영역을 넘어 사용성에 영향을 미칠 수 있습니다.

| 대시보드 탐색 | 결과 | 참고 |
| -------------------- | ------ | ----- |
| 사용자 검색 | 로그인한 사용자는 이메일 주소, 전화번호, 이름 또는 성으로 검색할 수 없습니다({::nomarkdown}) <ul> <li> 사용자 프로필을 볼 때 선행 표준 및 커스텀 속성이 표시되지 않습니다. </li> <li> Braze 대시보드에서 사용자 프로필의 선행 표준 속성을 편집할 수 없습니다. </li> <li> 사용자 프로필의 구독 상태를 업데이트할 수 없습니다. </li></ul> {:/} | 이 섹션에 접근하려면 여전히 사용자 프로필을 볼 수 있는 접근 권한이 필요합니다. |
| 사용자 가져오기 | 사용자는 **사용자 가져오기** 페이지에서 파일을 다운로드할 수 없습니다. | |
| {::nomarkdown} <ul> <li> 세그먼트 </li> <li> 캠페인 </li> <li> 캔버스 </li> </ul> {:/} | **사용자 데이터** 드롭다운에서: {::nomarkdown} <ul> <li> 사용자에게는 <b>CSV 이메일 주소 내보내기</b> 옵션이 없습니다. </li> <li> 사용자가 <b>CSV 내보내기 사용자 데이터</b>를 선택할 때 CSV 파일에서 선행 표준 및 커스텀 속성이 제공되지 않습니다. </li> </ul> {:/} | |
| 내부 테스트 그룹 | 사용자는 내부 테스트 그룹에 추가된 모든 사용자의 이전 표준 속성에 액세스할 수 없습니다. | |
| 메시지 활동 로그 | 사용자는 메시지 활동 로그에서 식별된 모든 사용자에 대해 앞의 표준 속성에 액세스할 수 없습니다. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
메시지를 미리 볼 때 **PII 보기** 권한이 적용되지 않으므로, 사용자는 Liquid를 통해 메시지에 참조된 경우 [선행 표준 속성](#potential-pii-attributes)을 볼 수 있습니다.
{% endalert %}

## 데이터 삭제 기본 설정 

이 설정을 사용하여 Braze가 이벤트에 대한 사용자 삭제 프로세스 중 특정 필드를 삭제해야 하는지에 대한 기본 설정을 설정할 수 있습니다. 이 기본 설정은 Braze가 삭제한 사용자에 대한 데이터에만 영향을 미칩니다. 

When a user is deleted, Braze removes all PII from event data but retains the anonymized data for analytics purposes. 최종 사용자 정보를 Braze에 전송하는 경우 일부 사용자 정의 필드에 PII가 포함될 수 있습니다. 이 필드에 PII가 포함되어 있는 경우, Braze가 삭제된 사용자의 이벤트 데이터를 익명화할 때 데이터를 삭제하도록 선택할 수 있습니다. 필드에 PII가 포함되어 있지 않은 경우, 분석을 위해 필드를 유지할 수 있습니다.

워크스페이스에 대한 올바른 환경설정을 결정하는 것은 회원님의 책임입니다. 적절한 설정을 결정하는 가장 좋은 방법은 이벤트 데이터를 Braze로 전송하는 내부 팀과 Braze에서 메시지 추가 기능을 사용하는 팀과 함께 검토하여 필드에 PII가 포함될 수 있는지 확인하는 것입니다.  

### 관련 필드  

| 이벤트 이름 또는 유형 | 필드 | 참고 |
| -------------------- | ------ | ----- |
| 사용자 지정 이벤트 | 등록정보 |  |
| 구매 이벤트 | 등록정보 |  |
| 메시지 보내기 | message_extras | Several event types contain a `message_extras` field. The preference applies to all message send event types that support `message_extras`, including event types added in the future. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**삭제는 영구적입니다!** 삭제된 사용자에 대해 Snowflake에서 필드를 제거하기로 선택하면, 이 설정은 귀하의 작업 공간의 모든 역사적 데이터와 미래에 삭제된 사용자에 대한 모든 이벤트에 적용됩니다. Braze가 삭제된 사용자의 과거 이벤트 데이터에 설정을 적용하는 프로세스를 실행한 후, **복원할 수 없습니다**.
{% endalert %}

### 환경설정 구성

사용자가 삭제될 경우 Braze가 제거해야 할 필드에 대한 기본 설정을 체크하여 설정하십시오. PII가 포함된 필드를 선택합니다. 이 기본 설정은 작업 공간이 기본 설정 그룹에 명시적으로 추가되지 않는 한 모든 현재 및 미래의 작업 공간에 적용됩니다.

To customize preferences by workspace, you may add preference groups with different settings from the default. 향후에 생성되는 워크스페이스를 포함하여 추가 환경설정 그룹에 추가되지 않은 모든 워크스페이스에는 기본 설정이 적용됩니다.  

![작업 공간별 데이터 삭제 기본 설정을 사용자 정의하기 위해 토글이 켜진 데이터 삭제 기본 설정 섹션입니다.]({% image_buster /assets/img/deletion_preferences_1.png %})

## 문제 해결 

### 2단계 인증(2FA) 설정 루프 문제

2FA를 위해 전화번호를 성공적으로 입력한 후 루프에 갇히고 로그인 페이지로 리디렉션되는 경우, 이는 첫 번째 시도에서 확인하지 못했기 때문일 수 있습니다. 이 문제를 해결하려면 다음 단계를 따르십시오:

1. 모든 광고 차단기를 끄십시오.
2. 브라우저 설정에서 쿠키를 활성화하십시오.
3. PC 또는 노트북을 재시작하십시오.
4. 다시 2FA를 설정해 보십시오.

이 단계 후에도 문제가 지속되면 [지원]({{site.baseurl}}/braze_support/)에 문의하여 도움을 받으십시오.

### 2단계 인증(2FA)을 활성화할 수 없습니다.

2FA가 활성화되어 있지만 **활성화** 버튼을 선택해도 아무런 반응이 없다면, 이는 브라우저가 SMS를 통해 인증 코드를 전송하는 데 필요한 리디렉션을 차단하고 있기 때문일 수 있습니다. 이 문제를 해결하기 위한 단계는 다음과 같습니다:

1. 브라우저에서 활성화된 모든 광고 차단기를 일시적으로 중단하십시오.
2. 브라우저 설정에서 서드파티 쿠키를 활성화했는지 확인하십시오.
3. 2FA를 설정해 보십시오.

### 인증 코드가 전송되지 않음

Authy 페이지에서 전화번호를 입력할 때 문제가 발생하고 SMS를 받지 못하는 경우, 다음 단계를 따르십시오:

1. 휴대폰에 Authy 앱을 설치하고 Authy 인증기에 로그인하세요.
2. 전화번호를 입력하고 Authy 앱에서 변경 사항이나 SMS 알림을 확인하세요.
3. 여전히 SMS를 받지 못하면, 집 네트워크나 비기업 Wi-Fi와 같은 다른 네트워크 연결을 사용해 보세요. 기업 네트워크는 SMS 전달에 방해가 되는 보안 정책을 가질 수 있습니다.

문제가 지속되면 Authy 앱에서 이전 프로필을 삭제하고 QR 코드를 다시 스캔하여 2FA를 설정하세요. 다시 설정을 시도하기 전에 광고 차단기를 비활성화하고, 서드파티 쿠키를 활성화하거나 다른 브라우저를 사용했는지 확인하세요.