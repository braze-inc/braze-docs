---
nav_title: アプリ内コンテンツへのディープリンク
article_title: アプリ内コンテンツへのディープリンク
page_order: 3
description: "この参考記事では、アプリ内メッセージコンテンツにディープリンクを追加する方法について説明しています。"

---

# アプリ内コンテンツへのディープリンク

## ディープリンクとは

ディープリンクは、ネイティブアプリを起動し、特定のアクションを実行したり、特定のコンテンツを表示したりするように指示する追加情報を提供する方法です。

これには次の 3 つの部分があります。

1. 起動するアプリを特定する
2. 実行するアクションをアプリに指示する
3. 必要な追加データをアクションに提供してください

ディープリンクは、アプリの特定の部分にリンクするカスタムURIで、これら3つの部分すべてが含まれます。重要なのは、カスタムスキームを定義することです。`http:`ほとんどの人が慣れ親しんでいるスキームですが、スキームはどの単語でも始めることができます。スキームは文字で始まる必要がありますが、文字、数字、プラス記号、マイナス記号、またはドットを含めることができます。実際には、競合を防ぐための中央レジストリはないため、ドメイン名をスキームに含めることがベストプラクティスです。たとえば、`twitter://`は X 用のモバイルアプリ (以前は Twitter) を起動するための iOS URI です。

ディープリンク内のコロンの後はすべて自由形式のテキストです。その構造と解釈を定義するのはあなた次第ですが、一般的な慣習としては、`//`先頭とクエリパラメータ (例:`?foo=1&bar=2`) を含めて `http:` URL をモデル化することです。前の例では`twitter://user?screen_name=[id]`、アプリ内の特定のプロファイルを起動するために使用されます。

{% alert important %}
Brazeは、Flutterなどのラッパーを使用してディープリンクを送信することをサポートしていません。この機能を使用するには、ネイティブレイヤーでディープリンクを構成する必要があります。
{% endalert %}


## UTM タグとキャンペーンアトリビューション

### UTM タグとは何ですか?

[UTM（Urchin Traffic Manager）タグを使用すると][4]、キャンペーンのアトリビューションの詳細をリンク内に直接含めることができます。UTMタグは、Google Analyticsがキャンペーンのアトリビューションデータを収集するために使用され、次のプロパティの追跡にも使用できます。

- `utm_source`: トラフィックの送信元の識別子 (例:`my_app`)
- `utm_medium`: キャンペーンメディア (例:`newsfeed`)
- `utm_campaign`: キャンペーンの識別子 (例:`spring_2016_campaign`)
- `utm_term`: アプリやウェブサイトにユーザーを誘導した有料検索用語の識別子 (例:`pizza`)
- `utm_content`: ユーザーがクリックした特定のリンク/コンテンツの識別子 (たとえば、または) `toplink` `android_iam_button2`

UTMタグは、通常のHTTP（ウェブ）リンクとディープリンクの両方に埋め込むことができ、Googleアナリティクスを使用して追跡できます。

### ブレイズで UTM タグを使用する

[メールキャンペーンのキャンペーンアトリビューションを行う場合など、UTMタグを通常のHTTP（ウェブ）リンクで使用したいが、組織ですでにGoogleアナリティクスを利用している場合は、GoogleのURLビルダーを使用してUTMリンクを生成するだけで済みます。][6]これらのリンクは、他のリンクと同様にBrazeキャンペーンコピーに簡単に埋め込むことができます。

アプリへのディープリンクで UTM タグを使用するには、アプリに関連する [Google Analytics SDK][5] が統合され、[ディープリンクを処理するように正しく設定されている必要があります][7]。これについて不明な点がある場合は、開発者に確認してください。

Analytics SDKを統合して設定すると、UTMタグをBrazeキャンペーンのディープリンクに使用できるようになります。キャンペーンにUTMタグを設定するには、リンク先のURLまたはディープリンクに必要な UTMタグを含めるだけです。次の例は、プッシュ通知とアプリ内メッセージで UTM タグを使用する方法を示しています。

#### UTM タグによるプッシュオープンのアトリビューション

プッシュ通知のディープリンクにUTMタグを含めるには、プッシュメッセージのクリック時の動作をディープリンクに設定し、ディープリンクのアドレスを記述して、次の方法で目的のUTMタグを含めるだけです。

```
myapp://products/20-gift-card?utm_source=my_app&utm_medium=push&utm_campaign=spring2016giftcards&utm_content=ios_deeplink
```

![][8]

#### UTM タグによるアプリ内メッセージクリックのアトリビューション

以下を使用して、アプリ内メッセージに含まれるディープリンクにUTMタグを含めることができます。

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
