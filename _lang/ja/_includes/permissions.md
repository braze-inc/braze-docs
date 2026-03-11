{% if include.content == "Differences" %}

[Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)、[権限セット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set)、[ユーザーロール]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role)を使って、Braze内での会社のユーザーアクセスと責任を管理できる。各機能には、権限とアクセスコントロールの異なるコレクションが含まれます。

### 主な違い

高いレベルでは、各機能にはそれぞれ異なるスコープがある：
- 権限セットは、会社のユーザーがすべてのワークスペースで何ができるかをコントロールする。
- ロールは、会社のユーザーが特定のワークスペースで何ができるかをコントロールする。
- チームは、企業ユーザーがメッセージングで到達できるオーディエンスをコントロールする。

| 機能 | あなたにできること | アクセス範囲 |
| - | - | - |
| [権限セット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | 特定の分野やアクションに関連する権限（例えば「開発者」や「マーケター」向け）をまとめて束ね、異なるワークスペースで同じ権限を必要とする会社のユーザーに適用する。 | 全社的に |
| [役割]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | 個別のカスタム権限とワークスペースアクセスコントロールを組み合わせる（例：「マーケター - ファッションブランド」では、ユーザーはマーケターとしての役割に関連する特定の権限を持ち、「ファッションブランド」ワークスペースに限定される）。次に、会社のユーザーに役割を割り当て、関連する権限とワークスペースへのアクセスを直接付与する。<br><br>このレベルのアクセス権を持つユーザーは、通常、より厳格にコントロールされた環境におけるマネージャーである。そのような環境では、単一のダッシュボードに複数のブランドや地域別のワークスペースが存在している。 | 特定のワークスペース |
| [チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | ユーザーのリソースへのアクセスを、オーディエンス（顧客基盤の所在地、言語、カスタム属性など）に基づいて制限する。<br><br>このアクセス権限を持つユーザーは、通常、担当するブランド内の特定範囲を担当する。例えば、多言語ブランド向けに言語固有のコンテンツを作成するといった業務だ。 | 特定のダッシュボード |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}