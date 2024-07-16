---
nav_title: Distributions with Custom Attributes
article_title:バウチャリファイによるカスタム属性を持つ配布
page_order:3
alias: /partners/voucherify/custom_attributes/
description:この記事は、BrazeとVoucherifyの統合について説明しています。Brazeの統合により、BrazeメッセージでVoucherifyコードを送信できます。
page_type: partner
search_tag:Partner
---

# カスタム属性を持つディストリビューション

> Braze統合により、BrazeメッセージでVoucherifyコードを送信できるようになります。この記事では、Brazeのカスタム属性をVoucherifyの配布で使用する方法について説明します。

{% alert tip %}
Brazeのカスタム属性をVoucherifyの配布で使用する前に、BrazeのユーザーをVoucherifyのダッシュボードに追加する必要があります。Braze Connected Contentを使用して、ユーザーを同期したり、CSVやAPIを通じて顧客をインポートしたりできます。[Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers)について詳しく知るには、[Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers)を訪れてください。
{% endalert %}

Braze のカスタム属性を使用すると、ユーザープロファイルのカスタム属性に Voucherify コードを割り当てることができます。ユニークなクーポン、ギフトカード、ロイヤルティカード、紹介コードを使用できます。まず、VoucherifyをBrazeに接続し、Voucherifyで配布を作成し、最後にBrazeでカスタム属性スニペットをメッセージテンプレートに含めたキャンペーンを作成します。

## ステップ1:BrazeにVoucherifyアカウントを接続する

まず、VoucherifyアカウントをBrazeに接続します。

1. BrazeアカウントからREST APIキーをコピーします。
2. **統合**ディレクトリに移動し、VoucherifyダッシュボードでBrazeを見つけて**接続**を選択します。  
    
    ![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_integrations.png %}){: style="margin-top:15px;margin-left:25px;margin-bottom:15px;"}
    
3. Braze APIキーを貼り付けて、**接続**を選択します。  
    
    ![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_enter_API_key.png %}){: style="max-width:60%;margin-top:15px;margin-left:25px;margin-bottom:15px;"}


## ステップ2:コード配布

接続されると、Brazeのユーザープロファイルのカスタム属性にコードを割り当てる新しいVoucherify [配布](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work)を開始できます。後で、Brazeキャンペーンでコード付きの受信属性を使用できます。

配布を設定する前に、BrazeユーザーをVoucherifyダッシュボードに追加する必要があります。[Voucherify](https://support.voucherify.io/article/67-how-to-import-my-customers)について詳しく知るには、こちらをご覧ください。

![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_distribution.png %})

Brazeにコードを配布するには、2つのモードがあります:

- **手動モード**
- ユーザーのアクションに応じてコード配信をトリガーする**自動化されたワークフロー**を定義します。

手動モードと自動モードの両方で、Voucherifyはユニークなコードをその属性と共に送信し、それらをユーザープロファイルのBrazeカスタム属性に割り当てます。

![Map fields to custom attributes]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_fields_mapping.png %})

{% tabs %}
{% tab Manual distribution %}

マニュアルモードは、選択されたオーディエンスにコードを割り当てる一度限りのアクションです。ダッシュボードの**配布**に移動し、プラスで配布マネージャーを実行し、**手動メッセージ**を選択します。

1.  あなたの配布物に名前を付けてください。

    ![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}<br>  
    
    一意のコードのソースとなるキャンペーンを選択し、ユーザーのセグメントまたは単一の顧客を受信者として選択します **(1)** **(2)**。[}Voucherify{](https://support.voucherify.io/article/51-customer-segments) について詳しく知るには、こちらをご覧ください。  
    
    ![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_name_distribution_choose_segment.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  

2.  次に、マーケティングの許可を追加します。オーディエンスからの許可を収集しない場合は、同意確認を無効にしてください。  
    
    ![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_consents.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
3.  Brazeをチャネルとして選択し、Brazeのユーザープロファイルに追加されるカスタムフィールドをマッピングします。発行されたバウチャーのコードを表すフィールドを追加する必要があります。残りのフィールドはオプションです。  
    
    ![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_channel.png %}){: style="max-width:90%;margin-top:15px;margin-bottom:15px;"}  
    
4.  完了すると、分布の概要を確認できます。**保存して送信**をクリックして、コードをBrazeのユーザープロファイルに配信します。  

_すべての手動配布は10分遅れで送信されることに注意してください。_

{% endtab %}
{% tab Automatic Workflow %}

Voucherifyは、次のトリガーに応じてBrazeにコードを自動的にプッシュできます:

- **顧客が特定のVoucherifyセグメントに出入りしました**
- **コードの公開に成功** – このメッセージは、キャンペーンのコードがVoucherifyの顧客に公開（割り当て）されたときに送信されます。
- **注文ステータスが変更されました**（注文が作成されました、注文が更新されました、注文が支払われました、注文がキャンセルされました）
- **ギフトクレジットが追加されました** – ギフトカードのクレジットが顧客のカードに追加されたときに送信されるメッセージです。
- **ロイヤルティポイントが追加されました** – ロイヤルティポイントが顧客のプロファイルに追加されたときに送信されるメッセージです。
- **バウチャーが引き換えられました** – バウチャーを正常に引き換えた顧客に送信されるメッセージです。
- **バウチャーの償還のロールバック** – 償還が正常にロールバックされた顧客に送信されるメッセージです。
- **報酬の引き換え** – メッセージは、顧客がロイヤルティまたは紹介報酬を引き換えるときに送信されます。
- **カスタムイベントが顧客のために記録されました** \- このメッセージは、Voucherifyが特定のカスタムイベントを記録したときにトリガーされます。

自動ワークフローをBrazeとVoucherifyで設定するには、[配布チュートリアルを訪問してください](https://support.voucherify.io/article/19-how-does-the-distribution-manager-work)。

{% endtab %}
{% endtabs %}

## ステップ3:BrazeキャンペーンでVoucherifyのカスタム属性を使用する

![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_code.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Brazeでコード付きのカスタム属性を顧客のカスタム属性に追加すると、キャンペーンで使用できるようになります。

メッセージ本文を編集し、Voucherify配布で定義されたカスタム属性を追加します。{% raw %}`{{custom_attribute.${custom_attribute_with_code}}}`{% endraw %}を配置して一意のコードを表示します。

![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_body.png %}){: style="max-width:75%;"}

準備ができたら、メッセージプレビューでコードを確認できます。

![\]({% image_buster /assets/img/voucherify/voucherify_custom_attributes_email_preview.png %})
