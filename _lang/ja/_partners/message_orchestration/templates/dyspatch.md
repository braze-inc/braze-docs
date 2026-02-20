---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "このリファレンス記事では、Braze とDyspatch の連携について概説します。ドラッグアンドドロップメールビルダーを使用すると、コードを記述することなく、美しくレスポンシブで魅力的なメールを作成できます。"
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) は、コードを書く必要なく、美しく、レスポンシブで魅力的なメールs を作成するために使用される直感的なドラッグアンドドロップメールビルダーを提供します。チームと協力して、Dyspatch 内でメールを作成して承認し、それらのメールを Braze にエクスポートします。この作業は短い手順で完了できます。 

_この統合は Dyspatch によって管理されます。_

## 統合について

Dyspatch と Braze の統合により、Dyspatch メールテンプレートを直接 Braze にエクスポートすることで、メール作成ライフサイクルを簡素化できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Dyspatch アカウント | このパートナーシップを利用するには、[所有者権限または管理者権限](https://docs.dyspatch.io/administration/dyspatch_roles/)を持つ[Dyspatch アカウント](https://www.dyspatch.io/login/)が必要です。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

BrazeとDyspatchインテグレーションを使用すると、BrazeのメディアライブラリーにDyspatch メール テンプレートを直接エクスポートしたり、テンプレートを読み込むしたり、手動でアップロードしたりできます。 

### ステップ1:Brazeインテグレーションの作成

Dyspatch 管理ポータルでユーザー名のドロップダウンメニューを開き、[**統合**] を選択します。新しいインテグレーションを作成し、**Braze**を選択して、Braze API キーを入力します。

**エクスポートのローカライズ**フィールドで、ローカライゼーションの管理方法を選択できます。このフィールドを使用すると、[メール テンプレートs](https://docs.dyspatch.io/localization/localizing_a_template/)をローカライズし、Brazeにエクスポートしてメールs パーソナライズされたを言語またはロケールで簡単に送信できます。 

![Dyspatchエクスポートテンプレート]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### ステップ 2:Brazeへのテンプレートのエクスポート

Dyspatch でメールを完了した後、テンプレートをBraze に送信するには、公開されたメール テンプレートを表示し、**Down読み込む/Export** をクリックしてから、**Export to Integration** をクリックします。

テンプレートを手動でアップロードする場合は、公開メール テンプレートを表示し、**Down 読み込む/Export** をクリックしてから、**Down 読み込む HTML** をクリックします。次に、テンプレートをアップロードするには、Brazeアカウントの**テンプレート s & Media > Eメールテンプレート s** セクションで、**From File** を選択します。

![Dyspatchエクスポートテンプレート]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
BrazeのDyspatch メール テンプレートの**Sending Info**で**インラインCSS**を選択しないでください。Dyspatch は、メールが堅牢でレスポンシブであり、送信できる状態であることを確認して、これに対応します。
{% endalert %}

### 使用

Braze アカウントの** テンプレート s & Media > E メールテンプレート s** でアップロードのDyspatch テンプレートを見つけます。これで、このメールテンプレートを使用して、顧客に魅力的なメールメッセージを送信できます。


