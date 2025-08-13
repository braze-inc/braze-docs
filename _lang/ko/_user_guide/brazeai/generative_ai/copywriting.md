---
nav_title: 카피라이팅
article_title: AI 카피라이팅 어시스턴트
page_order: 2.1
description: "이 참조 문서에서는 간단한 제품명이나 설명을 OpenAI의 GPT 카피 생성 도구에 전달하여 메시징에 사용할 사람과 유사한 마케팅 카피를 생성하는 기능인 AI 카피라이팅 어시스턴트에 대해 설명합니다."
---

# <sup>BrazeAITM으로</sup> 복사본 생성

> AI 카피라이팅 어시스턴트는 간단한 제품 이름이나 설명을 OpenAI가 소유한 타사 제공업체 GPT 카피 생성 도구에 전달하여 메시징에 사용할 사람과 유사한 마케팅 카피를 생성합니다. 이 기능은 대부분의 메시지 작성기가 Braze 대시보드에서 기본적으로 사용할 수 있습니다.

## 복사본 생성

### 1단계: AI 카피라이터 출시

메시지 작성기에서 <i class="fa-solid fa-wand-magic-sparkles"></i> **AI 카피라이터 실행**을 선택합니다.

인앱 메시지 드래그 앤 드롭 편집기에서 텍스트 블록을 선택하고 <i class="fa-solid fa-wand-magic-sparkles" title="AI 카피라이터"></i>를 선택합니다.

### 2단계: 세부 정보 입력

입력 필드에 제품 이름 또는 설명을 입력한 다음 대략적인 출력 길이를 선택합니다.

채널별 모범 사례에 따라 출력 길이를 특정 채널을 선택하거나 짧게(1문장), 중간(2~3문장) 또는 길게(1단락) 중에서 선택할 수 있습니다.

### 3단계: 추가 사용자 지정(선택 사항)

사본을 추가로 사용자 지정하려면 다음과 같이 할 수 있습니다:

- **브랜드 가이드라인을 적용합니다:** [<sup>BrazeAITM으로</sup> 브랜드 가이드라인을 생성한]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines) 후에는 이를 사용하여 카피를 생성할 수 있습니다.
- **톤을 선택합니다:** 각 톤은 다른 스타일로 사본을 생성합니다. 브랜드 보이스에 가장 잘 어울리는 톤을 선택하세요.
- **과거 캠페인 데이터를 참조하세요**: 활성화하면 캠페인 또는 캔버스 단계를 통해 전송된 이전 모바일 푸시 알림이 새 문구를 생성하는 데 스타일 참조로 사용됩니다. 자세한 내용은 [과거 캠페인 데이터 사용을](#past-campaign-data) 참조하세요.
- **사본 자동 번역:** 사본에 다른 출력 언어를 선택할 수 있습니다. 생성된 콘텐츠는 해당 언어로 출력됩니다.

### 4단계: 사본 생성

완료했으면 **생성을** 선택합니다. 당사는 귀하가 제공한 정보를 사용하여 GPT가 사본을 작성하도록 유도합니다. 응답은 OpenAI에서 가져와서 사용자에게 제공됩니다. 자세한 내용은 [내 데이터가 어떻게 사용되어 OpenAI로 전송되나요?](#ai-policy)

![사용 가능한 다양한 기능을 보여주는 AI 카피라이팅 도우미 모달"]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
당사는 OpenAI의 [콘텐츠 정책](https://beta.openai.com/docs/usage-guidelines/content-policy)을 위반하는 불쾌한 콘텐츠에 대한 응답을 필터링합니다.
{% endalert %}

## 과거 캠페인 데이터 정보 {#past-campaign-data}

푸시를 출력 길이로 사용할 때 **과거 캠페인 데이터 참조**를 선택하면 무작위로 선택된 이전 모바일 푸시 캠페인이 OpenAI로 전송되어 GPT가 이를 카피 생성의 기준으로 사용할 수 있습니다. 이 기능을 활용하지 않으려면 이 확인란을 선택하지 않은 상태로 둡니다. Braze와 OpenAI가 데이터를 사용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요. 

[브랜드 가이드라인]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/)과 함께 사용하는 경우 브랜드 가이드라인과 과거 캠페인 데이터가 모두 최종 결과물에 통합됩니다.

{% multi_lang_include brazeai/generative_ai/policy.md %}
