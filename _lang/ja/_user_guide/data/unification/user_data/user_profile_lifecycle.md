---
nav_title: ユーザープロファイルのライフサイクル
article_title: ユーザープロファイルのライフサイクル
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze のユーザープロファイルのライフサイクルと、ユーザープロファイルを識別して参照するさまざまな方法について説明します。"

---

# ユーザープロファイルのライフサイクル

> この記事では、Brazeユーザープロファイルのライフサイクルと、ユーザープロファイルの識別子と参照のさまざまな方法について説明する。カスタマーライフサイクルをより詳しく理解したい場合は、[ユーザーライフサイクルのマッピング](https://learning.braze.com/mapping-customer-lifecycles)に関する Braze ラーニングコースをご覧ください。

ユーザーに関連付けられるすべての永続データは、そのユーザープロファイルに保存されます。API を使用してユーザープロファイルが作成された後、または SDK によりユーザーが認識された後でユーザープロファイルが作成された後に、そのユーザーを識別および参照するために、そのプロファイルに多数のパラメーターを割り当てることができます。 

これらのパラメーターには以下のものが含まれます。

* `braze_id` (担当：Braze）
* `external_id`
* `email`
* `phone`
* 設定した任意の数のカスタムユーザーエイリアス

## 匿名ユーザープロファイル

`external_id` が指定されていないユーザーは[匿名ユーザー]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/)と呼ばれます。例えば、Webサイトを訪問したがサインアップしなかったユーザーや、モバイルアプリをダウンロードしたがプロファイルを作成しなかったユーザーなどである。

最初に、SDK によりユーザーが認識されると、匿名ユーザープロファイルが作成され、Braze によって自動的に割り当てられた一意の識別子 `braze_id` が関連付けられます。この識別子は編集できず、デバイスに固有です。この識別子を使用して、[API]({{site.baseurl}}/api/endpoints/user_data/) を介してそのユーザープロファイルを更新できます。

## 識別されたユーザープロファイル

ユーザー ID またはメールアドレスを入力することにより、アプリでユーザーが認識されたら、`changeUser` メソッドを使用してそのユーザープロファイルに `external_id` を割り当てることをお勧めします ([Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:))、[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html))。`external_id` により、複数のデバイスで同じユーザープロファイルを識別できます。

`external_id` を使用すると、さらに次のような利点があります。 

- 複数のデバイスやプラットフォームにわたって一貫したユーザーエクスペリエンスを提供できます (例えば、iPhone アプリの忠実なユーザーの Android タブレットには、離脱ユーザー向けの通知を送信しない)。
- ユーザーがアプリをアンインストールして再インストールするたびに、または別のデバイスにアプリをインストールするたびに、新しいユーザープロファイルが作成されていないことを確認して、分析の精度を向上できます。
- [ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/user_data/)を使用して、アプリ外のソースからユーザーデータをインポートできるようになり、また[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)を使用して、トランザクションメッセージのターゲットユーザーを設定できるようになります。
- セグメンター内で「テスト」[フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)を使用するか、または [[**ユーザー検索**]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/)] ページを使用して、個々のユーザーを検索できます。

### 外部IDに関する考察

{% alert warning %}
ユーザープロファイルを一意に識別する前に、`external_id` を割り当てないこと。ユーザーを識別した後、匿名ユーザーに戻すことはできません。
<br><br>
`external_id` は[`/users/external_ids/rename` エンドポイントを使って]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)更新できる。しかし、ユーザーのセッション中に異なる`external_id` を設定しようとすると、新しい`external_id` に関連付けられた新しいユーザープロファイルが作成される。2 つのプロファイル間でデータは渡されません。
{% endalert %} 

#### メールやハッシュ化されたメールを外部IDとして使用するリスク

メールアドレスまたはハッシュ化されたメールアドレスをBraze外部IDとして使用すると、データソース全体のID管理を簡素化できますが、ユーザープライバシーとデータセキュリティに対する潜在的なリスクを考慮することが重要です。

- **推測可能な情報:**メールアドレスは推測されやすく、攻撃されやすい。
- **悪用のリスク:**悪意のあるユーザーがWebブラウザーを改ざんし、他人のメールアドレスを外部IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性がある。

### 匿名ユーザーを識別するとどうなるか

匿名ユーザーを識別する場合、次の2つのシナリオのいずれかが発生する可能性があります。

1) **匿名ユーザーが、識別された新規ユーザーになる。**<br>`external_id` がまだBrazeに存在しない場合、匿名ユーザーは新しい識別子ユーザーとなり、匿名ユーザーと同じ属性と履歴をすべて保持する。 

2) **匿名ユーザーが、既存のユーザーとして識別される。**<br>`external_id` がすでにBrazeに存在する場合、このユーザーは、別のデバイス（タブレットなど）やインポートされたユーザーデータなど、何らかの他の方法で以前にシステムのユーザーとして識別されていたことになる。 

言い換えれば、あなたはすでにこのユーザーのユーザープロファイルを持っている。この場合、Braze は次のことを行います。
1. 匿名ユーザーを孤立させます
2. 匿名プロファイルから、識別されたユーザープロファイルにまだ存在しない[特定のユーザープロファイルのフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)をマージします
3. ユーザー数が増えないように、その匿名プロファイルをユーザー群から削除します

匿名ユーザーと既知のユーザーの両方に名がある場合、既知のユーザーの名が維持されます。既知のユーザーが NULL 値を持ち、匿名ユーザーが値が含まれており、その値がこれらの[特定のユーザープロファイルのフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)に該当すれば、匿名ユーザーの値は既知のユーザーのプロファイルにマージされます。

ユーザープロファイルに対して`external_id` を設定する方法については、ドキュメント[（iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift)、[Android]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android)、[Web]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web)）を参照のこと。

## ユーザーのエイリアス

Braze`external_id` 以外の識別子でユーザーを参照するには、ユーザープロファイルに対してユーザーエイリアスを設定する。ユーザープロファイルに設定されたエイリアスは、ユーザーの `braze_id` または`external_id` を置き換えるのではなく、それらに加えて作用します。ユーザープロファイルに設定できるエイリアスの数に制限はありません。

各エイリアスは、2 つの部分 (エイリアスのキーを定義する `alias_label` と、値を定義する `alias_name`) で構成されるキーと値のペアとして機能します。1つのラベルの `alias_name` は、ユーザー群全体で一意でなければなりません (`external_id` と同様)。既存のラベルと名前の組み合わせで2つ目のユーザープロファイルを更新しようとすると、ユーザープロファイルは更新されない。

### ユーザーエイリアスの更新

エイリアスは、[ユーザーデータエンドポイントを]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint)使用するか、SDKを通して新しい名前を渡すことによって、設定後に与えられたラベルの新しい名前で更新することができる。これにより、そのユーザーデータをエクスポートするときに、ユーザーエイリアスが表示されます。

![同じユーザーエイリアスラベルを持つが、異なるエイリアス名を持つ別のユーザーの 2 つの異なるユーザープロファイル]({% image_buster /assets/img_archive/Braze_User_aliases.png %})

### 匿名ユーザーにタグを付ける

ユーザーエイリアスを使用すると、匿名ユーザーに識別子のタグを付けることもできます。例えば、あるユーザーが e コマースサイトにメールアドレスを提供していてもまだサインアップしていない場合、そのメールアドレスをその匿名ユーザーのエイリアスとして使用できます。このようなユーザーは、エイリアスを使用してエクスポートしたり、API で参照したりできます。

### 匿名ユーザープロファイルでのエイリアスの動作

エイリアスを持つ、ある匿名ユーザープロファイルが後で `external_id` で認識された場合、それらは通常の識別されたユーザープロファイルとして扱われます。ただし、既存のエイリアスは保持され、そのエイリアスによって参照できます。

### 既知のユーザープロファイルにエイリアスを設定する

ユーザーエイリアスを既知のユーザープロファイルに設定して、別の外部の既知の ID によって既知のユーザーを参照することもできます。たとえば、Braze 内で参照しようとするビジネスインテリジェンスツール ID (Amplitude の ID など) をユーザーが持っている場合があります。

ユーザーエイリアスの設定方法については、各プラットフォーム ([iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users)、[Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users)) に関する弊社のドキュメントを参照してください。

![Brazeにおけるユーザープロファイルのライフサイクルのフローチャート。匿名ユーザーについて changeUser () が呼び出されると、そのユーザーは識別されたユーザーになり、そのデータは識別されたユーザープロファイルに移行されます。識別されたユーザーは Braze ID と external ID を持ちます。この時点で、2 人目の匿名ユーザーに changeUser() を呼び出すと、その識別されたユーザーにまだ存在しないユーザーデータのフィールドがマージされます。識別されたユーザーの既存のユーザープロファイルにエイリアスが追加されている場合、データは影響を受けませんが、エイリアスを持つ識別ユーザーになります。識別されたユーザーと同じエイリアスラベルを持つが、別のエイリアス名を持つ 3 人目の匿名ユーザーについて changeUser () を呼び出すと、識別されたユーザーに存在しないフィールドがすべてマージされ、識別されたユーザープロファイルのエイリアスラベルは維持されます。]({% image_buster /assets/img_archive/Braze_User_flowchart.png %})

{% alert tip %}
顧客のユーザープロファイルライフサイクルで、このプロセスがどのように行われるかを想像しにくい場合は、ユーザーデータ収集の[ベストプラクティス]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/)を参照してください。
{% endalert %}

## 高度なユースケース

SDKおよび[ユーザーデータエンドポイントを]({{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint)使用したAPIを通じて、既存の識別子ユーザープロファイルに新しいユーザーエイリアスを設定することができる。ただし、既存の未知のユーザープロファイルには、API を使用してユーザーエイリアスを設定することはできません。

このプロセスではユーザーエイリアスもマージされます。しかし、孤児となるユーザーとターゲットユーザーの両方が同じラベルのエイリアスを持つ場合、ターゲットユーザーのエイリアスのみが維持される。

アプリをアンインストールして再インストールすると、そのユーザーについて新規の匿名 `braze_id` が生成されます。

### ユーザーIDに関するトラブルシューティング

テストとして、ダッシュボードですべてのユーザー ID を使用して、ユーザーの検索および識別ができます。Braze ダッシュボードでダッシュボードを検索する方法については、「[テストユーザーの追加]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users)」を参照してください。

{% alert important %}
Brazeは、5,000,000セッションを超えるユーザー（「ダミーユーザー」）を禁止またはブロックし、これらのユーザーは一般的に誤統合の結果であるため、SDKイベントを取り込まなくなる。正当なユーザーにこのような事態が発生した場合は、Brazeアカウントマネージャーに連絡すること。
{% endalert %}