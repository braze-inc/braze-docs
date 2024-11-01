---
nav_title: ユーザーマネージャー
article_title: LINEユーザーマネージャー
page_order: 0
description: "この記事では、LINEのユーザーIDとその設定方法について解説する。"
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINEユーザーマネージャー

> LINEのユーザーIDは、`native_line_id` というユーザープロファイル属性に格納されている。この識別子は、LINEチャネルでユーザーにメッセージを送信する際に使用される。この記事は、`native_line_id` 属性をカバーし、LINEベータ・コレクションの一部である。[メインページに戻ります](https://www.braze.com/docs/line/)。

顧客ユーザーデータは、[Brazeユーザープロファイルで]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)表される。ユーザープロファイルには、名やメール・アドレスなど、企業のユーザーに関する情報や属性が保存される。

Brazeを通じてLINEメッセージを送信する際、Brazeは`native_line_id` 属性を使用してメッセージを送信するユーザーを識別する。ユーザーがチャネルをフォローしたときやメッセージに返信したときなど、LINEがBrazeのWebhookイベントを送信すると、`native_line_id` 、対応するユーザープロファイルが検索される。

{% alert note %}
LINEのユーザーIDは、LINEの提供元によって区別されている。特定のユーザーは、フォローしているプロバイダーごとに異なるLINEユーザーIDを持つことになる。ユーザーIDはフォローするブランドごとに変わるため、（メールや電話番号と違って）ユーザーが自分のLINE IDを知っている可能性は低い。
{% endalert %}

## `native_line_id` を設定する。

ユーザープロファイルに`native_line_id` が設定されるシナリオはいくつかあるが、その概要は以下の通り。

| シナリオ | を持つユーザープロファイルが存在するかどうか。 `native_line_id` | 結果 |
| --- | --- | --- |
|ユーザーがLINEチャネルをフォローする | いいえ| 匿名ユーザープロファイルが作成される（マージが必要）：<br> -`native_line_id` 、ユーザーのLINE IDが設定される。 <br>-`line_id` ユーザーエイリアスはユーザーのLINE IDに設定される。<br>\- ユーザーがチャネルのサブスクリプショングループにサブスクライブしている。 |
|ユーザーがLINEチャネルをフォローする| はい | `native_line_id` を持つすべてのユーザープロファイル：<br>\- チャネルのサブスクリプショングループにサブスクライブしている。|
|ユーザーCSVアップロードで、`ative_line_id` のカラムを使用している。| いいえ| 指定された`external_id` またはユーザーエイリアスのユーザープロファイルが存在しない場合：<br>-`native_line_id` が指定された値に設定される。<br> \- CSVで指定されたその他の属性はすべてユーザープロファイルに設定される|
|同社はユーザーCSVアップロードを`native_line_id` 列で使用している。 | はい | 指定された`external_id` またはユーザーエイリアスのユーザープロファイルが存在する場合：<br>-`native_line_id` が指定された値に設定される。<br>\- CSVで指定されたその他の属性はすべてユーザープロファイルに設定される<br>\- 複数のプロファイルが同じである。 `native_line_id` |
| 会社は`/users/track` エンドポイントを使用し、`native_line_id` 属性を指定する。 | いいえ | 指定されたユーザー[（`external_id`]({{site.baseurl}}/api/objects_filters/user_attributes_object/) 、`user_alias`({{site.baseurl}}/api/objects_filters/user_attributes_object/) 、`braze_id` 、`email` で指定({{site.baseurl}}/api/objects_filters/user_attributes_object/)）のユーザープロファイルが存在しない場合：<br>-`native_line_id` が指定された値に設定される。<br>\- リクエストで指定された他のすべての属性は、ユーザープロファイルに設定される。 |
| 会社は`/users/track` エンドポイントを使用し、`native_line_id` 属性を指定する。 | はい | 指定されたユーザー[（`external_id` 、`user_alias` 、`braze_id` または`email` で指定]({{site.baseurl}}/api/objects_filters/user_attributes_object/)）のユーザープロファイルが存在する場合：<br>-`native_line_id` が指定された値に設定される。<br>\- リクエストで指定された他のすべての属性は、ユーザープロファイルに設定される。<br>\- 複数のプロファイルが同じである。 `native_line_id` |
| 会社からBrazeにサブスクリプションステータスの同期を依頼する。 | いいえ | LINEから返されたユーザーLINE IDがBrazeに対応するユーザープロファイルを持たない場合、匿名ユーザープロファイルが作成される：<br>-`native_line_id` 、ユーザーのLINE IDが設定される。<br>-`line_id` ユーザーエイリアスはユーザーのLINE IDに設定される。<br>\- ユーザーがチャネルのサブスクリプショングループにサブスクライブしている。<br><br>同じLINE IDのユーザーを後から作成した場合、重複したユーザーが存在することになるが、どちらも正しいLINEのサブスクリプションステータスを持つことになる。ユーザー統合は、このような場合にユーザー群を一掃することができる。 |
| 会社からBrazeにサブスクリプションステータスの同期を依頼する。 | はい | LINEから返されたユーザーIDがBrazeのユーザープロファイルと一致する場合：<br>\- ユーザーがチャネルのサブスクリプショングループにサブスクライブしている。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## を見つける `native_line_id`

Brazeダッシュボードでユーザープロファイルを表示する際、`native_line_id` 属性が設定されているかどうかは、**エンゲージメントタブ**>**コンタクト設定**セクション >**LINE**セクションで確認できる。

`native_line_id` が設定されている場合は、**LINEユーザーIDの**下に表示される。そうでなければ表示されない。

![エンゲージメント・タブのライン・コンタクト設定。][1]{: style="max-width:60%;"}

[1]: {% image_buster /assets/img/line/line_contact_settings.png %}
