---
nav_title: Braze 파일럿
page_order: 10.5
layout: dev_guide
guide_top_header: "Braze 파일럿"
guide_top_text: "Braze 파일럿은 Braze 대시보드와 원활하게 연결되도록 설계된 모바일 앱입니다. 이 앱을 통해 캠페인과 캔버스를 시작하여 Braze 메시지를 자신의 전화에서 실현할 수 있습니다. Braze 파일럿에는 다양한 산업을 대표하는 허구의 브랜드에 대한 앱 시뮬레이션 라이브러리가 포함되어 있어 고객의 관점에서 메시징이 어떻게 보일지 경험할 수 있습니다."
description: "Braze 대시보드에서 전화로 메시지를 전송하는 다양한 방법을 확인해 보세요."

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

Braze 파일럿의 핵심은 앱 시뮬레이션 라이브러리입니다. 각 앱은 산업별 허구의 브랜드를 현실적으로 시뮬레이션한 것으로, 일반적인 Braze 사용 사례를 지원하는 무한한 기회를 창출하는 다양한 이벤트와 속성을 기록하도록 설계되었습니다.

{% tabs local %}
{% tab Fitness %}

### Steppington

Steppington은 운동, 운동 목표 및 Steppington+ 프리미엄 서비스를 제공하는 피트니스 앱입니다. 여기에는 [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards)를 보여줄 수 있는 여러 장소와 [기능 플래그]({{site.baseurl}}/developer_guide/feature_flags)로 활성화할 수 있는 섹션, 그리고 이 산업의 많은 고객 여정을 설명할 수 있는 강력한 커스텀 이벤트 로깅 라이브러리가 포함되어 있습니다.

![마라톤 훈련, 요가, 사이클링 및 웨이트 아이콘이 있는 Steppington의 홈 페이지입니다.]({% image_buster /assets/img/braze_pilot/steppington_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab eCommerce %}

### PantsLabyrinth

PantsLabyrinth는 (맞습니다) 바지를 판매하는 전자상거래 앱입니다! PantsLabyrinth 앱에는 전체 쇼핑 카트 체크아웃 경험, 기능 플래그로 활성화할 수 있는 선택적 위시리스트 기능, 그리고 영국 친구들과의 교묘한 농담을 위한 많은 기회가 포함되어 있습니다.

![장바구니에 청바지를 추가할 수 있는 PantsLabyrinth의 제품 페이지입니다.]({% image_buster /assets/img/braze_pilot/pantslabyrinth_app.png %}){:style="max-width:50%"}

{% endtab %}
{% tab Streaming %}

### MovieCanon 

MovieCanon은 콘텐츠 참여에 대한 일반적인 Braze 사용 사례를 설명하기 위해 완벽하게 설계된 스트리밍 서비스입니다. 

![시청할 수 있는 다양한 스릴러가 있는 MovieCanon 앱입니다.]({% image_buster /assets/img/braze_pilot/moviecanon_app.png %}){:style="max-width:50%"}

{% endtab %}
{% endtabs %}

## 파일럿이 Braze 대시보드와 연결되는 방법

Braze SDK는 앱이나 웹사이트에 통합되면 사용자로부터 데이터를 수집하는 코드 패키지입니다. 파일럿을 대시보드에 연결하면, 전화의 파일럿 앱과 Braze SDK 간의 연결을 초기화하고, 대시보드의 API 키 식별자를 파일럿에 제공하여 Braze 인스턴스와의 고유한 연결을 설정합니다.

![파일럿 설정의 첫 번째 단계입니다.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

파일럿이 Braze 대시보드에 연결되면, Braze SDK는 SDK를 귀하의 앱이나 웹사이트와 통합한 후처럼 앱에서 작동합니다. 이는 Braze가 다음을 수행함을 의미합니다:

- 앱의 허구 브랜드에 특정한 커스텀 데이터를 포함하여, 파일럿에서 사용자 활동에 대한 데이터를 저장합니다.
- 세션 데이터, 기기 정보 및 푸시 토큰을 자동으로 수집합니다.
- SDK 통합이 필요하여 작동하는 푸시 알림, 인앱 메시지 및 콘텐츠 카드 메시징 채널을 지원합니다.

Braze SDK에 대한 자세한 내용은 [통합]({{site.baseurl}}/user_guide/getting_started/integration)을 확인하세요.

![Braze 고객 참여 스택으로, 통합, API, 데이터 수집, 분류, 오케스트레이션, 개인화 및 고객과의 상호작용 피드백 루프를 위한 메시징 채널과 함께 작동하는 SDK를 포함합니다.]({% image_buster /assets/img/braze_pilot/braze_sdk_diagram.png %}){:style="max-width:70%"}

## Braze의 사용자 프로필

Braze에 전송된 모든 데이터 조각은 귀하의 앱이나 웹사이트의 특정 사용자에게 전용된 사용자 프로필에 저장됩니다. 파일럿을 Braze 대시보드와 연결하면, Braze는 파일럿의 사용자로서 귀하에 대한 데이터를 기록하기 시작합니다. 이 연결을 통해 생성될 수 있는 두 가지 유형의 사용자가 있습니다: 익명 및 식별된.

### 익명 

이 연결 상태는 아직 로그인하지 않은 귀하의 앱이나 웹사이트의 게스트 경험을 나타냅니다. 파일럿을 익명 사용자로 초기화하면, Braze는 귀하를 위한 [익명 사용자 프로필]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users)을 생성하고 그곳에 귀하의 활동에 대한 데이터를 기록합니다. 익명 사용자도 캠페인으로 타겟팅할 수 있지만, Braze 대시보드에서 직접 사용자 프로필을 조회할 수는 없습니다.

### 식별된

이 연결 상태는 Braze가 귀하에게 할당된 고유 식별자인 외부 식별자를 통해 귀하의 사용자 프로필을 인식함을 의미합니다. 대시보드의 **사용자 검색** 페이지에서 이 외부 식별자를 검색하여 귀하의 사용자 프로필을 찾을 수 있으며, 이는 앱에서의 활동에 따라 파일럿에서 기록된 모든 사용자 속성과 이벤트를 저장합니다.

![사용자 "torchie-208117"의 Braze 사용자 프로필 예시입니다.]({% image_buster /assets/img/braze_pilot/user_profile.png %})

### 연결 유형

연결 유형을 확인하려면 화면 오른쪽 상단에서 연결 상태를 확인할 수 있습니다.

{% tabs local %}
{% tab Anonymous user  %}

**익명**은 익명 사용자로 데이터를 기록하고 있음을 나타냅니다.

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

식별된 사용자로 데이터를 기록하는 경우, 외부 ID 옆에 사용자 아이콘이 표시됩니다.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_identified_user.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Not connected %}

**연결되지 않음**은 Braze SDK 연결을 Pilot와 초기화하지 않았음을 나타냅니다.

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/status_not_connected.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## 캠페인 및 캔버스

캠페인과 캔버스는 사용자에게 메시지를 보내는 방법입니다. 

- 캠페인은 다양한 채널에서 특정 오디언스 세그먼트에 단일 메시지를 보내는 데 가장 적합합니다. 
- 캔버스는 여러 채널에서 개인화된 고객 여정을 자동화하고 조율할 수 있는 고급 캠페인 워크플로우입니다. 캔버스 내에서 분기 로직, 지연, 결정 지점 및 전환 이벤트를 설정하여 일련의 상호 작용을 통해 고객을 안내할 수 있습니다. 캔버스는 다양한 접점에서 일관되고 원활한 커뮤니케이션을 보장하여 고객 참여 및 전환 가능성을 높이는 데 도움을 줍니다.

## 지원되는 메시징 채널

Braze Pilot은 현재 [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about)를 지원하며, 이는 앱에서 나타나며 사용자가 적극적으로 참여하는 동안 적시에 메시지를 전달합니다.

![MovieCanon 앱의 인앱 메시지 "MovieCanon을 즐기고 계신가요?" 친구를 추천하세요!" 이메일 주소를 입력하여 추천을 보낼 수 있는 옵션이 있습니다.]({% image_buster /assets/img/braze_pilot/moviecanon_iam.png %}){:style="max-width:40%"}