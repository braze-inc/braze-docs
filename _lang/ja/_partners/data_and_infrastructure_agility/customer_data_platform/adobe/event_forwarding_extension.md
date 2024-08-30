---
nav_title: イベント転送拡張
article_title: Adobe
description: "このリファレンス記事では、Adobe Experience Platform Edge Networkでキャプチャされたデータを活用し、サーバーサイドイベントの形式でBrazeに送信することを可能にするBrazeイベントフォワード拡張機能について説明します。"
page_type: partner
page_order: 2
search_tag: Partner

---

# トラックイベントAPIイベント転送拡張

> Braze Track Events API [イベント転送](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en)拡張機能を使用すると、Adobe Experience Platform Edge Networkでキャプチャされたデータを活用し、[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) APIを使用してサーバーサイドイベントの形式でBrazeに送信できます。

このドキュメントは、拡張機能の使用例、イベント転送ライブラリへのインストール方法、およびイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)でその機能を使用する方法について説明しています。

{% alert note %}
Brazeに属性を送信すると、Brazeのデータポイント消費が増加する可能性があります。送信する前にBrazeアカウントマネージャーに相談してください。Brazeのドキュメントの[課金対象データポイント]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points)についての詳細をご参照ください。
{% endalert %}

## ユースケース

この拡張機能は、Brazeのエッジネットワークからのデータを使用して、顧客分析およびターゲティング機能を活用する必要があります。

例えば、小売組織がマルチチャネルの存在感（Web サイトとモバイル）を持ち、Web サイトとモバイルプラットフォームからイベントデータとして取引または会話の入力をキャプチャしていると考えてみましょう。 

さまざまな[タグ](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en)ルールを使用して、このデータはリアルタイムでエッジネットワークに送信されます。ここから、Braze イベント転送拡張機能は、サーバー側から Braze に関連するイベントを自動的に送信します。

## レート制限

| API | レート制限 |
| --- | --- |
| ユーザー トラック | 1分あたり50,000リクエスト。<br><br>詳細については、[ユーザー トラック API ドキュメント]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit)を参照してください。
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:必要な構成の詳細を収集する

Edge NetworkをBrazeに接続するには、次のものが必要です:

| キータイプ | 説明 |
| --- | --- |
| Brazeインスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから取得するか、[API概要ページ]({{site.baseurl}}/api/basics/#endpoints)で見つけることができます。 |
| Braze REST API キー | すべての権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### ステップ2:秘密を作成する

新しい[イベント転送シークレット](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en)を作成し、値を[Braze API キー](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details)に設定します。これは、値を安全に保ちながらアカウントへの接続を認証するために使用されます。

### ステップ3:Braze拡張機能をインストールして構成する

1. 拡張機能をインストールするには、[イベント転送プロパティを作成する](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties)か、既存のプロパティを編集することを選択します。
2. 次に、左側のナビゲーションで**拡張機能**を選択します。「**カタログ**」タブで、Braze拡張機能のカードの「**インストール**」を選択します。
3. 次の画面で、REST インスタンスと API キーを入力し、完了したら**保存**を選択します。

### ステップ4:送信イベントルールを作成する

拡張機能をインストールした後、新しいイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)を作成し、必要に応じてその条件を設定します。ルールのアクションを構成する際に、**Braze**拡張機能を選択し、アクションタイプとして**イベントを送信**を選択します。

![][1]

{% tabs ローカル %}
{% tab ユーザー Identification %}

| 入力 | 説明 |
| --- | --- |
| 外部ユーザ ID | 長く、ランダムで、よく分散されたUUIDまたはGUID。ユーザーIDの名前を付ける別の方法を選択する場合、それらも長く、ランダムで、よく分散されている必要があります。[推奨されるユーザー ID の命名規則]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention)について詳しく学びます。 |
| Braze ユーザー ID | Braze ユーザー 識別子。 |
| ユーザーエイリアス | エイリアスは、代替の一意のユーザー識別子として機能します。エイリアスを使用して、コアユーザーIDとは異なる次元でユーザーを識別します。<br><br>ユーザーエイリアスオブジェクトは2つの部分で構成されています: 識別子自体の`alias_name`とエイリアスの種類を示す`alias_label`。ユーザーは異なるラベルで複数のエイリアスを持つことができますが、`alias_name`ごとに`alias_label`つだけです。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
イベントをユーザーに結びつけるには、`External User ID`フィールド、`Braze User Identifier`フィールド、または`User Alias`セクションのいずれかを記入する必要があります。
{% endalert %}

{% endtab %}
{% tab イベントデータ %}

| 入力 | 説明 | 必須 |
| --- | --- | --- |
| イベント名 | イベントの名前。 | はい |
| イベント時間 | ISO 8601または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の日付時刻文字列。 | はい |
| アプリ識別子 | アプリ識別子または`app_id`は、ワークスペース内の特定のアプリとアクティビティを関連付けるパラメーターです。それは、ワークスペース内のどのアプリと対話しているかを指定します。 | いいえ |
| イベントプロパティ | イベントのカスタムプロパティを含むJSONオブジェクト。 | いいえ |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
**Braze Send Event**アクションには**Event Name**と**Event Time**を指定するだけで済みますが、カスタムプロパティフィールドにはできるだけ多くの情報を含めるべきです。詳細については[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)を参照してください。
{% endalert %}

{% endtab %}
{% tab ユーザー 属性 %}

ユーザー属性は、指定されたユーザープロファイル上の指定された名前と値で属性を作成または更新するフィールドを含むJSONオブジェクトである可能性があります。次のプロパティがサポートされています:

| ユーザー 属性 | 説明 |
| --- | --- |
| 名 | ユーザーの名。 |
| 姓 | ユーザーの姓。 |
| 電話 | ユーザーの電話番号。 |
| メール | ユーザーのメールアドレス。 |
| 性別 | 次の文字列のいずれか:「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（言いたくない）。 |
| 市区町村 | ユーザーの市区町村。 |
| 国 | ユーザーの国は、[ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)形式の文字列です。 |
| 言語 | ユーザーの言語は[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)形式の文字列です。 |
| 生年月日 | 文字列形式のユーザーの生年月日（例：1980-12-21）。 |
| タイムゾーン | タイムゾーン名は、[IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)データベースから取得します（例：'America/New_York' または 'Eastern Time (US & Canada)'）。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| ツイッター | id（整数）、`screen_name`（文字列、X（旧Twitter）ハンドル）、`followers_count`（整数）、`friends_count`（整数）、`statuses_count`（整数）を含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
構成内で追加されたすべての属性は、属性の値が変更されたかどうかに関係なく、イベントがBrazeに送信されるたびに送信されます。ユーザー属性を設定する際には、これがデータポイントの消費にどのように影響するかを確認してください。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 5: 購入イベント送信ルールを作成する

拡張機能をインストールした後、新しいイベント転送[ルール](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en)を作成し、必要に応じてその条件を設定します。ルールのアクションを構成する際に、**Braze**拡張機能を選択し、アクションタイプとして**購入イベントを送信**を選択します。

![][3]

{% tabs ローカル %}
{% tab ユーザー Identification %}

| 入力 | 説明 |
| --- | --- |
| 外部ユーザ ID | 長く、ランダムで、よく分散されたUUIDまたはGUID。ユーザーIDの名前を付ける別の方法を選択する場合、それらも長く、ランダムで、よく分散されている必要があります。[推奨されるユーザー ID の命名規則]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention)について詳しく学びます。 |
| Braze ユーザー ID | Braze ユーザー 識別子。 |
| ユーザーエイリアス | エイリアスは、代替の一意のユーザー識別子として機能します。エイリアスを使用して、コアユーザーIDとは異なる次元でユーザーを識別します。<br><br>ユーザーエイリアスオブジェクトは2つの部分で構成されています: 識別子自体の`alias_name`とエイリアスの種類を示す`alias_label`。ユーザーは異なるラベルで複数のエイリアスを持つことができますが、`alias_name`ごとに`alias_label`つだけです。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
イベントをユーザーにリンクするには、`External User ID`フィールド、`Braze User Identifier`フィールド、または`User Alias`セクションのいずれかを完了する必要があります。
{% endalert %}

{% endtab %}
{% tab 購入データ %}

| 入力 | 説明 | 必須 |
| --- | --- | --- |
| 製品ID | 購入のための識別子。（例えば、製品名や製品カテゴリ） | はい |
| 購入時間 | ISO 8601または`yyyy-MM-dd'T'HH:mm:ss:SSSZ`形式の日付時刻文字列。 | はい |
| 通貨 | [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) アルファベット通貨コード形式の文字列としての通貨。 | はい |
| 価格 | 物の価格。 | はい |
| 数量 | 購入数量。提供されていない場合、デフォルト値は1になります。最大値は100未満でなければなりません。 | いいえ |
| アプリ識別子 | アプリ識別子または`app_id`は、ワークスペース内の特定のアプリとアクティビティを関連付けるパラメーターです。それは、ワークスペース内のどのアプリと対話しているかを指定します。 | いいえ |
| 購入プロパティ | 購入のカスタムプロパティを含むJSONオブジェクト。 | いいえ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
**購入イベントの送信**アクションには、`Product ID`、`Purchase Time`、`Currency`、および`Price`のみを指定する必要がありますが、購入プロパティフィールドにできるだけ多くの情報を含める必要があります。詳細については[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を参照してください。
{% endalert %}

{% endtab %}
{% tab ユーザー Attributes %}

構成ビュー内の各イベントに属性を送信するかどうかを選択できます。

ユーザー属性は、指定されたユーザープロファイル上の指定された名前と値で属性を作成または更新するフィールドを含むJSONオブジェクトである可能性があります。次のプロパティがサポートされています:

| ユーザー 属性 | 説明 |
| --- | --- |
| 名 | ユーザーの名。 |
| 姓 | ユーザーの姓。 |
| 電話 | ユーザーの電話番号。 |
| メール | ユーザーのメールアドレス。 |
| 性別 | 次の文字列のいずれか:「M」、「F」、「O」（その他）、「N」（該当なし）、「P」（言いたくない）。 |
| 市区町村 | ユーザーの市区町村。 |
| 国 | ユーザーの国は、[ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)形式の文字列です。 |
| 言語 | ユーザーの言語は[ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)形式の文字列です。 |
| 生年月日 | 文字列形式のユーザーの生年月日（例：1980-12-21）。 |
| タイムゾーン | タイムゾーン名は、[IANA Time Zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)データベースから取得します（例：'America/New_York' または 'Eastern Time (US & Canada)'）。 |
| Facebook | `id`（文字列）、`likes`（文字列の配列）、`num_friends`（整数）のいずれかを含むハッシュ。 |
| ツイッター | id（整数）、`screen_name`（文字列、X（旧Twitter）ハンドル）、`followers_count`（整数）、`friends_count`（整数）、`statuses_count`（整数）を含むハッシュ。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
構成内で追加されたすべての属性は、属性の値が変更されたかどうかに関係なく、イベントがBrazeに送信されるたびに送信されます。ユーザー属性を設定する際には、これがデータポイントの消費にどのように影響するかを確認してください。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 6: Braze内のデータを検証する

イベントコレクションとAdobe Experience プラットフォームの統合が成功した場合、[ユーザープロファイルを表示するとき]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)にBrazeコンソール内にイベントが表示されます。具体的には、Brazeに送信された新しいイベントデータは、特定のユーザーの**購入**または**カスタムイベント**セクションの[概要タブ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab)に反映されます。

[1]: {% image_buster /assets/img/efe.png %}
[3]: {% image_buster /assets/img/efe2.png %}