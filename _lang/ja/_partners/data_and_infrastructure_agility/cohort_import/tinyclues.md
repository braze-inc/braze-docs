---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "この参考記事では、BrazeとTinycluesのパートナーシップについて概説している。Tinycluesは、オーディエンス構築機能を提供し、よりターゲティングされたキャンペーンへの送信、新しい製品機会の発見、驚くほどユーザーフレンドリーなUIを使用した収益の向上を支援する。"
page_type: partner
search_tag: Partner

---

# Tinyclues

> [Tinyclues](https://www.tinyclues.com/) はオーディエンス構築機能であり、オンラインとオフラインの両方で CRM キャンペーンのパフォーマンスを追跡するために、カスタマーエクスペリエンスと分析に悪影響を及ぼすことなく、キャンペーン数と収益を増加できます。

BrazeとTinycluesの統合は、より良いCRMプランニングと戦略への道をユーザーに提供し、ユーザーはよりターゲットを絞ったキャンペーンを送信し、新しい製品機会を見つけ、信じられないほどユーザーフレンドリーなUIを使用して収益を向上させることができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Tinycluesアカウント | このパートナーシップを利用するには、Tinycluesのアカウントが必要だ。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## データ・インポートの統合

BrazeとTinycluesを統合するには、Tinycluesプラットフォームを設定し、既存のTinycluesキャンペーンをエクスポートし、今後のキャンペーンでユーザーをターゲットにするために使用できるユーザーコホートセグメントをBrazeで作成する必要がある。

### ステップ1:Brazeデータインポートキーを取得する

Braze で [**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Tinyclues**] を選択します。 

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**テクノロジーパートナー**] は [**統合**] にあります。
{% endalert %}

ここで、RESTエンドポイントを見つけて、Brazeデータインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。<br><br>![][6]{: style="max-width:90%;"} 

統合を完了するには、データインポートキーとRESTエンドポイントをTinycluesデータオペレーションチームに提供する必要がある。その後、Tinycluesが接続を確立し、セットアップ完了後に連絡を取る。

### ステップ2:Tinycluesプラットフォームからキャンペーンをエクスポートする

Braze で使用する Tinyclues ユーザーのコホートを作成するには、まず Tinyclues プラットフォームからエクスポートする必要があります。

Tinyclues でエクスポートするキャンペーンを選択し、[**Export Campaigns**] をクリックします。エクスポートすると、オーディエンスは自動的にBrazeアカウントにアップロードされる。

![][1]

### ステップ3:Tinycluesカスタムオーディエンスからセグメントを作成する

Brazeで「**セグメント**」に移動し、Tinycluesコホートセグメントに名前を付け、フィルターとして**Tinycluesコホートを**選択する。ここから、どのTinycluesコホートを含めるかを選択できる。Tinycluesコホートセグメントを作成した後、キャンペーンやキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。

![][3]{: style="max-width:90%;"}<br><br>
![Braze セグメントビルダーで、ユーザー属性フィルター「Tinyclues cohort」が「次を含む」と「Primary cohort」に設定されている。][4]{: style="max-width:90%;"}

コーホートの所在がわからず困っている？「[トラブルシューティング](#troubleshooting)」セクションでガイダンスをご確認ください。 

## この統合を使用する

Tinycluesセグメントを使用するには、Brazeキャンペーンまたはキャンバスを作成し、ターゲットオーディエンスとしてセグメントを選択する。 

![Braze キャンペーンビルダーのターゲティングステップで、[セグメントを基準にユーザーをターゲットに設定] フィルターが「Tinyclues cohort」に設定されている。][5]{: style="max-width:90%;"}

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合することができる。匿名ユーザーは、`device_id` 。元々匿名ユーザーとして作成された識別子ユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければならない。

## トラブルシューティング

リスト内で適切なコホートを見つけるのに苦労している？Tinyclues でキャンペーンの詳細を表示し、[**Export File Name**] をオンにして名前を確認します。

![キャンペーン詳細ページの下部にコホート名が表示されている。][2]{: style="max-width:30%;"}

これでもオーディエンスの取得で問題が解決しない場合は、その他のサポートについては、[Tinycluesチームに](mailto:support@tinyclues.com)問い合わせを。

[1]: {% image_buster /assets/img/tinyclues/tinyclues_1.png %}
[2]: {% image_buster /assets/img/tinyclues/tinyclues_2.png %}
[3]: {% image_buster /assets/img/tinyclues/tinyclues_3.png %}
[4]: {% image_buster /assets/img/tinyclues/tinyclues_4.png %}
[5]: {% image_buster /assets/img/tinyclues/tinyclues_5.png %}  
[6]: {% image_buster /assets/img/tinyclues/tinyclues_6.png %}  