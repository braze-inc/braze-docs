---
nav_title: Phrase
article_title: Phrase
alias: /partners/phrase/
description: "このリファレンス記事では、Brazeと、ローカライゼーション向けクラウドベースのソフトウエアであるフレーズとの提携について概説します。このインテグレーションを使用すると、Braze インターフェイスを離れることなく、メール テンプレートとコンテンツブロックを変換できます。"
page_type: partner
search_tag: Partner

---

# Phrase 

> [フレーズ](https://phrase.com/)は、ローカライゼーションマネジメントのためのクラウドベースのソフトです。句は自動化された翻訳ワークフローを有効にし、アジャイルチームの継続的なローカライゼーションをサポートします。

フレーズとBrazeインテグレーションを使用すると、Braze インターフェイスを離れることなく、メール テンプレートとコンテンツブロックを変換できます。Braze向けフレーズTMSインテグレーションでは、シームレスなローカライゼーションでカスタマーエンゲージメントを高め、新たなマーケットへの成長を牽引できます。

## 前提条件

| 要件 | 説明 |
| --- | --- |
| フレーズTMSアカウント | フレーズTMS Ultimate またはEnterprise アカウントは、この提携の前進タグe を考慮する必要があります。 |
| Braze REST API キー | すべての権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST エンドポイント | [Your REST エンドポイント URL][1].エンドポイントは、インスタンスのBraze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

## ステップ1:TMSフレーズ設定

フレーズで、**Settings > Integrations > Connectors > New** に移動します。

1. コネクションの名前を指定し、型を**Braze**に変更します。<br><br>
2. REST API キーとBraze REST エンドポイントを入力します。<br><br>
3. リンクされたコンテンツブロックを持つメール テンプレートをどのように読み込むかを選択します。 
- 選択メール テンプレートのみ
- コンテンツブロックを含める<br><br>
4. コネクターがメール テンプレート変換をエクスポートする方法を選択します。 
- 新規アイテムの作成
- Originアルアイテム
  - すべてのアイテムをOriginすると、同じテンプレート/ブロックに翻訳がエクスポートされます。言語Segments は、提供された属性によって定義されます。<br><br>
    {% raw %}
    元のアイテムが選択されている場合は、言語属性を入力します。言語属性はif/elsif引き数の言語を定義する。オリジナルのアイテムオプションを使用する場合は、以下のように構造化する必要があります。

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
    または、アサインキー/アサイン値m アプリリングを使用します。
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
    上記のリキッドは厳守する必要がありますが、言語属性、言語、鍵、数値は調整可能です。<br><br>
    各言語コードは1 回のみ使用できますが、複数の言語を1 つのSegmentに使用できます。たとえば、次のようになります。
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. **Test connection**をクリックします。接続が成功すると、耳にチェックマークがアプリされます。アイコンの上にマウスポインタを置くと、詳細が表示されます。<br><br>
7. 最後に、**Save**をクリックします。このコネクタは、**Connectors**ページで使用できます。

## ステップ3:文節に内容を送信し、Brazeに書き戻す

1. まず、[submitter portal](https://support.phrase.com/hc/en-us/articles/5709602111132)を設定して、サブミッターがオンラインリポジトリから直接リクエストにファイルを追加できるようにします。<br><br>
2. 指定されたワークフロー状態の変更が検出されたときにフレーズTMS が自動的に新しいプロジェクトを作成するようにするには、[Automated Project Creation (APC)](https://support.phrase.com/hc/en-us/articles/5709647363356) を使用します。<br><br>
3. 選択したコンテンツ項目は、APC の初回実行時にインポートされます。

[Connector API](https://cloud.memsource.com/web/docs/api#) は、ステップを自動化できます。それ以外の場合は、UI を使用して手動で実行します。[Webフック](https://support.phrase.com/hc/en-us/articles/5709693398812) を使用して、フレーズTMS が特定のイベント(たとえば、ジョブステータスの変更) についてサードパーティシステムに通知するようにすることができます。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
