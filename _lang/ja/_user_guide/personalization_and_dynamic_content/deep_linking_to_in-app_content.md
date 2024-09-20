---
nav_title: アプリ内コンテンツへのディープリンク
article_title: アプリ内コンテンツへのディープリンク
page_order: 3
description: "この参考記事では、アプリ内のメッセージコンテンツにディープリンクを追加する方法について解説している。"

---

# アプリ内コンテンツへのディープリンク

## ディープリンクとは何か？

ディープリンクは、ネイティブアプリを起動し、特定のアクションを実行したり、特定のコンテンツを表示したりするよう指示する追加情報を提供する方法だ。

これには3つの部分がある：

1. 起動するアプリを特定する
2. どのアクションを実行するかをアプリに指示する
3. アクションが必要とする追加データを提供する。

ディープリンクは、アプリの特定の部分にリンクするカスタムURIで、これら3つの部分すべてを含む。重要なのは、カスタムスキームを定義することである。`http:` はほとんど誰もが知っているスキームだが、スキームはどんな単語でも始めることができる。スキームは文字で始まらなければならないが、文字、数字、プラス記号、マイナス記号、ドットを含むことができる。現実的に言えば、競合を防ぐための中央レジストリは存在しないので、ドメイン名をスキームに含めるのがベストプラクティスである。例えば、`twitter://` は、X（旧ツイッター）のモバイルアプリを起動するためのiOS URIである。

ディープリンク内のコロン以降はすべて自由形式のテキストである。その構造と解釈を定義するのはあなた次第だが、一般的な慣例としては、先頭の`//` とクエリーパラメーター（例えば、`?foo=1&bar=2` ）を含む、`http:` URLをモデルにしている。先ほどの例では、`twitter://user?screen_name=[id]` 、アプリ内の特定のプロフィールを起動するために使われる。

{% alert important %}
Brazeは、Flutterのようなラッパーを使ってディープリンクを送信することはサポートしていない。この機能を使うには、ネイティブ層でディープリンクを設定する必要がある。
{% endalert %}


## UTMタグとキャンペーンのアトリビューション

### UTMタグとは何か？

[UTM（Urchin Traffic Manager）タグを][4]使えば、キャンペーンのアトリビューションの詳細をリンクに直接含めることができる。UTMタグは、Googleアナリティクスがキャンペーンのアトリビューションデータを収集するために使用され、以下のプロパティを追跡するために使用することができる：

- `utm_source`トラフィックの送信元の識別子（たとえば、`my_app` ）。
- `utm_medium`キャンペーン媒体（例えば、`newsfeed` ）。
- `utm_campaign`: キャンペーンの識別子（例えば、`spring_2016_campaign` ）。
- `utm_term`: ユーザーをアプリやウェブサイトに導いた有料検索キーワードの識別子（例：`pizza` ）。
- `utm_content`: ユーザーがクリックした特定のリンク/コンテンツの識別子（例えば、`toplink` または`android_iam_button2` ）。

UTMタグは、通常のHTTP（ウェブ）リンクとディープリンクの両方に埋め込むことができ、Google Analyticsを使ってトラッキングすることができる。

### BrazeでUTMタグを使う

通常のHTTP（ウェブ）リンクでUTMタグを使いたい場合（例えば、メールキャンペーンのアトリビューションを行う場合など）、すでにGoogleアナリティクスを使用している組織では、[GoogleのURLビルダーを使って][6]UTMリンクを生成するだけでよい。これらのリンクは、他のリンクと同様に、Brazeのキャンペーンコピーに簡単に埋め込むことができる。

アプリへのディープリンクでUTMタグを使用するには、アプリに関連する[GoogleアナリティクスSDKが][5]統合され、[ディープリンクを処理するように正しく設定されて][7]いる必要がある。不明な点は開発者に確認すること。

アナリティクスSDKを統合して設定すれば、BrazeのキャンペーンでUTMタグをディープリンクで使用できる。キャンペーンにUTMタグを設定するには、宛先URLまたはディープリンクに必要なUTMタグを含めるだけでよい。以下の例は、プッシュ通知やアプリ内メッセージでUTMタグを使う方法を示している。

#### UTMタグでプッシュオープンをアトリビュートする

プッシュ通知用のディープリンクにUTMタグを含めるには、プッシュメッセージのクリック時の動作をディープリンクに設定し、ディープリンクのアドレスを記述し、以下の方法で目的のUTMタグを含めるだけでよい：

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![][8]

#### UTMタグでアプリ内メッセージのクリックをアトリビュートする

アプリ内メッセージに含まれるディープリンクには、以下の方法でUTMタグを含めることができる。

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=iam&utm_campaign=spring2021giftcards&utm_content=web_link
```

![][10]

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/#Android_Deep_Advance
[4]: https://support.google.com/analytics/answer/1033863?hl=en
[5]: https://developers.google.com/analytics/devguides/collection/
[6]: https://support.google.com/analytics/answer/1033867
[7]: https://developers.google.com/analytics/solutions/mobile-campaign-deep-link
[8]: {% image_buster /assets/img_archive/push_utm_tags.png %}
[9]: {% image_buster /assets/img_archive/news_feed_utm_tags.png %}
[10]: {% image_buster /assets/img_archive/iam_utm_tags.png %}
[11]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/creating_a_news_feed_item/
