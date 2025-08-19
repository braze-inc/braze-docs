---
nav_title: ユースケース
article_title: "BrazeでのShopifyの使用例"
description: "このリファレンス記事では、一般的な初心者と高度なShopify ユースケースの概要を説明します。"
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases_legacy/"
page_order: 2
---

# ユースケース

> ユーザーのためにタイムリーで効果的なメッセージングを作成するために、Shopifyインテグレーションをどのように活用できるかに関心がありますか?詳しくは、以下の一般的な[ビギナー](#beginner)および[アドバンス](#advanced)ユースケースを参照してください。

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## 初心者

これらは、Shopifyを設定した直後に作成できる、シンプルで効果的なユースケースです。追加作業は必要ありません。 

### キャンペーン

これらのアクション経由のユースケースでは、Shopify指示に更新があったときにユーザーに警告することができます。

{% tabs ローカル %}
{% tab 返金 %}
**Shopify返金イベント** - `shopify_created_refund`

ユーザーに一部または全額が返金されました。このキャンペーンは、注文が正常に返金されたことをユーザーに知らせます。

![カスタムイベント"shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %})を実行するユーザーに入力するアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![テキスト「Your order has been refunded, Sorry that you were disappointed with your order.返金は成功裏にお送りいたしました。Please wait 3-5 business days for the funds to appear in your statement」と「View Account」ボタンが表示されているメール。]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab キャンセル %}
**Shopify キャンセル換算イベント** - `shopify_cancelled_order`

ユーザーはフルフィルメント前に注文をキャンセルできました。このキャンペーンにより、ユーザーは自分の購買が正常にキャンセルされたことを認識できます。 

![カスタムイベント"shopify_キャンセル led_order".]({% image_buster /assets/img/Shopify/cancellation.png %}) を実行するユーザーに入力するアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![メールに&quot と書かれています;ご注文はキャンセルされています、ご覧になれて申し訳ありません!We've successfully canceled your order.Please wait 3-5 business days for the funds to appear in your statement」と「View Account」ボタンが表示されているメール。]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab フルフィルメントが完了した注文 %}
**Shopify フルフィルメント完了イベント** - `shopify_fulfilled_order`

ユーザーの注文のすべての品目が正常にフルフィルメントされました。このキャンペーンは、ユーザーに、注文全体が履行されたことを知らせます。

![カスタムイベント"shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %})を実行するユーザーに入力するアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![テキスト「Your order's been fulfilled!カートに入っている商品は全て届きました！Please go into your account and confirm receipt.Bonus points for leaving feedback.」が表示されているテキストメッセージ。]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab 部分的にフルフィルメントされた注文 %}
**Shopify 部分的フルフィルメントイベント** - `shopify_partially_fulfilled_order`

ユーザーの注文の一部の品目が正常にフルフィルメントされました。このキャンペーンは、注文全体の一部がフルフィルメントされたことをユーザーに知らせます。

![カスタムイベント"shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %})を実行するユーザーに入るアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![テキスト「Your order's been partially fulfilled!ご注文いただいた商品の一部をお届けし、残りはお待ちしております！配送が完全に完了したら、別のアラートを送信します。"]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab 支払い済みの注文 %}
**Shopify 支払い済みの注文イベント** - `shopify_paid_order`

ユーザーが注文に対して支払いを行い、注文ステータスが支払い済みに変わります。このキャンペーンでは、ユーザーに、クレジットカードの支払いがキャプチャされたか、手動での支払いがあった場合に注文が支払い済みとしてマークされたことを通知します。

![カスタムイベント"shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %})を実行するユーザーに入力するアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![テキスト「We've received your Payment!あなたの注文はWoohooで支払われました!私たちが支払いを処理し、あなたの商品を準備するために、1～2営業日待ってください。Then we'll ship it out!」と「View Account」ボタンが表示されているメール。]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvases

{% tabs ローカル %}
{% tab 購入手続き放棄キャンバス %}

**購入手続き放棄キャンバス**

ユーザーが購入手続きフローを放棄し、離れる前に取引を完了できませんでした。このキャンバスでは、取引を完了していないユーザーを購入手続きフローに呼び戻すために、このようなユーザーに自動リマインダーを送信できます。

アクションベースのエントリイベント: `shopify_abandoned_checkout`<br>
例外イベント: `shopify_created_order` または購入

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab 購入後処理キャンバス %}

**購入後処理キャンバス**

ユーザーが購入を成功させ、自分の購入がどのように気に入ったかを知りたいと思うようになりました。このキャンバスでは、フォローアップメッセージをユーザーに送信してフィードバックを収集できます。 

アクションベースのエントリイベント: `shopify_created_order` または購入

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## 上級者

プラットフォームに慣れたら、より複雑なユースケースを設定できます。

### キャンペーン

{% tabs ローカル %}
{% tab ユーザーの推奨事項 %}
**ユーザーレコメンデーション**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

ユーザーはアイテムをクリックまたは表示しましたが、購入しませんでした。このキャンペーンは、同じまたは類似のアイテム(接続されたコンテンツで推奨)を持つユーザーにフォローアップメッセージを送信し、ユーザーにそのうちの1つを購入するように促します。

アクションベースのエントリイベント: `shopify_product_clicked`または `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
例外イベント: `shopify_created_order` または購入<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### キャンバス

{% tabs ローカル %}
{% tab 返金ウィンバックキャンバス %}

**返金ウィンバックキャンバス**

ユーザーに一部または全額が返金されました。このキャンバスは、フォローアップメッセージを送信して、ユーザーが再び購入するように働きかけます。

アクションベースのエントリイベント: `shopify_created_refund`<br>
例外イベント: `shopify_created_order` または購入

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab ウィンバックキャンセルキャンバス %}

**ウィンバックキャンセルキャンバス**

ユーザーはフルフィルメント前に注文をキャンセルできました。このキャンバスは、フォローアップメッセージを送信して、ユーザーが再び購入するように働きかけます。

アクションベースのエントリイベント: `shopify_cancelled_order`<br>
例外イベント: `shopify_created_order` または購入

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}