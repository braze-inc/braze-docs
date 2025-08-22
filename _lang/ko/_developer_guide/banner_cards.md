---
page_order: 2.2
nav_title: 배너 카드
article_title: 배너 카드
description: "이 랜딩 페이지에서는 배너 카드를 만드는 방법과 사용 사례 등 배너 카드에 대한 모든 것을 확인할 수 있습니다."
channel:
- Banners
---

# 배너 카드

> 배너 카드를 사용하면 이메일이나 푸시 알림과 같은 다른 채널의 도달 범위를 확장하면서 사용자를 위한 맞춤형 메시지를 만들 수 있습니다. [콘텐츠 카드와]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about) 마찬가지로 앱이나 웹사이트에 직접 카드를 삽입하여 자연스럽게 느껴지는 경험을 통해 사용자와 소통할 수 있습니다.

{% alert important %}
배너 카드는 현재 얼리 액세스 중입니다. 이번 얼리 액세스에 참여하려면 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 사용 사례

배너 카드는 만료되지 않고 사용자가 새 세션을 시작할 때마다 자동으로 개인화되므로 다음과 같은 용도로 유용합니다:

- 추천 콘텐츠 강조 표시
- 예정된 이벤트에 대해 사용자에게 알림
- 로열티 프로그램에 대한 업데이트 공유

## 배너 카드 정보

### 카드 만료

기본적으로 배너 카드는 만료되지 않지만 필요한 경우 종료 날짜를 선택할 수 있습니다.

### 배치 ID {#placement-ids}

배너 카드 배치는 각 워크스페이스마다 고유하며 단일 워크스페이스 내에서 10개의 캠페인에 걸쳐 사용할 수 있습니다. 또한 각 워크스페이스 내의 배치에는 고유 ID가 할당되어야 합니다. [배너 카드 캠페인을 만들]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/) 거나 [앱에 배너 카드를 삽입할]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/) 때 게재 위치를 생성하고 ID를 할당합니다.

{% alert important %}
배너 카드 캠페인을 시작한 후에는 게재 위치 ID를 수정하지 마세요.
{% endalert %}

### 카드 우선 순위 {#card-priority}

여러 캠페인이 동일한 게재 위치 ID를 참조하는 경우, 우선순위에 따라 카드가 표시됩니다. 기본적으로 새로 생성된 배너 카드는 중간으로 설정되지만 [우선순위를 수동으로]({{site.baseurl}}/developer_guide/banner_cards/creating_banner_cards/#set-card-priority) 높음, 중간 또는 낮음 설정할 수 있습니다. 여러 카드가 동일한 우선순위를 공유하는 경우 가장 최신 카드가 먼저 표시됩니다.

### 측정기준

가장 중요한 배너 카드 지표입니다. 메트릭, 정의 및 계산의 전체 목록은 [보고서 메트릭 용어집을]({{site.baseurl}}/user_guide/data/report_metrics/) 참조하세요.

| 측정기준 | 정의 |
| --- | --- |
| [총 노출 수]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-impressions) | 이전 상호 작용과 관계없이 메시지가 로드되어 사용자 화면에 표시된 횟수입니다(예: 사용자에게 메시지가 두 번 표시된 경우 두 번 계산됨). |
| [고유 노출 수]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-impressions) | 하루에 특정 메시지를 수신하고 열람한 총 사용자 수입니다. 각 사용자는 한 번만 계산됩니다. |
| [총 클릭 수]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-clicks) | 동일한 사용자가 여러 번 클릭했는지 여부와 관계없이 전달된 메시지 내에서 클릭한 사용자의 총 수(및 백분율)입니다. |
| [고유 클릭 수]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-clicks) | 메시지 내에서 한 번 이상 클릭한 고유한 수신자 수로, 다음으로 측정됩니다. [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/). 각 사용자는 한 번만 계산됩니다. |
| [주요 전환]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | Braze 캠페인에서 받은 메시지를 보고 상호작용한 후 정의된 이벤트가 발생한 횟수입니다. 이 정의된 이벤트는 캠페인을 구축할 때 사용자가 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 다음 단계

이제 배너 카드에 대해 알아봤으니 다음 단계로 넘어갈 준비가 되었습니다:

- [배너 카드 캠페인 만들기]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/)
- [앱에 배너 카드 임베드하기]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/)
