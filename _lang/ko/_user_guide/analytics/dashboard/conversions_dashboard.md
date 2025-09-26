---
nav_title: 전환 대시보드
article_title: 전환 대시보드
alias: "/conversions_dashboard_v2/"
description: "전환 대시보드에서는 다양한 기여도 방법을 사용하여 캠페인, 캔버스, 채널 전반의 전환을 분석할 수 있습니다."
page_order: 3
page_type: reference
tool: 
  - Reports
---

# 전환 대시보드

> 전환 대시보드는 다양한 [어트리뷰션 방법을](#attribution-methods) 사용하여 캠페인, 캔버스 및 채널 전반의 전환을 분석합니다. 전환을 측정할 때 시간 프레임, 전환 이벤트, 전환 기간을 지정할 수 있습니다.

## 보고서 설정

전환 대시보드 보고서를 설정하려면 다음과 같이 하세요:

1. **애널리틱스** > **전환으로** 이동합니다.
2. 보고서의 **날짜 범위** (최대 90일)를 선택합니다.
3. 분석할 캠페인 또는 캔버스(또는 둘 다)를 선택합니다. 
   - (선택 사항) 태그를 선택하여 캠페인과 캔버스를 필터링합니다.  
4. 메시지에 대해 분석할 **채널을** 선택합니다.
5. Select a **Breakdown by** layer to view different dimensions of data, such as by variant, Canvas step, country, or language.
6. (Optional) If you want to calculate conversions of an event that wasn't set up as a conversion event on the campaign or Canvas, turn on [Use custom events](#using-custom-events).
7. 선택한 메시지를 분석할 [어트리뷰션 방법을](#attribution-methods) 선택합니다.

{% alert note %}
여러 채널에 대한 전환을 분석하는 경우, **어트리뷰션 방법은** 기본적으로 **라스트 터치 어트리뷰션으로** 설정됩니다.
{% endalert %}

{:start="8"}
8\. **만들기를** 선택하여 보고서를 실행합니다.

페이지가 로드된 후 **전환 이벤트를** 선택하여 전환 데이터에 대한 보고서를 필터링합니다. 사용 가능한 선택 항목에는 캔버스 및 캠페인에 미리 구성된 이벤트가 포함됩니다. 보고서를 설정할 때 사용자 지정 이벤트를 선택한 경우(6단계) 이 옵션을 사용할 수 없습니다.

### 사용자 지정 이벤트 사용

사용자 지정 이벤트 지표가 전환 대시보드에 표시되려면 페이지에 지정된 날짜 범위의 전환 이벤트와 캔버스 입력 이벤트가 있어야 합니다. 

캠페인 또는 캔버스에서 전환 이벤트로 설정되지 않은 이벤트의 전환을 계산하려면 전환 이벤트로 사용할 특정 사용자 지정 이벤트를 선택합니다. 

1. 보고서를 설정할 때 **커스텀 이벤트 사용**을 켭니다.
2. 전환 이벤트로 사용할 사용자 지정 이벤트를 선택합니다.
3. 전환으로 계산할 이벤트가 발생했어야 하는 전환 기간을 선택합니다.

{% alert note %}
사용자 지정 이벤트를 선택하면 페이지에 **전환 이벤트** 드롭다운이 표시되지 않으며 다른 사용자 지정 이벤트의 전환을 보려면 리포팅을 다시 실행해야 합니다.
{% endalert %}

## 보고서 이해하기

보고서는 세 개의 섹션으로 나뉩니다:

- [전환 세부 정보](#conversion-details)
- [전환 퍼널](#conversion-funnel)
- [시간 경과에 따른 전환 수](#conversions-over-time)

### 전환 세부 정보

전환 세부 정보 테이블에는 항상 *수신자* 열과 *전환* (비율 및 합계)에 대한 열이 표시됩니다. 표시되는 나머지 두 개의 테이블 열은 보고서를 설정할 때 선택한 옵션에 따라 달라집니다. 

![Conversion details table showing Touches as the attribution method for columns three and four.]({% image_buster /assets/img_archive/conversions2_details.png %}){: style="border:none"}

다음 표에서는 가능한 메트릭에 대해 설명합니다.

| 표시된 메트릭 | 설명 |
| --- | --- |
| 수신자 | 보고서의 날짜 범위 내에서 선택한 채널을 통해 메시지를 수신한 사용자 수입니다. |
| 전환율(수신자) | 다음으로 계산됨: (전환 수) / (수신자 수) |
| 기여도 방법 | 보고서를 설정할 때 선택한 [어트리뷰션 방법에](#attribution-methods) 따라 정의됩니다. 라스트 터치 어트리뷰션의 경우 또는 여러 채널을 선택한 경우 [터치로](#terms-to-know) 표시됩니다. |
| 전환율(어트리뷰션 방식) | 보고서를 설정할 때 선택한 [어트리뷰션 방법에](#attribution-methods) 따라 정의됩니다. 여러 채널을 선택한 경우 기본적으로 라스트 터치 어트리뷰션으로 설정됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[보고서를 설정할](#setting-up-your-report) 때 캠페인 또는 캔버스에 대한 분류 수준 세부 정보를 선택한 경우(5단계) <i class="fas fa-angle-down"></i> 을 클릭하여 표를 확장할 수 있습니다.

### 전환 퍼널

이 막대 그래프는 선택한 채널을 기준으로 각 [인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)의 절대 개수를 보여줍니다. 전환 수는 선택한 어트리뷰션 방법에 따라 정의됩니다.

기본적으로 선택한 모든 캠페인과 캔버스가 표시됩니다. 캠페인 또는 캔버스를 선택 해제하려면 제외하려는 캠페인 또는 캔버스의 이름을 선택합니다. 참여 이벤트에 대한 자세한 내용을 보려면 각 막대 위로 마우스를 가져가세요.

시계열 데이터를 다운로드하려면 다운로드 옵션을 선택합니다: PNG, JPEG, PDF, SVG 또는 CSV.

{% alert note %}
이 그래프는 한 번에 하나의 채널에 대한 데이터만 표시합니다. 차트의 **채널** 드롭다운을 사용하여 단일 채널을 선택합니다.
{% endalert %}

![Conversions funnel bar graph for two email campaigns showing similar results for Email Delivered, Email Opened, Email Clicked, and Conversions.]({% image_buster /assets/img_archive/conversions2_funnel.png %})

### 시간 경과에 따른 전환 수

이 시계열 그래프에는 시간 경과에 따른 캠페인 또는 캔버스별 전환 수치가 포함되어 있습니다. 기본적으로 선택한 모든 캠페인과 캔버스가 표시됩니다. 캠페인 또는 캔버스를 선택 해제하려면 제외하려는 캠페인 또는 캔버스의 이름을 클릭합니다.

시계열 데이터를 다운로드하려면 <i class="fas fa-bars"></i> 을 선택한 다음 다운로드 옵션을 선택합니다. 사용 가능한 옵션은 PNG, JPEG, PDF, SVG 또는 CSV입니다.

![Conversions over time time series graph for two email campaigns, showing conversions by day.]({% image_buster /assets/img_archive/conversions2_over_time.png %})

### 기여도 방법

| 기여도 방법 | 정의 | 요금 계산 | 채널별 옵션 |
| --- | --- | --- | --- |
| 수신 시 | 메시지 수신 후 발생한 총 전환 수 | (고유 수신 전환 수) / (고유 수신자 수)로 계산됩니다. | {::nomarkdown}<ul><li>이메일 전송 시</li><li>SMS 전송 시</li></ul>{:/} |
| 발송 시 | 메시지 전송 후 발생한 총 전환 수 | (고유 발신 전환 수) / (고유 수신자 수)로 계산됨 | {::nomarkdown}<ul><li>푸시 전송 시</li><li>콘텐츠 카드 전송 시</li><li>SMS 전송 시</li></ul>{:/} |
| 열람 시 | 메시지 열기 후 발생한 총 전환 수 | (고유 열람 전환 수) / (고유 수신자 수)로 계산됨 | {::nomarkdown}<ul><li>이메일 열람 시</li><li>푸시 열람 시</li></ul>{:/} |
| 클릭 시 | 메시지 클릭으로 발생한 총 전환 수 | (고유 클릭 전환 수) / (고유 수신자 수)로 계산됨 | {::nomarkdown}<ul><li>이메일 클릭 시</li><li>콘텐츠 카드 클릭 시</li><li>IAM 클릭 시</li></ul>{:/} |
| 노출 시 | 노출 후 발생한 총 전환 수 | (고유 노출 전환 수) / (고유 수신자 수)로 계산됨 | {::nomarkdown}<ul><li>IAM 노출 시</li><li>콘텐츠 카드 노출 시</li></ul>{:/} |
| 마지막 터치 시 | 전환 기간 동안 마지막으로 터치하거나 클릭한 메시지에 모든 크레딧을 부여하는 전환입니다. | (터치 횟수) / (고유 수신자 수)로 계산됨 | 보고서에 여러 채널이 추가된 경우 라스트 터치 기여도가 자동으로 선택됩니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 알아두어야 할 용어

| 기간 | 정의 |
| --- | --- |
| 터치 | 메시지와의 물리적 상호작용 또는 접점입니다.<br><br>터치에는 다음이 포함될 수 있습니다:<br>{::nomarkdown}<ul><li>이메일 클릭</li><li>푸시 열람</li><li>콘텐츠 카드 클릭</li><li>인앱 메시지 클릭</li><li>SMS Click</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
