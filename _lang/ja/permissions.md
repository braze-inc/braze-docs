{% if include.content == "Differences" %}

[Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)、[パーミッションセット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set)、および[ユーザーロール]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role)を使用して、Braze内のダッシュボード ユーザーのアクセスと担当を管理できます。各機能には、権限とアクセスコントロールの異なるコレクションが含まれます。

### 主な違い

高いレベルでは、各機能にはそれぞれ異なるスコープがある：
- 権限セットは、すべてのワークスペースでダッシュボードユーザーが実行できる操作を制御します。
- ロールは、ダッシュボードのユーザーが特定のワークスペースでできることをコントロールする。
- チームは、ダッシュボード ユーザー s がメッセージで到達できるオーディエンス s をコントロールします。

| 機能| 実行できること| アクセス範囲|

| [権限セット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | 特定のサブジェクト領域またはアクションに関連するバンドル権限("Developers" や"Marketers" など) をバンドルし、異なるワークスペース間で同じ権限を必要とするダッシュボード ユーザーにアプリします。| 全社|
| [ロール]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | 個別のカスタム権限とワークスペース-アクセスコントロールをバンドルします(" マーケター - Fashion Brands" など。ここで、ユーザーはマーケターとしてのロールに関連付けられた特定の権限を持ち、"Fashion Brands" ワークスペース s に制限されます)。次に、ダッシュボード ユーザー s にロールを割り当てて、関連付けられた権限とワークスペース権限を直接的に付与します。<br><br>このレベルのアクセス権を持つユーザは、通常、多くのブランドまたはリージョナルワークスペースを1 つのダッシュボードに持つ、より緊密にコントロール主導の設定でマネージャーです。| 特定のワークスペース s |
[| チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams)｜ダッシュボードユーザーのリソースへのアクセスをオーディエンス（顧客群の所在地、言語、カスタム属性など）に基づいて制限する。|<br><br>このレベルのアクセス権を持つユーザは、通常、多言語ブランド用の言語固有のコンテンツを構築するなど、自分が作業しているブランド内の特定のスコープに対して責任を負います。| 特定のダッシュボード|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}