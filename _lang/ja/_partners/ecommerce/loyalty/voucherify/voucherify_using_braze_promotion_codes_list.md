---
nav_title: Voucherifyとプロモーションコード一覧
article_title: Voucherify と Braze のプロモーションコードリスト
page_order: 4
alias: /partners/voucherify/promotion/
description: "このリファレンス記事では、Brazeプロモーションコードの抜粋を使用してVoucherify コードsを共有する方法について説明します。"
page_type: partner
search_tag: Partner
---

# Voucherify・Braze推進コード一覧

> 接続されたコンテンツおよびカスタム属性s に加えて、Braze プロモコードs スニペットを使用してVoucherify コードs を共有できます。最初に Voucherify からコードをエクスポートしてから Braze にコードをインポートし、プロモーションリストからコードを取得するメールコードスニペットを追加します。 

_この統合は Voucherify によって管理されます。_

## ステップ 1: Voucherifyからの一意のコードのエクスポート

Voucherify で、Voucherify キャンペーンに移動します。次に、**CSV**にエクスポートを選択し、CSVファイルを編集して列の名前を削除し、コードs の一覧のみを残します。

![]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

## ステップ2:プロモーションコードリストを作成する

[**Data Settings**] > [**Promotion Codes**] に移動し、[**Promotion Code List**] をクリックします。

Voucherify キャンペーンの名前を使用して、一覧に名前を付け、データコンシステンシーを確認できます。

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

次に、リストからコードs を参照するコードスニペットを追加します。メッセージの送信時に一意のコードが入力されます。

### 追加の設定

リスト期限切れアラートやしきい値アラートなどのコードs に属性s を設定することもできますが、コードの背後にあるロジックはVoucherify がリスト設定s に関係なく管理することに注意してください。

![リストの有効期限]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

## ステップ 3:上読み込む CSVファイル

Voucherify コードを含む CSV ファイルをアップロードします。

![]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

リストにコードのみが含まれていること (列ヘッダーは含まれていないこと) を確認し、[**Start Upload**] をクリックします。インポートが完了したら、**Save List**をクリックしてリストの詳細を確認します。

![]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

## ステップ4:Braze キャンペーンでのコードスニペットの使用

Braze キャンペーン内のリストからコードs を使用するには、スニペットをコピーしてメール本文に追加します。

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

コードの抜粋コードを追加して、一覧からコードを表示します。

![]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

コードを含むメッセージが送信されると、同じコードは再び使用されません。

