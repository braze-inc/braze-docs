---
page_order: 2.1
nav_title: ChatGPT 앱
article_title: Braze와 ChatGPT 앱 통합하기
description: "Braze와 ChatGPT 앱을 통합하여 AI 기반 애플리케이션 내에서 분석 및 이벤트 로깅을 인에이블먼트하는 방법을 알아보세요."
platform:
  - ChatGPT Apps
---

# Braze와 ChatGPT 앱 통합하기

> 이 가이드에서는 AI 기반 애플리케이션 내에서 분석 및 이벤트 로깅을 인에이블먼트하기 위해 Braze를 ChatGPT 앱과 통합하는 방법을 설명합니다.

![ChatGPT 앱에 통합된 콘텐츠 카드입니다.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Overview

ChatGPT 앱은 AI 대화형 애플리케이션 구축을 위한 강력한 플랫폼을 제공합니다. Braze를 ChatGPT 앱과 통합하면 AI 시대에도 퍼스트파티 데이터 제어를 계속 유지할 수 있습니다:

- ChatGPT 앱 내에서 고객 참여 및 행동 추적(예: 고객이 사용하는 질문 또는 채팅 기능 식별자)
- AI 상호작용 패턴을 기반으로 Braze 캠페인을 세분화 및 리타겟팅(예: 일주일에 세 번 이상 채팅을 사용한 사용자에게 이메일 보내기)

### 주요 이점

- **고객 여정을 소유하세요:** 사용자가 ChatGPT를 통해 브랜드와 상호 작용하는 동안 귀사는 사용자의 행동, 선호도 및 참여 패턴에 대한 가시성을 유지할 수 있습니다. 이 데이터는 AI 플랫폼의 분석뿐만 아니라 Braze 고객 프로필로 직접 흘러들어갑니다.
- **크로스 플랫폼 리타겟팅:** ChatGPT 앱에서 사용자 상호 작용을 추적하고 AI 사용 패턴에 기반한 개인화된 캠페인으로 자사 채널(이메일, SMS, 푸시 알림, 인앱 메시지)에서 사용자를 리타겟팅할 수 있습니다.
- **1:1 프로모션 콘텐츠를 ChatGPT 대화에 반환합니다:** 팀이 앱용으로 구축한 커스텀 대화형 UI 구성 요소를 사용하여 ChatGPT 경험 내에서 바로 Braze [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) 등을 전달하세요.
- **매출 기여도:** ChatGPT 앱 상호작용에서 발생한 구매 및 전환을 추적하세요.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## 필수 조건

Braze를 ChatGPT 앱과 통합하기 전에 다음이 필요합니다:

- Braze 워크스페이스의 새로운 웹 앱 및 API 키
- OpenAI 플랫폼에서 생성된 [ChatGPT 앱](https://openai.com/index/introducing-apps-in-chatgpt/)[(OpenAI 샘플 앱)](https://github.com/openai/openai-apps-sdk-examples)

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

