---
nav_title: Komo
article_title: Komo
description: "この参考記事では、BrazeとKomoの提携について説明しています。Komoは、ゲーミフィケーション、インタラクティブコンテンツ、コンペティション、賞品、ロイヤルティを専門とするカスタマーエンゲージメントプラットフォームです。この統合を通じて、Komoで収集されたファーストパーティおよびゼロパーティデータはBrazeに公開できます。"
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo][7] は、ゲーミフィケーション、インタラクティブコンテンツ、試合、賞品、ロイヤルティに特化したカスタマーエンゲージメントプラットフォームです。

_この統合は Komo によって管理されます。_

## 統合について

Braze と Komo の統合により、Komo Engagment Hub を通じてファーストパーティデータとゼロパーティデータを収集できます。これらのハブは、インタラクティブなコンテンツとゲーミフィケーション機能を提供するダイナミックなマイクロサイトです。これらのハブから収集されたユーザーデータは、Braze APIに送信されます。

- KomoからBrazeにリアルタイムで収集されたファーストパーティおよびゼロパーティのユーザーデータを取り込む
- アンケート、投票、クイズの質問に回答する際に、市場調査およびユーザーの好みのデータを取り込みます。
- ユーザーが引き続きエンゲージし、ユーザー自身に関するデータをさらに共有するにつれて、Braze でユーザープロファイルを徐々に作成します。
- Brazeを通じて送信されるトランザクションメールの外観と感触を標準化する

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Komo アカウント | このパートナーシップを利用するには、アクティブなKomoアカウントが必要です。[Komo][7] を訪れて、今すぐトライアルを開始してください。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][1]。エンドポイントは、インスタンスのBraze URLに依存する。<br><br>たとえば、https://rest.iad-03.braze.com のようになります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ユースケース

{% tabs local %}
{% tab データキャプチャ (フォーム送信) %}

ユーザーが Komo でカスタマイズ可能なデータキャプチャフォームを送信すると、Braze 統合でマッピングされている Komo のフィールドが、`/users/track/` API 呼び出しを介して Braze に渡されます。

データキャプチャフォームは、カードの開始時または終了時のいずれかに存在します。

{% endtab %}
{% tab マーケター・リサーチ - 近日公開予定 %}

Komo は近々、ユーザーがクイズの質問、投票、性格診断、スワイパーなどに回答したときにキャプチャされる市場調査データをパススルーする機能を追加する予定です。このデータにより、フォーム送信でキャプチャしたデータを超えて、ユーザーのプロファイルを強化することができます。

{% endtab %}
{% endtabs %}

## 統合

### ステップ1:Komoエンゲージメントハブとカードを公開する

データキャプチャフォームを含む1つ以上のカードでKomo Engagement Hub を公開する必要があります。公開されると、ユーザーエクスペリエンスをエンドツーエンドでテストし、統合が正しく機能していることを確認できます。

![][2]

### ステップ2:Brazeインテグレーションを追加

Komoでは、**ハブ設定**タブに移動し、**統合**セクションを選択します。次に、リストからBraze統合を見つけて、**接続**ボタンを選択して統合を有効にします。

![][3]

![][4]

#### ユーザーのマッピングを構成する

最初に設定する必要があるのは、Komo でキャプチャされたユーザーを Braze 内のユーザーにどのようにマッピングするかです。Komo 内のフィールドで `braze_id` または `external_id` をキャプチャする場合は、適切なキーを選択できます。それ以外の場合は、最も一般的なオプションを選択します。これは、メールまたは電話のユーザーエイリアスになります。

![][5]{: style="max-width:65%;"}

次に、KomoフィールドをBraze属性に転送するためのマップを定義する必要があります。Komoは大量のデータをキャプチャするため、Braze統合でマッピングされたフィールドのみがBrazeに送信されます。

![][6]{: style="max-width:65%;"}

最後に、API キーとRESTエンドポイントURLを追加し、**保存**をクリックして統合を有効にします。

## 統合を使用する

統合が完了すると、Brazeに送信されたKomoデータを使用してターゲティングのためのセグメントを作成できます。


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/komo/komo_hub_publish.png %}
[3]: {% image_buster /assets/img/komo/komo_hub_settings_integrations.png %}
[4]: {% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %}
[5]: {% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}
[6]: {% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}
[7]: https://komo.tech/