---
nav_title: カスタムデータの管理
article_title: カスタムデータの管理
page_order: 20
page_type: reference
description: "このリファレンス記事では、キャンペーンやセグメントへの事前入力、禁止リストへのデータの追加、データの削除など、カスタムデータの管理方法について説明します。"
---

# カスタムデータの管理

> このページでは、キャンペーンとセグメントにカスタムデータを事前に入力する方法、役に立たなくなったデータをブロックリストする方法、およびカスタムイベントと属性とプロパティを管理する方法について説明します。<br><br>特にカスタム属性を管理する方法については、[カスタム属性の管理]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes)を参照してください。

## カスタムデータの事前入力

開発チームがカスタムデータを統合する前に、そのカスタムデータを使用してキャンペーンやセグメントを設定したい場合があります。Braze では、カスタムイベントやカスタム属性のデータの追跡を開始する前に、ダッシュボードにそれらのデータを事前入力できるため、これらのイベントや属性をドロップダウンやキャンペーン作成プロセスの一部として使用できます。

カスタムイベントとカスタム属性を事前入力するには次の手順に従います。

1. [**データ設定**] > [**カスタムイベント**] または [**カスタム属性**] または [**製品**] に移動します。

![[カスタム属性]、[カスタムイベント] または [製品] に移動します。][21]{: style="max-width:90%;" }

{: start="2"}
2\.カスタム属性、カスタムイベント、または製品を追加するには、それぞれのページに移動して、[**カスタム属性を追加**]、[**カスタムイベントを追加**]、または [**製品を追加**] を選択します。<br><br>カスタム属性の場合は、この属性の[データ型][20] (ブール型、文字列など) を選択します。属性のデータ型によって、その属性に使用できるセグメンテーションフィルターが決まります。<br><br>![新しい属性またはイベントの追加][22]{: style="max-width:80%;" }
3\.[**保存**] を選択します。

### カスタムイベントとカスタム属性の命名

カスタムイベントとカスタム属性では大文字小文字が区別されます。開発チームが後でこれらのカスタムイベントやカスタム属性を統合するときには、この点に留意してください。開発チームがカスタムイベントやカスタム属性に付ける名前は、ここで付けた名前とまったく同じでなければなりません。異なる場合、Braze により別のカスタムイベントやカスタム属性が生成されます。

## プロパティの管理

カスタムイベントまたは製品を作成した後、そのイベントまたは製品の [**プロパティの管理**] を選択して、新しいプロパティの追加、禁止リストへの既存のプロパティの追加、および[トリガーイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)でこのプロパティを使用するキャンペーンまたはキャンバスの表示ができます。

![カスタムイベントのカスタムプロパティ。][73]{: style="max-width:80%"}

これらの追加されたカスタム属性、カスタムイベント、製品、またはカスタムイベントプロパティを追跡可能にするには、以前の追加時に使用した正確な名前を使用して SDK でそれらを作成するように、開発チームに依頼する必要があります。または、Braze [API]({{site.baseurl}}/api/basics/) を使用してその属性のデータをインポートすることもできます。その後、カスタム属性、カスタムイベントなどのアクションが可能になり、ユーザーに適用されます。

{% alert note %}
ユーザープロファイルのすべてのデータ (カスタムイベント、カスタム属性、カスタムデータ) は、ユーザープロファイルがアクティブである限り保存されます。
{% endalert %}

## 禁止リストへのカスタムデータの追加

たまに、カスタム属性、カスタムイベント、購入イベントについて、データポイントの消費量が多いもの、マーケティング戦略に不要になったもの、または誤って記録されたものが見つかることがあります。 

開発チームがアプリや Web サイトのバックエンドからこのデータを削除する作業をしている間、このデータが Braze に送信されないようにするために、カスタムデータオブジェクトを禁止リストに入れておくことができます。禁止リストにカスタムデータオブジェクトを追加すると、そのデータが Braze に記録されなくなります。つまり、特定ユーザーを検索するときにそのデータが表示されなくなります。

{% alert important %}
カスタムデータをブロックリストするには、キャンペーン、キャンバス、およびセグメントにアクセスして編集するための[ユーザ権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) が必要です。
{% endalert %}

禁止リストに追加されたデータは SDK から送信されず、Braze ダッシュボードは、禁止リストに追加済みであれば、他のソース (API など) からのデータを処理しません。ただし、禁止リストを使用しても、ユーザープロファイルからデータが削除されたり、そのカスタムデータオブジェクトで生じたデータポイントの量が遡及的に減少したりすることはありません。

### 禁止リストへのカスタム属性、カスタムイベント、製品の追加

{% alert important %}
イベントや属性を禁止リストに追加すると、そのイベントや属性を使用しているセグメント、キャンペーン、またはキャンバスがアーカイブされます。
{% endalert %}

特定のカスタム属性、カスタムイベント、または製品の追跡を停止するには、次のステップに従います。

1. [**カスタム属性**]、[**カスタムイベント**] または [**製品**] のページで追跡を停止するものを検索します。
2. カスタム属性、カスタムイベント、または製品を選択します。カスタム属性とカスタムイベントについては、一度に100個まで選択してブロックリストに追加できます。
3. [**禁止リスト**] をクリックします。

![[カスタム属性] ページで選択され、禁止リストに追加された複数のカスタム属性。]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

禁止リストには、最大で 300 個のカスタム属性と 300 個のカスタムイベントを追加できます。特定のデバイス属性の収集を停止する方法については、[SDKガイド][88]を参照してください。

カスタムイベントやカスタム属性を禁止リストに追加すると、以下のことが適用されます。

- Brazeに送信されたデータは処理されず、ブロックリストされたイベントおよび属性はデータポイントsとしてカウントされなくなります
- 再びアクティブにしない限り、既存のデータは利用できません。
- 禁止リストに追加したイベントや属性は、フィルターやグラフに表示されません。
- アクティブなキャンバスの下書き内で禁止リストに追加済みのデータを参照すると、無効な値として読み込まれ、エラーの発生する可能性があります。
- 禁止リストにあるイベントや属性を使用したものはすべてアーカイブされます。

これを実現するために、Braze は禁止リスト情報を各デバイスに送信します。膨大な数のイベントや属性 (数十万、数百万に及ぶ) を禁止リストに追加することを考えた場合、これはデータ集約的な操作になるため重要です。

### 禁止リストの考慮事項

多数のイベントと属性をブロックリストに含めることは可能ですが、推奨されません。イベントが実行されたり、属性が Braze に送信される (可能性がある) たびに、このイベントや属性を禁止リスト全体と照合しなければならないためです。

最大300個の項目がSDKに送信され、ブロックリストに登録されます。300を超える項目をブロックリストに登録すると、このデータはSDKから送信されます。今後、イベントまたは属性を使用する必要がない場合は、次回のリリースでアプリコードから削除することを検討してください。禁止リストの変更が伝播するまで数分かかることがあります。任意のブロックリストイベントまたは属性をいつでも再度有効にできます。

## カスタムデータの削除

ターゲットを絞ったキャンペーンやセグメントを構築していくうちに、カスタムイベントやカスタム属性が不要になるかもしれない。たとえば、1 回限りのキャンペーンの一部として特定のカスタム属性を使用した場合、[blocklisting it](#blocklisting-custom-attributes-custom-events-and-products) の後でこのデータを削除し、その参照をアプリから削除できます。任意のデータ型(文字列、数値、ネストされたカスタム属性など)を削除できます。

{% alert important %}
カスタムデータを削除するには、[Braze 管理者]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)である必要があります。
{% endalert %}

カスタムイベントやカスタム属性を削除するには、以下のようにする：

1. 削除するデータのタイプに応じて、[**データ設定**] > [**カスタム属性**] または [**カスタムイベント**] に移動します。
2. カスタムデータに移動して <i class="fa-solid fa-ellipsis-vertical"></i> ［**アクション**] > ［**禁止リスト**] を選択します。
3. カスタムデータが禁止リストに登録されてから7日間経過したら、<i class="fa-solid fa-ellipsis-vertical"></i> ［**アクション**] > ［**削除**] を選択します。

### 削除の仕組み

カスタムデータを削除すると、以下のようになります。 

- **カスタム属性の場合:**すべてのユーザープロファイルから属性データを永久に削除する。
- **カスタムイベントの場合：**すべてのユーザープロファイルからイベントメタデータを永久に削除する。

属性またはイベントが削除対象として選択されると、そのステータスが [**削除済み**] に変更されます。その後7日間は、属性またはイベントを復元できます。7日後に復元しなければ、データは永久に削除されます。属性やイベントをリストアすると、ブロックリストの状態に設定される。

削除してもユーザープロファイルにカスタム・データ・オブジェクトが追加で記録されることは防げないため、イベントや属性を削除する前に、カスタム・データが記録されなくなったことを確認すること。

### 知っておくべきこと

カスタムデータを削除する場合は、次の点に注意してください。

* **削除は完全に実施されます**。データは復元できません。
* データはBrazeプラットフォームとユーザープロファイルから削除される。
* 削除したカスタム属性名やカスタムイベント名は「再利用」できる。つまり、削除後に Braze でカスタムデータが「再表示」された場合、これは統合が停止しておらず、同じカスタムデータ名でデータを送信し続けていることが原因で発生している可能性があります。
* 削除した結果、カスタムデータが再び表示される場合、アイテムを禁止リストに登録する必要があることがあります。カスタムデータが削除されるため、禁止リスト登録ステータスは維持されません。
* カスタムデータを削除しても、[データポイント]({{site.baseurl}}/user_guide/data/data_points)は消費されず、使用する新しいデータポイントも生成されません。

## データ型の比較の強制

Braze は、受信した属性データのデータ型を自動的に認識します。しかし、イベントで 1 つの属性に複数のデータ型が適用されている場合、任意の属性にデータ型を強制することで、その属性の実体がわかります。**Data Type**欄のドロップダウンから選択する。

{% alert note %}
データ型の強制は、イベントプロパティや購入プロパティには適用されない。
{% endalert %}

![カスタム属性のデータタイプ・ドロップダウン][75]

{% alert warning %}
属性のデータ型を強制することを選択した場合、指定された型ではないデータがその型に強制的に取り込まれます。そのような強制が不可能な場合(例えば、数字に強制される文字を含む文字列)、データは無視されます。型の変更前に取り込まれたデータは、古い型として引き続き保存され(したがって、セグメント化できない場合があります)、影響を受けるユーザのプロファイルの属性の横に警告が表示されます。
{% endalert %}

### データ型の強制

| 強制データ型 | 説明 |
|------------------|-------------|
| ブール値 | `1`、`true`、`t` (大文字小文字は区別されない) の入力は、`true` として保存されます |
| ブール値 | `0`、`false`、`f` (大文字小文字は区別されない) の入力は、`false` として保存されます |
| 数値 | 整数または浮動小数点数(`1`、`1.5` など) は数値として保存されます |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

さまざまなデータ型の比較によって公開される特定のフィルターオプションの詳細については、[レポートの設定][43]] を参照してください。また、利用可能な他のデータ型の詳細については、「カスタム属性のデータ型」][44]を参照してください。

{% alert note %}
Braze に送信されたデータは不変であり、受信後の削除または変更ができません。ただし、ダッシュボードで追跡しているものをコントロールするために、前のセクションに挙げたステップのいずれかを使用できます。
{% endalert %}


[1]: {% image_buster/assets/img_archive/blocklist_warning.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[21]: {% image_buster /assets/img_archive/prepopulate_page.png %}
[22]: {% image_buster /assets/img_archive/prepopulate_add.png %}
[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[73]: {% image_buster /assets/img_archive/manageproperties1.png %}
[75]: {% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %}
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection
