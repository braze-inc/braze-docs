---
nav_title: Phrase
article_title:フレーズ
alias: /partners/phrase/
description:「この参考記事では、BrazeとクラウドベースのローカライゼーションソフトウェアであるPhraseのパートナーシップについて概説しています。この統合により、Braze インターフェイスを離れることなくメールテンプレートとコンテンツブロックを翻訳できます。「
page_type: partner
search_tag:Partner

---

# フレーズ 

> [Phrase](https://phrase.com/) は、ローカライゼーション管理用のクラウドベースのソフトウェアです。Phraseは自動翻訳ワークフローを可能にし、アジャイルチームの継続的なローカライゼーションをサポートします。

フレーズとBrazeの統合により、Brazeインターフェイスを離れることなくメールテンプレートとコンテンツブロックを翻訳できます。Braze 用の Phrase TMS 統合により、シームレスなローカライゼーションによってカスタマーエンゲージメントを高め、新しい市場への成長を促進できます。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| フレーズ TMS アカウント | このパートナーシップを利用するには、Phrase TMS Ultimateまたはエンタープライズアカウントが必要です。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| Braze REST エンドポイント | [あなたの REST エンドポイント URL][1]。エンドポイントは、インスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

## ステップ1:フレーズ TMS 設定

Phraseで、「**設定」>「インテグレーション」>「コネクター」>「新規**」に移動します。

1. 接続の名前を指定し、タイプを **Braze** に変更します。<br><br>
2. REST API キーと Braze REST エンドポイントを入力します。<br><br>
3. コネクターがリンクされたコンテンツブロックを含むメールテンプレートをインポートする方法を選択します。 
- 選択したメールテンプレートみ
- コンテンツブロックを含める<br><br>
4. コネクタがメールテンプレート翻訳をエクスポートする方法を選択します。 
- 新しい商品を作成
- オリジナルアイテム
  - オリジナルアイテムは、翻訳を同じテンプレート/ブロックにエクスポートします。言語セグメントは、指定された属性によって定義されます。<br><br>
    {% raw %}
    元のアイテムを選択した場合は、言語属性。言語属性は、if/elsif 引数の言語を定義します。オリジナル商品オプションを使用する場合は、以下に示すように構成する必要があります。

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
    または、キー/値の割り当てマッピングを使用する:
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
    上記のLiquidに厳密に従う必要がありますが、言語属性と言語、キー、値は調整可能です。<br><br>
    各言語コード一度しか使用できませんが、1つのSegment に複数の言語を使用できます。次に例を示します。
    ```liquid
    {% elsif {{custom_attribute.${attribute_name}}} == 'de-DE' or {{custom_attribute.${attribute_name}}} == 'de-AT' or {{custom_attribute.${attribute_name}}} == 'de-CH' %}
    {% endraw %}
    ```
5. \[**接続をテスト**] をクリックします。接続が成功すると、チェックマークが表示されます。アイコンにカーソルを合わせると、詳細が表示されます。<br><br>
7. 最後に、\[**保存**] をクリックします。このコネクターは「**コネクター**」ページにあります。

## ステップ3:コンテンツを Phrase に送信し、Braze にエクスポートして戻す

1. まず、[提出者がオンラインリポジトリから直接リクエストにファイルを追加できるように提出者ポータルを設定します](https://support.phrase.com/hc/en-us/articles/5709602111132)。<br><br>
2. [自動プロジェクト作成（APC）](https://support.phrase.com/hc/en-us/articles/5709647363356)を使用すると、指定されたワークフロー状態の変更が検出されたときに Phrase TMS が自動的に新しいプロジェクトを作成するようにできます。<br><br>
3. 選択したコンテンツ項目は、APC を初めて実行したときにインポートされます。

[Connector API](https://cloud.memsource.com/web/docs/api#) は、通常は UI を使用して手動で実行する手順を自動化できます。[Webhook](https://support.phrase.com/hc/en-us/articles/5709693398812) を使用すると、特定のイベント（ジョブステータス変更など）について Phrase TMS がサードパーティシステムに通知するように設定できます。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
