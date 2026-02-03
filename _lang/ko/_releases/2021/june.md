--- 
nav_title: 6월
page_order: 6
noindex: true
page_type: update
description: "이 문서에는 2021년 6월의 릴리스 노트가 포함되어 있습니다."
---

# 2021년 6월

## 트랜잭션 이메일 캠페인

거래 이메일은 발신자와 수신자 간에 합의된 거래를 진행하기 위해 전송되는 이메일입니다. Braze의 [거래 이메일 캠페인은]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) 주문 확인, 비밀번호 재설정, 청구 알림 또는 기타 비즈니스에 중요한 알림과 같은 자동화된 비홍보성 이메일 메시지를 전송하기 위해 특별히 제작되었습니다. 또한 해당 [트랜잭션 이메일 엔드포인트가]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) 생성되었습니다. 트랜잭션 이메일과 새로운 엔드포인트는 일부 Braze 패키지의 일부로만 사용할 수 있습니다. 

## 이벤트 속성에 대한 중첩 개체 지원

이제 Braze는 커스텀 이벤트와 구매 이벤트에 [중첩된 개체]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/nested_object_support/)를 지원합니다. 중첩된 개체를 사용하면 데이터 배열을 커스텀 이벤트 및 구매의 속성으로 전송할 수 있습니다. 이 중첩된 데이터는 Liquid 및 점 표기법을 사용하여 API 트리거 메시지에서 개인화된 정보를 템플릿화하는 데 사용할 수 있습니다.

## 새로운 HMAC 액체 필터

새로운 [`hmac_sha1` 및 `hmac_sha256` 리퀴드 인코딩 필터가]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/) Braze 플랫폼에 추가되었습니다.

## 구매 이벤트 페이지

Braze의 구매 이벤트에 대한 자세한 내용이 궁금하신가요? 자세한 내용은 전용 [구매 이벤트]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) 게시글을 참조하세요.

## 새로운 Braze 파트너십

### Nexla - 워크플로 자동화

[Nexla]({{site.baseurl}}/partners/nexla)는 통합 데이터 운영 분야의 리더이자 2021년 Gartner의 쿨 벤더로 선정된 기업입니다. 커런츠를 사용하여 데이터 웨어하우스로 데이터를 전송하는 고객은 Nexla를 활용하여 해당 데이터를 추출, 변환, 다른 위치로 로드할 수 있으므로 전체 에코시스템에서 데이터에 쉽게 액세스할 수 있습니다. Nexla를 사용하면 Braze 커런츠에서 간단한 포인트 앤 클릭만으로 원하는 목적지로 커스텀 형식의 데이터를 전송할 수 있습니다. 

### Amperity - 고객 데이터 플랫폼

[Amperity는]({{site.baseurl}}/partners/amperity/) 종합적인 기업 고객 데이터 플랫폼으로, 브랜드가 고객을 파악하고 전략적 결정을 내리며 소비자에게 더 나은 서비스를 제공하기 위한 올바른 조치를 일관되게 취할 수 있도록 지원합니다. Amperity는 CDP와 Braze에 걸쳐 고객에 대한 통합 보기를 제공하여 귀사의 중요한 Amperity 데이터를 Braze로 전송할 수 있도록 함으로써 Braze 플랫폼을 지원합니다.

### Digioh - 설문조사

[Digioh]({{site.baseurl}}/partners/digioh/)를 사용하면 목록을 늘리고, 퍼스트파티 데이터를 수집하고, 데이터를 Braze 캠페인에 활용할 수 있습니다. 드래그 앤 드롭 빌더를 사용하면 브랜드 양식, 팝업, 환경 설정 센터, 랜딩 페이지 및 설문조사를 쉽게 생성하여 고객과 소통할 수 있습니다.

### AppsFlyer 오디언스 - 기여도/분석

[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/)는 마케팅 분석 모바일 기여도와 딥링킹을 통해 앱을 분석하고 최적화할 수 있도록 도와주는 모바일 마케팅 분석 및 기여도 플랫폼입니다. [AppsFlyer 오디언스]({{site.baseurl}}/partners/appsflyer_audiences/)를 사용하면 오디언스 세그먼트를 생성하고 이러한 세그먼트를 Braze에 직접 전달하여 강력한 고객 참여 캠페인을 만들 수 있습니다.

