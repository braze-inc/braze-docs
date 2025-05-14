---
nav_title: AI 카피라이팅 어시스턴트
article_title: AI 카피라이팅 어시스턴트
page_order: 4
description: "이 참조 문서에서는 간단한 제품명이나 설명을 OpenAI의 GPT 카피 생성 도구에 전달하여 메시징에 사용할 사람과 유사한 마케팅 카피를 생성하는 기능인 AI 카피라이팅 어시스턴트에 대해 설명합니다."
---

# AI 카피라이팅 어시스턴트

> AI 카피라이팅 어시스턴트는 간단한 제품 이름이나 설명을 OpenAI가 소유한 타사 제공업체 GPT 카피 생성 도구에 전달하여 메시징에 사용할 사람과 유사한 마케팅 카피를 생성합니다. 이 기능은 대부분의 메시지 작성기가 Braze 대시보드에서 기본적으로 사용할 수 있습니다.

## 카피 만들기 {#steps}

AI 카피라이팅 어시스턴트를 사용하여 카피를 생성하려면 다음 단계를 따르세요.

1. 메시지 작성기에서 <i class="fa-solid fa-wand-magic-sparkles"></i> **AI 카피라이터 실행**을 선택합니다.
   * 인앱 메시지 드래그 앤 드롭 편집기에서 텍스트 블록을 선택하고 <i class="fa-solid fa-wand-magic-sparkles" title="AI 카피라이터"></i>를 선택합니다.
2. 입력 필드에 제품 이름 또는 설명을 입력합니다.
3. 대략적인 출력 길이를 선택합니다. 채널별 모범 사례에 따라 출력 길이를 특정 채널을 선택하거나 짧게(1문장), 중간(2~3문장) 또는 길게(1단락) 중에서 선택할 수 있습니다. 
4. (선택 사항) 브랜드 가이드라인을 만들거나 적용하여 이 카피를 브랜드에 맞게 조정할 수 있습니다. 이러한 가이드라인은 워크스페이스에 저장되며 생성 후 재사용할 수 있습니다. 자세한 내용은 [브랜드 가이드라인 만들기]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/)를 참조하세요.
5. (선택 사항) 사용 가능한 옵션에서 메시지 톤을 선택합니다. 이렇게 하면 생성되는 사본의 스타일이 결정됩니다.
6. (선택 사항) 푸시 알림에 사용할 수 있습니다. 이전 **캠페인 데이터 참조**를 선택하여 이전 모바일 푸시 메시지(캠페인 및 캔버스 단계)를 새 문구 생성을 위한 스타일 참조로 사용합니다. 이 옵션을 선택하면 출력은 이전 메시지의 스타일을 모방합니다.
7. 출력 언어를 선택합니다. 이는 입력 언어와 다를 수 있습니다.
8. Select **Generate**.

Braze는 사용자가 제공한 정보를 사용하여 GPT가 사용자를 대신하여 카피를 작성하도록 유도합니다. 응답은 OpenAI에서 가져와서 사용자에게 제공됩니다. 

![사용 가능한 다양한 기능을 보여주는 AI 카피라이팅 어시스턴트 모달"][1]{: style="max-width:70%;"}

{% alert important %}
당사는 OpenAI의 [콘텐츠 정책](https://beta.openai.com/docs/usage-guidelines/content-policy)을 위반하는 불쾌한 콘텐츠에 대한 응답을 필터링합니다.
{% endalert %}

## 과거 캠페인 데이터 사용

푸시를 출력 길이로 사용할 때 **과거 캠페인 데이터 참조**를 선택하면 무작위로 선택된 이전 모바일 푸시 캠페인이 OpenAI로 전송되어 GPT가 이를 카피 생성의 기준으로 사용할 수 있습니다. 이 기능을 활용하지 않으려면 이 확인란을 선택하지 않은 상태로 둡니다. Braze와 OpenAI가 데이터를 사용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요. 

[브랜드 가이드라인]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/)과 함께 사용하는 경우 브랜드 가이드라인과 과거 캠페인 데이터가 모두 최종 결과물에 통합됩니다.

## GPT란 무엇인가요?

[GPT](https://openai.com/product/gpt-4)는 인공 지능으로 구동되는 OpenAI의 최첨단 자연어 생성 도구입니다. 텍스트 생성, 완성, 분류와 같은 다양한 자연어 작업을 수행할 수 있습니다. 작업할 때 직접 영감을 얻고 카피를 다양화할 수 있도록 Braze 대시보드에 이 기능을 추가했습니다.

## 내 데이터는 어떻게 사용되고 OpenAI로 전송되나요?

복사본을 생성하기 위해 Braze는 사용자의 쿼리를 OpenAI로 전송합니다. Braze에서 OpenAI로 전송되는 모든 쿼리는 익명으로 처리되므로, "과거 캠페인 데이터 참조" 옵션을 활성화할 때 입력한 정보나 과거 캠페인 데이터에 고유 식별 정보를 포함하지 않으면 OpenAI가 해당 쿼리가 누구로부터 전송되었는지 확인할 수 없습니다. [OpenAI의 정책](https://openai.com/policies/api-data-usage-policies)에 따라 Braze를 통해 OpenAI의 API로 전송된 데이터는 모델을 학습하거나 개선하는 데 사용되지 않으며 30일 후에 삭제됩니다. 고객님과 Braze 사이에서 GPT를 사용하여 생성된 모든 콘텐츠는 고객님의 지적 재산입니다. Braze는 해당 콘텐츠에 대한 저작권 소유권을 주장하지 않으며, AI가 생성한 콘텐츠와 관련하여 어떠한 종류의 보증도 하지 않습니다.

## 더 많은 AI 도구

미디어 라이브러리에서 [AI를 사용하여 이미지를 생성할]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) 수도 있습니다. 여기에는 자연어 설명으로 사실적인 이미지와 아트를 만들 수 있는 OpenAI의 AI 시스템인 [DALL-E 3](https://openai.com/index/dall-e-3/)를 활용합니다.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"
