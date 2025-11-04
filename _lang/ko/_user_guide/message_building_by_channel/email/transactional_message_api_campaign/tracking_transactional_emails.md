---
nav_title: 트랜잭션 이메일 추적
article_title: 트랜잭션 이메일 추적
page_order: 1
description: "이 참조 문서에서는 트랜잭션 이메일 캠페인에 대한 실시간 추적을 설정하는 방법을 다룹니다."
page_type: reference
tool:
  - Campaigns
channel: email

---

# 거래 이메일 추적

> 이 페이지는 [트랜잭션 이메일 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)에 대한 실시간 추적을 설정하는 방법을 설명합니다. 엔드포인트 자체에 대한 자세한 내용은 [API 기반 전달을 사용하여 트랜잭션 이메일 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/)를 참조하십시오.

거래 이메일(주문 확인서나 비밀번호 재설정과 같은)을 보낼 때, 고객에게 도달하는지 여부를 아는 것이 중요합니다. Braze 트랜잭션 HTTP 이벤트 포스트백을 통해 모든 트랜잭션 이메일의 상태에 대한 실시간 통찰력을 얻을 수 있으므로 문제가 발생할 경우 신속하게 조치를 취할 수 있습니다.

이 기능을 사용하여:

- **실시간으로 이메일을 모니터링하세요.** 즉시 메시지가 전송, 처리, 배달되었는지 또는 문제가 발생했는지 확인하십시오.
- **적극적으로 대응하다** 재시도 메시지, SMS와 같은 다른 채널로 전환하거나 대체 시스템을 사용하여 커뮤니케이션이 전달되도록 합니다.

## 거래 이메일 추적

{% multi_lang_include http_event_postback.md %}


