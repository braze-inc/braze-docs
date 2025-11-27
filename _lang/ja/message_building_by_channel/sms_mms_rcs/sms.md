---
nav_title: "SMS"
article_title: SMSについて
page_order: 13
description: "この記事では、SMS チャネルの全般的なユースケースと、SMS を起動して実行するために必要な条件について説明します。"
page_type: reference
alias: /about_sms/
channel:
  - SMS
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}SMSについて

> この記事では、SMS の統合を支援し、顧客とのコミュニケーションを効果的かつ戦略的に行うために役立つ一般的なユースケース、要件、および用語について説明します。![「Braze へようこそ。弊社の製品をご利用いただきありがとうございます。最初に当社のドキュメントをご覧ください。https:///docs/ ヘルプが必要な場合は SMS で HELP、停止するには STOP と返信してください。」というテキストを含む SMS メッセージ。www.braze.com(]({% image_buster /assets/img/sms/sms_about.png %})){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
ショートメッセージサービスとも呼ばれるSMSは、携帯電話にテキストメッセージを送信するために使用されます。現在、世界中で毎日230億通以上のテキストメッセージが送信されており、SMSはユーザーsや顧客sに到達する最も直接的な方法です。このように幅広く利用され、実証された価値があることから、中小企業はあらゆる規模の企業にとって効果的なマーケティング手段となっている。
<br><br>
## 潜在ユースケースs

| ユースケース | 説明 |
|---|---|
| ジェネラルマーケティング | SMS メッセージは、ダイレクトで柔軟かつ効率的な方法で、今後のお買い得情報、有利なセール情報、現在または将来の販売商品などを顧客に伝えることができます。 |
| リマインダー | SMS は、サービスのアポイントメントを設定したユーザーに通知を送るのに効果的です。例えば、診察予約の前日に SMS でリマインダーメッセージを送ることで、予約ミスを最小限に抑え、お客様と顧客の双方が時間とコストを節約することができます。 |
| トランザクションメッセージ | SMSは、発注確認や発送情報などのアクション的な通知を効率的に発信し、必要な情報を1カ所にまとめてお届けする方法です。トランザクションメッセージを送信する際は、法的なガイドラインに準拠する必要があることに注意してください。これらのガイドラインが不明な場合は、内部の法律事務所にお問い合わせください。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 要件

SMSの送信を開始する前に、いくつか必要なことがあります。詳しくは、次の表を参照してください。

|要件 | 説明 | 取得 |
|---|---|---|
| 専用の電話番号(ショートコードまたはロングコード) | 単一のブランドまたはホストにのみ提供される専用の電話番号。 | Braze がこれらの番号の取得を処理します。詳細については、[ショートコードとロングコード]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/)を参照してください。|
| 電話番号付きユーザー一覧 | メールの送信を始めるには、あらかじめユーザーsを登録しておく必要があります。さらに、オーディエンスのおおよその規模を把握しておく必要があります。  | ユーザは最初、バックエンドを介してBrazeに追加されます。このリストは Braze に提供していただき、弊社がお客様用にアップロードします。電話番号は 10 桁の数字で記述し、国コードも指定します。詳細については、[ユーザーの電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/)を参照してください。 |
| [SMS キーワードと応答]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) | メッセージングを開始する前に、すべての基本キーワードに応答が属性付けられている必要があります。 | これらをリスト化し、オンボーディング中に Braze 担当者またはオンボーディングマネージャーに提供してください。[SMS キーワード テンプレートs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application)を表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 知っておくべき用語

用語の完全なリストについては、SMS [ ご確認ください]({{site.baseurl}}/sms_terms_to_know/)。

