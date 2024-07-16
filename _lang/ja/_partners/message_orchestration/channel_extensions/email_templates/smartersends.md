---
nav_title: SmarterSends
article_title:よりスマートな送り
description:「この参考記事では、BrazeとSmarterSendsのパートナーシップについて概説しています。SmarterSendsは、マーケティング担当者以外の人がブランドに準拠したメールキャンペーンを作成、スケジュール、展開できるように設計された使いやすいインターフェイスです。「
alias: /partners/smartersends/
page_type: partner
search_tag:Partner
---

# よりスマートな送り

> [SmarterSendsは、企業がマーケティングキャンペーンを作成、スケジュール設定、展開することで、使用するコンテンツやデータをコントロール][2]しながらブランドや法的コンプライアンスを強化し、パーソナライゼーションを促進します。 

BrazeとSmarterSendsのパートナーシップにより、Brazeのパワーを分散型ユーザーが所有するハイパーローカライズされたコンテンツと組み合わせて、マーケティングキャンペーンの効果を高めることができます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| SmarterSendsアカウント | このパートナーシップを利用するには、[SmarterSendsアカウントが必要です][2]。 |
| Braze REST API キー | 以下の権限が付与された Braze REST API キー: {::nomarkdown}<ul><li><code>users.track</code></li><li><code>users.export.ids</code></li><li><code>messages.schedule.create</code></li><li><code>messages.schedule.update</code></li> <li><code>messages.schedule.delete</code></li><li><code>sends.id.create</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>sends.data_series</code></li></ul>{:/} これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。セキュリティを強化するには、SmarterSendsのIPアドレス（インスタンスで使用可能）をホワイトリストに登録してください。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
| Braze API キャンペーン ID | [Braze APIキャンペーン IDは]({{site.baseurl}}/api/api_campaigns/)、SmarterSendsを通じて送信されるすべてのキャンペーンの固有の識別子です。これは Braze ダッシュボードの \[**メッセージング**] > \[**キャンペーン**] で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、**開発者コンソール** > API **設定で API** キーを作成できます。
{% endalert %}

## ユースケース

BrazeとSmarterSendsの統合により、複数のチャネルと場所でマーケティングキャンペーンを作成して実行することで、分散型マーケティングを活用できます。これらの利点には以下が含まれます。

1. **リーチの拡大:**複数のチャネルとロケーションを使用して幅広いオーディエンスリーチし、さまざまな地域の顧客をターゲットにすることで、ブランドの露出度が高まります。
2. **ターゲットを絞ったメッセージング:**顧客とのより効果的なコミュニケーションとエンゲージメントを実現するために、地域のオーディエンスの共感を得られるように、チャネルや場所を問わずメッセージングカスタマイズします。 
3. **ブランドの一貫性の向上:**すべてのチャネルと場所でブランドメッセージングと画像, 写真統一することは、強力で認知度の高いブランドを構築するために重要です。
4. **より優れた洞察:**さまざまなチャネルや場所からデータを収集し、顧客行動や好みに関する貴重な洞察を提供します。この情報は、ローカルレベルとグローバルレベルの両方でマーケティング戦略と戦術を改善するために使用できます。
5. **効率の向上:**さまざまなチャネルや場所の強みを活用することで、望ましいマーケティング目標を達成しながら、リソースをより効率的に使用できます。 

## 統合

### ステップ1:REST API キーを作成する

1. Braze で \[**設定**] > \[**API キー**] に移動し、\[**新しい API キーを作成**] をクリックします。
2. API キーの名前を入力します。
3. SmarterSendsがBrazeワークスペースを操作できるようにするには、このキーに次の権限を選択してください。
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
4. SmarterSendsのIPアドレスを「**ウィッシュリストIP**」セクションに追加します。
5. 「**API キーを保存**」をクリックします。
6. 適切な権限を持つAPI キーをコピーして、**SmarterSendsのBrazeメールサービスプロバイダー設定に貼り付けます**。

### ステップ2:アプリケーション ID を作成またはコピーする

1. Braze ワークスペースで、**\[設定] > \[アプリ設定****]** に移動します。 
2. 新しいアプリを設定するか、ワークスペース内の既存のアプリケーションのアプリケーション ID を使用します。アプリケーション ID には **API キーというラベルが付いていることに注意してください**。 
3. この ID をコピーして、**SmarterSendsの「アプリID** フィールド貼り付けます。

### ステップ3:API キャンペーンを作成する

APIキャンペーンでは、Braze内のすべてのSmarterSendsメールのメトリクスをトラッキング, 追跡でき、SmarterSendsがこれらのAPIベースのキャンペーンをトリガーできるようになります。

1. Braze で [API キャンペーンを作成します]({{site.baseurl}}/api/api_campaigns/#create-a-new-campaign)。
2. 「**メッセージチャネル選択」で「****メール**」をクリックして、メトリックのトラッキング, 追跡を開始するメッセージングチャネルを追加します。
3. 次に、Brazeからキャンペーン **IDをコピーしてSmarterSendsのキャンペーンIDフィールド**貼り付けます。 
4. Braze のメッセージバリエーション ID をコピーして SmarterSends **のメッセージバリアント ID** フィールド貼り付けます。これは、SmarterSendsで各グループのメッセージIDを作成しない場合に使用されるデフォルトメッセージIDになります。
5. SmarterSendsで作成したグループごとに、BrazeのAPIキャンペーンにメッセージバリアントを追加します。次に、メッセージバリアント ID を SmarterSends のグループのメッセージバリアント ID にコピーします。

{% alert tip %}
SmarterSendsで作成した各グループのメッセージバリアントIDを作成すると、Brazeワークスペースで各グループの送信のメトリックを個別に表示できます。これは、Braze でレポートを作成するときに、グループ全体の傾向を特定するのに役立ちます。
{% endalert %}

## カスタマイズ

SmarterSendsの各インスタンスは、ブランドのロゴカラーとカスタムドメイン名で完全にカスタマイズ可能で、使い慣れた環境を作り出します。さらに、さらにパーソナライゼーションするために、Brazeワークスペース内のセグメントに基づいてキャンペーンのユーザーをターゲットにする属性とカスタム属性を定義できます。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://smartersends.com