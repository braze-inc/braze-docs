---
nav_title: 보고서 및 인사이트
article_title: 보고서 및 인사이트
description: "AI 기반 의사 결정이 캠페인에 어떤 영향을 미치는지 파악하기 위해 Braze에서 BrazeAI Decisioning Studio™ 보고서를 보는 방법을 알아보세요."
page_order: 3
---

# 보고서 및 인사이트

> AI 기반 의사 결정이 캠페인에 어떤 영향을 미치는지 파악하기 위해 Braze에서 BrazeAI Decisioning Studio™ 보고서를 보는 방법을 알아보세요. 성과 측정기준부터 데이터 상태 및 시스템 변경 사항까지, 이러한 보고서를 통해 결과를 이해하고, 문제를 해결하고, 자신 있게 정보에 입각한 의사 결정을 내릴 수 있습니다.

## 필수 조건

Braze에서 Decisioning Studio 보고서를 보려면 다음 조건을 충족해야 합니다:

- Braze 및 BrazeAI Decisioning Studio™에 대한 활성 계약을 체결해야 합니다. 
- 고객 성공 매니저에게 연락하여 BrazeAI Decisioning Studio™를 활성화해야 합니다.
- 라이브 BrazeAI Decisioning Studio™ 에이전트가 있어야 합니다.

## 보고서 보기 {#view}

Braze에서 Decisioning Studio 에이전트의 측정기준을 보려면 **AI Decisioning** > **BrazeAI Decisioning Studio™**로 이동한 다음 에이전트를 선택합니다.

![BrazeAI Decisioning Studio™ 보고서 홈 화면에 여러 보고서 카드가 있는 대시보드가 표시됩니다. 각 카드에는 성과, 인사이트, 진단, 타임라인 등의 보고서 유형이 각각에 대한 간략한 설명 및 아이콘과 함께 표시됩니다.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

여기에서 성과, 인사이트, 진단 및 타임라인과 같은 보고서를 볼 수 있습니다. 자세한 내용은 [사용 가능한 보고서](#available-reports)를 참조하세요.

## 보고서 날짜 변경

[보고서를 연](#view) 후 캘린더 드롭다운에서 새 시작 날짜와 종료 날짜를 선택하여 날짜 범위를 변경할 수 있습니다.

![BrazeAI Decisioning Studio™ 날짜 범위 선택기가 열려 있고 캘린더 드롭다운이 표시됩니다. 캘린더에는 보고서 보기를 커스텀하기 위해 선택 가능한 시작 날짜와 종료 날짜가 표시됩니다.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

기본값 시작 날짜를 설정하거나 항상 제외할 날짜를 선택할 수도 있습니다. 제외된 날짜는 해당 에이전트의 모든 보고서에서 필터링됩니다.

날짜를 설정하거나 제외하려면 <i class="fa-solid fa-gear"></i> **설정**을 선택한 다음 필요에 따라 기본값 날짜를 변경하거나 날짜를 제외합니다.

![BrazeAI Decisioning Studio™에서 기본값 시작 날짜를 설정하고 특정 날짜를 보고서에서 제외하는 옵션을 보여주는 설정 패널이 열려 있습니다. 이 패널에는 기본값 시작 날짜 및 제외 날짜라는 두 섹션이 표시됩니다. 제외 날짜 아래에 여러 날짜가 각 날짜 옆에 체크박스와 함께 나열됩니다.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## 사용 가능한 보고서 {#available-reports}

- [성과]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance/): 처리 그룹과 대조군을 비교하는 고수준 에이전트 측정기준으로, **추세** 및 **드라이버 트리** 보기를 제공합니다.
- [인사이트]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights/): 에이전트 선호도 및 SHAP 보고서를 포함하여 동작 뱅크의 추천 옵션이 어떻게 생성되는지 보여줍니다.
- [진단]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics/): 추천 볼륨 및 데이터 피드 모니터링을 포함한 아웃바운드 및 인바운드 데이터 상태를 보여줍니다.
- [타임라인]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline/): 에이전트 실행, 구성 변경, 가드레일 업데이트 등 주요 이벤트를 성과 측정기준과 함께 시각적으로 기록합니다.