---
nav_title: 커런츠 이벤트 체인지로그
page_order: 6
description: "이 페이지에는 각 커런츠 릴리스에 대한 이벤트 변경 사항이 포함되어 있습니다."
tool: Currents
---

# 커런츠 체인지로그

## 버전 5의 변경 사항(릴리스 날짜 2026-02-04)

* 새로운 이벤트 유형 추가 `agentconsole.AgentExecuted`.

* 새로운 이벤트 유형 추가 `agentconsole.ToolInvocation`.

* 새로운 이벤트 유형 추가 `users.messages.email.Retry`.

* 새로운 이벤트 유형 추가 `users.messages.line.Retry`.

* 새로운 이벤트 유형 추가 `users.messages.pushnotification.Retry`.

* 새로운 이벤트 유형 추가 `users.messages.sms.Retry`.

* 새로운 이벤트 유형 추가 `users.messages.webhook.Retry`.

* 새로운 이벤트 유형 추가 `users.messages.whatsapp.Retry`.

* 이벤트 유형으로 필드 변경 `users.behaviors.pushnotification.TokenStateChange`:
    * 새로운 `long` 필드 추가 `time_ms`: 이벤트가 발생한 시간(밀리초)


## 버전 4의 변경 사항(릴리스 날짜 2026-01-08)

* 이벤트 유형으로 필드 변경 `users.behaviors.pushnotification.TokenStateChange`:
    * 새로운 `string` 필드 추가 `push_token`: 이벤트의 푸시 토큰

* 이벤트 유형으로 필드 변경 `users.messages.pushnotification.Bounce`:
    * 새로운 `string` 필드 추가 `push_token`: 이벤트의 푸시 토큰

* 이벤트 유형으로 필드 변경 `users.messages.pushnotification.Send`:
    * 새로운 `string` 필드 추가 `push_token`: 이벤트의 푸시 토큰

* 이벤트 유형으로 필드 변경 `users.messages.rcs.Click`:
    * 새로운 `string` 필드 추가 `canvas_variation_name`: 이 사용자가 받은 캔버스 변형의 이름
    * `user_phone_number` 필드는 이제 *선택* 사항입니다.

* 이벤트 유형으로 필드 변경 `users.messages.rcs.InboundReceive`:
    * `user_id` 필드는 이제 *선택* 사항입니다.

* 이벤트 유형으로 필드 변경 `users.messages.rcs.Rejection`:
    * 새로운 `string` 필드 추가 `canvas_step_message_variation_id`: 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID


## 버전 3의 변경 사항(릴리스 날짜 2025-10-08)

* 새로운 이벤트 유형 추가 `users.messages.line.Abort`.

* 새로운 이벤트 유형 추가 `users.messages.line.Click`.

* 새로운 이벤트 유형 추가 `users.messages.line.InboundReceive`.

* 새로운 이벤트 유형 추가 `users.messages.line.Send`.

* 새로운 이벤트 유형 추가 `users.messages.rcs.Abort`.

* 새로운 이벤트 유형 추가 `users.messages.rcs.Click`.

* 새로운 이벤트 유형 추가 `users.messages.rcs.Delivery`.

* 새로운 이벤트 유형 추가 `users.messages.rcs.InboundReceive`.

* 새로운 이벤트 유형 추가 `users.messages.rcs.Read`.

* 새로운 이벤트 유형 추가 `users.messages.rcs.Rejection`.

* 새로운 이벤트 유형 추가 `users.messages.rcs.Send`.

* 이벤트 유형으로 필드 변경 `users.messages.sms.Delivery`:
    * 새로운 `boolean` 필드 추가 `is_sms_fallback`: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 발송 ID를 통해 RCS 거부 이벤트에 연결할 수 있습니다.

* 이벤트 유형으로 필드 변경 `users.messages.sms.DeliveryFailure`:
    * 새로운 `boolean` 필드 추가 `is_sms_fallback`: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 발송 ID를 통해 RCS 거부 이벤트에 연결할 수 있습니다.

* 이벤트 유형으로 필드 변경 `users.messages.sms.Rejection`:
    * 새로운 `boolean` 필드 추가 `is_sms_fallback`: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 발신 ID와 발송 ID를 통해 RCS 거부 이벤트에 연결할 수 있습니다. 발신 ID와 발송 ID를 통해 RCS 거부 이벤트에 연결할 수 있습니다. (이벤트 속성정보)

* 이벤트 유형으로 필드 변경 `users.messages.whatsapp.Delivery`:
    * 새로운 `string` 필드 추가 `flow_id`: WhatsApp 매니저에 있는 플로우의 고유 ID입니다. 메시징에 WhatsApp 플로우에 응답하는 CTA가 포함된 경우 표시합니다.
    * 새로운 `string` 필드 추가 `template_name`: [PII] WhatsApp 매니저에 있는 템플릿의 이름입니다. 템플릿 메시지를 보내는 경우 선물하기
    * 새로운 `string` 필드 추가 `message_id`: 이 메시징에 대해 메타에서 생성한 고유 ID입니다.

* 이벤트 유형으로 필드 변경 `users.messages.whatsapp.Failure`:
    * 새로운 `string` 필드 추가 `message_id`: 이 메시징에 대해 메타에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 추가 `template_name`: [PII] WhatsApp 매니저에 있는 템플릿의 이름입니다. 템플릿 메시지를 보내는 경우 선물하기
    * 새로운 `string` 필드 추가 `flow_id`: WhatsApp 매니저에 있는 플로우의 고유 ID입니다. 메시징에 WhatsApp 플로우에 응답하는 CTA가 포함된 경우 표시합니다.

* 이벤트 유형으로 필드 변경 `users.messages.whatsapp.InboundReceive`:
    * 새로운 `string` 필드 추가 `catalog_id`: 인바운드 메시지에서 제품이 참조되는 경우 제품의 카탈로그 ID입니다. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 추가 `product_id`: 인바운드 메시징에 제품이 참조된 경우 제품 SKU. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 추가 `flow_id`: WhatsApp 매니저에 있는 플로우의 고유 ID입니다. 사용자가 WhatsApp 플로우에 응답하는 경우 표시합니다.
    * 새 `string` 필드 추가 `flow_response_json`: [PII] 사용자가 응답한 양식 값입니다. 사용자가 WhatsApp 플로우에 응답하는 경우 표시합니다.
    * 새로운 `string` 필드 추가 `message_id`: 이 메시징에 대해 메타에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 추가 `in_reply_to`: 이 메시징이 회신하는 메시징의 message_id 

* 이벤트 유형으로 필드 변경 `users.messages.whatsapp.Read`:
    * 새로운 `string` 필드 추가 `template_name`: [PII] WhatsApp 매니저에 있는 템플릿의 이름입니다. 템플릿 메시지를 보내는 경우 선물하기
    * 새로운 `string` 필드 추가 `message_id`: 이 메시징에 대해 메타에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 추가 `flow_id`: WhatsApp 매니저에 있는 플로우의 고유 ID입니다. 메시징에 WhatsApp 플로우에 응답하는 CTA가 포함된 경우 표시합니다.

* 이벤트 유형으로 필드 변경 `users.messages.whatsapp.Send`:
    * 새로운 `string` 필드 추가 `flow_id`: WhatsApp 매니저에 있는 플로우의 고유 ID입니다. 메시징에 WhatsApp 플로우에 응답하는 CTA가 포함된 경우 표시합니다.
    * 새로운 `string` 필드 추가 `template_name`: [PII] WhatsApp 매니저에 있는 템플릿의 이름입니다. 템플릿 메시지를 보내는 경우 선물하기
    * 새로운 `string` 필드 추가 `message_id`: 이 메시징에 대해 메타에서 생성한 고유 ID입니다.

