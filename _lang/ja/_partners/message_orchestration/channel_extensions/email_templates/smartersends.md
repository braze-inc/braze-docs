---
nav_title: SmarterSends
article_title: SmarterSends
description: "この参考記事では、BrazeとSmarterSendsのパートナーシップについて概説している。SmarterSendsは、マーケティング担当者でなくても、ブランドに準拠したEメールキャンペーンを作成、スケジュール、展開できるように設計された使いやすいインターフェースである。"
alias: /partners/smartersends/
page_type: partner
search_tag: Partner
---

# SmarterSends

> [SmarterSendsは][2]、企業が作成、スケジュール、展開できるマーケティング・キャンペーンでパーソナライゼーションを推進し、使用するコンテンツやデータをコントロールしながら、ブランドや法的コンプライアンスを強化する。 

BrazeとSmarterSendsのパートナーシップにより、Brazeのパワーと分散したユーザーが所有するハイパーローカライズされたコンテンツを組み合わせることができ、マーケティングキャンペーンを向上させることができる。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| SmarterSendsアカウント | このパートナーシップを利用するには、[SmarterSendsのアカウントが][2]必要である。 |
| Braze REST API キー | これらの権限を持つBraze REST APIキー： {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} これは、Brazeダッシュボードの**「設定**」>「**APIキー**」から作成できる。さらなるセキュリティのために、SmarterSendsのIPアドレス（インスタンスで利用可能）を許可リストに入れる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][1]。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Braze APIキャンペーンID | [Braze APIキャンペーンIDは]({{site.baseurl}}/api/api_campaigns/)、SmarterSendsを通じて送信されるすべてのキャンペーンの一意の識別子である。これはBrazeダッシュボードの**Messaging**>**Campaignsで**作成できる。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsで**APIキーを作成できる。
{% endalert %}

## ユースケース

BrazeとSmarterSendsの統合により、複数のチャネルや場所にまたがるマーケティングキャンペーンを作成・実行することで、分散型マーケティングを活用することができる。これらの利点には以下が含まれる：

1. **リーチの拡大：**複数のチャネルや場所を利用することで、より幅広いオーディエンスにリーチし、さまざまな場所にいる顧客をターゲットにすることで、ブランドの露出を増やす。
2. **ターゲットを絞ったメッセージング：**顧客とのより効果的なコミュニケーションとエンゲージメントを実現するため、地域のオーディエンスに響くよう、チャネルや場所を超えてメッセージングを調整する。 
3. **ブランドの一貫性が向上した：**ブランドメッセージとイメージをすべてのチャネルと場所で統一することは、強力で認知度の高いブランドを構築するために重要である。
4. **より優れた洞察力**さまざまなチャネルや場所からデータを収集し、顧客の行動や嗜好に関する貴重な洞察を提供することで、地域レベルでもグローバルレベルでも、マーケティング戦略や戦術を洗練させることができる。
5. **効率が向上した：**異なるチャネルやロケーションの強みを活用することで、望ましいマーケティング目標を達成しつつ、より効率的にリソースを活用することができる。 

## 統合

### ステップ1:REST APIキーを作成する

1. Brazeで、**\[Settings**] > \[**API Keys]**に進み、\[**Create New API Key**]をクリックする。
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
5. **Save API Keyを**クリックする。
6. SmarterSendsの**Braze Email Service Provider**設定に、適切なパーミッションを持つAPIキーをコピー＆ペーストする。

### ステップ2:アプリケーションIDを作成またはコピーする

1. Brazeのワークスペースで、**Settings**>**App Settingsに**進む。 
2. 新しいアプリケーションをセットアップするか、ワークスペース内の既存のアプリケーションのアプリケーションIDを使用する。アプリケーションIDが**APIキーと**表示されていることに注意。 
3. このIDをコピーしてSmarterSendsの**App ID**フィールドに貼り付ける。

### ステップ3:APIキャンペーンを作成する

APIキャンペーンは、Braze内のすべてのSmarterSendsメールのメトリクスを追跡し、SmarterSendsがこれらのAPIベースのキャンペーンをトリガーできるようにする。

1. Brazeで[APIキャンペーンを作成]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign)する。
2. **Select Message Channel**」の下にある「**Email**」をクリックし、メトリクスのトラッキングを開始するメッセージング・チャンネルを追加する。
3. 次に、BrazeのキャンペーンIDをSmarterSendsの**キャンペーンID**フィールドにコピー＆ペーストする。 
4. BrazeのメッセージバリエーションIDをSmarterSendsの**メッセージバリエーションID**フィールドにコピー＆ペーストする。SmarterSendsでグループごとにメッセージIDを作成しない場合、これがデフォルトのメッセージIDとなる。
5. SmarterSendsで作成したグループごとに、BrazeのAPIキャンペーンにメッセージのバリアントを追加する。次に、メッセージバリアントIDをSmarterSendsのグループのメッセージバリアントIDにコピーする。

{% alert tip %}
SmarterSendsで作成したグループごとにメッセージバリアントIDを作成し、Brazeのワークスペースで各グループの送信のメトリクスを個別に表示する。これは、Brazeでレポートを作成する際に、グループ間の傾向を特定するのに役立つ。
{% endalert %}

## カスタマイズ

SmarterSendsの各インスタンスは、ブランドのロゴカラーやカスタムドメイン名で完全にカスタマイズ可能で、親しみやすい環境を作ることができる。さらに、パーソナライゼーションを進めるために、Brazeワークスペース内のセグメントに基づいて、キャンペーンでユーザーをターゲットにする属性やカスタム属性を定義できる。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://smartersends.com