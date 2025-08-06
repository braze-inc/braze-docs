---
nav_title: 세그먼트 인사이트
article_title: 세그먼트 인사이트
page_order: 4
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "이 사용 방법 문서는 세그먼트 인사이트를 사용하는 방법, 해석하는 방법 및 공유하는 방법을 안내합니다."
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}세그먼트 인사이트

> 세그먼트 인사이트 사용, 해석 및 공유 방법을 배우세요. 

세그먼트 인사이트는 미리 선택된 일련의 핵심 성과 지표(KPI)에 대해 한 세그먼트의 성과가 다른 세그먼트와 어떻게 비교되는지 보여줍니다.

## 세그먼트 인사이트 보기

대시보드의 **세그먼트 인사이트** 페이지로 이동하여 **분석**에서 <i class="fas fa-plus"></i> **세그먼트 추가**를 클릭하여 기준선과 비교한 최대 네 개의 다른 세그먼트를 확인하세요.

![세그먼트 인사이트 대시보드.][1]

기준 세그먼트는 사용자가 선택한 특정 세그먼트이거나 모든 사용자를 포함하는 세그먼트일 수 있습니다. 세그먼트 인사이트를 사용하여 다음 통계를 비교할 수 있습니다:

| 측정 | 설명 | 산출식 |
| --------------------- | ------------- | ------------- |
| 세션 빈도 | 세그먼트 사용자 세션의 평균 일일 수 | (총 세션 수) / (첫 세션 이후 일수) |
| 최초 세션 이후 경과한 시간 | 세그먼트 사용자의 첫 번째 세션부터 지금까지 경과한 평균 시간 | 오늘 ~ 최초 세션 날짜 |
| 마지막 세션 이후 경과한 시간 | 세그먼트 사용자의 마지막 세션부터 지금까지 경과한 평균 시간 | 오늘 ~ 마지막 세션 날짜 |
| 생애주기 매출 | 세그먼트 사용자의 평균 생애주기 수익 | 사용자 생애주기 지출액 |
| 첫 구매까지 걸린 시간 | 세그먼트 사용자의 첫 번째 세션부터 첫 구매 시점까지 경과한 평균 시간 | 첫 구매 날짜 – 첫 세션 날짜 |
| 마지막 구매 이후 시간 | 세그먼트 사용자의 마지막 구매 시점부터 지금까지 경과한 평균 시간 | 오늘 – 마지막 구매 날짜 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

페이지의 고유 URL을 사용하여 특정 비교를 팀원과 쉽게 공유할 수 있으며, 각 세그먼트 아래를 클릭하여 해당 세그먼트에 대한 추가 정보를 확인할 수 있습니다. 이러한 비교는 작업 공간을 전환할 때 재설정됩니다.

![][2]

## 세그먼트 세부사항 페이지

세그먼트 인사이트 have also been built right into the **세그먼트 Details** view. 특정 세그먼트를 살펴볼 때, 이전에 설정한 세그먼트에서 동적이고 회색인 세그먼트 통계 상자 내에 설명된 동일한 여섯 가지 통계를 찾을 수 있습니다. 여기에서 세그먼트 인사이트 도구를 빠르게 실행하여 이 특정 세그먼트를 이전에 설정한 다른 세그먼트와 비교할 수 있지만, 이는 세그먼트 인사이트 도구 내에서 이전에 선택한 세그먼트를 덮어쓸 것입니다.

![][3]

## 사용 사례 {#insights-use-cases}

### 인구 통계 사용 및 구매 패턴 비교

세그먼트 인사이트의 가장 좋은 사용법 중 하나는 사용자 인구 통계가 앱 사용 및 캠페인 효과에 미치는 영향에 대한 질문에 답하는 것입니다. 예:

- 특정 사용자 인구 통계가 평균보다 훨씬 더 잘 수행되고 있습니까?
- 특정 캠페인의 현지화를 다시 생각해봐야 할까요?
- 특정 인구 통계를 대상으로 하는 캠페인이 참여하고 있습니까?
- 특정 인구 통계를 대상으로 하는 캠페인의 목표는 무엇으로 설정해야 할까요?

세그먼트 인사이트는 사용자 인구 통계 간의 차이를 발견하는 데 도움이 될 수 있습니다. 다음 예는 앱의 사용자 기반을 언어별로 비교하여 영어 사용자가 다른 언어 사용자보다 더 높은 LTV와 활동 수준을 보이는 것을 보여줍니다.

![][5]

이 예에서 독일어 사용자는 평균적으로 더 오래 전에 가입했으며, 이는 그들이 더 이상 활발하지 않은 이유를 설명할 수 있습니다. 이것은 여러 가지 요인 때문일 수 있습니다. 예를 들어, 앱이 처음 유럽에서 출시되었지만 현재 미국에서 더 인기가 있으며, 대부분의 사람들이 영어 또는 스페인어를 사용하는 경우입니다. 보다 강력한 결과를 얻기 위해, 인구 통계학적 지표 전반에 걸쳐 핵심 성과 지표(KPI)를 분석할 때, 일반적인 인구 통계학적 연구(예: 언어가 모든 사용자의 LTV에 영향을 미치는지 여부)를 통해 얻은 결과를 더 작고 유사한 인구 집단을 살펴보고 결과가 지속되는지 확인하는 것이 합리적입니다.

영어 이외의 언어를 사용하는 사람들 사이에서 전환율을 높이기 위해 좋은 첫 번째 단계는 [캠페인][10]을 사용자의 기기 언어로 현지화하고 이러한 메시지의 사본이 [다변량 캠페인][11]을 사용하여 외국어 사본의 다양한 버전을 테스트하여 사용자를 참여시키는지 확인하는 것입니다.

### 더 높은 매출의 지표 이해

사용자가 구매자로 전환하도록 하는 것은 어려울 수 있으며, 새로운 비활성 또는 참여하지 않는 사용자를 직접 구매로 유도하려고 하면 사용자가 앱을 제거할 수 있습니다. 세그먼트 인사이트는 사용자가 아직 구매하지 않고도 구매 퍼널을 더 진행할 수 있도록 도와줍니다. 예를 들어, 위시리스트에 항목 추가, 소셜 미디어에서 공유 또는 콘텐츠 즐겨찾기와 같은 행동을 발견할 수 있습니다. For example, you can chart out the impact on purchases different behaviors within an eCommerce app.

![][7]

이 경우, 현재 뉴스레터에 가입한 사용자는 상대적으로 적지만, 이 사용자들은 일반적으로 더 활발합니다. 새로운 사용자가 참여하도록 유지하려면 온보딩 캠페인에 뉴스레터 주문 초대를 포함하는 것이 좋습니다. 휴면 사용자와 다시 연결하려면 일반적인 [휴면 사용자 캠페인][9]을 보내고 후속 캠페인으로 [전환한 사용자][12]를 대상으로 뉴스레터에 가입하도록 하는 것이 좋습니다.

[1]: {% image_buster /assets/img_archive/segment_insights.png %}
[2]: {% image_buster /assets/img_archive/Segment_Insights_Info.png %}
[3]: {% image_buster /assets/img_archive/Segment_Segment_Insights.png %}
[5]: {% image_buster /assets/img_archive/Segment_Language_Insights.png %}
[7]: {% image_buster /assets/img_archive/Segment_Insights_Events1.png %}
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[10]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter
