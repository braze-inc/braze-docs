---
nav_title: Braze의 Shopify 데이터
article_title: "Braze에서 Shopify 데이터 사용"
description: "이 참조 문서에서는 개인화 및 세분화를 위해 Braze에서 Shopify 데이터를 사용하는 방법을 간략하게 설명합니다."
page_type: partner
search_tag: Partner
alias: "/shopify_data_legacy/"
page_order: 1
---

# Braze의 Shopify 데이터

> 사용자 지정 이벤트에 대한 중첩 개체 지원을 사용하여 Braze Shopify 고객은 중첩된 이벤트 속성의 Liquid 템플릿 변수를 사용할 수 있습니다.

앱 설치가 완료되면 Braze는 자동으로 웹후크 및 ScriptTag를 생성하여 Shopify와 통합합니다. 지원되는 Shopify 이벤트가 Braze 커스텀 이벤트 및 커스텀 속성에 매핑되는 방식에 대한 자세한 내용은 다음 표를 참조하세요.

## 지원되는 Shopify 이벤트

{% tabs %}
{% tab Shopify 이벤트 %}
{% subtabs global %}
{% subtab Product Viewed %}
**이벤트**: `shopify_product_viewed`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 아이템 ID | `{{event_properties.${id}}}` |
| 항목 제목 | `{{event_properties.${title}}}` |
| 아이템 가격 | `{{event_properties.${price}}}` |
| 항목 제공업체 | `{{event_properties.${vendor}}}` |
| 항목 이미지 | `{{event_properties.${images}}}` |


{% endraw %}
{% endsubtab %}


{% subtab Product Clicked %}
**이벤트**: `shopify_product_clicked`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 아이템 ID | `{{event_properties.${id}}}` |
| 항목 제목 | `{{event_properties.${title}}}` |
| 아이템 가격 | `{{event_properties.${price}}}` |
| 항목 제공업체 | `{{event_properties.${vendor}}}` |
| 항목 이미지 | `{{event_properties.${images}}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Cart %}
**이벤트**: `shopify_abandoned_cart`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 장바구니 ID | `{{event_properties.${cart_id}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
{% endraw %}
{% endsubtab %}


{% subtab Abandoned Checkout %}
**이벤트**: `shopify_abandoned_checkout`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 결제 ID | `{{event_properties.${checkout_id}}}` |
| 버려진 장바구니 URL | `{{event_properties.${abandoned_checkout_url}}}` |
| 할인 코드 | `{{event_properties.${discount_code}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 할인 금액 | `{{event_properties.${applied_discount}[0].amount}}` |
| 할인 제목 | `{{event_properties.${applied_discount}[0].title}}` |
| 할인 설명 | `{{event_properties.${applied_discount}[0].description}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Created Order %}


**이벤트**: `shopify_created_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)

{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 태그 | `{{event_properties.${tags}}}` |
| 할인 코드 | `{{event_properties.${discount_codes}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
|Shopify 스토어 | `{{event_properties.${shopify_storefront}}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 참조 사이트 | `{{event_properties.${referring_site}}}` |
| 결제 게이트웨이 이름 | `{{event_properties.${payment_gateway_names}}}` |
| 배송지 주소 1 | `{{event_properties.${shipping_address[0].address1}}}` |
| 배송지 주소 2번 줄 | `{{event_properties.${shipping_address[0].address2}}}` |
| 배송지 주소 도시 | `{{event_properties.${shipping_address[0].city}}}` |
| 배송지 국가 | `{{event_properties.${shipping_address[0].country}}}` |
| 배송지 주소 이름 | `{{event_properties.${shipping_address[0].first_name}}}` |
| 배송지 주소 성 | `{{event_properties.${shipping_address[0].last_name}}}` |
| 배송지 주 | `{{event_properties.${shipping_address[0].province}}}` |
| 배송지 우편번호 | `{{event_properties.${shipping_address[0].zip}}}` |
| 청구지 주소 1 | `{{event_properties.${billing_address[0].address1}}}` |
| 청구지 주소 2번 줄 | `{{event_properties.${billing_address[0].address2}}}` |
| 청구지 주소 도시 | `{{event_properties.${billing_address[0].city}}}` |
| 청구지 주소 국가 | `{{event_properties.${billing_address[0].country}}}` |
| 청구지 주소 이름 | `{{event_properties.${billing_address[0].first_name}}}` |
| 청구지 주소 성 | `{{event_properties.${shipping_address[0].last_name}}}` |
| 청구지 주소 주 | `{{event_properties.${billing_address[0].province}}}` |
| 청구지 주소 우편번호 | `{{event_properties.${billing_address[0].zip}}}` |
{% endraw %}


{% endsubtab %}
{% subtab Purchase %}


**이벤트**: 구매<br>
**유형**: [Braze 구매 이벤트]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}


{% endsubtab %}
{% subtab Paid Order %}
**이벤트**: `shopify_paid_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 태그 | `{{event_properties.${tags}}}` |
| 할인 코드 | `{{event_properties.${discount_codes}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Partially Fulfilled Order %}
**이벤트**: `shopify_partially_fulfilled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 비공개 타임스탬프 | `{{event_properties.${closed_at}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 주문 처리 배송 상태 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillments}[0].status}}` |
| 주문 처리 추적 회사 | `{{event_properties.${fulfillments}[0].tracking_company}}` |
| 주문 처리 추적 번호 | `{{event_properties.${fulfillments}[0].tracking_number}}` |
| 주문 처리 추적 번호 | `{{event_properties.${fulfillments}[0].tracking_numbers}}` | 주문 처리 추적 번호
| 주문 처리 추적 URL | `{{event_properties.${fulfillments}[0].tracking_url}}` |
| 주문 처리 추적 URL | `{{event_properties.${fulfillments}[0].tracking_urls}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| 주문 처리 이름 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| 주문 처리 가격 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| 주문 처리 제품 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| 주문 처리 수량 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| 주문 처리 배송 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| 주문 처리 SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| 주문 처리 제목 | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| 주문 처리 공급업체 | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Fulfilled Order %}
**이벤트**: `shopify_fulfilled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인 상태 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 비공개 타임스탬프 | `{{event_properties.${closed_at}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 주문 처리 배송 상태 | `{{event_properties.${fulfillments}[0].shipment_status}}` |
| 상태 | `{{event_properties.${fulfillments}[0].status}}` |
| 주문 처리 추적 회사 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_company}}` |
| 주문 처리 추적 번호 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_number}}` |
| 주문 처리 추적 번호 | `{{event_properties.${fulfillments}[0].Fulfillment tracking_numbers}}` | 주문 처리 추적 번호
| 주문 처리 추적 URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_url}}` |
| 주문 처리 추적 URL | `{{event_properties.${fulfillments}[0].Fulfillment tracking_urls}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillments}[0].line_items[0].fulfillment_status}}` |
| 주문 처리 이름 | `{{event_properties.${fulfillments}[0].line_items[0].name}}` |
| 주문 처리 가격 | `{{event_properties.${fulfillments}[0].line_items[0].price}}` |
| 주문 처리 제품 ID | `{{event_properties.${fulfillments}[0].line_items[0].product_id}}` |
| 주문 처리 수량 | `{{event_properties.${fulfillments}[0].line_items[0].quantity}}`|
| 주문 처리 배송 | `{{event_properties.${fulfillments}[0].line_items[0].requires_shipping}}` |
| 주문 처리 SKU | `{{event_properties.${fulfillments}[0].line_items[0].sku}}` |
| 주문 처리 제목 | `{{event_properties.${fulfillments}[0].line_items[0].title}}` |
| 주문 처리 공급업체 | `{{event_properties.${fulfillments}[0].line_items[0].vendor` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}


{% subtab Cancelled Order %}
**이벤트**: `shopify_cancelled_order`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 총 가격 | `{{event_properties.${total_price}}}` |
| 총 할인 | `{{event_properties.${total_discounts}}}` |
| 확인됨 | `{{event_properties.${confirmed}}}` |
| 주문 상태 URL | `{{event_properties.${order_status_url}}}` |
| 주문 번호 | `{{event_properties.${order_number}}}` |
| 취소된 타임스탬프 | `{{event_properties.${cancelled_at}}}` |
| 태그 | `{{event_properties.${tags}}}` |
| 할인 코드 | `{{event_properties.${discount_codes}}}` |
| 주문 처리 상태 | `{{event_properties.${fulfillment_status}}}` |
| 주문 처리 | `{{event_properties.${fulfillments}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 주문 처리 상태 | `{{event_properties.${line_items}[0].fulfillment_status}}` |
| 배송 제목 | `{{event_properties.${shipping}[0].title}}` |
| 배송비 | `{{event_properties.${shipping}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}

{% subtab Created Refund %}
**이벤트**: `shopify_created_refund`<br>
**유형**: [커스텀 이벤트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)


{% raw %}
| 변수 | 리퀴드 템플레이트 |
| --- | --- |
| 주문 ID | `{{event_properties.${order_id}}}` |
| 주문 참고 사항 | `{event_properties.${note}}}` |
| 아이템 ID | `{{event_properties.${line_items}[0].product_id}}` |
| 아이템 수량 | `{{event_properties.${line_items}[0].quantity}}` |
| 상품 SKU | `{{event_properties.${line_items}[0].sku}}` |
| 항목 제목 | `{{event_properties.${line_items}[0].title}}` |
| 항목 제공업체 | `{{event_properties.${line_items}[0].vendor}}` |
| 항목 이름 | `{{event_properties.${line_items}[0].name}}` |
| 항목 속성정보 | `{{event_properties.${line_items}[0].properties}}` |
| 아이템 가격 | `{{event_properties.${line_items}[0].price}}` |
| 배리언트 ID | `{{event_properties.${line_items}[0].variant_id}}` |
| 배리언트 제목 | `{{event_properties.${line_items}[0].variant_title}}` |
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab 페이로드 예제 %}
{% subtabs global %}
{% subtab Product Viewed %}
```json
{
 "name": "shopify_product_viewed",
 "properties": {
     "id": 5971657097407,
     "title": "Example T-Shirt",
     "price": 1999,
     "vendor": "Acme",
     "images": [
         "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
     ]
 }
}
```
{% endsubtab %}
{% subtab Product Clicked %}
```json
{
   "name": "shopify_product_clicked",
   "properties": {
       "id": 5971657097407,
       "title": "Example T-Shirt",
       "price": 1999,
       "vendor": "Acme",
       "images": [
           "//cdn.shopify.com/s/files/1/0503/3849/6703/products/green-t-shirt.jpg?v=1603397913"
       ]
   }
}
```
{% endsubtab %}
{% subtab Abandoned Cart %}
```json
{
   "name": "shopify_abandoned_cart",
   "time": "2022-10-14T15:08:31.571Z",
   "properties": {
     "cart_id": "163989958f6b0de13f3b4f702fa5ee0d",
     "line_items": [
       {
         "price": 60,
         "product_id": 7110622675033,
         "properties": null,
         "quantity": 1,
         "sku": null,
         "title": "Spinach Surprise Smoothie - 12 Pack",
         "variant_id": 40094740545625,
         "vendor": "Jennifer's Juice"
       }
     ]
   },
   "braze_id": "63497b3ca3eabd0053380451"
 }

```
{% endsubtab %}
{% subtab Abandoned Checkout %}
```json
{
 "name": "shopify_abandoned_checkout",
 "time": "2020-09-10T18:53:37-04:00",
 "properties": {
   "applied_discount": {
     "amount": "30.00",
     "title": "XYZPromotion",
     "description": "Promotionalitemforblackfriday."
   },
   "discount_code": "30_DOLLARS_OFF",
   "total_price": "398.00",
   "line_items": [
     {
   "price": "199.00",
   "properties": {},       
   "product_id": 632910392,
       "quantity": 1,
       "sku": "IPOD2008PINK",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545625,
       "variant_title": "Pink iPod Nano 8 GB",
       "vendor": "Apple",
     }
   ],
   "abandoned_checkout_url": "https://checkout.local/690933842/checkouts/123123123/recover?key=example-secret-token",
   "checkout_id": "123123123"
 }
}
```
{% endsubtab %}
{% subtab Created Order %}
```json
{
 "name": "shopify_created_order",
 "time": "2020-09-10T18:53:45-04:00",
 "properties": {
   "total_discounts": "5.00",
   "total_price": "403.00",
   "discount_codes": [],
   "line_items": [
     {
       "product_id": 632910392,
       "quantity": 1,
       "sku": "IPOD2008PINK",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545625,
       "variant_title": "Pink iPod Nano 8 GB",
       "vendor": null,
       "name": "IPodNano-8GB",
       "properties": [],
       "price": "199.00"
     },
     {
       "product_id": 632910393,
       "quantity": 1,
       "sku": "IPOD2008SILVER",
       "title": "IPodNano-8GB",
       "variant_id": 40094740545626,
       "variant_title": "Silver iPod Nano 8 GB",
       "vendor": null,
       "name": "IPodNano-8GB",
       "properties": [],
       "price": "199.00"
     }
   ],
   "order_id": 820982911946154500,
   "confirmed": false,
   "order_status_url": "https://apple.myshopify.com/690933842/orders/123456abcd/authenticate?key=abcdefg",
   "order_number": 1234,
   "cancelled_at": "2020-09-10T18:53:45-04:00",
   "shipping": [
     {
       "title": "Standard",
       "price": "10.00"
     },
     {
       "title": "Expedited",
       "price": "25.00"
     }
   ],
   "tags": "heavy"
 }
}
```
{% endsubtab %}
{% subtab Purchase %}
```json
{
 "product_id": 632910392,
 "currency": "USD",
 "price": "199.00",
 "time": "2020-09-10T18:53:45-04:00",
 "quantity": 1,
 "source": "shopify",
 "properties": {
   "name": "IPodNano-8GB",
   "sku": "IPOD2008PINK",
   "variant_id": 40094740545626,
   "variant_title": "Silver iPod Nano 8 GB",
   "vendor": null,
   "properties": []
 }
}
```
{% endsubtab %}
{% subtab Paid Order %}
```json
{
 "name": "shopify_paid_order",
 "time": "2022-05-23T13:52:38-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": null,
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ],
 }
}
```
{% endsubtab %}
{% subtab Partially Fulfilled Order %}
```json
{
 "name": "shopify_partially_fulfilled_order",
 "time": "2022-05-23T14:43:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": null,
   "fulfillment_status": "partial",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "123",
       "tracking_numbers": [
         "123"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "properties": [],
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% subtab Fulfilled Order %}
```json
{
 "name": "shopify_fulfilled_order",
 "time": "2022-05-23T14:44:34-04:00",
 "properties": {
   "order_id": 4444668657855,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143032066239,
       "sku": null,
       "title": "Dark Denim Top",
  "variant_id": 40094740549876,
       "variant_title": "Small Dark Denim Top",


       "vendor": "partners-demo",
       "name": "Dark Denim Top",
       "properties": [],
       "price": "60.00",
       "fulfillment_status": "fulfilled"
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "130.66",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1093,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": null,
   "tags": "",
   "closed_at": "2022-05-23T14:44:34-04:00",
   "fulfillment_status": "fulfilled",
   "fulfillments": [
     {
       "shipment_status": null,
       "status": "success",
       "tracking_company": "Other",
       "tracking_number": "456",
       "tracking_numbers": [
         "456"
       ],
       "tracking_url": "https://braze.com",
       "tracking_urls": [
         "https://braze.com"
       ],
       "line_items": [
         {
           "fulfillment_status": "fulfilled",
           "name": "Dark Denim Top",
           "price": "60.00",
           "product_id": 6143032066239,
           "quantity": 1,
           "requires_shipping": true,
           "sku": null,
           "title": "Dark Denim Top",
           "variant_id": 40094740549876,
           "variant_title": "Small Dark Denim Top",
           "vendor": "partners-demo"
         }
       ]
     }
   ]
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Cancelled Order %}
```json
{
 "name": "shopify_cancelled_order",
 "time": "2022-05-23T14:40:52-04:00",
 "properties": {
   "order_id": 4444596371647,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "name": "LED High Tops",
       "properties": [],
       "price": "80.00",
       "fulfillment_status": null
     }
   ],
   "shipping": [
     {
       "title": "Standard",
       "price": "0.00"
     }
   ],
   "total_price": "141.54",
   "confirmed": true,
   "total_discounts": "0.00",
   "discount_codes": [],
   "order_number": 1092,
   "order_status_url": "https://test-store.myshopify.com/",
   "cancelled_at": "2022-05-23T14:40:52-04:00",
   "tags": "",
   "closed_at": "2022-05-23T14:40:51-04:00",
   "fulfillment_status": null,
   "fulfillments": []
 },
 "braze_id": "123abc123abc"
}
```
{% endsubtab %}
{% subtab Created Refund %}
```json
{
 "name": "shopify_created_refund",
 "time": "2022-05-23T14:40:50-04:00",
 "properties": {
   "order_id": 4444596371647,
   "note": null,
   "line_items": [
     {
       "quantity": 1,
       "product_id": 6143033344191,
       "sku": null,
       "title": "LED High Tops",
       "variant_id": 40094740549876,
       "variant_title": "",
       "vendor": "partners-demo",
       "properties": [],
       "price": "80.00"
     },
     {
       "quantity": 1,
       "product_id": 6143032852671,
       "sku": null,
       "title": "Chequered Red Shirt",
       "variant_id": 40094796619876,
       "variant_title": "",
       "vendor": "partners-demo",
       "properties": [],
       "price": "50.00"
     }
   ]
 },
 "braze_id": "abc123abc123"
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 지원되는 Shopify 사용자 지정 속성
{% tabs local %}
{% tab Shopify 사용자 지정 속성 %}
| 속성 이름 | 설명 | 설명
| --- | --- |
| `shopify_tags` | 쉼표로 구분된 값의 문자열 형식으로 상점 소유자가 고객에게 첨부한 태그입니다. 고객은 최대 250개의 태그를 보유할 수 있습니다. 각 태그에는 최대 255자까지 입력할 수 있습니다. |
| `shopify_total_spent` | 고객이 주문 내역에서 지출한 총 금액입니다. |
| `shopify_order_count` | 이 고객과 관련된 주문 수입니다. 테스트 및 보관된 주문은 계산되지 않습니다. |
| `shopify_last_order_id` | 고객의 마지막 주문 ID입니다. |
| `shopify_last_order_name` | 고객의 마지막 주문 이름입니다. 이는 주문 리소스의 `name` 필드와 직접 관련이 있습니다. |
| `shopify_zipcode` | 기본 주소의 고객 우편번호입니다. |
| `shopify_province` | 기본 주소에서 고객의 시/도입니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 유동적인 개인화

Shopify 커스텀 속성에 대한 Liquid 개인화를 추가하려면 **\+ 개인화**를 선택합니다. 그런 다음 **사용자 지정 속성을** 개인화 유형으로 선택합니다.

!['속성' 드롭다운이 확장된 '개인화 추가' 섹션.]({% image_buster /assets/img/Shopify/add_personalization_2.png %}){: style="max-width:40%;"}

커스텀 속성을 선택한 후 기본값을 입력하고 Liquid 스니펫을 메시지에 복사합니다.

![리퀴드 스니펫을 메시지에 붙여넣기]({% image_buster /assets/img/Shopify/copy_liquid_snippet.png %})

#### 페이로드 예시

```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```

{% endtab %}
{% tab 페이로드 예제 %}
{% subtabs %}
{% subtab Shopify Tags %}
```json
{
  "attributes": [
    {
      "shopify_tags": "VIP_customer",
      "shopify_total_spent": "60.00",
      "shopify_order_count": "3",
      "shopify_last_order_id": "1234567",
      "shopify_last_order_name": "test_order",
      "shopify_zipcode": "10001",
      "shopify_province": "null"
    }
  ]
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 지원되는 Shopify 표준 속성

- 이메일
- 이름
- 성
- 전화
- 도시
- 국가

{% alert note %}
Braze는 기존 사용자 프로필과 데이터에 차이가 있는 경우에만 지원되는 Shopify 사용자 지정 속성 및 Braze 표준 속성을 업데이트합니다. 예를 들어, 인바운드 Shopify 데이터에 Bob이라는 이름이 포함되어 있고 Braze 고객 프로필에 Bob이 이미 이름으로 존재하는 경우 Braze는 업데이트를 트리거하지 않으며 데이터 포인트가 청구되지 않습니다.
{% endalert %}

## 세분화

세분화의 모든 [기존 사용자 지정 필터를]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) 사용하여 Shopify의 이벤트를 필터링할 수 있습니다. 

![사용자 지정 이벤트 "shopify_checkouts_abandon"에 대한 필터가 강조 표시된 Shopify_Test 세그먼트의 세그먼트 세부 정보 페이지입니다.][12]{: style="max-width:80%;"}

In addition, you can use the breadth of purchase filter in Braze to create segments of users based on:
- 첫 구매/마지막 구매
- 특정 앱의 첫 구매/마지막 구매
- 지난 30일 이내에 구매한 적이 있는 제품
- 구매 횟수

![2020년 10월 17일 이후에 처음 구매한 사용자를 위한 세분화 필터입니다.][13]

![세분화 필터로 특정 제품 ID를 검색합니다.][14]

{% alert note %}
사용자 지정 이벤트 속성으로 세분화하려는 경우, 고객 성공 관리자 또는 Braze [지원팀과]({{site.baseurl}}/braze_support/) 협력하여 세분화 및 Liquid 내에서 사용하려는 모든 관련 이벤트 속성에 대한 필터링을 사용하도록 설정해야 합니다.
{% endalert %} 

## 캠페인 및 캔버스 트리거링 

Braze의 Shopify 사용자 지정 이벤트를 사용하면 다른 [사용자 지정 이벤트와]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-storage) 마찬가지로 캔버스 또는 캠페인을 트리거할 수 있습니다. 예를 들어 캔버스 진입 기준 내에서 Shopify `shopify_checkouts_abandon` 이벤트에서 트리거되는 실행 기반 캔버스를 생성할 수 있습니다. 

![사용자 지정 이벤트 "shopify_checkouts_abandon"을 수행하는 사용자를 입력하는 액션 기반 캔버스입니다.][5]

With nested object support for custom event properties, customers can trigger campaigns and Canvases using a nested event property. 다음은 `shopify_created_order` 사용자 지정 이벤트에서 특정 제품을 사용하여 캠페인을 트리거하는 예제입니다. `list_items[0].product_id`를 사용하여 항목 목록을 색인화하고 제품 ID에 액세스해야 합니다.

![중첩된 속성 "product_id"가 특정 숫자와 같은 사용자 지정 이벤트 "shopify_created_order"를 수행하는 사용자에게 전송하는 액션 기반 캠페인입니다.][26]

[5]: {% image_buster /assets/img/Shopify/shopify_integration11.png %}
[12]: {% image_buster /assets/img/Shopify/shopify_segmentation2.png %}
[13]: {% image_buster /assets/img/Shopify/shopify_segmentation3.png %}
[14]: {% image_buster /assets/img/Shopify/shopify_segmentation4.png %}
[26]: {% image_buster /assets/img/Shopify/shopify_integration17.png %}
