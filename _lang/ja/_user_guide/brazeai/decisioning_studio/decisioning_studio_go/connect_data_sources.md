---
nav_title: データソースを接続する
article_title: データソースを接続する
page_order: 1
description: "BrazeAI Decisioning Studio Goが、カスタマーエンゲージメントプラットフォームを通じて顧客データに接続する方法を学ぶ。"
---

# データソースを接続する

> BrazeAI Decisioning Studio™ Goは、カスタマーエンゲージメントプラットフォーム（CEP）を通じて顧客データに接続する。この記事では、どのようなデータが使用され、接続がどのように機能するかを説明する。

## Goが顧客データにアクセスする方法

Decisioning Studio Proとは異なり、Decisioning Studio Goは様々なソースとの直接的なデータ統合をサポートする。Decisioning Studio Goは、CEPを介して顧客データにアクセスする。これはつまり：

- **オーディエンスデータ** は、CEP (BrazeまたはSalesforce Marketing Cloud) で定義されたSegments またはリストから直接プルされ、特定の事前定義された属性s (1P データではありません) のみを含めることができます。
- **エンゲージメントデータ**(開封、クリック、送信)は、自動クエリーまたはCEP とのネイティブ統合によってキャプチャされます
- **CEP で設定した以上の追加データパイプラインのセットアップ** は必要ありません

## サポートされている統合パターン

Decisioning Studio Goは、データアクセスにおいて以下のCEPをサポートする：

| CEP | オーディエンスソース | エンゲージメントデータ |
|-----|-----------------|-----------------|
| **Braze** | セグメント | Braze Currentsのエクスポート |
| **セールスフォース マーケティングクラウド** | データ拡張 | SQLクエリのオートメーション |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## CEPによるデータ要件

{% tabs %}
{% tab Braze %}

### Brazeのデータ要件

Brazeとの連携において、Decisioning Studio Goは以下の要件を必要とする：

1. **Braze Currents**:Braze Currentsをイネーブルし、エンゲージメントデータをDecisioning Studio Goにエクスポートするよう設定しなければならない。これによりエージェントは顧客の反応から学習できる。

2. **セグメントアクセス**：作成するAPI キーは、ターゲットオーディエンスを定義するセグメントにアクセスする権限を持たなければならない。

3. **ユーザープロファイルデータ**：エージェントに考慮させたいユーザープロファイル属性やカスタム属性は、すべてBraze APIを通じてアクセス可能でなければならない。

{% alert important %}
比較対象とするキャンペーン（通常運用キャンペーンを含む）のデータが、必ずBraze Currentsのエクスポートに含まれていることを確認せよ。
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMCのデータ要件

Salesforce Marketing Cloudとの連携において、Decisioning Studio Goは以下の要件を必要とする：

1. **データ拡張機能**：対象オーディエンスは、Decisioning Studio Goがアクセス可能なデータ拡張で定義されなければならない。SubscriberKeyを主要なユーザー識別子として使用する。
2. **トラッキング, 追跡へのアクセス**：インストール済みアプリパッケージがエンドツーエンドのオートメーションセットアップをサポートしている限り、追加の設定は不要だ。 

データ拡張とSQLクエリは[、オーケストレーション設定]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)の一部として構成される。

{% endtab %}
{% endtabs %}

## ベストプラクティス

- **データを最新の状態に保て**。顧客セグメントと顧客データは定期的に（最低でも毎日）更新するように。そうすればエージェントは最新の情報を扱える。
- **関連する属性を記載する**：顧客の特性がどのメッセージに響くかを左右する可能性について考えてみるんだ。人口統計、エンゲージメント履歴、購買行動、ライフサイクル段階は、どれも貴重な手がかりだ。

## 次のステップ

Goがデータに接続する仕組みを理解したところで、CEP統合の設定に進む：

- [オーケストレーションを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

