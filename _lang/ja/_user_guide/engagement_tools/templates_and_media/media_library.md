---
nav_title: メディアライブラリ
article_title: メディアライブラリ
page_order: 0
page_type: reference
description: "この参考記事では、メディアライブラリについて説明します。ここでは、アセットを1か所で一元管理する方法、AI を使用して画像を生成する方法、メッセージコンポーザーでメディアにアクセスする方法を学ぶことができます。"
tool: Media

---

# メディアライブラリ

> メディアライブラリを使用すると、アセットを1か所で一元管理できます。 

**メディアライブラリは** [**テンプレート**] にあります。

**メディアライブラリ**は次の用途に使用できます。

* 複数の画像を一度にアップロードする
* 仮想連絡先ファイル (.vcf) をアップロードする
* WhatsApp メッセージで使用する動画ファイルのアップロード
* 画像を含むフォルダーをアップロードする (最大50画像)
* [AI を使用して画像を生成し](#generate-ai)、メディアライブラリに保存する
* 既存の画像をトリミングして、メッセージに適した比率にする
* タグやチームを追加して、画像をさらに整理しやすくする
* メディアライブラリグリッドでタグまたはチームで検索する
* アップロードする画像またはフォルダーをドラッグ＆ドロップする
* 画像を削除する

![メディアライブラリページ。ファイルをドラッグ＆ドロップしてアップロードするための [ライブラリにアップロード] セクションがあります。メディアライブラリには、アップロードされたコンテンツのリストもあります。][1]

{% alert tip %} メディアライブラリの詳細については、[テンプレートとメディアに関するよくある質問]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs)をご覧ください。 {% endalert %}

## 画像詳細

メディアライブラリー内では、アセットの種類、サイズ、寸法、URL、ライブラリーに追加された日付、その他の情報を確認できる。 

### メディアライブラリと CDN の使い方

メディアライブラリを使用すると、アプリ内メッセージのキャッシュとパフォーマンスが向上します。アプリ内メッセージで見つかったすべてのメディアライブラリアセットは、より速く表示できるように事前にキャッシュされ、オフラインで表示できるようになります。さらに、メディアライブラリは Braze コンポーザーと統合されているため、マーケターは画像のURLをコピーして貼り付けるのではなく画像を選択またはタグ付けできます。

## 画像の仕様

メディアライブラリにアップロードされるすべての画像は5 MB 未満でなければなりません。サポートされているファイルタイプはPNG、JPEG、GIF、SVGである。メッセージングチャネル別の特定の推奨画像については、次のセクションを参照してください。

### コンテンツカードによって促進された

{% multi_lang_include image_specs.md variable_name='content cards' %}

### メール

{% multi_lang_include image_specs.md variable_name="email"  %}

### アプリ内メッセージ

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

詳しくは、[アプリ内メッセージクリエイティブの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)をご覧ください。

### プッシュ

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

##### その他のリソース

- [プッシュ画像とテキストの仕様]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)

### 動画

メディアライブラリにアップロードされた動画は、今のところWhatsAppメッセージでのみ使用できる。詳しくは[WhatsAppメッセージを作成するを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages)参照。

{% alert important %}
WhatsAppメッセージに動画を追加することは、現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## メッセージコンポーザーからメディアライブラリにアクセスする

すべての画像がメディアライブラリに直接アップロードされるため、メディアライブラリはダッシュボードのアセットを一元管理する場所として機能します。これにより、さまざまなメッセージで画像を再利用できます。

![メディアライブラリにアクセスするための一般的な 2 つの方法 (メッセージ作成画面によって異なる)。そのうちの1つでは、「画像とGIF」というタイトルの付いたメールドラッグ＆ドロップエディターと「メディアライブラリから追加」ボタンが表示されます。もう一方は、プッシュやアプリ内メッセージなどの標準的なエディターが表示され、「メディア」というタイトルと「画像を追加」というボタンがある。][1.5]{: style="border:none"}

## AI を使用して画像を生成する {#generate-ai}

Braze のサードパーティプロバイダーである OpenAI の AI システムである [DALL·E 3](https://openai.com/index/dall-e-3/) を使用して、メディアライブラリ用の画像を生成できます。このシステムでは、自然言語での説明からリアルな画像やアートを作成できます。リクエストごとに4種類のプロンプトが生成され、会社では1日に10回画像を生成できます。この合計は、社内のすべてのユーザーに適用されます。

1. メディアライブラリから、「<i class="fas fa-wand-magic-sparkles"></i>**AI 画像ジェネレーター**」を選択します。
2. 生成する画像の説明を最大300文字で入力します。説明が詳細であればあるほど、結果は良くなります。この機能はテキスト入力にのみ対応しており、画像、写真を参照としてアップロードすることはできない。
3. [**画像を生成**] を選択します。画像が生成されるまでに約1分かかることがあります。
4. メディアライブラリに追加する画像の [<i class="fas fa-download" title="メディアライブラリに画像を追加"></i>] を選択します。

![メディアライブラリのAIイメージジェネレーターモーダル。][6]{: style="max-width:75%"}

お客様と Braze の間において、DALL·E 3 を使用して生成された画像はお客様の知的財産となります。Braze は、そのような画像の著作権所有権を主張することはなく、AI が生成したコンテンツまたは画像に関していかなる種類の保証も行いません。

画像, 写真を生成するために、BrazeはOpenAIのAPIプラットフォームにクエリを送信する。Braze から OpenAI に送信されるすべてのクエリは匿名化されます。つまり、提供する入力内容に一意に識別できる情報を含めない限り、OpenAI はクエリの送信元を特定できません。[OpenAI の API プラットフォームコミットメント](https://openai.com/policies/api-data-usage-policies)に詳述されているように、Braze 経由で OpenAI の API に送信されたデータは、モデルのトレーニングや改善には使用されず、30日後に削除されます。お客様に関連する OpenAI のポリシーを必ず遵守してください。これには、OpenAI の[使用ポリシー](https://openai.com/policies/usage-policies)や[共有および公開ポリシー](https://openai.com/policies/sharing-publication-policy)が含まれる場合があります。Braze は AI が生成したコンテンツに関していかなる種類の保証も行いません。 


[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1.5] ： {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]: https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}
