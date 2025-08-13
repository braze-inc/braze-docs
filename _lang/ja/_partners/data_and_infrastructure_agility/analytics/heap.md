---
nav_title: Heap
article_title: "ヒープ解析"
description: "このリファレンス記事では、Braze Currents を使用して Heap でエンゲージメントイベントを自動的に分析する方法について説明します。Heap はデジタルインサイトプラットフォームであり、Braze への Heap データのインポート、ユーザー コホートの作成、セグメント作成のための Heap への Braze データのエクスポートを行うことができます。"
page_type: partner
search_tag: Partner


---

# ヒープ分析

> この記事では、解析のために Braze から Heap にエンゲージメントイベントを自動送信する方法について説明します。Heap と他の機能 (Braze との [Heap コホートの同期]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration) など) の統合について詳しくは、メインの[Heap の記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/)を参照してください。

## データエクスポート統合

Braze Currentsを使用して、Brazeからヒープにエンゲージメントの事象(送信されたメール、送信されたプッシュなど)を自動的に送信し、解析する。

### ステップ1:ヒープ認証情報の取得

この統合を設定するには、Webhook エンドポイント URL が必要です。この URL は、Heap アカウントマネージャーから取得できます。

### ステップ2:Braze Currents を設定する

Braze で [**パートナー連携**] > [**データのエクスポート**] に移動し、[**新しい Currents を作成**] をクリックし、[**ヒープのエクスポート**] を選択します。 

エクスポートに名前を付け、**Current Details** ページに進みます。この画面では、エンドポイントとオプションのベアラトークン(提供されている場合)を入力します。

統合の認証情報を設定したら、ヒープにエクスポートするすべてのメッセージエンゲージメント、顧客行動、およびユーザーのイベントを確認し、**Launch Current**をクリックします。

![][5]{: style="max-width:90%;"}

[5]: {% image_buster /assets/img/heap/heap4.png %} 
