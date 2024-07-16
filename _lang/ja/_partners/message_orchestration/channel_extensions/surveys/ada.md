---
nav_title: Ada
article_title:エイダ
description:「この参考記事では、顧客との対話を自動化およびパーソナライズするAI搭載プラットフォームであるBrazeとAdaのパートナーシップについて概説しています。この統合により、自動化されたAda会話から収集されたデータでユーザープロファイルを補強できます。「
alias: /partners/ada/
page_type: partner
search_tag:Partner

---

# エイダ

> [Adaは](https://ada.cx)、会話型AIを使用してカスタマーエクスペリエンスを自動化およびパーソナライズするブランドインタラクションプラットフォームです。Adaを使用すると、ユーザーデータに基づいてメッセージングやキャンペーンをSegment したり、会話を測定および分析して新しい機会を発見したり、顧客とのチャットから得た洞察を利用してユーザープロファイルを充実させたりできます。  

BrazeとAdaの統合により、自動化されたAda会話から収集されたデータでユーザープロファイルを強化できます。Adaチャット中に収集した情報に基づいてカスタムユーザー属性を設定し、Ada会話の特定の時点でBrazeでカスタムイベントを記録できます。AdaチャットボットをBrazeに接続することで、ブランドについて消費者が尋ねる質問に基づいて、または積極的に会話を始めて、消費者の興味や好みについて詳しく知ることができるような質問をすることで、消費者についてより深く知ることができます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Ada アカウント | このパートナーシップを利用するには、Braze および Answer Utilities アプリケーションが有効になっている [Ada](https://ada.cx) アカウントが必要です。 |
| Braze REST API キー | `users.track`権限のあるBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Braze と Ada の統合の一般的な使用例は次のとおりです。
- 消費者が Ada ボットと行ったさまざまなやり取りを Braze のカスタムイベントとして追跡することで、どの顧客が Ada でプロアクティブなキャンペーンに参加したか、サポートエージェントに引き継がれたか、特定の質問をしたか、特定のアクションを完了したかを把握できます。
- 消費者の興味、好み、人口統計などについて尋ねます。カスタム属性を使用して、この新しい情報で Braze のプロファイルを自動的に更新します。

## 統合

Braze と Ada を統合するには、まず Ada ダッシュボードで Braze アプリケーションを設定し、Ada チームと協力して Ada 埋め込みスクリプトにユーザー ID メタ変数を設定する必要があります。次に、Braze ブロックを Answer エディターの Braze に情報を送信したい場所 (イベントまたは属性) にドラッグします。

### ステップ1:Ada で Braze アプリセットアップする

Ada ダッシュボードで、**\[設定] > \[インテグレーション] > \[Handoff インテグレーション]** に移動します。

Braze の横にある「**接続**」をクリックし、次の情報を入力します。
- **REST エンドポイント**:Braze REST エンドポイント URL を入力します。 
- **API キー**:Braze REST API キーを入力します。 
- **アプリ ID**: Ada チャッターを関連付けたいアプリ ID を入力します。

### ステップ2:Braze から Ada に識別子渡す

確認するには're updating the correct user, you'、Adaチームに連絡する必要があります。Brazeから識別子を受け取れるように、Ada埋め込みスクリプトに必要な変更を加えるのを手伝ってもらえます。このインテグレーションは外部 ID を受け入れるように設計されていますが、ユーザーエイリアスなどの他の識別子を渡すこともできます。 

### ステップ3:Braze ブロックを該当する回答にドロップしてください

Braze ブロックを使用するには、ブロックドロワーから適切な Answer にドラッグし、アクションを選択します。Braze ブロックでは、次の 2 つのアクションを実行できます。
* トラックイベント
* \[属性を更新]

{% tabs local %}
{% tab track event %}

#### 回答ユーティリティブロック

1. Answer UtilitiesブロックブロックドロワーからBrazeブロック真上にドラッグします。 
2. 「**日付をフォーマット**」アクションを選択し、「**日付**」`today` フィールドに入力します。
3. 「**出力形式**」`iso` フィールドに入力します。「**応答を変数として保存**」で、「**フォーマットされた日付**」`iso_time` という変数を作成します。

![The Answer Utilities block with fields populated as described in preceding text.]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### Braze ブロック

**4。**Braze ブロックの \[**外部 ID**] フィールドに、前のステップで Ada `external_id` が設定したメタ変数を入力します。<br>
**5。****イベント名フィールドに**、トラッキングしたいBrazeイベントの名前を入力します。<br>
**6。**「**イベントの時間**」フィールドに、Answer Utilities `iso_time` ブロックで作成した変数を入力します。<br>
**7。**Braze へのイベントの投稿中に問題が発生した場合は、フォールバックの回答を選択してください。

![The Braze block with fields populated as described in preceding text.]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab update attribute %}

#### Braze ブロック

1. Braze ブロックの \[**外部 ID**] フィールドに、前のステップで Ada `external_id` が設定したメタ変数を入力します。 
2. 「**属性名**」フィールドに、トラッキングしたいBraze属性の名前を入力します。 
3. 「**属性値**」フィールドに、設定する値 (テキスト、変数、またはテキストと変数の組み合わせ) を入力します。 
4. Brazeへの属性投稿中に問題が発生した場合は、フォールバック回答を選択してください。

![The Braze block with fields populated as described in preceding text.]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}