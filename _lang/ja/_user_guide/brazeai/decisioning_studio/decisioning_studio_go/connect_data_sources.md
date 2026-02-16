---
nav_title: データソースの接続
article_title: データソースの接続
page_order: 1
description: "BrazeAI決定スタジオGo がカスタマーエンゲージメントプラットフォームを介して顧客データに接続する方法について説明します。"
---

# データソースの接続

> BrazeAI Decisioning Studio™Go は、カスタマーエンゲージメントプラットフォーム(CEP)を介して顧客データに接続します。ここでは、どのようなデータを使用し、どのように接続するかについて説明します。

## 顧客データへのアクセス方法

さまざまなソースとの直接データ統合をサポートするDecisioning Studio Proとは異なり、Decisioning Studio GoはCEPを通じて顧客データにアクセスします。つまり、

- **オーディエンスデータ** は、CEP (Braze、Salesforce Marketing Cloud、またはKlaviyo) で定義されたSegments またはリストから直接プルされ、特定の事前定義された属性s (1P データではありません) のみを含めることができます。
- **エンゲージメントデータ**(開封、クリック、送信)は、自動クエリーまたはCEP とのネイティブ統合によってキャプチャされます
- **CEP で設定した以上の追加データパイプラインのセットアップ** は必要ありません

## サポートされる統合パターン

Studio Go の決定では、データアクセス用に次のCEP がサポートされます。

| CEP | オーディエンスソース | エンゲージメントデータ |
|-----|-----------------|-----------------|
| **Braze** | セグメント | Braze Currents輸出 |
| **Salesforce Marketing Cloud** | データ拡張 | SQL クエリの自動化 |
| **クラビヨ** | セグメント | ネイティブAPI 統合 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## CEPのデータ要件

{% tabs %}
{% tab Braze %}

### Braze要求事項

Braze統合の場合、デシジョンスタジオGoには以下が必要です。

1. **Braze Currents**:デシジョンスタジオへエンゲージメントデータをエクスポートするには、Braze Currentsを有効にして設定する必要があります。これにより、エージェントは顧客レスポンスから学習できます。

2. **セグメントアクセス**:作成するAPI キーには、対象オーディエンスを定義するSegmentにアクセスするための権限が必要です。

3. **ユーザプロファイルデータ**:エージェントが考慮するユーザープロファイル 属性s またはカスタム属性s は、Braze API からアクセス可能である必要があります。

{% alert important %}
Braze Currentsエクスポートに、比較するキャンペーン(BAU キャンペーンを含む)のデータが含まれていることを確認します。
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMCのデータ要件

Salesforce Marketing Cloud 統合の場合、Decisioning Studio Go には以下が必要です。

1. **データ拡張**:オーディエンスは、デシジョンスタジオがアクセスできるデータエクステンションで定義する必要があります。サブスクライバキーをプライマリユーザー 識別子として使用します。
2. **イベントアクセスの追跡**:インストール済みアプリケーションパッケージがエンドツーエンドの自動設定をサポートしている限り、追加の設定は必要ありません。 

データエクステンションとSQLクエリーは、[オーケストレーションセットアップ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)の一部として設定されます。

{% endtab %}
{% tab Klaviyo %}

### Klaviyoのデータ要件

Klaviyo統合の場合、Decisioning Studio Goには以下が必要です。

1. **セグメントアクセス**:オーディエンスは、API キーが使用できるKlaviyo Segmentとして定義する必要があります。
2. **プロファイルデータ**:顧客 属性s を読み取るには、API キーにプロファイルへのフルアクセス権限が必要です。
3. **メトリックアクセス**:エンゲージメント情報を取得するには、API キーにメトリクスとイベントへのフルアクセス権限が必要です。

{% endtab %}
{% endtabs %}

## ベストプラクティス

- **データを新規に保持**:オーディエンス Segment s と顧客データが定期的に(最低でも毎日)更新されていることを確認してください。そうすることで、エージェントは最新の情報を使用できます。
- **関連する属性を含めるs**:どのような顧客の特徴が、人口統計、エンゲージメント履歴、購買行動、ライフサイクルタグeなどのメッセージに影響を与えるかを考えてみよう。

## 次のステップ

Go がどのようにデータに接続するかを理解したので、CEP 統合のセットアップに進みます。

- [オーケストレーションの設定]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

