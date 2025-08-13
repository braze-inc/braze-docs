---
nav_title: ZapierによるFaceBookのリード広告
article_title: ZapierによるFaceBookのリード広告
description: "このリファレンス記事では、Zapierを介した Braze と Facebook リード獲得広告との統合による Facebook から Brazeへのリードデータの転送の自動化について説明します。これにより、リアルタイムのエンゲージメントとパーソナライズされたフォローアップアクションが可能になります。"
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# ZapierインテグレーションによるFaceBookのリード広告

> <a href="https://zapier.com/" target="_blank">Zapier</a> を介した Facebook リード獲得広告への統合により、Facebook から Braze にリードをインポートし、リードがキャプチャされたときにカスタムイベントを追跡することができます。 

Facebook Lead Ads は、企業が Facebook で直接リード情報を収集できる広告フォーマットです。リード獲得広告は、リード生成プロセスを簡単かつシームレスにするように設計されています。Zapier 統合と Braze を利用することで、Facebook から Braze へのリードデータの転送を自動化でき、リアルタイムのエンゲージメントとパーソナライズされたフォローアップアクションが可能になります。 

## 前提条件

| 要件 | 説明 |
|---|---|
| Zapierアカウント | このパートナーシップを活用するには、Zapier アカウントが必要です。この統合には、<a href="https://zapier.com/app/pricing/" target="_blank">プレミアム Zapier アプリ</a>を使用する必要があります。そのため、ご利用の Zapier プランでプレミアムアプリを使用できることを確認してください。 |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Facebook リードアクセス</a> | Braze で使用する予定の各広告アカウンには、Facebook リードアクセスが必要です。 |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager</a> | この統合の一環として、Facebook Business Manager を使用します。Facebook Business Manager は、ブランドの Facebook アセット (広告アカウント、ページ、アプリなど) を管理するための一元的なツールです。 |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Facebook 広告アカウント</a> | あなたのブランドの事業マネージャーと結びついた、有効なFaceBookの広告アカウントが必要になります。<br><br>Braze で使用する予定の各広告アカウントに対する「Manage ad accounts」権限を持っており、広告アカウントの利用規約に同意していることを確認します。 |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Facebook ページ</a> | 自社のブランドのビジネスマネージャーに関連付けられているアクティブな Facebook ページが必要になります。<br><br>Braze で使用する Facebook ページごとに、「Manage Pages」権限があることを確認します。 |
| Braze REST エンドポイント | [ REST エンドポイント URL][1] を確認してください。API エンドポイントは、Brazeインスタンスのダッシュボード URL と一致します。<br><br> たとえば、ダッシュボード URL が`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` になります。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キーがあることを確認します。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:インスタントフォームでリード広告キャンペーンを作成する

Facebook 広告マネージャから、<a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Facebook リードキャンペーンと Facebook リード獲得広告フォーム</a>を作成します。

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)へのリクエスト時に、メールの住所または電話番号を使用して、ユーザープロファイルを更新または作成できます。このため、リード広告フォームに**メール**または**phone**の**連絡先フィールド**を含めてください。名または姓を収集する場合は、フルネームではなくフォームで別々に収集します。

### ステップ2:Facebook アカウントを Zapier に接続する 

#### ステップ 2a: Zapierで接続方法を選択する

Zapier で [**Apps**] に移動して利用可能なFacebook アプリを検索します。[**Facebook Lead Ads**] または [**Facebook Lead Ads (for Business admins)**] のいずれかを選択します。

Facebook アカウントを Zapier に接続するこの2つの方法の詳細については、以下を参照してください。

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (for Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![][2]{: style="max-width:80%;"}

#### ステップ 2b: Facebook Business Manager でリードアクセスに Zapier を追加する

Facebook Business Manager で、左側のメニューの [**Integrations**] > [**Leads Access**] に移動します。Facebook ページを選択し、[**CRMs**] をクリックします。[CRM] タブで、[**Assign CRMs**] を選択し、[**Zapier**] を追加します。

![][3]{: style="max-width:80%;"}

CRMインテグレーションとしてZapierを割り当てるステップについては、FaceBookの<a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">ドキュメント</a>を参照してください。

### ステップ3:Zap を作成する

#### ステップ3a:トリガーの作成 

Facebook アカウントを接続したら、Zap の作成に進むことができます。**トリガー**の場合は、ステップ2での選択に基づいて、[**Facebook Lead Ads**] または [**Facebook Lead Ads (for Business Admins)**] を選択します。 

![][4]{: style="max-width:80%;"}

**Event**では、**New Leads**> **Continue**を選択します。 

![][5]{: style="max-width:80%;"}

Facebook アカウントを選択し、[**Continue**] を選択します。 

![][6]{: style="max-width:80%;"}

以前に作成した Facebook ページとインスタントフォームを選択し、[**Continue**] を選択します。

![][7]{: style="max-width:80%;"}

次に、このトリガーを試します。フォーム出力を検証したら、**選択したレコードで続行**を選択します。

#### ステップ3b:アクションの作成

新しいステップを追加し、** Web hooks by Zapier** を選択します。次に、**Custom Request**を**Event**フィールドに選択し、**Continue**を押します。 

![][8]{: style="max-width:80%;"}

最後に、ペイロードにフィールドを挿入してカスタムリクエストを設定します。次のコードスニペットは、ペイロードの例を示しています。 

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

### ステップ4:Facebook Lead Ads Zap をテストする

このエンドツーエンドをテストするには、Facebook Developer Console で Facebook の Leads Ads Testing Tool を使用します。詳細については、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">テストとトラブルシューティング</a>を参照してください。

## ユーザー識別管理

この統合により、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number)からのメールに基づいて Facebook リードを紐づけることができます。

* メールが既存の1つのユーザープロファイルと一致する場合、Braze は Facebook リードデータを使用してそのプロファイルを更新します。
* 同じメールが設定されているユーザープロファイルが複数ある場合、Braze は更新時に、external ID を持つ最新の更新済みプロファイルを優先します。
* external ID が存在しない場合、Braze は、一致するメールを持つ最新の更新済みプロファイルを優先します。
* 指定されたメールを持つプロファイルが存在しない場合、Braze は新しいプロファイルを作成し、新しいエイリアスユーザープロファイルが作成されます。新しく作成された別名ユーザープロファイルs を識別するには、[`/users/identify`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) を使用します。

{% alert note %}
これらのフィールドが利用可能で、インテグレーションに使用したいプライマリ識別子がある場合は、Brazeへのリクエストの一部として電話番号または外部ID を使用することもできます。これを行うには、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に示すようにリクエストペイロードを変更します。
{% endalert %}

## トラブルシューティング

{% details トリガーとアクションを正常にテストしたため、Zapierのザップを公開できないのはなぜですか? %}
この統合を使用するには、プレミアムアプリs をサポートする<a href="https://zapier.com/app/pricing/" target="_blank">Zapierプラン</a> が必要です。
{% enddetails %}

{% details Facebook リードが Braze に同期されないのはなぜですか? %}
1. 管理者が Facebook ページ、広告アカウント、リードアクセスにアクセスできることを確認します。次に、Zapier でアカウントを再接続します。
2. Facebook で作成したインスタントフォームが、トリガーステップで選択したフォームにマッピングされていることを確認します。 
3. [**Facebook Business Manager**] > [**Integrations**] > [**Lead Access**] に移動して、Zapier を Leads Access に割り当てていることを確認します。
{% enddetails %}

{% details 同じメールが設定されている重複ユーザープロファイルが表示されるのはなぜですか? %}
[ユーザープロファイルライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle) に基づいて、Braze でユーザープロファイルs を作成および管理する独自の方法があります。

内部プロセスによっては、Braze 内での顧客の作成をトリガーするときに、統合によって作成されるユーザープロファイルの競合状態と、ユーザーがシステムから作成された時点に応じて、重複するユーザープロファイルが発生することがあります。Braze では[ユーザープロファイルをマージできます]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)。
{% enddetails %}

{% details Zapier アカウントを持っていません。Facebook Lead Ads Webhook を Braze にトリガーするにはどうすればよいですか? %}
Zapier を使用しておらず、Zapier を使用する予定がない場合は、Facebook から Braze への直接の統合を構築できます。詳細については、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">リード獲得広告のドキュメント</a>を参照してください。

Facebook からリードを取得するには、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">Webhook</a> を使用します。Facebook で Webhook の使用を開始するには、<a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">Webhook のドキュメント</a> を参照してください。

Facebook で Webhook URL を確立したら、チームと協力して、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)にデータを転送するための最適なパスを決定します。Zapier アプローチと同様に、`users/track` エンドポイントから [メールによるリクエスト]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-phone-number)を実行することをお勧めします。
{% enddetails %}

{% alert tip %}
トラブルシューティングのヒントについては、Zapierの<a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Facebook リードのトラブルシューティングガイド</a>を参照してください。
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