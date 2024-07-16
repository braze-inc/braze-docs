---
nav_title: Sheetlabs
article_title:シートラボ
description:「この参考記事では、BrazeとSheetlabsのパートナーシップについて概説しています。Sheetlabsは、スプレッドシートから提供されたデータを使用してマーケティングキャンペーンをパーソナライズできるサービスです。「
alias: /partners/sheetlabs/
page_type: partner
search_tag:Partner

---

# シートラボ

> [Sheetlabsは][1]、スプレッドシートを強力で十分に文書化されたAPIに変換できるプラットフォームです。Google スプレッドシートや Excel からデータをインポートして API に変換し、その API を Braze などの他のアプリケーションで使用できます。

Sheetlabs と Braze の統合により、[コネクテッドコンテンツを活用して][2] Sheetlabs API を Braze マーケティングキャンペーンに組み込むことができます。これは通常、Google スプレッドシート (マーケティングチームが直接更新) と Braze テンプレートをつなぐために使用されます。これにより、翻訳や大量のカスタム属性セットなど、Brazeテンプレートでより多くのことを実現できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| シートラボアカウント | このパートナーシップを利用するには、[Sheetlabs アカウントが必要です][1]。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Braze と Sheetlabs の統合により、以下のユースケースを実現できます。

1. **マーケターアクセスと Braze キャンペーンアクセスの分離**:チームによっては、すべてのスタッフに Braze のテンプレートやコンテンツを直接設定するためのアクセス権を与えないようにしたい場合があります。代わりに、スタッフにスプレッドシートのマーケティングコンテンツを更新してもらいたいと考えています。SheetlabsはスプレッドシートとBrazeをつなぐ架け橋となり、リアルタイムで更新できます。
2. **翻訳**:Braze テンプレートはネイティブに翻訳をサポートしていません。複数の言語をサポートしたい場合は、複数のテンプレートを作成する必要があります。SheetlabsをBrazeと組み合わせて使用することで、1つのBrazeテンプレートを複数の言語に翻訳することができます。
3. **カスタム属性の拡張**:Braze には、設定可能なカスタム属性がいくつか用意されています。SheetlabsをBrazeと組み合わせて使用することで、この最初の割り当て以外にもカスタム属性を追加できます。

これらのユースケースの詳細については、[Sheetlabs][3] を参照してください。

## 統合

### ステップ1:スプレッドシートをSheetlabsにインポートする

Sheetlabs で Excel スプレッドシートをアップロードするか、Google アカウントをリンクして Google スプレッドシートをインポートします。 

- Excel スプレッドシートをインポートするには、メニューバーの \[**データテーブル**] をクリックし、次に \[**CSV/Excel からインポート**] をクリックします。
- Google スプレッドシートからインポートするには、メニューバーの \[**データテーブル**] をクリックし、次に \[**Google からインポート**] をクリックします。次に、Google のログイン認証情報を入力し、シートをインポートする必要があります。

Googleスプレッドシートを同期させておくこともできます。つまり、Sheetlabsは、データが変更されたときにGoogleスプレッドシートから最新のデータを自動的に取得します。

Brazeユーザー ID は、スプレッドシートなどに含めて、後で検索できるようにしてください。

### ステップ2:シートラボで API を作成する

次に、Sheetlabsで \[API] **> \[APIの作成] に移動し、APIに名前を付けます**。Braze ユーザー ID など、スプレッドシートのルックアップフィールドによるクエリを許可したい場合があります。

この時点で、次のようなリンクで API にアクセスできるはずです。<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`][4]。

### ステップ3:Braze コネクテッドコンテンツで API を使用する

API にアクセスできるようになったので、コネクテッドコンテンツの呼び出しで使用できます。翻訳テンプレートがどのようなものになるかの例を次に示します。

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}

{% alert tip %}
[Sheetlabsとの統合に関するその他の例とアドバイスについては、Sheetlabsのドキュメントを参照してください。](https://app.sheetlabs.com/docs/producers/braze/)
{% endalert %}


[1]: https://sheetlabs.com/
[2]: https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[3]: https://app.sheetlabs.com/docs/producers/braze/
[4]: https://sheetlabs.com/ACME/email1_translations?country=en