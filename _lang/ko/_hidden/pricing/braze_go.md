---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> Braze Go는 마케팅 팀이 어디서든 시작하고 어디로든 이동할 수 있도록 Braze 고객 참여 플랫폼에 대한 간소화된 액세스를 제공합니다. 단순성과 효율성을 위해 설계된 Braze Go는 일부 신흥 시장을 위해 맞춤 제작되었습니다.

{% alert important %}
일부 시장에서는 Braze Go를 사용할 수 없습니다. Braze Go에 대해 자세히 알아보려면 계정 관리자에게 문의하세요.
{% endalert %}

Braze Go는 Braze와 동일한 기능을 모두 제공하며, 다음 기능에 중점을 두고 변경되었습니다: 

- 최대 30개의 활성 캠페인을 만들 수 있습니다.
- 활성 캔버스는 최대 20개까지 만들 수 있습니다.
- 총 REST API 기본 사용량 제한은 워크스페이스당 시간당 50,000입니다.
    - Braze Go 이외의 용도로 사용하는 경우 [REST API 제한]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type)에 대해 자세히 알아보세요.
- 캠페인 및 캔버스 상호 작용 데이터 보존 기간은 2개월이며 복원할 수 없습니다.
    - Braze Go 이외의 용도로 사용하는 경우 [메시징 상호작용 데이터 가용성]({{site.baseurl}}/messaging_interaction_data/)에 대해 자세히 알아보세요.

{% alert note %}
캠페인 및 캔버스에 대한 상호작용 데이터는 Snowflake 데이터와 다르며 전혀 영향을 미치지 않습니다.
{% endalert %}

- Braze-to-Braze 웹훅은 지원되지 않습니다.
- 태그와 관련된 필터, 특히 다음 필터는 지원되지 않습니다:
    - 태그가 있는 캠페인 또는 캔버스를 클릭하거나 열었습니다.
    - 태그가 있는 캠페인 또는 캔버스에서 마지막으로 받은 메시지
    - 태그가 있는 캠페인 또는 캔버스 수신
- Braze는 또한 1년 동안 다시 수행되지 않은 이벤트, 구매 또는 둘 다 1년이 지난 고객 프로필 이벤트 및 구매 데이터에 대한 데이터 보존 정책을 시행할 수 있습니다. 그러나 이 데이터는 SQL 세그먼트 확장 프로그램에서 2년 동안 계속 사용할 수 있습니다.

위의 기능이 업데이트되면 이 글에 반영되고 [릴리스 노트]({{site.baseurl}}/help/release_notes/#most-recent-braze-release-notes)에 명시됩니다.