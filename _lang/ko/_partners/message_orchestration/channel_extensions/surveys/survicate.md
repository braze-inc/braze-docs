---
nav_title: Survicate
article_title: Survicate
description: "이 참고 문서에서는 여러 채널과 사용자 여정 전반에 걸쳐 고객 인사이트를 수집, 분석 및 조치할 수 있도록 지원하는 고객 피드백 플랫폼인 Braze와 Survicate의 파트너십에 대해 설명합니다."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

![Braze 이메일에서 임베드된 HTML 설문조사(첫 번째 질문)의 예제.][2]{: style="float:right;max-width:40%;border:0; margin-left:8px;"}

> [Survicate는][1] 여러 채널과 사용자 여정 전반에 걸쳐 고객 인사이트를 수집, 분석 및 조치할 수 있는 고객 피드백 플랫폼입니다.  

_This integration is maintained by Survicate._

## 통합 정보

Braze와 Survicate의 통합을 통해 설문조사를 Braze 이메일에 직접 삽입하여 응답률을 높일 수 있습니다. 설문조사 응답은 사용자 지정 속성 또는 이벤트로서 Braze 사용자 프로필과 자동으로 동기화됩니다. 실시간 인사이트를 통해 고객 데이터와 함께 피드백을 쉽게 추적 및 분석하고 타겟팅된 후속 조치를 만들 수 있습니다.

## 사용 사례

Braze와 Survicate는 다양한 피드백 사용 사례를 함께 다루며 실행 가능한 사용자 인사이트를 수집하고 고객 경험을 개선할 수 있도록 지원합니다:

- 고객 만족도 측정(예: CSAT, NPS 또는 CES)
- 제품 피드백 수집
- 사용자 또는 시장 조사를 수행하다
- 고객 여정의 중요한 단계에서 인사이트 수집하기
- 고객 피드백을 기반으로 개인화된 워크플로우를 트리거하고 후속 캠페인을 자동화하세요.

## 통합의 주요 기능

Survicate와 Braze의 통합은 실시간 데이터 동기화를 제공하므로 Survicate 설문조사의 최신 정보를 Braze에서 즉시 확인할 수 있습니다. 설문조사 응답을 기반으로 이 데이터를 사용하여 시기적절한 맞춤형 조치를 취할 수 있습니다.

- **설문조사 응답을 사용자 지정 사용자 속성으로 Braze에 전송합니다**: 설문조사 응답 데이터로 Braze 사용자 프로필을 보강하세요.
- **Braze에서 사용자 지정 이벤트를 트리거하세요**: 설문조사 답변에 기반한 이벤트를 사용하여 특정 그룹을 타겟팅하거나 후속 캠페인을 시작하세요.
- **세부 세그먼트를 구축하세요**: Survicate 설문조사 데이터를 사용하여 Braze 세그먼트를 생성하여 홍보 활동을 더욱 맞춤화할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Survicate 계정 | 이 통합을 활성화하려면 Survicate 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Survicate에서 설문조사를 작성하세요

1. Survicate 패널에서 **새 설문조사 만들기를** 선택합니다.
2. 설문조사 채널을 선택하세요. 이메일**, 링크, 웹사이트, 제품 내 설문조사, 모바일 앱 설문조사를** 사용할 수 있습니다. 
3. 설문조사를 처음부터 디자인하거나, AI 설문조사 작성기를 사용하거나, 바로 사용할 수 있는 100개 이상의 템플릿 중에서 선택하세요.

![설문조사를 만드는 네 가지 옵션: 처음부터 시작하기, 템플릿 사용, AI 지원 생성, 질문 가져오기.][4]

### 2단계: Braze 이메일을 통해 자동으로 응답자 식별하기

1. 설문조사가 준비되면 **구성** 탭으로 이동합니다.
2. *응답자 식별에서* **Braze를** 선택합니다. 이렇게 하면 응답이 자동으로 Braze 고객 프로필에 연결되므로 설문조사에서 연락처 정보를 물어볼 필요가 없습니다.

![Braze가 응답자로 선정되었습니다.][5]

### 3단계: 통합 연결

1. 그런 다음 **연결 탭에서** Braze를 찾아 **연결을** 선택하여 통합합니다. 
2. Braze 계정 워크스페이스 API 키와 Braze 인스턴스 URL을 삽입합니다.

![워크스페이스 API 키와 Braze 인스턴스 URL을 입력하는 필드입니다.][3]

### 4단계: 설문조사를 공유하세요

1. 그런 다음 **공유** 탭에서 설문조사를 배치할 위치를 선택합니다. 옵션은 다음과 같습니다:
- **직접 링크**: 링크를 복사하여 Braze에서 버튼이나 하이퍼링크로 사용할 수 있습니다.
- **첫 번째 질문을 포함합니다**: HTML 코드를 복사하여 첫 번째 설문조사 질문을 Braze 이메일 본문에 바로 삽입합니다.
- **웹사이트 또는 제품 내에서 설문조사를 시작합니다**: 추적 코드를 한 번만 설치하면 서베이케이트 패널에서 바로 설문조사를 실시간으로 설정할 수 있습니다.

### 5단계: Braze 이메일 캠페인에 설문조사 추가

1. Braze에서 설문조사 링크 또는 HTML 코드를 이메일 캠페인의 콘텐츠에 붙여넣습니다.
2. 서바이베이트 내에서 바로 피드백을 수집하고 응답을 추적하세요.


[1]: https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter
[2]:  {% image_buster /assets/img/survicate/survicate_asset_1.png %}
[3]:  {% image_buster /assets/img/survicate/image1.png %}
[4]:  {% image_buster /assets/img/survicate/survicate_asset_3.png %}
[5]:  {% image_buster /assets/img/survicate/survicate_asset_2.png %}
