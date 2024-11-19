---
nav_title: 배너 카드 만들기
article_title: 배너 카드 만들기
permalink: "/create_banner_card/"
description: "이 참고 문서에서는 Braze 캠페인을 사용하여 배너 카드를 만들고 전송하는 방법을 설명합니다."
page_type: reference
---

# 배너 카드 만들기

> 이 문서에서는 캠페인을 만들 때 Braze에서 배너 카드를 만드는 방법에 대해 설명합니다.

[콘텐츠 카드와]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) 마찬가지로 배너 카드는 앱이나 웹사이트에 직접 임베드되므로 자연스럽게 느껴지는 경험으로 사용자의 참여를 유도할 수 있습니다. 이메일이나 푸시 알림과 같은 다른 채널의 도달 범위를 확장하면서 사용자를 위한 개인화된 메시지를 빠르고 원활하게 생성할 수 있는 솔루션입니다. 

배너 카드는 다음과 같은 경우에 유용합니다:

- 추천 콘텐츠 강조 표시
- 예정된 이벤트에 대해 사용자에게 알림
- 로열티 프로그램에 대한 업데이트 공유

배너 카드는 사용자가 새 세션을 시작할 때마다 개인화되고 만료되지 않도록 구성할 수 있으므로 참여 전략에 추가할 수 있는 유용한 도구입니다.

{% alert important %}
배너 카드는 현재 얼리 액세스 중입니다. 이 얼리 액세스에 참여하고 싶다면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 전제 조건: 배치 결정

배너 카드를 만들기 전에 앱에서 배너 카드를 표시할 영역을 지정해야 합니다. 이를 배치라고도 합니다. 게재 위치를 생성한 후 배너 카드 캠페인을 만들 때 해당 게재 위치를 선택할 수 있습니다. 이미 배치를 받은 경우 [1단계로](#step-1-create-your-campaign) 건너뛰세요.

게재 위치를 만들려면

1. **설정** > **배너 카드 배치로** 이동합니다.
2. 배너 카드 배치에 이름을 지정합니다.
3. (선택 사항) 이 배너 카드를 배치할 위치를 설명하는 설명을 추가합니다.
4. 고유한 게재 위치 ID를 입력합니다. 통합하는 동안 이 ID를 사용해야 하므로 개발자 팀과 협력하여 이 ID를 정의하세요. 앱 또는 웹사이트와의 연동이 중단될 수 있으므로 실행 후 게재 위치 ID를 수정하지 마세요.
5. **저장**을 선택하십시오.

각 게재 위치는 최대 10개의 캠페인에서 사용할 수 있습니다. 

{% alert important %}
배치 ID는 워크스페이스마다 고유합니다.
{% endalert %}

## 1단계: 캠페인 만들기

배너 카드 배치를 결정했으면 이제 캠페인을 구축할 차례입니다.

1. **메시징** > **캠페인**으로 이동하여 **캠페인 만들기**를 선택합니다.
2. **배너 카드를** 선택합니다.
3. 캠페인의 이름을 명확하고 의미 있는 것으로 정하세요.
4. 필요에 따라 팀과 태그를 추가하세요. 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어 보고서 작성기를 사용할 때 관련 태그를 기준으로 필터링할 수 있습니다.
5. 캠페인과 연결할 [게재 위치를](#prerequisite-determine-placement) 선택합니다. 배너 카드가 앱이나 사이트에 표시되는 위치입니다.
6. 캠페인에 원하는 만큼 이형 상품을 추가하고 이름을 지정하세요. 추가된 각 변형에 대해 서로 다른 메시지 유형과 레이아웃을 선택할 수 있습니다. 변형에 대한 자세한 내용은 [다변량 및 A/B 테스트를]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 참조하세요.

## 2단계: 배너 카드 작성

메시지 콘텐츠의 세부 정보를 수정하려면 다음과 같이 하세요:

1. **메시지 수정을** 선택합니다. 작곡가가 열립니다.
2. 메시지에 맞는 행 스타일을 선택합니다. 행을 캔버스 영역으로 끌어다 놓습니다.
3. 블록을 행에 끌어다 놓아 메시지를 작성합니다.
4. 메시지 [스타일을](#styles) 정의합니다.

### 스타일

**스타일을** 선택하여 메시지의 모든 블록에 적용할 설정을 조정합니다.

![배너 카드 작성기의 스타일 패널]({% image_buster /assets/img/banner_cards/banner_card_styles.png %})

여기에서 배너 카드에 배경 속성, 테두리 설정 및 기본값과 같은 사용자 지정 스타일을 제공할 수 있습니다. 여기에 적용된 스타일은 특정 블록 또는 행에 대해 재정의할 수 있습니다. 스타일을 재정의하려면 특정 블록 또는 행을 선택하여 해당 속성을 보고 변경합니다.

### 클릭 시 동작

고객이 배너 카드의 링크를 클릭하면 앱으로 더 깊이 이동하거나 다른 웹페이지로 리디렉션할 수 있습니다.

사용자 지정 속성 또는 사용자 지정 이벤트를 기록하도록 선택할 수도 있습니다. 이렇게 하면 고객이 배너 카드를 클릭할 때 고객 프로필이 사용자 지정 데이터로 업데이트됩니다.

## 3단계: 나머지 캠페인 구축

다음으로, 나머지 캠페인을 구축하십시오. 배너 카드를 제작하는 데 도구를 가장 잘 활용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

### 캠페인 기간 선택

배너 카드 캠페인의 시작 날짜와 시간을 선택합니다. 

기본적으로 배너 카드는 무기한으로 지속됩니다. 원하는 경우 **종료 시간을** 선택하여 종료 날짜와 시간을 지정합니다.

### 타겟팅할 사용자 선택

다음으로 세그먼트 또는 필터를 선택하여 사용자를 타겟팅하여 오디언스의 범위를 좁힙니다. 대략적인 세그먼트 인구가 현재 어떤 모습인지에 대한 스냅샷이 자동으로 제공됩니다. 정확한 세그먼트 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점에 유의하세요.

### 전환 이벤트 선택

Braze를 사용하면 사용자가 캠페인을 수신한 후 특정 액션과 전환 이벤트를 얼마나 자주 수행하는지 추적할 수 있습니다. 사용자가 지정된 작업을 수행하면 최대 30일 동안 전환이 카운트되도록 허용할 수 있습니다.

## 4단계: 테스트 및 배포

캠페인을 구축한 후에는 캠페인을 테스트하고 검토하여 캠페인이 예상대로 작동하는지 확인합니다. 그러면 배너 카드 캠페인을 시작할 준비가 된 것입니다!

## 알아두어야 할 사항

### 배너 카드 만료

기본적으로 배너 카드에는 만료일이 없지만, 선택적으로 종료일을 추가할 수 있습니다.

### 배치 관리

배치는 워크스페이스마다 고유하며, 각 배치는 최대 10개 캠페인에서 사용할 수 있습니다.

배치 ID는 워크스페이스에 고유해야 하며 실행 후 편집해서는 안 됩니다. 통합하는 동안 이 ID를 사용해야 하므로 개발자 팀과 협력하여 이 ID를 정의하세요. 

### 분석

다음 표에서는 주요 배너 카드 지표를 정의합니다.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href='https://braze.com/docs/user_guide/data_and_analytics/report_metrics#total-impressions'>총 노출 수</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-impressions'>고유 노출 수</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#total-clicks'>총 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-clicks'>고유 클릭 수</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event'>주요 전환</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}<ul><li>{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</li><li>{% multi_lang_include metrics.md metric='Conversion Rate' %}</li></ul></td>
        </tr>
    </tbody>
</table>

메트릭, 정의 및 계산에 대한 전체 목록은 [보고서 메트릭 용어집을]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/) 참조하세요.