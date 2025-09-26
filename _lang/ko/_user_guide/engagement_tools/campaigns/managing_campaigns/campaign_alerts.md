---
nav_title: 캠페인 알림
article_title: 캠페인 알림
page_order: 6

page_type: reference
description: "이 참조 문서는 캠페인 알림, 그 이점 및 마음의 평화를 제공하는 데 도움이 되도록 설정하는 방법에 대한 개요를 제공합니다."
tool: Campaigns
channel:
- email
- webhooks

---

# 캠페인 알림

> 우리는 예상과 다를 때 경고를 보내고, 배가 순항하고 있다는 안심을 드리고 싶습니다. 캠페인 임계값 경고는 안심을 제공합니다. 중요한 캠페인이 예상보다 더 많거나 적은 메시지를 보내는 경우 가장 먼저 알 수 있습니다.

캠페인 알림은 다음 캠페인에 사용할 수 있습니다:

- 반복되는 예약 캠페인
- 행동 기반 캠페인
- API로 시작된 캠페인

## 캠페인 알림 설정

캠페인의 분석 페이지로 이동하여 알림 설정을 시작하세요. **Set Up Alert**을 선택하면 상한 및 하한 경고 임계값뿐만 아니라 경고 수신자 및 채널을 지정할 수 있습니다.

![캠페인 모니터링 대화 상자에는 두 개의 버튼이 있습니다: 취소 및 저장]({% image_buster /assets/img_archive/campaign_alerts.png %})

예약된 반복 캠페인의 경우, 캠페인이 보낼 때마다 전송되는 메시지의 상한선과 하한선을 설정할 수 있습니다. 트리거된 캠페인의 경우 시간당 및 일일로 전송되는 메시지 수에 대한 상한 및 하한 임계값을 설정할 수 있습니다.

이메일 알림, 웹훅 알림 또는 둘 다 설정할 수 있습니다. 웹훅 알림은 매우 유용할 수 있습니다. 슬랙 채널에 알림을 보낼 수 있기 때문입니다. Slack과 캠페인 알림을 통합하는 방법에 대한 자세한 내용은 [설명서]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration)를 참조하세요.

{% alert note %}
미래 캠페인에 대한 캠페인 알림을 설정할 때 캠페인이 시작되기 전과 종료된 후에 업데이트를 받을 수 있습니다. 이것은 캠페인 알림이 캠페인이 수동으로 중지될 때까지 계속 전송되기 때문입니다.
{% endalert %}

## 캠페인 알림 웹훅 페이로드

다음은 캠페인 경고 웹훅 본문의 샘플 페이로드입니다. 이 예시는 주어진 캠페인 발송에 대해 발송된 메시지가 500 이하로 떨어질 때 전송되도록 구성된 알림을 사용합니다.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

