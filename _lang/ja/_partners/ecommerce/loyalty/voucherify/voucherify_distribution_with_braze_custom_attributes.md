---
nav_title: カスタム属性を持つディストリビューション
article_title: Voucherify でカスタム属性を使用するディストリビューション
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "このリファレンス記事では、Braze と Voucherify の統合について説明しています。Brazeの統合により、BrazeメッセージでVoucherifyコードを送信できます。"
page_type: partner
search_tag: Partner
---

# カスタム属性を持つディストリビューション

> Brazeの統合により、BrazeメッセージでVoucherifyコードを送信できます。このリファレンス記事では、Voucherify ディストリビューションで Braze のカスタム属性を使用する方法について説明します。

_この統合は Voucherify によって管理されます。_

{% alert tip %}
Voucherify ディストリビューションで Braze のカスタム属性を使用する前に、Braze ユーザーを Voucherify ダッシュボードに追加する必要があります。Braze コネクテッドコンテンツを使用して、ユーザーを同期したり、CSV や API を使用して顧客をインポートしたりできます。[Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) について詳しく知るには、こちらをご覧ください。
{% endalert %}

Braze のカスタム属性を使用すると、ユーザープロファイルのカスタム属性に Voucherify コードを割り当てることができます。ユニークなクーポン、ギフトカード、ロイヤルティカード、および紹介コードを使用できます。まず Voucherify を Braze に接続し、Voucherify でディストリビューションを作成し、最後に Braze でメッセージテンプレートのカスタム属性スニペットを使用したキャンペーンを作成します。

## ステップ1:BrazeにVoucherifyアカウントを接続する

まず、VoucherifyアカウントをBrazeと接続します。

1. BrazeアカウントからREST APIキーをコピーします。
2. Voucherifyダッシュボードの**Integrations**ディレクトリに移動し、Brazeを見つけて**Connect.**を選択します。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Braze API キーを貼り付けて、**接続**を選択します。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## ステップ2:コード配布

接続されると、Brazeのユーザープロファイルのカスタム属性にコードを割り当てる新しいVoucherify [配布](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work)を開始できます。後で、受け取った属性をコードと一緒にBrazeキャンペーンで使用できます。

ディストリビューションを設定する前に、Braze ユーザーを Voucherify ダッシュボードに追加する必要があります。[Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) について詳しく知るには、こちらをご覧ください。

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Braze にコードを配布するには、2 つのモードを使用できます:

- **マニュアルモード**
- ユーザーがアクションを実行したときにコードの配信をトリガーする**自動化されたワークフロー**を定義します。

手動モードと自動モードの両方で、Voucherify は固有のコードをその属性とともに送信し、それらをユーザープロファイルの Braze カスタム属性に割り当てます。

![カスタム属性にフィールドをマッピングする]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab マニュアルディストリビューション %}

マニュアルモードは、選択されたオーディエンスにコードを割り当てる一度限りのアクションです。ダッシュボードの [**Distribution**] に移動し、プラス記号を使ってディストリビューションマネージャーを実行し、[**Manual Message**] を選択します。

1.  ディストリビューションに名前を付けます。

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    ユニークなコードのソースとなるキャンペーン**(1)**を選択し、ユーザーのセグメントまたは単一の顧客を受信者として選択します**(2)**。顧客セグメントの詳細については、[Voucherify](https://support.voucherify.io/article/51-customer-segments) にアクセスしてください。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  次に、マーケティングの権限を追加します。オーディエンスからの許可を収集しない場合は、同意確認を無効にしてください。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Brazeをチャネルとして選択し、Brazeのユーザープロファイルに追加されるカスタムフィールドをマッピングします。発行されたバウチャーのコードを表すフィールドを追加する必要があります。残りのフィールドはオプションです。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  完了すると、分布の概要を確認できます。**保存して送信**をクリックして、コードをBrazeのユーザープロファイルに配信します。  

_すべてのマニュアルディストリビューションは10分遅れで送信されることに注意してください。_

{% endtab %}
{% tab 自動ワークフロー %}

Voucherifyは、次のトリガーに応じてBrazeにコードを自動的にプッシュできます:

- **Customer entered/left specific Voucherify segment**
- **Successful code publish** – Voucherify でキャンペーンのコードが顧客に発行された (割り当てられた) ときに送信されるメッセージです。
- **Order status changed** (order created、order updated、order has been paid、order canceled)
- **Gift credits added** – このメッセージは、ギフトカードクレジットが顧客のカードに追加されたときに送信されます。
- **ロイヤルティポイントが追加されました** – ロイヤルティポイントが顧客のプロファイルに追加されたときに送信されるメッセージです。
- **Voucher redeemed** – このメッセージは、バウチャーの引き換えが正常に完了した顧客に送信されます。
- **Voucher redemption rollback** – このメッセージは引き換えが正常にロールバックされた顧客に送信されます。
- **Reward redemption** – このメッセージは、顧客がロイヤルティまたは紹介報酬を引き換えるときに送信されます。
- **Custom event was logged for a customer** \- このメッセージは、Voucherify が特定のカスタムイベントを記録したときにトリガーされます。

Braze と Voucherify を使用して自動ワークフローを設定するには、[ディストリビューションチュートリアルを参照してください](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work)。

{% endtab %}
{% endtabs %}

## ステップ3:BrazeのキャンペーンでVoucherifyのカスタム属性を使用する

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

カスタム属性がBrazeの顧客のカスタム属性にコードと共に追加されると、それをキャンペーンで使用できます。

メッセージ本文を編集し、Voucherifyディストリビューションで定義されたカスタム属性を追加します。一意のコードを表示するため、{% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %} を配置します。

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

準備ができたら、メッセージプレビューでコードを確認できます。

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})

