---
nav_title: ユースケース
article_title: "BrazeでのShopifyの使用例"
description: "このリファレンス記事では、一般的な初心者と高度なShopify ユースケースの概要を説明します。"
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases/"
page_order: 2
---

# ユースケース

> ユーザーのためにタイムリーで効果的なメッセージングを作成するために、Shopifyインテグレーションをどのように活用できるかに関心がありますか?詳しくは、以下の一般的な[ビギナー](#beginner)および[アドバンス](#advanced)ユースケースを参照してください。

## 初心者

これらは、Shopifyを設定した直後に作成できる、シンプルで効果的なユースケースです。追加作業は必要ありません。 

### キャンペーン

これらのアクション経由のユースケースでは、Shopify指示に更新があったときにユーザーに警告することができます。

{% tabs ローカル %}
{% tab 返金 %}
**Shopify返金イベント** - `shopify_created_refund`

利用者には、一部または全部の払い戻しが行われた。このキャンペーンは、注文が正常に返金されたことをユーザーに知らせます。

![カスタムイベント"shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %})を実行するユーザーに入力するアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![メールに&quot と書かれています; ご注文は返金されています、ご注文にアプリの指摘がなかったことをお詫びします。返金は成功裏にお送りいたしました。ファンドがステートメント&クォートで耳をアプリするまで、3～5営業日お待ちください; " View Account" button.]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab キャンセル %}
**Shopify キャンセル換算イベント** - `shopify_cancelled_order`

ユーザは、フルフィルメント前に注文をキャンセルすることができました。このキャンペーンにより、ユーザーは自分の購買が正常にキャンセルされたことを認識できます。 

![カスタムイベント"shopify_キャンセル led_order".]({% image_buster /assets/img/Shopify/cancellation.png %}) を実行するユーザーに入力するアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![メールに&quot と書かれています;ご注文はキャンセルされています、ご覧になれて申し訳ありません!ご注文のキャンセルに成功しました。ファンドがステートメント&クォートで耳をアプリするまで、3～5営業日お待ちください; " View Account" button.]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab 受注完了 %}
**Shopifyが満たされたイベント** - `shopify_fulfilled_order`

ユーザーの注文のすべての品目が正常に実行されました。このキャンペーンは、ユーザーに、注文全体が履行されたことを知らせます。

![カスタムイベント"shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %})を実行するユーザーに入力するアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![テキスト&quot を含むテキストメッセージ;ご注文は完了しました!カートに入っている商品は全て届きました！あなたの口座に入り、領収書を確認してください。フィードバック."]({% image_buster /assets/img/Shopify/fulfilled2.png %})を終了するためのボーナスポイント{: style="max-width:40%;border:0;"}

{% endtab %}
{% tab 一部受注完了 %}
**Shopify部分的に満たされたイベント** - `shopify_partially_fulfilled_order`

ユーザーの注文の一部の品目が正常に実行されました。このキャンペーンにより、ユーザー s は注文全体の一部が履行されたことを知ることができます。

![カスタムイベント"shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %})を実行するユーザーに入るアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![テキスト&quotを含むテキストメッセージ;ご注文の一部が完了しました!ご注文いただいた商品の一部をお届けし、残りはお待ちしております！配送が完全に完了したら、別のアラートを送信します。"]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab 有料オーダー %}
**Shopify有料オーダーイベント** - `shopify_paid_order`

ユーザは注文に対して支払いを行い、注文ステータスは支払い済みに変更されます。このキャンペーンでは、ユーザーに、クレジットカードの支払いがキャプチャされたか、手動での支払いがあった場合に注文が支払い済みとしてマークされたことを通知します。

![カスタムイベント"shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %})を実行するユーザーに入力するアクションベースのキャンペーン{: style="max-width:45%;"}

**メッセージングの例**

![テキスト &quot を含むメール;お支払いを受け取りました!あなたの注文はWoohooで支払われました!私たちが支払いを処理し、あなたの商品を準備するために、1～2営業日待ってください。その後、出荷します!" a "View Account" button.]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvases

{% tabs ローカル %}
{% tab 放棄されたチェックアウトキャンバス %}

**放棄されたチェックアウトキャンバス**

ユーザはチェックアウトフローを破棄し、出発までにトランスアクションを完了できません。このキャンバスでは、トランスアクションを終了していないユーザーに自動リマインダーを送信して、チェックアウトフローに戻すことができます。

アクションベースのエントリ `shopify_abandoned_checkout`<br>
例外イベント: `shopify_created_order` または購入

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab 購入後のキャンバス %}

**購入後のキャンバス**

ユーザーが購入を成功させ、自分の購入がどのように気に入ったかを知りたいと思うようになりました。このキャンバスでは、フォローアップメッセージをユーザーに送信してフィードバックを収集できます。 

アクションベースのエントリイベント: `shopify_created_order` または購入

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## 詳細

プラットフォームに慣れると、より複雑なユースケースs を設定できます。

### キャンペーン

{% tabs ローカル %}
{% tab ユーザーの推奨事項 %}
**ユーザーの推奨事項**
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

利用者には、一部または全部の払い戻しが行われた。このキャンバスはフォローアップメッセージを送信して、ユーザーが再び購買するようにします。

アクションベースのエントリ `shopify_created_refund`<br>
例外イベント: `shopify_created_order` または購入

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab ウィンバック・キャンセル・レイション・キャンバス %}

**ウィンバック・キャンセル・レイション・キャンバス**

ユーザは、フルフィルメント前に注文をキャンセルすることができました。このキャンバスはフォローアップメッセージを送信して、ユーザーが再び購買するようにします。

アクションベースのエントリ `shopify_cancelled_order`<br>
例外イベント: `shopify_created_order` または購入

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}