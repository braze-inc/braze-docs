---
nav_title: Dyspatch
article_title:Dyspatch
alias: /partners/dyspatch
description:「この参考記事では、BrazeとDyspatchのパートナーシップについて概説しています。Dyspatchは、コード記述しなくても、美しく、レスポンシブ、魅力的なメールをドラッグアンドドロップで作成できるメールメールビルダーです。「
page_type: partner
search_tag:Partner

---

# Dyspatch

> [Dyspatchは][1]、直感的なドラッグアンドドロップのメールビルダーを提供しており、コード記述しなくても、美しく、レスポンシブく、魅力的なメールを作成できます。チームと協力してDyspatch内でメールを作成して承認し、Brazeにエクスポートするだけです。これらはすべて数ステップで完了します。 

Dyspatch と Braze の統合により、Dyspatch メールテンプレートを Braze に直接エクスポートすることで、メール作成のライフサイクルを簡素化できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dyspatch アカウント | このパートナーシップを利用するには、[[オーナーまたは管理者の役割を持つDyspatchアカウントが必要です][4]][3]。 |
| Braze REST API キー | **完全なテンプレート権限を持つBraze** REST API キーです。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

Braze と Dyspatch の統合により、Dyspatch メールテンプレートを Braze メディアライブラリーに直接エクスポートしたり、テンプレートをダウンロードして手動でアップロードしたりできます。 

### ステップ1:Braze インテグレーションを作成する

**Dyspatch管理ポータルで、ユーザー名のドロップダウンメニュー開封、「インテグレーション」を選択します。**新しいインテグレーションを作成し、**Braze** を選択し、Braze API キーを入力します。

「**Localize Exports By**」フィールドでは、ローカライゼーションをどのように管理したいかを選択できます。このフィールドでは、[メールテンプレートをローカライズして][6] Braze にエクスポートし、言語やロケールごとにパーソナライズされたメールを簡単に送信できます。 

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### ステップ2:テンプレートを Braze にエクスポート

**Dyspatch でメールを送信した後、テンプレートを Braze に送信するには、公開されているメールテンプレートを表示して \[**ダウンロード/エクスポート] をクリックし、\[インテグレーションにエクスポート**] をクリックします。**

テンプレートを手動でアップロードする場合は、公開されているメールテンプレートを表示し、\[**ダウンロード/エクスポート**]、\[HTML **のダウンロード**] の順にクリックします。次に、Braze アカウントの \[**テンプレートとメディア] > \[メールテンプレート**] セクションで、\[**ファイルから**] を選択してテンプレートをアップロードします。

![Dyspatch Export Template]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
Braze の Dyspatch メールテンプレートの「**送信情報**」セクションで「**インライン CSS**」を選択しないでください。Dyspatchは、メールが堅牢でレスポンシブ、送信準備が整っていることを確認することで、この問題を処理します。
{% endalert %}

### 使用

アップロードした Dyspatch テンプレートは、Braze アカウントの \[**テンプレートとメディア] > \[メールテンプレート**] セクションにあります。これで、このメールテンプレートを使用して、顧客への魅力的なメールメッセージの送信を開始できます。

[1]: https://www.dyspatch.io
[2]: https://dashboard.braze.com/sign_in
[3]: https://www.dyspatch.io/login/
[4]: https://docs.dyspatch.io/administration/dyspatch_roles/
[5]: https://docs.dyspatch.io/exports/export_to_braze/#download-your-template
[6]: https://docs.dyspatch.io/localization/localizing_a_template/
