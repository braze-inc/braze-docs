---
nav_title: 현재 이벤트 변경 로그
page_order: 6
description: "이 페이지에는 각 Currents 릴리스에 대한 이벤트 변경 사항이 포함되어 있습니다."
tool: Currents
---

# Currents 변경 로그

## 버전 3의 변경 사항 (릴리스 날짜 2025-10-08)

* 새로운 이벤트 유형 `users.messages.rcs.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Rejection`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Read`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Abort`이 추가되었습니다.

* 이벤트 유형 `users.messages.whatsapp.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 관리자에서 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하라는 CTA가 포함된 경우 표시됩니다.
    * 새로운 `string` 필드 `template_name`가 추가되었습니다: [PII] WhatsApp 관리자에서 템플릿의 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Read`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `template_name`가 추가되었습니다: [PII] WhatsApp 관리자에서 템플릿의 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 관리자에서 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하라는 CTA가 포함된 경우 표시됩니다.

* 이벤트 유형 `users.messages.whatsapp.InboundReceive`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `catalog_id`가 추가되었습니다: 수신 메시지에 제품이 참조된 경우 제품의 카탈로그 ID입니다. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 `product_id`가 추가되었습니다: 수신 메시지에 제품이 참조된 경우 제품 SKU입니다. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 관리자에서 Flow의 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `flow_response_json`가 추가되었습니다: [PII] 사용자가 응답한 양식 값입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `in_reply_to`가 추가되었습니다: 이 메시지가 응답한 메시지의 message_id

* 이벤트 유형 `users.messages.whatsapp.Failure`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `template_name`가 추가되었습니다: [PII] WhatsApp 관리자에서 템플릿의 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 관리자에서 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하라는 CTA가 포함된 경우 표시됩니다.

* 이벤트 유형 `users.messages.whatsapp.Delivery`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 관리자에서 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하라는 CTA가 포함된 경우 표시됩니다.
    * 새로운 `string` 필드 `template_name`가 추가되었습니다: [PII] WhatsApp 관리자에서 템플릿의 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.

* 이벤트 유형 `users.messages.sms.Rejection`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 배달, 배달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 배포 ID를 통해 RCS 거부 이벤트에 연결될 수 있습니다.
전송 ID 및 배포 ID를 통해 RCS 거부 이벤트에 연결될 수 있습니다. (이벤트 속성)

* 이벤트 유형 `users.messages.sms.DeliveryFailure`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 배달, 배달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 배포 ID를 통해 RCS 거부 이벤트에 연결될 수 있습니다.

* 이벤트 유형 `users.messages.sms.Delivery`에 대한 필드 변경 사항:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 배달, 배달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 배포 ID를 통해 RCS 거부 이벤트에 연결될 수 있습니다.

