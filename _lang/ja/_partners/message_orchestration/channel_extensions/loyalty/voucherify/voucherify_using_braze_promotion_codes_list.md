---
nav_title: Voucherify and Promotion Codes List
article_title:VoucherifyとBrazeプロモーションコードリスト
page_order:4
alias: /partners/voucherify/promotion/
description:この参考記事では、Brazeプロモコードスニペットを使用してVoucherifyコードを共有する方法について説明します。
page_type: partner
search_tag:Partner
---

# VoucherifyとBrazeのプロモーションコードリスト

> さらに、接続されたコンテンツとカスタム属性に加えて、Brazeプロモコードスニペットを使用してVoucherifyコードを共有できます。まず、Voucherifyからコードをエクスポートし、Brazeにコードをインポートし、プロモーションリストからコードを取得するためのメールコードスニペットを追加します。 

## ステップ1:バウチャリファイからユニークコードをエクスポートする

Voucherifyで、Voucherifyキャンペーンに移動します。次に、**CSVにエクスポート**を選択し、CSVファイルを編集して列の名前を削除し、コードのリストのみを残します。

![\]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

## ステップ2:プロモーションコードリストを作成する

**データ設定** > **プロモーションコード** に移動し、**プロモーションコードリストを作成** をクリックします。

{% alert note %}
古いナビゲーションを使用している場合は、プロモーションコードを統合の下に見つけることができます。
{% endalert %}

バウチャリファイキャンペーン名を使用してリストに名前を付け、データの一貫性を確認できます。

![\]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

次に、リストからのコードを参照するコードスニペットを追加します。メッセージが送信されると、固有のコードが入力されます。

### 追加の設定

コードの属性（リストの有効期限やしきい値アラートなど）を設定することもできます。ただし、リスト設定に関係なく、Voucherifyはコードの背後にあるロジックを管理します。

![List expiration]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

## ステップ3:CSVファイルをアップロード

バウチャリーコードを含むCSVファイルをアップロードしてください。

![\]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

リストにコードのみが含まれていることを確認し、**アップロード開始**をクリックします。インポートが完了したら、リストの詳細を確認するために**リストを保存**をクリックします。

![\]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

## ステップ 4:Brazeキャンペーンでコードスニペットを使用する

Brazeキャンペーンでリストのコードを使用するには、スニペットをコピーしてメール本文に追加します。

![\]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

リストからコードを表示するコードスニペットを追加します。

![\]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

メッセージがコードと共に送信されると、同じコードは再利用されません。
