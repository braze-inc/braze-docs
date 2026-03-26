---
nav_title: Denada
article_title: Denada
alias: /partners/denada/
description: "이 참조 문서에서는 Braze와 Denada 간의 파트너십에 대해 설명합니다. Denada는 AI 기반 마케팅 크리에이티브 플랫폼으로, 자연스러운 대화를 통해 브랜드에 맞는 이메일 템플릿을 만들고 Braze로 직접 내보낼 수 있습니다."
page_type: partner
search_tag: Partner
---

# Denada

> [Denada](https://heydenada.com)는 AI 기반 마케팅 크리에이티브 플랫폼으로, 주제 전문가가 자연스러운 대화를 통해 브랜드에 맞는 마케팅 자료를 만들 수 있습니다. Denada를 사용하면 팀이 디자인 전문 지식 없이도 아이디어 구상부터 완성된 이메일 콘텐츠까지 빠르게 진행할 수 있습니다.

_이 통합은 Denada에서 유지 관리합니다._

## 통합 소개

Braze와 Denada 통합을 사용하면 Denada에서 만든 이메일 템플릿을 Braze 미디어 라이브러리에 자동으로 이미지를 업로드하는 것을 포함하여 Braze로 직접 내보낼 수 있습니다. 이를 통해 크리에이티브 아이디어 구상에서 캠페인 실행까지의 프로세스가 간소화됩니다.

## 필수 조건

이 통합을 사용하려면 다음이 필요합니다:

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Denada 계정 | 이 통합을 사용하려면 [Denada 계정](https://app.heydenada.com)이 필요합니다. |
| Braze REST API 키 | 전체 **템플릿** 권한이 있는 Braze REST API 키. <br><br>이 키는 Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 활용 사례

Denada는 디자인이나 코딩 기술 없이 브랜드에 맞는 이메일 콘텐츠를 만들고자 하는 마케터와 주제 전문가를 위해 만들어졌습니다. 다음과 같은 경우에 적합합니다:
- 대화형 AI를 사용하여 이메일 템플릿을 빠르게 생성하고 Braze로 직접 푸시하고 싶은 경우
- 충돌 감지 및 덮어쓰기 지원을 통해 Denada에서 다시 내보내 기존 Braze 이메일 템플릿을 반복 수정해야 하는 경우
- 내보내기 중 Braze 미디어 라이브러리에 자동 이미지 업로드 및 관리를 원하는 경우

## 통합

### 1단계: 통합 구성

Denada에서 왼쪽 하단의 회사 이름을 선택한 다음 **Team settings** > **Add integration**을 선택합니다.

통합으로 **Braze**를 선택한 다음 Braze **API 키**를 입력하고 사용 가능한 지역 목록에서 **REST API 엔드포인트**를 선택합니다.

{% alert note %}
이 설정은 한 번만 하면 됩니다. 자격 증명이 검증되면 구성이 향후 모든 내보내기에 대해 저장됩니다.
{% endalert %}

### 2단계: Braze로 템플릿 내보내기

Denada에서 에디터의 이메일 템플릿을 열고 **Export** > **Braze**를 선택합니다.

이메일의 템플릿 이름과 제목란을 입력합니다. 이미지 처리 방식을 선택합니다:
- **Upload new:** 모든 이미지를 Braze 미디어 라이브러리에 업로드합니다.
- **Use existing:** 가능한 경우 이전에 업로드한 이미지를 재사용합니다.

동일한 이름의 템플릿이 Braze에 이미 존재하는 경우, Denada가 충돌을 감지하고 기존 템플릿을 덮어쓸지 새 템플릿을 만들지 확인을 요청합니다.

**Export**를 선택합니다. Denada가 템플릿을 HTML로 렌더링하고, 이미지를 Braze에 업로드하며, Braze 계정에 이메일 템플릿을 생성하거나 업데이트합니다.

## 통합 사용

업로드된 Denada 이메일은 Braze의 **템플릿 및 미디어** > **이메일 템플릿**에서 확인할 수 있습니다. 모든 Braze 캠페인 또는 캔버스에서 바로 사용할 수 있습니다.

Denada는 이전 내보내기를 추적하므로, 동일한 템플릿을 다시 내보내면 중복을 만들지 않고 기존 Braze 템플릿을 업데이트할 수 있습니다.