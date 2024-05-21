---
nav_title: "SMSについて"
article_title: SMSについて
page_order: 1
description: "この参考記事では、SMSチャネルの一般的な使用例と、SMSを稼働させるために必要な要件について説明します。"
page_type: reference
channel:
  - SMS
search_rank: 2
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}SMSについて

> この記事では、SMSの統合を支援し、顧客と効果的かつ戦略的なコミュニケーションを可能にする、一般的なユースケース、要件、および用語を紹介します！あなたの加入を心待ちにしています。まずはドキュメントをご覧ください：//www.braze.com/docs/ Text HELP for help and STOP to stop."][picture]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
SMSはショート・メッセージ・サービスとも呼ばれ、携帯電話にテキスト・メッセージを送信するために使われる。現在、世界中で毎日230億通以上のテキストメッセージが送信されており、SMSはユーザーや顧客に到達する最も直接的な方法である。このように広く利用され、その価値が証明されているため、SMSはあらゆる規模の企業にとって効果的なマーケティングツールとなっている。
<br><br>
## 想定される使用例

| ユースケース
|---|---|
| 一般的なマーケティング｜SMSメッセージは、ダイレクトでフレキシブル、そして効率的な方法です。|
| リマインダー｜SMSメッセージは、サービスのアポイントメントを設定したユーザーに通知するのに効果的です。例えば、医者の予約の前日にSMSでリマインドメッセージを送れば、予約の取り逃しを最小限に抑えることができ、貴社も顧客も時間とお金の節約になります。|
| 取引メッセージ｜SMSメッセージは、注文確認や発送情報などの取引通知を送信する効率的な方法であり、必要な情報を1つの便利な場所で提供します。Transactional Messagesを送信する際には、遵守しなければならない法的ガイドラインが存在することに注意してください。これらのガイドラインが不明な場合は、社内の法務チームに問い合わせてください。
{: .reset-td-br-1 .reset-td-br-2}

## 要件

SMSの送信を始める前に、必要なものがいくつかあります。詳しくは以下の表を参照。

|必要条件｜説明｜取得
|---|---|---|
| 専用電話番号（ショートコードまたはロングコード）｜単一のブランドまたはホストのみに提供される専用電話番号です。| 電話番号の取得はBrazeにお任せください。[ショートコードとロング]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/)コードについて詳しくはこちら。
| ユーザーリスト（電話番号付き）｜メッセージの送信を開始する前に、アカウントにユーザーを追加する必要があります。さらに、オーディエンスのおおよその規模を知っておく必要があります。  | Brazeのバックエンドからユーザーを追加します。このリストを私たちに渡してアップロードしてもらう必要があります。電話番号は、10桁の数字と国別の市外局番でフォーマットする必要があります。[ユーザー電話番号について]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/)詳しくはこちら|
[| SMSのキーワードとレスポンス]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/)｜すべての基本キーワードには、メッセージングを開始する前にレスポンスが必要です。[SMSキーワードテンプレートを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application)見る|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 知っておきたい用語

- **ショートコード：**5～6桁のコードで、完全な電話番号よりも短い。このコードは、SMSメッセージの宛先と送信に使用される。<br><br>
- **ロングコード：**SMSメッセージの宛先に使用される10桁のコード。ほとんどの平均的な電話番号はロングコードとみなされます（例：123-456-7891）。これらのコードは、SMSメッセージの宛先と送信に使用される。<br><br>
- サブスクリプショングループ特定のタイプのメッセージング目的で使用される送信電話番号（ショートコード、ロングコード、英数字の送信者IDなど）のコレクション。例えば、ブランドがトランザクションとプロモーションの両方のSMSメッセージングを送信する計画がある場合、Brazeダッシュボード内で、送信電話番号の別々のプールを持つ2つのサブスクリプショングループを設定する必要があります。<br><br>
- **メッセージセグメントと文字数の制限：**メッセージセグメントとは、最初のSMSメッセージをいくつのセグメントに分けるかを意味します。各メッセージには文字数制限があり、それを超えるとメッセージが分割される。使用するエンコーディング規格（UTF-2またはGSM-7）に応じて、文字数の制限が異なります。メッセージのセグメンテーションとメッセージの文字数制限の詳細については、[メッセージのコピー制限][2]を参照してください。<br><br>
- **一般的なSMSキャンペーンの指標**<br>*送信済み*]、[*キャリアに送信済み*]、[*配信失敗*]、[*配信確認済み*]、[*拒否*]、[*オプトアウト]*、[*ヘルプ*]。<br>これらの指標については、[SMS reporting][1]を参照のこと。*キャリアへの送信は*非推奨ですが、すでに持っているユーザーには引き続きサポートされます。

<br><br>

用語の詳細については、SMS[用語]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/terms/)集をご覧ください。

[写真]： {% image_buster /assets/img/sms/sms_about.png %}
[1]:{{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]:{{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy
