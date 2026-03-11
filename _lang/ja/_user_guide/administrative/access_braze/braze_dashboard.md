---
nav_title: ダッシュボード
article_title: Brazeダッシュボード
page_order: 5
page_type: reference
description: "Brazeダッシュボードは、カスタマーエンゲージメントの構築、管理、分析を行うための中心的なワークスペースだ。メッセージングツール、オーディエンスインサイト、セグメンテーション、リアルタイムのパフォーマンスデータを一箇所に集約する。"

---

# Brazeダッシュボード

> Brazeダッシュボードは、カスタマーエンゲージメントの構築、管理、分析を行うための中心的なワークスペースだ。または[dashboard.braze.com](https://dashboard.braze.com/)で[dashboard.braze.eu](https://dashboard.braze.eu/)アクセスできる。

Brazeダッシュボードを使って、キャンペーンの計画、メッセージの配信と管理、オーディエンスのインサイト、セグメンテーションの調整を行い、単一のインターフェイスからリアルタイムのパフォーマンスとエンゲージメント指標を確認する。

## ダッシュボードの概要

ログインすると、ダッシュボードはエンゲージメントツールとデータを一元的に表示する。

- **ホームページ：**[最近編集したコンテンツ](#pick-up-where-you-left-off)と主要なパフォーマンス指標を一目で確認できる
- **左側のナビゲーション：**ツールを機能別に整理する（メッセージング、オーディエンス、分析、設定）
- **グローバルヘッダー：**検索、サポート、言語設定、通知、アカウントへの素早いアクセスを提供する

ダッシュボードの操作環境は[ワークスペース]({{site.baseurl}}/user_guide/getting_started/workspaces)ごとに整理されている。これにより、異なるブランド、地域、チーム向けのコンテンツを管理しやすくなる。サイドナビゲーションからいつでも[ワークスペースを切り替えられる](#workspace-switcher)。

## ダッシュボードにアクセスする

始めるには、[Brazeアカウントにサインインする]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account)。ダッシュボード内のページへのアクセス権と特定のアクションを実行する権限は、割り当てられた[ユーザー]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions)権限に基づいている。権限設定で問題がある場合は、Brazeの管理者にお問い合わせください。

## Brazeを操作する

Braze のナビゲーションは、デバイスを問わず機能やコンテンツに効率的にアクセスできるように設計されています。Brazeダッシュボードには2段階のナビゲーションがある：グローバルヘッダーとサイドナビゲーションだ。

グローバルヘッダーは、ほぼ常に画面の上部に表示されている。必要なツールや設定に素早くアクセスできる。具体的には以下の通りだ：

- 検索
- サポートとコミュニティリンク
- [ダッシュボードの言語]({{site.baseurl}}/user_guide/administrative/access_braze/language/)
- 通知
- アカウント設定
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/)

### サイドナビゲーションを使え

左側の縦型メニューは、Brazeのツールを機能別に整理し、最もよく使う項目をすぐ使えるように配置している。メインメニュー項目を選択すると、スタックされた垂直レイアウトにそのオプションが表示されます。 

![Brazeダッシュボードのワークスペース切替機能]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### ワークスペーススイッチャー

サイドナビゲーションの上部に位置するワークスペーススイッチャーは、Brazeインスタンス内の異なるワークスペース間を移動できるようにする。アクティブなワークスペースが強調表示されている。

[ワークスペースは]({{site.baseurl}}/user_guide/getting_started/workspaces)、ブランド、地域、製品ライン、またはチームごとにコンテンツを整理するのに役立つ。各ワークスペースには、独自のデータ、キャンペーン、設定が含まれている。アクセス権はワークスペースによって異なる場合がある。例えば、あるワークスペースでは編集権限を持ち、別のワークスペースでは閲覧のみ権限を持つ場合がある。

ワークスペースを切り替えるには、サイドナビゲーション上部のワークスペースドロップダウンを選択し、アクセスしたいワークスペースを選ぶ。よく使う[ワークスペースをお気に入りに追加](#adding-favorite-workspaces)すれば、より素早くアクセスできる。

#### サイドナビゲーションを最小化する

視覚的な煩雑さを減らすため、特にキャンバスをデザインするといった作業中は、サイドナビゲーションパネルを最小化できる。**最小化メニュー**を押すと折りたたまれる。最小化していても、アイコンにカーソルを合わせればメニュー項目の名前が表示される。これにより、ワークスペースを整理したままツール間を素早く移動できる。

![最小化と最大化のメニューアイコン]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### レスポンシブなナビゲーション

ナビゲーションは様々な画面サイズにシームレスに適応する。小さい画面では、サイドナビゲーションは自動的に折りたたまれます。必要に応じて、<i class="fa-solid fa-bars" aria-label="ナビゲーションメニュー"></i>を押してメニューを開きます。 

![小さい画面では、サイドナビゲーションは自動的に折りたたまれます。メニューアイコンをタップすると、ナビゲーションオプションが開封される。]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## ダッシュボードを検索する

ヘッダーにあるグローバル検索バーは、Brazeダッシュボード全体でコンテンツを探す最も速い方法だ。選択すると検索インターフェイスが開き、必要な場所に直接移動できる。 

![検索語句を入力せずにグローバル検索を開くと、最近開封したページが表示される。]({% image_buster /assets/img/navigation/search_recently_opened.png %})

最近開封したコンテンツは検索バーの下に表示される。これには、最近操作したキャンペーン、キャンバス、テンプレート、ページが含まれる。これにより、作業を再開するのが簡単になる。

### 検索できる項目

次の項目とアクションを検索できます。

- キャンペーン名
- キャンバス名
- コンテンツブロック
- セグメント名
- メールテンプレート名
- Braze内のページ（同義語を含む）

{% alert tip %}
完全に一致するテキストを検索するには、検索語を引用符 ("") で囲みます。例えば、“すべてのユーザー“ を検索すると、“すべてのユーザー“ と完全に一致する語句を名前に含むすべての項目が返されます。
{% endalert %}

### コンテンツタイプとステータスタグ

各結果には、その内容の種類（キャンペーン、キャンバス、セグメントなど）とステータス（アクティブ、アーカイブ済み、停止済み）を示すタグが付いている。

### 有効および下書き内容のフィルター

デフォルトでは、検索はアクティブ、下書き、アーカイブされたアイテムを含む。**「アクティブと下書きのみを表示」**トグルを使って、結果を絞り込む。

!["有効と下書きのみを表示"を切り替えます。]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### キーボードショートカット

キーボードを使って検索結果を移動できる。

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| アクション (Action)                      | キーボードショートカット                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| 検索メニューを開く        | {::nomarkdown}<ul> <li> Mac: <kbd>⌘</kbd> + <kbd>K</kbd></li> <li>Windows:<kbd>Ctrl</kbd> + <kbd>K</kbd></li> </ul> {:/}  |
| 検索結果間の移動 | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| 検索結果を選択      | <kbd>Enter</kbd>    |
| 検索メニューを閉じる       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ヒント

Brazeのダッシュボードには、作業効率を高め、最も頻繁に使用するツールやコンテンツに素早くアクセスするための機能がいくつか備わっている。

### 中断したところから再開

ホームページでは、ダッシュボードに最近編集または作成したキャンペーン、キャンバス、セグメントが表示される。これで作業中のファイルを簡単に再開できる。探す必要はない。各項目には、コンテンツの種類とステータス（下書き、有効、停止など）を示すタグが付いている。

![[中断したところから再開] セクションのキャンバスの下書き、アクティブなセグメント、およびキャンペーンの下書き。]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

詳細については、[ホームダッシュボードを]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off)参照せよ。

### お気に入りのワークスペースを追加する

複数のワークスペースをまたがって作業する場合、最も頻繁に使用するワークスペースをお気に入りに登録すれば、より速くアクセスできる。お気に入りのワークスペースを追加するには、[プロファイル設定にアクセスし](#accessing-your-profile-settings)、**アカウントプロファイル**セクション内**のお気に入りワークスペース**フィールドを探し、お気に入りに追加したいワークスペースを選択する。お気に入りのワークスペースは、ワークスペース切替画面の上部に表示される。すぐにアクセスできる。

### プロファイル設定にアクセスする

アカウント設定、通知設定、個人情報を管理するには：

1. グローバルヘッダーにあるプロファイルアイコンを選択せよ。
2. **アカウント管理**を選択してプロファイルページにアクセスする。

プロファイルページから、メール設定の更新、2 要素認証の設定、API キーの確認、その他のアカウント詳細の管理ができる。

## ダッシュボードのアクセシビリティ

Brazeのダッシュボードは、WCAG AA基準を満たすブランドカラーを使用している。これは全てのユーザーにとって包括的な体験を支え、アクセシビリティのベストプラクティスに沿っている。

## フィードバックの共有

意見を聞かせてくれないか？ナビゲーション、アクセシビリティ、ユーザビリティ、ビジュアルデザインなどに関するフィードバックを共有できる。グローバルヘッダーの**サポート**メニューを開封し、**フィードバックを共有**を選択する。すべてのフィードバックを確認し、Brazeの体験を改善する手助けをする。

## 関連リソース

### 事務作業

- [ワークスペースを作成し管理する]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)
- [Brazeユーザーを管理する]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- [ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)
- [チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)

### 主要な課題と今後のステップ

- **キャンペーンを作成する**：[キャンペーンを作成する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)
- **旅を作る**：[キャンバスを作る]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- **オーディエンスを定義する**：[セグメントを作成する]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)
- **パフォーマンスをレビューする**[分析の概要]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/)
- **設定を構成する**：[アプリ設定]({{site.baseurl}}/user_guide/administrative/app_settings/)


