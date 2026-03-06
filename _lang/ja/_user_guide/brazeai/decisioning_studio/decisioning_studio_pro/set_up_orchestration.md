---
nav_title: オーケストレーションの設定
article_title: オーケストレーションの設定
page_order: 2
description: "パーソナライズされたコミュニケーションを可能にするために、Decisioning Studio Pro エージェントにオーケストレーションを設定する方法を学ぶ。"
toc_headers: h2
---

# オーケストレーションの設定

> 意思決定エージェントは、カスタマーエンゲージメントプラットフォーム（CEP）に接続し、顧客データを取り込み、1:1レベルでパーソナライズされたコミュニケーションをオーケストレーションする必要がある。この記事では、サポートされているCEPごとに統合を設定する方法を説明する。

## サポートされるCEP

Decisioning Studio Proは、以下のカスタマーエンゲージメントプラットフォームをサポートしている：

| CEP | 統合タイプ | セットアップの複雑さ |
|-----|-----------------|------------------|
| **Braze** | ネイティブAPIの統合 | 低い（推奨） |
| **セールスフォース・マーケティングクラウド** | ネイティブAPIイベント＋ジャーニー | 中 |
| **クラビオ** | ネイティブAPIイベント＋フロー | 中 |
| **その他のCEP** | 顧客（推奨ファイル） | 高 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

以下からCEPを選択し、統合設定を開始する。

{% tabs %}
{% tab Braze %}

## Brazeとの統合設定

以下のステップに従って、Braze Decisioning StudioエージェントをBrazeのオーケストレーション機能と統合する（Brazeのサービスチームがサポートする）：

### ステップ 1: API キーの作成

**設定**＞**APIキーと**進み、以下の権限で新しいキーを作成する：

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### ステップ 2:APIトリガーキャンペーンを設定する

APIトリガーキャンペーンを各ベーステンプレートに設定し、すべての最適化されたディメンションのAPIトリガープロパティを設定する。

ベーステンプレートとは、デシジョニングエージェントがメッセージのオーケスト レーションに使用する可能性のあるテンプレートのことである。意思決定エージェントは、1つのベーステンプレートを持つかもしれないし、複数のベーステンプレートを持つかもしれない。その場合、各顧客に適切なベーステンプレートを選択することは、エージェントがパーソナライズされた意思決定の1つとなる。

### ステップ 3:再入会資格を設定する

すべてのAPIトリガーキャンペーンで、ユーザーが15分以内に再資格取得できるようにする。

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Decisioning Studioエージェントは同じキャンペーンを1日に複数回送信することはないが、テスト目的で同じキャンペーンを1日に複数回送信する機能を持ちたいだろう。
{% endalert %}

### ステップ 4: ダイナミックなプレースホルダーを追加する

これらは、Decisioning Studioエージェントが最適化する意思決定のダイナミックなプレースホルダとして機能する。

#### 例1：メールキャンペーン

Decisioning Studioエージェントがメールキャンペーンを最適化しているとする。このような構成になるかもしれない：

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

仮にエージェントがテンプレートとコール・トゥ・アクション（CTA）メッセージの選択を最適化しているとすると、APIトリガーキャンペーンは各テンプレートに対して作成されるべきであり、1つのテンプレートのCTAセクションは以下のようになる：

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### 例2：プッシュキャンペーン

意思決定スタジオのエージェントがプッシュキャンペーンのメッセージを最適化しているとする。このような構成になるかもしれない：

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

その結果、次のようなメッセージが表示された：

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### 例3：SMSキャンペーン

Decisioning StudioエージェントがSMSキャンペーンのフィールドを最適化しているとする。このような構成になるかもしれない：

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

その結果、次のようなメッセージが表示された：

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC統合の設定

Decisioning Studio Proは、Salesforce Marketing Cloudとのネイティブ統合をサポートしている。Decisioning Studioは、ダイナミックな要素にデータを入力するために必要なAPIイベントをジャーニーにトリガーする。

SFMCのオーケストレーションの設定は、Decisioning Studio ProとDecisioning Studio Goの両方で同様である。SFMC統合を構成する詳細なステップについては、Decisioning Studio Goドキュメントの[SFMCの説明に従って]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)ください。

{% endtab %}
{% tab Klaviyo %}

## Klaviyoとの統合を設定する

Decisioning Studio ProはKlaviyoとのネイティブ統合をサポートしている。Decisioning StudioはAPIイベントをトリガーして、ダイナミックな要素に必要なデータをフローに入力する。

Klaviyoのオーケストレーションのセットアップは、Decisioning Studio ProとDecisioning Studio Goの両方で似ている。Klaviyoとの統合を設定する詳細なステップについては、Decisioning Studio Goドキュメントの[Klaviyoのインストラクションに]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)従う。

{% endtab %}
{% tab Other CEPs %}

## 他のCEP統合を設定する

Decisioning Studioは、あらゆるカスタマーエンゲージメントプラットフォームと統合できる。しかし、Decisioning Studioでは通信を直接トリガーすることができないため、チームによるカスタム・エンジニアリングが必要になるかもしれない。

このシナリオでは、エージェントは "推薦ファイル "を配信する。このファイルには、各顧客の行があり、その顧客のパーソナライズされた決定を示す列がある。

例えば、次のような推薦ファイルがある：

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

以下のようなメールキャンペーンを最適化するために使われるかもしれない：

![デシジョン・プロ・ダイアグラム]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## 次のステップ

オーケストレーションの設定が終わったら、エージェントの設計に進む：

- [エージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

