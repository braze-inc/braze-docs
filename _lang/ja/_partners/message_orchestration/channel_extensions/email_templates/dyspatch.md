---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "このリファレンス記事では、Braze とDyspatch の連携について概説します。ドラッグアンドドロップメールビルダーを使用すると、コードを記述することなく、美しくレスポンシブで魅力的なメールを作成できます。"
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch][1] は、コードを書く必要なく、美しく、レスポンシブで魅力的なメールs を作成するために使用される直感的なドラッグアンドドロップメールビルダーを提供します。チームと協力して、Dyspatch 内でメールを作成して承認し、それらのメールを Braze にエクスポートします。この作業は短い手順で完了できます。 

Dyspatch と Braze の統合により、Dyspatch メールテンプレートを直接 Braze にエクスポートすることで、メール作成ライフサイクルを簡素化できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dyspatch アカウント | このパートナーシップを利用するには、[所有者権限または管理者権限][4]を持つ[Dyspatch アカウント][3]が必要です。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

BrazeとDyspatchインテグレーションを使用すると、BrazeのメディアライブラリーにDyspatch メール テンプレートを直接エクスポートしたり、テンプレートを読み込むしたり、手動でアップロードしたりできます。 

### ステップ1:Brazeインテグレーションの作成

Dyspatch管理ポータルで、ユーザー名のドロップダウンメニューを開封し、**Integrationsを**選択する。新しいインテグレーションを作成し、**Braze**を選択して、Braze API キーを入力します。

**エクスポートのローカライズ**フィールドで、ローカライゼーションの管理方法を選択できます。このフィールドを使用すると、[メール テンプレートs][6]をローカライズし、Brazeにエクスポートしてメールs パーソナライズされたを言語またはロケールで簡単に送信できます。 

![Dyspatchエクスポートテンプレート]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### ステップ2:Brazeへのテンプレートのエクスポート

Dyspatch でメールを完了した後、テンプレートをBraze に送信するには、公開されたメール テンプレートを表示し、**Down読み込む/Export** をクリックしてから、**Export to Integration** をクリックします。

テンプレートを手動でアップロードする場合は、公開メール テンプレートを表示し、**Down 読み込む/Export** をクリックしてから、**Down 読み込む HTML** をクリックします。次に、Braze アカウントの **[テンプレートとメディア] > [メールテンプレート]** セクションで [**元のファイル**] を選択して、テンプレートをアップロードします。

![Dyspatchエクスポートテンプレート]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
BrazeのDyspatch メール テンプレートの**Sending Info**で**インラインCSS**を選択しないでください。Dyspatch は、メールが堅牢でレスポンシブであり、送信できる状態であることを確認して、これに対応します。
{% endalert %}

### 使用

アップロードした Dyspatch テンプレートを、Braze アカウントの**[テンプレートとメディア] > [メールテンプレート]** セクションで確認します。これで、このメールテンプレートを使用して、顧客に魅力的なメールメッセージを送信できます。

[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: https://www.dyspatch.io/login/
[4]: https://docs.dyspatch.io/administration/dyspatch_roles/
[5]: https://docs.dyspatch.io/exports/export_to_braze/#download-your-template
[6]: https://docs.dyspatch.io/localization/localizing_a_template/
