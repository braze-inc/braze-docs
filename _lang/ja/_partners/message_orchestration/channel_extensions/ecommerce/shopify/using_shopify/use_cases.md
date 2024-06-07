---
nav_title: ユースケース
article_title: "BrazeにおけるShopifyの使用例"
description: "この参考記事では、一般的なShopifyの初心者と上級者の使用例を概説しています。"
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases/"
page_order: 2
---

# ユースケース

> Shopifyとの統合を活用して、ユーザーにタイムリーで効果的なメッセージングを作成する方法にご興味がありますか？一般的な[初心者の](#beginner)使用例と[上級者の](#advanced)使用例については、以下のセクションを参照してください！

## 初心者

これらは、Shopifyを立ち上げてすぐに作成できる、シンプルで効果的な使用例である。追加の作業は必要ない。 

### キャンペーン

これらのトランザクションユースケースでは、Shopifyの注文に更新があったときにユーザーにアラートを出すことができます。

{% tabs local %}
{% tab Refund %}
**Shopify返金イベント** `shopify_created_refund`

利用者には、一部または全額の払い戻しが行われた。このキャンペーンでは、ユーザーに注文が正常に返金されたことを知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "Your order has been refunded, Sorry that you were disappointed with your order. We've successfully sent your refund. Please wait 3-5 business days for the funds to appear in your statement" and a "View Account" button.]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Cancellation %}
**Shopifyキャンセルイベント** `shopify_cancelled_order`

利用者は注文を履行前にキャンセルすることができた。このキャンペーンは、ユーザーに購入がキャンセルされたことを知らせます。 

![Action-based campaign that enters users who perform the custom event "shopify_cancelled_order".]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "Your order has been canceled, Sorry to see you go! We've successfully canceled your order. Please wait 3-5 business days for the funds to appear in your statement" and a "View Account" button.]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Fulfilled order %}
**Shopify充実のイベント** `shopify_fulfilled_order`

ユーザーの注文のすべての行項目が正常に完了しました。このキャンペーンは、ユーザーに注文がすべて完了したことを知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Text message with the text "Your order's been fulfilled! All items in your cart have been delivered! Please go into your account and confirm receipt. Bonus points for leaving feedback."]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Partially fulfilled order %}
**Shopifyが部分的に履行したイベント** `shopify_partially_fulfilled_order`

ユーザー注文の一部の行項目が正常に処理されました。このキャンペーンにより、ユーザーは注文全体の一部が達成されたことを知ることができる。

![Action-based campaign that enters users who perform the custom event "shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Text message with the text "Your order's been partially fulfilled! We've delivered some of the items in your order and the rest are on the way! We'll send you another alert when the delivery's been fully complete."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Paid order %}
**Shopify有料注文イベント** `shopify_paid_order`

ユーザーは注文の代金を支払い、注文ステータスは支払済みに変更されます。このキャンペーンでは、クレジットカードによる支払いが行われたこと、または手動で支払いが行われた場合は注文が支払い済みとしてマークされたことをユーザーに知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "We've received your Payment! Woohoo your order's been paid for! Please wait 1-2 business days for us to process the payment and prep your items. Then we'll ship it out!" and a "View Account" button.]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvases

{% tabs local %}
{% tab Abandoned checkout Canvas %}

**放棄されたチェックアウト・キャンバス**

ユーザーはチェックアウトフローを放棄し、トランザクションを完了できずに離脱している。このキャンバスでは、トランザクションを完了していないユーザーに自動リマインダーを送信し、チェックアウトフローに戻すことができます。

アクションベースのエントリーイベント： `shopify_abandoned_checkout`<br>
例外イベント：`shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Post-purchase Canvas %}

**購入後のキャンバス**

ユーザーは購入に成功した。このキャンバスでは、ユーザーにフォローアップメッセージを送信してフィードバックを収集することができます。 

アクションに基づくエントリー・イベント：`shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## 上級者

プラットフォームに慣れてきたら、より複雑なユースケースを設定することができる。

### キャンペーン

{% tabs local %}
{% tab User recommendations %}
**ユーザーの推奨**
![\]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

ユーザーが商品をクリックまたは閲覧したが、購入しなかった。このキャンペーンでは、同じ商品または類似の商品（コネクテッドコンテンツがおすすめする商品）をフォローアップメッセージとしてユーザーに送り、いずれかの商品の購入を促します。

アクションベースのエントリーイベント：`shopify_product_clicked` または `shopify_product_viewed`<br>
{% image_buster /assets/img/Shopify/product_view3.png %}{: style="max-width:45%;border:0;"}
<br><br>
例外イベント：`shopify_created_order` または購入<br>
{% image_buster /assets/img/Shopify/product_view2.png %}{: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### キャンバス

{% tabs local %}
{% tab Refund winback Canvas %}

**リファンド・ウィンバック・キャンバス**

利用者には、一部または全額の払い戻しが行われた。このキャンバスは、ユーザーに再度購入してもらうためのフォローアップ・メッセージを送信する。

アクションベースのエントリーイベント： `shopify_created_refund`<br>
例外イベント：`shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Winback cancellation Canvas %}

**ウィンバックキャンセルキャンバス**

利用者は注文を履行前にキャンセルすることができた。このキャンバスは、ユーザーに再度購入してもらうためのフォローアップ・メッセージを送信する。

アクションベースのエントリーイベント： `shopify_cancelled_order`<br>
例外イベント：`shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}