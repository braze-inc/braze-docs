---
nav_title: ユーザープロファイルのライフサイクル
article_title: ユーザープロファイルのライフサイクル
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze のユーザープロファイルのライフサイクルと、ユーザープロファイルを識別して参照するさまざまな方法について説明します。"

---

# ユーザープロファイルのライフサイクル

> この記事では、Braze のユーザープロファイルのライフサイクルと、ユーザープロファイルを識別して参照するさまざまな方法について説明します。カスタマーライフサイクルをより詳しく理解したい場合は、[ユーザーライフサイクルのマッピング](https://learning.braze.com/mapping-customer-lifecycles)に関する Braze ラーニングコースをご覧ください。

ユーザーに関連付けられるすべての永続データは、そのユーザープロファイルに保存されます。

ユーザープロファイルが作成された後 (ユーザーが SDK によって認識されたか、API を介して作成された後)、そのユーザーを識別して参照する目的で多数のパラメーターをユーザープロファイルに割り当てることができます。 

これらのパラメーターには以下のものが含まれます。

* `braze_id`
* `external_id`
* 設定した任意の数のカスタムユーザーエイリアス

## 匿名ユーザープロファイル

`external_id` が指定されていないユーザーは匿名ユーザーと呼ばれます。例えば、Web サイトを表示したがモバイルアプリのサインアップやダウンロードを行っておらず、プロファイルを作成していないユーザーなどです。

最初に、SDK を介してユーザーが認識されると、匿名ユーザープロファイルが作成され、Braze によって設定された一意の識別子 `braze_id` が関連付けられます。この識別子を使用して、[API]({{site.baseurl}}/api/endpoints/user_data/) を介してそのユーザープロファイルを更新できます。

`braze_id` は Braze によって自動的に割り当てられ、編集できません。また、デバイスによって異なります。

## 識別されたユーザープロファイル

ユーザーがユーザー ID またはメールアドレスを入力することにより、アプリでそのユーザーが認識されたら、`changeUser` メソッド([Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69), [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/appboy/Appboy.html#changeUser-java.lang.String-)) を使用してそのユーザープロファイルに `external_id` を割り当てることをお勧めします。`external_id` により、複数のデバイスで同じユーザープロファイルを識別できます。 

`external_id` を使用すると、さらに次のような利点があります。 

- 複数のデバイスやプラットフォームにわたって一貫したユーザーエクスペリエンスを提供できます (例えば、iPhone アプリの忠実なユーザーの Android タブレットには、離脱ユーザー向けの通知を送信しない)。
- ユーザーがアプリをアンインストールして再インストールするたびに、または別のデバイスにアプリをインストールするたびに、新しいユーザープロファイルが作成されていないことを確認して、分析の精度を向上できます。
- [ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/user_data/)を使用して、アプリ外のソースからユーザーデータをインポートできるようになり、また[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)を使用して、トランザクションメッセージのターゲットユーザーを設定できるようになります。
- セグメンター内で「テスト」[フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)を使用して、また [[ユーザー検索]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/)] ページで、個々のユーザーを検索できます。

{% alert warning %}
ユーザーを一意に識別できるようになるまで、ユーザープロファイルに `external_id` を割り当てないでください。ユーザーを識別した後、匿名ユーザーに戻すことはできません。
<br><br>
さらに、`external_id` は、ユーザープロファイルに設定した後に変更することができません。あるユーザーのセッション中に異なる `external_id` を設定しようとすると、新規のユーザープロファイルが作成され、新しい `external_id` が関連付けられます。2 つのプロファイル間でデータは渡されません。
{% endalert %} 

匿名ユーザーを識別する場合、次の 2 つのシナリオがあります。

1) **匿名ユーザーが、識別された新規ユーザーになる:**<br>`external_id` が Braze にまだ存在しない場合、匿名ユーザーは識別された新規ユーザーになり、その匿名ユーザーと同じ属性と履歴をすべて保持します。 

2) **匿名ユーザーが、既存のユーザーとして識別される:**<br>`external_id` が Braze に既に存在する場合、このユーザーは以前、タブレットなどの別のデバイスやインポートされたユーザーデータなどを介して、何らかの方法でシステム内のユーザーとして識別されています。 

したがって、このユーザーのユーザープロファイルは既に作成されています。この場合、Braze は次のことを行います。
1. 匿名ユーザーを孤立させます
2. 匿名プロファイルから、識別されたユーザープロファイルにまだ存在しない[特定のユーザープロファイルのフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)をマージします
3. ユーザー数が増えないように、その匿名プロファイルをユーザー群から削除します

ある匿名ユーザーが名を持ち、既知のユーザーにも名が設定されている場合、ターゲットの名が保持されます。ターゲットユーザーが NULL 値を持ち、匿名ユーザーが値を持つ場合、これらの[特定のユーザープロファイルのフィールド]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)に該当すれば、その値がターゲットユーザーにマージされます。

ユーザープロファイルに `external_id` を設定する方法については、弊社のドキュメント ([iOS][24]、[Android][30]、[Web][31]) を参照してください。

## ユーザーのエイリアス

Braze の `external_id` 以外の識別子でユーザーを参照するには、ユーザープロファイルにユーザーエイリアスを設定します。ユーザープロファイルに設定されたエイリアスは、ユーザーの `braze_id` または`external_id` を置き換えるのではなく、それらに加えて作用します。ユーザープロファイルに設定できるエイリアスの数に制限はありません。

各エイリアスは、2 つの部分 (エイリアスのキーを定義する `alias_label` と、値を定義する `alias_name`) で構成されるキーと値のペアとして機能します。1 つのラベルの `alias_name` は、ユーザー群全体で一意でなければなりません (`external_id` と同様)。既存のラベルと名前の組み合わせを使用して 2 番目のユーザープロファイルを更新しようとしても、ユーザープロファイルは更新されません。

`external_id` とは異なり、エイリアスは、[ユーザーデータエンドポイント][32] を使用するか、SDK を使用して新規の名前を渡すことで、指定したラベルの新規の名前に更新できます。これにより、そのユーザーデータをエクスポートするときに、ユーザーエイリアスが表示されます。

![同じユーザーエイリアスラベルを持つが、異なるエイリアス名を持つユーザーの 2 つの異なるユーザープロファイル][29]

ユーザーエイリアスを使用すると、匿名ユーザーに識別子のタグを付けることもできます。例えば、あるユーザーが e コマースサイトでメールアドレスを提供していてもまだサインアップしていない場合、そのメールアドレスをその匿名ユーザーのエイリアスとして使用できます。このようなユーザーは、エイリアスを使用してエクスポートしたり、API で参照したりできます。

エイリアスを持つ、ある匿名ユーザープロファイルが後で `external_id` で認識された場合、それらは通常の識別されたユーザープロファイルとして扱われます。ただし、既存のエイリアスは保持され、そのエイリアスによって参照できます。

ユーザーエイリアスを既知のユーザープロファイルに設定して、別の外部の既知の ID によって既知のユーザーを参照することもできます。たとえば、Braze 内で参照しようとするビジネスインテリジェンスツール ID (Amplitude の ID など) をユーザーが持っている場合があります。

ユーザーエイリアスの設定方法については、各プラットフォーム ([iOS][1]、[Android][2]、[Web][3]) に関する弊社のドキュメントを参照してください。

![Braze でのユーザープロファイルのライフサイクルのフローチャート。匿名ユーザーについて changeUser () が呼び出されると、そのユーザーは識別されたユーザーになり、そのデータは識別されたユーザープロファイルに移行されます。識別されたユーザーは Braze ID と external ID を持ちます。この時点で、2 人目の匿名ユーザーに changeUser() を呼び出すと、その識別されたユーザーにまだ存在しないユーザーデータのフィールドがマージされます。識別されたユーザーの既存のユーザープロファイルにエイリアスが追加されている場合、データは影響を受けませんが、エイリアスを持つ識別ユーザーになります。識別されたユーザーと同じエイリアスラベルを持つが、別のエイリアス名を持つ 3 人目の匿名ユーザーについて changeUser () を呼び出すと、識別されたユーザーに存在しないフィールドがすべてマージされ、識別されたユーザープロファイルのエイリアスラベルは維持されます。][26]

{% alert tip %}
顧客のユーザープロファイルライフサイクルで、このプロセスがどのように行われるかを想像しにくい場合は、ユーザーデータ収集の[ベストプラクティス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/)を参照してください。
{% endalert %}

## 高度なユースケース情報

当社の SDK および APIを 介して [ユーザーデータエンドポイント][27] を使用すると、既存の識別済みユーザープロファイルに新規のユーザーエイリアスを設定できます。ただし、既存の未知のユーザープロファイルには、API を使用してユーザーエイリアスを設定することはできません。

一致するエイリアス名を共有するが異なるラベルを持つ匿名ユーザープロファイルに既存の `external_id` を設定しようとすると、既存の既知のユーザープロファイルのエイリアスラベルのみが保持されます。

ユーザーがアプリをアンインストールして再インストールすると、そのユーザーについて新規の匿名 `braze_id` が生成されます。

### ユーザー ID に関するトラブルシューティング方法

テストとして、ダッシュボードですべてのユーザー ID を使用して、ユーザーの検索および識別ができます。Braze ダッシュボードでダッシュボードを検索する方法については、[テストユーザーの追加][28]を参照してください。

{% alert important %}
Brazeは、セッション数が 500 万を超えるユーザー (「ダミーユーザー」) の禁止またはブロックを行い、SDK イベントの取り込みを停止します。これは通常、誤った連携の結果であるためです。正規ユーザーに対して禁止またはブロックが発生しているとわかった場合は、Braze アカウントマネージャーに連絡してください。
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users

[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id
[24]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/
[25]: {{site.baseurl}}/developer_guide/home/
[26]: {% image_buster /assets/img_archive/Braze_User_flowchart.png %}
[27]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
[28]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[29]: {% image_buster /assets/img_archive/Braze_User_aliases.png %}
[30]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[31]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[32]: {{site.baseurl}}/developer_guide/rest_api/user_data/#new-user-alias-endpoint
