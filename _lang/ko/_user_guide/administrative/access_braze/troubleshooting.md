---
nav_title: 문제 해결
article_title: Braze 액세스 문제 해결
page_order: 8
page_type: reference
description: "이 문서에서는 Braze에 액세스하려고 할 때 발생할 수 있는 문제 해결 방법을 안내합니다."

---

# Braze 액세스 문제 해결

> 이 도움말은 Braze에 액세스하려고 할 때 발생할 수 있는 문제를 해결하는 데 도움이 됩니다.

## 계정 잠김

Braze 계정이 잠겼더라도 걱정하지 마세요! 다시 참여할 수 있도록 도와드리겠습니다.	

어떤 종류의 잠금이 발생했는지는 오류 메시지로 확인할 수 있습니다.	

- [비밀번호 관련 오류가 표시됩니다.](#password-error)	
- [오류는 표시되지 않지만 여전히 Braze가 나를 허용하지 않습니다.](#instance-error)	
- [계정 일시 정지에 대한 오류가 표시됩니다.](#account-suspension)	

### 비밀번호 오류

계정 보안은 당사에 매우 중요하므로 Braze 계정에 로그인하려면 비밀번호가 필요합니다.	
- 올바른 [Braze 대시보드 인스턴스에]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) 로그인하고 있는지 확인합니다. 계정 관리자 또는 Braze 계정 관리자에게 문의하여 확인하세요.	
- 비밀번호가 만료되었을 수 있으므로 비밀번호를 [재설정해야]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password) 합니다.	
- [통합]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) 인증 서비스를 사용하는 경우 계정 관리자에게 설정이 제대로 완료되었는지 확인하세요.	
- 회사에서 여러 개의 Braze 인스턴스를 사용 중인 경우 잘못된 이메일을 사용하여 로그인하고 있을 수 있습니다.  	

확실하지 않은 경우 언제든지 [비밀번호를 재설정할]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password) 수 있습니다.	

### 인스턴스 오류

평소 로그인할 때 사용하는 것과 동일한 기기를 사용하는 경우, Braze는 자동으로 올바른 인스턴스를 감지합니다. 그러나 그렇지 않거나 처음 로그인하는 경우 다음 사항을 고려하는 것이 좋습니다:	

- 올바른 [Braze 대시보드 인스턴스에]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances) 로그인하고 있는지 확인합니다. 계정 관리자 또는 Braze 계정 관리자에게 문의하여 확인하세요.
- 회사에서 여러 개의 Braze 인스턴스를 사용 중인 경우 잘못된 이메일을 사용하여 로그인하고 있을 수 있습니다.	

### 계정 일시 정지	

이런 일이 자주 발생하지는 않지만 일시 정지 및 삭제는 매우 심각하게 고려하고 있습니다. 이 오류가 발생하면 회사의 Braze 관리자, Braze 계정 관리자 또는 [지원]] [지원]]으로 문의하시기 바랍니다.

## Braze 대시보드가 로드되지 않거나 예상대로 작동하지 않습니다.

먼저, 대시보드가 다른 브라우저에서 로드되는지 테스트합니다. 다른 브라우저에서도 문제가 해결되지 않으면 다음을 시도해 보세요:

- **대시보드를 다시 시작합니다:** 로그아웃하고 브라우저를 종료한 다음 대시보드에 로그인을 시도합니다.
- **로컬 브라우저를 새로 고칩니다:** [쿠키와 브라우저 캐시를 지운]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies) 다음 대시보드에 다시 로그인해 보세요.
- **호환되는 플러그인 또는 타사 도구를 사용합니다:** 광고 차단기나 보안 소프트웨어로 인해 Braze 대시보드가 로드되지 않을 수 있습니다. 광고 차단기를 비활성화한 다음 Braze 대시보드에 로그인하여 테스트해 보세요.
        \- 브라우저 콘솔 로그도 확인할 수 있습니다. `ERR_BLOCKED_BY_CLIENT` 관련 오류는 콘텐츠가 광고 차단기에 의해 차단되었음을 나타낼 수 있습니다.
- **연결 품질을 확인하세요:** 연결 품질이 좋지 않을 수 있습니다. 다른 기기에서 Braze 대시보드에 로그인해 보세요.
- **올바른 클러스터에 액세스하고 있는지 확인합니다:** 회사에 할당된 클러스터에 로그인하고 있는지 확인하세요. 예를 들어 US-03에 배정되었지만 US-01에 로그인하는 경우입니다.
- **브라우저를 업데이트하세요:** [지원되는]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers) 최신 브라우저로 브라우저를 업데이트한 다음 대시보드에 로그인을 시도합니다.

모든 브라우저에서 문제가 발생하면 다음을 시도해 보세요:

- **네트워크 연결을 확인하세요:** 가능하면 VPN을 끄거나 네트워크 연결을 비활성화했다가 다시 활성화하세요.
- **장치를 다시 시작합니다:** 디바이스를 재시작한 후 Braze 대시보드에 로그인해 보세요.

이전 문제를 해결했는데도 대시보드가 여전히 로드되지 않거나 예상대로 작동하지 않는 경우 [지원팀에]({{site.baseurl}}/braze_support/) 문의하세요.


