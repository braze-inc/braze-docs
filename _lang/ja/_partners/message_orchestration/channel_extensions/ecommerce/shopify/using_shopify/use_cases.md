---
nav_title: Use Cases
article_title:BrazeにおけるShopifyのユースケース
description:この参考記事は、一般的な初心者および上級者向けのShopifyの使用例を概説しています。
page_type: partner
search_tag:Partner
alias: "/shopify_use_cases/"
page_order:2
---

# ユースケース

> ユーザーにタイムリーで効果的なメッセージを作成するために、Shopify統合をどのように活用できるか興味がありますか？次のセクションを参照して、一般的な[初心者](#beginner)および[上級](#advanced)の使用例について詳しく学んでください。

## 初心者

これらは、Shopifyのセットアップ直後に作成できる、シンプルでありながら効果的なユースケースのいくつかです。追加の作業は必要ありません。 

### キャンペーン

これらのトランザクションユースケースにより、Shopifyの注文に更新があったときにユーザーに通知することができます。

{% tabs local %}
{% tab Refund %}
**Shopify返金イベント** - `shopify_created_refund`

ユーザーには、部分的または完全な払い戻しが提供されました。このキャンペーンは、ユーザーに注文が正常に返金されたことを知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "Your order has been refunded, Sorry that you were disappointed with your order. We've successfully sent your refund. Please wait 3-5 business days for the funds to appear in your statement" and a "View Account" button.]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Cancellation %}
**Shopifyキャンセルイベント** - `shopify_cancelled_order`

ユーザーは注文が完了する前にキャンセルすることができました。このキャンペーンは、ユーザーに購入が正常にキャンセルされたことを知らせます。 

![Action-based campaign that enters users who perform the custom event "shopify_cancelled_order".]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "Your order has been canceled, Sorry to see you go! We've successfully canceled your order. Please wait 3-5 business days for the funds to appear in your statement" and a "View Account" button.]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Fulfilled order %}
**Shopifyがイベントを完了しました** - `shopify_fulfilled_order`

ユーザーの注文のすべての品目が正常に処理されました。このキャンペーンは、ユーザーに注文全体が完了したことを知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Text message with the text "Your order's been fulfilled! All items in your cart have been delivered! Please go into your account and confirm receipt. Bonus points for leaving feedback."]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Partially fulfilled order %}
**Shopify部分的に履行されたイベント** - `shopify_partially_fulfilled_order`

ユーザーの注文のいくつかの品目は正常に処理されました。このキャンペーンは、ユーザーに注文全体の一部が完了したことを知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Text message with the text "Your order's been partially fulfilled! We've delivered some of the items in your order and the rest are on the way! We'll send you another alert when the delivery's been fully complete."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Paid order %}
**Shopifyの支払い済み注文イベント** - `shopify_paid_order`

ユーザーが注文を支払い、注文のステータスが支払い済みに変更されます。このキャンペーンは、クレジットカードの支払いが処理されたこと、または手動支払いがあった場合に注文が支払済みとしてマークされたことをユーザーに知らせます。

![Action-based campaign that enters users who perform the custom event "shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**メッセージングの例**

![Email with the text "We've received your Payment! Woohoo your order's been paid for! Please wait 1-2 business days for us to process the payment and prep your items. Then we'll ship it out!" and a "View Account" button.]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvases

{% tabs local %}
{% tab Abandoned checkout Canvas %}

**放棄されたチェックアウトキャンバス**

ユーザーはチェックアウトフローを放棄し、出発前に取引を完了できていません。このキャンバスを使用すると、取引を完了していないユーザーに自動リマインダーを送信して、チェックアウトフローに戻すことができます。

アクションベースのエントリーイベント: `shopify_abandoned_checkout`<br>
例外イベント: `shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Post-purchase Canvas %}

**購入後のキャンバス**

ユーザーは購入に成功し、今度は購入を気に入ったかどうかを知りたいと思っています。このキャンバスを使用すると、ユーザーにフォローアップメッセージを送信してフィードバックを収集できます。 

アクションベースのエントリーイベント: `shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## 高度な

プラットフォームに慣れてきたら、より複雑なユースケースを設定できます。

### キャンペーン

{% tabs local %}
{% tab User recommendations %}
**ユーザーのおすすめ**
![\]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

ユーザーがアイテムをクリックまたは表示しましたが、購入しませんでした。このキャンペーンは、ユーザーに同じまたは類似のアイテム（Connected Contentによって推奨される）をフォローアップメッセージとして送信し、ユーザーにそれらのいずれかを購入するよう促します。

アクションベースのエントリーイベント: `shopify_product_clicked` または `shopify_product_viewed`<br>
![\]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
例外イベント: `shopify_created_order` または購入<br>
![\]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### キャンバス

{% tabs local %}
{% tab Refund winback Canvas %}

**返金の取り戻しキャンバス**

ユーザーには、部分的または完全な払い戻しが提供されました。このキャンバスは、ユーザーに再購入を促すフォローアップメッセージを送信します。

アクションベースのエントリーイベント: `shopify_created_refund`<br>
例外イベント: `shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Winback cancellation Canvas %}

**Winbackキャンセルキャンバス**

ユーザーは注文が完了する前にキャンセルすることができました。このキャンバスは、ユーザーに再購入を促すフォローアップメッセージを送信します。

アクションベースのエントリーイベント: `shopify_cancelled_order`<br>
例外イベント: `shopify_created_order` または購入

![\]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}