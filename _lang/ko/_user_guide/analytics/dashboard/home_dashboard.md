---
nav_title: 홈 대시보드
article_title: 홈 대시보드(이전 개요)
page_order: 1
page_type: reference
description: "이 참조 문서에서는 홈 대시보드에 대해 설명하고 이 페이지에서 사용할 수 있는 통계에 대한 정의를 제공합니다."
tool: 
  - Reports

---

# 홈 대시보드

> 대시보드의 **홈** 페이지에서는 앱 또는 웹사이트의 성과를 추적하고 이해할 수 있는 주요 지표를 제공하며, 사용자층을 한눈에 파악할 수 있는 높은 수준의 정보를 제공합니다.

**홈** 페이지에는 두 개의 주요 섹션이 있습니다:
- [중지한 위치에서 재개](#pick-up-where-you-left-off)
- [성능 개요](#peformance-overview)

![Home dashboard in Braze.]({% image_buster /assets/img_archive/home_dashboard.png %})

## 중지한 위치에서 재개

최근에 편집하거나 만든 파일에 바로 액세스하여 Braze 대시보드에서 중단한 부분을 다시 시작할 수 있습니다. 이 섹션은 Braze 대시보드의 **홈** 페이지 상단에 나타납니다.

최근에 편집하거나 생성한 캠페인, 캔버스 및 세그먼트를 다시 방문할 수 있습니다. 각 카드에는 콘텐츠 유형(캠페인, 캔버스, 세그먼트) 및 상태(활성, 초안, 보관됨, 중지됨)를 나타내는 태그가 함께 제공됩니다.

![A Canvas draft, an active segment, and a campaign draft in the "Pick up where you left off" section.]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

## 성능 개요

기본적으로 **성능 개요** 섹션에는 모든 앱과 사이트에 대한 최근 30일간의 데이터가 표시됩니다. 지표는 모두 선택한 날짜 범위를 기준으로 계산됩니다.

![Date range and app fields on the Home dashboard.]({% image_buster /assets/img_archive/home_dashboard_select_date.png %}){: style="max-width:60%;"}

백분율은 이전 날짜 범위와 비교한 현재 날짜 범위를 기준으로 계산되며, 범위 대신 이전 기간의 마지막 날을 사용하는 *월간 활성 사용자* 수(MAU)는 예외입니다. 

예를 들어 날짜 범위를 **지난 7일로** 설정하고 *일간 활성 사용자* 증가율이 1.8%로 표시되면 이번 주 일간 활성 사용자 수가 지난 주에 비해 1.8% 증가했음을 의미합니다.

![]({% image_buster /assets/img_archive/home_dashboard_metric_tile.png %}){: style="max-width:60%;"}

### 내역 표시

실적 개요 통계의 각 행에 대해 분석 **표시를** 선택하여 지정된 날짜 범위에 대한 각 통계의 일별 값을 확인합니다.

![Expand]({% image_buster /assets/img_archive/home_dashboard_breakdown.png %})

## 사용 가능한 통계

다음은 사용 가능한 통계의 정의, 통계 계산 방법, 통계가 중요한 이유에 대한 설명입니다.

### 사용자

*사용자*는 해당 워크스페이스에서 생성된 총 사용자 수입니다. 여기에는 특정 시점에 앱이나 웹사이트를 사용한 기록이 있는 모든 사용자와 특정 앱이나 웹사이트와 관련이 없을 수 있는 사용자도 포함됩니다. 이 숫자는 평생 사용자 중 *월간 활성 사용자* (MAU)로 표시되는 사용자의 비율로, 장기간에 걸친 사용자 유지율을 확인하는 데 유용합니다.

사용자 대비 MAU 비율이 낮다면 메시징 채널을 다양화하거나 휴면 사용자에게 도달하기 위한 노력을 강화해야 한다는 의미일 수 있습니다. See our quick win on [capturing lapsing users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) for more info. 일반적으로 사용자 이탈로 인해 시간이 지남에 따라 MAU 대 생애 비율은 필연적으로 감소하지만, Braze 도구를 사용하면 사용자의 참여를 더 오래 유지하여 이러한 영향을 최소화할 수 있습니다.

### 평생 세션

*평생 세션은* 통합 이후 Braze가 기록한 총 세션 수입니다. 간단히 말해, 세션은 사용자가 앱을 사용하거나 웹사이트를 방문할 때마다 발생합니다. 플랫폼별로 세션이 정의되는 방식에 대한 보다 정확한 정의는 해당 플랫폼의
[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), or [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web) session tracking developer articles.

### 월간 활성 사용자

*월간 활성 사용자*(MAU)는 지난 30일 동안 앱 또는 사이트에서 세션을 기록한 사용자 수입니다. MAU는 30일 단위로 매일 밤 계산됩니다. MAU는 사용 강도가 다양한 날 사이의 불일치를 완화하여 장기간에 걸친 앱 또는 사이트의 상태를 잘 파악할 수 있게 해줍니다.

MAU 수 옆의 백분율은 이전 기간과 비교한 이 기간의 MAU 변화를 나타냅니다.

$$\text{Change in MAU} = \frac{\text{MAU of last date in range} - \text{MAU of day before start date}}{\text{MAU of day before start date}}$$

{% alert note %}
익명 사용자도 MAU에 포함됩니다. 모바일 디바이스의 경우 익명 사용자는 디바이스에 따라 다릅니다. 웹 사용자의 경우 익명 사용자는 브라우저 캐시에 의존합니다.
{% endalert %}

### 일일 활성 사용자

*일일 활성 사용자*(DAU)는 특정 날짜에 앱이나 사이트에서 최소 한 세션 이상을 기록한 순 사용자 수를 표시합니다. DAU는 앱 또는 사이트 사용의 일상적인 변동성을 조사하고 메시징 캠페인을 최대한 효과적으로 조정하는 데 유용한 통계가 될 수 있습니다. 예를 들어, 주말에 앱 사용량이 눈에 띄게 급증하는 경우 평일보다 주말에 인앱 메시지로 더 많은 사용자에게 도달할 수 있다는 것을 알 수 있습니다.

### 신규 사용자

*신규 사용자*는 이전에 세션을 기록한 적이 없는 사용자 중 앱이나 사이트를 사용하기 시작한 사용자 수를 알려줍니다. 이 숫자는 해당 기간 동안 신규 사용자의 총합입니다. 이 통계는 광고 활동의 효과를 추적하는 데 매우 유용할 수 있습니다.

{% alert note %}
처음에 Braze를 통합할 때 모든 사용자는 이전에 세션을 기록한 적이 없기 때문에 신규 사용자처럼 보입니다.
{% endalert %}

### 사용자 고착도

*사용자 고착도* 값은 특정 기간의 DAU와 MAU의 비율입니다. 기본적으로 고착성은 매일 재방문하는 MAU의 비율을 측정합니다.

예를 들어 날짜 범위를 30일로 설정한 경우 50%의 비율은 평균적으로 활성 사용자가 30일 중 15일 동안 앱 또는 웹사이트를 사용하거나 활성 사용자의 절반 정도가 매일 재방문한다는 의미입니다. 대부분의 사용자가 앱을 싫어해서 사용을 중단하는 것이 아니라 일상 생활의 일부가 되지 않았기 때문에 고착화는 성공의 중요한 척도입니다. 따라서 사용자 고착도를 사용자 참여도를 측정하기 위한 프록시로 사용할 수 있습니다.

사용자 고착도 비율 옆의 백분율은 이전 기간과 비교한 이 기간의 사용자 고착도 변화를 나타냅니다.

$$\text{Change in stickiness} = \frac{\text{Stickiness of last period} - \text{Stickiness of this period}}{\text{Stickiness of last period}}$$

'지난 기간'과 '이번 기간'의 기간은 선택한 날짜 범위에 따라 결정됩니다.

{% alert important %}
MAU 값은 매일 밤 계산되며 다음날까지 업데이트되지 않습니다.
{% endalert %}

### 일일 세션

*일일 세션*은 특정 날짜에 기록된 세션 수입니다. 이 값을 DAU 수와 비교하면 사용자가 세션을 한 번 이상 기록한 날에 앱을 열거나 웹사이트를 방문한 횟수를 알 수 있습니다.

### MAU당 일일 세션 수

*MAU당 일일 세션* 수는 특정 날짜의 MAU 대비 *일일 세션* 수의 비율입니다. 이 통계는 MAU당 하루에 얼마나 많은 세션이 기록될 것으로 예상되는지 알려줍니다. 이를 집계하여 평균을 내면 사용자가 앱이나 사이트를 언제 사용하는지 상대적인 빈도를 파악할 수 있습니다. 즉, *MAU당 일일 세션* 수가 평균 0.5라면 각 MAU가 2일에 한 번씩 세션을 기록할 것으로 예상할 수 있습니다.  

