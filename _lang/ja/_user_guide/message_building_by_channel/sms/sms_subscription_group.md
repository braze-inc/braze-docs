---
nav_title: "SMS 購読グループ"
article_title: SMS 購読グループ
page_order: 4
description: "この参考文献は、SMSのサブスクリプショングループ、サブスクリプションの状態、およびサブスクリプショングループのセットアッププロセスについて説明している。"
page_type: reference
channel:
  - SMS
  
---

# SMS 購読グループ

> サブスクリプショングループは、Brazeを通じてSMSやMMSを送信するための基盤である。購読グループは、特定の種類のメッセージング目的で使用される[送信側の電話番号][2] (ショートコード、ロングコード、英数字の送信者 ID) のコレクションです。例えば、ブランドがトランザクションとプロモーションの両方のSMSメッセージングを送信する計画がある場合、Brazeダッシュボード内で、送信電話番号の別々のプールを持つ2つのサブスクリプショングループを設定する必要がある。

## SMS の購読状態

SMS ユーザーには、`subscribed` と`unsubscribed` の 2 つの購読状態があります。ユーザーの購読状態は購読グループ間で共有されません。つまり、あるユーザーはトランザクション購読グループでは `subscribed` で、プロモーション購読グループでは `unsubscribed` になることがあります。ブランドにとって、このような状態の分離は、ユーザーに適切なSMSメッセージを送り続けることを保証する。

| 状態 | 定義 |
| --------- | ---------- |
| サブスクリプション登録済み | ユーザーが、特定の購読グループから SMS を受信する意志を明示的に示しました。ユーザーは、Braze の購読 API を介して購読状態を更新するか、オプトインのキーワード応答テキストを送信することで、購読に登録できます。ユーザーがSMSを受信するには、SMS受信グループに登録されていなければならない。 |
| 配信停止済み | ユーザーが、SMS受信グループおよび受信グループ内の送信電話番号からのメッセージ送信を明示的にオプトアウトした。ユーザーはオプトアウトのキーワード応答テキストを送信することで購読解除できます。また、ブランドは [Braze の購読 API][4] を通じてユーザーを購読解除できます。SMS購読グループから登録解除されたユーザーは、その購読グループに属する送信電話番号からのSMSを受信しなくなる。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ユーザーのSMS購読グループはどのように設定されるか 

- **Rest API:**Braze REST API を使用することで、ユーザープロファイルは[`/subscription/status/set` エンドポイント][4] によってプログラムで設定できます。
- **SDKインテグレーション** [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:))、または[Web][11]]の`addToSubscriptionGroup` メソッドを使用して、ユーザーをEメールまたはSMS購読グループに追加できる。
- **ユーザーのオプトイン / オプトアウト時に自動的に処理される:**ユーザーがデフォルトのオプトインまたはオプトアウト[キーワード][7]]をテキスト入力することで、Brazeはユーザーの購読状態を自動的に設定・更新する。
- **ユーザー輸入**：ユーザは、**Import Users（ユーザのインポート**）により、EメールまたはSMS購読グループに追加することができる。購読グループのステータスを更新する場合、CSV には `subscription_group_id` と `subscription_state` の2 列が必要です。詳細については、[ユーザーインポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status)を参照してください。

ユーザープロファイルで電話番号が更新されると、新しい電話番号はそのユーザーの契約グループステータスを継承する。電話番号が Braze に既に存在する番号に更新された場合、その既存の電話番号の購読ステータスが継承されます。

例えば、ユーザー A の電話番号が複数の購読グループに登録されていて、その電話番号がユーザー B に追加された場合、ユーザー B は同じ購読グループに登録されます。ユーザーによる既存の購読の継承を防ぐには、ユーザーが番号を変更するたびに、REST API を使用して古い番号の購読グループをリセットします。複数のユーザーがこの電話番号を共有している場合、その全員が登録解除される。

### ユーザーの SMS 購読グループを確認する方法

- **ユーザープロフィール:**Braze ダッシュボードのサイドバーにある [ユーザー検索] を使用して、個々のユーザープロファイルにアクセスできます。ここでは、電子メールアドレス、電話番号、外部ユーザーIDでユーザープロファイルを検索できる。ユーザープロファイルの [エンゲージメント] タブに、ユーザーの SMS 購読グループが表示されます。 
- **Rest API:**Braze REST API を使用することで、[ユーザーの購読グループをリストするエンドポイント][9]または[ユーザーの購読グループのステータスをリストするエンドポイント][8]で、個々のユーザープロファイルの購読グループを確認できます。 

## 購読グループを使用する送信

Braze 経由で SMS キャンペーンを開始するには、次の画像に示すように、ドロップダウンで購読グループを選択する必要があります。購読グループを選択すると、オーディエンスフィルターがキャンペーンまたはキャンバスに自動的に追加され、選択した購読グループを購読している (`subscribed`) ユーザーのみが確実にターゲットオーディエンスに含まれます。国際的な[通信コンプライアンスとガイドライン]][3] を遵守するため、Brazeは選択した購読グループに加入していないユーザーにSMSを送信することはない。  

![ユーザーが購読グループのドロップダウンを開き、[Messaging Service A for SMS] を強調表示した SMS 作成画面。][6]

## セットアッププロセス

お客様の SMS オンボーディングプロセスで、Braze のオンボーディングマネージャーがお客様のダッシュボードアカウントに購読グループを設定します。お客様に協力して、必要な購読グループの数を決定し、適切な送信電話番号を購読グループに追加します。サブスクリプショングループのセットアップにかかる時間は、追加する電話番号のタイプによって異なる。例えば、ショートコードの申請には8～12週間かかるが、ロングコードは1日で設定できる。Brazeダッシュボードの設定について質問がある場合は、Brazeの担当者に連絡してサポートを受ける。  

## サブスクリプション・グループのMMS有効化

MMS メッセージを送信するには、購読グループ内の少なくとも 1 つの番号で MMS の送信を有効にする必要があります。これは、購読グループの横にあるタグによって示されます。 

![[Messaging Service A for SMS] が強調表示された購読グループのドロップダウン。エントリーの先頭に "MMS "というタグが付く。][10]{: style="max-width:40%"}


[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
