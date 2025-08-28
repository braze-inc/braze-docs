---
nav_title: SDK 개요 
article_title: SDK 개요 
page_order: 9
page_type: reference
description: "이 참조 문서는 Braze SDK의 기본 사항을 다룹니다."
---

# SDK 개요 

> Braze SDK는 세션 데이터 수집, 사용자 식별, 구매 및 커스텀 이벤트 기록을 웹사이트나 앱을 통해 쉽게 할 수 있게 해줍니다. 또한 SDK를 사용하여 Braze 대시보드에서 직접 인앱 메시지 및 푸시 알림을 보내 사용자와 상호 작용할 수 있습니다.

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

Braze SDK는 사용자 수준에서 엄청난 양의 데이터를 자동으로 수집하여 앱 및 사용자 기반에 대한 주요 측정기준을 쉽게 확인할 수 있게 합니다. 유사한 앱을 대시보드의 단일 워크스페이스로 그룹화합니다. 예를 들어, iOS 및 Android 버전의 앱을 동일한 작업 공간에 그룹화하여 두 플랫폼의 사용자로부터 수집된 데이터를 볼 수 있습니다. 이것은 웹 및 모바일 채널 전반에 걸쳐 사용자에 대한 보다 완전한 뷰를 제공합니다. See the article on the [Home page]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) for more information.

## 인앱 메시징

SDK는 사용자를 직접 참여시키기 위해 인앱 메시지를 작성하고 보내는 것을 쉽게 만듭니다. 캠페인 전략에 따라 슬라이드업, 모달 또는 전체 화면 메시지를 보낼 수 있습니다. For more information on composing an in-app message, see our page on [creating an in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push displayed on a web browser]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## 푸시 알림

푸시 알림은 사용자와 소통할 수 있는 또 다른 훌륭한 옵션이며, 특히 시간에 민감한 조치를 처리하는 데 유용합니다. 모바일 푸시 알림은 사용자의 기기에 나타나며, 웹 푸시 알림은 사이트가 열려 있지 않을 때에도 나타납니다. For specifics on using push notifications, see our [push notification article]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

웹사이트 또는 앱 사용자는 푸시 알림을 받기 위해 옵트인해야 합니다. See [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) for more details. 

## 세분화 및 전달 규칙

기본값으로 캠페인에 포함된 인앱 메시지는 해당 작업 공간의 모든 버전의 앱으로 전송됩니다. 예를 들어, 메시지는 웹 및 모바일 사용자 모두에게 전송됩니다. 웹 또는 모바일에만 인앱 메시지를 보내려면 캠페인을 적절하게 세그먼트해야 하며, 이는 기본값으로 Braze SDK를 통해 지원됩니다. 

You can create a segment of your web users by setting **Apps and websites targeted** to **Users from specific apps**, then select only your website for the **Specific Apps**.

![Segment Details page with web app in focus]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

이것은 사용자의 행동을 지능적으로 기반으로 하여 타겟팅할 수 있게 해줍니다. 웹 사용자가 모바일 앱을 다운로드하도록 유도하려면 이 세그먼트를 타겟 오디언스로 설정해야 합니다. 메시징 캠페인을 모바일 인앱 메시지를 포함하지만 웹 메시지를 포함하지 않는 메시징 캠페인을 보내려면 세그먼트에서 웹사이트 아이콘의 선택을 해제합니다.

## Braze는 어떤 통합 기능을 가지고 있습니까?
Braze는 많은 플랫폼(웹, Android, iOS, Flutter, React Native 등)을 위한 SDK 버전을 제공하지만, 모두 본질적으로 동일한 방식으로 작동합니다. 따라서 "웹 SDK"에 대한 언급을 보면, 이는 웹사이트를 위한 Braze SDK의 버전일 뿐입니다.

<style>
table th:nth-child(1) {
width: 33%;
}
table th:nth-child(2) {
width: 33%;
}
table th:nth-child(3) {
width: 33%;
}
table td {
word-break: break-word;
text-align: center;
}
</style>
주요 통합   |    |   
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) |[![iOS]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) |[![Web]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)  

모든 통합   |    |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=android) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova&tab=ios) | [![Flutter Android and iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter Android and iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=flutter)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=react%20native) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=roku) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unreal%20engine)

