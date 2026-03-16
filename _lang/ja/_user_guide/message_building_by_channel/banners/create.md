---
nav_title: バナーを作成する
article_title: バナーを作成する
page_order: 1
description: "この参考記事では、Brazeのキャンペーンとキャンバスを使ってバナーを作成、作成、設定、送信する方法について説明する。"
tool:
  - Campaigns
channel:
  - banners
---

# バナーを作成する

> Brazeでキャンペーンやキャンバスを作成する際に、バナーの作り方を学習しよう。一般的な情報については、[バナーについて]({{site.baseurl}}/user_guide/message_building_by_channel/banners)を参照してください。

{% alert important %}
キャンバスでのバナーメッセージ作成機能は、現在早期アクセス中だ。この早期アクセスへ参加することに興味がある場合は、カスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

バナーを配信する前に、開発チームが[アプリやWeb サイトに広告枠を設定]({{site.baseurl}}/developer_guide/banners/creating_placements/)しなければならない。バナーキャンペーンの下書き作成は引き続き行えるが、掲載枠の設定が完了するまでキャンペーンを開始することはできない。

## バナーメッセージを作成する

{% multi_lang_include banners/creating_placements.md section="user" %}

### ステップ 2:メッセージを作成する場所を選択する

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のターゲットを絞ったメッセージングキャンペーンに適している。一方、キャンバスは複数ステップのユーザーージャーニーに適している。

{% tabs %}
{% tab Campaign %}

1. [**メッセージング**] > [**キャンペーン**] の順に進み、[**キャンペーンを作成**] を選択します。
2. [**バナー**] を選択します。
3. キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて[チームや]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) [タグを]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)追加します。タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。たとえばレポートビルダーを使用する場合、関連するタグでフィルタリングできます。
5. 以前に登録した配置を選択して、キャンペーンに関連付けます。
6. 必要に応じてバリアントを追加します。それぞれ異なるメッセージタイプとレイアウトを選択できます。バリアントの詳細については、[多変量およびA/B 検定]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing)を参照してください。
7. バナーキャンペーンの開始日時を選択します。デフォルトでは、バナーは無期限に存続します。これを変更するには、[**終了時刻**] を選択し、終了日時を指定します。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、**Copy from Variant** を**Add Variant** ドロップダウンから選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. キャンバス作成ツールを使用して [[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーでメッセージステップを追加します。ステップに、明確で意味のある名前を付けます。
3. **バナーを**メッセージングチャネルとして選択せよ。
4. バナーの配置場所を選択せよ。
5. バナーの優先度を設定する。[バナー優先度]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority)により、複数のバナーが同じ配置を共有する場合に表示される順序が決まります。
6. バナーの有効期限を設定する。これは、そのステップが利用可能になってから一定期間後、あるいは特定の日時に設定できる。

{% endtab %}
{% endtabs %}

### ステップ 3:バナーを作成する {#compose-a-banner}

バナーを作成するには、以下の方法がある：

- 白紙のテンプレートから始める。
- Brazeバナーテンプレートを使用する
- 保存したバナーテンプレートを選択する

![空白のバナーまたはテンプレートを選択するオプション。]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### ステップ 3.1:バナーのスタイル設定

ブロックと行をキャンバス領域にドラッグアンドドロップして、メッセージの作成を開始できます。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

メッセージの背景プロパティ、ボーダー設定などをカスタマイズするには、**Styles** を選択します。特定のブロックまたは行のスタイルのみをカスタマイズする場合は、それを選択して変更します。

![バナー作成画面の [スタイル] パネル。]({% image_buster /assets/img/banners/banner_card_styles.png %})()

#### ステップ 3.2:クリック時の動作を定義する（オプション）

ユーザーがバナー内のリンクをクリックしたときに、アプリのさらに内部へ誘導するか、別の Web ページにリダイレクトするかを選択できます。さらに、[カスタム属性やイベントをログに記録]({{site.baseurl}}/developer_guide/analytics/)する選択も可能だ。これにより、ユーザーがバナーをクリックした際に、カスタムデータでユーザープロファイルが更新される。

{% alert important %}
{::nomarkdown}
「バナー」のボタン、リンク、イメージなどの特定のエレメントがクリック時に独自のビヘイビアを持つ場合、クリック時のビヘイビアを上書きできます。たとえば、以下のクリック時の動作があるとします。<br><ul><li>バナーには、ウェブサイトのホームページにリダイレクトするオンクリック動作があります。</li><li>バナーのイメージには、ウェブサイトの製品ページにリダイレクトするオンクリック動作があります。</li></ul>ユーザーが画像をクリックすると、商品ページにリダイレクトされる。しかし、バナーの周囲をクリックすると、ホームページにリダイレクトされる。
{:/}
{% endalert %}

#### ステップ3.3：カスタムプロパティを追加する（任意） {#custom-properties}

バナーにカスタムプロパティを追加して、文字列やJSONオブジェクトなどの構造化されたメタデータを添付できる。これらのプロパティはバナーの表示方法には影響しないが、[Braze SDKを通じてアクセス]({{site.baseurl}}/developer_guide/banners/placements/)可能であり、アプリの動作や外観を変更するために利用できる。例えば、次のようなことができる：

- サードパーティの分析ツールや連携サービス向けにメタデータを送信する。
- メタデータ（例：JSON`timestamp`オブジェクト）を使って条件分岐ロジックをトリガーする。
- バナーの動作を、含まれるメタデータ（例：`ratio`や）に基づいてコントロール`format`する。

カスタムプロパティを追加するには、**設定**＞**プロパティ**＞**プロパティの追加**を選択する。

![バナーキャンペーンに最初のカスタムプロパティを追加するオプションを表示するプロパティページ。]({% image_buster /assets/img/banners/add_property.png %})

追加したい各プロパティについて、以下の項目を記入する：

| フィールド | 説明 | 例 |
|-------|-------------|---------|
| プロパティタイプ | プロパティのデータ型。サポートされている型には、文字列、ブール値、数値、タイムスタンプ、画像URL、およびJSONオブジェクトが含まれる。 | string |
| プロパティキー | プロパティの固有識別子。このキーはSDKでプロパティにアクセスするために使用される。 | `color` |
| 値 | プロパティに割り当てられた値。選択したプロパティタイプと一致しなければならない。 | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

[**完了**] を選択します。

![プロパティページには、キーがcolorで値が#FF0000.の文字列プロパティがある。]({% image_buster /assets/img/banners/example_property.png %})

### ステップ 4: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab Campaign %}

#### バナー優先度の設定(オプション)

[バナー優先度]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority)により、複数のバナーが同じ配置を共有する場合に表示される順序が決まります。優先度を手動で設定するには、次のようにします。

1. [**正確な優先度を設定**] を選択します。
2. キャンペーンをドラッグアンドドロップして、正しい優先順位でキャンペーンを順序付けします。
3. [**並べ替えを適用**] を選択します。

{% alert tip %}
同じ配置ID を使用する複数のBanner キャンペーンがある場合は、ドラッグアンドドロップの優先順位ソーターを使用して正確な優先順位を定義することをお勧めします。
{% endalert %}

#### オーディエンスを選ぶ

1. **ターゲットオーディエンス**では、セグメントやフィルターを選択してオーディエンスを絞り込む。おおよそのセグメント人口のプレビューが自動的に表示される。メッセージが送信される前に、正確なセグメントの所属が計算される。

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\.**アサインコンバージョン**では、キャンペーン受信後のユーザーアクションを追跡する。コンバージョンイベントを定義し、最大30日間の期間を設定できる。

{% multi_lang_include target_audiences.md %}

#### コンバージョンイベントを選択する

Brazeは、キャンペーン受信後のユーザーの[コンバージョンイベントや]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)、特定のアクションを実行する頻度をトラッキングできる。ユーザーが指定されたアクションを取った場合、コンバージョンがカウントされる期間を最大30日間まで設定できる。

{% endtab %}

{% tab Canvas %}

キャンバスコンポーネントが完成していない場合は、残りのセクションを完成させます。キャンバスの残りの部分の構築方法の詳細については、[多変量検定]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)と[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)を実装してください。その他については、キャンバスのドキュメントの[キャンバスの構築]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

### ステップ 5: メッセージをテストします(オプション)

{% multi_lang_include banners/testing.md page="campaigns" %}

### ステップ 6:レビューと展開

キャンペーンやキャンバスの作成が終わったら、詳細を確認し、[テストしてから]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/)、準備が整ったら送信するんだ。
