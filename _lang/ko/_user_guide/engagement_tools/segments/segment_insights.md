---
nav_title: 세그먼트 인사이트
article_title: 세그먼트 인사이트
page_order: 8
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "이 사용법 문서에서는 세그먼트 인사이트를 사용하고, 해석하고, 공유하는 방법을 안내합니다."
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"} 세그먼트 인사이트

> 세그먼트 인사이트를 사용하고, 해석하고, 공유하는 방법에 대해 알아보세요. 

세그먼트 인사이트는 미리 선택된 일련의 KPI에 대해 한 세그먼트가 다른 세그먼트와 비교하여 어떤 성능/성과를 거두고 있는지 보여줍니다.

## 세그먼트 인사이트 보기

대시보드의 **분석** 아래 **세그먼트 인사이트** 페이지로 이동하여 기준선과 비교하여 최대 10개의 서로 다른 세그먼트를 볼 수 있습니다.

기준 세그먼트인 '전체 사용자'와 '영국 사용자', '프랑스 사용자', '캘리포니아 사용자'의 세 세그먼트를 비교한 세그먼트 인사이트 대시보드.]({% image_buster /assets/img_archive/segment_insights.png %})

기준 세그먼트는 선택한 특정 세그먼트이거나 모든 사용자를 포함하는 세그먼트일 수 있습니다. 세그먼트 인사이트를 사용하여 다음 통계를 비교할 수 있습니다:

| 측정 | 설명 | 공식 |
| --------------------- | ------------- | ------------- |
| 일일 세션 수 | 세그먼트 사용자당 하루 평균 세션 수 | (총 세션 수) / (첫 세션 이후 일수) |
| 첫 세션 이후 일수 | 세그먼트 사용자의 첫 세션과 현재까지의 평균 일 수 | 오늘 - 첫 세션 날짜 |
| 마지막 세션 이후 일수 | 세그먼트 사용자의 마지막 세션과 현재 세션 사이의 평균 일수 | 오늘 - 마지막 세션 날짜 |
| 평생 매출(달러) | 세그먼트 사용자의 평균 평생 매출(달러) | 사용자 평생 지출 |
| 첫 구매 이후 일수 | 세그먼트 사용자의 첫 세션과 첫 구매 사이의 평균 일수 | 첫 구매 날짜 - 첫 세션 날짜 |
| 마지막 구매 이후 일수 | 세그먼트 사용자의 마지막 구매와 현재 구매 사이의 평균 일수 | 오늘 - 마지막 구매 날짜 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

페이지의 고유 URL을 사용하여 팀원들과 특정 비교를 쉽게 공유할 수 있으며, 각 세그먼트 옆에 있는 눈 아이콘을 선택하면 해당 세그먼트에 대한 자세한 정보를 볼 수도 있습니다. 이러한 비교는 작업 공간 간에 전환하면 초기화됩니다.

'프리미엄 사용자(iOS 비디오앱)' 세그먼트에 대한 세부 정보에 과거 회원 수를 표시하는 그래프와 다양한 메시징 채널에 대한 예상 규모를 세분화한 차트가 포함되어 있습니다.]({% image_buster /assets/img_archive/Segment_Insights_Info.png %}){: style="max-width:50%;"}

## 세그먼트 세부 정보 페이지

세그먼트 인사이트도 **세그먼트 세부 정보** 보기에 바로 구축되었습니다. 이전에 설정한 특정 세그먼트를 살펴보면 동적인 회색 세그먼트 통계 상자 안에 동일한 6가지 통계가 표시되어 있습니다. 여기에서 세그먼트 인사이트 툴을 빠르게 실행하여 이 특정 세그먼트를 이전에 설정한 다른 세그먼트와 비교할 수 있지만, 세그먼트 인사이트 툴 내에서 이전에 선택한 모든 세그먼트를 덮어쓰게 됩니다.

\![]({% image_buster /assets/img_archive/Segment_Segment_Insights.png %})

## 사용 사례 {#insights-use-cases}

### 인구통계학적 사용 및 구매 패턴 비교

세그먼트 인사이트의 가장 좋은 활용 사례 중 하나는 사용자 인구통계가 앱 사용 및 캠페인 효과에 미치는 영향에 대한 질문에 답하는 것입니다:

- 특정 사용자 인구 통계의 성능/성과가 평균보다 현저히 좋거나 나쁜가요?
- 특정 캠페인의 현지화를 다시 고려해야 하나요?
- 특정 인구 통계가 캠페인에 참여하고 있나요?
- 특정 인구 집단을 대상으로 하는 캠페인에 어떤 목표를 설정해야 하나요?

세그먼트 인사이트는 사용자 인구 통계 간의 차이를 발견하는 데 도움이 될 수 있습니다. 다음 예는 앱의 사용자 기반을 언어별로 비교한 것으로, 영어 사용자가 다른 언어 사용자보다 LTV 및 활동 수준이 더 높은 경향이 있음을 보여줍니다.

영어, 독일어, 프랑스어, 스페인어 세그먼트에 대한 세그먼트 인사이트 분석.]({% image_buster /assets/img_archive/Segment_Language_Insights.png %})

이 예에서는 독일어 사용자가 평균적으로 더 오래 전에 가입했기 때문에 더 이상 활동하지 않는 것으로 보입니다. 이는 여러 가지 요인으로 인해 발생할 수 있습니다. 예를 들어 유럽에서 처음 출시된 앱이지만 대부분의 사람들이 영어나 스페인어를 사용하는 미국에서 더 인기가 있는 경우입니다. 보다 확실한 결과를 얻으려면 인구 통계 전반에 걸쳐 KPI를 분석할 때, 인구 통계에 대한 일반적인 연구 결과(예: 언어가 모든 사용자의 LTV에 영향을 미치는지)를 더 작고 유사한 모집단을 대상으로 테스트하여 그 결과가 지속되는지 확인하는 것이 좋습니다.

영어 이외의 언어를 사용하는 사용자의 전환율을 높이려면 먼저 [캠페인을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) 사용자의 기기 언어로 [현지화하고]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages), [다변량 캠페인을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests) 통해 다양한 버전의 외국어 카피를 테스트하여 해당 메시지의 카피가 사용자의 참여를 유도하는지 확인하는 것이 좋습니다.

### 매출 증가 지표 이해하기

사용자를 구매자로 전환시키는 것은 어려울 수 있으며, 비활성 상태이거나 참여도가 낮은 신규 사용자를 구매로 직접 푸시하려고 하면 사용자가 앱을 삭제할 수 있습니다. 세그먼트 인사이트는 뉴스레터 구독, 소셜 미디어 공유, 프로모션 메시지 가입 등 사용자가 아직 구매를 하지 않아도 구매 퍼널의 더 아래로 유도하는 행동을 발견하는 데 도움이 될 수 있습니다. 예를 들어, 이커머스 앱 내에서 다양한 행동이 구매에 미치는 영향을 도표로 만들 수 있습니다.

소셜 미디어에 공유한 사용자, 프로모션에 가입한 사용자, 뉴스레터에 가입한 사용자에 대한 세그먼트 인사이트 분석입니다.]({% image_buster /assets/img_archive/Segment_Insights_Events1.png %})

이 경우 현재 프로모션 메시징에 가입한 사용자는 상대적으로 적고 활동적인 사용자는 많지 않지만, 이러한 사용자의 평생 매출이 더 높습니다. 매출을 늘리려면 온보딩 캠페인에 프로모션 메시징 가입 초대를 포함시키는 것이 좋습니다. 휴면 사용자의 재참여를 유도하려면 일반적인 [휴면 사용자 캠페인을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users) 발송하고 후속 캠페인을 통해 [전환한 사용자를]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter) 타겟팅하여 프로모션 메시지에 가입하도록 하는 것이 좋은 계획이 될 수 있습니다.

