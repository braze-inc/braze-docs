---
nav_title: 가격 인하 알림
article_title: 가격 인하 알림
page_order: 3
alias: "/price_drop_notifications/"
description: "이 참조 문서에서는 Braze 카탈로그에서 가격 하락 알림을 생성하는 방법을 설명합니다."
---

# 가격 하락 알림

> This page covers how price drop notifications work and how you can set up and use them. Braze 카탈로그와 캔버스를 통해 가격 인하 알림을 조합하면, 고객에게 상품의 가격이 하락했음을 알릴 수 있습니다.

## How it works

사용자가 항목에 대한 커스텀 이벤트를 트리거하면 해당 항목의 가격 하락 알림을 자동으로 가입합니다. 항목의 가격이 재고 규칙(예: 50% 이상의 하락)을 충족하면 모든 구독자는 캠페인 또는 캔버스를 통해 알림을 받을 수 있습니다. 그러나 알림을 선택한 사용자만 알림을 받게 됩니다. 

## 가격 인하 알림을 위한 커스텀 이벤트 설정

구독 이벤트로 사용할 커스텀 이벤트를 설정합니다. 예를 들어 `product_clicked` 이벤트와 같은 이벤트입니다. 이 이벤트에는 항목 ID(카탈로그 항목 ID) 속성이 포함되어야 합니다. 카탈로그 이름을 포함하는 것을 권장하지만, 필수는 아닙니다. 가격 필드의 이름을 제공해야 하며, 이는 숫자 데이터 유형이어야 합니다. 

You can create a price drop subscription for a user and a catalog item when the following occurs:

- 사용자가 선택한 커스텀 이벤트가 수행됩니다.
- 커스텀 이벤트에는 `type` 속성이 있으며, `price_drop`를 포함합니다 (`type`는 배열이어야 합니다)

To set both price-drop and back-in-stock notifications in the same event, you can use the `type` property, which must be an array. 항목의 가격 변경이 가격 규칙을 충족하면 해당 항목에 구독한 모든 사용자(구독 이벤트를 수행한 사용자)를 조회하고 캠페인 또는 캔버스를 트리거하는 데 사용할 수 있는 Braze 커스텀 이벤트를 보냅니다. 

이벤트 속성은 사용자와 함께 전송되므로, 캠페인이나 캔버스에 항목 세부정보를 템플릿으로 삽입할 수 있습니다.

## 가격 인하 알림 설정

다음 단계를 따라 특정 카탈로그에서 가격 하락 알림을 설정하세요.

1. 카탈로그로 이동하여 **설정** 탭을 선택하십시오.
2. **가격 인하** 토글을 선택하십시오.
3. 전역 카탈로그 설정이 구성되지 않은 경우, 알림을 트리거하는 데 사용될 커스텀 이벤트 및 속성을 설정하라는 메시지가 표시됩니다. <br><br> ![Catalog settings drawer.]({% image_buster /assets/img/catalog_settings_drawer.png %}){: style="max-width:70%;"}

| 필드 | 설명 |
| --- | --- |
| **대체 카탈로그** | 구독에 사용되는 카탈로그는 커스텀 이벤트에 `catalog_name` 속성이 없는 경우입니다. |
| **구독을 위한 커스텀 이벤트** | 카탈로그 알림을 위해 사용자를 구독시키는 데 사용되는 커스텀 이벤트입니다. 이 이벤트가 발생하면 이벤트를 수행한 사용자가 구독됩니다. |
| **구독 취소를 위한 사용자 지정 이벤트** | 알림에서 사용자를 탈퇴시키는 데 사용되는 커스텀 이벤트입니다. This event is optional. If the user doesn't perform this event, they'll be unsubscribed after 90 days or when the price drop event triggers, whichever occurs first. |
| **항목 ID 등록정보** | 위의 커스텀 이벤트에서 구독 또는 구독 취소 항목을 결정하는 데 사용되는 속성입니다. 이 속성은 커스텀 이벤트에 있는 항목 ID를 포함해야 합니다. 커스텀 이벤트에는 이 항목이 속한 카탈로그를 지정하는 `catalog_name` 속성이 포함되어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

다음은 예시 커스텀 이벤트입니다:

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
                "type": ["price_drop", "back_in_stock"]
            }
        }
    ]
}
```

{: start="4"}
4\. **저장**을 선택하고, 알림 규칙을 설정하기 위해 다음 섹션으로 계속 진행합니다.

### 알림 규칙 설정

1. 카탈로그의 **설정** 페이지로 이동합니다. 
2. **알림 규칙**에 대해 다음 옵션 중에서 선택합니다:<br>

    - **모든 구독 사용자에게 알림:** 상품의 가격이 하락할 때 대기 중인 모든 고객에게 알림을 보냅니다.
    - **알림 한도 설정:** 설정한 알림 주기에 따라 지정된 수의 고객에게 알립니다. Braze는 알림을 받을 고객 수를 지정된 수만큼 순차적으로 알립니다. 더 이상 알릴 고객이 없거나, 해당 품목의 가격이 다시 오를 때까지 알림을 보냅니다. 알림 속도는 분당 10,000명의 사용자에게 알림을 보낼 수 없습니다.<br>

2. 카탈로그에서 **가격 필드를 설정하십시오**. 이것은 항목의 가격을 결정하는 데 사용될 카탈로그 필드입니다. 숫자 형식이어야 합니다.
3. **가격 인하 규칙**을 설정하세요. 이것은 알림을 보내야 하는지 여부를 결정하는 데 사용되는 논리입니다. A price drop can be configured as a percentage price change or by the change in value for the price field.
4. **저장 설정**을 선택합니다.

![카탈로그 설정에 가격 하락 기능이 켜져 있습니다. The price drop rule is a change of three percent to the original price.]({% image_buster /assets/img/price_drop_notifications.png %})

{% alert important %}
이 설정의 알림 규칙은 캔버스 알림 설정(예: 방해금지 시간)을 대체하지 않습니다.
{% endalert %}

## Using price drop notifications in a Canvas

After setting up the price drop notifications in a catalog, follow these steps to use these notifications for a Canvas.

1. 액션 기반 캔버스를 설정합니다.
2. 트리거로 **가격 인하 이벤트 수행**을 선택하십시오.
3. 카탈로그 이름을 선택하여 가격 하락 알림을 받으세요.
4. 계속해서 [캔버스를 설정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)하세요.

이제 고객님께서는 상품의 가격이 하락할 때 알림을 받게 됩니다.

### Liquid 사용

가격이 하락한 카탈로그 항목에 대한 세부 정보를 템플릿화하려면 `canvas_entry_properties` Liquid 태그를 사용하여 `item_id`에 액세스할 수 있습니다. 

Using {%raw%}``{{canvas_entry_properties.${catalog_update}.item_id}}``{%endraw%} will return the ID of the item that dropped in price. {%raw%}``{{canvas_entry_properties.${catalog_update}.previous_value}}``{%endraw%} will return the price value of the item before the update, and {%raw%}``{{canvas_entry_properties.${catalog_update}.new_value}}``{%endraw%} will return the new price value after the update. 

이 Liquid 태그 {%raw%}``{% catalog_items <name_of_your_catalog> {{canvas_entry_properties.${catalog_update}.item_id}} %}}``{%endraw%}를 메시지 상단에 사용한 다음, {%raw%}`{{items[0].<field_name>}}`{%endraw%}를 사용하여 메시지 전체에서 해당 항목에 대한 데이터를 액세스하세요.

## 고려사항

- 사용자는 90일 동안 구독됩니다. 항목의 가격이 90일 이내에 떨어지지 않으면 사용자는 구독에서 제거됩니다.
- **구독한 모든 사용자에게 알림** 규칙을 사용할 때, Braze는 10분 동안 100,000명의 사용자에게 알림을 보냅니다.
- Braze will process 10 requests to update catalog items per minute. Update endpoints allow for 50 item updates per request, supporting up to 500 item updates per minute that can trigger back-in-stock notifications

