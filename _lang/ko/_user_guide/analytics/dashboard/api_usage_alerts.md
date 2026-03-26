---
nav_title: API 사용 알림
article_title: API 사용 알림
description: "이 문서는 예상치 못한 트래픽을 사전에 탐지할 수 있도록 지원하는 API 사용량 알림에 대한 개요를 제공합니다."
page_order: 3.6
---

# API 사용 알림

> API 사용 알림은 API 사용 현황에 대한 중요한 가시성을 제공하여 예상치 못한 트래픽을 사전에 탐지할 수 있게 합니다. 이러한 알림을 설정하여 주요 API 요청량을 추적하면 실시간으로 알림을 받고, 문제가 마케팅 캠페인에 영향을 미치기 전에 해결할 수 있습니다.

## API 사용 알림에 관하여

API 사용량 알림을 사용하여 다음 범주의 요청량을 모니터링할 수 있습니다:

| API 카테고리 | 세부 정보 |
|--------------|---------|
| REST API 엔드포인트 | Braze 백엔드에 대한 모든 REST API 호출(예: 메시지 전송, 캠페인 생성, 사용자 내보내기 등)의 사용 내역을 추적합니다. |
| 소프트웨어 개발 키트 API 요청 | 클라이언트 앱에서 Braze SDK를 통해 이루어지는 API 요청(예: 인앱 메시지 트리거링 또는 사용자 데이터 동기화)을 추적합니다.<br><br>_\*월간 활성 사용자(MAU) – CY 24-25를 구매한 고객에게만 제공됩니다._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## API 사용량 알림 생성

API 사용량 알림을 생성하려면:

1. **설정** > **API 및 식별자** > **API 사용량 알림으로** 이동한 후 새 알림을 생성하세요.
2. 알림에 대한 이름을 입력하고 알림을 받고 싶은 REST API 엔드포인트 및 API 키를 선택하세요.
3. 하나 이상의 응답 코드를 선택하고 [경보 임계값을](#api-usage-alert-thresholds) 지정하여 경보 기준을 정의하십시오.
4. 완료되면 **알림을** 토글하세요.
    ![API 사용량 경고의 예시로서, '사용자 추적' 엔드포인트가 1시간 내에 100% 증가할 때 알림을 전송합니다.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## 경보 임계값 {#api-usage-alert-thresholds}

경보 기준을 정의할 때 다음 임계값을 조정할 수 있습니다:

<table>
  <thead>
    <tr>
      <th>필드</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>역치 조건</td>
      <td>
        경보를 받고자 하는 임계값에 도달하기까지의 조건을 정의합니다. 다음이 지원됩니다:<br><br>
        <ul>
          <li><strong>증가 </strong>또는 <strong>감소</strong>: 요청을 이전 시간 창과 비교합니다.</li>
          <li><strong>퍼센트 증가</strong> 또는 <strong>퍼센트 감소</strong>: 이전 시간 창 대비 요청량의 백분율 변화를 비교합니다.</li>
          <li><strong>보다 크거나 같음</strong>, 또는 <strong>보다 작거나 같음</strong>: 시간 창 내에서 요청을 집계합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>역치 음량</td>
      <td>임계값 조건과 함께 사용됩니다.</td>
    </tr>
    <tr>
      <td>내부에서</td>
      <td>경보 평가를 위한 시간 창.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 알림 설정

이메일 알림, 웹훅 알림 또는 둘 다 설정할 수 있습니다. 웹훅 알림은 Slack 채널과 같은 외부 플랫폼에 알림을 전송하는 등의 사용 사례에 매우 유용할 수 있습니다. 예를 들어, 알림 설정을 위한 Slack과의 알림 통합에 관한 당사 [설명서를](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) 참조하십시오.

![경고 조건이 충족되면 선택한 이메일 주소로 이메일이 발송됩니다.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### 샘플 페이로드 {#payload}

다음은 API 사용 알림 웹훅 본문의 샘플 페이로드입니다.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### 예시 알림

다음과 같은 시나리오에서 알림을 받도록 API 사용량 알림 설정을 구성하는 방법은 다음과 같습니다.

{% tabs local %}
{% tab api health %}
API의 전반적인 상태를 모니터링하기 위한 알림을 설정할 수 있습니다. 예를 들어, API 오류가 급격히 증가할 때(예: 이전 시간 대비 20% 증가) 이러한 알림을 설정할 수 있습니다.

| Endpoint | API key | 응답 코드 | 역치 조건 | 역치 음량 | 내부에서 |
| --- | --- | --- | --- | --- | --- |
| 모든 엔드포인트 | 모든 API 키 | `4XX` and `5XX` | 10% 증가 | 10 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
작업 공간의 `/users/track`엔드포인트에 대한 속도 제한에 도달하면 알림을 받으세요. 이 구성을 다른 Braze 엔드포인트에도 적용할 수 있습니다.

| Endpoint | API key | 응답 코드 | 역치 조건 | 역치 음량 | 내부에서 |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | 모든 API 키 | `429` | 보다 크거나 같음 | 100 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
이 알림 설정은 API로 트리거된 캠페인 및 캔버스에서 오류가 발생할 때 알려주며, 일부는 높은 우선순위일 수 있습니다.

| Endpoint | API key | 응답 코드 | 역치 조건 | 역치 음량 | 내부에서 |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | 모든 API 키 | `4XX` and `5XX` | 보다 크거나 같음 | 1 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
파트너 통합이 Braze로 데이터 전송을 중단할 때 알림을 받으려면 다음 알림 구성을 사용하십시오.

| Endpoint | API key | 응답 코드 | 역치 조건 | 역치 음량 | 내부에서 |
| --- | --- | --- | --- | --- | --- |
| 모든 엔드포인트 | 파트너 통합에 사용되는 API 키 | 모든 응답 코드 | 보다 작거나 같음 | 0 | 1일 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## 고려 사항

- 각 활성 알림은 8시간마다 한 번씩만 이메일 또는 웹훅 알림을 전송합니다. 이는 단일 알림에서 너무 많은 알림이 발생하지 않도록 하기 위함입니다. 알림이 너무 일찍 전송되는 경우, 사용 사례에 더 잘 맞도록 알림 기준을 편집하는 것을 고려하십시오.
- 작업 공간당 최대 10개의 알림을 설정할 수 있습니다.
