---
nav_title: Tinyclues
article_title:小さな手がかり
alias: /partners/tinyclues/
description:「この参考記事では、BrazeとTinycluesのパートナーシップについて概説しています。これにより、非常にユーザーフレンドリーなUIを使用して、より多くのターゲティングキャンペーンへの送信、新製品の機会の発見、収益の増加に役立つオーディエンス構築機能が提供されます。「
page_type: partner
search_tag:Partner

---

# 小さな手がかり

> [Tinycluesは](https://www.tinyclues.com/)、カスタマーエクスペリエンスを損なうことなくキャンペーンの数と収益を増やす機能と、オンラインとオフラインの両方でCRMキャンペーンのパフォーマンス追跡する分析機能を提供するオーディエンス構築機能です。

BrazeとTinycluesの統合により、ユーザーはより的を絞ったキャンペーンを送信し、新製品の機会を見つけ、非常にユーザーフレンドリーなUIを使用して収益を上げることができ、より的を絞ったキャンペーンを送信したり、新製品の機会を見つけたり、収益を上げたりすることができます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Tinyclues アカウント | このパートナーシップを利用するには、Tinycluesアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2}

## データインポート統合

Braze と Tinyclues を統合するには、Tinyclues プラットフォームを設定し、既存の Tinyclues キャンペーンをエクスポートして、今後のキャンペーンでユーザーをターゲットにするために使用できるユーザーコホートSegment を Braze で作成する必要があります。

### ステップ1:Braze データインポートキーを取得

**Braze で \[**パートナー統合] > \[**テクノロジーパートナー****] に移動し、\[Tinyclues] を選択します。** 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。<br><br>![][6]{: style="max-width:90%;"} 

統合を完了するには、データインポートキーと REST エンドポイントを Tinyclues データ運用チームに提供する必要があります。その後、Tinycluesが接続を確立し、セットアップが完了した後に連絡します。

### ステップ2:Tinyclues プラットフォームからキャンペーンをエクスポートする

Braze で使用する Tinyclues ユーザーのコホートを作成するたびに、まず Tinyclues プラットフォームからそれをエクスポートする必要があります。

**Tinyclues で、エクスポートするキャンペーンを選択し、「キャンペーンをエクスポート」をクリックします。**エクスポート時に、オーディエンス自動的に Braze アカウントにアップロードされます。

![][1]

### ステップ3:Tinyclues カスタムオーディエンスからSegment を作成する

**Braze で \[Segment] に移動し、Tinyclues **コホートセグメントに名前を付け**、フィルターとして Tinyclues コホートを選択します。**ここから、含めたいTinycluesコホートを選択できます。TinycluesコホートSegment を作成したら、キャンペーンまたはキャンバスを作成するときにオーディエンスフィルターとして選択できます。

![][3]{: style="max-width:90%;"}<br><br>
![Braze Segment ビルダーでは、ユーザー属性フィルター「Tinyclues コホート」が「含む」と「Primary コホート」に設定されています。][4]{: style="max-width:90%;"}

コホートを見つけるのに苦労していませんか？ガイダンスについては、[トラブルシューティングセクションをご覧ください](#troubleshooting)。 

## このインテグレーションを使用する

Tinyclues Segment を使用するには、Braze キャンペーンまたは Canvas を作成し、そのSegment をターゲットオーディエンスとして選択します。 

![Brazeキャンペーンビルダーのターゲティングステップでは、「Segment 別にユーザーをターゲットにする」フィルターが「Tinycluesコホート」に設定されています。][5]{: style="max-width:90%;"}

## トラブルシューティング

リストの中から適切なコホートを見つけるのに苦労していませんか？Tinyclues でキャンペーン詳細を表示し、**エクスポートファイル名を確認して名前を確認します**。

![キャンペーン詳細ページの下部には、あなたのコホート名が表示されます。][2]{: style="max-width:30%;"}

まだオーディエンス取得に問題がありますか？追加のサポートについては、[Tinyclues チームにお問い合わせください](mailto:support@tinyclues.com)。

[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %}
[2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %}
[3]: {% image_buster /assets/img/tinyclues/tinyclues_3.png %}
[4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %}
[5]: {% image_buster /assets/img/tinyclues/tinyclues_5.png %}  
[6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  