---
nav_title: 概要
article_title: プリファレンス・センターの概要
page_order: 1
description: "この記事では、Eメール・プリファレンス・センターとそのカスタマイズ方法について説明する。"
channel:
  - email
---

# プリファレンス・センターの概要

> プリファレンスセンターを設定することで、ユーザーが[メールメッセージの]({{site.baseurl}}/user_guide/message_building_by_channel/email/)通知設定を編集・管理するためのワンストップショップを提供できる。<br><br>以下の記事では、APIによって生成されたプリファレンス・センターを構築する方法を説明しているが、[ドラッグ＆ドロップ・エディターを使って]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/)プリファレンス・センターを構築することもできる。

Brazeのダッシュボードで、**Audience**>**Subscriptions**>**Email Preference Centerと**進む。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは「**ユーザー**」>「**購読グループ」>「Eメール設定センター**」にある。
{% endalert %}

ここで各サブスクリプショングループを管理し、見ることができる。あなたが作成した各サブスクリプショングループは、このプリファレンスセンターリストに追加される。複数のプリファレンスセンターを作ることができる。

{% alert important %}
プリファレンスセンターは、BrazeのEメールチャネル内で使用されることを意図している。プリファレンス・センターのリンクは、各ユーザーに基づいて動的に設定されるため、外部でホストすることはできない。
{% endalert %}

## API経由でプリファレンス・センターを作成する

[プリファレンスセンターBrazeエンドポイントを]({{site.baseurl}}/api/endpoints/preference_center)使用することで、プリファレンスセンター（Brazeがホストするウェブサイト）を作成し、ユーザーのサブスクリプション状態やサブスクリプショングループのステータスを表示することができる。HTMLとCSSを使ってプリファレンス・センターを構築し、ページのスタイリングをブランド・ガイドラインに合わせる。

Liquidを使うことで、購読グループの名前と各ユーザーのステータスを取得することができる。こうすることで、Brazeはページがロードされたときにこのデータを保存・取得する。

### 前提条件

| 必要条件 | 説明 |
|---|---|
| プリファレンス・センターを有効にする | Brazeダッシュボードには、プリファレンスセンター機能を使用する権限がある。 |
| Eメール、SMS、またはWhatsAppの購読グループで有効なワークスペース | 有効なユーザーと、Eメール、SMS、またはWhatsAppの購読グループを持つ作業ワークスペース。 |
| 有効なユーザー | メールアドレスと外部IDを持つユーザー。 |
| プリファレンス・センターの権限を持つAPIキーを生成する | Brazeダッシュボードで、**\[設定]>**\[**APIキー]**に進み、プリファレンスセンターの権限を持つAPIキーにアクセスできることを確認する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、\[**開発者コンソール**] > \[**API 設定**] から API キーを作成できます。
{% endalert %}

### ステップ 1:API経由でプリファレンス・センターを作成する

[プリファレンス・センターの作成」エンドポイントを使って]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)、プリファレンス・センターを作り始めよう。プリファレンス・センターをカスタマイズするには、`preference_center_page_html` フィールドと`confirmation_page_html` フィールドにブランディングに沿ったHTMLを含めることができる。

[プリファレンスセンターURLの生成エンドポイントを]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)使用すると、Brazeを通じて送信される電子メールの外側で、特定のユーザーのプリファレンスセンターURLを取得できる。

### ステップ 2:Eメールキャンペーンに含める

{% multi_lang_include preference_center_warning.md %}

メールにプリファレンスセンターへのリンクを設置するには、配信停止URLを挿入する方法と同様に、メール内の必要な場所に以下のLiquidタグを使用する。

{% raw %}
```liquid
{{preference_center.${preference_center_name_example}}}
```
{%endraw%}

リキッドを含むHTMLを組み合わせて使うこともできる。例えば、HTMLエディターでもドラッグ＆ドロップ・エディターでも、URLとして次のように貼り付けることができる。これにより、すべてのEメール購読グループを自動的にリストアップする基本的なプリファレンスセンターのレイアウトが表示される。 

{% raw %}
```html
<a href="{{preference_center.${preference_center_name_example}}}">Edit your preferences</a>
```
{%endraw%}

プリファレンスセンターには、ユーザーがすべてのメールの配信を停止できるチェックボックスがある。テスト・メッセージとして送信された場合、これらの設定を保存することはできないので注意すること。

{% alert important %}
上記のリキッドタグは、キャンペーンやキャンバスを立ち上げるときにのみ機能する。テストメールを送信しても、有効なリンクは生成されない。
{% endalert %}

#### プリファレンス・センターを編集する

プリファレンス・センターの[更新エンドポイントを]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)使えば、プリファレンス・センターを編集・更新できる。 

#### 選好センターと詳細を特定する

プリファレンス・センターを特定するには、[プリファレンス・センターの詳細を表示エンドポイントを]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)使用して、最終更新タイムスタンプ、プリファレンス・センターIDなどの関連情報を返す。

## カスタマイズ

Brazeは、プリファレンスセンターからのサブスクリプションの状態更新を管理し、プリファレンスセンターの同期を保つ。しかし、[サブスクリプション・グループAPIを使って]({{site.baseurl}}/developer_guide/rest_api/subscription_group_api/)、以下のオプションで独自のプリファレンス・センターを作成し、ホストすることもできる。

### オプション 1: 文字列クエリパラメータを持つリンク

URL本文のクエリー文字列フィールドと値のペアを使用して、ユーザーIDとEメールカテゴリーをページに渡す。このオプションは、ユーザー識別子をハッシュ形式で保存し、まだサブスクリプション・センターを持っていない人に適している。

このオプションでは、各メールのカテゴリーごとに固有の配信停止リンクが必要となる：<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
リキッドフィルターを使って、送信時にユーザーの外部IDをハッシュ化することも可能だ。これは例えば、`user_id` をMD5ハッシュ値に変換する：
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
