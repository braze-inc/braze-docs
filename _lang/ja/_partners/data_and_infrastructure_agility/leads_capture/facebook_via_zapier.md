---
nav_title: ZapierによるFaceBookのリード広告
article_title: ZapierによるFaceBookのリード広告
description: "このレファレンス記事では、BrazeとFac eBookリード広告の統合をZapierを介して概説し、Fac eBookからBrazeへのリードデータの転送を自動化し、リアルタイムのエンゲージメントとパーソナライズされたのフォローアップアクションsを可能にします。"
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# ZapierインテグレーションによるFaceBookのリード広告

> Fac eBook リードアドインテグレーションでは、<a href="https://zapier.com/" target="_blank">Zapier</a> を使用して、リードをFac eBookからBraze に読み込んで、リードがキャプチャされたときにカスタムイベントを追跡できます。 

Fac eBookリード広告は、企業がFac eBookで直接的にリード情報を収集できる広告形式です。これらの広告は、リード生成プロセスを簡単かつシームレスにするように設計されています。ZapierインテグレーションとBrazeを活用することで、Fac eBookからBrazeへのリードデータの転送を自動化し、リアルタイムのエンゲージメントとパーソナライズされたのフォローアップアクションを可能にします。 

## 前提条件

| 要件 | 説明 |
|---|---|
| Zapier勘定 | この提携の前進タグeを考慮するには、Zapierな考慮が必要である。この統合では、<a href="https://zapier.com/app/pricing/" target="_blank">プレミアムZapier アプリs</a>を使用する必要があるため、Zapierプランがプレミアムアプリsにアクセスできることを確認します。 |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Fac eBook リードアクセス</a> | Fac eBook リードアクセスは、Braze で使用する予定の広告アカウントごとに必要です。 |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">ファックeBook事業部長</a> | この統合の一環として、Fac eBookビジネスマネージャを使用して、ブランドのFac eBookアセット(広告アカウント、ページ、アプリなど)を管理します。 |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">FaceBookの広告アカウント</a> | あなたのブランドの事業マネージャーと結びついた、有効なFaceBookの広告アカウントが必要になります。<br><br>「&quot」、「Ad accounts&quot の管理」、「Braze」で使用する予定の広告アカウントごとの権限、および広告アカウントの条件を承諾していることを確認します。 |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">ファクスeBook画面</a> | 自社の事業マネージャーに合わせて、能動的なFac eBookページが必要となる。<br><br>Braze で使用するFac eBook ページごとに、"Manage Pages" 権限があることを確認します。 |
| Braze REST エンドポイント | [ REST エンドポイント URL][1] を確認してください。API エンドポイントは、Brazeインスタンスのダッシュボード URL と一致します。<br><br> たとえば、ダッシュボード URL が`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` になります。 |
| Braze REST API キー | `users.track` 権限を持つBraze REST API キーがあることを確認します。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:インスタントフォームでリード広告キャンペーンを作成する

Fac eBook Ads Manager から、<a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Fac eBook リードキャンペーンとFac eBook リードアドフォーム</a> を作成します。

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)へのリクエスト時に、メールの住所または電話番号を使用して、ユーザープロファイルを更新または作成できます。このため、リード広告フォームに****メール**または**phone**の**連絡先フィールド**を含めてください。名または姓を収集する場合は、フルネームではなくフォームで別々に収集します。

### ステップ2:Fac eBook をZapier に接続する 

#### ステップ 2a: Zapierで接続方法を選択する

Zapierで、**アプリ s** に移動し、使用可能なFac eBook アプリ s を検索します。**Fac eBook リード広告**または**Fac eBook リード広告(ビジネス管理者向け)**を選択します。

Fac eBook アカウントを Zapier に接続する方法の詳細については、以下を参照してください。

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Fac eBook リードアド(企業管理者向け)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">ファック・eBookのリード広告</a>

![][2]{: style="max-width:80%;"}

#### ステップ 2b: Fac eBook Business Manager へのZapierの追加

Fac eBook ビジネスマネージャの左側のメニューで、**Integrations** > **Leads Access** に移動します。Fac eBook ページを選択し、**CRM s** をクリックします。CRMタブで、**CRMs**を割り当て、**Zapier**を追加します。

![][3]{: style="max-width:80%;"}

CRMインテグレーションとしてZapierを割り当てるステップについては、FaceBookの<a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">ドキュメント</a>を参照してください。

### ステップ3:Zap を作成する

#### ステップ3a:トリガーの作成 

Fac eBook アカウントを接続したら、Zap の作成に進むことができます。**Trigger**の場合は、ステップ 2 からお好みの**Fac eBook リードアド**または**Fac eBook リードアド(ビジネス管理者向け)**を選択します。 

![][4]{: style="max-width:80%;"}

**Event**では、**New Leads**> **Continue**を選択します。 

![][5]{: style="max-width:80%;"}

Fac eBookを選択し、**Continue**を選択します。 

![][6]{: style="max-width:80%;"}

以前に作成したFac eBook ページとインスタントフォームを選択し、**Continue** を選択します。

![][7]{: style="max-width:80%;"}

次に、このトリガーを試します。フォーム出力を検証したら、**選択したレコードで続行**を選択します。

#### ステップ3b:アクションの作成

新しいステップを追加し、** Web hooks by Zapier** を選択します。次に、**Custom Request**を**Event**フィールドに選択し、**Continue**を押します。 

![][8]{: style="max-width:80%;"}

最後に、フィールド s を有料読み込むに挿入して、カスタムリクエストを設定します。次のコード スニペットは、サンプルの給与読み込むを示しています。 

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

次に、Zapier の例を示します。

![][9]{: style="max-width:80%;"}

Webhookを設定した後、**Continue とtest** を選択します。テストが成功した場合は、Zap を公開できます。

### ステップ4:Fac eBook リードアドザップのテスト

このエンドツーエンドのをテストするには、Fac eBook 開発者コンソールでFac のリードアドテストツールを使用します。詳細については、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">テストとトラブルシューティング</a>を参照してください。

## ユーザー識別管理

このインテグレーションでは、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number)をメールしてFaceBookリードを属性できます。

* メールが既存のユーザープロファイルと一致した場合、Braze はFac eBook リードデータでプロファイルを更新します。
* 同じメールを持つ複数のユーザープロファイルs がある場合、Braze は更新s の外部ID を持つ最後の更新d プロファイルに優先順位を付けます。
* 外部ID が存在しない場合、Braze は、一致するメールを持つ最新の更新d プロファイルを優先します。
* 指定されたプロファイルがメールと共に存在しない場合、Brazeは新しいプロファイルを作成し、新しい別名ユーザープロファイルが作成されます。新しく作成された別名ユーザープロファイルs を識別するには、[`/users/identify`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) を使用します。

{% alert note %}
これらのフィールドが利用可能で、インテグレーションに使用したいプライマリ識別子がある場合は、Brazeへのリクエストの一部として電話番号または外部ID を使用することもできます。これを行うには、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) に示すように、リクエストの支払い読み込むを変更します。
{% endalert %}

## トラブルシューティング

{% details トリガーとアクションを正常にテストしたため、Zapierのザップを公開できないのはなぜですか? %}
この統合を使用するには、プレミアムアプリs をサポートする<a href="https://zapier.com/app/pricing/" target="_blank">Zapierプラン</a> が必要です。
{% enddetails %}

{% details ファクスeBookがBrazeに同期しないのはなぜですか? %}
1. ファックeBookページ、広告アカウント、およびリードアクセスに管理者がアクセスできることを確認します。次に、Zapier でアカウントを再接続します。
2. Fac eBook で作成したインスタントフォームが、トリガーステップで選択したフォームにマッピングされていることを確認します。 
3. **Fac eBook Business Manager**> **Integrations**> **Lead Access**に移動して、リードアクセスにZapierを割り当てたことを確認します。
{% enddetails %}

{% details なぜ同じメールの重複ユーザープロファイルsを見ているのですか? %}
[ユーザープロファイルライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle) に基づいて、Braze でユーザープロファイルs を作成および管理する独自の方法があります。

内部の処理に応じて、またBraze 内で顧客 s を作成するトリガーを作成しているときに、統合によって作成されるユーザープロファイルの競合と、システムからユーザーが作成されるときに、重複するユーザープロファイル s が発生することがあります。[マージユーザープロファイルs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)をBrazeで使用できます。
{% enddetails %}

{% details Zapier口座を持っていません。Fac eBookのリード広告webhookをBrazeにトリガーするにはどうすればよいですか? %}
Zapier を使用せず、Zapier を使用する予定がない場合は、Fac eBook からBraze にインテグレーションを構築できます。詳細については、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">リード広告ドキュメント</a>を参照してください。

Fac eBookからリードを取得するには、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhook</a> を使用します。ファクトeBookのwebhookを始めるには、<a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">webhook ドキュメント</a>を参照してください。

Fac eBook でwebhook URL を確立したら、チームと協力して、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) にデータを転送する最適なパスを決定します。Zapier アプリ ローチと同様に、`users/track` エンドポイントを通じて、メール によって[ リクエストを行うことをお勧めします。
{% enddetails %}

{% alert tip %}
トラブルシューティングのヒントについては、Zapierの<a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Fac eBookのトラブルシューティングガイド</a>を参照してください。
{% endalert %}


[1]: {{site.baseurl}}/api/basics/#api-definitions
[2]: {% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}
[3]: {% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}
[4]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}
[5]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}
[6]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}
[7]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}
[8]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}
[9]: {% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}