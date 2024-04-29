---
nav_title: ユースケース
article_title: "ろう付けの使用事例"
description: "このリファレンス記事では、一般的な初心者と高度なShopifyのユースケースについて概説します。"
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases/"
page_order: 2
---

# ユースケース

> Shopifyの統合を活用して、ユーザーのためのタイムリーで効果的なメッセージングを作成する方法に興味がありますか?詳細については、一般的な[ビギナー](#beginner)および[アドバンスト](#advanced)ユースケースの以下のセクションを参照してください。

## 未経験者

これらは、Shopify を設定した直後に作成できる、単純で効果的なユースケースです。追加作業は必要ありません。 

### キャンペーン

これらのトランザクションユースケースを使用すると、Shopify の順序が更新されたときにユーザにアラートを送信できます。

{% tabs local %}
{% tab Refund %}
**Shopify返金イベント** - `shopify_created_refund`

利用者には、一部または全部の払い戻しが行われた。このキャンペーンでは、注文が正常に返金されたことがユーザに通知されます。

![Action-based campaign that enters users who perform the custom event "shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "Your order has been refunded, Sorry that you were disappointed with your order. We've successfully sent your refund. Please wait 3-5 business days for the funds to appear in your statement" and a "View Account" button.]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Cancellation %}
**Shopifyキャンセルイベント** - `shopify_cancelled_order`

ユーザーはフルフィルメント前に注文をキャンセルすることができました。このキャンペーンでは、購入が正常にキャンセルされたことがユーザに通知されます。 

![Action-based campaign that enters users who perform the custom event "shopify_cancelled_order".]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "Your order has been canceled, Sorry to see you go! We've successfully canceled your order. Please wait 3-5 business days for the funds to appear in your statement" and a "View Account" button.]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Fulfilled order %}
**Shopify fulfilled event** - `shopify_fulfilled_order`

ユーザの注文のすべての明細項目が正常に満たされました。このキャンペーンでは、ユーザーに注文全体が完了したことを知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Text message with the text "Your order's been fulfilled! All items in your cart have been delivered! Please go into your account and confirm receipt. Bonus points for leaving feedback."]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Partially fulfilled order %}
**Shopify partially fulfilled event** - `shopify_partially_fulfilled_order`

ユーザの注文の一部の品目が正常に実行されました。このキャンペーンでは、注文全体の一部が履行されたことをユーザーに知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Text message with the text "Your order's been partially fulfilled! We've delivered some of the items in your order and the rest are on the way! We'll send you another alert when the delivery's been fully complete."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Paid order %}
**Shopify 有料オーダーイベント** - `shopify_paid_order`

ユーザは注文に対して支払いを行い、注文ステータスは支払い済みに変わります。このキャンペーンでは、クレジットカード決済がキャプチャされたか、手動決済があった場合に注文が有料とマークされたことをユーザーに知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "We've received your Payment! Woohoo your order's been paid for! Please wait 1-2 business days for us to process the payment and prep your items. Then we'll ship it out!" and a "View Account" button.]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### 見ることができます。

{% tabs local %}
{% tab Abandoned checkout Canvas %}

**放棄されたチェックアウトキャンバス**

ユーザーはチェックアウトフローを破棄し、出発前にトランザクションを完了できません。このキャンバスでは、トランザクションを完了していないユーザーに自動リマインダーを送信して、チェックアウトフローに戻すことができます。

アクションベースのエントリイベント: `shopify_abandoned_checkout`<br>
例外イベント: `shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Post-purchase Canvas %}

**購入後のキャンバス**

ユーザーが購入を成功させ、自分の購入がどのように気に入ったかを知りたいと思うようになりました。このキャンバスでは、ユーザーにフォローアップメッセージを送信してフィードバックを収集できます。 

アクションベースのエントリイベント: `shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## 上級者

プラットフォームに慣れると、より複雑なユースケースを設定できます。

### キャンペーン

{% tabs local %}
{% tab User recommendations %}
**ユーザーの推奨事項**


ユーザーはアイテムをクリックまたは表示しましたが、購入しませんでした。このキャンペーンでは、同じアイテムまたは類似のアイテム(Connected Content で推奨) を持つユーザにフォローアップメッセージを送信し、そのうちの1 つを購入するようにユーザに求めます。

アクションベースのエントリイベント: `shopify_product_clicked` または `shopify_product_viewed`<br>
{% image_buster /assets/img/Shopify/product_view3.png %}{: style="max-width:45%;border:0;"}
<br><br>
例外イベント: `shopify_created_order` または購入<br>
{% image_buster /assets/img/Shopify/product_view2.png %}{: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### キャンバス

{% tabs local %}
{% tab Refund winback Canvas %}

**返金ウィンバックキャンバス**

利用者には、一部または全部の払い戻しが行われた。このキャンバスはフォローアップメッセージを送信して、ユーザーが再び購入するようにします。

アクションベースのエントリイベント: `shopify_created_refund`<br>
例外イベント: `shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Winback cancellation Canvas %}

**Winbackキャンセルキャンバス**

ユーザーはフルフィルメント前に注文をキャンセルすることができました。このキャンバスはフォローアップメッセージを送信して、ユーザーが再び購入するようにします。

アクションベースのエントリイベント: `shopify_cancelled_order`<br>
例外イベント: `shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}