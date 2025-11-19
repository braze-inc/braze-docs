---
nav_title: API 사용량 알림
article_title: API 사용량 알림
description: "이 도움말에서는 예기치 않은 트래픽을 사전에 감지할 수 있는 API 사용량 알림에 대한 개요를 제공합니다."
page_order: 3.6
---

# API 사용량 알림

> API 사용량 알림은 API 사용량에 대한 중요한 가시성을 제공하여 예기치 않은 트래픽을 사전에 감지할 수 있게 해줍니다. 이러한 알림을 설정하여 주요 API 요청량을 추적하면 실시간 알림을 받고 마케팅 캠페인에 영향을 미치기 전에 문제를 해결할 수 있습니다.

## API 사용량 알림 정보

API 사용량 알림을 사용하여 다음 카테고리에 대한 요청량을 모니터링할 수 있습니다:

| API 카테고리 | 세부 정보 |
|--------------|---------|
| REST API 엔드포인트 | 메시지 전송, 캠페인 생성, 사용자 내보내기 등 Braze의 백엔드에 대한 모든 REST API 호출의 사용량을 추적합니다. |
| 소프트웨어 개발 키트 API 요청 | 인앱 메시지 트리거 또는 사용자 데이터 동기화 등 클라이언트 앱의 Braze SDK에서 발생한 API 요청을 추적합니다.<br><br>_\*월간 활성 사용자 - CY 24-25를 구매한 고객에게만 제공됩니다._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## API 사용량 알림 만들기

API 사용량 알림을 만들려면 다음과 같이 하세요:

1. **설정** > **API 및 식별자** > **API 사용 알림으로** 이동한 다음 새 알림을 만듭니다.
2. 알림의 이름을 입력하고 알림을 받을 REST API 엔드포인트와 API 키를 선택합니다.
3. 하나 이상의 응답 코드를 선택하고 [알림 임계값을](#api-usage-alert-thresholds) 지정하여 알림 기준을 정의하세요.
4. 완료했으면 **알림 인에이블먼트를** 토글합니다.
    사용자 추적 엔드포인트가 1시간 이내에 100% 증가하면 알림을 보내는 API 사용량 알림의 예입니다.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## 알림 임계값 {#api-usage-alert-thresholds}

알림 기준을 정의할 때 다음과 같은 임계값을 조정할 수 있습니다:

<table>
  <thead>
    <tr>
      <th>필드</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>임계값 조건</td>
      <td>
        알림을 받고자 하는 임계값 볼륨에 이르는 조건을 정의합니다. 지원되는 항목은 다음과 같습니다:<br><br>
        <ul>
          <li><strong>증가</strong> 또는 <strong>감소</strong>: 이전 기간과 요청을 비교합니다.</li>
          <li><strong>백분율로 증가</strong> 또는 <strong>백분율로 감소</strong>: 이전 기간 대비 요청의 백분율 변화율을 비교합니다.</li>
          <li><strong>보다 크거나 같음</strong>, 또는 <strong>보다 작거나 같음</strong>: 시간 창에서 요청을 계산합니다.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>임계값 볼륨</td>
      <td>임계값 조건과 함께 사용됩니다.</td>
    </tr>
    <tr>
      <td>내</td>
      <td>알림 평가를 위한 시간 창입니다.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## 알림 알림 설정하기

이메일 알림, 웹훅 알림 또는 둘 다 설정할 수 있습니다. 웹훅 알림은 Slack 채널과 같은 외부 플랫폼에 알림을 보내는 등의 사용 사례에 매우 유용할 수 있습니다. 예를 들어 알림 기본 설정에 대한 알림을 Slack과 통합하는 방법에 대한 [설명서를](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) 참조하세요.

알림 기준에 도달하면 선택한 이메일로 이메일이 전송됩니다.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### 샘플 페이로드 {#payload}

다음은 API 사용량 알림 웹훅 본문에 대한 페이로드 샘플입니다.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": [
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition: "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    	],
    "timeframe_start": 2025-03-20T15:35:00Z,
    "timeframe_end": 2025-03-20T16:35:00Z,
    "volume": 1500,
    "previous_timeframe_start": 2025-03-20T14:35:00Z,
    "previous_timeframe_end": 2025-03-20T15:35:00Z,
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### 알림 예시

다음은 다음 시나리오에서 알림을 받도록 API 사용량 알림 구성을 설정하는 몇 가지 방법입니다.

{% tabs local %}
{% tab api health %}
API의 일반적인 상태를 모니터링하도록 알림을 설정할 수 있습니다. 예를 들어 API 오류가 이전 시간 대비 20%와 같이 급격하게 증가할 때 이러한 알림을 설정할 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 볼륨 | 내 |
| --- | --- | --- | --- | --- | --- |
| 모든 엔드포인트 | 모든 API 키 | `4XX` 그리고 `5XX` | 10% 증가 | 10 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
워크스페이스가 `/users/track` 엔드포인트의 속도 제한에 도달하면 알림을 받습니다. 다른 Braze 엔드포인트에도 이 구성을 적용할 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 볼륨 | 내 |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | 모든 API 키 | `429` | 다음보다 크거나 같음 | 100 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
이 알림 구성은 API 트리거 캠페인 및 캔버스에서 오류가 발생할 때 알려주며, 그중 일부는 우선 순위가 높을 수 있습니다.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 볼륨 | 내 |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/캠페인/트리거/보내기</code></li><li><code>/캔버스/트리거/보내기</code></li><li><code>/메시징/보내기</code></li></ul>{:/} | 모든 API 키 | `4XX` 그리고 `5XX` | 다음보다 크거나 같은 | 1 | 1시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
파트너 통합이 Braze에 데이터 전송을 중단할 때 알림을 받으려면 다음 알림 구성을 사용하세요.

| 엔드포인트 | API 키 | 응답 코드 | 임계값 조건 | 임계값 볼륨 | 내 |
| --- | --- | --- | --- | --- | --- |
| 모든 엔드포인트 | 파트너 통합에 사용되는 API 키입니다. | 모든 응답 코드 | 다음보다 작거나 같음 | 0 | 1일 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## 고려 사항

- 각 활성 알림은 8시간에 한 번씩만 이메일 또는 웹훅 알림을 보냅니다. 이는 하나의 알림에서 너무 많은 알림이 전송되는 것을 방지하기 위한 것입니다. 알림이 너무 일찍 알려주는 경우 사용 사례에 더 잘 맞도록 알림 기준을 편집해 보세요.
- 워크스페이스당 최대 10개의 알림을 받을 수 있습니다.
