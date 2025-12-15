{% if include.content == "Differences" %}

[チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)、[権限設定]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set)、[ユーザーロールを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role)使用して、Braze内のダッシュボードユーザーへのアクセスやレスポンシブを管理することができる。各機能には、権限とアクセスコントロールの異なるコレクションが含まれます。

### 主な違い

高いレベルでは、各機能にはそれぞれ異なるスコープがある：
- 権限セットは、すべてのワークスペースでダッシュボードユーザーが実行できる操作を制御します。
- ロールは、ダッシュボードのユーザーが特定のワークスペースでできることをコントロールする。
- チームは、ダッシュボードユーザーがメッセージングでリーチできるオーディエンスをコントロールする。

| 機能 | あなたにできること | アクセス範囲 |
| - | - | - |
| [権限セット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | 特定のサブジェクト領域やアクション（「開発者」や「マーケター」など）に関連する権限を束ね、異なるワークスペース間で同じ権限を必要とするダッシュボードユーザーに適用する。 | 会社全体 |
| [役割]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | 個々のカスタム権限とワークスペースへのアクセスコントロールをバンドルする（例えば、"マーケター - ファッションブランド "のように、ユーザーはマーケターとしての役割に関連する特定の権限を持ち、"ファッションブランド "ワークスペースに限定される）。次に、ダッシュボードユーザーにロールを割り当て、関連する権限とワークスペースへのアクセスを直接付与する。<br><br>このレベルのアクセス権を持つユーザーは、多くのブランドや地域のワークスペースが1つのダッシュボードにあるような、より厳しくコントロールされたセットアップのマネージャーであることが一般的だ。 | 特定のワークスペース |
| [チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | オーディエンス（顧客群の所在地、言語、カスタム属性など）に基づいて、ダッシュボードユーザーのリソースへのアクセスを制限する。<br><br>このレベルのアクセス権を持つユーザーは、通常、多言語ブランドのための言語別コンテンツの構築など、ブランド内の特定の範囲を担当している。 | 特定のダッシュボード |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}