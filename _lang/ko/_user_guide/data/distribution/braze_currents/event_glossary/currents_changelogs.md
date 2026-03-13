---
nav_title: 커런츠 이벤트 체인지로그
page_order: 6
description: "이 페이지에는 각 커런츠 릴리스에 대한 이벤트 변경 사항이 포함되어 있습니다."
tool: Currents
---

# 커런츠 체인지로그

## 버전 6의 변경 사항 (릴리스 날짜 2026-03-04)

### 저장소에 대한 변경 사항

* 이벤트 유형 `agentconsole.AgentExecuted`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `error` 추가: 오류 설명

* 이벤트 유형 `agentconsole.ToolInvocation`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `request_id` 추가: 이 전체 LLM 요청 및 완전 실행을 위한 고유 ID

* 이벤트 유형 `users.messages.rcs.InboundReceive`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름

### 데이터 공유에 대한 변경 사항

* 이벤트 유형 `agentconsole.AgentExecuted`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `error` 추가: 오류 이름

* 이벤트 유형 `agentconsole.ToolInvocation`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `request_id` 추가: 이 전체 LLM 요청 및 완전 실행을 위한 고유 ID

* 이벤트 유형 `users.behaviors.subscription.GlobalStateChange`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.behaviors.subscriptiongroup.StateChange`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.campaigns.Conversion`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `conversion_behavior` 추가: 전환 행동을 설명하는 JSON 인코딩 문자열

* 이벤트 유형 `users.campaigns.EnrollInControl`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름

* 이벤트 유형 `users.canvas.Conversion`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `conversion_behavior` 추가: 전환 행동을 설명하는 JSON 인코딩 문자열

* 이벤트 유형 `users.canvas.Entry`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.canvas.exit.MatchedAudience`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.canvas.exit.PerformedEvent`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.canvas.experimentstep.Conversion`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `experiment_split_name` 추가: 실험 분할의 이름
    * 새로운 `string` 필드 `conversion_behavior` 추가: 전환 행동을 설명하는 JSON 인코딩 문자열

* 이벤트 유형 `users.canvas.experimentstep.SplitEntry`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `experiment_split_name` 추가: 실험 분할의 이름

* 이벤트 유형 `users.canvasstep.Progression`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.banner.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름

* 이벤트 유형 `users.messages.banner.Click`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름

* 이벤트 유형 `users.messages.banner.Impression`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름

* 이벤트 유형 `users.messages.contentcard.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.contentcard.Click`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.contentcard.Dismiss`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.contentcard.Impression`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.contentcard.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Bounce`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Click`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Deferral`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Delivery`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.MarkAsSpam`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Open`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Retry`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.SoftBounce`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.email.Unsubscribe`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.featureflag.Impression`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름

* 이벤트 유형 `users.messages.inappmessage.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.inappmessage.Click`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.inappmessage.Impression`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.line.Retry`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.pushnotification.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.pushnotification.Bounce`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.pushnotification.InfluencedOpen`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.pushnotification.IosForeground`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.pushnotification.Open`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.pushnotification.Retry`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.pushnotification.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.rcs.InboundReceive`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름

* 이벤트 유형 `users.messages.sms.Abort`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.sms.CarrierSend`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.sms.Delivery`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.sms.DeliveryFailure`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.sms.InboundReceive`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name` 추가: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.sms.Rejection`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `campaign_name` 추가: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name` 추가: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name` 추가: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.sms.Retry`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.sms.Send`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.sms.ShortLinkClick`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.webhook.Abort`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.webhook.Failure`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름

* 이벤트 유형 `users.messages.webhook.Retry`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.webhook.Send`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.whatsapp.Abort`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.whatsapp.Click`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.whatsapp.Delivery`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.whatsapp.Failure`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.whatsapp.InboundReceive`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름

* 이벤트 유형 `users.messages.whatsapp.Read`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.whatsapp.Retry`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름

* 이벤트 유형 `users.messages.whatsapp.Send`에 대한 필드 변경:
    * 새로운 `string` 필드 `campaign_name`가 추가되었습니다: 캠페인의 이름
    * 새로운 `string` 필드 `canvas_name`가 추가되었습니다: 캔버스의 이름
    * 새로운 `string` 필드 `canvas_step_name`가 추가되었습니다: 캔버스 단계의 이름
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 새로운 `string` 필드 `message_variation_name`가 추가되었습니다: 메시지 변형의 이름

## 버전 5의 변경 사항 (출시 날짜 2026-02-04)

### 저장소에 대한 변경 사항

* 새로운 이벤트 유형 `agentconsole.AgentExecuted`이 추가되었습니다.

* 새로운 이벤트 유형 `agentconsole.ToolInvocation`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Retry`이 추가되었습니다.

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`에 대한 필드 변경:
    * 새로운 `long` 필드 `time_ms`가 추가되었습니다: 이벤트가 발생한 시간(밀리초)

### 데이터 공유에 대한 변경 사항

* 새로운 이벤트 유형 `agentconsole.AgentExecuted`이 추가되었습니다.

* 새로운 이벤트 유형 `agentconsole.ToolInvocation`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Retry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Retry`이 추가되었습니다.

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`에 대한 필드 변경:
    * 새로운 `long` 필드 `time_ms`가 추가되었습니다: 이벤트가 발생한 시간(밀리초)

## 버전 4의 변경 사항 (출시 날짜 2026-01-07)

### 저장소에 대한 변경 사항

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`에 대한 필드 변경:
    * 새로운 `string` 필드 `push_token`가 추가되었습니다: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.pushnotification.Bounce`에 대한 필드 변경:
    * 새로운 `string` 필드 `push_token`가 추가되었습니다: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.pushnotification.Send`에 대한 필드 변경:
    * 새로운 `string` 필드 `push_token`가 추가되었습니다: 이벤트의 푸시 토큰

* 이벤트 유형 `users.messages.rcs.Click`에 대한 필드 변경:
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 필드 `user_phone_number`이 이제 *선택적*입니다.

* 이벤트 유형 `users.messages.rcs.InboundReceive`에 대한 필드 변경:
    * 필드 `user_id`이 이제 *선택적*입니다.

* 이벤트 유형 `users.messages.rcs.Rejection`에 대한 필드 변경:
    * 새로운 `string` 필드 `canvas_step_message_variation_id`가 추가되었습니다: 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID

### 데이터 공유에 대한 변경 사항

* 이벤트 유형 `users.messages.rcs.Click`에 대한 필드 변경:
    * 새로운 `string` 필드 `canvas_variation_name`가 추가되었습니다: 이 사용자가 받은 캔버스 변형의 이름
    * 필드 `user_phone_number`이 이제 *선택적*입니다.

* 이벤트 유형 `users.messages.rcs.InboundReceive`에 대한 필드 변경:
    * 필드 `user_id`이 이제 *선택적*입니다.

* 이벤트 유형 `users.messages.rcs.Rejection`에 대한 필드 변경:
    * 새로운 `string` 필드 `canvas_step_message_variation_api_id`가 추가되었습니다: 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID

## 버전 3의 변경 사항 (출시 날짜 2025-10-08)

### 저장소에 대한 변경 사항

* 새로운 이벤트 유형 `users.messages.line.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Read`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Rejection`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Send`이 추가되었습니다.

* 이벤트 유형 `users.messages.sms.Delivery`에 대한 필드 변경:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 배포 ID를 통해 RCS 거부 이벤트에 연결될 수 있습니다.

* 이벤트 유형 `users.messages.sms.DeliveryFailure`에 대한 필드 변경:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 배포 ID를 통해 RCS 거부 이벤트에 연결될 수 있습니다.

* 이벤트 유형 `users.messages.sms.Rejection`에 대한 필드 변경:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 거부된 RCS 메시지로 인해 SMS 대체 메시지가 전송되었음을 나타냅니다. 메시지는 전달, 전달 실패 또는 거부로 이어질 수 있습니다. 전송 ID 및 배포 ID를 통해 RCS 거부 이벤트에 연결될 수 있습니다. 전송 ID 및 배포 ID를 통해 RCS 거부 이벤트에 연결될 수 있습니다. (이벤트 속성정보)

* 이벤트 유형 `users.messages.whatsapp.Delivery`에 대한 필드 변경:
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하라는 CTA가 포함된 경우 표시됩니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Failure`에 대한 필드 변경:
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하라는 CTA가 포함된 경우 표시됩니다.

* 이벤트 유형 `users.messages.whatsapp.InboundReceive`에 대한 필드 변경:
    * 새로운 `string` 필드 `catalog_id`가 추가되었습니다: 수신 메시지에 제품이 참조된 경우 제품의 카탈로그 ID입니다. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 `product_id`가 추가되었습니다: 수신 메시지에 제품이 참조된 경우 제품 SKU입니다. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `flow_response_json` 추가: [PII] 사용자가 응답한 양식 값입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `in_reply_to`가 추가되었습니다: 이 메시지가 응답한 메시지의 message_id입니다.

* 이벤트 유형 `users.messages.whatsapp.Read`에 대한 필드 변경:
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하라는 CTA가 포함된 경우 표시됩니다.

* 이벤트 유형 `users.messages.whatsapp.Send`에 대한 필드 변경:
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 메시지에 WhatsApp Flow에 응답하라는 CTA가 포함된 경우 표시됩니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.

### 데이터 공유에 대한 변경 사항

* 새로운 이벤트 유형 `users.messages.line.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.line.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Read`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Rejection`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.rcs.Send`이 추가되었습니다.

* 이벤트 유형 `users.messages.sms.Delivery`에 대한 필드 변경:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 이 거부된 RCS 메시지에 대해 SMS 대체가 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트에 연결/페어링되어 있습니다.

* 이벤트 유형 `users.messages.sms.DeliveryFailure`에 대한 필드 변경:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 이 거부된 RCS 메시지에 대해 SMS 대체가 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트에 연결/페어링되어 있습니다.

* 이벤트 유형 `users.messages.sms.Rejection`에 대한 필드 변경:
    * 새로운 `boolean` 필드 `is_sms_fallback`가 추가되었습니다: 이 거부된 RCS 메시지에 대해 SMS 대체가 시도되었는지 여부를 나타냅니다. SMS 전달 이벤트에 연결/페어링되어 있습니다.

* 이벤트 유형 `users.messages.whatsapp.Delivery`에 대한 필드 변경:
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.

* 이벤트 유형 `users.messages.whatsapp.Failure`에 대한 필드 변경:
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.

* 이벤트 유형 `users.messages.whatsapp.InboundReceive`에 대한 필드 변경:
    * 새로운 `string` 필드 `catalog_id`가 추가되었습니다: 수신 메시지에 제품이 참조된 경우 제품의 카탈로그 ID입니다. 그렇지 않으면 비어 있습니다.
    * 새로운 `string` 필드 `product_id`가 추가되었습니다: 구매한 제품의 ID
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `flow_response_json` 추가: [PII] 사용자가 응답한 양식 값입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `in_reply_to`가 추가되었습니다: 이 메시지가 응답한 메시지의 message_id입니다.

* 이벤트 유형 `users.messages.whatsapp.Read`에 대한 필드 변경:
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.

* 이벤트 유형 `users.messages.whatsapp.Send`에 대한 필드 변경:
    * 새로운 `string` 필드 `flow_id`가 추가되었습니다: WhatsApp 매니저의 Flow의 고유 ID입니다. 사용자가 WhatsApp Flow에 응답하는 경우 표시됩니다.
    * 새로운 `string` 필드 `template_name` 추가: [PII] WhatsApp 매니저의 템플릿 이름입니다. 템플릿 메시지를 보내는 경우 표시됩니다.
    * 새로운 `string` 필드 `message_id`가 추가되었습니다: 이 메시지에 대해 Meta에서 생성한 고유 ID입니다.

## 버전 2의 변경 사항(출시 날짜 없음)

### 저장소에 대한 변경 사항

* 새로운 이벤트 유형 `users.behaviors.app.FirstSession`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.app.SessionEnd`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.app.SessionStart`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.CustomEvent`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.InstallAttribution`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.liveactivity.PushToStartTokenChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.liveactivity.UpdateTokenChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Location`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Purchase`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.subscription.GlobalStateChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.subscriptiongroup.StateChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Uninstall`이 추가되었습니다.

* 새로운 이벤트 유형 `users.campaigns.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.campaigns.EnrollInControl`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.Entry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.exit.MatchedAudience`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.exit.PerformedEvent`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.experimentstep.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.experimentstep.SplitEntry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvasstep.Progression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Dismiss`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Bounce`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Deferral`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.MarkAsSpam`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Open`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.SoftBounce`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Unsubscribe`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.featureflag.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.liveactivity.Outcome`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.liveactivity.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Bounce`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.IosForeground`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Open`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.CarrierSend`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.DeliveryFailure`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Rejection`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.ShortLinkClick`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Failure`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Failure`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Read`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.RandomBucketNumberUpdate`이 추가되었습니다.

### 데이터 공유에 대한 변경 사항

* 새로운 이벤트 유형 `changelogs.GlobalControlGroup`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.app.FirstSession`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.app.NewsFeedImpression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.app.SessionEnd`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.app.SessionStart`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.CustomEvent`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.geofence.DataEvent`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.geofence.RecordEvent`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.InstallAttribution`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.liveactivity.PushToStartTokenChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.liveactivity.UpdateTokenChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Location`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Purchase`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.subscription.GlobalStateChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.subscriptiongroup.StateChange`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.Uninstall`이 추가되었습니다.

* 새로운 이벤트 유형 `users.behaviors.UpgradedApp`이 추가되었습니다.

* 새로운 이벤트 유형 `users.campaigns.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.campaigns.EnrollInControl`이 추가되었습니다.

* 새로운 이벤트 유형 `users.campaigns.FrequencyCap`이 추가되었습니다.

* 새로운 이벤트 유형 `users.campaigns.Revenue`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.Entry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.exit.MatchedAudience`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.exit.PerformedEvent`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.experimentstep.Conversion`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.experimentstep.SplitEntry`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.FrequencyCap`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvas.Revenue`이 추가되었습니다.

* 새로운 이벤트 유형 `users.canvasstep.Progression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.banner.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Dismiss`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.contentcard.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Bounce`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Deferral`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.MarkAsSpam`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Open`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.SoftBounce`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.email.Unsubscribe`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.featureflag.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.inappmessage.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.liveactivity.Outcome`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.liveactivity.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.newsfeedcard.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.newsfeedcard.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.newsfeedcard.Impression`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Bounce`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.InfluencedOpen`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.IosForeground`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Open`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.pushnotification.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.CarrierSend`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.DeliveryFailure`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Rejection`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.sms.ShortLinkClick`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Failure`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.webhook.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Abort`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Click`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Delivery`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Failure`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.InboundReceive`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Read`이 추가되었습니다.

* 새로운 이벤트 유형 `users.messages.whatsapp.Send`이 추가되었습니다.

* 새로운 이벤트 유형 `users.RandomBucketNumberUpdate`이 추가되었습니다.

* 새로운 이벤트 유형 `users.UserDeleteRequest`이 추가되었습니다.

* 새로운 이벤트 유형 `users.UserOrphan`이 추가되었습니다.
