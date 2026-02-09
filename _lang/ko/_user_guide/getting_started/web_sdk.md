---
nav_title: SDK 개요
article_title: SDK 개요 
page_order: 9
page_type: reference
description: "이 참조 문서는 Braze SDK의 기본 사항을 다룹니다."
---

# SDK 개요 

> Braze SDK는 세션 데이터를 수집하고 사용자를 식별하며 웹사이트나 앱을 통해 구매 및 커스텀 이벤트를 기록합니다. 또한 소프트웨어 개발 키트를 사용하여 Braze 대시보드에서 직접 인앱 메시지와 푸시 알림을 전송하여 사용자의 참여를 유도할 수 있습니다.

간단히 말해서, Braze 소프트웨어 개발 키트:
* 사용자 데이터를 수집하고 동기화하여 통합된 고객 프로필로 만듭니다
* 마케팅 인게이지먼트 데이터 및 비즈니스에 특정한 커스텀 데이터를 캡처합니다
* 푸시 알림, 인앱 메시지 및 콘텐츠 카드 메시징 채널을 지원합니다

## SDK란 무엇입니까?
소프트웨어 개발 키트(SDK)는 새로운 기능을 지원하기 위해 디지털 애플리케이션에 추가할 수 있는 사전 제작된 도구 세트입니다. 이는 작은 코드 블록들로 구성되어 있습니다. Braze SDK는 앱 또는 사이트로 정보를 보내고 받는 데 사용됩니다. 고객 프로필 생성, 커스텀 이벤트 로깅, 푸시 알림 트리거링 등 시작부터 필수 기능을 제공하도록 설계되었습니다. 

이 기능은 Braze에서 기본값으로 제공되므로 개발자는 핵심 비즈니스에 집중할 수 있습니다. SDK가 없으면 모든 Braze 클라이언트는 데이터 처리, 세분화 논리, 전달 옵션, 익명 사용자 처리, 캠페인 분석 등을 위한 모든 인프라와 도구를 완전히 처음부터 만들어야 합니다. 그것은 훨씬 더 오래 걸리고 우리 SDK를 통합하는 데 걸리는 한 시간 정도보다 훨씬 더 고통스러울 것입니다.

## 구현

앱이나 사이트에 SDK를 통합하려면 누군가가 SDK의 코드를 해당 애플리케이션을 구동하는 전체 코드 베이스에 추가해야 합니다. 이는 엔지니어링 팀이 참여하여 본질적으로 Braze 앱을 연결하여 정보와 작업이 그들 사이에서 흐르도록 한다는 것을 의미합니다. 하지만 개발자가 참여하더라도 SDK는 통합하기 쉽고 사용자 친화적으로 설계되었습니다. 

시간을 절약하고 원활한 통합을 보장하기 위해 엔지니어링 팀이 커스텀 이벤트, 커스텀 속성 및 SDK를 동시에 설정할 것을 권장합니다. Learn more about the steps that your Marketing and Engineering teams will need to think through together by reading our [implementation article]({{site.baseurl}}/user_guide/getting_started/integration/). 

## 데이터 집계

Braze 소프트웨어 개발 키트는 사용자 수준 데이터를 자동으로 캡처하여 앱과 사용자 기반에 대한 주요 측정기준을 제공합니다. 유사한 앱을 하나의 작업 공간으로 그룹화하여(예: iOS와 Android 버전을 함께) 여러 플랫폼에서 수집된 데이터를 확인하고 사용자 활동에 대한 전체적인 그림을 구축하세요. See the article on the [Home page]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) for more information.

## 인앱 메시징

소프트웨어 개발 키트를 사용하여 인앱 메시지를 직접 작성하고 전송하세요. 캠페인 전략에 따라 슬라이드업, 모달 또는 전체 화면 메시지를 선택할 수 있습니다. 구성에 대한 자세한 내용은 [인앱 메시지 만들기를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) 참조하세요.

![푸시가 웹 브라우저에 표시됨]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## 푸시 알림

푸시 알림은 사용자와 소통할 수 있는 또 다른 훌륭한 옵션이며, 특히 시간에 민감한 조치를 처리하는 데 유용합니다. 모바일 푸시 알림은 사용자의 기기에 나타나며, 웹 푸시 알림은 사이트가 열려 있지 않을 때에도 나타납니다. For specifics on using push notifications, see our [push notification article]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

웹사이트 또는 앱 사용자는 푸시 알림을 받기 위해 옵트인해야 합니다. See [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) for more details. 

## 세분화 및 전달 규칙

기본값으로 캠페인에 포함된 인앱 메시지는 해당 작업 공간의 모든 버전의 앱으로 전송됩니다. 예를 들어, 메시지는 웹 및 모바일 사용자 모두에게 전송됩니다. 웹 또는 모바일에만 인앱 메시지를 보내려면 캠페인을 적절하게 세그먼트해야 하며, 이는 기본값으로 Braze SDK를 통해 지원됩니다. 

You can create a segment of your web users by setting **Apps and websites targeted** to **Users from specific apps**, then select only your website for the **Specific Apps**.

![웹 앱에 초점을 맞춘 세그먼트 세부 정보 페이지]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

이것은 사용자의 행동을 지능적으로 기반으로 하여 타겟팅할 수 있게 해줍니다. 웹 사용자가 모바일 앱을 다운로드하도록 유도하려면 이 세그먼트를 타겟 오디언스로 설정해야 합니다. 메시징 캠페인을 모바일 인앱 메시지를 포함하지만 웹 메시지를 포함하지 않는 메시징 캠페인을 보내려면 세그먼트에서 웹사이트 아이콘의 선택을 해제합니다.

## 지원 플랫폼

Braze는 웹, Android, Swift 등 다양한 플랫폼용 SDK를 제공합니다. 전체 목록은 [Braze 개발자 가이드를]({{site.baseurl}}/developer_guide/home) 참조하세요.
