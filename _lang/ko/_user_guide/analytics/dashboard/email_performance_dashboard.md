---
nav_title: 채널 성능/성과 대시보드
article_title: 채널 성능/성과 대시보드
page_order: 2
page_type: reference
description: "이 참조 문서는 채널 성능 대시보드에 대해 다루며, 캠페인과 캔버스 전반에 걸쳐 전체 채널의 성능 측정기준을 볼 수 있습니다."
tool: 
  - Reports

---

# 채널 성능/성과 대시보드

> 채널 실적 대시보드에는 캠페인과 캔버스 모두에서 전체 채널에 대한 종합적인 실적 지표가 표시됩니다. 이 대시보드는 현재 이메일 및 SMS에 사용할 수 있습니다.

![이메일 성능/성과 대시보드가 지난 30일 동안의 이메일 채널 인게이지먼트를 표시합니다.][1]

다음 대시보드를 볼 수 있습니다:
- [이메일 성능/성과 대시보드](#email-performance-dashboard)
- [이메일 인사이트 대시보드](#email-insights-dashboard)
- [SMS 성능/성과 대시보드](#sms-performance-dashboard)

## 이메일 성능/성과 대시보드

**분석** > **이메일 성과로** 이동하여 데이터를 보려는 기간의 날짜 범위를 선택하면 이메일 성과 대시보드를 볼 수 있습니다. 날짜 범위는 최대 1년 전까지 가능합니다.

### 메트릭 계산 방법

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

이메일 성능 대시보드에서 다양한 측정기준에 대한 계산은 개별 메시지 수준(예: 캠페인 분석)과 동일합니다. 선택한 날짜 범위에 대해 모든 캠페인 및 캔버스의 측정기준이 집계된 대시보드입니다. 이 정의에 대해 자세히 알아보려면 [이메일 측정기준]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics)을 참조하십시오.

각 타일은 먼저 비율 메트릭을 표시하고, 그 다음에 개수 메트릭을 표시합니다 (*Sends*의 경우는 예외로, 개수 메트릭을 먼저 표시하고 하루 평균을 표시합니다). 예를 들어, 고유 클릭 타일에는 선택한 기간의 *고유 클릭률*과 해당 기간의 고유 클릭 총 수가 포함됩니다. 각 타일은 또한 [지난 기간과의 비교](#comparison-to-last-period-change-in-totals-or-rates)를 보여줍니다.

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 발송 수 | 카운트 | 날짜 범위 내 각 날짜별 전송 횟수 총계 |
| 전달율 | 비율 | (날짜 범위 내 각 날짜의 총 전달 횟수) / (날짜 범위 내 각 날짜의 총 발송 횟수) |
| 반송률 | 비율 | (날짜 범위 내 각 날짜의 총 반송 횟수) / (날짜 범위 내 각 날짜의 총 발송 횟수) |
| 구독취소율 | 비율 | (날짜 범위 내 각 날짜의 고유 구독 취소 수) / (날짜 범위의 총 전달 수)<br><br>이는 고유 구독 취소를 사용하며, 이는 캠페인 분석, 개요 및 보고서 빌더에서도 사용됩니다. 이러한 구독 취소는 모든 소스(예: SDK, REST API, CSV 가져오기, 이메일 및 목록 구독 취소)에 걸쳐 기록됩니다. 캠페인 및 캔버스 분석의 구독 취소율은 Braze에서 전송한 이메일의 구독 취소 클릭으로 인해 발생하는 구독 취소율입니다.  |
| 고유 열람률 | 비율 | (날짜 범위 내 각 날짜의 고유 열람 수 총합) / (날짜 범위의 총 전달 수) |
| 기타 열람율 | 비율 | (날짜 범위 내 각 날짜의 총 다른 열람 수) / (날짜 범위의 총 전달 수)<br><br>기타 열기에는 사용자가 이메일을 열 때와 같이 기계 열람으로 식별되지 않은 이메일이 포함됩니다. 이 메트릭은 고유하지 않으며 총 오픈 수의 하위 메트릭입니다.  |
| 고유 클릭률 | 비율 | (날짜 범위 내 각 날짜의 고유 클릭 수 총합) / (날짜 범위의 총 전달 수) |
| 고유 클릭 후 열람율 | 비율 | (날짜 범위 내 각 날짜의 고유 클릭 수 총합) / (날짜 범위 내 각 날짜의 고유 열람 수 총합) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 이메일 인사이트 대시보드 

이메일 인사이트 대시보드는 고객이 언제 어디서 이메일과 상호 작용하는지를 추적합니다. 이 보고서는 이메일 최적화를 통해 더 큰 인게이지먼트를 유도하는 방법에 대한 풍부하고 세분화된 데이터를 제공할 수 있습니다. 이메일 인사이트 대시보드에는 최대 최근 6개월의 데이터가 포함되어 있습니다. 대시보드에 액세스하려면 **분석** > **이메일 성능/성과** > **이메일 인사이트**로 이동하십시오.

### 기기별 참여

**기기별 참여** 보고서는 사용자가 이메일에 참여하는 데 사용하는 기기에 대한 분석을 제공합니다. 이 데이터는 모바일, 데스크톱, 태블릿 및 기타 기기 유형에서 이메일 인게이지먼트를 추적합니다. This data is based on the user agent string passed from your users' devices.

{% alert note %}
If you use CloudFront as your CDN, make sure your users' user agent is passed along to the ESP. Otherwise, every user agent will be "Amazon Cloudfront".
{% endalert %}

The “Other” category includes any user string that cannot be identified as desktop, mobile, or tablet. 예를 들어 텔레비전, 자동차, 비디오 게임 콘솔, OTT(오버더톱 또는 스트리밍) 등이 이에 해당합니다. 이것은 null 또는 빈 값도 포함될 수 있습니다.

To better understand what is in this "Other" category, you can extract the user agents using either of these options:

1. [Currents]({{site.baseurl}}/user_guide/data/braze_currents) will send you the exact user agent string that was retrieve from the your users' devices.
2. Leverage our [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) to use SQL or our [AI Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) to view the user agents.

![기기별 인게이지먼트 보고서에는 모바일, 데스크톱, 태블릿 및 기타 기기의 클릭 수가 표시됩니다. 클릭 수가 가장 많은 것은 모바일 기기에서 발생합니다.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

이메일 열기에서는 Braze가 Google 이미지 프록시, Apple 이미지 프록시 및 Yahoo 메일 프록시를 분리합니다. 이 서비스는 이메일의 모든 포함된 이미지를 캐시하고 로드한 후 수신자에게 전달됩니다. 결과적으로, 이는 받은편지함 제공자의 서버에서 이메일을 여는 트리거가 되어 수신자의 서버가 아닌, 이메일 열람 수가 부풀려질 수 있습니다. 이 서비스는 이미지를 로드할 때 프라이버시, 보안, 성능/성과 및 효율성을 향상시키기 위한 것입니다. 이것은 또한 수신자로부터 실제 열람을 포함할 수 있습니다. 이러한 프록시 서비스는 사용자 에이전트를 마스킹하고, 우리는 사용자 에이전트를 사용하여 프록시 데이터를 분류합니다.

![기기별 인게이지먼트 보고서에는 모바일, 데스크탑, 태블릿, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy 및 기타에 대한 클릭 수가 표시됩니다. 가장 많은 수의 열림은 모바일 기기에서 발생합니다.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

### 받은편지함 제공자의 인게이지먼트

**받은편지함 제공업체의 인게이지먼트** 보고서는 클릭 또는 열기에 기여하는 주요 받은편지함 제공업체를 표시합니다. 특정 주요 받은편지함 제공업체를 클릭하여 특정 수신 도메인으로 세부 분석할 수 있습니다. 예를 들어, Microsoft가 이 보고서에서 상위 받은편지함 제공업체 측정기준 중 하나로 나열된 경우, "outlook.com", "hotmail.com", "live.com" 등과 같은 수신 도메인에 대한 세부 정보를 추가로 확인할 수 있습니다.

![][5]{: style="max-width:70%;"}

### 참여 시간

**인게이지먼트 시간** 보고서는 사용자가 이메일에 인게이지먼트하는 시기에 대한 데이터를 표시합니다. 이것은 고객의 인게이지먼트가 가장 높은 요일이나 시간을 파악하는 데 도움이 될 수 있습니다. 이러한 통찰력을 통해 메시지를 보내는 최적의 날이나 시간을 실험하여 더 높은 참여를 유도할 수 있습니다. 이 시간은 회사의 표준 시간대를 기준으로 합니다.

**요일** 참여 보고서는 요일별로 열림 또는 클릭을 분석합니다. 

![][6]

**하루 중 시간** 참여 보고서는 24시간 창 내에서 시간별로 열림 또는 클릭을 분류합니다.

![][7]

이메일에 대한 분석에 대한 자세한 내용은 [이메일 보고서]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)를 확인하세요.

## SMS 성능/성과 대시보드

SMS 성능 대시보드를 사용하려면 **분석** > **SMS 성능**으로 이동하여 보고 싶은 기간의 날짜 범위를 선택하세요. 날짜 범위는 최대 1년 전까지 가능합니다.

### 메트릭 계산 방법

![][2]{: style="max-width:40%;float:right;margin-left:15px;border:none;"}

SMS 성능/성과 대시보드에서 다양한 측정기준에 대한 계산은 개별 메시지 수준(예: 캠페인 분석)과 동일합니다. 선택한 날짜 범위에 대해 모든 캠페인 및 캔버스의 측정기준이 집계된 대시보드입니다. 이 정의에 대해 더 알아보려면 [SMS 측정기준]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/)을 참조하십시오.

각 타일은 먼저 비율 메트릭을 표시하고, 그 다음에 개수 메트릭을 표시합니다 (_Sends_의 경우는 예외로, 개수 메트릭을 먼저 표시하고 하루 평균을 표시합니다). 각 타일은 또한 [지난 기간과의 비교](#comparison-to-last-period-change-in-totals-or-rates)를 보여줍니다.

| 측정기준 | 유형 | 계산 |
| --- | --- | ---- |
| 발송 수 | 카운트 | 날짜 범위 내 각 날짜별 전송 횟수 총계 |
| 확인된 전달률 | 비율 | (날짜 범위 내 각 날짜의 총 전달 횟수) / (날짜 범위 내 각 날짜의 총 발송 횟수) |
| 전달 실패율 | 비율 | (날짜 범위 내 각 날짜의 총 실패 횟수) / (날짜 범위 내 각 날짜의 총 전송 횟수) |
| 거부율 | 비율 | (날짜 범위 내 각 날짜의 총 거부 수) / (날짜 범위 내 각 날짜의 총 발송 수) |
| 클릭률 | 비율 | (날짜 범위 내 각 날짜의 총 클릭 수) / (날짜 범위 내 각 날짜의 총 배송 수) |
| 총 옵트인 | 비율 | 날짜 범위 내 각 날짜별 수신 메시지 옵트인 총 수 |
| 총 옵트아웃 | 비율 | 날짜 범위 내 각 날짜별 수신 메시지 수신 거부 총 수 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 대시보드 필터

다음 필터 옵션을 사용하여 대시보드의 데이터를 필터링할 수 있습니다:

- **태그:** 태그를 하나 선택하세요. 적용되면 대시보드는 선택한 태그에 대한 측정기준만 표시됩니다.
- **캔버스:** 최대 10개의 캔버스를 선택하세요. 적용되면, 대시보드는 선택한 캔버스에 대한 측정기준만 표시됩니다. 먼저 태그 필터를 선택하면 캔버스 필터 옵션에는 선택한 태그가 포함된 캔버스만 포함됩니다.
- **캠페인:** 최대 10개의 캠페인을 선택하세요. 적용되면, 대시보드는 선택한 캠페인에 대한 측정기준만 표시됩니다. 태그 필터를 먼저 선택하면 캠페인 필터 옵션에는 선택한 태그가 포함된 캠페인만 포함됩니다.

![채널 성능/성과 대시보드에서 필터 옵션을 사용하여 태그와 필터링할 캔버스 목록을 선택할 수 있습니다.][3]

## 기간 비교

채널 성능 대시보드는 날짜 범위에서 선택한 기간과 동일한 일수를 합산한 이전 기간을 자동으로 비교합니다. 예를 들어, 대시보드에서 날짜 범위로 "지난 7일"을 선택하면, 지난 기간과의 비교는 지난 7일의 측정기준을 그 이전 7일과 비교하게 됩니다. 커스텀 날짜 범위(예: 5월 10일부터 5월 15일까지, 총 6일간의 데이터)를 선택하면 대시보드는 해당 기간의 측정기준을 5월 4일부터 5월 9일까지의 측정기준과 비교합니다.

비교는 두 기간 간의 차이를 계산하고 이를 이전 기간의 지표로 나누어 계산된 마지막 기간과 현재 기간 간의 백분율 변화입니다.

### 총 개수 및 요금 변경 사항 보기

**합계의 변화 표시**—두 기간 동안의 총 수(예: 전달된 이메일 수)를 비교하는 것—와 **비율의 변화 표시**—비율(예: 전달 비율)을 비교하는 것— 사이를 전환할 수 있습니다.

![채널 성능 대시보드의 총계 변화 또는 비율 변화를 표시하기 위해 전환하는 라디오 버튼입니다.][4]

## 자주 묻는 질문

### 왜 내 대시보드가 빈 값을 표시합니까?

측정기준의 값이 비어 있을 수 있는 몇 가지 시나리오가 있습니다.

- Braze는 선택한 날짜 범위에서 해당 특정 지표에 대해 0을 기록했습니다.
- 선택한 날짜 범위 동안 메시지를 보내지 않았습니다.
- 선택한 날짜 범위에 대해 오픈, 클릭 또는 구독 취소와 같은 측정기준이 있었지만, 발송이나 전송은 없었습니다. 이 경우 Braze는 비율 메트릭을 계산하지 않습니다.

더 많은 측정기준을 보려면 날짜 범위를 확장해 보세요.

### 왜 내 이메일 대시보드가 고유 열람보다 기타 열람을 더 많이 표시합니까?

_고유 열람_ 지표의 경우 Braze는 특정 사용자가 등록한 반복 열람(여기에는 _기계 열람_ 또는 _기타 열람_이 포함될 수 있음)을 중복 제거하여 사용자가 여러 번 열람하더라도 단일 _고유 열람_만 증가하도록 합니다. _기타 열람_의 경우 Braze는 중복 제거를 하지 않습니다.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

[1]: {% image_buster /assets/img_archive/email_performance_dashboard_1.png %}
[2]: {% image_buster /assets/img_archive/email_performance_dashboard_2.png %}
[3]: {% image_buster /assets/img_archive/dashboard_filters.png %}
[4]: {% image_buster /assets/img_archive/email_performance_dashboard_3.png %}
[5]: {% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}
[6]: {% image_buster /assets/img_archive/time_engagement.png %}
[7]: {% image_buster /assets/img_archive/time_engagement_day.png %}
