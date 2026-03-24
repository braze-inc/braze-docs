{% if include.content == "Differences" %}

[Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), [권한 세트]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) 및 [사용자 역할을]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) 사용하여 Braze 내에서 회사 사용자 접근 권한과 책임을 관리할 수 있습니다. 각 기능에는 서로 다른 권한 및 액세스 제어 컬렉션이 포함되어 있습니다.

### 주요 차이점

크게 보면 각 기능의 범위가 다릅니다:
- 권한 집합은 회사 사용자가 모든 작업 영역에서 수행할 수 있는 작업을 제어합니다.
- 역할은 회사 사용자가 특정 작업 공간에서 수행할 수 있는 작업을 제어합니다.
- Teams는 회사 사용자가 메시지로 도달할 수 있는 오디언스를 관리합니다.

| Feature | 할 수 있는 작업 | 접근 범위 |
| - | - | - |
| [권한 세트]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | 특정 주제 영역이나 작업(예: "개발자" 및 "마케터")과 관련된 권한을 묶은 다음, 서로 다른 작업 공간에서 동일한 권한이 필요한 회사 사용자에게 적용하십시오. | 전사적으로 |
| [역할]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | 개별 커스텀 권한과 작업 공간 접근 제어를 묶어 제공합니다(예: "마케터 - 패션 브랜드" 역할은 마케터 역할에 따른 특정 권한을 부여받으며 "패션 브랜드" 작업 공간으로 접근이 제한됨). 그런 다음 회사 사용자에게 역할을 할당하여 관련 권한과 작업 공간 접근 권한을 직접 부여하십시오. <br><br>이 수준의 접근 권한을 가진 사용자는 일반적으로 하나의 대시보드에 여러 브랜드나 지역별 작업 공간이 포함된, 보다 엄격하게 설정된 환경에서 매니저 역할을 수행합니다. | 특정 작업 공간 |
| [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | 오디언스(예: 고객 기반 위치, 언어 및 커스텀 속성)에 따라 회사 사용자의 리소스 접근을 제한하십시오. <br><br>이 수준의 접근 권한을 가진 사용자는 일반적으로 담당 브랜드 내에서 특정 영역을 책임집니다. 예를 들어 다국어 브랜드의 경우 해당 언어별 콘텐츠를 구축하는 업무를 수행합니다. | 특정 대시보드 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}