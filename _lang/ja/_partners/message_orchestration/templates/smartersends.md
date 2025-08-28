---
nav_title: SmarterSends
article_title: SmarterSends
description: "この参考記事では、BrazeとSmarterSendsのパートナーシップについて概説している。SmarterSendsは、マーケティング担当者でなくても、ブランドに準拠したEメールキャンペーンを作成、スケジュール、展開できるように設計された使いやすいインターフェースである。"
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSendsは](https://smartersends.com)、企業が作成、スケジュール、展開できるマーケティング・キャンペーンでパーソナライゼーションを推進し、使用するコンテンツやデータをコントロールしながら、ブランドや法的コンプライアンスを強化する。 

_この統合は SmarterSends によって管理されます。_

## 統合について

Braze と SmarterSends のパートナーシップにより、Braze の機能と、分散ユーザーが所有するハイパーローカライズされたコンテンツを組み合わせて、マーケティングキャンペーンを強化できます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| SmarterSendsアカウント | このパートナーシップを活用するには、[SmarterSends アカウント](https://smartersends.com)が必要です。 |
| Braze REST API キー | これらの権限を持つBraze REST APIキー： {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} これは、Brazeダッシュボードの**「設定**」>「**APIキー**」から作成できる。さらなるセキュリティのために、SmarterSendsのIPアドレス（インスタンスで利用可能）を許可リストに入れる。 |
| Braze RESTエンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Braze APIキャンペーンID | [Braze API キャンペーン ID]({{site.baseurl}}/api/api_campaigns/) は、SmarterSends を介して送信されるすべてのキャンペーンの一意の識別子です。これは Braze ダッシュボードの [**メッセージング**] > [**キャンペーン**] で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

BrazeとSmarterSendsの統合により、複数のチャネルや場所にまたがるマーケティングキャンペーンを作成・実行することで、分散型マーケティングを活用することができる。これには次のようなメリットがあります。

1. **リーチの拡大:**複数のチャネルや場所を利用することで、より幅広いオーディエンスにリーチし、さまざまな場所にいる顧客をターゲットにすることで、ブランドの露出を増やす。
2. **ターゲットを絞ったメッセージング:**顧客とのより効果的なコミュニケーションとエンゲージメントを実現するため、地域のオーディエンスに響くよう、チャネルや場所を超えてメッセージングを調整する。 
3. **ブランドの一貫性の向上:**ブランドのメッセージとイメージをすべてのチャネルと場所で統一します。これは、強力で認識しやすいブランドを構築するうえで重要です。
4. **より優れたインサイト:**さまざまなチャネルや場所からデータを収集し、顧客の行動や嗜好に関する貴重なインサイトを提供します。このインサイトは、ローカルレベルとグローバルレベルの両方でマーケティング戦略や戦術を洗練させるために利用できます。
5. **効率性の向上:**異なるチャネルや場所の強みを活用します。その結果、マーケティング目標を達成し、リソースをより効率的に活用できるようになります。 

## 統合

### ステップ1:REST APIキーを作成する

1. Brazeで、**[Settings**] > [**API Keys]**に進み、[**Create New API Key**]をクリックする。
2. APIキーの名前を入力する。
3. SmarterSendsがBrazeワークスペースとやり取りできるように、このキーに以下の権限を選択する。
- `users.track`
- `users.export.ids`
- `messages.schedule.create`
- `messages.schedule.update`
- `messages.schedule.delete`
- `sends.id.create`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `sends.data_series`
4. SmarterSendsのIPアドレスを**Whislist IPs**セクションに追加する。
5. [**API キーを保存**] をクリックします。
6. SmarterSendsの**Braze Email Service Provider**設定に、適切なパーミッションを持つAPIキーをコピー＆ペーストする。

### ステップ2:アプリケーションIDを作成またはコピーする

1. Braze ワークスペースで、[**設定**] > [**アプリ設定**] に移動します。 
2. 新しいアプリケーションをセットアップするか、ワークスペース内の既存のアプリケーションのアプリケーションIDを使用する。アプリケーション ID に **API キー**というラベルが付いていることに注意してください。 
3. このIDをコピーしてSmarterSendsの**App ID**フィールドに貼り付ける。

### ステップ3:APIキャンペーンを作成する

APIキャンペーンは、Braze内のすべてのSmarterSendsメールのメトリクスを追跡し、SmarterSendsがこれらのAPIベースのキャンペーンをトリガーできるようにする。

1. Braze で [API キャンペーンを作成]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign)します。
2. **Select Message Channel**」の下にある「**Email**」をクリックし、メトリクスのトラッキングを開始するメッセージング・チャンネルを追加する。
3. 次に、BrazeのキャンペーンIDをSmarterSendsの**キャンペーンID**フィールドにコピー＆ペーストする。 
4. BrazeのメッセージバリエーションIDをSmarterSendsの**メッセージバリエーションID**フィールドにコピー＆ペーストする。SmarterSendsでグループごとにメッセージIDを作成しない場合、これがデフォルトのメッセージIDとなる。
5. SmarterSendsで作成したグループごとに、BrazeのAPIキャンペーンにメッセージのバリアントを追加する。次に、SmarterSends でこのメッセージバリアント ID をグループのメッセージバリアント ID にコピーします。

{% alert tip %}
SmarterSendsで作成したグループごとにメッセージバリアントIDを作成し、Brazeのワークスペースで各グループの送信のメトリクスを個別に表示する。これは、Brazeでレポートを作成する際に、グループ間の傾向を特定するのに役立つ。
{% endalert %}

## カスタマイズ

SmarterSendsの各インスタンスは、ブランドのロゴカラーやカスタムドメイン名で完全にカスタマイズ可能で、親しみやすい環境を作ることができる。さらに、パーソナライゼーションを進めるために、Brazeワークスペース内のセグメントに基づいて、キャンペーンでユーザーをターゲットにする属性やカスタム属性を定義できる。


