---
nav_title: Worthy
article_title: Worthy
description: "이 참조 문서에서는 개인화된 풍부한 인앱 경험을 생성하고 Braze를 통해 전달할 수 있도록 지원하는 메시지 개인화 플랫폼인 Worthy와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> Braze와 [Worthy](https://worthy.ai/)의 통합을 통해 Worthy의 끌어서 놓기 편집기를 사용하여 개인화된 풍부한 인앱 경험을 손쉽게 생성하고 Braze를 통해 전달할 수 있습니다. 또한, Worthy는 자동으로 다음을 수행합니다:

_This integration is maintained by Worthy._

## 통합 정보

- 메시징을 위한 연결된 콘텐츠 서버 및 보안 API를 생성합니다.
- 분석 및 클릭 추적을 통해 인앱 메시지를 구성하면 Braze에 바로 표시됩니다.
- Worthy의 끌어서 놓기 편집기를 통해 HTML을 자동으로 내보내 Braze의 **커스텀 코드** 인앱 메시지 캠페인을 사용하고, 필요한 API 연결 및 사용자가 구성한 동적 콘텐츠를 완료합니다.

## 사용 사례

- 사용자 온보딩 선택에 기반한 커스텀 환영 경험
- 특별 이벤트 및 프로모션을 위한 인앱 경험
- 앱 행동에 기반한 고객 피드백 및 평가 수집
- 잠재적인 앱 제품 아이디어를 빠르게 테스트
- 다양한 공지사항, 뉴스 및 커뮤니티 업데이트

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| [Worthy](https://worthy.ai/) 계정 | 이 파트너십을 이용하려면 Worthy 계정이 필요합니다. |
| Braze SDK | 리치 인앱 메시지를 보내려면 모바일 애플리케이션에서 Braze SDK를 구성해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 통합

### 1단계: Worthy에서 개인화된 메시지 만들기

Worthy 대시보드에서 앱으로 이동하여 **메시지 작성기를** 선택하고 사용자 참여를 유도하는 데 사용할 맞춤 메시지를 작성합니다.

### 2단계: Braze 캠페인 만들기

Braze에서 [인앱 메시지 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)을 생성하고 **메시지 유형**을 **커스텀 코드**로 설정합니다.

### 3단계: 개인화된 메시지를 Braze에 복사

Worthy 메시지 작성기에서 **내보내기**를 클릭하고 **Braze**를 선택하여 Braze 캠페인에서 사용할 개인화된 메시지를 내보냅니다. 내보낸 콘텐츠를 Braze 캠페인 에디터의 **HTML + 에셋 압축** 아래의 HTML 텍스트 상자에 복사합니다.

끝입니다! Braze 캠페인 에디터의 **테스트** 탭을 사용하여 개인화된 메시지를 즉시 테스트할 수 있습니다. 

