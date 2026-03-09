---
page_order: 2.1
nav_title: 챗GPT 앱
article_title: Braze를 ChatGPT 앱과 통합하세요
description: "Braze를 ChatGPT 앱과 통합하여 AI 기반 애플리케이션 내에서 분석 및 이벤트 로깅을 인에이블먼트하는 방법을 알아보세요."
platform:
  - ChatGPT Apps
---

# Braze를 ChatGPT 앱과 통합하세요

> 이 가이드는 Braze를 ChatGPT 앱과 통합하여 AI 기반 애플리케이션 내에서 분석 및 이벤트 로깅을 인에이블먼트하는 방법을 다룹니다.

![ChatGPT 앱에 통합된 콘텐츠 카드.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Overview

ChatGPT 앱은 AI 대화형 애플리케이션을 구축하기 위한 강력한 플랫폼을 제공합니다. Braze를 ChatGPT 앱과 통합함으로써, AI 시대에도 다음과 같은 방식을 포함해 퍼스트파티 데이터 통제권을 지속적으로 유지할 수 있습니다:

- ChatGPT 앱 내에서 사용자 참여도와 행동을 추적하세요(예: 고객이 어떤 질문이나 채팅 기능을 사용하는지 식별).
- AI 상호작용 패턴(예: 주당 3회 이상 채팅을 이용한 사용자에게 이메일 발송)을 기반으로 Braze 캠페인을 세그먼트하고 리타겟팅합니다.

### 주요 이점

- **고객 여정을 주도하세요:** 사용자가 ChatGPT를 통해 귀사의 브랜드와 상호작용하는 동안, 귀사는 그들의 행동, 선호도 및 참여 패턴에 대한 가시성을 유지합니다. 이 데이터는 AI 플랫폼의 분석 기능뿐만 아니라 Braze 고객 프로필에 직접 반영됩니다.
- **크로스 플랫폼 리타겟팅:** 사용자의 ChatGPT 앱 내 상호작용을 추적하고, AI 사용 패턴을 기반으로 한 개인화된 캠페인을 통해 자사 채널(이메일, SMS, 푸시 알림, 인앱 메시지) 전반에 걸쳐 리타겟팅하세요.
- **1:1 프로모션 콘텐츠를 ChatGPT 대화로 반환:** 팀이 앱을 위해 구축한 커스텀 대화형 UI 구성 요소를 활용하여 ChatGPT 환경 내에서 Braze [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) 등을 직접 전달하세요.
- **매출 기여도:** ChatGPT 앱 상호작용에서 비롯된 구매 및 전환을 추적합니다.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## 필수 조건

Braze를 ChatGPT 앱과 통합하기 전에 다음을 준비해야 합니다:

- Braze 작업 공간에 새로운 웹 앱 및 API 키
- OpenAI 플랫폼에서 생성된 [ChatGPT 앱](https://openai.com/index/introducing-apps-in-chatgpt/) ([OpenAI 샘플 앱](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

