---
nav_title: 콘텐츠 카드
article_title: 캔버스의 콘텐츠 카드
page_order: 1
page_type: reference
description: "이 참조 문서에서는 캔버스 내에서 메시징 채널로 콘텐츠 카드를 사용하는 것과 관련된 기능과 뉘앙스를 설명합니다."
tool: Canvas
channel: content cards

---

# 캔버스의 콘텐츠 카드

> 콘텐츠 카드는 고객의 캔버스 여정의 일부로 보낼 수 있습니다. 이 문서에서는 캔버스 내에서 메시징 채널로서 콘텐츠 카드를 사용하는 것과 관련된 기능 및 뉘앙스를 설명합니다.

다른 캔버스 메시징 채널과 마찬가지로, 콘텐츠 카드는 사용자가 해당 단계에 대해 지정된 오디언스 및 타겟팅 기준을 충족할 때 사용자의 기기로 전송됩니다. 콘텐츠 카드가 전송된 후, 각 해당 사용자의 피드가 새로 고쳐질 때 다음 번에 카드 피드에서 사용할 수 있습니다.

![Content Cards selected as the messaging channel for a Message step.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Two options that will change how the Content Card step will interact with Canvas are its [expiration](#content-card-expiration) and [removal](#removal).

## 콘텐츠 카드 만료 {#content-card-expiration}

새 콘텐츠 카드를 작성할 때 발송 시간에 따라 사용자 피드에서 만료되는 시점을 선택할 수 있습니다. 콘텐츠 카드의 만료에 대한 카운트다운은 사용자가 카드가 전송된 캔버스의 메시지 단계에 도달할 때 시작됩니다. 카드는 이 시점부터 만료될 때까지 사용자의 피드에서 활성화됩니다. 카드는 사용자의 피드에 최대 30일 동안 존재할 수 있습니다. 

![Expiration settings for a Content Card for a Message step that will be removed after three hours in a user's feed.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Types of expiration

카드가 사용자 피드에서 사라지는 시점을 설정하는 두 가지 방법이 있습니다: 상대 날짜 또는 절대 날짜.

#### 상대 날짜

When you choose a relative date, like "Remove sent cards after 5 days in a user's feed", you can set an expiration date of up to 30 days.

#### 절대 날짜

절대 날짜를 선택할 때, 예를 들어 "2023년 12월 1일 오후 4시에 보낸 카드를 제거"와 같은 경우, 약간의 미묘한 차이가 있습니다.

비록 만료 기간을 30일 이상으로 지정할 수 있지만, 콘텐츠 카드는 사용자의 피드에 최대 30일 동안 존재합니다. 30일 이상의 기간을 지정하면 메시지 단계를 트리거하기 전에 지연을 고려할 수 있지만, 사용자의 피드에서 카드의 최대 수명을 연장하지는 않습니다.

캔버스를 출시한 후 30일 이상 경과한 만료일을 설정할 때는 주의하세요. 사용자가 지정된 만료일보다 30일 이상 전에 메시지 단계에 도달하면 카드는 발송되지 않습니다.

### 만료 동작

콘텐츠 카드는 사용자가 캔버스 여정의 다음 단계로 진행하더라도 만료 날짜에 도달할 때까지 사용자의 피드에 계속 표시됩니다. 콘텐츠 카드가 캔버스의 다음 단계가 전달될 때 라이브 상태가 되지 않도록 하려면, 만료 기간이 후속 단계의 지연 시간보다 짧은지 확인하세요.

콘텐츠 카드가 만료되면 사용자가 아직 보지 않았더라도 다음 새로고침 시 자동으로 피드에서 제거됩니다.

## Content Card removal {#removal}

Content Cards can be removed when users complete a purchase or perform a custom event. You can select one of the following as the removal event: **Perform Custom Event** and **Make Purchase**. Then, select **Add Event**.

!["Remove cards when users complete a purchase or perform a custom event." selected with the trigger to remove cards for users who make a specific purchase for "Bracelet".]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## 보고 및 분석

캔버스에서 콘텐츠 카드 단계를 시작한 후 이 단계를 분석하기 위해 여러 측정기준을 분석할 수 있습니다. 이러한 측정기준에는 발송된 메시지 수, 고유 수신자, 전환율, 총 매출 등이 포함됩니다.

![Analytics for a Message step with the Content Card message performance.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

For more information on the available metrics and their definitions, see our [Report Metrics Glossary]({{site.baseurl}}/user_guide/data/report_metrics/).

## 사용 사례

#### 프로모션 제공

사용자가 특정 프로모션 및 광고에 적합할 때 피드에 카드를 추가합니다. 예를 들어, 사용자가 작업을 수행하거나 구매를 한 후 새로운 제안을 받을 자격이 생기면, 캔버스를 사용하여 다른 메시징 채널 외에도 콘텐츠 카드를 보낼 수 있으므로 다음에 앱을 열 때 제안이 제공됩니다.

#### 푸시 알림 받은편지함

사용자가 푸시 알림을 해제하거나 이메일을 삭제할 때가 있지만, 마음이 바뀔 경우를 대비해 알림을 보내거나 제안을 홍보하고 싶을 때가 있습니다.

캔버스를 사용하여 콘텐츠 카드와 푸시 알림을 모두 보내는 구성 요소를 추가하여 푸시를 통해 전송된 프로모션 메시지와 일치하는 카드의 지속적인 "받은편지함"을 사용자에게 제공할 수 있습니다. 

#### 카테고리별로 여러 피드

사용자가 탐색할 수 있는 다양한 주제 또는 트랜잭션 및 마케팅 피드와 같은 카테고리를 기준으로 콘텐츠 카드를 여러 피드로 분리할 수 있습니다. For more information on creating multiple feeds using key-value pairs, check out our guide for [Customizing Content Card feeds]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).


