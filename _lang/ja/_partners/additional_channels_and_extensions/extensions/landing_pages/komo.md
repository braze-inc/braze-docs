---
nav_title: Komo
article_title: Komo
description: "この参考記事では、BrazeとKomoの提携について説明しています。Komoは、ゲーミフィケーション、インタラクティブコンテンツ、コンペティション、賞品、ロイヤルティを専門とするカスタマーエンゲージメントプラットフォームです。この統合を通じて、Komoで収集されたファーストパーティおよびゼロパーティデータはBrazeに公開できます。"
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) は、ゲーミフィケーション、インタラクティブコンテンツ、試合、賞品、ロイヤルティに特化したカスタマーエンゲージメントプラットフォームです。

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
| Komo アカウント | このパートナーシップを利用するには、アクティブなKomoアカウントが必要です。[Komo](https://komo.tech/) にアクセスして、今すぐトライアルを開始してください。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。<br><br>たとえば、https://rest.iad-03.braze.com のようになります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ユースケース

{% tabs local %}
{% tab Data Capture - Form Submission %}

ユーザーが Komo でカスタマイズ可能なデータキャプチャフォームを送信すると、Braze 統合でマッピングされている Komo のフィールドが、`/users/track/` API 呼び出しを介して Braze に渡されます。

データキャプチャフォームは、カードの開始時または終了時のいずれかに存在します。

{% endtab %}
{% tab Market Research - Coming soon %}

Komoはまた、ユーザーがクイズの質問、投票、パーソナリティテスト、スワイパーなどに回答したときに取得したマーケットリサーチデータを渡すこともできる。このデータにより、フォーム送信でキャプチャしたデータを超えて、ユーザーのプロファイルを強化することができます。

{% endtab %}
{% endtabs %}

## 統合

### ステップ1:Komoエンゲージメントハブとカードを公開する

データキャプチャフォームを含む少なくとも1枚のカードを持つKomo Hubを発行する必要がある。公開されると、ユーザーエクスペリエンスをエンドツーエンドでテストし、統合が正しく機能していることを確認できます。

![コモ・ハブ]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### ステップ 2:Braze Connectedアプリを追加する 

Komoの「**Company Settings」**タブで「**Connected Apps**」セクションを選択する。 

次に、リストからBraze統合を見つけて、**接続**ボタンを選択して統合を有効にします。

![Brazeの統合を接続する。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Brazeインテグレーション・ステップ2bを接続する。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### ワークフローで統合を構成する

ワークスペース、サイト、カード内で、Brazeにデータを同期するワークフローを設定する必要がある。 

ワークスペース全体、サイト（多くのカードを含む）、または単一のカードのいずれをワークフローのスコープとするかは、ワークフローを多くのカードまたはキャンペーンのいずれにトリガーさせたいかによる。 

ワークフローを作成後、トリガーを定義し、ステップメニューでBrazeを検索し、「ユーザーを追跡」ステップを追加する。 

![トラッキングユーザーの設定。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

ここから、KomoからBrazeに同期させたいイベント、アトリビューション、サブスクリプションを設定する。 

![Content blocks list.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## 統合の使用

これで統合は完了し、ワークフロー実行タブで各実行をモニターできる。 
