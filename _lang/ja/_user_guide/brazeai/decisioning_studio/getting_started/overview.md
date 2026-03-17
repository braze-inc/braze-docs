---
nav_title: 概要
article_title: 概要
page_order: 1
page_type: reference
description: "このリファレンスは、データソースの接続、オーケストレーションの設定、意思決定エージェントの設計など、Decisioning Studioの設定ステップの概要を説明する。"
---

# 概要

> このリファレンスは、データソースの接続、オーケストレーションの設定、意思決定エージェントの設計など、Decisioning Studioの設定ステップの概要を説明する。

BrazeAI Decisioning Studio™は、あらゆるビジネス指標を最適化する意思決定エージェントを設計・展開することを可能にする。意思決定エージェントとは、特定のビジネス目標を達成するためにカスタマイズされた設定である。

そのためには、データソースを接続し、オーケストレーションを設定し、意思決定エージェントを設計しなければならない。

{% alert tip %}
Decisioning Studio Proの顧客には、AIエキスパートサービスチームがDecisioning Studioの最適なパフォーマンス設定を支援する。
{% endalert %}

## Decisioning Studioの設定

Decisioning Studioを設定するには、以下のステップを完了する：

### ステップ 1: データソースを接続する

顧客プロファイルとエンゲージメントデータを連携させる。そうすることで、作成した意思決定エージェントが各顧客の正体と行動パターンを理解できるようになる。

通常、データソースの接続は一度だけ行えばよい。それはDecisioning Studioの初期設定時である。後でユースケースを拡張する場合、新しいデータソースを追加する必要があるかもしれない。

{% alert tip %}
[Brazeデータプラットフォーム]({{site.baseurl}}/user_guide/data/braze_data_platform)に既に存在するデータは、すべて自動的にDecisioning Studioで利用可能となる。
{% endalert %}

詳細なガイダンスについては、使用しているDecisioning Studioのティアのドキュメントを参照せよ。
- [Decisioning Studioゴー：データソースを接続する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/connect_data_sources/)
- [Decisioning Studio Pro:データソースを接続する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/connect_data_sources/)

### ステップ 2:オーケストレーションを設定する

Decisioning Studioをカスタマーエンゲージメントプラットフォーム（CEP）と統合し、エージェントがアクションのオーケストレーションを行うことができるようにする。CEPは、エージェントの決定に基づいて顧客にパーソナライズされた体験を提供するプラットフォームである。

このオーケストレーションの設定は通常、一度だけ行えばよい。

詳細なガイダンスについては、使用しているDecisioning Studioのティアのドキュメントを参照せよ。
- [Decisioning Studioゴー：オーケストレーションを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro:オーケストレーションを設定する]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

### ステップ 3:エージェントを設計せよ

意思決定エージェントを設定し、最大化したい成果と、それを達成するためにエージェントが実行できるアクションを定義する。エージェント設計の詳細なガイダンスについては、[「意思決定エージェントの設計」]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)を参照せよ。

各階層ごとのガイダンスについては：
- [Decisioning Studioゴー：エージェントを設計せよ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)
- [Decisioning Studio Pro:エージェントを設計せよ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

{% alert tip %}
Decisioning Studio Proの顧客には、AI意思決定サービスチームが意思決定エージェントの設計と立ち上げを支援する。
{% endalert %}

### ステップ 4: 意思決定エージェントを起動せよ

意思決定エージェントを起動し、ビジネス成果に向けて継続的に学習と最適化を行わせるのだ。

詳細なガイダンスについては、使用しているDecisioning Studioのティアのドキュメントを参照せよ。
- [Decisioning Studioゴー：エージェントを起動せよ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
- [Decisioning Studio Pro:エージェントを起動せよ]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/) 

## 次のステップ

Decisioning Studioの主要な概念について基本的な理解が得られたので、意思決定エージェントの設計を始められる。

- [意思決定エージェントの設計]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)