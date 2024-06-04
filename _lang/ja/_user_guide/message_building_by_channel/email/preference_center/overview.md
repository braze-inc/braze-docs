---
nav_title: 概要
article_title: プリファレンスセンターの概要
page_order: 1
description: "この記事では、メール設定センターとそのカスタマイズ方法について説明します。"
channel:
  - email
---

# プリファレンスセンターの概要

> プリファレンスセンターを設定すると、ユーザーが [メールメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/email/)の通知設定を編集および管理するためのワンストップショップが提供されます。<br><br>次の記事では、API で生成された設定センターを構築する方法について説明しますが、 [ドラッグ アンド ドロップ エディター]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/)を使用して設定センターを構築することもできます。

Braze ダッシュボードで、**メール設定センターの** **Audience** > **Subscriptions** >に移動します。

{% alert note %}
[以前のナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは **[ユーザー**] > **[サブスクリプション グループ] > [メール設定センター**] にあります。
{% endalert %}

ここでは、各サブスクリプション グループを管理および表示できます。作成した各サブスクリプショングループは、このプリファレンスセンターリストに追加されます。複数のプリファレンスセンターを作成できます。

{% alert important %}
プリファレンスセンターは、Brazeメールチャネル内で使用するためのものです。プリファレンスセンターのリンクは、各ユーザーに基づいて動的であり、外部でホストすることはできません。
{% endalert %}

## API経由で設定センターを作成

[プリファレンスセンターの Braze エンドポイント]({{site.baseurl}}/api/endpoints/preference_center)を使用すると、ユーザーのサブスクリプションの状態とサブスクリプショングループのステータスを表示できるプリファレンスセンター (Braze がホストする Web サイト) を作成できます。HTML と CSS を使用すると、開発者チームは HTML と CSS を使用して設定センターを構築し、ページのスタイルをブランドガイドラインに合わせることができます。

Liquidを使用すると、サブスクリプショングループの名前と各ユーザーのステータスを取得できます。このようにして、Brazeはページがロードされたときにこのデータを保存し、取得します。

### 前提 条件

|応募資格 |説明 |
|---|---|
|有効化されたプリファレンスセンター |Brazeダッシュボードには、プリファレンスセンター機能を使用する権限があります。|
|メール、SMS、または WhatsApp サブスクリプション グループを含む有効なワークスペース |有効なユーザーとメール、SMS、または WhatsApp サブスクリプション グループを含む作業ワークスペース。|
|有効なユーザー |メールアドレスと外部 ID を持つユーザー。 |
|プリファレンスセンターの権限で生成されたAPIキー |Brazeダッシュボードで、[ **設定** ]> **[APIキー** ]に移動して、プリファレンスセンターの権限を持つAPIキーにアクセスできることを確認します。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**開発者コンソール**の **[API 設定**] > API キーを作成できます。
{% endalert %}

### ステップ 1:API経由で設定センターを作成

[設定センターの作成]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)エンドポイントを使用して、設定センターの構築を始めましょう。プリファレンスセンターをカスタマイズするには、ブランディング `preference_center_page_html` に合わせたHTMLをフィールドと `confirmation_page_html` フィールドに含めることができます。

[設定センターのURLを生成]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)エンドポイントを使用すると、Brazeを介して送信される電子メールの外部にある特定のユーザーの設定センターのURLを取得できます。

### ステップ 2:メールキャンペーンに含める

メールにプリファレンスセンターへのリンクを配置するには、登録解除URLを挿入する方法と同様に、メール内の目的の場所で次のLiquidタグを使用します。

{% raw %}
```liquid
{{preference_center.${preference_center_name_example}}}
```
{%endraw%}

また、Liquid を含む HTML を組み合わせて使用することもできます。たとえば、HTML エディターまたはドラッグ アンド ドロップ エディターで URL として以下を貼り付けることができます。これにより、すべてのメール購読グループが自動的に一覧表示される基本的な設定センターのレイアウトが表示されます。 

{% raw %}
```html
<a href="{{preference_center.${preference_center_name_example}}}">Edit your preferences</a>
```
{%endraw%}

プリファレンスセンターには、ユーザーがすべてのメールの購読を解除できるチェックボックスがあります。これらの設定をテストメッセージとして送信した場合、保存できないことに注意してください。

{% alert important %}
上記のLiquidタグは、キャンペーンまたはキャンバスを起動するときにのみ機能します。テストメールを送信しても、有効なリンクは生成されません。
{% endalert %}

#### プリファレンスセンターの編集

プリファレンスセンターを編集および更新するには、 [プリファレンスセンターの更新エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)を使用します。 

#### プリファレンスセンターと詳細の識別

プリファレンスセンターを特定するには、 [プリファレンスセンター]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) エンドポイントの詳細を表示を使用して、最終更新タイムスタンプ、プリファレンスセンターIDなどの関連情報を返します。

## カスタマイズ

Brazeは、プリファレンスセンターからサブスクリプション状態の更新を管理し、プリファレンスセンターの同期を維持します。ただし、次のオプションで [サブスクリプショングループ API]({{site.baseurl}}/developer_guide/rest_api/subscription_group_api/) を使用して、独自のプリファレンスセンターを作成およびホストすることもできます。

### オプション 1:文字列クエリ パラメーターとのリンク

URL の本文でクエリ文字列のフィールドと値のペアを使用して、ユーザー ID とメール カテゴリをページに渡すと、ユーザーは登録解除の選択を確認するだけで済みます。このオプションは、ユーザー識別子をハッシュ形式で保存し、サブスクリプション センターをまだ持っていないユーザーに適しています。

このオプションでは、各メールカテゴリに固有の登録解除が必要です link:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
また、Liquidフィルターを使用して、送信時にユーザーの外部IDをハッシュ化することもできます。これにより、次のように が `user_id` MD5 ハッシュ値に変換されます。
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### オプション 2:JSON Web トークンによる認証

[JSON Web トークン](https://auth0.com/learn/json-web-tokens/)を使用して、通常はユーザー名やパスワードによるログインなどの認証レイヤーの背後にある Web サーバーの一部 (アカウント設定など) に対してユーザーを認証します。 

このアプローチでは、クエリ文字列の値のペアを JSON Web トークンのペイロードで渡すことができるため、URL に埋め込む必要はありません。

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```
