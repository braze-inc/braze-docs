---
nav_title: "SMS サブスクリプショングループ"
article_title: SMS サブスクリプショングループ
page_order: 4
description: "この参考資料では、SMSサブスクリプショングループ、サブスクリプションの状態、およびサブスクリプショングループのセットアッププロセスについて説明します。"
page_type: reference
channel:
  - SMS
  
---

# SMS サブスクリプショングループ

> サブスクリプショングループは、Brazeを通じてSMSやMMSを送信するための基盤です。サブスクリプショングループは、特定のタイプのメッセージング目的のために使用される[送信電話番号][2]（ショートコード、ロングコード、および/または英数字の送信者IDなど）の集まりである。例えば、ブランドがトランザクションとプロモーションの両方のSMSメッセージングを送信する計画がある場合、Brazeダッシュボード内で、送信電話番号の別々のプールを持つ2つのサブスクリプショングループを設定する必要があります。

## SMSの購読状態

SMSユーザーには、`subscribed` と`unsubscribed` の2つの購読状態がある。ユーザーのサブスクリプションの状態は、サブスクリプショングループ間で共有されません。つまり、ユーザーはトランザクションサブスクリプショングループに`subscribed` 、プロモーションサブスクリプショングループに`unsubscribed` 。ブランドにとっては、このように状態を分けることで、ユーザーに適切なSMSメッセージを送り続けることができる。

| 状態｜定義
| --------- | ---------- |
| Subscribed（購読中）｜ユーザーは、特定の購読グループからSMSを受信することを明示的に確認した。ユーザーは、Braze購読APIを通じて購読状態を更新するか、オプトインキーワード応答をテキスト送信することで購読できます。ユーザーがSMSを受信するには、SMS受信グループに登録されていなければならない。|
| 配信停止｜ユーザは、SMSの受信グループおよび受信グループ内の送信電話番号からのメッセージ送信を明示的に停止しました。ユーザーは、オプトアウトキーワード応答をテキストで送信することで配信を停止したり、ブランドが[Braze subscription API][4]を通じてユーザーの配信を停止したりすることができます。SMS購読グループから退会したユーザーは、購読グループに属する送信電話番号からのSMSを受信しなくなります。
{: .reset-td-br-1 .reset-td-br-2}

### ユーザーのSMS購読グループの設定方法 

- **Rest API:**ユーザープロファイルはプログラムによって設定することができます。/subscription/status/set` endpoint][4] by using the Braze REST API.
- **SDKインテグレーション** [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-)、[iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)、または[Web][11]の`addToSubscriptionGroup` メソッドを使用して、EメールまたはSMS購読グループにユーザーを追加できます。
- **ユーザーのオプトイン/オプトアウト時に自動的に処理されます：**ユーザーがデフォルトのオプトインまたはオプトアウト[キーワード][7]をテキスト入力することで、Brazeはユーザーの購読状態を自動的に設定・更新します。
- **ユーザー輸入**：ユーザは、**ユーザをインポートする**ことでEメールまたはSMS購読グループに追加できます。購読グループのステータスを更新する場合、CSV に`subscription_group_id` と`subscription_state` の 2 つのカラムが必要です。詳しくは[ユーザーインポートを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status)参照。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは「**ユーザーインポート**」と呼ばれ、「**ユーザー**」の下にあります。
{% endalert %}

ユーザープロファイルで電話番号が更新されると、新しい電話番号はそのユーザーの契約グループステータスを継承します。電話番号がBrazeに既に存在する番号に更新された場合、その既存の電話番号の契約ステータスが継承されます。

例えば、ユーザーAがいくつかのサブスクリプショングループにサブスクライブしている電話番号を持っていて、その電話番号がユーザーBに追加された場合、ユーザーBは同じサブスクリプショングループにサブスクライブすることになる。ユーザーが既存の購読を継承しないようにするには、ユーザーが番号を変更するたびに、REST APIを介して古い番号の購読グループをリセットすることができます。複数のユーザーがこの電話番号を共有している場合、すべてのユーザーが配信停止になります。

### ユーザーのSMS受信グループを確認する方法

- **ユーザープロフィール:**個々のユーザープロフィールは、Brazeダッシュボードからサイドバーのユーザー検索を選択してアクセスできます。ここでは、電子メールアドレス、電話番号、または外部ユーザーIDによってユーザープロファイルを検索することができます。ユーザープロファイルのEngagementタブで、ユーザーのSMS購読グループを見ることができます。 
- **Rest API:**Braze REST APIを使用し、[List user's subscription groups endpoint][9]または[List user's subscription group status endpoint][8]で、個々のユーザープロファイルの契約グループを確認することができます。 

## 購読グループでの送信

Brazeを通じてSMSキャンペーンを開始するには、以下の画像に示すように、ドロップダウンで購読グループを選択する必要があります。選択されると、キャンペーンまたはキャンバスにオーディエンスフィルターが自動的に追加され、選択された購読グループのユーザー（`subscribed` ）だけがターゲットオーディエンスになるようにします。国際的な[通信コンプライアンスとガイドライン][3]を遵守するため、Brazeは選択された購読グループに加入していないユーザーにSMSを送信することはありません。  

![SMSコンポーザーで、契約グループのドロップダウンを開き、"Messaging Service A for SMS "をユーザーがハイライトした状態][6]。

## セットアッププロセス

SMSオンボーディングプロセスで、Brazeオンボーディングマネージャーがお客様のダッシュボードアカウントにサブスクリプショングループを設定します。必要な購読グループの数を決定し、適切な送信電話番号を購読グループに追加します。購読グループの設定スケジュールは、追加する電話番号の種類によって異なります。例えば、ショートコードの申請には8～12週間かかるが、ロングコードは1日で設定できる。Brazeダッシュボードの設定についてご質問がある場合は、Brazeの担当者にお問い合わせください。  

## サブスクリプション・グループのMMS有効化

MMSメッセージを送信するには、契約グループ内の少なくとも1つの番号がMMS送信を有効にしている必要があります。これは購読グループの隣にあるタグで示される。 

![サブスクリプショングループのドロップダウンで、"メッセージングサービスA for SMS "を強調表示します。エントリーの先頭に "MMS "というタグが付く][10]。{: style="max-width:40%"}


[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]:{{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/
[3]:{{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[4]:{{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]:{{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]:{{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]:{{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
