---
nav_title: 활용 사례
article_title: "Braze의 Shopify 사용 사례"
description: "이 참조 문서에서는 일반적인 초급 및 고급 Shopify 사용 사례를 간략하게 설명합니다."
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases_legacy/"
page_order: 2
---

# 사용 사례

> Shopify 통합을 활용하여 사용자에게 시기적절하고 효과적인 메시지를 생성하는 방법에 대해 알고 싶으신가요? 자세한 내용은 일반적인 [초급](#beginner) 및 [고급](#advanced) 사용 사례에 대한 다음 섹션을 참조하세요!

## 무경험자

다음은 Shopify를 설정한 직후에 생성할 수 있는 간단하면서도 효과적인 몇 가지 사용 사례입니다. 추가 작업이 필요하지 않습니다. 

### 캠페인

이러한 트랜잭션 사용 사례를 사용하면 Shopify 주문에 업데이트가 있을 때 사용자에게 알림을 보낼 수 있습니다.

{% tabs local %}
{% tab 환불 %}
**Shopify 환불 이벤트** - `shopify_created_refund`

사용자에게 일부 또는 전액 환불을 제공했습니다. 이 캠페인은 주문이 성공적으로 환불되었음을 사용자에게 알립니다.

![사용자 지정 이벤트 "shopify_created_refund"를 수행하는 사용자를 입력하는 액션 기반 캠페인.]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**메시징 예제**

!["주문이 환불되었습니다. 주문에 실망하여 죄송합니다."라는 텍스트가 포함된 이메일이 전송됩니다. 환불을 성공적으로 보냈습니다. 명세서에 환불 금액이 표시될 때까지 영업일 기준 3~5일 정도 기다려 주세요.'라는 문구와 '계좌 보기' 버튼이 표시됩니다.]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab 취소 %}
**Shopify 취소 이벤트** - `shopify_cancelled_order`

사용자는 주문이 처리되기 전에 주문을 취소할 수 있었습니다. 이 캠페인은 구매가 성공적으로 취소되었음을 사용자에게 알립니다. 

![사용자 지정 이벤트 "shopify_cancelled_order"를 수행하는 사용자를 입력하는 액션 기반 캠페인.]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**메시징 예제**

!['주문이 취소되었습니다, 죄송합니다! 주문이 성공적으로 취소되었습니다. 명세서에 환불 금액이 표시될 때까지 영업일 기준 3~5일 정도 기다려 주세요.'라는 문구와 '계좌 보기' 버튼이 표시됩니다.]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab 주문 처리된 주문 %}
**Shopify 주문 처리 이벤트** - `shopify_fulfilled_order`

사용자 주문의 모든 라인 항목이 성공적으로 처리되었습니다. 이 캠페인을 통해 사용자는 전체 주문이 처리되었음을 알 수 있습니다.

![사용자 지정 이벤트 "shopify_fulfilled_order"를 수행하는 사용자를 입력하는 액션 기반 캠페인.]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**메시징 예제**

!["주문이 처리되었습니다!"라는 텍스트가 포함된 문자 메시지가 표시됩니다. 장바구니에 있는 모든 상품이 배송되었습니다! 계정으로 이동하여 영수증을 확인하세요. 피드백을 남기면 보너스 포인트가 제공됩니다.']({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab 부분 주문 처리된 주문 %}
**Shopify 부분 주문 처리 이벤트** - `shopify_partially_fulfilled_order`

사용자 주문의 일부 품목이 성공적으로 처리되었습니다. 이 캠페인을 통해 사용자는 전체 주문의 일부가 처리되었음을 알 수 있습니다.

![사용자 지정 이벤트 "shopify_partially_fulfilled_order"를 수행하는 사용자를 입력하는 액션 기반 캠페인입니다.]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**메시징 예제**

!["주문이 부분적으로 처리되었습니다!"라는 텍스트가 포함된 문자 메시지. 주문하신 상품 중 일부가 배송되었으며 나머지는 배송 중입니다! 배송이 완전히 완료되면 다시 알림을 보내드리겠습니다."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab 지급 완료된 주문 %}
**Shopify 지급 완료된 주문 이벤트** - `shopify_paid_order`

사용자가 주문 금액을 결제하면 주문 상태가 결제됨으로 변경됩니다. 이 캠페인은 사용자에게 신용카드 결제가 캡처되었거나 수동 결제가 있는 경우 주문이 결제된 것으로 표시되었음을 알려줍니다.

![사용자 지정 이벤트 "shopify_paid_order"를 수행하는 사용자를 입력하는 액션 기반 캠페인.]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**메시징 예제**

!["결제가 접수되었습니다!"라는 텍스트가 포함된 이메일이 전송됩니다. 우후, 주문이 결제되었습니다! 결제를 처리하고 상품을 준비할 때까지 영업일 기준 1~2일 정도 기다려 주세요. 그러면 배송해 드립니다!"와 "계정 보기" 버튼이 표시됩니다.]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### 캔버스

{% tabs local %}
{% tab 중단된 결제 캔버스 %}

**중단된 결제 캔버스**

사용자가 결제 흐름을 포기하고 출발하기 전에 거래를 완료하지 못합니다. 이 캔버스를 사용하면 거래를 완료하지 않은 사용자에게 자동 알림을 보내 결제 흐름에 다시 참여하도록 유도할 수 있습니다.

실행 기반 진입 이벤트: `shopify_abandoned_checkout`<br>
예외 이벤트: `shopify_created_order` 또는 구매

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab 구매 후 캔버스 %}

**구매 후 캔버스**

사용자가 구매에 성공했으니 이제 구매에 대해 어떻게 생각하는지 알고 싶을 것입니다. 이 캔버스를 사용하면 사용자에게 후속 메시지를 보내 피드백을 수집할 수 있습니다. 

액션 기반 응모 이벤트: `shopify_created_order` 또는 구매

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## 고급

플랫폼에 익숙해지면 좀 더 복잡한 사용 사례를 설정할 수 있습니다.

### 캠페인

{% tabs local %}
{% tab 사용자 추천 %}
**사용자 추천**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

사용자가 항목을 클릭하거나 보았지만 구매하지 않은 경우. 이 캠페인은 사용자에게 동일하거나 유사한 아이템(커넥티드 콘텐츠에서 추천한 아이템)이 있는 후속 메시지를 보내 사용자에게 구매를 유도합니다.

액션 기반 응모 이벤트: `shopify_product_clicked` 또는 `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
예외 이벤트: `shopify_created_order` 또는 구매<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### 캔버스

{% tabs local %}
{% tab 환불 윈백 캔버스 %}

**환불 윈백 캔버스**

사용자에게 일부 또는 전액 환불을 제공했습니다. 이 캔버스는 사용자의 재구매를 유도하는 후속 메시지를 보냅니다.

실행 기반 진입 이벤트: `shopify_created_refund`<br>
예외 이벤트: `shopify_created_order` 또는 구매

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab 윈백 취소 캔버스 %}

**윈백 취소 캔버스**

사용자는 주문이 처리되기 전에 주문을 취소할 수 있었습니다. 이 캔버스는 사용자의 재구매를 유도하는 후속 메시지를 보냅니다.

실행 기반 진입 이벤트: `shopify_cancelled_order`<br>
예외 이벤트: `shopify_created_order` 또는 구매

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}