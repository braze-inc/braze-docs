---
nav_title: ワークスペースの作成と管理
article_title: ワークスペースの作成と管理
page_order: 0
page_type: reference
description: "この記事では、ワークスペースの作成、設定、および管理を行う方法について説明します。"

---

# ワークスペースの作成と管理

> この記事では、ワークスペースの作成、設定、および管理を行う方法について説明します。 

## ワークスペースとは

Braze での操作はすべて、ワークスペース内で行われます。ワークスペースとは、関連するモバイルアプリや Web サイトのエンゲージメントの追跡および管理を行うための共有環境です。ワークスペースは、同じアプリ、またはよく似たアプリ (モバイルアプリの Android 版と iOS 版など) のグループです。 

## ワークスペースの作成

### ステップ 1: 計画の立案

始める前に、チームや Braze のオンボーディングマネージャーと協力して、ユースケースに最適なワークスペース構成を決定する必要があります。Braze でのワークスペース計画の詳細については、[開始;ワークスペース][link] ガイド。

### ステップ 2: ワークスペースの追加

グローバルヘッダーのワークスペースのドロップダウンから、新しいワークスペースを作成したり、既存のワークスペース間で切り替えたりできます。

1. ワークスペースのドロップダウンを選択し、<i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> [**ワークスペースを作成**] を選択します。

![ワークスペース・ドロップダウンに「ワークスペースを作成」ボタンがある。][1]{: style="max-width:60%;"}

{:start="2"}
2\.ワークスペースに名前を付けます。

{% alert tip %}
社内の他のユーザーがこのワークスペースを簡単に見つけられるように、命名規則を採用することをお勧めします。以下に例を示します。「Upon Voyage US - Production」と「On Voyage US - Staging」です。
{% endalert %}

{:start="3"}
3\.[**作成**] を選択します。Braze が ワークスペースを作成するまで数秒かかることがあります。

![「Upon Voyage US-Staging」という名前の「ワークスペースの作成」モーダル。][2]{: style="max-width:60%" }

アプリインスタンスの追加を開始するための [**アプリ設定**] ページが表示されます。このページには、[**設定**] > [**アプリ設定**] からいつでもアクセスできます。

![アプリを追加するためのボタンがある Upon Voyage US-Staging ワークスペースの [アプリ設定] ページ。][3]

### ステップ 3: アプリインスタンスの追加

ワークスペース内に収集したさまざまなサイトやアプリを「アプリインスタンス」と呼びます。

1. [**アプリ設定**] ページで、[**\+ アプリを追加**] を選択します。
2. アプリインスタンスに名前を付けて、配置先のプラットフォームを 1 つ以上選択します。複数のプラットフォームを選択した場合、Braze はプラットフォームごとにアプリインスタンスを 1 つ作成します。

![「Add New App to Upon Voyage US - Staging" モーダルでアプリの詳細を選択できる。][4]{: style="max-width:60%" }

{:start="3"}
3\.[**アプリを追加**] を選択して確定します。

#### アプリの API キー

アプリインスタンスを追加したら、その API キーにアクセスできます。API キーは、アプリインスタンスと Braze API の間でリクエストを行う際に使用されます。API キーは、Braze SDK とお客様のアプリや Web サイトとの連携にも重要です。

![API キーと SDK エンドポイントのフィールドがある Upon Voyage iOS アプリの設定ページ。][5]

{% alert note %}
各プラットフォームでアプリのバージョンごとに個別のアプリインスタンスを作成する必要があります。例えば、iOS と Android の両方に無料版とプロ版のアプリがある場合は、ワークスペース内に 4 つのアプリインスタンス (無料版 iOS アプリ、無料版 Android アプリ、プロ版 iOS アプリ、プロ版 Android アプリ) を作成します。これにより、アプリインスタンスごとに 1 つずつ、使用する API キーが 4 つ得られます。
{% endalert %}

#### ライブ SDK バージョン

特定アプリの [アプリ設定] ページに表示される [ライブ SDK バージョン] は、1 日の総セッション数の 5% を占める最高のアプリバージョンであり、過去 1 日で少なくとも 500 件のセッションがあります。

このフィールドは、Braze SDK とアプリまたは Web サイトを連携した後に表示されます。新しいバージョンの Braze SDK がプラットフォームで利用可能の場合、「新しいバージョンが利用可能」というタグとともにここに表示されます。

![フィールド値が「5.4.0」で、新しいバージョンが利用可能であることを示すアイコンが表示された「Live SDK バージョン」セクション。][6]

### ステップ 4: 必要に応じて繰り返し

ステップ 2 と 3 を繰り返して、計画に必要な数のワークスペースを設定します。ベストプラクティスとして、連携とキャンペーンのテスト向けにテスト用ワークスペースを作成することをお勧めします。

{% alert tip %}
**テスト用ワークスペースの追加**<br>生産インスタンスから特定のユーザーを完全にサンドボックス化して、アプリのテストを実行できます。新しいワークスペースを作成し、アプリケーションを公開するときに、Braze の使用する API キーを、テスト用ワークスペースではなく、必ず生産ワークスペースの API キーと一致するように変更してください。
{% endalert %}

## ワークスペースの管理

### お気に入りの追加

お気に入りのワークスペースを追加すると、最も頻繁に使用するワークスペースに、より迅速にアクセスできます。

![ワークスペース・ドロップダウンに「お気に入りワークスペース」のタブがある。][7]{: style="max-width:50%;"}

お気に入りのワークスペースを追加するには、次の手順に従います。

1. プロファイルドロップダウンを選択し、**アカウントを管理**を選択します。
2. [**アカウントプロフィール**] セクションで、[**お気に入りのワークスペース**] フィールドを見つけます。
3. リストからワークスペースを選択します。
4. **変更の保存**を選択します。

お気に入りにするワークスペースの数に制限はありませんが、便宜上、このリストを短くしておくことをお勧めします。

### ワークスペース名の変更

ワークスペース名を変更するには、次の手順に従います。

1. [**設定**] > [**アプリ設定**] に移動します。
2. ワークスペースの名前にマウスポインタを置き、<i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i> を選択します。
3. ワークスペースに新しい名前を付け、<i class="fa-solid fa-square-check" style="color: #0b8294;"></i>**保存**を選択します。

![ワークスペース名の横に現れる鉛筆のアイコン。][8]{: style="max-width:50%;"}

### ワークスペースとアプリインスタンスを削除する

ワークスペースまたはアプリインスタンスを削除する：

1. [**設定**] > [**アプリ設定**] に移動します。
2. それぞれのワークスペースを削除するには、**「ワークスペースを削除**」を選択するか、それぞれのアプリインスタンスの横にあるゴミ箱アイコンを選択する。

現在ユーザーをターゲットとして使用しているアプリインスタンスやワークスペース、または1,000人以上のユーザーを持つアプリインスタンスやワークスペースは削除できない。そうしようとすると、エラーメッセージが表示される。続けて削除するには、ダッシュボードのリンクと削除するアプリインスタンスまたはワークスペース名を含む[サポートケースを作成する]({{site.baseurl}}/user_guide/administrative/access_braze/support/)。

{% alert warning %}
ワークスペースを削除する際には注意してください。ワークスペースは、削除すると復元できません。
{% endalert %}

![ワークスペースを削除するボタンと、アプリを削除するゴミ箱アイコンがあるアプリ設定ページ。][9]

## よくある質問

### 更新したアプリをリリースするときに、新しいワークスペースを作成したほうがよいですか?

ユーザーがアプリを更新するだけで済み、アプリストアにまったく新規のアプリをリリースしない場合、旧バージョンのユーザーにメッセージを送信する予定がなければ、新しいワークスペースを作成しないでください。

旧バージョンのアプリの履歴データとユーザープロファイルはすべて、作成した新しいワークスペースに引き継がれません。したがって、既存のユーザーが新しいアプリのバージョンにアップグレードすると、古いアプリの行動データが一切含まれない新しいプロファイルが作成されます。

さらに、ユーザーは古いワークスペースと新しいワークスペースの 2 か所に存在することになります。また、同じプッシュトークンを持つ可能性もあります。したがって、古いワークスペースユーザーのみを対象にしたマーケティングメッセージが、既にアップグレード済みのユーザーにも送信される可能性があります。

#### どのような代替方法がありますか?

古いアプリと新しいアプリを分離するには、同じワークスペース内に新規のアプリインスタンスを作成します。これにより、セグメンテーションの際にそのアプリを選択すれば、新バージョンのユーザーを効果的にターゲットにできます。旧バージョンを使用しているユーザーにメッセージを送信する場合は、フィルターを使用して[旧バージョンのアプリをターゲットにする]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions)ことができます。

### 1 つのワークスペースに複数のアプリインスタンスがあります。メッセージで 1 つのアプリのみをターゲットにしていることは、どのようにして確認できますか?{#singular-app}

メッセージのターゲットが特定のアプリのみであることを確認するには、選択したアプリインスタンスのユーザーのみをターゲットにするセグメントを追加します。これは特に、ユーザーが同じワークスペース内の異なるアプリインスタンスに対して 2 つのプッシュトークンを持つ可能性がある場合に重要です。このシナリオでは、ユーザーが現在使用しているアプリとは別のアプリの通知を受信する可能性があります。これは理想的なエクスペリエンスではありません。

セグメントのデフォルトのターゲットは、ワークスペース内のすべてのアプリと Web サイトです。1 つのアプリや Web サイトのみをターゲットにするセグメントを設定するには、次の手順に従います。

1. セグメントを作成し、わかりやすい名前を付けます。Braze では、「すべてのユーザー (({Name} {Platform}))」という形式を使用しています。例は、「すべてのユーザー (Upon Voyage iOS)」です。
2. [**ターゲットに設定されたアプリと Web サイト**] で、[**特定のアプリのユーザー**] を選択します。
3. [**特定のアプリ**] ドロップダウンで、アプリまたはサイトを選択します。

![特定のアプリからのユーザーを対象としたセグメンテーション。][10]

次に、このセグメントをメッセージに追加し、必要に応じてさらにセグメントやフィルターを追加して、オーディエンスの絞り込みを開始できます。

#### キャンペーン

キャンペーンの場合は、コンポーザーの「**ターゲットユーザー**」ステップにセグメントを追加します。

#### キャンバスフロー

キャンバスフローの [**配信検証**] セクションのメッセージステップにセグメントを追加します。配信検証では、メッセージ送信時にオーディエンスが配信条件を満たしていることが再確認されます。正しいアプリに配信されるように、必ず各メッセージステップに配信検証を指定してください。エントリレベルでセグメンテーションを行う必要はありません。

{% details 元のキャンバスワークフローでのステップs の展開 %}

{% alert important %}
2023 年 2 月 28 日以降、元のエディターを使用したキャンバスの作成や複製はできなくなりました。このコンテンツは参考用であり、元のエディターでのセグメントとターゲット設定を理解するためのものです。<br><br>Braze では、元のキャンバスエクスペリエンスを使用しているお客様に、キャンバスフローへの移行をお勧めしています。これは、キャンバスの構築と管理をより良く行う目的で改良された編集エクスペリエンスです。「[キャンバスからキャンバスフローへの複製]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)」を参照してください。
{% endalert %}

元のキャンバスワークフローで、[**オーディエンス**] セクションのキャンバスコンポーネントレベルにセグメントを追加します。エントリレベルでセグメンテーションを行う必要はありません。
{% enddetails %}


[1]: {% image_buster /assets/img/workspaces/workspace_create.png %}
[2]: {% image_buster /assets/img/workspaces/workspace_name.png %}
[3]: {% image_buster /assets/img/workspaces/workspace_empty_state.png %}
[4]: {% image_buster /assets/img/workspaces/workspace_add_app.png %}
[5]: {% image_buster /assets/img/workspaces/app_api_key.png %}
[6]: {% image_buster /assets/img/workspaces/app_live_sdk_version.png %}
[7]: {% image_buster /assets/img/workspaces/workspace_favorites.png %}
[8]: {% image_buster /assets/img/workspaces/workspace_rename.gif %}
[9]: {% image_buster /assets/img/workspaces/workspace_delete.png %}
[10]: {% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %}
[link]: {{site.baseurl}}/user_guide/getting_started/workspaces/
