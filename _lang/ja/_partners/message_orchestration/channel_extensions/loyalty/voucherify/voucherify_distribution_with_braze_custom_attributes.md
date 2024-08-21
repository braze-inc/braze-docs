---
nav_title: カスタム属性を持つディストリビューション
article_title: Voucherifyを使用したカスタム属性の配布
page_order: 3
alias: /partners/voucherify/custom_attributes/
description: "このリファレンス記事は、BrazeとVoucherifyの統合について説明しています。Brazeの統合により、BrazeメッセージでVoucherifyコードを送信できます。"
page_type: partner
search_tag: Partner
---

# カスタム属性を持つディストリビューション

> Brazeの統合により、BrazeメッセージでVoucherifyコードを送信できます。このリファレンス記事では、Brazeのカスタム属性をVoucherifyの配信で使用する方法について説明します。

{% alert tip %}
Voucherifyの配布でBrazeのカスタム属性を使用する前に、BrazeユーザーをVoucherifyのダッシュボードに追加する必要があります。Brazeコネクテッドコンテンツを使用して、ユーザーを同期したり、CSVやAPIを通じて顧客をインポートしたりできます。[Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) について詳しく知るには、こちらをご覧ください。
{% endalert %}

Braze のカスタム属性を使用すると、ユーザープロファイルのカスタム属性に Voucherify コードを割り当てることができます。ユニークなクーポン、ギフトカード、ロイヤルティカード、および紹介コードを使用できます。まず、VoucherifyをBrazeに接続し、Voucherifyで配布を作成し、最後にBrazeでカスタム属性スニペットをメッセージテンプレートに含めたキャンペーンを作成します。

## ステップ1:BrazeにVoucherifyアカウントを接続する

まず、VoucherifyアカウントをBrazeと接続します。

1. BrazeアカウントからREST APIキーをコピーします。
2. Voucherifyダッシュボードの**Integrations**ディレクトリに移動し、Brazeを見つけて**Connect.**を選択します。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Braze API キーを貼り付けて、**接続**を選択します。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## ステップ2:コード配布

接続されると、Brazeのユーザープロファイルのカスタム属性にコードを割り当てる新しいVoucherify [配布](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work)を開始できます。後で、受け取った属性をコードと一緒にBrazeキャンペーンで使用できます。

配布を設定する前に、BrazeユーザーをVoucherifyダッシュボードに追加する必要があります。[Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers) について詳しく知るには、訪問してください。

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Braze にコードを配布するには、2 つのモードを使用できます:

- **マニュアルモード**
- ユーザーがアクションを実行したときにコードの配信をトリガーする**自動化されたワークフロー**を定義します。

手動モードと自動モードの両方で、Voucherifyは固有のコードをその属性とともに送信し、それらをユーザープロファイルのBrazeカスタム属性に割り当てます。

![カスタム属性にフィールドをマッピングする]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab 手動配布 %}

マニュアルモードは、選択されたオーディエンスにコードを割り当てる一度限りのアクションです。ダッシュボードの**配布**に移動し、プラスで配布マネージャーを実行し、**手動メッセージ**を選択します。

1.  あなたの配布物に名前を付けてください。

    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    ユニークなコードのソースとなるキャンペーン**(1)**を選択し、ユーザーのセグメントまたは単一の顧客を受信者として選択します**(2)**。[Voucherify](https://support.voucherify.io/article/51-customer-segments) にアクセスして顧客セグメントの詳細をご覧ください。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  次に、マーケティングの権限を追加します。オーディエンスからの許可を収集しない場合は、同意確認を無効にしてください。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Brazeをチャネルとして選択し、Brazeのユーザープロファイルに追加されるカスタムフィールドをマッピングします。発行されたバウチャーのコードを表すフィールドを追加する必要があります。残りのフィールドはオプションです。  
    
    ![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  完了すると、分布の概要を確認できます。**保存して送信**をクリックして、コードをBrazeのユーザープロファイルに配信します。  

_すべての手動配信は10分遅れで送信されることに注意してください。_

{% endtab %}
{% tab 自動ワークフロー %}

Voucherifyは、次のトリガーに応じてBrazeにコードを自動的にプッシュできます:

- **顧客 entered/left specific Voucherify Segment**
- **コードの発行に成功しました** – コードがキャンペーンから顧客に発行（割り当て）されたときに送信されるメッセージです。
- **注文ステータスが変更されました**（注文が作成されました、注文が更新されました、注文が支払われました、注文がキャンセルされました）
- **ギフトクレジットが追加されました** – メッセージは、ギフトカードクレジットが顧客のカードに追加されたときに送信されます。
- **ロイヤルティポイントが追加されました** – ロイヤルティポイントが顧客のプロファイルに追加されたときに送信されるメッセージです。
- **バウチャーが引き換えられました** – このメッセージは、バウチャーを正常に引き換えた顧客に送信されます。
- **バウチャーの償還のロールバック** – メッセージは償還が正常にロールバックされた顧客に送信されます。
- **報酬引き換え** – メッセージは顧客がロイヤルティまたは紹介報酬を引き換えるときに送信されます。
- **カスタムイベントが顧客に対して記録されました** \- このメッセージは、Voucherifyが特定のカスタムイベントを記録したときにトリガーされます。

BrazeとVoucherifyを使用して自動ワークフローを設定するには、[配布チュートリアルを参照してください](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work)。

{% endtab %}
{% endtabs %}

## ステップ3:BrazeのキャンペーンでVoucherifyのカスタム属性を使用する

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

カスタム属性がBrazeの顧客のカスタム属性にコードと共に追加されると、それをキャンペーンで使用できます。

メッセージ本文を編集し、Voucherifyディストリビューションで定義されたカスタム属性を追加します。{% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %}を配置して、ユニークなコードを表示します。

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

準備ができたら、メッセージプレビューでコードを確認できます。

![]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})
