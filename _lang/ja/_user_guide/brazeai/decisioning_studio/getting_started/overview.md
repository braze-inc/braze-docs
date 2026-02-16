---
nav_title: 概要
article_title: 概要
page_order: 1
page_type: reference
description: "このリファレンスでは、データソースの接続、オーケストレーションの設定、デシジョンエージェントの設計など、デシジョニングスタジオの設定に関わるステップの概要を説明する。"
---

# 概要

> このリファレンスでは、データソースの接続、オーケストレーションの設定、デシジョンエージェントの設計など、デシジョニングスタジオの設定に関わるステップの概要を説明する。

BrazeAI Decisioning Studio™では、あらゆるビジネス指標を最適化する意思決定エージェントを設計し、展開することができる。意思決定エージェントは、特定のビジネス目標を達成するために調整されたカスタム構成である。

そのためには、データソースを接続し、オーケストレーションを設定し、意思決定エージェントを設計しなければならない。

{% alert tip %}
Decisioning Studio Pro顧客の場合、AIエキスパート・サービス・チームが最適なパフォーマンスのためにDecisioning Studioの設定をサポートする。
{% endalert %}

## デシジョン・スタジオの設定

Decisioning Studioを設定するには、以下のステップを完了する：

### ステップ 1: データソースを接続する

顧客プロファイルとエンゲージメントデータを結びつけ、作成した意思決定エージェントが各顧客がどのような人物で、どのように行動するかを理解できるようにする。

通常、データソースを接続する必要があるのは、Decisioning Studioの初期セットアップ時に一度だけである。後にユースケースを拡大する場合、新しいデータソースを追加する必要があるかもしれない。

{% alert tip %}
すでに[Brazeデータ]({{site.baseurl}}/user_guide/data/braze_data_platform)プラットフォームにあるデータはすべて、自動的にDecisioning Studioで利用できる。
{% endalert %}

詳細なガイダンスについては、Decisioning Studioの各階層のドキュメントを参照のこと：
- [デシジョン・スタジオ・ゴーデータソースを接続する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [デシジョン・スタジオ・プロデータソースを接続する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)

### ステップ 2:オーケストレーションの設定

Decisioning Studioをカスタマーエンゲージメントプラットフォーム（CEP）と統合し、エージェントがアクションをオーケストレーションできるようにする。CEPは、エージェントの判断に基づいてカスタマーエクスペリエンスをパーソナライズされた形で顧客に提供するためのプラットフォームである。

通常、このオーケストレーションを設定する必要があるのは一度だけだ。

詳細なガイダンスについては、Decisioning Studioの各階層のドキュメントを参照のこと：
- [デシジョン・スタジオ・ゴーオーケストレーションの設定]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [デシジョン・スタジオ・プロオーケストレーションの設定]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

### ステップ 3:エージェントをデザインする

意思決定エージェントを設定して、最大化したい結果と、それを達成するためにエージェントが取れるアクションを定義する。エージェントの設計に関する詳しいガイダンスについては、「[意思決定エージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)」を参照のこと。

ティア別のガイダンスについては、こちらを参照のこと：
- [デシジョン・スタジオ・ゴーエージェントをデザインする]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
- [デシジョン・スタジオ・プロエージェントをデザインする]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

{% alert tip %}
デシジョニング・スタジオ・プロ顧客の場合、AIデシジョニング・サービス・チームがデシジョニング・エージェントの設計と立ち上げをサポートする。
{% endalert %}

### ステップ 4: 意思決定エージェントを立ち上げる

意思決定エージェントを学習させ、継続的に学習させ、ビジネス成果のために最適化させる。

詳細なガイダンスについては、Decisioning Studioの各階層のドキュメントを参照のこと：
- [デシジョン・スタジオ・ゴーエージェントを立ち上げる]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
- [デシジョン・スタジオ・プロエージェントを立ち上げる]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/) 

## 次のステップ

デシジョニング・スタジオの主要コンセプトの基本的な理解ができたので、デシジョニング・エージェントの設計を開始できる。

- [意思決定エージェントをデザインする]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)