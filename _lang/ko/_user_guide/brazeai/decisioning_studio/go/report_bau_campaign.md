---
nav_title: BAU 캠페인 보고서
article_title: BAU 캠페인 보고
page_order: 10
description: "이 문서에서는 BrazeAI Decisioning Studio Go 포털에서 BAU(Business as Usual) 캠페인 보고와 관련하여 자주 묻는 질문에 대한 답변을 제공합니다."
---

# 평소와 다름없는 비즈니스 캠페인 보고하기

> 이 문서에서는 BrazeAI Decisioning Studio™ Go 포털에서 BAU(Business as Usual) 캠페인 보고와 관련하여 자주 묻는 질문에 대한 답변을 제공합니다.

## BAU 캠페인 보고 정보

기본값으로, BrazeAI Decisioning Studio™ Go 포털 리포팅은 BrazeAI Decisioning Studio™ Go와 무작위 대조군을 비교합니다. 이 두 그룹을 비교하는 것 외에도, BrazeAI Decisioning Studio™ Go의 성능/성과를 비교하고자 하는 BAU(Business as Usual) 그룹이 있을 수 있습니다. BAU 보고를 설정하면 BrazeAI Decisioning Studio™ Go 포털의 한 곳에서 세 그룹의 성능/성과를 모두 확인할 수 있습니다.

BAU 보고 설정의 주요 이점은 세 실험 그룹 모두에 적용될 경우, 의심스러운 머신 클릭과 탈퇴 링크 클릭에서 발생하는 추가 노이즈를 제거하여 가장 정확하고 공정한(또는 "사과 대 사과") 클릭 성능/성과 비교가 가능한 BrazeAI Decisioning Studio™ Go의 무효 클릭 필터링을 적용한다는 점입니다.

## 요구 사항

BAU 보고를 설정하기 전에 먼저 BAU 처리 그룹, BrazeAI Decisioning Studio™ Go, 무작위 대조군 간에 사과 대 사과 비교가 있는지 확인합니다. 여기에는 확인이 포함됩니다:

- 수신자는 실험 기간 동안 두 개 이상의 그룹에 속할 수 없습니다.
- 수신자는 그룹에 무작위로 할당되므로 그룹 할당에 편향성이 없습니다.
- BAU 그룹이 사용할 수 있는 모든 옵션(크리에이티브, 빈도, 시간, 인센티브 또는 제안)을 BrazeAI Decisioning Studio™ Go와 무작위 대조군에서 사용할 수 있습니다.

"사과와 사과를 비교하는" 실험 설계가 없으면 BAU 보고가 혼란스럽거나 오해의 소지가 있을 수 있습니다.

실험 설계를 검증한 후 BAU 보고를 설정하려면 다음 세부 정보가 필요합니다:
- 캠페인의 모든 커뮤니케이션이 BAU 커뮤니케이션인 통합 활성화 플랫폼(Braze, Salesforce 마케팅 클라우드 또는 클라비요)의 캠페인 ID 하나 이상
    - Braze의 경우 캠페인과 캔버스가 허용됩니다.
    - Salesforce 마케팅 클라우드의 경우 여정만 허용됩니다.
    - 클라비요의 경우, 플로우만 허용됩니다.
- 통합 활성화 플랫폼의 하나의 오디언스 ID로 매일 BAU 오디언스에 포함된 수신자를 추적합니다.
    - Braze의 경우 세그먼트만 허용됩니다.
    - Salesforce 마케팅 클라우드의 경우 데이터 확장만 허용됩니다.
    - 클라비요의 경우, 세그먼트만 허용됩니다.

BAU 오디언스를 추적하는 기존 오디언스가 없는 경우 오디언스를 만들어야 합니다.

{% alert note %}
**Braze 고객 전용입니다:** BrazeAI Decisioning Studio™ Go로 내보내는 Braze Current에 BAU 캠페인의 데이터가 포함되어 있는지 확인하세요.
{% endalert %}

## 고려 사항

일반적으로 BrazeAI Decisioning Studio™ Go와 유사하게, BAU 보고는 클릭 KPI만 다루며 전환 KPI는 다루지 않습니다.

현재 특정 캔버스 단계 ID에 대한 필터링은 지원하지 않습니다. 모든 캔버스 단계의 이벤트가 BAU 데이터에 포함됩니다. 특정 캔버스 단계만 포함해야 하는 경우 BAU와의 비교가 무효화될 수 있다는 점에 유의하세요.

## BAU 캠페인 설정하기 

BrazeAI Decisioning Studio™ Go 포털의 지침을 따르세요. 하나 이상의 [캠페인 ID와 오디언스 ID가](#what-are-the-requirements-to-use-in-portal-bau-reporting) 있어야 합니다.