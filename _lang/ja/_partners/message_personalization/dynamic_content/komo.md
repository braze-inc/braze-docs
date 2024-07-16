---
nav_title: Komo
article_title:コモ
description:"この参考記事では、ゲーミケーション、インタラクティブコンテンツ、コンペティション、賞品、ロイヤルティを専門とするカスタマーエンゲージメントプラットフォームであるKomoとBrazeのパートナーシップについて概説している。この統合により、Komoに取り込まれたファーストパーティとゼロパーティのデータをBrazeに公開することができる。
alias: /partners/komo/
page_type: partner
search_tag:Partner

---

# コモ

> \[Komo][7] は、ゲーミフィケーション、インタラクティブ・コンテンツ、コンペティション、プライズ、ロイヤリティに特化したカスタマーエンゲージメントプラットフォームである。

BrazeとKomoの統合により、Komo Engagement Hubsを通じてファーストパーティとゼロパーティのデータを収集することができる。これらのハブは、インタラクティブなコンテンツやゲーミフィケーション機能を提供するダイナミックなマイクロサイトである。これらのハブから収集されたユーザーデータは、Braze APIに送信される。

- KomoからBrazeに収集されたファーストパーティおよびゼロパーティのユーザーデータをリアルタイムで取り込む。
- ユーザーがアンケートや投票、クイズに回答する際に、マーケットリサーチやユーザー嗜好のデータを取り込む。
- ユーザーがエンゲージメントを継続し、ユーザーに関するデータを共有するにつれて、Brazeにユーザープロファイルを徐々に構築していく
- Brazeを通じて送信されるトランザクションメールのルック＆フィールを標準化する。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| 小桃アカウント | このパートナーシップを利用するには、アクティブなKomoアカウントが必要だ。Komo][7] 、今すぐトライアルを開始しよう。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][1]。エンドポイントはインスタンスのBraze URLに依存する。<br><br>例えば、次のようなものだ： https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## ユースケース

{% tabs local %}
{% tab Data Capture (Form Submission) %}

ユーザーがKomoでカスタマイズ可能なデータ取得フォームを送信すると、Braze統合でマッピングされたKomoフィールドが、`/users/track/` APIコールを介してBrazeに渡される。

データ収集フォームは、カードの開始時または終了時に存在する。

{% endtab %}
{% tab Market Research (Coming soon) %}

近々、Komoは、ユーザーがクイズの質問、投票、性格テスト、スワイパーなどに答えたときに取得したマーケットリサーチデータを渡す機能を追加する予定だ。このデータにより、フォーム送信で取得したデータ以上にユーザープロファイルを強化することができる。

{% endtab %}
{% endtabs %}

## 統合

### ステップ1:Komoエンゲージメント・ハブとカードを発行する

データ収集フォームを含む少なくとも1つのカードを持つKomoエンゲージメント・ハブを発行する必要がある。公開されたら、エンドツーエンドのユーザー体験をテストし、統合が正しく機能していることを確認できる。

![][2]

### ステップ2:Brazeとの統合を追加する

Komoで、**Hub Settings**タブに行き、**Integrations**セクションを選択する。次に、リストからBrazeインテグレーションを見つけ、**Connect**ボタンを選択してインテグレーションをイネーブルメントにする。

![][3]

![][4]

#### ユーザーマッピングを設定する

最初に設定する必要があるのは、KomoでキャプチャしたユーザーをBrazeのユーザーにマッピングする方法だ。Komo内のフィールドで`braze_id` または`external_id` をキャプチャしている場合は、適切なキーを選択できる。そうでない場合は、最も一般的なオプションとして、メールまたは電話のユーザーエイリアスを選択する。

![][5]{: style="max-width:65%;"}

次に、Braze属性に転送したいKomoフィールドのマップを定義する必要がある。Komoは大量のデータをキャプチャするので、Braze統合でマッピングされたフィールドだけがBrazeに送信される。

![][6]{: style="max-width:65%;"}

最後に、APIキーとRESTエンドポイントURLを追加し、**保存を**クリックしてイネーブルメントを有効にする。

## 統合を利用する

統合が完了したら、Brazeに送られたKomoのデータを使って、ターゲティングのためのセグメンテーションを作成できる。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/komo/komo_hub_publish.png %}
[3]: {% image_buster /assets/img/komo/komo_hub_settings_integrations.png %}
[4]: {% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %}
[5]: {% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}
[6]: {% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}
[7]: https://komo.tech/