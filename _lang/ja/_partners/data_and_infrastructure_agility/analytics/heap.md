---
nav_title: Heap
article_title:"ヒープ分析"
description:"この参考記事では、HeapデータをBrazeにインポートし、ユーザーコホートを作成し、BrazeデータをHeapにエクスポートしてセグメンテーションを作成できる、デジタルインサイトプラットフォームであるHeapを使用して、エンゲージメントイベントを自動的に分析するためにBraze Currentsを使用する方法を概説している。"
page_type: partner
search_tag:Partner


---

# ヒープ分析

> この記事では、エンゲージメントイベントをBrazeからHeapに自動的に送信して分析する方法について説明する。Heapの[コホートと]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration)Brazeの[同期など]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration)、Heapとその他の機能の統合についての詳細は、[Heapの]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/)メイン[記事を]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/)参照のこと。

## データ・エクスポートの統合

Braze Currentsを使用して、エンゲージメントイベント（メール送信、プッシュ送信など）をBrazeからHeapに自動的に送信し、分析を行う。

### ステップ1:ヒープ認証情報を取得する

この統合を設定するには、WebhookエンドポイントURLが必要で、これはHeapアカウントマネージャーから取得できる。

### ステップ2:Braze電流を設定する

Brazeで、**Partner Integrations**>**Data Exportに**移動し、**Create New Currentsを**クリックし、**Heap Exportを**選択する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Integrationsの**下に**Currentsが**ある。
{% endalert %}

エクスポートに名前を付け、**Currents Details**ページに進む。このページで、エンドポイントとオプションのベアラ・トークン（提供されている場合）を入力する。

統合の認証情報を設定した後、Heapにエクスポートしたいすべてのメッセージエンゲージメント、カスタマー行動、ユーザーイベントにチェックを入れ、「**Launch Currents**」をクリックする。

![][5]{: style="max-width:90%;"}

[5]: {% image_buster /assets/img/heap/heap4.png %} 
