---
nav_title: オーケストレーションを設定する
article_title: オーケストレーションを設定する
page_order: 2
description: "Decisioning Studio Proエージェントのオーケストレーション設定方法を学習し、パーソナライズされたコミュニケーションをイネーブルメントする。"
toc_headers: h2
---

# オーケストレーションを設定する

> 意思決定エージェントは、顧客データを取得し1対1レベルでパーソナライズされた後、コミュニケーションのオーケストレーションを行うためにカスタマーエンゲージメントプラットフォーム（CEP）に接続する必要がある。この記事では、サポートされている各CEPの統合設定方法を説明する。

## サポートされているCEP

Decisioning Studio Proは以下のカスタマーエンゲージメントプラットフォームをサポートする：

| CEP | 統合タイプ | 設定の複雑さ |
|-----|-----------------|------------------|
| **Braze** | ネイティブAPIの統合 | 低（推奨） |
| **セールスフォース マーケティングクラウド** | ネイティブAPIイベント＋ジャーニー | 中 |
| **クラヴィオ** | ネイティブAPIイベント＋フロー | 中 |
| **その他のCEP** | カスタム（推奨ファイル） | 高 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

以下のCEPを選択して、統合設定を開始する。

{% tabs %}
{% tab Braze %}

## Brazeの連携設定

以下のステップに従って、Braze Decisioning StudioエージェントをBrazeのオーケストレーション機能と統合する（Brazeのサービスチームが支援する）：

### ステップ 1: API キーの作成

**設定**＞**API キー**に移動し、以下の権限で新しいキーを作成する：

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### ステップ 2:APIトリガーによるキャンペーンを設定する

各基本テンプレートに対して、最適化されたすべての次元のAPIトリガープロパティを備えたAPIトリガー型キャンペーンを設定する。

ベーステンプレートとは、意思決定エージェントがメッセージングのオーケストレーションに使用する可能性のあるあらゆるテンプレートを指す。意思決定エージェントは、1つの基本テンプレートを持つ場合もあれば、複数の基本テンプレートを持つ場合もある。後者の場合、各顧客に適した基本テンプレートを選択することが、エージェントがパーソナライズする意思決定の一つとなる。

### ステップ 3:再適格性を設定する

すべてのAPIトリガー型キャンペーンにおいて、ユーザーが15分以内に再対象となることを可能にせよ。

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Decisioning Studioエージェントは同じキャンペーンを1日に複数回送信することはないが、テスト目的で同じキャンペーンを1日に複数回送信する機能は必要だろう。
{% endalert %}

### ステップ 4: ダイナミックなプレースホルダーを追加する

これらは、Decisioning Studioエージェントが最適化している決定事項のダイナミックなプレースホルダーとして機能する。

#### 例1：メールキャンペーン

仮にDecisioning Studioエージェントがメールキャンペーンを最適化しているとしよう。これは次のように設定できるかもしれない：

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

仮にエージェントがテンプレートの選択と行動喚起（CTA）メッセージの最適化を行っている場合、各テンプレートごとにAPIトリガー型キャンペーンを作成すべきだ。あるテンプレートのCTAセクションは以下のように見えるかもしれない：

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### 例２：プッシュキャンペーン

仮に、Decisioning Studioのエージェントがプッシュキャンペーンのメッセージを最適化しているとしよう。これは次のように設定できるかもしれない：

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

その結果、次のメッセージが表示される：

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### 例3：SMSキャンペーン

仮に、Decisioning StudioエージェントがSMSキャンペーンのフィールドを最適化しているとしよう。これは次のように設定できるかもしれない：

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

その結果、次のメッセージが表示される：

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC統合の設定

Decisioning Studio ProはSalesforce Marketing Cloudとのネイティブ統合をサポートする。Decisioning Studioは、ダイナミックな要素を埋めるために必要なデータと共に、APIイベントをジャーニーにトリガーする。

SFMCのオーケストレーション設定は、Decisioning Studio ProとDecisioning Studio Goの両方で同様である。SFMC統合の設定のステップの詳細については、Decisioning Studio Goのドキュメントに記載されている[SFMCの指示]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)に従うこと。

{% endtab %}
{% tab Klaviyo %}

## Klaviyoの連携設定

Decisioning Studio ProはKlaviyoとのネイティブ統合をサポートしている。Decisioning Studioは、ダイナミックな要素を埋めるために必要なデータと共にAPIイベントをフローにトリガーする。

Klaviyoのオーケストレーション設定は、Decisioning Studio ProとDecisioning Studio Goの双方で同様である。Klaviyo連携の設定のステップの詳細については、Decisioning Studio Goのドキュメントに記載[されているKlaviyoの指示]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)に従うこと。

{% endtab %}
{% tab Other CEPs %}

## 他のCEP統合の設定

Decisioning Studioはあらゆるカスタマーエンゲージメントプラットフォームと連携できる。ただし、これは貴社のチームによるカスタム開発作業が必要となる可能性がある。Decisioning Studioは直接通信をトリガーできないためだ。

このシナリオでは、エージェントは「推奨ファイル」を届ける。このファイルには顧客ごとの行が含まれており、各列はその顧客に対するすべてのパーソナライズされた決定を示している。

例えば、次の推奨ファイル：

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

次のようなメールキャンペーンを最適化するために使われるかもしれない：

![意思決定プロ図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## 次のステップ

オーケストレーションの設定が終わったら、次にエージェントの設計に進む：

- [エージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

