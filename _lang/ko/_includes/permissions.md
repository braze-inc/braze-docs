{% if include.content == "Differences" %}

[Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), [권한 집합]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) 및 [사용자 역할을]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) 사용하여 Braze 내에서 대시보드 사용자 액세스 및 책임을 관리할 수 있습니다. 각 기능에는 서로 다른 권한 및 액세스 제어 컬렉션이 포함되어 있습니다.

### 주요 차이점

크게 보면 각 기능의 범위가 다릅니다:
- 권한 집합은 대시보드 사용자가 모든 워크스페이스에서 수행할 수 있는 작업을 제어합니다.
- 역할은 대시보드 사용자가 특정 작업 영역에서 수행할 수 있는 작업을 제어합니다.
- Teams는 대시보드 사용자가 메시지를 통해 도달할 수 있는 오디언스를 제어합니다.

| Feature | 할 수 있는 작업 | 액세스 범위 |
| - | - | - |
| [권한 세트]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | 특정 주제 영역 또는 작업과 관련된 권한('개발자' 및 '마케터' 등)을 묶은 다음, 여러 워크스페이스에서 동일한 권한이 필요한 대시보드 사용자에게 적용하세요. | 회사 전체 |
| [역할]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | 개별 고객 승인 및 워크스페이스 액세스 제어(예: 사용자가 마케터로서의 역할과 관련된 특정 권한을 가지고 있으며 '패션 브랜드' 워크스페이스로 제한되는 '마케터 - 패션 브랜드')를 번들로 묶습니다. 그런 다음 대시보드 사용자에게 역할을 할당하여 관련 권한 및 워크스페이스 액세스 권한을 직접 부여하세요. <br><br>이 수준의 액세스 권한을 가진 사용자는 일반적으로 하나의 대시보드에 여러 브랜드 또는 지역별 워크스페이스가 있는 보다 엄격하게 관리되는 설정의 매니저입니다. | 특정 작업 공간 |
| [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | 오디언스(예: 사용자 기반 위치, 언어, 커스텀 속성)에 따라 대시보드 사용자의 리소스 액세스를 제한하세요. <br><br>이 수준의 액세스 권한을 가진 사용자는 일반적으로 다국어 브랜드를 위한 언어별 콘텐츠를 구축하는 등 브랜드 내에서 특정 범위를 담당하게 됩니다. | 특정 대시보드 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}