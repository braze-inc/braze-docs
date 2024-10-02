---
nav_title: テニクル
article_title: テニクル
alias: /partners/tinyclues/
description: "この参考記事では、BrazeとTinycluesのパートナーシップについて概説している。Tinycluesは、オーディエンス構築機能を提供し、よりターゲティングされたキャンペーンへの送信、新しい製品機会の発見、驚くほどユーザーフレンドリーなUIを使用した収益の向上を支援する。"
page_type: partner
search_tag: Partner

---

# テニクル

> [Tinycluesは](https://www.tinyclues.com/)、顧客体験を損なうことなくキャンペーン数と収益を増加させる機能と、オンラインとオフラインの両方でCRMキャンペーンのパフォーマンスを追跡する分析機能を提供するオーディエンス構築機能である。

BrazeとTinycluesの統合は、より良いCRMプランニングと戦略への道をユーザーに提供し、ユーザーはよりターゲットを絞ったキャンペーンを送信し、新しい製品機会を見つけ、信じられないほどユーザーフレンドリーなUIを使用して収益を向上させることができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Tinycluesアカウント | このパートナーシップを利用するには、Tinycluesのアカウントが必要だ。 |
{: .reset-td-br-1 .reset-td-br-2}

## データ・インポートの統合

BrazeとTinycluesを統合するには、Tinycluesプラットフォームを設定し、既存のTinycluesキャンペーンをエクスポートし、今後のキャンペーンでユーザーをターゲットにするために使用できるユーザーコホートセグメントをBrazeで作成する必要がある。

### ステップ1:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Tinycluesを**選択する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵の生成後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。<br><br>![][6]{: style="max-width:90%;"} 

統合を完了するには、データインポートキーとRESTエンドポイントをTinycluesデータオペレーションチームに提供する必要がある。その後、Tinycluesが接続を確立し、セットアップ完了後に連絡を取る。

### ステップ2:Tinycluesプラットフォームからキャンペーンをエクスポートする

Brazeで使用するTinycluesユーザーのコホートを作成するには、まずTinycluesプラットフォームからエクスポートする必要がある。

Tinycluesで、エクスポートしたいキャンペーンを選択し、**キャンペーンのエクスポートを**クリックする。エクスポートすると、オーディエンスは自動的にBrazeアカウントにアップロードされる。

![][1]

### ステップ3:Tinycluesカスタムオーディエンスからセグメントを作成する

Brazeで「**セグメント**」に移動し、Tinycluesコホートセグメントに名前を付け、フィルターとして**Tinycluesコホートを**選択する。ここから、どのTinycluesコホートを含めるかを選択できる。Tinycluesコホートセグメントを作成した後、キャンペーンやキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。

![][3]{: style="max-width:90%;"}<br><br>
![Brazeセグメントビルダーで、ユーザー属性フィルター「Tinyclues cohort」が「includes」と「Primary cohort」に設定されている。][4]{: style="max-width:90%;"}

コーホートの所在がわからず困っている？[トラブルシューティングの](#troubleshooting)セクションを参照してほしい。 

## この統合を使う

Tinycluesセグメントを使用するには、Brazeキャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてセグメントを選択する。 

![ターゲティングステップのBrazeキャンペーンビルダーで、"Target users by segment "フィルターが "Tinyclues cohort "に設定されている。][5]{: style="max-width:90%;"}

## トラブルシューティング

リスト内で適切なコホートを見つけるのに苦労している？Tinycluesでキャンペーンの詳細を表示し、**Export File Nameを**チェックして名前を確認する。

![キャンペーン詳細ページの下部には、あなたのコホート名が表示される。][2]{: style="max-width:30%;"}

視聴者の検索にまだ問題があるのか？その他のサポートについては、[Tinycluesチームに](mailto:support@tinyclues.com)問い合わせを。

[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %}
[2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %}
[3]: {% image_buster /assets/img/tinyclues/tinyclues_3.png %}
[4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %}
[5]: {% image_buster /assets/img/tinyclues/tinyclues_5.png %}  
[6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  