---
nav_title: "SMS購読グループ"
article_title: SMS購読グループ
page_order: 4
description: "この参考文献は、SMSのサブスクリプショングループ、サブスクリプションの状態、およびサブスクリプショングループのセットアッププロセスについて説明している。"
page_type: reference
channel:
  - SMS
  
---

# SMS購読グループ

> サブスクリプショングループは、Brazeを通じてSMSやMMSを送信するための基盤である。サブスクリプショングループは、\[ショートコード、ロングコード、および/または英数字の送信者IDのような送信電話番号][2] ]のコレクションであり、特定のタイプのメッセージング目的のために使用される。例えば、ブランドがトランザクションとプロモーションの両方のSMSメッセージングを送信する計画がある場合、Brazeダッシュボード内で、送信電話番号の別々のプールを持つ2つのサブスクリプショングループを設定する必要がある。

## SMSの購読状態

SMSユーザーには、`subscribed` と`unsubscribed` の2つの購読状態がある。ユーザーのサブスクリプションの状態は、サブスクリプショングループ間で共有されない。つまり、ユーザーはトランザクションサブスクリプショングループに`subscribed` 、プロモーションサブスクリプショングループに`unsubscribed` 。ブランドにとって、このような状態の分離は、ユーザーに適切なSMSメッセージを送り続けることを保証する。

| 状態 | 定義 |
| --------- | ---------- |
| サブスクリプション登録済み | ユーザーは、特定の購読グループからSMSを受信したいことを明示的に確認した。ユーザーは、Braze購読APIを通じて購読状態を更新させるか、オプトインキーワード応答をテキスト送信することで購読することができる。ユーザーがSMSを受信するには、SMS受信グループに登録されていなければならない。 |
| 配信停止済み | ユーザーが、SMS受信グループおよび受信グループ内の送信電話番号からのメッセージ送信を明示的にオプトアウトした。ユーザーは、オプトアウトキーワードをテキストで送信することで購読を解除することができる。また、ブランドは、\[Braze subscription API][4].SMS購読グループから登録解除されたユーザーは、その購読グループに属する送信電話番号からのSMSを受信しなくなる。|
{: .reset-td-br-1 .reset-td-br-2}

### ユーザーのSMS購読グループはどのように設定されるか 

- **Rest API:**ユーザープロファイルは、Braze REST APIを使用して、\[`/subscription/status/set` エンドポイント][4] からプログラムで設定できる。
- **SDKインテグレーション** [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-)、[iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)、または\[Web][11]]の`addToSubscriptionGroup` メソッドを使用して、ユーザーをEメールまたはSMS購読グループに追加できる。
- **ユーザーのオプトイン/オプトアウト時に自動的に処理される：**ユーザーがデフォルトのオプトインまたはオプトアウト\[キーワード][7]]をテキスト入力することで、Brazeはユーザーの購読状態を自動的に設定・更新する。
- **ユーザー輸入**：ユーザは、**Import Users（ユーザのインポート**）により、EメールまたはSMS購読グループに追加することができる。サブスクリプション・グループのステータスを更新する場合、CSVに次の2つのカラムが必要である：`subscription_group_id` と`subscription_state` 。詳しくは[ユーザーインポートを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status)参照のこと。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは**ユーザーインポートと**呼ばれ、**ユーザーの**下にある。
{% endalert %}

ユーザープロファイルで電話番号が更新されると、新しい電話番号はそのユーザーの契約グループステータスを継承する。電話番号がBrazeに既に存在する番号に更新された場合、その既存の電話番号の契約ステータスが継承される。

例えば、ユーザーAが複数のサブスクリプショングループにサブスクライブしてい る電話番号を持っていて、その電話番号がユーザーBに追加された場合、ユーザーB は同じサブスクリプショングループにサブスクライブすることになる。ユーザーが既存のサブスクリプションを継承しないようにするには、ユーザーが番号を変更するたびに、REST APIを介して古い番号のサブスクリプショングループをリセットすることができる。複数のユーザーがこの電話番号を共有している場合、その全員が登録解除される。

### ユーザーのSMS購読グループを確認する方法

- **ユーザープロフィール:**個々のユーザープロフィールは、Brazeダッシュボードからサイドバーのユーザー検索を選択してアクセスできる。ここでは、電子メールアドレス、電話番号、外部ユーザーIDでユーザープロファイルを検索できる。ユーザー・プロフィールのEngagementタブで、ユーザーのSMS購読グループを見ることができる。 
- **Rest API:**個々のユーザープロファイル購読グループは、Braze REST APIを使用して、\[List user's subscription groups endpoint][9] ]または\[List user's subscription group status endpoint][8] ]で確認できる。 

## 購読グループで送信する

Brazeを通じてSMSキャンペーンを開始するには、次の画像に示すように、ドロップダウンで購読グループを選択する必要がある。選択されると、キャンペーンまたはキャンバスにオーディエンスフィルターが自動的に追加され、選択された購読グループに属するユーザー（`subscribed` ）だけがターゲットオーディエンスになる。国際的な\[通信コンプライアンスとガイドライン]][3] を遵守するため、Brazeは選択した購読グループに加入していないユーザーにSMSを送信することはない。  

![SMSコンポーザーで、サブスクリプション・グループのドロップダウンを開き、"Messaging Service A for SMS "を強調表示する。][6]

## セットアッププロセス

SMSオンボーディングプロセスで、Brazeオンボーディングマネージャーがダッシュボードアカウントにサブスクリプショングループを設定する。必要な購読グループの数を決定し、適切な送信電話番号を購読グループに追加する。サブスクリプショングループのセットアップにかかる時間は、追加する電話番号のタイプによって異なる。例えば、ショートコードの申請には8～12週間かかるが、ロングコードは1日で設定できる。Brazeダッシュボードの設定について質問がある場合は、Brazeの担当者に連絡してサポートを受ける。  

## サブスクリプション・グループのMMS有効化

MMSメッセージを送信するには、契約グループ内の少なくとも1つの番号がMMSを送信できるようになっていなければならない。これは購読グループの隣にあるタグで示される。 

![サブスクリプション・グループのドロップダウンで、"メッセージング・サービスA for SMS "をハイライトする。エントリーの先頭に "MMS "というタグが付く。][10]{: style="max-width:40%"}


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
