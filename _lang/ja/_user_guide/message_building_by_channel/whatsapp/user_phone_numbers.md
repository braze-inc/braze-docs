---
nav_title: "ユーザーの電話番号"
article_title: WhatsApp ユーザーの電話番号
page_order: 1.5
description: "この記事では、WhatsApp 電話番号のフォーマット、電話番号のインポート方法、および WhatsApp サブスクリプショングループにユーザーを追加する方法について説明します。"
page_type: reference
channel: 
  - WhatsApp
  
---

# ユーザーの電話番号

> この記事では、ユーザーや顧客の電話番号に関するさまざまなトピックについて説明します。

電話番号はローカル形式でユーザープロファイルに表示されますが、番号の読み込みに使用する形式では表示されません(`(724) 123 4567`)。

## 電話番号のインポート

[CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) または [API]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) 経由でアップロードしてユーザーを作成する方法で、電話番号をインポートできます。

### フォーマット

[`E.164`](https://en.wikipedia.org/wiki/e.164) 形式のU.S以外の数値を、"+" とカントリーコードを含めて読み込むことが大切です。この形式で指定されていない電話番号は、US 番号として解釈されます。  

電話番号が強制的にE.164形式に変換され、検証に合格しない場合、Brazeはこの番号にWhatsAppを送信できません。フォーマット可能でない電話番号を持つユーザーは、WhatsApp を含むキャンバスステップを自動的に終了します。

すべてのU.S. 番号は有効で、有効な市外コードのある10 桁の電話番号である必要があります。`+` とカントリーコードを指定せずに入力できます。Braze はすべての有効な10 桁の電話番号をU.S. 番号としてマッピングします。

すべての国際番号は、`+` で始まり、その後に国別コードと電話番号が続きます(e.g `+442071838750`)。

![][picture]{: style="max-width:50%;border: 0;"}

ただし、国コードや市外局番が異なる複数の地域に送信する場合は、`E.164` 形式を使用することをお勧めします。これは米国ベースの電話番号でも同様です。

次の表では、ローカル数値フォーマットとユニバーサル、`E.164` フォーマットの違いを確認できます。

| 国 | ローカル | 国コード | `E.164` |
|---|---|---|---|
| アメリカ合衆国 | `4155552671` | 1 | `+14155552671` |
| 英国 | `02071838750` | 44 | `+442071838750` |
| ブラジル | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

### サブスクリプショングループをWhatsAppするためのユーザーの追加

顧客が WhatsApp メッセージを受信するには、有効な電話番号を持っていて、購読グループにオプトインしている必要があります。詳細については、[WhatsApp 購読グループ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)を参照してください。


### 同じ電話番号を持つ複数のユーザー

複数のユーザーが1 つのキャンペーンまたはキャンバスステップのSegment内で同じ電話番号を持つ場合、Braze は送信を重複排除し、その1 つの電話番号に1 つのメッセージのみを送信します。 

[picture]: {% image_buster /assets/img/sms/e164.png %}

