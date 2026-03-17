---
nav_title: スプリオ
article_title: スプリオ
alias: /partners/splio/
description: "この参考記事では、BrazeとSplioのパートナーシップについて概説している。このパートナーシップにより、よりターゲットを絞ったキャンペーンを送信し、新しい製品機会を見つけ、収益を向上させることができる。"
page_type: partner
search_tag: Partner

---

# スプリオ

> [Splioは](https://splio.com/)、カスタマーエクスペリエンスを損なわずにキャンペーン数を増やし、収益を上げることができるオーディエンス構築ツールであり、オンラインとオフラインの両方でCRMキャンペーンのパフォーマンスを追跡するための分析を提供する。

BrazeとSplioの統合により、より良いCRM戦略を計画・実行し、よりターゲットを絞ったキャンペーンを送り、新しい製品機会を見つけ、収益を上げることができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| スプリオアカウント | この提携にはスプリオのアカウントが必要だ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## データインポート統合

BrazeとSplioを統合するには、Splioプラットフォームを設定し、既存のSplioキャンペーンをエクスポートし、今後のキャンペーンでユーザーをターゲットにするコホートセグメントをBrazeで作成する必要がある。

### ステップ 1: Braze データインポートキーを取得する

Brazeで、「**Partner Integrations**」>「**Technology Partners**」と進み、「**Splio**」を選択する。

RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵を生成した後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。<br><br>![RESTエンドポイントとデータインポートキーが記載されたSplioテクノロジーパートナーのページ。]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

統合を完了するには、データインポートキーとRESTエンドポイントをSplioデータオペレーションチームに提供する。スプリオは接続を確立し、セットアップ完了後にあなたに連絡する。

### ステップ 2:スプリオのプラットフォームからキャンペーンをエクスポートする

BrazeでSplioユーザーのコホートを作成するには、まずSplioプラットフォームからエクスポートする必要がある。

Splioで、エクスポートしたいキャンペーンを選択し、**キャンペーンのエクスポートを**クリックする。エクスポート後、オーディエンスは自動的にBrazeアカウントにアップロードされる。

![Splioプラットフォームからキャンペーンをエクスポートする。]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### ステップ 3:Splioカスタムオーディエンスからセグメンテーションを作成する。

Brazeで**Segmentsに**移動し、Splioコホートセグメントに名前を付け、フィルターとして**Splioコホートを**選択する。ここから、どのスプリオのコホートを含めるかを選択する。Splioコホートセグメントを作成した後、キャンペーンやキャンバスを作成する際にオーディエンスフィルターとして選択することができる。

![BrazeでSplioコホートセグメントを作成する。]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![Brazeセグメントビルダーで、ユーザー属性フィルター「Splioコホート」が「includes」と「Primaryコホート」に設定されている。]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

コーホートの所在がわからず困っている？[トラブルシューティングの](#troubleshooting)セクションを参照してほしい。

{% alert important %}
すでにBrazeに存在するユーザーだけが、コホートに追加または削除される。コホートインポートはBrazeに新しいユーザーを作成しない。
{% endalert %}

## この統合を使う

Splioセグメントを使用するには、Brazeキャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてセグメントを選択する。

![Brazeキャンペーンビルダーのターゲティングステップで、"Target users by segment "フィルターが "Splio cohort "に設定されている。]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## ユーザーマッチング

Brazeは、`external_id` または`alias` によって識別されたユーザーをマッチングする。匿名ユーザーは`device_id` でマッチングされる。元々匿名ユーザーとして作成された識別子ユーザーは、`device_id` ではマッチングできず、`external_id` または`alias` でマッチングしなければならない。

## トラブルシューティング

リストで正しいコホートが見つからない場合は、Splioでキャンペーンの詳細を表示し、**エクスポートファイル名を**チェックして名前を確認する。

![キャンペーン詳細ページの下部にコホート名が表示されている。]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

オーディエンスの検索に問題がある場合は、[スプリオ・チームに](mailto:support-team@splio.com)連絡してサポートを受けてほしい。