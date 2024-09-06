---
nav_title: "SMSについて"
article_title: SMSについて
page_order: 1
description: "このリファレンス記事では、SMS チャネルの全般的なユースケースと、SMSを起動して実行するために必要な条件について説明します。"
page_type: reference
channel:
  - SMS
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}SMSについて

> この記事では、SMSの統合を支援し、顧客s.![SMSメッセージとテキスト"Brazeへようこそ!と効果的かつ戦略的なコミュニケーションを可能にすることを知るために、要件、条件から引き出すいくつかの一般的なユースケースを共有しています。私たちはあなたが乗船することに興奮しています。開始するには、私たちのドキュメントを確認してください。https://www.braze.com/docs/ ヘルプのためのテキストHELPと、停止するためのSTOP."]\[ピクチャ]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
ショートメッセージサービスとも呼ばれるSMSは、携帯電話にテキストメッセージを送信するために使用されます。現在、世界中で毎日230億通以上のテキストメッセージが送信されており、SMSはユーザーsや顧客sに到達する最も直接的な方法です。このように幅広く利用され、実証された価値があることから、中小企業はあらゆる規模の企業にとって効果的なマーケティング手段となっている。
<br><br>
## 潜在ユースケースs

| ユースケース | 説明 |
|---|---|
| ジェネラルマーケティング | SMSメッセージは、今後の取引、好調な販売、現在または将来の商品を顧客に伝えるための、直接的で柔軟かつ効率的な方法です。 |
| 注意事項 | SMSは、サービスのアプリを設定したユーザーに通知するのに効果的です。例えば、顧客にアプリ用軟膏の前日に注意を促すSMSを送ることで、あなたと顧客の時間と費用を節約して、見落とされたアプリ用軟膏を最小限に抑えることができます。 |
| 全件送信アクション | SMSは、発注確認や発送情報などのアクション的な通知を効率的に発信し、必要な情報を1カ所にまとめてお届けする方法です。Trans アクション al Messages を送信する際に守るべき法的な指針があることに注意してください。これらの指針がわからない場合は、内部の法務部に連絡してください。|
{: .reset-td-br-1 .reset-td-br-2}

## 要件

SMSの送信を開始する前に、いくつか必要なことがあります。詳しくは、次の表を参照してください。

|要件 | 説明 | 取得 |
|---|---|---|
| 専用の電話番号(ショートコードまたはロングコード) | 単一のブランドまたはホストにのみ提供される専用の電話番号。 | Brazeは、これらの数値の取得を処理します。[short とlong コード s]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/) について詳しく説明します。|
| 電話番号付きユーザー一覧 | メールの送信を始めるには、あらかじめユーザーsを登録しておく必要があります。さらに、オーディエンスの最大アプリ容量を知っておく必要があります。  | ユーザは最初、バックエンドを介してBrazeに追加されます。あなたはこの一覧を私たちにあなたのためにアップロードに渡さなければなりません。電話番号は、国名コードと同様に、10桁の数字でフォーマットする必要があります。[ユーザーの電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/)について詳しく知りたい。 |
| [SMSキーワードとレスポンス]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | メッセージングを開始するには、すべての基本キーワードsに属性dのレスポンスが必要です | これらを記載し、オンボーディング中にBraze担当者またはオンボーディング マネージャーに送付してください。[SMS キーワード テンプレートs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application)を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 知っておくべき用語

- **短いコード:**5～6桁のコードで、完全な電話番号より短い。このコードは、SMSのアドレス指定と送信に使用されます。<br><br>
- **長いコードs:**10桁のコードで、SMSの宛先として使用されます。ほとんどの平均的な電話番号は長いコードs と見なされます(e.g 123-456-7891)。これらのコードは、SMSのアドレス指定と送信に使用されます。<br><br>
- **サブスクリプショングループ:**特定の種類のメッセージングに使用される、送信電話番号(短いコードs、長いコードs、英数字の送信者IDなど)の集まり。たとえば、ブランドがトランスアクションal とプロモーションSMS メッセージングの両方を送信する予定がある場合、電話番号を送信する別々のプールを持つ2 つのサブスクリプショングループをBraze ダッシュボード内に設定する必要があります。<br><br>
- **メールSegmentと文字数制限:**メッセージSegmentとは、最初のSMSメッセージを分割するSegmentの数のことです。それぞれのメッセージには文字制限があり、それを超えるとメッセージはSegments に分割されます。使用するエンコード標準(UTF-2 またはGSM-7) に基づいて、さまざまな文字制限があります。メッセージング セグメンテーションとメッセージ文字の制限の詳細については、\[message copy limits][2] を参照してください。<br><br>
- **一般的なSMS キャンペーンメトリクス:**<br>*送信済み*、*キャリアに送信*、*配信失敗*、*確認済み配信*、*拒否*、*Opt-Out*、*ヘルプ*。<br>これらのメトリクスについては、\[SMS レポート ing][1]を参照してください。*キャリアへの送信*は非推奨ですが、すでに存在するユーザーでは引き続きサポートされます。

<br><br>

用語の完全なリストについては、SMS [ ご確認ください]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/terms/)。

\[picture]: {% image_buster /assets/img/sms/sms_about.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy
