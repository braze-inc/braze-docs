---
nav_title: 4월
page_order: 8
noindex: true
page_type: update
description: "이 문서에는 2021년 4월의 릴리스 노트가 포함되어 있습니다."
---
# 2021년 4월

## iOS 푸시 고급 구현 가이드

이 상세 가이드에서는 푸시 알림 콘텐츠 앱 확장 프로그램을 활용하여 푸시 메시지를 최대한 활용하는 방법에 대해 설명합니다. 여기에는 저희 팀이 구축한 세 가지 사용자 지정 사용 사례(대화형 푸시, 데이터 캡처 푸시, 진행률 기반 푸시)와 함께 제공되는 코드 스니펫, 로깅 분석에 대한 안내가 포함되어 있습니다. 자세한 내용은 [iOS 푸시 고급 구현 가이드]({{site.baseurl}}/developer_guide/push_notifications/examples/?sdktab=swift)를 참조하세요.

## 멀티미디어 메시지 서비스(MMS)에 대한 VFC 지원

가상 연락처 파일(VCF)이라고도 하는 vCard는 주소록/연락처로 쉽게 가져올 수 있는 비즈니스/연락처 정보를 전송하기 위한 표준화된 파일 형식입니다. 이제 이러한 VFC 파일을 [MMS를]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/create/) 통해 전송하고 Braze 미디어 라이브러리에 추가할 수 있습니다. 

## 사용자 삭제에 대한 업데이트

2020년 10월에는 데이터 주체의 전화번호 또는 이메일 주소 삭제 처리 방식을 [개선]({{site.baseurl}}/help/release_notes/2020/october/)했습니다. 

## 새로운 Braze 파트너십

### Airbridge - 기여도

[에어브릿지와 Braze의 통합을]({{site.baseurl}}/partners/message_orchestration/attribution/airbridge/) 통해 모든 오가닉 및 비오가닉 설치 어트리뷰션 데이터를 Braze에 전달하여 보다 개인화된 마케팅 캠페인을 구축하고 사용자가 어디서 유입되었는지 정확히 파악할 수 있습니다.
### Kubit - 분석

[Kubit]({{site.baseurl}}/partners/data_and_analytics/analytics/kubit/)은 코드가 필요 없는 셀프 서비스 분석 플랫폼으로, 즉각적인 제품 인사이트를 제공합니다. Braze와의 원활한 코드 없는 통합을 통해 사용자 코호트 정보를 Braze로 가져와 특정 코호트를 타겟팅하는 참여 캠페인을 시작할 수 있습니다. 또한, Snowflake 보안 데이터 공유를 사용하면 Braze의 원시 캠페인 및 노출 횟수 데이터를 Kubit의 제품 분석과 통합하여 이러한 캠페인의 영향을 실시간으로 측정할 수 있습니다. 

### Census - 고객 데이터 플랫폼

[Census]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/census#census)를 사용하면 엔지니어링 부서의 지속적인 도움 없이도 고객 데이터를 동기화하여 고객 성공, 영업, 마케팅 팀이 모두 동일한 정보를 공유할 수 있습니다.

### 트레저데이터 - 고객 데이터 플랫폼

[Treasure Data]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/treasure_data/)는 데이터, 인사이트, 인게이지먼트가 완벽하게 조화를 이루도록 함으로써 관련성 높은 고객 경험을 제공할 수 있도록 지원합니다. 실행 가능한 지표로 무장한 마케팅, 영업, 고객 서비스를 포함한 CX 팀은 전체 고객 여정에서 지출을 효과적으로 최적화하고 옴니채널 상호 작용을 개인화할 수 있습니다. 

## 자카드 - A/B 테스트

Braze 고객 참여는 멀티채널 마케팅을 통해 관계를 발전시킵니다. Braze는 [Jacquard와]({{site.baseurl}}/partners/message_personalization/dynamic_content/content_optimization_testing/jacquard/) 협력하여 브랜드 보이스에 맞게 맞춤화된 브랜드 언어를 여러 채널에 대규모로 배포할 수 있습니다. Jacquard의 딥러닝 엔진은 테스트를 처리하고 결과를 모니터링하며 학습한 내용을 기반으로 새로운 언어를 생성합니다. 