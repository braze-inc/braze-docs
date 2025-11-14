---
nav_title: 채널 성능/성과 대시보드
article_title: 채널 성능/성과 대시보드
page_order: 2
page_type: reference
description: "이 참고 문서에서는 캠페인과 캔버스 모두에서 전체 채널의 성능/성과 측정기준을 확인할 수 있는 채널 성과 대시보드에 대해 설명합니다."
tool: 
  - Reports

---

# 채널 성능/성과 대시보드

> 채널 성과 대시보드에는 캠페인과 캔버스 모두에서 전체 채널에 대한 종합적인 성과 측정기준이 표시됩니다. 이 대시보드는 현재 이메일과 SMS로 제공됩니다.

지난 30일 동안의 이메일 채널 참여도를 표시하는 이메일 성능/성과 대시보드.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

다음 대시보드를 볼 수 있습니다:
- [이메일 성능/성과 대시보드](#email-performance-dashboard)
- [이메일 인사이트 대시보드](#email-insights-dashboard)
- [SMS 성능/성과 대시보드](#sms-performance-dashboard)

## 이메일 성능/성과 대시보드

**분석** > **이메일 성능으로** 이동하여 데이터를 보려는 기간의 날짜 범위를 선택하면 이메일 성능 대시보드를 볼 수 있습니다. 날짜 범위는 과거 최대 1년까지 가능합니다.

### 측정기준 계산 방법

335,630건, 하루 평균 11,187.667건을 전송한 이메일 캠페인의 예입니다.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

이메일 성능 대시보드의 다양한 측정기준에 대한 계산은 개별 메시지 수준(예: 캠페인 분석)에서의 계산과 동일합니다. 이 대시보드에서는 선택한 날짜 범위의 모든 캠페인과 캔버스에서 측정기준이 집계됩니다. 이러한 정의에 대해 자세히 알아보려면 [이메일 측정기준을]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics) 참조하세요.

각 타일에는 요금 측정기준이 먼저 표시되고 그 다음에 횟수 측정기준이 표시됩니다(단, 일별 평균에 이어 횟수 측정기준이 표시되는 *발송은* 제외). 예를 들어 고유 클릭 수 타일에는 선택한 기간의 *고유 클릭률과* 해당 기간의 총 고유 클릭 수 개수가 포함됩니다. 각 타일에는 [지난 기간과의 비교도](#comparing-time-periods) 표시됩니다.

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 전송 | Count | 날짜 범위 내 매일의 총 전송 횟수 |
| 전달률 | 평가 | (날짜 범위의 각 일별 총 전달 횟수) / (날짜 범위의 각 일별 총 발송 횟수) |
| 반송률 | 평가 | (날짜 범위의 각 일별 총 반송 횟수) / (날짜 범위의 각 일별 총 발신 횟수) |
| 탈퇴율 | 평가 | (날짜 범위의 각 일별 총 고유 탈퇴 건수) / (날짜 범위의 총 전달 건수)<br><br>여기에는 캠페인 분석, 개요 및 보고서 빌더에서도 사용되는 고유한 탈퇴를 사용합니다. 이러한 탈퇴는 모든 소스(예: 소프트웨어 개발 키트, REST API, CSV 가져오기, 이메일 및 목록 탈퇴)에 걸쳐 기록됩니다. 캠페인 및 캔버스 분석의 탈퇴율은 Braze에서 전송한 이메일의 수신 거부 클릭으로 인해 발생하는 탈퇴율입니다.  |
| 고유 열람율 | 평가 | (날짜 범위의 각 일별 고유 열람 총 건수) / (날짜 범위의 총 전달 건수) |
| 기타 열람율 | 평가 | (날짜 범위의 각 일별 총 기타 오픈 수) / (날짜 범위의 총 배송 수)<br><br>기타 열람에는 사용자가 이메일을 열 때와 같이 컴퓨터 열람으로 식별되지 않은 이메일이 포함됩니다. 이 측정기준은 고유하지 않으며 총 열람 횟수의 하위 지표입니다.  |
| 고유 클릭률 | 평가 | (날짜 범위의 각 일별 총 고유 클릭 수) / (날짜 범위의 총 전달 수) |
| 고유 클릭 열람율 | 평가 | (날짜 범위의 각 일별 총 고유 클릭 수) / (날짜 범위의 각 일별 총 고유 열람 수) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 이메일 인사이트 대시보드 

이메일 인사이트 대시보드는 고객이 언제 어디서 이메일과 상호 작용하는지 추적합니다. 이러한 보고서는 이메일을 최적화하여 더 많은 참여를 유도하는 방법에 대한 풍부하고 세분화된 데이터를 제공할 수 있습니다. 이메일 인사이트 대시보드에는 최대 최근 6개월의 데이터가 포함됩니다. 대시보드에 액세스하려면 **분석** > **이메일 성능/성과** > 이메일 인사이트로 이동하세요.

### 기기별 참여도

**기기별 참여** 보고서에서는 사용자가 이메일에 참여하는 데 사용하는 기기에 대한 분석을 제공합니다. 이 데이터는 모바일, 데스크톱, 태블릿 및 기타 기기 유형에서 이메일 참여를 추적합니다. 이 데이터는 사용자 기기로부터 전달된 사용자 에이전트 문자열을 기반으로 합니다.

{% alert note %}
CloudFront를 CDN으로 사용하는 경우 사용자의 사용자 에이전트가 이메일 서비스 공급업체에 전달되는지 확인하세요. 그렇지 않으면 모든 사용자 에이전트가 "Amazon 클라우드프론트"가 됩니다.
{% endalert %}

'기타' 카테고리에는 데스크톱, 모바일 또는 태블릿으로 식별할 수 없는 모든 사용자 문자열이 포함됩니다. 예를 들어 텔레비전, 자동차, 비디오 게임 콘솔, OTT(오버더톱 또는 스트리밍) 등이 이에 해당합니다. 여기에는 널 또는 빈 값도 포함될 수 있습니다.

이 '기타' 카테고리의 내용을 더 잘 이해하려면 다음 옵션 중 하나를 사용하여 사용자 상담원을 추출할 수 있습니다:

1. [커런츠는]({{site.baseurl}}/user_guide/data/braze_currents) 사용자의 기기에서 검색된 정확한 사용자 에이전트 문자열을 전송합니다.
2. [쿼리 빌더를]({{site.baseurl}}/user_guide/analytics/query_builder) 활용하여 SQL을 사용하거나 [AI 쿼리 빌더를]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) 사용하여 사용자 에이전트를 볼 수 있습니다.

모바일, 데스크톱, 태블릿 및 기타 기기에 대한 클릭 수를 보여주는 기기별 참여 보고서입니다. 모바일 기기에서 가장 많은 클릭 수가 발생합니다.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

이메일 열기 시 Braze는 Google 이미지 프록시, Apple 이미지 프록시, Yahoo 메일 프록시를 구분합니다. 이러한 서비스는 이메일이 수신자에게 전달되기 전에 이메일에 포함된 모든 이미지를 캐싱하고 로드합니다. 결과적으로 수신자의 서버가 아닌 사서함 제공업체의 서버에서 이메일이 트리거되어 이메일 열람 횟수가 부풀려질 수 있습니다. 이러한 서비스는 이미지를 로드할 때 개인정보 보호, 보안, 성능/성과 및 효율성을 향상시키기 위한 것입니다. 이러한 프록시 서비스는 사용자 에이전트를 마스킹하고 사용자 에이전트를 사용하여 프록시 데이터를 분류하기 때문에 수신자의 실제 열람도 포함될 수 있습니다.

모바일, 데스크톱, 태블릿, Apple 개인정보 보호 프록시, Google 이미지 프록시, Yahoo 메일 프록시 및 기타에 대한 클릭 수를 보여주는 기기별 참여 보고서입니다. 모바일 기기에서 가장 많은 열기 횟수가 발생합니다.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

### 사서함 제공 업체별 참여

**사서함 공급자별 참여** 보고서에는 클릭 또는 열람에 기여한 상위 사서함 공급자가 표시됩니다. 특정 프리미어 사서함 공급업체를 클릭하여 특정 수신 도메인으로 드릴다운할 수 있습니다. 예를 들어 이 보고서에서 Microsoft가 상위 사서함 공급자 측정기준 중 하나로 나열되어 있는 경우 "outlook.com", "hotmail.com", "live.com" 등과 같은 수신 도메인에 대한 세부 정보를 추가로 볼 수 있습니다.

사서함 공급자별 참여 보고서 예시(구글, 애플 iCloud, 야후, 마이크로소프트, Mail.Ru 그룹 및 해당 클릭 수).]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

### 참여 시간

**참여 시간** 보고서에는 사용자가 언제 이메일에 참여했는지에 대한 데이터가 표시됩니다. 이를 통해 고객 참여도가 가장 높은 요일이나 시간대와 같은 질문에 대한 답을 찾을 수 있습니다. 이러한 인사이트를 통해 메시지를 보내기에 가장 좋은 요일이나 시간을 실험하여 참여도를 높일 수 있습니다. 이 시간은 회사의 표준 시간대를 기준으로 합니다.

**요일별** 참여 보고서는 요일별로 열거나 클릭한 항목을 분석합니다. 

예시 월요일과 수요일에 가장 많은 클릭이 발생한 요일 참여 보고서입니다.]({% image_buster /assets/img_archive/time_engagement.png %})

**하루 중** 시간대별 참여 보고서 분석은 24시간을 기준으로 각 시간별로 열리거나 클릭합니다.

오전 12시부터 오후 11시까지 열거나 클릭한 시간대별 참여 보고서 예시.]({% image_buster /assets/img_archive/time_engagement_day.png %})

이메일 분석에 대한 자세한 내용은 [이메일 보고를]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) 참조하세요.

## SMS 성능/성과 대시보드

SMS 성능 대시보드를 사용하려면 **분석** > **SMS 성능으로** 이동하여 데이터를 보려는 기간의 날짜 범위를 선택합니다. 날짜 범위는 과거 최대 1년까지 가능합니다.

### 측정기준 계산 방법

335,630건, 하루 평균 11,187.667건을 전송한 SMS 캠페인의 예시입니다.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

SMS 성능 대시보드의 다양한 측정기준에 대한 계산은 개별 메시지 수준(예: 캠페인 분석)에서의 계산과 동일합니다. 이 대시보드에서는 선택한 날짜 범위의 모든 캠페인과 캔버스에서 측정기준이 집계됩니다. 이러한 정의에 대해 자세히 알아보려면 [SMS 측정기준을]({{site.baseurl}}/sms_mms_rcs_reporting/) 참조하세요.

각 타일에는 요금 측정기준이 먼저 표시되고 그 다음에 횟수 측정기준이 표시됩니다(단, 일별 평균에 이어 횟수 측정기준이 표시되는 _발송은_ 제외). 각 타일에는 [지난 기간과의 비교도](#comparison-to-last-period-change-in-totals-or-rates) 표시됩니다.

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 전송 | Count | 날짜 범위 내 매일의 총 전송 횟수 |
| 확인된 전달률 | 평가 | (날짜 범위의 각 일별 총 전달 횟수) / (날짜 범위의 각 일별 총 발송 횟수) |
| 전달 실패율 | 평가 | (날짜 범위의 각 일별 총 실패 횟수) / (날짜 범위의 각 일별 총 전송 횟수) |
| 거부율 | 평가 | (날짜 범위의 각 일별 총 거부 횟수) / (날짜 범위의 각 일별 총 전송 횟수) |
| 클릭률 | 평가 | (날짜 범위의 각 일별 총 클릭 수) / (날짜 범위의 각 일별 총 전달 수) |
| 총 옵트인 수 | 평가 | 날짜 범위의 각 일별 인바운드 메시지 옵트인 총 수 |
| 총 옵트아웃 수 | 평가 | 날짜 범위의 각 일별 인바운드 메시지 옵트아웃 총 건수 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 대시보드 필터

다음 필터 옵션을 사용하여 대시보드의 데이터를 필터링할 수 있습니다:

- **태그:** 태그를 하나 선택합니다. 적용하면 대시보드에 선택한 태그에 대한 측정기준만 표시됩니다.
- **캔버스:** 최대 10개의 캔버스를 선택하세요. 적용하면 대시보드에 선택한 캔버스에 대한 측정기준만 표시됩니다. 태그 필터를 먼저 선택하면 캔버스 필터 옵션에 선택한 태그가 있는 캔버스만 포함됩니다.
- **캠페인:** 최대 10개의 캠페인을 선택하세요. 적용하면 대시보드에 선택한 캠페인에 대한 측정기준만 표시됩니다. 태그 필터를 먼저 선택하면 캠페인 필터 옵션에 선택한 태그가 있는 캠페인만 포함됩니다.

채널 성능 대시보드의 필터 옵션에서 태그와 필터링할 캔버스 목록을 선택할 수 있습니다.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## 기간 비교

채널 성능/성과 대시보드는 날짜 범위에서 선택한 기간과 이전 기간을 자동으로 비교하여 동일한 일수를 합산합니다. 예를 들어 대시보드에서 날짜 범위로 '지난 7일'을 선택하면 최근 기간과의 비교는 지난 7일의 측정기준과 7일 전의 측정기준을 비교합니다. 커스텀 날짜 범위(예: 5월 10일부터 5월 15일까지 6일간의 데이터)를 선택하면 대시보드에서 해당 날짜의 측정기준을 5월 4일부터 5월 9일까지의 측정기준과 비교합니다.

비교는 지난 기간과 현재 기간의 변화율을 백분율로 나타낸 것으로, 두 기간의 차이를 지난 기간의 측정기준으로 나누어 계산합니다.

### 총 개수 및 요금 변경 사항 보기

두 기간 간의 총 개수(예: 전달된 이메일 수)를 비교하는 **합계 변경 사항 표시와**요금(예: 전달률)을 비교하는 요금 **변경 사항 표시**간에 전환할 수 있습니다.

라디오 버튼을 사용하여 채널 성능/성과 대시보드의 총액 변경 표시 또는 요금 변경 표시 간에 전환할 수 있습니다.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## 자주 묻는 질문

### 대시보드에 빈 값이 표시되는 이유는 무엇인가요?

측정기준에 빈 값이 발생할 수 있는 몇 가지 시나리오가 있습니다:

- 선택한 날짜 범위에서 특정 측정기준에 대해 Braze가 0을 기록했습니다.
- 선택한 날짜 범위 동안 메시지를 보낸 적이 없습니다.
- 선택한 날짜 범위에 대한 열기, 클릭 또는 탈퇴와 같은 측정기준은 있었지만 전달이나 전송은 없었습니다. 이 경우 Braze는 요금 측정기준을 계산하지 않습니다.

더 많은 측정기준을 보려면 날짜 범위를 확장해 보세요.

### 이메일 대시보드에 고유 열람 건수보다 기타 열람 건수가 더 많이 표시되는 이유는 무엇인가요?

_고유 열람_ 횟수 측정기준의 경우, 특정 사용자가 등록한 모든 반복 열람( _머신 열람_ 또는 _기타 열람_ 포함 여부)을 중복 제거하여 사용자가 여러 번 열람하는 경우 단 하나의 _고유 열람_ 횟수만 증가하도록 합니다. _기타 오픈의_ 경우, Braze는 중복 제거를 하지 않습니다.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

