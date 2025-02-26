---
nav_title: 会社ユーザー
article_title: 会社ユーザー
page_order: 23
layout: dev_guide
guide_top_header: "会社ユーザー"
guide_top_text: "会社の Braze アカウント管理者には、より細かく、またはケースバイケースでユーザーを管理しなければならないことがあります。Braze でチームを作成し、ユーザー権限と全社的な設定を管理することで、そのようなユーザー管理が容易になります。"

page_type: landing
description: "このランディングページには、ユーザーの追加と削除、ユーザー権限の設定、チームの作成、会社の設定の管理など、Braze ユーザーの管理に関する記事の一覧があります。"

guide_featured_title: "セクションの記事"
guide_featured_list:
- name: Braze ユーザーの管理
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/
  image: /assets/img/braze_icons/user-plus-01.svg
- name: ユーザー権限の設定
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/
  image: /assets/img/braze_icons/user-square.svg
- name: チーム
  link: /docs/user_guide/administrative/app_settings/manage_your_braze_users/teams/
  image: /assets/img/braze_icons/users-01.svg
---

## チーム、権限設定、役割の違いは何か？ 

チーム、権限セット、ユーザーロールを使用して、Braze内のダッシュボードユーザーのアクセスと責任を管理できる。各機能には、権限とアクセスコントロールの異なるコレクションが含まれます。

### 主な違い

高いレベルでは、各機能にはそれぞれ異なるスコープがある：
- 権限セットは、すべてのワークスペースでダッシュボードユーザーが実行できる操作を制御します。
- ロールは、ダッシュボードのユーザーが特定のワークスペースでできることをコントロールする。
- チームは、ダッシュボードのユーザーがメッセージを送信できるオーディエンスをコントロールします。

| 特集｜何ができるのか？
| - | - |
| [ 権限セット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | 特定のサブジェクト領域またはアクションに関連する権限 ("Developers" や"Marketers" など) をバンドルし、さまざまなワークスペースで同じ権限を必要とするダッシュボードユーザーに適用します。|
[| ロール]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role)｜個々のカスタム権限とワークスペースへのアクセス制御を定義済みのロール（「マーケター - ファッションブランド」や「マーケター - スキンケアブランド」など）にまとめ、ダッシュボードユーザーにロールを割り当てて、関連するワークスペースへのアクセスと権限を直接付与する。|
[| チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)｜ダッシュボードユーザーのリソースへのアクセスをオーディエンス（顧客群の所在地、言語、カスタム属性など）に基づいて制限する。|
{: .reset-td-br-1 .reset-td-br-2 }