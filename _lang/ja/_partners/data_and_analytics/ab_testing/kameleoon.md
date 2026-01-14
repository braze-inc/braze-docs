---
nav_title: カメレオン
article_title: カメレオン
description: "カメレオオンとBrazeを統合する方法を学ぶ"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# カメレオン

>[Kameleoon](https://www.kameleoon.com)は、1つの統一プラットフォームにおいて、実験、AIパワードパーソナライゼーション、および機能マネジメント機能を備えた最適化ソリューションです。

## 前提条件

開始する前に、次のものが必要になります。

| 要件 | 説明 |  
| --- | --- |  
| カメレオン勘定 | この提携の前進タグeをとるにはカメレオンの勘定が必要である。|  
| Braze アカウント| Web ページに [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) が統合されたアクティブな Braze アカウント。また、行動プロパティ セグメンテーションを有効にする必要があります。要求するには、[考慮事項](#considerations)を参照してください。|  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## ユースケース

カメレオンはカスタムイベントをBrazeに送り、実験やパーソナライゼーション キャンペーンに参加しているユーザーを特定し、より正確なターゲティングとパーソナライズされた メッセージングを可能にします。

## カメレオオンの統合

この統合は、Kameleoon のengine.js を介してJavaScript トラッカーとして実行されます。カメレオンのプラットフォームからすぐに有効にすることができます。

### ステップ 1: Kameleoon Integrations ページに移動します

カメレオンアプリで、サイドバーの**Admin**を選択し、次に**Integrations**を選択します。

![カメレオオンプラットフォームの管理パネル。]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### ステップ 2:Braze工具の取り付け

デフォルトでは、Brazeツールはインストールされていません。Brazeのアイコンを探し、**ツールをインストールします**を選択します。![下向き矢印の付いた灰色の正方形。]({% image_buster /assets/img/kameleoon/img_2.png %})

Brazeツールを有効にするプロジェクトを選択します。これにより、カメレオオンデータがBrazeに正しくレポートされます。

![カメルーンのBrazeツールアイコン。]({% image_buster /assets/img/kameleoon/img_3.png %})

ツールを設定したら、**Validate**を選択し、設定パネルを閉じます。次に、Brazeツールのアイコンの横に**ON**トグルが表示されます。これには、ツールが設定されているプロジェクトの数も含まれます。

![Brazeツールは、"On"をカメレオオンで切り替えました。]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}  
この機能はベータ版です。[Kameleoon ベータプログラム](https://help.kameleoon.com/account-and-team-management/join-beta-program/)に参加して、この統合の使用を開始します。  
{% endalert %}  
    
### ステップ 3:Brazeとカメレオン・キャンペーンの提携

#### グラフィック/コードエディタで

実験を終了するには、**Integrations**ステップを選択してBrazeを"トラッキングツールとして設定し、**Braze**を選択します。

![カメレオンの統合ダッシュボードには、有効な統合Brazeを含む、利用可能なすべての統合が表示されます。]({% image_buster /assets/img/kameleoon/img_5.png %})

Brazeは、本番に入る前にサマリーに記載されます。カメレオンは自動的にデータをBrazeに送信し、Brazeでの解析やセグメンテーションに使用できるようになります。

##### カスタマイズの作成

**Personalization Creation** ページでは、レポートツールの中からBrazeを選択して、レポートをカスタマイズできます。

![「ヒープ」、「ミックスパネル」、「透明度」などの統合を表示し、Brazeを選択した状態の「レポートツール」セクション。]({% image_buster /assets/img/kameleoon/img_6.png %})

##### 機能フラグ作成

**Integrations**で、フィーチャーフラグ環境でのインテグレーションを設定します。アクティブにする環境で有効にします。

![Kameleoon のFeature Flag(機能フラグ)ページで、利用可能な統合があります。パートナーごとに、"Delivery rules"および"Feature experiments"の2つの切り替えるがあります。]({% image_buster /assets/img/kameleoon/img_7.png %})

##### 結果ページ

Brazeを実験のレポートツールとして設定した後、**Experiment configuration**メニューのKameleoon resultsページで選択(または選択解除)できます。

{% alert note %}  
この統合には[ハイブリッド実装](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) が必要で、ウェブSDKs とのみ互換性があります。
{% endalert %}

![結果ページのサイドパネルはKameleoon にあります。]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

試験に関連付けられたレポートツールが表示されます。この選択を編集するには、**編集**を選択します。

### ステップ 4: Braze でのカメレオオンデータの分析と活用

統合が設定されると、Kameleoon は`kameleoon_exposure` というカスタムイベントを**Experiment name**、**Experiment ID**、**Variation name**、**Variation ID** などのプロパティーとともにBraze に送信します。

![カスタムイベント ユーザーはBrazeにログインし、カメレオオンからBrazeが受け取ったイベントの報酬読み込むの例を示します。]({% image_buster /assets/img/kameleoon/img_9.png %})

次に、このデータをカスタムイベントs で表示し、カスタムイベント レポートs を作成してカメレオオンのキャンペーン露出を識別し、イベントプロパティーに基づいてセグメンテーションを有効にします。カスタムイベント s は、[ アクション Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups)、[ アクション ベースのトリガーs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) または[ Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) を使用して、後続またはリンクされたキャンペーンs およびキャンバスを作成するときに使用できます。

さらに、これらの事象は、[Currents カスタムイベントオブジェクト]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/)を介してアクセス可能であり、包括的なレポートおよび解析を可能にする。

## 考慮事項

### リクエストイベントプロパティのセグメンテーション

イベントプロパティセグメンテーションを使用するには、事前に Braze で有効にしておく必要があります。次のテンプレートを使用して、Braze CSM またはサポートチームに問い合わせてください。

   <table>
   <thead>
      <tr>
         <th>フィールド</th>
         <th>詳細</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>件名</strong></td>
         <td>Kameleoon 統合のイベントプロパティセグメンテーションを有効にするリクエスト</td>
      </tr>
      <tr>
         <td><strong>本文</strong></td>
         <td>
         Braze チームのみなさん、こんにちは。<br><br>
         Kameleoon&lt;> Braze インテグレーションから送られてきたイベントのイベントプロパティ セグメンテーションを可能にしたいと考えています。詳細は次のとおりです。<br><br>
         - <strong>イベント名:</strong>カメレオン<br>
         - <strong>イベントプロパティ:</strong> <code>kameleoon_campaign_name</code>,<code>kameleoon_variation_name</code><br><br>
         アカウントでプロパティが有効になったらご確認ください。<br><br>
         ありがとうございます。
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Braze データポイント

カメレオオンからBrazeに送信されるカスタムイベント(セグメンテーションで有効になっているすべてのイベントプロパティーを含む) は、Brazeインスタンス内のデータポイントs を記録します。