---
nav_title: アプリ内コンテンツへのディープリンク
article_title: アプリ内コンテンツへのディープリンク
page_order: 3
description: "この記事では、アプリ内メッセージのコンテンツにディープリンクを追加する方法について説明します。"

---

# アプリ内コンテンツへのディープリンク

## ディープリンクとは何か？

ディープリンクは、ネイティブアプリを起動し、特定のアクションを実行したり、特定のコンテンツを表示したりするように指示する追加情報を提供する方法です。

これには 3 つの部分があります。

1. 起動するアプリを特定します。
2. 実行するアクションをアプリに指示します。
3. 必要な追加データをアクションに指定します。

ディープリンクは、アプリの特定の部分にリンクするカスタムURIで、これら3つの部分すべてを含む。キーは、カスタムスキームを定義することです。`http:` は、ほとんどの人が慣れ親しんでいるスキームですが、スキームは任意の単語から始めることができます。スキームは文字で始める必要がありますが、文字、数字、プラス記号、マイナス記号、ドットを含むことができます。現実的に言えば、競合を防ぐための中央レジストリは存在しないので、ドメイン名をスキームに含めるのがベストプラクティスである。例えば、`twitter://` は、X (旧称ツイッター) のモバイルアプリを起動するための iOS 用 URI です。

ディープリンク内のコロン以降はすべて自由形式のテキストである。構造と解釈を定義するのはユーザー次第です。ただし、一般的な規則として、`http:` URL の後に、先頭の`//` とクエリパラメータ(たとえば、`?foo=1&bar=2`) を含めてモデル化することがあります。先ほどの例では、`twitter://user?screen_name=[id]` 、アプリ内の特定のプロフィールを起動するために使われる。

{% alert important %}
Braze では、Flutter のようなラッパーを使ってディープリンクを送信することはサポートされません。この機能を使用するには、ネイティブレイヤでディープリンクを設定する必要があります。
{% endalert %}

## UTMタグとキャンペーンのアトリビューション

### UTMタグとは何か？

[UTM（Urchin Traffic Manager）タグを](https://support.google.com/analytics/answer/10917952?sjid=14344007686729081565-NC#zippy=%2Cin-this-article)使えば、キャンペーンのアトリビューションの詳細をリンクに直接含めることができる。UTMタグは、Googleアナリティクスがキャンペーンのアトリビューションデータを収集するために使用され、以下のプロパティを追跡するために使用することができる：

- `utm_source`:トラフィックの送信元の識別子 (`my_app` など)
- `utm_medium`:キャンペーンメディア(`newsfeed` など)
- `utm_campaign`:キャンペーンの識別子(`spring_2016_campaign` など)
- `utm_term`:アプリまたはウェブサイトにユーザを移動させた有料検索用語の識別子(`pizza` など)
- `utm_content`:ユーザがクリックした特定のリンクまたはコンテンツの識別子(`toplink` または`android_iam_button2` など)

UTMタグは、通常のHTTP（ウェブ）リンクとディープリンクの両方に埋め込むことができ、Google Analyticsを使ってトラッキングすることができる。

### BrazeでUTMタグを使う

通常のHTTP (ウェブ) リンクでUTM タグを使用する場合(たとえば、メールキャンペーンのキャンペーン属性を行う場合)、組織でGoogle Analytics がすでに使用されている場合は、[Google のURL ビルダー](https://ga-dev-tools.google/ga4/campaign-url-builder/) を使用してUTM リンクを生成できます。これらのリンクは、他のリンクと同様に、Brazeのキャンペーンコピーに簡単に埋め込むことができる。

アプリへのディープリンクでUTMタグを使用するには、関連する[Google Analytics SDK](https://developers.google.com/analytics/devguides/collection/)が統合され、ディープリンクを処理するように正しく設定されている必要があります。不明な点は開発者に確認すること。

Analytics SDK が統合および設定された後、UTM タグはBraze キャンペーンのディープリンクで使用できます。キャンペーンのUTM タグを設定するには、宛先URL またはディープリンクに必要なUTM タグを含めます。以下の例は、プッシュ通知やアプリ内メッセージでUTMタグを使う方法を示している。

#### UTM タグによるプッシュ開封のアトリビュート指定

プッシュ通知用のディープリンクにUTMタグを含めるには、プッシュメッセージのオンクリック動作をディープリンクに設定してから、ディープリンクアドレスを書き込み、目的のUTMタグを次のように含めます。

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

\![]({% image_buster /assets/img_archive/push_utm_tags.png %})

#### UTM タグによるアプリ内メッセージのクリックのアトリビュート指定

アプリ内メッセージのディープリンクにUTMタグを含めるには、次を使用します。

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

\![]({% image_buster /assets/img_archive/iam_utm_tags.png %})

