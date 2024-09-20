---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "この参考記事では、BrazeとSheetlabsの提携について概説している。Sheetlabsは、スプレッドシートから得たデータを使ってマーケティング・キャンペーンをパーソナライズできるサービスである。"
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner

---

# Sheetlabs

> [Sheetlabsは][1]、スプレッドシートをパワフルで文書化されたAPIに変えることを可能にするプラットフォームだ。Google SheetsやExcelからデータをインポートしてAPI化し、そのAPIをBrazeなどの他のアプリケーションで使うことができる。

SheetlabsとBrazeの統合により、[Connected Contentを][2]活用して、BrazeのマーケティングキャンペーンにSheetlabsのAPIを含めることができる。これは、Googleスプレッドシート（マーケティングチームが直接更新する）とBrazeテンプレートの橋渡しによく使われる。これにより、翻訳やカスタム属性の大規模なセットなど、Brazeテンプレートでより多くのことを実現できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| シートラボアカウント | このパートナーシップを利用するには、[Sheetlabsのアカウントが][1]必要である。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

BrazeとSheetlabsの統合により、以下のユースケースを実現できる：

1. **マーケターアクセスとBrazeキャンペーンアクセスを分離する**：チームによっては、すべてのスタッフにBrazeのテンプレートやコンテンツを直接設定するためのアクセス権を与えたくない場合もある。その代わり、スタッフはスプレッドシートでマーケティング・コンテンツを更新することを望んでいる。SheetlabsはスプレッドシートとBrazeの橋渡しをし、リアルタイムで更新できる。
2. **翻訳する**：Brazeのテンプレートはネイティブに翻訳をサポートしていない。複数の言語をサポートしたい場合は、複数のテンプレートを作成する必要がある。SheetlabsとBrazeを併用することで、一つのBrazeテンプレートを多言語に翻訳することができる。
3. **カスタム属性を拡張する**：Brazeには、設定可能なカスタム属性が一定数用意されている。SheetlabsをBrazeと併用することで、この最初の割り当てを超えてカスタム属性を追加することができる。

これらの使用例の詳細については、[Sheetlabsを][3]参照のこと。

## 統合

### ステップ1:スプレッドシートをSheetlabsにインポートする

Sheetlabsでは、エクセルのスプレッドシートをアップロードするか、グーグルアカウントをリンクしてグーグルシートをインポートする。 

- エクセルのスプレッドシートをインポートするには、メニューバーの「**Data Tables**」をクリックし、「**Import from CSV/Excel**」をクリックする。
- Google Sheetsからインポートするには、メニューバーの**Data Tablesを**クリックし、次に**Import from Googleを**クリックする。その後、グーグルのログイン認証情報を入力し、シートをインポートする必要がある。

また、Google Sheetを同期させておくこともできる。つまり、SheetlabsはGoogle Sheetに変更があった場合、自動的に最新のデータを取得する。

BrazeのユーザーIDをスプレッドシートに含めるか、後で検索に使えるようにしておくこと。

### ステップ2:SheetlabsでAPIを作成する

次に、Sheetlabsで**API > Create APIと**進み、APIに名前を付ける。おそらく、BrazeユーザーIDのようなスプレッドシートからのルックアップフィールド経由でのクエリーを許可したいだろう。

この時点で、以下のようなリンクでAPIにアクセスできるはずだ：<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`][4].

### ステップ3:Braze Connected ContentでAPIを使用する

これでAPIにアクセスできるようになったので、Connected Contentの呼び出しでAPIを使うことができる。以下は、翻訳テンプレートの例である：

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}

{% alert tip %}
Sheetlabsとの統合に関する詳しい例やアドバイスについては、[Sheetlabsのドキュメントを](https://app.sheetlabs.com/docs/producers/braze/)参照されたい。
{% endalert %}


[1]: https://sheetlabs.com/
[2]: https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[3]: https://app.sheetlabs.com/docs/producers/braze/
[4]: https://sheetlabs.com/ACME/email1_translations?country=en