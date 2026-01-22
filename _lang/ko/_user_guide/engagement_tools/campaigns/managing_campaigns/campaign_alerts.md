---
nav_title: 캠페인 알림
article_title: 캠페인 알림
page_order: 6

page_type: reference
description: "이 참고 문서에서는 캠페인 알림의 개요와 혜택, 안심하고 사용할 수 있도록 설정하는 방법에 대해 설명합니다."
tool: Campaigns
channel:
- email
- webhooks

---

# 캠페인 알림

> 예상과 다른 상황이 발생했을 때 알려드리고 배가 순조롭게 항해하고 있다는 안도감을 드리고자 합니다. 캠페인 임계값 알림은 중요한 캠페인이 예상보다 많은 메시지를 보내거나 적은 메시지를 보내는 경우 가장 먼저 알려주므로 안심할 수 있습니다.

다음 캠페인에 대해 캠페인 알림을 사용할 수 있습니다:

- 반복 예약 캠페인
- 액션 기반 캠페인
- API 트리거 캠페인

## 캠페인 알림 설정하기

캠페인의 분석 페이지로 이동하여 알림 설정을 시작합니다. **알림 설정을** 선택하면 상한 및 하한 알림 임계값과 알림 수신자 및 채널을 지정할 수 있습니다.

두 개의 버튼이 있는 캠페인 모니터링 대화상자: 취소하고 저장합니다.]({% image_buster /assets/img_archive/campaign_alerts.png %})

예약된 반복 캠페인의 경우 캠페인이 전송될 때마다 전송되는 메시지에 대한 상한 및 하한 임계값을 설정할 수 있습니다. 트리거된 캠페인의 경우 시간별 및 매일 전송되는 메시지 수에 대한 상한 및 하한 임계값을 설정할 수 있습니다.

이메일 알림, 웹훅 알림 또는 둘 다 설정할 수 있습니다. 웹훅 알림은 Slack 채널에 알림을 보낼 수 있으므로 매우 유용할 수 있습니다. 캠페인 알림을 Slack과 통합하는 방법에 대한 자세한 내용은 [설명서를]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration) 참조하세요.

{% alert note %}
향후 캠페인에 대한 캠페인 알림을 설정할 때 캠페인 시작 전과 종료 후에 업데이트를 받을 수 있습니다. 캠페인 알림은 캠페인이 수동으로 중지될 때까지 계속 전송되기 때문입니다.
{% endalert %}

## 캠페인 알림 웹훅 페이로드

다음은 캠페인 알림 웹훅 본문에 대한 페이로드 샘플입니다. 이 예에서는 지정된 캠페인 전송에 대해 전송된 메시지가 500개 미만이 될 때 알림을 보내도록 구성된 알림을 사용합니다.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

