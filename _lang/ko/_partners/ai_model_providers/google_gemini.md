---
nav_title: Google Gemini
article_title: Google Gemini
description: "이 참조 문서에서는 Gemini 모델을 Braze에 연결하여 커스텀 AI 에이전트와 함께 사용할 수 있는 Braze와 Google Gemini 간의 파트너십에 대해 설명합니다."
alias: /partners/gemini/
page_type: partner
search_tag: Partner

---

# Google Gemini

> [Google Gemini](https://deepmind.google/technologies/gemini/)는 텍스트, 코드, 이미지 전반에 걸친 고급 추론을 결합하여 브랜드가 더욱 스마트하고 개인화된 경험을 제공할 수 있도록 지원하는 Google의 AI 모델 제품군입니다.

{% multi_lang_include alerts/important_alerts.md alert='Braze Agents' %}

_이 통합은 Google에서 유지 관리합니다._

## 통합 정보

Braze와 Google Gemini 통합을 통해 Google Gemini API 키 또는 Vertex AI 키를 Braze에 연결하여 커스텀 AI 에이전트를 구축할 때 Gemini 모델을 사용할 수 있습니다. 이 통합을 통해 에이전트는 개인화된 카피를 생성하고, 실시간 의사 결정을 내리거나, Google의 Gemini 모델을 사용하여 카탈로그 필드를 업데이트할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Gemini API 키 또는 Vertex AI 키가 있는 Google Cloud 계정 | Gemini API 키 또는 Vertex AI 키가 있는 Google Cloud 계정입니다. 도움이 필요하면 관리자 또는 [Google Cloud 고객지원](https://cloud.google.com/support)에 문의하세요. |
| Braze 인스턴스 | [API 개요 페이지]({{site.baseurl}}/api/basics/#endpoints) 또는 Braze 온보딩 매니저를 통해 Braze 인스턴스를 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Google Gemini API 키를 Braze에 연결하려면 다음을 수행합니다.

1. Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동하여 Google Gemini를 찾습니다.
2. **API 유형**에서 **Gemini API** 또는 **Vertex AI**를 선택합니다.
3. Google에서 받은 API 키를 입력합니다. Vertex AI의 경우 프로젝트 ID를 입력합니다.
4. **저장**을 선택합니다.

저장 후 에이전트 콘솔에서 [커스텀 에이전트를 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)할 때 Gemini 모델을 선택할 수 있습니다.

통합과 관련된 문제나 질문이 있는 경우 [Google Cloud 고객지원](https://cloud.google.com/support)에 문의하세요.