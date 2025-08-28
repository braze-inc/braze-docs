---
nav_title: 6월
page_order: 7
noindex: true
page_type: update
description: "이 문서에는 2020년 6월의 릴리스 노트가 포함되어 있습니다."
---
# 2020년 6월

## 리텐션 보고서

이제 리텐션 보고서에서 [캠페인과]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) [캔버스에]({{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/) 대한 범위 리텐션을 제공합니다. 범위 유지는 특정 시간 간격 동안 얼마나 많은 사용자가 다시 돌아와서 선택한 유지 이벤트를 수행했는지 측정합니다. 

## 사용자 추적 API 업데이트

이제 [`users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)는 2020년 6월 2일 이후에 생성된 대시보드 회사에 대해 분당 50,000건의 API 요청을 기본으로 처리합니다. 이 날짜 이전에 생성된 기존 회사 및 해당 워크스페이스는 `users/track` 엔드포인트에 대한 API 요청을 무제한으로 허용합니다.

Braze는 API와 인프라의 안정성과 신뢰성 목표를 향한 한 걸음으로 가장 많이 사용되는 고객 대면 엔드포인트에 이 기본값을 적용하고 있습니다. 부과된 한도는 매우 느슨한 수준이며, 대시보드 회사 및 일반 운영에 영향을 미치는 경우는 극히 일부에 불과합니다. 이 한도를 늘려야 하는 경우 고객 성공 관리자 또는 지원팀에 문의하여 한도 증액을 요청하세요.

