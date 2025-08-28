---
nav_title: Braze 개요
article_title: "시작하기: Braze 개요"
page_order: 1
page_type: reference
description: "Braze에서 작업할 때 알아야 할 핵심 개념에 대해 알아보세요."

---

# 시작하기: Braze 개요

Braze에 오신 것을 환영합니다! 이 글 모음은 플랫폼을 시작하는 데 도움이 되며 Braze의 주요 용어, 특징 및 기능을 소개합니다. 이 페이지에서는 Braze에서 작업할 때 알아야 할 핵심 개념을 소개합니다.

{% alert tip %}
이 글과 함께 [모두를 위한 Braze 파운데이션](https://learning.braze.com/page/braze-foundations-for-everyone) 무료 강좌를 확인해 보시기를 적극 추천합니다. 이 강좌에는 특별한 로그인이나 계정이 필요하지 않습니다. If you're a developer looking for a technical rundown of Braze, check out [Getting Started for Developers]({{site.baseurl}}/developer_guide/getting_started/platform_overview/), too.
{% endalert %}

시작하기 섹션에서는 Braze의 일반적인 구현에 중점을 두고 설명합니다. 하지만 Braze는 매우 유연하며 다양한 방식으로 조직에 가치를 제공하도록 맞춤 설정할 수 있습니다. 명확성과 간결성을 위해 딱딱한 지침을 제공하는 대신 기본 설정에 대한 설명적인 개요를 제공했습니다. 저희는 모든 조직이 각기 다른 요구사항을 가지고 있다는 것을 알고 있으며, Braze는 특정 요구사항에 맞는 다양한 사용자 지정 옵션을 제공할 수 있도록 제작되었습니다.

Braze의 강력한 기능을 함께 살펴보세요.

## Braze 작동 방식

Braze는 모든 규모의 브랜드가 다양한 채널에서 개인화된 타겟팅 캠페인을 만들 수 있도록 지원하는 고객 참여 플랫폼입니다. Braze를 사용하면 고객의 말을 경청하고, 고객의 행동이 무엇을 의미하는지 파악한 다음, 적시에 적절한 채널을 통해 고객에게 적절한 메시지를 전송하여 조치를 취할 수 있습니다.

{% alert tip %}
동료 함께 플랫폼을 탐색할 수 있도록 [Braze에 동료를 추가하세요]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users).
{% endalert %}

## 사용자 및 세그먼트

사용자는 Braze를 사용하여 보내는 메시지를 받는 사람들, 즉 여러분의 고객입니다. 사용자에 대해 수집하여 Braze에 수집하는 모든 데이터는 인구 통계, 개인 정보, 선호도 및 행동과 같은 고객 프로필에 저장됩니다. 이 정보는 메시징을 강화하고 적절한 사용자에게 메시지를 맞춤화할 수 있는 기반이 됩니다.

![]({% image_buster /assets/img/getting_started/user_profile.png %})

세그먼트는 고객 기반을 더 작은 그룹으로 나눈 다음 특정 메시지로 타겟팅할 수 있습니다. 성별, 위치, 연령과 같은 특성부터 이전 캠페인과의 상호작용 패턴이나 고객 여정 중 어느 단계에 있는지와 같은 행동에 이르기까지 다양한 변수를 사용하여 세그먼트를 생성할 수 있습니다.

세그먼트는 동적이며, 사용자는 자신의 행동과 브랜드와의 관계에 따라 실시간으로 세그먼트에 들어오고 나갈 수 있습니다. 이를 통해 고객은 언제든지 자신에게 가장 관련성이 높은 메시지를 받을 수 있습니다. 타겟팅 및 메시징 목적에 따라 필요한 만큼 세그먼트를 만들 수 있습니다.

![]({% image_buster /assets/img/getting_started/segment.png %})

자세한 내용은 여기에서 확인하세요: [시작하기: 사용자 및 세그먼트]({{site.baseurl}}/user_guide/getting_started/users_segments/).

## 캠페인 및 캔버스

캠페인과 캔버스는 사용자에게 메시지를 보내는 방법입니다.

캠페인은 다양한 채널에서 특정 오디언스 세그먼트에 단일 메시지를 보내는 데 가장 적합합니다. 캠페인에서 지원되는 모든 메시징 채널(이메일, 푸시, 인앱 메시지, SMS 등)을 활용할 수 있습니다.

캔버스는 여러 채널에서 개인화된 고객 여정을 자동화하고 조율할 수 있는 고급 캠페인 워크플로우입니다. 캔버스 내에서 분기 로직, 지연, 결정 지점 및 전환 이벤트를 설정하여 일련의 상호 작용을 통해 고객을 안내할 수 있습니다. 캔버스는 다양한 터치포인트에서 일관되고 원활한 커뮤니케이션을 보장하여 고객 참여와 전환 가능성을 높입니다. 

자세한 내용은 여기에서 확인하세요: [시작하기: 캠페인 및 캔버스]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

## 워크스페이스

워크스페이스는 사용자, 세그먼트, 캠페인, 캔버스 등의 데이터를 한 곳에 그룹화합니다. 정보는 워크스페이스 간에 공유되지 않으므로 웹사이트와 앱을 워크스페이스에 추가할 때 이 점을 염두에 두세요. 모범 사례로 동일한 앱의 서로 다른 버전 또는 매우 유사한 앱을 하나의 워크스페이스에 모으는 방식만 제안합니다.

워크스페이스의 사용 예는 다음과 같습니다:

- 다양한 제품 라인 또는 앱
- 다양한 대상(예: 배달 기사 대 고객)
- 비즈니스 분리
- 테스트 환경

자세한 내용은 여기에서 확인하세요: [시작하기: 워크스페이스]({{site.baseurl}}/user_guide/getting_started/workspaces/).

## Braze 통합

Braze는 빠르고 쉽게 시작하고 실행할 수 있도록 설계되었습니다. 수백 개의 브랜드로 구성된 고객 기반에서 평균 가치 실현 시간은 6주입니다.

![]({% image_buster /assets/img/getting_started/timetovalue.png %})

다음은 병렬로 작업할 수 있는 네 가지 구성 요소를 기반으로 통합에 걸리는 시간을 예측하는 Braze 프레임워크입니다. 일반적인 범위는 30일에서 180일이며, 대부분의 계정은 45일에서 60일 이내에 통합을 완료합니다.

- **캠페인 마이그레이션 복잡도 수준:** 캠페인을 마이그레이션하는 데 걸리는 시간은 캠페인의 수, 개인화 정도, 리소스에 따라 달라집니다. 마이그레이션할 캠페인이 10개 미만인 경우 60일 이내에 마이그레이션할 수 있습니다. 하지만 캠페인이 100개가 넘으면 더 복잡해집니다. 한 사람이 100개의 캠페인을 마이그레이션하는 경우와 10명이 100개의 캠페인을 마이그레이션하는 것은 다릅니다.

{% alert tip %}
마이그레이션에 도움이 필요하신가요? [인증된 Braze 파트너가](https://www.braze.com/partners/solutions-partners) 도와드립니다!
{% endalert %}

- **이메일 전송량:** 이메일을 보내려면 IP를 워밍업해야 합니다. [IP warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) is the process of building sender reputation with your newly assigned IP addresses. 하루에 2~3백만 개 미만의 이메일을 보내는 경우 IP 워밍업은 30일 이내에 완료해야 합니다. 최대 전송량을 염두에 두세요. 평소에는 하루에 2백만 개의 이메일을 보내지만 계절에 따라 7백만 개의 이메일을 보낼 계획이라면 이 '피크' 전송에 대비해야 합니다. 대량 발송자는 여러 IP를 사용하여 워밍업 프로세스의 속도를 높일 수 있습니다.
- **조직의 복잡성:** 온보딩 프로세스는 비즈니스 요구에 맞게 조정할 수 있습니다. 단일 사업부, 전문 센터, 여러 독립 부서, 에이전시와 함께 팀을 보강하는 등 Braze는 모든 시나리오에서 작업한 경험을 보유하고 있습니다.
- **데이터 인프라의 정교함:** Braze SDK만 구현하거나 이미 고객 데이터 플랫폼(CDP)을 보유하고 있는 경우, 단 30일 만에 모든 설정을 완료할 수 있습니다. 최신 CDP를 사용하면 프로세스 속도를 높일 수 있습니다. 그러나 Braze와 연결할 백엔드 시스템, 도구 또는 데이터베이스가 많은 경우 설정을 완료하는 데 시간이 오래 걸리고 더 많은 전용 리소스가 필요할 수 있습니다.

자세한 내용은 여기에서 확인하세요: [시작하기: 통합 개요]({{site.baseurl}}/user_guide/getting_started/integration/).

