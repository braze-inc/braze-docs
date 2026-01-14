---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "この参考記事では、BrazeとSheetlabsの提携について概説している。Sheetlabsは、スプレッドシートから得たデータを使ってマーケティング・キャンペーンをパーソナライズできるサービスである。"
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/) は、スプレッドシートを、強力で明確に文書化された API に変換できるプラットフォームです。Google SheetsやExcelからデータをインポートしてAPI化し、そのAPIをBrazeなどの他のアプリケーションで使うことができる。
_この統合は Sheetlabs によって管理されます。_

## 統合について

SheetlabsとBrazeの統合により、[コネクテッドコンテンツを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/)使用して、BrazeマーケティングキャンペーンにSheetlabs APIを含めることができる。これは、Googleスプレッドシート（マーケティングチームが直接更新する）とBrazeテンプレートの橋渡しによく使われる。これにより、翻訳やカスタム属性の大規模なセットなど、Brazeテンプレートでより多くのことを実現できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Sheetlabs アカウント | このパートナーシップを活用するには、[Sheetlabs アカウント](https://sheetlabs.com/)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

BrazeとSheetlabsの統合により、以下のユースケースを実現できる：

1. **マーケターアクセスとBrazeキャンペーンアクセスを分離する**：チームによっては、すべてのスタッフにBrazeのテンプレートやコンテンツを直接設定するためのアクセス権を与えたくない場合もある。その代わり、スタッフはスプレッドシートでマーケティング・コンテンツを更新することを望んでいる。SheetlabsはスプレッドシートとBrazeの橋渡しをし、リアルタイムで更新できる。
2. **翻訳**:Brazeのテンプレートはネイティブに翻訳をサポートしていない。複数の言語をサポートしたい場合は、複数のテンプレートを作成する必要がある。Sheetlabs と Braze を併用することで、1つの Braze テンプレートを多言語に翻訳できます。
3. **カスタム属性の拡張**:Brazeには、設定可能なカスタム属性が一定数用意されている。SheetlabsをBrazeと併用することで、この最初の割り当てを超えてカスタム属性を追加することができる。

これらのユースケースの詳細については、[Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/) を参照してください。

## 統合

### ステップ1:スプレッドシートをSheetlabsにインポートする

Sheetlabs では、Excel スプレッドシートをアップロードするか、Google アカウントをリンクして Google スプレッドシートをインポートします。 

- エクセルのスプレッドシートをインポートするには、メニューバーの「**Data Tables**」をクリックし、「**Import from CSV/Excel**」をクリックする。
- Google スプレッドシートからインポートするには、メニューバーの [**Data Tables**] をクリックし、次に [**Import from Google**] をクリックします。その後、Google ログイン認証情報を入力してスプレッドシートをインポートする必要があります。

また、Google Sheetを同期させておくこともできる。つまり、SheetlabsはGoogle Sheetに変更があった場合、自動的に最新のデータを取得する。

BrazeのユーザーIDをスプレッドシートに含めるか、後で検索に使えるようにしておくこと。

### ステップ2:SheetlabsでAPIを作成する

次に Sheetlabs で **[APIs] > [Create API]** に移動し、API に名前を付けます。おそらく、BrazeユーザーIDのようなスプレッドシートからのルックアップフィールド経由でのクエリーを許可したいだろう。

この時点で、以下のようなリンクでAPIにアクセスできるはずだ：<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en)。.

### ステップ 3:Braze Connected ContentでAPIを使用する

API にアクセスできるようになったので、コネクテッドコンテンツ呼び出しで API を使用できます。以下は、翻訳テンプレートの例である：

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Sheetlabs との統合に関する詳しい例やアドバイスについては、[Sheetlabs のドキュメント](https://app.sheetlabs.com/docs/producers/braze/)を参照してください。
{% endalert %}
