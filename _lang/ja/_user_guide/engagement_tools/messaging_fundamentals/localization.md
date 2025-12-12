---
nav_title: ローカライゼーション
article_title: ローカライゼーション
page_order: 7
description: "この参照記事では、ローカライズの基本について説明し、キャンペーンとキャンバス間で異なるオーケストレーションアプローチの利点を示し、ユーザがメッセージングでパーソナライゼーションを処理できるさまざまな方法を示します。"
tool:
    - Campaigns
    - Canvas
---

# ローカライゼーション

> 多くの国に顧客を持つ企業の場合、Braze ジャーニーの早い段階でローカライゼーションを処理することで、会社の時間とリソースを節約できます。

## CDI の仕組み

[Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/)を統合すると、ユーザーデバイスからのロケール情報が自動的に収集されます。ロケールには、言語と地域識別子が含まれています。この情報は、Braze セグメンテーションツールの [**国**] と [**言語**] で確認できます。

{% alert tip %}
ロケールの受信方法に関する技術的な詳細については、公式の[iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) および[Android](http://developer.android.com/reference/java/util/Locale.html) ドキュメントを参照してください。
{% endalert %}

## 翻訳管理

次の翻訳管理方法を検討してください。

{% tabs local %}
{% tab campaign %}
### すべてに対して1つのテンプレート

このアプローチでは、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) を使用して Braze が1つのテンプレートにローカライゼーションが適用されます。送信後、ダッシュボードは集計されたキャンペーン分析を提供する。ユーザーレベルのエンゲージメントは、例えば**国**と**受信キャンペーン**のフィルターを組み合わせるなど、カスタムのセグメントファネルを使用して測定できます。

| メリット | 考慮事項 |
| --- | --- |
| \- 集中アプローチ<br>\- メールの作成時間を短縮。何度もメールを作成する必要がない。 | \- マニュアル・レポート作成<br>\- キャンペーンレポートには、国ごとの指標ではなく、集計された指標が表示される<br>\- Liquid を徹底的にテストして、期待どおりに事前入力されることを確認する必要がある<br>\- 国の値をどのように引き出すか、または設定した国の数によっては、各国のテストが難しい場合がある<br>\- 複数のタイムゾーンで特定の時間に送信をスケジュールするのが難しくなる<br>\- 国ごとに別々のコンテンツを送信したい場合は使いにくい |
| \--- | \--- | \--- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 国ごとに1つのテンプレート 

このアプローチでは、テンプレートをさまざまな送信ロケールに分けます。送信後、ダッシュボードは国別に送信分析を報告し、下流のユーザーレベルの[Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)イベントも特定のキャンペーンに関連付けられる。

- テンプレートは、メンテナンスとトラッキングの目的で[タグを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags)実装することで恩恵を受ける。
- キャンペーンは、同じ[Brazeテンプレートや]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) [コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks)（Liquidを含む[メールテンプレートなど]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template)）の設定を継承できる。
- 既存のキャンペーンやテンプレートを[複製]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating/)することで、価値創出までの時間を短縮できます。

| メリット | 考慮事項 |
| --- | --- |
| \- 複数の場所に拡張可能<br>\- Braze 内の国ごとの収益に関するレポート (キャンペーンごとなど)<br>\- コンテンツが国ごとに大きく異なる場合の柔軟性 | \- 戦略的な構造化が必要<br>\- 国ごとにキャンペーンを行うなど、より多くの構築作業が必要である。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab canvas %}
### 1つのジャーニーですべてに対応

このアプローチでは、ローカライズは[Canvas Journeys]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey)およびLiquid内で処理され、各ユーザのメッセージングを定義します。 

キャンバスが送信された後、ダッシュボードには集計された[キャンバス分析]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/)が表示され、ユーザーレベルのエンゲージメントは、カスタムの[セグメントファネル]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/) ([**国**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country)と[**受信キャンバスステップ**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step)のフィルターの組み合わせなど) で測定できます。

| メリット | 考慮事項 |
| --- | --- |
| \- 集中アプローチ<br>\- メール作成時間の短縮 - 何度もメールを作成する必要はありません。 | \- マニュアル・レポート作成<br>\- キャンバスレポートには、国ごとの指標ではなく、集計された指標が表示される<br>\- Liquid を徹底的にテストして、期待どおりに事前入力されることを確認する必要がある<br>\- 国の値をどのように引き出すか、または設定した国の数によっては、各国のテストが難しい場合がある<br>\- 複数のタイムゾーンで特定の時間に送信をスケジュールするのが難しくなる<br>\- 国ごとに別々のコンテンツを送信したい場合は使いにくい |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 国ごとに1つのジャーニー

このアプローチでは、[Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)ジャーニービルダーは、複数の[Canvas コンポーネント]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)を介してユーザジャーニーを作成する柔軟性を提供します。これらのコンポーネントは、コンポーネントレベルおよびジャーニー全体で[複製]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating)できます。

ローカライゼーションは、次の方法で実行できます。

- 国ごとにキャンバスを分けることで、複雑なユーザージャーニーがオーディエンスフィルターを使用してファネルの一番上に定義されるようにする。
- 国ごとに特注のユーザージャーニーを作成し、[Audience Pathsを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/)実装することで、1つのCanvasに国ごとに個別のメッセージスレッドを作成することで、ジャーニーごとに大規模にユーザーを直感的にセグメント化する。

送信後、ダッシュボードには顧客の現在地に基づいて、国ごとおよびユーザーレベルの [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) イベント内のダイナミックな分析が表示されます。

| メリット | 考慮事項 |
| --- | --- |
| \- Braze 内の国ごとの収益に関するレポート (キャンバス、バリアント、ステップごとなど)<br>\- コンテンツが国ごとに大きく異なる場合の柔軟性<br>\- 将来のジャーニーの一環として他のチャネルを追加できる | \- 戦略的な構造化が必要<br>\- 追加の構築作業が必要 (国ごとに個別のメッセージステップを設定するなど)<br>\- 1つのキャンバスに国ごとのカスタムで複雑なジャーニーがあると、キャンバスが大きくなり、読みづらくなることがある。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## 翻訳されたメッセージの送信

ユーザの言語またはロケールに基づいてパーソナライズされたメッセージを送信するには、次のいずれかの方法を使用します。

{% tabs local %}
{% tab Manually %}
メッセージの本文にコンテンツを手動で貼り付け、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/)を使用して[条件付きで]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic)正しい言語を受信者に表示できます。これを行う方法:

1. メッセージを作成し、[**言語**] を選択して、選択した言語ごとに Liquid の条件付きロジックを生成します。
2. メッセージの作成には次の Liquid テンプレートを使用できます。テンプレートを使用するフィールドごとに、テンプレートの中括弧内のセグメントの後にバリエーションを入力する必要があります。バリエーションは、その前の中括弧で参照されている言語コードに対応していなければなりません。
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. 送信前にユーザーの ID またはメールアドレスを入力してメッセージをテストし、言語に応じてメッセージがどのように表示されるかを確認します。 

{% alert tip %}
メッセージングには必ず{% raw %}`{% else %}`{% endraw %}ステートメントを含めることをお勧めします。ほとんどのユーザーには特定の言語のメッセージが表示されますが、次のようなユーザーにはこのテキストが表示されます。
- 言語を選択していない
- Brazeがサポートしていない言語を持っている
- 言語が認識されないデバイスを使用している
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Braze の[コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks)は再利用が可能なコンテンツのブロックです。ブロックが変更されると、そのブロックへの参照もすべて変更される。たとえば、メールヘッダーまたはフッターの更新は、すべてのメールまたは翻訳に反映されます。これらのブロックは REST API を使用して[作成]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block)および[更新]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)することもでき、ユーザーはプログラムを使って翻訳をアップロードできます。 

ダッシュボードでキャンペーンを作成する際、{% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %} タグを使用してコンテンツブロックを参照できます。これらのブロックは、オプション1に示すように、各言語の条件ロジック内にすべての翻訳を格納することもできるし、各言語ごとに独立したブロックを使用することもできる。

コンテンツブロックは、翻訳が必要なコンテンツをコンテンツブロック内に格納し、取得、翻訳、更新するための翻訳管理プロセスとしても利用できます。
1. 「翻訳要」というタグが付いたコンテンツブロックをダッシュボードに手動で作成します。
2. サービスが [`/content_blocks/list` エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/)を使用してすべてのコンテンツブロックを夜間に取得します。
3. サービスが [`/content_blocks/info` エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/)を通じて各コンテンツブロックの詳細を取得し、どのブロックが翻訳対象としてタグ付けされているかを確認します。
4. 翻訳サービスは、すべての「翻訳要」コンテンツブロックの本文を翻訳します。
5. サービスは [`/content_block/update` エンドポイント]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)にアクセスして翻訳されたコンテンツを更新し、タグを「翻訳完了」に更新します。
{% endtab %}

{% tab Catalogs %}
[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)を使用すると、Liquid のカスタム属性やカスタムイベントプロパティと同様に、インポートされた JSON オブジェクトのデータに API や CSV ファイルを介してアクセスし、メッセージを充実させることができます。例えば次のようにします。

{% subtabs local %}
{% subtab API %}

次の API 呼び出しでカタログを作成します。
```json
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

次の API 呼び出しでアイテムを追加します。

```json
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
次の形式で CSV を作成します。

| id | コンテキスト | language | 本文 |
| --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | エス | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hey |
| 6 | 2 | エス | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hey |
| 10 | 3 | エス | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endsubtab %}
{% endsubtabs %}

これらのカタログアイテムは、以下に示すように[パーソナライゼーション]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#using-catalogs-in-a-message)を使用して参照したり、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)を使用してデータのグループを作成したりできます。 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Locale messages %}
メッセージにロケールを追加して使用することで、メールキャンペーンやプッシュチャネルのキャンバスまたは1つのキャンペーン内で異なる言語のユーザーをターゲットにすることができます。詳細なウォークスルーについては、[メールメッセージのロケール]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/)または[プッシュメッセージのロケール]({{site.baseurl}}/user_guide/message_building_by_channel/push/using_locales/)を参照してください。

{% alert important %}
この機能は現在早期アクセス段階です。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}
{% endtab %}

{% tab Braze partners %}
[Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) や [Crowdin](https://crowdin.com/) など、多くの Braze パートナーがローカライゼーションソリューションを提供しています。通常、ユーザーは社内チームや翻訳業者と一緒にプラットフォームを使用します。これらの翻訳はそこにアップロードされ、REST API 経由でアクセスできるようになります。これらのサービスでは多くの場合、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)を活用して、ユーザーが API 経由で翻訳を取得できるようにしています。

例えば、次のコネクテッドコンテンツの呼び出しでは、Transifex と Crowdin を呼び出して翻訳を取得し、{% raw %}`{{${language}}}`{% endraw %} を利用して特定のユーザー用に正しい翻訳を特定します。その後、この翻訳が JSON ブロックの「文字列」に保存され、参照されます。

{% subtabs local %}
{% subtab Transifex example %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin example %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Spreadsheets %}
スプレッドシートで翻訳をホストし、次のいずれかの方法を使用して、該当する言語でメッセージを送信します。

{% subtabs local %}
{% subtab Connected Content %}
翻訳エージェントと協力して Google スプレッドシートに翻訳を保存し、[Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) を使用してこのコンテンツに対してクエリを実行できます。メッセージを送信すると、ユーザーが選択した言語に基づいて、各ユーザーに対して適切な翻訳がキャンペーン本文に取り込まれます。 

{% alert note %}
Google スプレッドシート API には、1 プロジェクトあたり 100 秒間に 500 リクエストという制限があります。コネクテッドコンテンツの通話はキャッシュできますが、このソリューションはトラフィックの多いキャンペーンには拡張できません。
{% endalert %}
{% endsubtab %}

{% subtab JSON API via SheetDB %}
このオプションは、Google スプレッドシートを、コネクテッドコンテンツ経由でクエリされる JSON オブジェクトに変換する代替方法を提供します。スプレッドシートを SheetDB 経由でJSON API に変換することで、API 呼び出しの頻度に応じて[複数のサブスクリプションティア](https://sheetdb.io/pricing)から選択できます。

スプレッドシートの構造はオプション 4 の手順と同じですが、SheetDB にはオブジェクトをクエリするための[追加のフィルター](https://docs.sheetdb.io/#sheetdb-api)も用意されています。

Liquid とコネクテッドブロックの依存関係が少ない SheetDB を実装したいユーザーは、大きな条件付きブロックを構築するよりも、GET リクエスト呼び出しに SheetDB の[検索メソッド](https://docs.sheetdb.io/#get-search-in-document)を実装して {% raw %} `{{${language}}}` {% endraw %} Liquid タグに基づいてJSON オブジェクトをフィルタリングして 1 つの言語の結果を自動的に返すことができます。

#### ステップ 1:Google スプレッドシートをフォーマットする

まず、各言語が異なるオブジェクトになるように Google シートを作成します。

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

#### ステップ2:コネクテッドコンテンツ呼び出しで Liquid の言語タグを使用する

次に、コネクテッドコンテンツの呼び出しに Liquid タグ {% raw %}`{{${language}}}`{% endraw %} を実装します。ここで SheetDB はスプレッドシートの作成時に `sheet_id` を自動生成することに注意してください。

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### ステップ 3:メッセージをテンプレート化する

最後に、Liquid を使用してメッセージをテンプレート化します。

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### 考慮事項

- {% raw %}`{{${language}}}`{% endraw %} フィールドはすべてのユーザー向けに定義する必要があります。そうでない場合、言語のないユーザーのフォールバックハンドラーとして Liquid 条件ブロックを使用する必要があります。
- Google スプレッドシート内のデータモデリングは、メッセージオブジェクトを使用するのではなく、言語主導の異なる分野に従う必要があります。
- SheetDB は制限付きの無料アカウントと複数の有料オプションがあり、キャンペーン戦略に基づいて検討する必要があります。 
- コネクテッドコンテンツ呼び出しはキャッシュできます。API 呼び出しの予測ケイデンスを測定し、検索メソッドを使用する代わりにメインの SheetDB エンドポイントを呼び出す別の方法を検討することをお勧めします。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
