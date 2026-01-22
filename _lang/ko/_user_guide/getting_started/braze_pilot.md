---
nav_title: Braze 파일럿
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze 파일럿"
guide_top_text: "Braze 파일럿은 Braze 대시보드와 원활하게 연결되도록 설계된 모바일 앱입니다. 이를 통해 앱에서 캠페인과 캔버스를 실행하여 내 휴대폰에서 Braze 메시지를 생생하게 전달할 수 있습니다. Braze 파일럿에는 다양한 업계를 담당하는 가상의 브랜드에 대한 앱 시뮬레이션 라이브러리가 포함되어 있어 고객 관점에서 메시징이 어떻게 보일지 경험해 볼 수 있습니다."
description: "Braze 대시보드에서 휴대폰으로 메시지를 보내는 다양한 방법을 알아보세요."

guide_featured_title: "섹션 기사"
guide_featured_list:
  - name: Braze 파일럿 시작하기
    link: /docs/user_guide/getting_started/braze_pilot/getting_started/
    image: /assets/img/braze_icons/brush-02.svg
  - name: 데이터 사전
    link: /docs/user_guide/getting_started/braze_pilot/data_dictionary/
    image: /assets/img/braze_icons/book-closed.svg
  - name: 딥링크
    link: /docs/user_guide/getting_started/braze_pilot/deep_links/
    image: /assets/img/braze_icons/link-03.svg

---

## 파일럿 앱 시뮬레이션

Braze Pilot의 핵심은 앱 시뮬레이션 라이브러리입니다. 각 앱은 산업별 가상의 브랜드를 현실적으로 시뮬레이션한 것으로, 다양한 이벤트와 속성을 기록하여 일반적인 Braze 사용 사례를 강화할 수 있는 무한한 기회를 창출합니다.

{% tabs local %}
{% tab Fitness %}

### 스테핑턴턴

스테핑톤은 운동, 운동 목표, 스테핑톤+ 프리미엄 서비스를 제공하는 피트니스 앱입니다. [콘텐츠 카드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) 시연할 수 있는 여러 장소, [기능 플래그로]({{site.baseurl}}/developer_guide/feature_flags) 표시할 수 있는 섹션, 강력한 커스텀 이벤트 로깅 라이브러리를 제공하여 이 업계의 다양한 고객 여정을 설명할 수 있습니다.

마라톤 훈련, 요가, 사이클링, 웨이트 아이콘이 있는 스테핑턴 홈 페이지입니다.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### 바지미로

팬츠라비린스는 (짐작하셨겠지만) 바지를 판매하는 전자상거래 앱입니다! 팬츠라비린스 앱에는 전체 장바구니 결제 경험, 기능 플래그로 인에이블먼트할 수 있는 위시리스트 기능(옵션), 영국 친구들과 교묘한 농담을 나눌 수 있는 다양한 기회가 포함되어 있습니다.

청바지를 장바구니에 추가할 수 있는 옵션이 있는 PantsLabyrinth의 제품 페이지입니다.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

MovieCanon은 콘텐츠 참여와 관련된 일반적인 Braze 사용 사례를 설명하기 위해 완벽하게 설계된 스트리밍 서비스입니다. 

다양한 스릴러 영화를 감상할 수 있는 MovieCanon 앱입니다.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## Pilot과 Braze 대시보드의 연결 방법

Braze SDK는 앱이나 웹사이트와 통합되면 사용자로부터 데이터를 수집하는 코드 패키지입니다. Pilot을 대시보드에 연결하면 휴대폰의 Pilot 앱과 Braze SDK 간의 연결을 초기화하고, 대시보드의 API 키 식별자를 Pilot에 제공하여 Braze 인스턴스와의 고유한 연결을 설정합니다.

파일럿 설정의 첫 번째 단계.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Pilot이 Braze 대시보드에 연결되면 앱이나 웹사이트에 SDK를 통합한 것과 마찬가지로 앱에서 Braze SDK가 작동합니다. 즉, Braze는 그럴 것입니다:

- 앱의 가상의 브랜드와 관련된 커스텀 데이터를 포함하여 사용자 활동에 대한 데이터를 파일럿에 저장하세요.
- 세션 데이터, 기기 정보, 푸시 토큰을 자동으로 수집합니다.
- 푸시 알림, 인앱 메시지, 콘텐츠 카드 메시징 채널이 작동하려면 SDK 통합이 필요합니다.

Braze SDK에 대한 자세한 내용은 [통합을]({{site.baseurl}}/user_guide/getting_started/integration) 참조하세요.

데이터 수집, 분류, 오케스트레이션, 개인화, 고객과의 대화형 피드백 루프를 위한 메시징 채널을 통한 통합, API, SDK를 포함하는 Braze 고객 참여 스택을 통해 고객과 소통할 수 있습니다.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Braze의 고객 프로필

Braze로 전송되는 모든 데이터는 앱 또는 웹사이트의 특정 사용자 전용 사용자 프로필에 저장됩니다. Pilot을 Braze 대시보드와 연결하면, Braze는 Pilot 사용자에 대한 데이터를 기록하기 시작합니다. 이 연결을 통해 생성할 수 있는 사용자 유형은 익명 사용자와 식별자 사용자 두 가지입니다.

### 익명 

이 연결 상태는 아직 로그인하지 않은 앱 또는 웹사이트 게스트의 경험을 나타냅니다. Pilot을 익명 사용자로 초기화하면 Braze가 [익명 사용자 프로필을]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users) 생성하고 여기에 사용자 활동에 대한 데이터를 기록합니다. 익명 사용자는 여전히 캠페인을 통해 타겟팅할 수 있지만, Braze 대시보드에서 직접 고객 프로필을 조회할 수는 없습니다.

### 식별자

이 연결 상태는 외부 식별자라고 하는 회원님에게 할당된 고유 식별자를 통해 Braze가 회원님의 고객 프로필을 인식한다는 의미입니다. 대시보드의 **사용자 검색** 페이지에서 이 외부 식별자를 검색하여 사용자 프로필을 찾을 수 있으며, 여기에는 앱에서의 활동을 기반으로 Pilot에서 기록된 모든 사용자 속성과 이벤트 로그가 저장됩니다.

!"[사용자 "torchie-208117"의 Braze 고객 프로필 예시.]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### 연결 유형

어떤 유형의 연결 상태인지 확인하려면 화면 오른쪽 상단에서 연결 상태를 확인하면 됩니다.

{% tabs local %}
{% tab Anonymous user  %}

**익명은** 익명 사용자로 데이터를 로깅하고 있음을 나타냅니다.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_anonymous.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Identified user %}

식별된 사용자로 데이터를 기록하는 경우 외부 ID 옆에 사용자 아이콘이 표시됩니다.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**연결되지 않음은** 아직 Pilot과의 Braze 소프트웨어 개발 키트 연결을 초기화하지 않았음을 나타냅니다.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## 캠페인 및 캔버스

캠페인과 캔버스는 사용자에게 메시지를 보내는 방법입니다. 

- 캠페인은 다양한 채널에서 특정 오디언스 세그먼트에 단일 메시지를 보내는 데 가장 적합합니다. 
- 캔버스는 여러 채널에서 개인화된 고객 여정을 자동화하고 오케스트레이션할 수 있는 고급 캠페인 워크플로우입니다. 캔버스 내에서 분기 로직, 지연, 결정 지점 및 전환 이벤트를 설정하여 일련의 상호 작용을 통해 고객을 안내할 수 있습니다. 캔버스는 다양한 접점에서 일관되고 원활한 커뮤니케이션을 보장하여 고객 참여와 전환 가능성을 높입니다.

## 지원되는 메시징 채널

현재 Braze 파일럿은 앱에 표시되는 [인앱 메시지를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about) 지원하여 사용자가 적극적으로 참여하는 동안 적시에 메시징을 전달합니다.

무비캐논 앱의 인앱 메시지 "무비캐논을 즐기고 계십니까? 친구를 추천하세요!"라는 문구와 함께 이메일 주소를 입력하여 추천을 보낼 수 있는 옵션이 표시됩니다.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}