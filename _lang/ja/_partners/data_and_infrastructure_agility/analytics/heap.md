---
nav_title: Heap
article_title: "ヒープ解析"
description: "このリファレンス記事では、Braze Currents を使用してヒープでエンゲージメントのイベントを自動的に分析する方法について説明します。ヒープは、デジタルインサイトs プラットフォームで、Brazeにヒープデータをインポートし、ユーザー コホートs を作成し、BrazeデータをヒープにエクスポートしてSegments を作成することができます。"
page_type: partner
search_tag: Partner


---

# ヒープ分析

> 解析のためにBrazeからヒープにエンゲージメント事象を自動的に送信する方法について述べた。ヒープと他の機能の統合については、[ヒープコホートs]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration)をBrazeに同期するなど、メインの[ヒープ記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/)を参照してください。

## データエクスポート統合

Braze Currentsを使用して、Brazeからヒープにエンゲージメントの事象(送信されたメール、送信されたプッシュなど)を自動的に送信し、解析する。

### ステップ1:ヒープ認証情報の取得

このインテグレーションを設定するには、ヒープアカウントマネージャーから取得できるWebhook エンドポイント URL が必要です。

### ステップ2:Braze Currentsの設定

Braze で、**Partner Integrations**> **Data Export** に移動し、**Create New Current** をクリックし、**Heap Export** を選択します。 

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**Currents**の下に**統合**があります。
{% endalert %}

エクスポートに名前を付け、**Current Details** ページに進みます。この画面では、エンドポイントとオプションのベアラトークン(提供されている場合)を入力します。

統合の認証情報を設定したら、ヒープにエクスポートするすべてのメッセージエンゲージメント、顧客行動、およびユーザーのイベントを確認し、**Launch Current**をクリックします。

![][5]{: style="max-width:90%;"}

[5]: {% image_buster /assets/img/heap/heap4.png %} 
