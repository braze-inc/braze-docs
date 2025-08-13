---
nav_title: 재고 부족 알림
article_title: 품절 알림 설정
page_order: 2
description: "Learn how to set up back-in-stock notifications using your catalog and custom events, so you can automatically subscribe customers to receive notifications when an item is back in stock."
---

# 품절 알림

> Learn how to set up back-in-stock notifications using your catalog and custom events, so you can automatically subscribe customers to receive notifications when an item is back in stock. Keep in mind, this only applies to users who've already opted in to notifications.

## How it works

You can set up a custom event to use as a subscription event, such as a `product_clicked` event. 이 이벤트에는 항목 ID(카탈로그 항목 ID) 속성이 포함되어야 합니다. 카탈로그 이름을 포함하는 것을 권장하지만 필수는 아닙니다. 또한 숫자 데이터 유형이어야 하는 재고 수량 필드의 이름도 입력합니다. 

카탈로그 품목의 재고가 0이어야 사용자가 성공적으로 구독할 수 있습니다. When an item has an inventory quantity greater than zero, Braze will look up all users subscribed to that item and send a custom event that you can use to trigger a campaign or Canvas.

이벤트 속성은 사용자와 함께 전송되므로 전송하는 캠페인이나 캔버스에 항목 세부 정보를 템플릿으로 만들 수 있습니다.

## 품절 알림 설정

특정 카탈로그에서 품절 알림을 설정하려면 다음 단계를 따르세요.

1. 카탈로그로 이동하여 **설정** 탭을 선택하십시오.
2. **재고 있음** 토글을 선택합니다.
3. 글로벌 재입고 설정이 구성되지 않은 경우 재입고 알림을 트리거하는 데 사용할 사용자 지정 이벤트 및 속성을 설정하라는 메시지가 표시됩니다:
    <br> ![Catalog settings drawer.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}
    - **대체 카탈로그** 커스텀 이벤트에 `catalog_name` 속성이 없는 경우 이월 구독에 사용할 카탈로그입니다.
    - **구독을 위한 사용자 지정 이벤트는** 사용자에게 품절 알림을 구독하도록 설정하는 데 사용되는 Braze 사용자 지정 이벤트입니다. 이 이벤트가 발생하면 이벤트를 수행한 사용자가 구독하게 됩니다.
    - **구독 취소를 위한 사용자 지정 이벤트는** 재고가 없는 알림에서 사용자의 구독을 취소하는 데 사용되는 Braze 사용자 지정 이벤트입니다. This event is optional. If the user doesn't perform this event, they'll be unsubscribed after 90 days or when the back-in-stock event triggers, whichever occurs first.
    - **품목 ID 이벤트 속성**은 위 커스텀 이벤트의 속성으로, 이월 구독 또는 구독 취소를 위한 품목을 결정하는 데 사용됩니다. This property on the custom event should contain an item ID (`id`) that is present in a catalog. The item ID must be sent as a string so that it matches the `id` data type stored in the target catalog. The custom event should also contain a `catalog_name` property, to specify which catalog this item is in.
    
    - 샘플 커스텀 이벤트는 다음과 같습니다
    ```json
    {
        "events": [
            {
                "external_id": "<external_id>",
                "name": "subscription",
                "time": "2024-04-15T19:22:28Z",
                "properties": {
                    "id": "shirt-xl",
                    "catalog_name": "on_sale_products",
                    "type": ["back_in_stock"]
                }
            }
        ]
    }
    ```
{% alert note %}
재고 소진 및 가격 인하 트리거는 동일한 이벤트를 사용하여 사용자를 알림에 가입시키므로 `type` 속성을 사용하여 동일한 이벤트에서 가격 인하 및 재고 소진 알림을 모두 설정할 수 있습니다. `type` 속성은 배열이어야 합니다.
{% endalert %}

{: start="4"}
4\. **저장**을 선택하고 카탈로그의 **설정** 페이지로 계속 진행하십시오.
5\. 알림 규칙을 설정하세요. 두 가지 옵션이 있습니다:
    - **구독한 모든 사용자에게 알림은** 상품이 재입고되면 대기 중인 모든 고객에게 알림을 보냅니다.
    - **알림 제한을 설정하면** 구성된 알림 기간에 따라 지정된 수의 고객에게 알림이 전송됩니다. Braze는 더 이상 알림을 받을 고객이 없거나 상품이 품절될 때까지 지정된 수의 고객에게 순차적으로 알림을 보냅니다. 알림 속도는 분당 10,000명의 사용자에게 알림을 보낼 수 없습니다.
6\. **카탈로그에서 인벤토리 필드를** 설정합니다. 이 카탈로그 필드는 품목의 품절 여부를 확인하는 데 사용됩니다. 필드는 숫자 유형이어야 합니다.
7\. **저장 설정**을 선택합니다.

![카탈로그 설정에서 이월 재고 기능이 켜져 있음을 표시합니다. The notification rules are to notify a thousand users every ten minutes.]({% image_buster /assets/img/back_in_stock_settings.png %})

{% alert important %}
이 설정의 알림 규칙은 캔버스 알림 설정(예: 방해금지 시간)을 대체하지 않습니다.
{% endalert %}

## 캔버스에서 재고 부족 알림 사용

카탈로그에서 이월 재고 기능을 설정한 후 다음 단계에 따라 캔버스에서 사용하세요.

1. 액션 기반 캔버스를 설정합니다.
2. 트리거로 **다시 입고**를 선택합니다.
3. 품절 알림이 표시된 카탈로그의 이름을 선택합니다.
4. 계속해서 [캔버스를 설정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)하세요.

이제 상품이 재입고되면 고객에게 알림을 받을 수 있습니다.

### Liquid 사용

재고가 있는 카탈로그 품목에 대한 세부 정보를 템플릿으로 작성하려면 `canvas_entry_properties` Liquid 태그를 사용하여 `item_id`에 액세스할 수 있습니다. 

{%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%}을 사용하면 재고로 돌아온 아이템의 ID를 반환합니다. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%}은 업데이트 전 아이템의 인벤토리 값을 반환하고 {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%}은 업데이트 후 새 인벤토리 값을 반환합니다.

Use this Liquid tag {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}``{%endraw%} at the top of your message, then use {%raw%}``{{ items[0].<field_name> }}``{%endraw%} to access data about that item throughout the message.

## 고려사항

- 사용자는 90일 동안만 구독할 수 있습니다. 90일 이내에 품목이 재입고되지 않으면 사용자의 구독이 취소됩니다.
- **구독한 모든 사용자**에게 알림 규칙을 사용하는 경우 Braze는 10분에 걸쳐 100,000명에게 알림을 보냅니다.
- Braze는 1분 동안 최대 10개의 아이템 업데이트를 처리합니다. 1분 동안 11개의 품목을 업데이트하는 경우 처음 10개 품목만 재고 부족 알림을 트리거할 수 있습니다.

