---
nav_title: ユーザー管理
article_title: LINEユーザーマネージャー
page_order: 0
description: "この記事では、LINEのユーザーIDとその設定方法について解説する。"
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINEユーザーマネージャー

> LINE ユーザID は、`native_line_id` というユーザプロファイル属性に保存されます。この属性は、LINE チャネルでユーザにメッセージを送信するために使用されます。この記事では、`native_line_id` 属性を設定して検索する方法について説明します。

顧客ユーザーデータは、[Braze ユーザープロファイル]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)で表されます。ユーザープロファイルには、名やメール・アドレスなど、企業のユーザーに関する情報や属性が保存される。 

Brazeを通じてLINEメッセージを送信する際、Brazeは`native_line_id` 属性を使用してメッセージを送信するユーザーを識別する。ユーザーがチャネルをフォローしたりメッセージに返信したりするときなど、LINE によって Braze Webhook イベントが送信されると、`native_line_id` が使用されて対応するユーザープロファイルが検索されます。

{% alert note %}
LINEのユーザーIDは、LINEの提供元によって区別されている。特定のユーザーは、フォローしているプロバイダーごとに異なるLINEユーザーIDを持つことになる。ユーザーIDはフォローするブランドごとに変わるため、（メールや電話番号と違って）ユーザーが自分のLINE IDを知っている可能性は低い。
{% endalert %}

## `native_line_id` 属性の設定

ユーザープロファイルに`native_line_id` が設定されるシナリオはいくつかあるが、その概要は以下の通り。

| シナリオ | `native_line_id` を持つユーザープロファイルが存在するかどうか | 結果 |
| --- | --- | --- |
|ユーザーがLINEチャネルをフォローする | いいえ| 匿名ユーザープロファイルが作成される (マージが必要)：<br> -`native_line_id` にユーザーの LINE ID が設定されます <br>-`line_id` ユーザーエイリアスはユーザーのLINE IDに設定される。<br>\- ユーザーがチャネルの Braze 購読グループに購読登録されている |
|ユーザーがLINEチャネルをフォローする| はい | `native_line_id` を持つすべてのユーザープロファイル：<br>\- チャネルの Braze 購読グループに購読登録済みです|
|会社は n`ative_line_id` 列を持つユーザーの CSV アップロードを使用します| いいえ| 指定された`external_id` またはユーザーエイリアスのユーザープロファイルが存在しない場合：<br>-`native_line_id` が指定された値に設定されます<br> \- CSVで指定されたその他の属性はすべてユーザープロファイルに設定される|
|同社はユーザーCSVアップロードを`native_line_id` 列で使用している。 | はい | 指定した `external_id` またはユーザーエイリアスのユーザープロファイルが存在する場合：<br>-`native_line_id` が指定された値に設定されます<br>\- CSVで指定されたその他の属性はすべてユーザープロファイルに設定される<br>\- 複数のプロファイルに同じ `native_line_id` があります |
| 会社は `/users/track` エンドポイントを使用し、`native_line_id` 属性を指定します | いいえ | 指定したユーザー ([`external_id`、`user_alias`、`braze_id`、`email` で指定]({{site.baseurl}}/api/objects_filters/user_attributes_object/)) のユーザープロファイルが存在しない場合:<br>-`native_line_id` が指定された値に設定されます<br>\- リクエストで指定された他のすべての属性がユーザープロファイルに設定されます |
| 会社は `/users/track` エンドポイントを使用し、`native_line_id` 属性を指定します | はい | 指定したユーザー ([`external_id`、`user_alias`、`braze_id`、`email` で指定]({{site.baseurl}}/api/objects_filters/user_attributes_object/)) のユーザープロファイルが存在する場合:<br>-`native_line_id` が指定された値に設定されます<br>\- リクエストで指定された他のすべての属性がユーザープロファイルに設定されます<br>\- 複数のプロファイルに同じ `native_line_id` があります |
| 会社からBrazeにサブスクリプションステータスの同期を依頼する。 | いいえ | LINEから返されたユーザーLINE IDがBrazeに対応するユーザープロファイルを持たない場合、匿名ユーザープロファイルが作成される：<br>-`native_line_id` にユーザーの LINE ID が設定されます<br>-`line_id` ユーザーエイリアスはユーザーのLINE IDに設定される。<br>\- ユーザーがチャネルの Braze 購読グループに購読登録されている<br><br>同じLINE IDのユーザーを後から作成した場合、重複したユーザーが存在することになるが、どちらも正しいLINEのサブスクリプションステータスを持つことになる。ユーザーのマージによって、このような場合にユーザー群をクリーンアップできます。 |
| 会社からBrazeにサブスクリプションステータスの同期を依頼する。 | はい | LINE から返されたユーザー ID に対応するユーザープロファイルが Braze にある場合:<br>\- ユーザーがチャネルの Braze 購読グループに購読登録されている |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

## `native_line_id` を見つける

Braze ダッシュボードでユーザープロファイルを表示する際、`native_line_id` 属性が設定されているかどうかは、**エンゲージメントタブ**>**コンタクト設定**セクション >**LINE**セクションで確認できる。

`native_line_id` が設定されていれば、**LINEユーザーIDの**下に表示される。そうでなければ表示されない。

![エンゲージメントタブのラインコンタクト設定。]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}

