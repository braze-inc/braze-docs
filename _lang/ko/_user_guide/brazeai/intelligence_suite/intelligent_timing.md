---
nav_title: Intelligent Timing
article_title: Intelligent Timing
page_order: 1.3
description: "이 문서는 Intelligent Timing(이전 Intelligent Delivery) 개요와 캠페인 및 Canvas에서 이 기능을 활용하는 방법을 설명합니다."
---

# [![Braze Learning 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Intelligent Timing

> Intelligent Timing을 사용하면 Braze가 산정한 각 사용자별 최적 전송 시점, 즉 사용자가 상호작용(열기 또는 클릭)할 가능성이 가장 높은 시점에 메시지를 보냅니다. 사용자에게 선호하는 시간에 메시지를 보내고 있음을 더 쉽게 확인할 수 있어 참여를 높일 수 있습니다.

## Intelligent Timing 정보

Braze는 사용자의 앱 및 각 메시지 채널과의 과거 상호작용에 대한 통계 분석으로 최적 전송 시점을 계산합니다. 사용하는 상호작용 데이터는 다음과 같습니다.

- 세션 시간
- 푸시 직접 열기
- 푸시 영향 열기
- 이메일 클릭
- 이메일 열기([기계 열기]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens) 제외)
- SMS 클릭([링크 단축]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) 및 고급 추적이 활성화된 경우에만)

최적 전송 시점 계산에 필요한 관련 상호작용 데이터가 없는 사용자의 경우 대체 시간을 지정할 수 있습니다.

## 사용 사례

- 시간에 민감하지 않은 반복 캠페인 전송
- 여러 시간대의 사용자에게 캠페인 자동화
- 가장 참여도가 높은 사용자에게 메시지 보내기(상호작용 데이터가 가장 많음)

캠페인 및 Canvas에 대한 상세 설정 단계, 무음 시간, 대체 시간, 제한 사항 및 FAQ는 왼쪽 목차 또는 Braze 대시보드 도움말의 전체 문서를 참조하세요.
