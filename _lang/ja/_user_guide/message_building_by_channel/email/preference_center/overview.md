---
nav_title: 概要
article_title: ユーザー設定センターの概要
page_order: 1
description: "この記事では、Eメール・プリファレンス・センターとそのカスタマイズ方法について説明する。"
channel:
  - email
---

# ユーザー設定センターの概要

> ユーザー設定センターを設定することで、ユーザーが[メールメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/email/)の通知設定を編集や管理するためのワンストップショップを提供できます。この記事では、API で生成されたユーザー設定センターの作成手順を説明しますが、[ドラッグ＆ドロップエディター]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/)を使ってユーザー設定センターを作成することもできます。

Braze ダッシュボードで、[**オーディエンス**] > [**購読**] > [**メールユーザー設定センター**] に移動します。

ここで各サブスクリプショングループを管理し、見ることができる。作成した各購読グループは、このユーザー設定センターリストに追加されます。複数のユーザー設定センターを作成することができます。

{% alert important %}
ユーザー設定センターは、Braze のメールチャネル内で使用するために用意されています。ユーザー設定センターのリンクは、各ユーザーに基づいて動的に設定されるため、外部でホストすることはできません。
{% endalert %}

## API を使用してユーザー設定センターを作成する

[ユーザー設定センターの Braze エンドポイント]({{site.baseurl}}/api/endpoints/preference_center)を使用することで、ユーザー設定センター （Braze がホストする Web サイト） を作成し、ユーザーの購読状態や購読グループのステータスを表示することができます。開発者チームは HTML と CSS を使ってユーザー設定センターを作成することにより、ページのスタイルをブランドガイドラインに合わせることができます。

Liquid を使うことで、購読グループの名前と各ユーザーのステータスを取得できます。こうすることで、Brazeはページがロードされたときにこのデータを保存・取得する。

### 前提条件

| 必要条件 | 説明 |
|---|---|
| ユーザー設定センターが有効になっている | Braze ダッシュボードには、ユーザー設定センター機能を使用する権限があります。 |
| Eメール、SMS、またはWhatsAppの購読グループで有効なワークスペース | 有効なユーザーと、Eメール、SMS、またはWhatsAppの購読グループを持つ作業ワークスペース。 |
| 有効なユーザー | メールアドレスと外部IDを持つユーザー。 |
| ユーザー設定センターの権限を持つ API キーを生成済みである | Brazeダッシュボードで、**[設定]>**[**APIキー]**に進み、プリファレンスセンターの権限を持つAPIキーにアクセスできることを確認する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ1:ユーザー設定センターの作成エンドポイントを使用する

[ユーザー設定センターの作成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)を使って、ユーザー設定センターの作成を開始します。ユーザー設定センターをカスタマイズするには、`preference_center_page_html` フィールドと `confirmation_page_html` フィールドにブランディングに沿った HTML を含めることができます。

[ユーザー設定センターの URL の生成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)を使用すると、Braze を通じて送信されるメールの外で、特定のユーザーのユーザー設定センター URL を取得できます。

### ステップ 2: メールキャンペーンに含める

{% multi_lang_include preference_center_warning.md %}

メールにユーザー設定センターへのリンクを配置するには、配信停止 URL を挿入する方法と同様に、メール内の適切な場所で以下の Liquid タグを使用します。

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

リキッドを含むHTMLを組み合わせて使うこともできる。例えば、HTMLエディターでもドラッグ＆ドロップ・エディターでも、URLとして次のように貼り付けることができる。これにより、すべてのメール購読グループを自動的にリストアップする基本的なユーザー設定センターのレイアウトが表示されます。 

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}">Edit your preferences</a>
```
{%endraw%}

ユーザー設定センターには、ユーザーがすべてのメールの配信を停止できるチェックボックスがあります。テスト・メッセージとして送信された場合、これらの設定を保存することはできないので注意すること。

{% alert important %}
上記のリキッドタグは、キャンペーンやキャンバスを立ち上げるときにのみ機能する。テストメールを送信しても、有効なリンクは生成されない。
{% endalert %}

#### ユーザー設定センターの編集

[ユーザー設定センターの更新のエンドポイント]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)を使って、ユーザー設定センターを編集・更新できます。 

#### ユーザー設定センターと詳細の確認

ユーザー設定センターを特定するには、[ユーザー設定センターの詳細を表示エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)を使用して、最終更新タイムスタンプ、ユーザー設定センター ID などの関連情報を返します。

## カスタマイズ

Braze は、ユーザー設定センターからの購読状態の更新を管理し、ユーザー設定センターの同期を保ちます。ただし、[購読グループ API]({{site.baseurl}}/api/endpoints/subscription_groups/) を使用して、以下のオプションで独自のユーザー設定センターを作成し、ホストすることも可能です。

### オプション 1: 文字列クエリパラメータを持つリンク

URL の本文でクエリ文字列フィールドと値のペアを使用して、ユーザーの ID とメールカテゴリをページに渡します。これにより、ユーザーは配信を停止する選択肢を確認するだけで済みます。このオプションは、ユーザー識別子をハッシュ形式で保存し、まだサブスクリプション・センターを持っていない人に適している。

このオプションでは、各メールのカテゴリーごとに固有の配信停止リンクが必要となる：<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Liquid フィルターを使って、送信時にユーザーの外部 ID をハッシュ化することも可能です。これは例えば、`user_id` をMD5ハッシュ値に変換する：
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### オプション 2: JSONウェブトークンで認証する

[JSONウェブトークンを使って](https://auth0.com/learn/json-web-tokens/)、通常はユーザー名とパスワードによるログインのような認証レイヤーの後ろにあるウェブサーバーの一部（例えば、アカウント設定）でユーザーを認証する。 

このアプローチでは、URLに埋め込まれたクエリー文字列のバリュー・ペアを必要としないため、例えばJSONウェブトークンのペイロードで渡すことができる：

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

## よくある質問

### ユーザー設定センターをまだ作成していません。ダッシュボードに "PreferenceCenterBrazeDefault "が表示されるのはなぜか？

これは、レガシー Liquid {%raw%}`${preference_center_url}`{%endraw%} が仕様されている場合にユーザー設定センターをレンダリングするために使用されます。つまり、{%raw%}`${preference_center_url}` または `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} のいずれかを参照するキャンバスステップまたはテンプレートは機能しません。これは、レガシーLiquidや "PreferenceCenterBrazeDefault "をメッセージの一部として含む、過去に送信されたメッセージにも適用される。 

新しいメッセージで {%raw%}`${preference_center_url}`{%endraw%} を再度参照すると、「PreferenceCenterBrazeDefault」という名前のユーザー設定センターが再度作成されます。

### ユーザー設定センターは多言語に対応しているか？

いいえ。ただしカスタムのオプトインおよびオプトアウトページの HTML を作成するときに Liquid を利用できます。ダイナミックリンクを使って配信停止を管理している場合、これは 1 つのリンクになります。 

たとえば、スペイン語圏のユーザーの配信停止率を追跡する場合には、別のキャンペーンを使用するか、Currents に関する分析 (ユーザーが配信停止したタイミングを調べ、そのユーザーの優先言語をチェックするなど) を利用する必要があることがあります。

もう 1 つの例として、スペイン語圏のユーザーの配信停止率を追跡するために、ユーザーの言語がスペイン語であれば `?Spanish=true` のようなクエリパラメーター文字列を配信停止 URL に追加しそれ以外の場合には標準の配信停止リンクを使用することができます。

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

そして、Currentsを通して、どのユーザーがスペイン語を話し、その配信停止リンクのクリックイベントが何回あったかを識別することができる。

### 配信停止リンクとユーザー設定センターの両方が送信に必要か？

いいえ。配信停止リンクがコンテンツブロック内にある場合、メールキャンペーンの作成中に「メール本文に配信停止のリンクが含まれていません」というメッセージが表示されます。
