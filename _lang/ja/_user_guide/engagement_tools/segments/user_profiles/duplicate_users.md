---
nav_title: 重複ユーザー
article_title: 重複ユーザー
description: "Braze ダッシュボードで重複ユーザーを見つけてマージする方法について説明します。"
page_order: 0
---

# 重複ユーザー

> 重複ユーザーを見つけて統合する方法を学ぶことで、キャンペーンとキャンバスの効果を最大化できます。

{% alert tip %}
Braze REST API を使用して重複ユーザーをマージするには、[ ポストを参照してください。ユーザーをマージする ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
{% endalert %}

## 個別のマージ

ユーザー検索で重複プロファイルが返された場合、Braze ダッシュボードのユーザープロファイルから各プロファイルを個別にマージできます。

### ステップ1: 重複するプロファイルを検索する

Braze で、[**オーディエンス**] > [**ユーザー検索**] を選択します。

![ナビゲーションメニューで強調表示された「ユーザー検索」タイル]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

メールアドレスや電話番号など、重複プロファイルの一意の識別子を入力し、「**検索**」を選択します。

![Braze ダッシュボードの [ユーザー検索] ページ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### ステップ2:重複をマージする

マージ処理を開始するには、[**重複をマージする**] を選択します。

![重複するユーザープロファイルの 1 つ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

保持するユーザープロファイルとマージするユーザープロファイルを選択し、[**プロファイルをマージする**] を選択します。重複するプロファイルをすべて統合するまで、このプロセスを繰り返します。

![個人の重複するプロファイルのマージページ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
マージ後、重複したユーザープロファイルを復元できません。
{% endalert %}

## 一括マージ

重複ユーザーを一括マージする場合、Braze は一致する識別子 (メールアドレスなど) を持つプロファイルを検索し、そのすべてのデータを、`external_id` を持つ最も新しく更新されたプロファイルにマージします。`external_id` を持つプロファイルがない場合、`external_id` を持たないのない最も最近に更新されたプロファイルが代わりに使用されます。

### ステップ1: [オーディエンスを管理] に移動する

Braze ダッシュボードで、[**オーディエンス**] > [**オーディエンスを管理**] を選択します。

![ナビゲーションメニューの強調表示された [オーディエンスを管理] タイル。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### ステップ2:結果をプレビューする (オプション)

重複をマージする前に結果をプレビューするには、[**重複のリストを作成するを**] 選択します。

![[重複のリストを生成] が強調表示された [オーディエンスを管理] ページ。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze がプレビューを作成し、CSV ファイルとしてあなたのメールアドレスに送信します。

![生成されたCSVファイルへのリンクが記載されたBrazeからのメール。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

以下の例では、Braze はユーザーの外部 ID を使用して、重複するプロファイルにフラグを立て、どちらを保持するかを特定します。これらのプロファイルが一括マージされた場合、Braze は外部 ID を持つプロファイルをユーザーの新しいプライマリプロファイルとして使用します。

{% tabs local %}
{% tab csvファイルの例 %}
| メールアドレス｜外部 ID｜電話番号｜Braze ID｜ルールの識別子｜保持するプロファイル｜マージするプロファイル |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### マージ動作

Brazeは、保持しているプロファイルの空のフィールドを、統合したプロファイルの値で埋める。入力されるフィールドのリストについては、「[マージ動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)」を参照してください。

### ステップ 3:重複を統合する

プレビューの結果に満足したら、[**すべての重複項目をマージ**] を選択します。

{% alert warning %}
マージ後、重複したユーザープロファイルを復元できません。
{% endalert %}

![[すべての重複項目をマージ] が強調表示された [オーディエンスを管理] ページ。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## ルールベースのマージ

ルールを使用して、マージを実行する際に重複プロファイルの解決方法をコントロールし、最も関連性の高いユーザープロファイルを保持することができます。ルールが設定されると、Brazeは条件に一致するプロフィールを保持する。

### ステップ 1:ルールを明確にする

1. [**オーディエンス**] > [**オーディエンスを管理**] > [**ルールを編集**] に移動します。.
2. **ルールの編集]**パネルの**[保持するプロファイル]**セクションで、重複をマージする際に保持するプロファイルの**[識別子]**を選択する。これはメールアドレスでも電話番号でも構わない。
3. [**同点の解決**] セクションで、[**保持するプロファイル**] の条件が一致する複数のプロファイルからいずれを優先するか解決する方法の決定基準を選択します。以下の項目を選択できます。<br>
- **解決に使用**: 作成日、更新日、最終セッション
- **優先基準**: 最新、最古

![[保持するプロファイル] と [同点の解決] のオプションを選択するセクションを持つ [ルールを編集] パネル。]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

例えば、電話番号を持つプロファイルを保持できます。複数のユーザーが同じ電話番号を持っている場合、**更新日**フィールドを使用して結びつきを解決し、最も最近更新されたユーザーを優先することができる。

### ステップ2:結果をプレビューする (オプション)

ルールを保存した後、**重複リストを生成するを**選択すると、そのルールがどのように機能するかをプレビューすることができる。Brazeはプレビューを作成し、あなたのルールが適用された場合にどのユーザーが維持され、マージされるかを示すCSVファイルとして、あなたの電子メールアドレスに送信する。 

### ステップ 3:重複をマージする

プレビューの結果に満足したら、**「Manage Audience」**ページに戻り、**「Merge all duplicates**」を選択する。

{% alert warning %}
マージ後、重複したユーザープロファイルを復元できません。
{% endalert %}

## スケジュールされたマージ

ルールベースのマージと同様に、スケジュールされたマージでは、事前設定されたルールを使用して、ユーザープロファイルのマージを毎日自動化できます。

![[スケジュール] ボタンのある [オーディエンスの管理] ページ。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %}

この機能をオンにすると、Braze はユーザーの会社が位置するタイムゾーンの時刻で午前 12 時にマージ処理を毎日実行するタイムスロットを自動的に割り当てます。スケジュールされたマージはいつでもオフにできます。Braze は、スケジュールされたマージが発生する24時間前にワークスペースの管理者に通知し、設定を確認するためのリマインダーと時間を提供します。

{% alert warning %}
マージ後、重複したユーザープロファイルを復元できません。
{% endalert %}
