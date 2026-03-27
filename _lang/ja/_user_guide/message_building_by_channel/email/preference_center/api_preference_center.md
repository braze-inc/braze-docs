---
nav_title: APIメール ユーザー設定センター
article_title: APIメール ユーザー設定センター
page_order: 1
description: "この記事では、APIメールユーザー設定センターとそのカスタマイズ方法について説明します。"
channel:
  - email
---

# APIメール ユーザー設定センター

> ユーザー設定センターを設定することで、ユーザーが[メールメッセージング]({{site.baseurl}}/user_guide/message_building_by_channel/email/)の通知設定を編集・管理するためのワンストップショップを提供できます。この記事では、API で生成されたユーザー設定センターの作成手順を説明しますが、[ドラッグ＆ドロップエディター]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/)を使ってユーザー設定センターを作成することもできます。

Braze のダッシュボードで、**オーディエンス** > **メールユーザー設定センター**に移動します。

ここで各サブスクリプショングループを管理・確認することができます。作成した各サブスクリプショングループは、このユーザー設定センターリストに追加されます。複数のユーザー設定センターを作成することができます。

{% alert important %}
ユーザー設定センターは、Braze のメールチャネル内で使用することを目的としています。ユーザー設定センターのリンクは各ユーザーに基づいてダイナミックに生成されるため、外部でホストすることはできません。
{% endalert %}

## API を使用してユーザー設定センターを作成する

[ユーザー設定センターの Braze エンドポイント]({{site.baseurl}}/api/endpoints/preference_center)を使用することで、ユーザー設定センター（Braze がホストする Web サイト）を作成し、ユーザーのサブスクリプション状態やサブスクリプショングループのステータスを表示することができます。開発者チームは HTML と CSS を使ってユーザー設定センターを作成し、ページのスタイルをブランドガイドラインに合わせることができます。

Liquid を使うことで、サブスクリプショングループの名前と各ユーザーのステータスを取得できます。こうすることで、Braze はページが読み込まれたときにこのデータを保存・取得します。

### 前提条件

| 必要条件 | 説明 |
|---|---|
| ユーザー設定センターが有効になっている | Braze ダッシュボードに、ユーザー設定センター機能を使用する権限があります。 |
| メール、SMS、または WhatsApp のサブスクリプショングループを持つ有効なワークスペース | 有効なユーザーと、メール、SMS、または WhatsApp のサブスクリプショングループを持つ稼働中のワークスペース。 |
| 有効なユーザー | メールアドレスと external ID を持つユーザー。 |
| ユーザー設定センターの権限を持つ API キーを生成済みである | Braze ダッシュボードで、**設定** > **API キー**に進み、ユーザー設定センターの権限を持つ API キーにアクセスできることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ 1: ユーザー設定センターの作成エンドポイントを使用する

[ユーザー設定センターの作成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)を使って、ユーザー設定センターの作成を開始しましょう。ユーザー設定センターをカスタマイズするには、`preference_center_page_html` フィールドと `confirmation_page_html` フィールドにブランディングに沿った HTML を含めることができます。

[ユーザー設定センターの URL 生成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)を使用すると、Braze を通じて送信されるメールの外で、特定のユーザーのユーザー設定センター URL を取得できます。

### ステップ 2: メールキャンペーンに含める

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

メールにユーザー設定センターへのリンクを配置するには、配信停止 URL を挿入する方法と同様に、メール内の適切な場所で以下の Liquid タグを使用します。

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Liquid を含む HTML を組み合わせて使うこともできます。例えば、HTML エディターでもドラッグ＆ドロップエディターでも、URL として次のように貼り付けることができます。これにより、すべてのメールサブスクリプショングループを自動的にリストアップする基本的なユーザー設定センターのレイアウトが表示されます。[リンクエイリアス]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/)を使用する場合は、Braze がトラッキングパラメーターを追加できるように、Liquid タグの後に末尾のクエスチョンマーク（`?`）を追加してください。

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

ユーザー設定センターには、ユーザーがすべてのメールの配信を停止できるチェックボックスがあります。テストメッセージとして送信された場合、これらの設定を保存することはできないので注意してください。

{% alert important %}
上記の Liquid タグは、キャンペーンやキャンバスを起動するときにのみ機能します。テストメールを送信しても、有効なリンクは生成されません。ユーザー設定センターのリンクを確認するには、テストプロファイルのみをターゲットとするキャンペーンでメッセージを起動してください。
{% endalert %}

#### ユーザー設定センターの編集

[ユーザー設定センターの更新エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)を使って、ユーザー設定センターを編集・更新できます。 

#### ユーザー設定センターと詳細の確認

ユーザー設定センターを特定するには、[ユーザー設定センターの詳細を表示エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)を使用して、最終更新タイムスタンプ、ユーザー設定センター ID などの関連情報を返します。

## カスタマイズ

Braze は、ユーザー設定センターからのサブスクリプション状態の更新を管理し、ユーザー設定センターの同期を保ちます。ただし、[サブスクリプショングループ API]({{site.baseurl}}/api/endpoints/subscription_groups/) を使用して、以下のオプションで独自のユーザー設定センターを作成し、ホストすることも可能です。

### オプション 1: 文字列クエリパラメーターを持つリンク

URL の本文でクエリ文字列のフィールドと値のペアを使用して、ユーザーの ID とメールカテゴリをページに渡します。これにより、ユーザーは配信停止の選択を確認するだけで済みます。このオプションは、ユーザー識別子をハッシュ形式で保存し、まだサブスクリプションセンターを持っていない場合に適しています。

このオプションでは、各メールカテゴリーごとに固有の配信停止リンクが必要となります：<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Liquid フィルターを使って、送信時にユーザーの external ID をハッシュ化することも可能です。これにより、`user_id` を MD5 ハッシュ値に変換できます。例：
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### オプション 2: JSON Web トークンで認証する

[JSON Web トークン](https://auth0.com/learn/json-web-tokens/)を使って、通常はユーザー名とパスワードによるログインのような認証レイヤーの後ろにある Web サーバーの一部（例えば、アカウント設定）でユーザーを認証します。 

このアプローチでは、URL に埋め込まれたクエリ文字列の値ペアを必要としません。これらは JSON Web トークンのペイロードで渡すことができます。例：

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": "offers"
}
```

## よくある質問

### ユーザー設定センターをまだ作成していません。ダッシュボードに「PreferenceCenterBrazeDefault」が表示されるのはなぜですか？

これは、レガシー Liquid {%raw%}`${preference_center_url}`{%endraw%} が使用されている場合にユーザー設定センターをレンダリングするために使用されます。つまり、{%raw%}`${preference_center_url}` または `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} のいずれかを参照するキャンバスステップまたはテンプレートは機能しません。これは、レガシー Liquid や「PreferenceCenterBrazeDefault」をメッセージの一部として含む、過去に送信されたメッセージにも適用されます。 

新しいメッセージで {%raw%}`${preference_center_url}`{%endraw%} を再度参照すると、「PreferenceCenterBrazeDefault」という名前のユーザー設定センターが再度作成されます。

### ユーザー設定センターは多言語に対応していますか？

いいえ。ただし、カスタムのオプトインおよびオプトアウトページの HTML を作成するときに Liquid を利用できます。ダイナミックリンクを使って配信停止を管理している場合、これは1つのリンクになります。 

たとえば、スペイン語圏のユーザーの配信停止率を追跡する場合には、別のキャンペーンを使用するか、Currents に関する分析（ユーザーが配信停止したタイミングを調べ、そのユーザーの優先言語をチェックするなど）を利用する必要があります。

もう1つの例として、スペイン語圏のユーザーの配信停止率を追跡するために、ユーザーの言語がスペイン語であれば `?Spanish=true` のようなクエリパラメーター文字列を配信停止 URL に追加し、それ以外の場合には標準の配信停止リンクを使用することができます。

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

そして、Currents を通して、どのユーザーがスペイン語を話し、その配信停止リンクのクリックイベントが何回あったかを特定することができます。

### 配信停止リンクとメールユーザー設定センターの両方が送信に必要ですか？

いいえ。メールキャンペーンの作成中に「メール本文に配信停止のリンクが含まれていません」というメッセージが表示されることがありますが、配信停止リンクがコンテンツブロック内にある場合、これは想定された警告です。

### デフォルトのブラウザアイコンはどうやって更新しますか？

デフォルトでは、ブラウザタブ名の横にあるアイコン（ファビコン）は Braze のロゴを使用します。カスタムファビコンを追加するには、Create または Update の[ユーザー設定センター API 呼び出し]({{site.baseurl}}/api/endpoints/preference_center)で `links-tags` 属性を使って設定します。Braze はその後、ホストされたページに {% raw %}`<link rel="icon" ...>`{% endraw %} タグを挿入します。

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}