---
nav_title: Constructor
article_title: Constructor
description: "このリファレンス記事では、Braze と Constructor のパートナーシップについて説明します。このパートナーシップにより、Constructor の Offsite Product Discovery を使用して、Braze メッセージでパーソナライズされたおすすめ商品を動的に生成して配信することができます。"
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructor

> [Constructor](https://constructor.com/) は、AI と機械学習を利用してパーソナライズされた検索、レコメンデーション、ブラウジング体験を e コマースおよび小売 (店) の Web サイトに提供する、検索・商品発見プラットフォームです。

Braze と Constructor の統合により、Constructor の Offsite Product Discovery を使用して、Braze メッセージでパーソナライズされたおすすめ商品を動的に生成して配信することができます。

## ユースケース

- **放棄カートと注文後のフォローアップ**: ユーザーの行動とカートの内容に基づいて、おすすめ商品を動的に生成し、放棄カートのリマインダーや注文後の提案をパーソナライズして送信します。
- **放棄カートのアイテムと類似した商品のおすすめ**: ユーザーのカートに残されているアイテムに類似した商品を提案し、商品利用の継続と代替品の提案を可能にします。
- **最近見たアイテムのリマインダー**: 最近閲覧したがまだ購入していない商品についてユーザーに通知し、購入を完了するよう促す。
- **プロモーションキャンペーン**:季節的なセールや特別なオファーに向けてユーザーの好みに合わせてキュレートされたおすすめ商品が記載されたプロモーションメッセージをパーソナライズして配信します。
- **視覚的に類似した商品の提案**: ユーザーが最近閲覧した商品と視覚的に類似した商品を推奨し、ユーザーが好むかもしれない関連オプションを発見できるように支援します。

## 前提条件

| 必要条件 | 説明 |
|-------------|-------------|
| Constructor のアカウント | このパートナーシップを利用するには、Offsite Discovery サービスが有効化された Constructor アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Constructor のオンボーディングチームと協力して、統合プロセスを完了します。Web サイトやその他の関連データソースからの行動データが利用可能であり、おすすめ商品のパーソナライズが可能であることを確認します。Constructor のオンボーディングチームは、Braze メッセージでの使用に必要なHTML スニペットの設定もサポートします。

## Constructor の Offsite Discovery API の URL

Constructor の Offsite Discovery API の URL を使用して、商品の画像をレンダリングし、ユーザーを適切な商品詳細ページに誘導できます。以下は、エンドポイントの構造の内訳とその使用例です。

### 例

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img 
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200" 
    border="0" 
    alt="Shop Now" 
  />
</a>
```

### パラメータ

| パラメータ | 説明 |
|-------------|-------------|
| `position` | 推奨リスト内の特定の推奨アイテムのランキングを示します (例えば `position = 2`)。<br>![アイテムランキングの位置を設定します。] ({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | ユーザーの識別子を表し、推奨結果をパーソナライズさせるために重要です。`ui` パラメーターを Braze で顧客の `external_id` に設定します。省略された場合、コンストラクターはユーザー固有の推奨ではなく、一般的な推奨を返します。 |
| `pod_id` | 推奨事項の戦略と検索ルールを含むポッドの識別子 (たとえば、ベストセラー戦略を持つポッドは、パーソナライズされたベストセラーを生成します)。 |
| `key` | 当該顧客の Constructor でのインデックスキー。 |
| `style_id` | 商品カードに表示する画像、写真を決定します。たとえば、`style_ids` のそれぞれが、個別の商品カードの画像を表示します。 |
| `campaign_id` | メールキャンペーンの一意の ID。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### オプション入力

| インプット | 説明 |
|-------------|-------------|
| `item_id` | シード項目を表します。代替、補完、バンドルなど、項目間ベースの戦略に必要です。たとえば、メールの最初のアイテムをシードアイテムにして、後続のアイテムをは代替アイテムとして使用できます。 |
| `num_results` | メールに追加する商品の数。デフォルトは 10、最大で 100 です。例えば、`num_results = 3` は、3 つの推奨が追加されることを意味します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

