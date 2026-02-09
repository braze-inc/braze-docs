---
nav_title: Transcend
article_title: Transcend
description: "このリファレンス記事では、Braze と Transcend のパートナーシップについて説明します。Transcend はデータプライバシーインフラストラクチャプラットフォームであり、Braze のユーザーがデータ主体要求を自動的に履行できるようにします。"
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend はデータプライバシーインフラストラクチャ企業であり、企業のユーザーがデータを簡単に管理できるようにし、すべてのデータシステムおよびベンダーに対するデータ主体要求を社内での自動的に履行します。 

_この統合は Transcend によって管理されます。_

## 統合について

BrazeとTranscendのパートナーシップは、ユーザーが数十のデータシステムにわたってデータをオーケストレーションすることによってプライバシー要求を自動化し、チームがGDPRやCCPAのような規制に準拠するのを支援する。Transcend はエンドユーザーに対し、`privacy.\<company\>.com` でホストされるコントロールパネルまたはプライバシーセンターを提供します。このコントロールパネルまたはプライバシーセンターでは、ユーザーが各自のプライバシー設定の管理、データのエクスポート、データの削除を行うことができます。 

## 前提条件

| 要件 | 説明 |
|---|---|
| Transcend アカウント | このパートナーシップを利用するには、管理者権限を持つ[Transcend](https://app.transcend.io/) アカウントが必要です。 |
| BrazeのAPIキー | `users.delete, users.alias.new, users.export.ids, email.unsubscribe,`および`email.blacklist` 権限を持つ Braze REST API キー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Transcend では、Braze プラットフォームでコミュニケーションへのアクセス、消去、ユーザーのオプトアウトを、データプライバシー規制に従ってプログラムで実行できるようにします。

### ステップ1:Brazeとの統合をセットアップする
開始するには、[Transcend](https://app.transcend.io/login) にログインします。
1. **[Data Map] > [Add Data Silo] > [Braze]** に移動し、[**Connect**] ボタンを選択します。<br><br>
2. アカウントがプロビジョニングされると、対応するURLのいずれかにログインする：`https://dashboard-01.braze.com` `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu` 。<br> 以下の[表を使って]({{site.baseurl}}/api/basics/#endpoints)、ダッシュボードのURLからどのサブドメインを含めるべきかを考えよう。<br><br>
3. 接続したら、Transcend の [**Privacy Center**] タブに移動します。ここで、Brazeのデータをあなたのデータプラクティスにマッピングする必要がある。これを行うには、適切な命名規則で新しいカテゴリと新しいデータコレクションを作成します (（「Mailing Lists or User Profile」など)。完了したら、**Publishを**選択する。<br><br>
4. データマップに戻り、Brazeデータサイロ化を選択する。**Manage Datapoints（データポイントの管理**）を展開して、前のステップで作成したコ レクション・ラベル（カテゴリ）をドロップダウンから選択する。また、どのデータポイントに対してどのデータアクション (アクセスや消去など) を有効にするかを選択することもできます。<br><br>
5. 次に、Braze データサイロが表示された状態で、[**Manage Identifiers**] を展開します。有効にしたい識別子のボックスにチェックを入れる。たとえば、Transcend でユーザーをメールアドレスで検索する場合は、このチェックボックスをオンにしてメールアドレス識別子を有効にします。

{% alert note %}
識別子が適切に有効化されていない場合、Transcend は特定のユーザーのリクエストを処理できないことがあります。
{% endalert %}

### ステップ2:要求をテストする
Transcend は、エンドユーザーからの要求の処理を開始する前に、Data Map 全体で要求をテストすることを推奨しています。
1. Transcendの**Privacy Centerに**行き、**View your Privacy Centerを**選択する。<br><br>
2. **プライバシーセンターから**「**コントロールする**」を選択し、「**自分のデータをダウンロードする**」を選択する。要求を送信する前に、自分自身を認証するためにメールを入力するか、ログインします。<br><br>
3. メールで Transcend からのメッセージを確認します。リクエストを確認するために、確認リンクをクリックするよう求められる。<br><br>
4. 次に、**管理者**ダッシュボードに戻って、**受信リクエスト**タブに移動し、リクエストを選択する。ここに要求が表示されない場合は、Transcend ([support@transcend.io](mailto:support@transcend.io)) までお問い合わせください。<br><br>
5. 要求をクリックしたら、[**Data Silos**] タブに移動し、[**Braze**] を選択します。返されたデータを検査し、確認する。<br><br>
6. 最後に、**「レポート**」タブに移動し、「**承認して送信**」をクリックする。申請時に提出したEメールアドレスに報告書が届くはずだ。

## Braze 統合を削除する
Transcend Data Mapから Braze データサイロを削除するには、次の手順に従います。
1. **Data Map** に移動し、[**Braze**] をクリックします。<br><br>
2. 画面の下部で [**Remove Braze**] を展開し、[**Remove Silo**] をクリックします。サイロを削除するかどうかを確認するプロンプトが表示される。[**OK**] をクリックします。<br><br>
3. Data Map に戻り、サイロが削除されたことを確認します。


