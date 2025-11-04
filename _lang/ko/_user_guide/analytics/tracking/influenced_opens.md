---
nav_title: 영향받은 열람 수
article_title: 영향받은 열람 수
page_order: 7
page_type: reference
description: "이 참조 문서에서는 영향받은 열람과 이를 추적하여 푸시 캠페인에 대한 보다 자세한 정보를 제공하는 방법에 대해 설명합니다."
channel: push

---

# 영향을 받은 열기

> 사용자가 푸시 알림을 선택해 앱으로 전송되면 Braze는 이를 직접 실행한 것으로 기록합니다. 사용자가 알림을 선택하지 않았지만 푸시 알림의 영향을 받을 수 있는 경우, Braze는 해당 알림을 영향을 받은 열람으로 기록합니다. 이를 통해 푸시 캠페인의 효과에 대한 보다 풍부한 수준의 세부 정보를 얻을 수 있습니다.

## 작동 방식

기본적으로 영향 받은 열기는 알림을 선택하지 않고 알림을 받은 후 앱을 연 사용자 수를 측정합니다. 알림을 앱 열기와 직접 연결하는 작업이 없으므로 사용자가 푸시 알림을 받은 후 30분 이내에 앱을 열거나 해당 사용자의 마지막 세션 이후 평균 시간의 절반 미만이면 영향받은 열기가 기록됩니다.

예를 들어 앱 사용자에게 푸시 알림을 보낸다고 가정해 보겠습니다. 일반적으로 하루에 30번 앱을 여는 사용자가 푸시를 받은 후 6시간 후에 앱을 여는 경우, 푸시가 열람에 영향을 미쳤다고 인정받지 못합니다. 그러나 일반적으로 한 달에 한 번 앱을 사용하는 사용자가 푸시를 받은 후 6시간 후에 앱을 열면 영향받은 열람으로 집계될 가능성이 훨씬 더 높습니다. 

이는 푸시 캠페인의 전환 이벤트로 앱 열기를 설정하는 것과는 다릅니다. 전환의 경우, 전환 창 내의 모든 열람은 캠페인으로 어트리뷰션됩니다. 영향받은 열람은 개별 사용자의 행동에 따라 시간 창과 어트리뷰션 크레딧을 설정합니다.

## 캠페인의 영향력 있는 열람 보기

영향받은 오픈은 캠페인의 직접 오픈에 추가되어 총 오픈 수를 제공합니다. 푸시 캠페인의 **캠페인 애널리틱스** 페이지에 표시됩니다. 총 열람 수와 직접 열람 수는 메시지 실적 및 **기록 실적** 섹션에 표시됩니다. 영향받은 열람은 두 측정값 간의 차이입니다.

![Influenced opens statistics on the Campaign Details page for a campaign]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

For more information on tracking opens, check out the conversion tracking section of our [best practices for push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

