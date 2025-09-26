---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "このリファレンス記事では、Braze と Phrase のパートナーシップについて説明します。Phrase はクラウドベースのローカライゼーションソフトウェアです。この統合により、Braze インターフェイスを離れることなく、メールテンプレートとコンテンツブロックを翻訳できます。"
page_type: partner
search_tag: Partner

---

# Phrase 

> [Phrase](https://phrase.com/) はローカライゼーション管理のためのクラウドベースのソフトウェアです。句は自動化された翻訳ワークフローを有効にし、アジャイルチームの継続的なローカライゼーションをサポートします。

_この統合は Phrase によって管理されます。_

## 統合について

Phrase と Braze の統合により、Braze インターフェイスを離れることなく、メールテンプレートとコンテンツブロックを翻訳できます。Braze 向け Phrase TMS 統合により、シームレスなローカライゼーションでカスタマーエンゲージメントを高め、新しい市場への拡大を促進できます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| Phrase TMS アカウント | この提携を利用するには、Phrase TMS Ultimate または Enterprise アカウントが必要です。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

## ステップ1:Phrase TMS の設定

Phraseで、**[Settings] > [Integrations] > [Connectors] > [New]** の順に進みます。

1. コネクションの名前を指定し、型を**Braze**に変更します。<br><br>
2. REST API キーとBraze REST エンドポイントを入力します。<br><br>
3. コネクターがメール テンプレートおよびリンクされたコンテンツブロックをインポートする方法を選択します。 
- 選択メール テンプレートのみ
- コンテンツブロックを含める<br><br>
4. コネクターがメール テンプレート変換をエクスポートする方法を選択します。 
- 新規アイテムの作成
- 元のアイテム
  - すべてのアイテムをOriginすると、同じテンプレート/ブロックに翻訳がエクスポートされます。言語Segments は、提供された属性によって定義されます。<br><br>
    {% raw %}
    元のアイテムが選択されている場合は、言語属性を入力します。言語属性はif/elsif引き数の言語を定義する。元のアイテムのオプションを使用している場合は、次のように構造化する必要があります。

    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
    danish content
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
    portuguese content
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
    swedish content
    {% else %}
    Original content
    {% endif %}
    ```
    または、assign キー/値マッピングを使用します。
    ```liquid
    {% if {{custom_attribute.${attribute_name}}} == 'da-DK' %}
      {% assign abc_key1 = "danish_value1" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'pt-PT' %}
      {% assign abc_key = "portuguese value" %}
    {% elsif {{custom_attribute.${attribute_name}}} == 'sv-SE' %}
      {% assign abc_key = "swedish value" %}
    {% else %}
      {% assign abc_key = "Source language value" %}
    {% endif %}
    ```
    上記の Liquid に厳密に従う必要がありますが、言語属性と言語、キー、および値は調整可能です。<br><br>
    各言語コードは1 回のみ使用できますが、複数の言語を1 つのSegmentに使用できます。たとえば、次のようになります。
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. [**Test connection**] をクリックします。接続に成功するとチェックマークが表示されます。アイコンの上にマウスポインタを置くと、詳細が表示されます。<br><br>
7. 最後に、**Save**をクリックします。このコネクターは [**Connectors**] ページで使用可能になります。

## ステップ3:コンテンツを Phrase に送信して Braze に再びエクスポートする

1. まず [submitter portal](https://support.phrase.com/hc/en-us/articles/5709602111132) を設定して、送信者がオンラインリポジトリからファイルを直接リクエストに追加できるようにします。<br><br>
2. 指定されたワークフロー状態の変更が検出されたときに Phrase TMS が新しいプロジェクトを自動的に作成するようにするには、[Automated Project Creation (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356) を使用します。<br><br>
3. 選択されているコンテンツアイテムは、APC の初回実行時にインポートされます。

[Connector API](https://cloud.memsource.com/web/docs/api#) は、ステップを自動化できます。それ以外の場合は、UI を使用して手動で実行します。[webhook](https://support.phrase.com/hc/en-us/articles/5709693398812) を使用して、Phrase TMS が特定のイベント (ジョブのステータス変更など) についてサードパーティのシステムに通知するようにできます。


