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

![The "User Search" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:90%;"}

メールアドレスや電話番号など、重複プロファイルの一意の識別子を入力し、「**検索**」を選択します。

![The "User Search" page in the Braze dashboard with an email entered in the search bar.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### ステップ2: 重複をマージする

マージ処理を開始するには、[**重複をマージする**] を選択します。

![One of the duplicate user's profiles.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:55%;"}

保持するユーザープロファイルとマージするユーザープロファイルを選択し、[**プロファイルをマージする**] を選択します。重複するプロファイルをすべて統合するまで、このプロセスを繰り返します。

![The individual merge page for a duplicate profile.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

{% alert warning %}
マージ後、重複したユーザープロファイルを復元できません。
{% endalert %}

## 一括マージ

{% alert important %}
重複ユーザーの一括マージは現在早期アクセス中です。早期アクセスへの参加に興味がある場合は、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

重複ユーザーを一括マージする場合、Braze は一致する識別子 (メールアドレスなど) を持つプロファイルを検索し、そのすべてのデータを、`external_id` を持つ最も新しく更新されたプロファイルにマージします。`external_id` を持つプロファイルがない場合、`external_id` を持たないのない最も最近に更新されたプロファイルが代わりに使用されます。

### ステップ1: [オーディエンスを管理] に移動する

Braze ダッシュボードで、[**オーディエンス**] > [**オーディエンスを管理**] を選択します。

![The "Manage Audience" tile highlighted in the navigation menu.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:90%;"}

### ステップ2: 結果をプレビューする (オプション)

重複をマージする前に結果をプレビューするには、[**重複のリストを作成するを**] 選択します。

![The "Manage Audience" page with "Generate list of duplicates" highlighted.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze がプレビューを作成し、CSV ファイルとしてあなたのメールアドレスに送信します。

![An email from Braze with a link to the generated CSV file.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

以下の例では、Braze はユーザーの外部 ID を使用して、重複するプロファイルにフラグを立て、どちらを保持するかを特定します。これらのプロファイルが一括マージされた場合、Braze は外部 ID を持つプロファイルをユーザーの新しいプライマリプロファイルとして使用します。これで、そのユーザーがマージされたプロファイルを使ってログインすると、Braze が代わりに新しいプライマリプロファイルを更新します。

{% tabs local %}
{% tab example csv file %}
| メールアドレス｜外部 ID｜電話番号｜Braze ID｜ルールの識別子｜保持するプロファイル｜マージするプロファイル |
|----------------------|-------------|--------------|--------------------------|---------------------|-----------------|------------------|
| alex@company.com     |   A8i3mkd99          |      (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |  |      (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |   |      (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% endtabs %}

### ステップ3 重複を統合する

プレビューの結果に満足したら、[**すべての重複項目をマージ**] を選択します。

{% alert warning %}
マージ後、重複したユーザープロファイルを復元できません。
{% endalert %}

![The "Manage Audience" page with "Merge all duplicates" highlighted.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}
