---
nav_title: Contentsquare
article_title: Contentsquare
description: "이 참조 문서에서는 고객의 디지털 경험을 기반으로 메시지를 타겟팅하여 캠페인의 관련성과 전환율을 향상시킬 수 있는 디지털 경험 분석 플랫폼인 Contentsquare와 Braze 간의 파트너십을 간략히 설명합니다."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/)는 고객 경험에 대한 뛰어난 이해 기반을 구축하는 디지털 경험 분석 플랫폼입니다.

_This integration is maintained by Contentsquare._

## 통합 정보

Braze와 Contentsquare의 통합을 통해 실시간 신호(사기, 불만 신호 등)를 Braze에서 커스텀 이벤트로 전송할 수 있습니다. Contentsquare의 경험 인사이트를 활용하여 고객의 디지털 경험과 신체 언어를 기반으로 메시지를 타겟팅하여 캠페인의 관련성과 전환율을 향상시킬 수 있습니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Contentsquare 계정 | 이 파트너십을 활용하려면 Contentsquare 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. Braze 대시보드에서 새 키를 만들려면 **설정** > **API 키로** 이동합니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL][1]. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

다음은 몇 가지 일반적인 Braze 및 Contentsquare 사용 사례입니다.
- Braze 내에서 고객 경험 데이터를 표시하여 고객의 의도에 따라 메시지를 고도로 개인화합니다.
- 고객의 디지털 행동, 망설임, 좌절감, 의도를 기반으로 고객을 리타겟팅하세요.
- Contentsquare 내에서 안 좋은 경험을 식별하고 타겟팅 메시지와 유지 제안으로 고객을 재유치합니다.
- 적절한 시기와 장소에서 보다 관련성 있고 공감할 수 있는 메시지를 전송하여 위험에 처한 고객을 회복하세요.

## 통합

Contentsquare를 Braze에 통합하려면 Contentsquare 통합 카탈로그에서 '실시간 신호' 통합 설치를 요청해야 합니다.

1. Contentsquare의 **설정** 메뉴에서 **콘솔**을 클릭합니다. 그러면 현재 작업 중인 프로젝트로 리디렉션됩니다. 
2. **프로젝트** 페이지에서 **연동** 탭으로 이동하여 **\+ 연동 추가** 버튼을 클릭합니다.
3. 통합 서비스 카탈로그에서 **실시간 신호** 통합 서비스를 찾아 **추가**를 클릭합니다. 그러면 Contentsquare 팀이 연락하여 Braze에 실시간 신호를 보낼 수 있도록 코드 스니펫을 구성합니다.
4. 이제 Contentsquare에서 통합을 처리합니다. 연동이 완료되면 표시기 텍스트가 업데이트됩니다.

자세한 내용은 [Contentsquare 통합 요청](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186)을 참조하세요.

## 이 통합 사용

통합이 완료되면 Contentsquare 커스텀 이벤트를 캠페인과 캔버스에서 사용할 수 있습니다. **데이터 설정** > **사용자 지정** 이벤트에서 어떤 이벤트가 Braze로 전송되는지 확인할 수 있습니다.

![Braze 커스텀 이벤트 탭의 Contentsquare 실시간 신호 데이터][1]


[1]: {% image_buster /assets/img/contentsquare_custom_events.png %} 
