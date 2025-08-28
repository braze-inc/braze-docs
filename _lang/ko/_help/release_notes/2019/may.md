---
nav_title: 5월
page_order: 8
noindex: true
page_type: update
description: "이 문서에는 2019년 5월의 릴리스 노트가 포함되어 있습니다."
---

# 2019년 5월

## 콘텐츠 카드

콘텐츠 카드는 고객의 앱 및 웹 경험 내에 표시되는 영구 콘텐츠입니다.

콘텐츠 카드를 사용하면 고객의 경험을 방해하지 않고도 고객이 즐겨 사용하는 앱 내에서 바로 고도로 타겟팅된 풍부한 콘텐츠의 동적 스트림을 고객에게 보낼 수 있습니다. 또는 콘텐츠 카드를 이메일이나 푸시 알림과 같은 다른 채널과 페어링하여 일관된 마케팅 전략을 사용할 수 있습니다.

![콘텐츠 카드 피드]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

또한 콘텐츠 카드는 카드 고정, 카드 방출, API 기반 전달, 커스텀 카드 만료 시간, 카드 분석 등 더욱 개인화된 기능을 지원합니다.

알림 센터, 홈페이지 피드, 프로모션 피드를 만드는 데 사용할 수 있습니다.

지원되는 Braze SDK 버전으로 업데이트해야 합니다:
- iOS: 3.8.0 이상
- Android: 2.6.0 이상
- 웹: 2.2.0 이상

[여기에서 콘텐츠 카드에 대해 자세히 알아보세요!]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)

{% alert update %}
커런츠용 콘텐츠 카드와 콘텐츠 카드용 API 설명서는 이번 주 후반에 출시될 예정입니다. 기대해 주세요!
{% endalert %}

## Roku 플랫폼 추가

Braze의 기능에 새로운 채널이 추가되었습니다! 새로운 채널로 확장함으로써 고객은 시청 행동을 이해하여 데이터를 강화하거나 모든 관련 채널에서 소비자에게 의미 있는 경험을 제공할 수 있습니다.

이제 데이터 강화 및 커스텀 이벤트 추적 기술을 위해 [Roku 기기에서 데이터를 검색]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku)할 수 있습니다.

## 캔버스 또는 캠페인 업데이트에 대한 알림 기본 설정

이 [새로운 알림]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences)은 캠페인이나 캔버스가 활성화, 업데이트, 재활성화 또는 비활성화되면 이메일을 통해 알려줍니다. Braze 계정의 **알림 환경설정에서** 이 기능을 활성화하세요.

## Jampp 기술 파트너 문서

Jampp는 모바일 고객을 확보하고 리타겟팅하기 위한 퍼포먼스 마케팅 플랫폼입니다. 행동 데이터와 예측 및 프로그래매틱 기술을 결합하여 소비자가 처음 구매하거나 더 자주 구매하도록 유도하는 개인 맞춤형 관련성 광고를 표시함으로써 광고주에게 수익을 창출합니다.

Braze 고객은 이벤트를 Jampp로 스트리밍하도록 Braze 웹훅 채널을 구성하여 [Jampp와 통합]({{site.baseurl}}/partners/jampp/)할 수 있습니다. 그 결과, 고객은 모바일 광고 생태계 내에서 Jampp를 통해 리타겟팅 이니셔티브에 더 풍부한 데이터 세트를 추가할 수 있습니다.

## 인앱 메시지용 플랫폼 선택기

캠페인 제작 과정에서 이 단계를 강조하는 플랫폼 선택 기능을 통해 인앱 메시지가 전달될 위치와 플랫폼을 쉽게 선택할 수 있습니다.

![플랫폼 선택기]({% image_buster /assets/img/iam_platforms.gif %})

## 이메일용 발송 ID 커런츠 필드

{% alert update %}
`dispatch_id`에 대한 동작은 캔버스와 캠페인 간에 다르며, 이는 Braze가 캔버스 단계(예약 가능한 엔트리 단계 제외)를 "예약된" 경우에도 트리거된 이벤트로 취급하기 때문입니다. 캔버스 및 캠페인의 [`dispatch_id` 동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)에 대해 자세히 알아보세요.

_2019년 8월에 업데이트가 기록되었습니다._
{% endalert %}

커런츠 기능을 지속적으로 개선하기 위해 모든 커넥터 유형에 걸쳐 커런츠 이메일 이벤트에 `dispatch_id` 필드를 추가하고 있습니다.

`dispatch_id`는 Braze 플랫폼에서 전송되는 각 전송 또는 발송에 대해 생성된 고유 ID입니다.

예약 메시지를 받는 모든 고객은 동일한 `dispatch_id`를 받지만, 작업 기반 또는 API 트리거된 메시지를 받는 고객은 메시지당 고유한 `dispatch_id`를 받습니다. `dispatch_id` 필드를 사용하면 어떤 반복 캠페인 인스턴스가 전환을 담당하고 있는지 식별할 수 있으므로 어떤 유형의 캠페인이 비즈니스 목표를 달성하는 데 도움이 되는지에 대한 더 많은 인사이트와 정보를 얻을 수 있습니다.

## '내 것만 표시' 캠페인 정렬 기능

사용자가 캠페인 그리드에서 `Only Show Mine` 확인란을 선택하면 로그인한 사용자가 만든 캠페인만 표시되도록 결과가 필터링됩니다. 또한 사용자는 `created_by_me:true` 을 입력하여 검색창을 사용할 수 있습니다.

또한 캠페인 그리드 사이드바의 크기를 조정할 수 있습니다!

## 별칭으로 사용자 삭제

이제 `users/delete` 엔드포인트를 사용하여 [별칭별로 사용자를 삭제]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request)할 수 있습니다!

## 이메일 클릭 및 열람에 대한 고유한 계산

이제 이메일의 고유 클릭 수와 고유 열람 횟수가 사용자당 7일을 기준으로 캡처되어 표시되며, 해당 7일 기간 내에 각 `dispatch_id`당 1씩 증가합니다.

`dispatch_id`를 사용하면 반복 메시지에 각 메시지의 실제 고유 열람 수 또는 고유 클릭 수를 반영할 수 있습니다. 이제 고객들은 커런츠에서 `dispatch_id`를 통해 이 데이터를 쉽게 찾을 수 있습니다.

이전 고유성 기간이 30일 이상이었기 때문에 Mailjet을 사용하는 모든 사용자도 이 수치가 급증하는 것을 볼 수 있습니다. 이 변경 사항은 3주 전에 알려드렸어야 합니다.  SendGrid 고객은 아무런 차이를 느끼지 못할 것입니다.

업데이트된 용어는 [보고서 메트릭 용어집에서]({{site.baseurl}}/user_guide/data/report_metrics/) 검색할 수 있습니다.

{% alert update %}
`dispatch_id`에 대한 동작은 캔버스와 캠페인 간에 다르며, 이는 Braze가 캔버스 단계(예약 가능한 엔트리 단계 제외)가 "예약된" 경우에도 트리거된 이벤트로 취급하기 때문입니다. [캔버스와 캠페인의 [`dispatch_id` 동작]({{site.baseurl}}/help/help_articles/data/dispatch_id/)에 대해 자세히 알아보세요.

_2019년 8월에 업데이트가 기록되었습니다._
{% endalert %}


## 참여도가 가장 높은 채널

{% alert update %}
[2019년 11월 제품 릴리스부터]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite)'가장 참여도가 높은 채널'은 ['지능형 채널']({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)로 이름이 변경되었습니다.
{% endalert %}

참여도가 가장 높은 채널 필터는 선택한 메시징 채널이 "최고"의 채널인 오디언스 중 일부를 선택합니다. 이 경우 "최고"는 "사용자의 기록을 고려할 때 인게이지먼트 가능성이 가장 높음"을 의미합니다. 이메일, 웹 푸시 또는 모바일 푸시(사용 가능한 모든 모바일 OS 또는 기기 포함)를 채널로 선택할 수 있습니다.

이 새 필터 확인하기: [세분화 필터 라이브러리]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).

