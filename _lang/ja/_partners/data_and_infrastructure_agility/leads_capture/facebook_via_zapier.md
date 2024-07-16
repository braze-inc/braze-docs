---
nav_title: Facebook Lead Ads via Zapier
article_title:Zapierを使ったFacebookリード広告
description:"この参考記事では、FacebookからBrazeへのリードデータの転送を自動化し、リアルタイムのエンゲージメントとパーソナライズされたフォローアップアクションを可能にする、Zapierを介したBrazeとFacebookリード広告の統合について概説している。"
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag:Partner

---

# Zapier統合によるFacebookリード広告

> <a href="https://zapier.com/" target="_blank">Zapierを</a>介したFacebookリード広告の統合により、FacebookからBrazeにリードをインポートし、リードが捕捉されたときにカスタムイベントを追跡することができる。 

Facebookリード広告は、企業がFacebookで直接リード情報を収集できる広告フォーマットだ。これらの広告は、リードジェネレーションのプロセスを簡単かつシームレスにするためにデザインされている。ZapierインテグレーションとBrazeを活用することで、FacebookからBrazeへのリードデータの転送を自動化し、リアルタイムのエンゲージメントとパーソナライズされたフォローアップアクションを可能にする。 

## 前提条件

| 要件 | 説明 |
|---|---|
| Zapierアカウント | このパートナーシップを利用するには、Zapierアカウントが必要だ。この統合には、<a href="https://zapier.com/app/pricing/" target="_blank">プレミアムZapierアプリを</a>使用する必要があるため、Zapierプランがプレミアムアプリにアクセスできることを確認すること。 |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">フェイスブック・リード・アクセス</a> | Facebook Leadsへのアクセスは、Brazeで使用する予定の広告アカウントごとに必要である。 |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">フェイスブック・ビジネス・マネージャー</a> | この統合の一環として、ブランドのFacebook資産（広告アカウント、ページ、アプリなど）を一元管理するツールであるFacebookビジネスマネージャーを使用する。 |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">フェイスブック広告アカウント</a> | あなたのブランドのビジネスマネージャーと結びついたアクティブなFacebook広告アカウントが必要だ。<br><br>Brazeで使用する予定の各広告アカウントの「広告アカウントのマネージャー」権限があり、広告アカウントの利用規約に同意していることを確認する。 |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">フェイスブックページ</a> | あなたのブランドのビジネスマネージャーと結びついたアクティブなFacebookページが必要だ。<br><br>Brazeで使用する予定の各Facebookページの "Manage Pages "権限があることを確認する。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURLを][1]確認しておくこと。APIエンドポイントがBrazeインスタンスのダッシュボードURLと一致する。<br><br> 例えば、ダッシュボードのURLが`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` となる。 |
| Braze REST API キー | `users.track` の権限を持つREST APIキーを持っていることを確認する。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:インスタントフォームでリード広告キャンペーンを作成する

Facebook広告マネージャーから、<a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">FacebookリードキャンペーンとFacebookリード広告フォームを</a>作成する。

ユーザープロファイルを更新または作成するために[`/users/track` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)リクエストを行う際には、メール アドレスまたは電話番号のいずれかを使用することができる。そのため、リード広告のフォームに**メールや** **電話の** **コンタクトフィールドを**設ける。名や姓を集める場合は、フルネームを使うのではなく、フォームの中で別々に集める。

### ステップ2:FacebookアカウントをZapierに接続する 

#### ステップ 2a: Zapierで接続方法を選択する。

Zapierの「**Apps**」で、利用可能なFacebookアプリを検索する。**Facebookリード広告**または**Facebookリード広告（Business管理者向け**）のいずれかを選択する。

FacebookアカウントをZapierに接続するこれら2つの方法の詳細については、以下を参照のこと：

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebookリード広告（企業管理者向け）</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">フェイスブック・リード広告</a>

![][2]{: style="max-width:80%;"}

#### ステップ 2b: FacebookビジネスマネージャーのリードアクセスにZapierを追加する

Facebook Businessマネージャーで、左側のメニューから**Integrations**>**Leads Accessに**進む。Facebookページを選択し、**CRMを**クリックする。CRMタブで、**Assign CRMsを**選択し、**Zapierを**追加する。

![][3]{: style="max-width:80%;"}

CRMインテグレーションとしてZapierを割り当てるステップについては、Facebookのドキュメントを参照のこと。

### ステップ3:ザップを作成する

#### ステップ3a：トリガーを作成する 

Facebookアカウントとの接続が完了したら、Zapの作成に進むことができる。**トリガーには**、ステップ2で選択した**Facebook Lead Ads**または**Facebook Lead Ads (for Business Admins)**を選択する。 

![][4]{: style="max-width:80%;"}

**イベントについては**、「**New Leads（新規リード**）」＞「**Continue（続行**）」を選択する。 

![][5]{: style="max-width:80%;"}

Facebookアカウントを選択し、**Continue（続行**）する。 

![][6]{: style="max-width:80%;"}

Facebookページと以前に作成したインスタントフォームを選択し、**Continue（続行**）する。

![][7]{: style="max-width:80%;"}

次に、このトリガーをテストする。フォームの出力を検証したら、**Continue with selected recordを**選択する。

#### ステップ3b：アクションを作成する

新しいステップを追加し、**Webhooks by Zapierを**選択する。次に、「**イベント」**フィールドで「**カスタムリクエスト**」を選択し、「**続行**」をクリックする。 

![][8]{: style="max-width:80%;"}

最後に、ペイロードにフィールドを挿入して、カスタムリクエストを設定する。次のコード・スニペットは、ペイロードの例を示している。 

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

これがZapierでの例だ：

![][9]{: style="max-width:80%;"}

Webhookを設定したら、**Continue and testを**選択する。テストが成功すれば、Zapを公開することができる。

### ステップ 4:Facebookリード広告のザップをテストする

このエンドツーエンドのテストを行うには、Facebook Developer ConsoleでFacebookのLeads Ads Testing Toolを使用する。詳しくは、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">テストとトラブルシューティングを</a>参照のこと。

## ユーザーIDマネージャー

この統合により、[`/users/track` エンドポイントを通じて]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number)、Facebookリードのメール属性を設定することができる。

* メールが既存のユーザープロファイルと一致する場合、BrazeはFacebookのリードデータでプロファイルを更新する。
* 同じメールを持つユーザープロファイルが複数ある場合、Brazeは外部IDを持つ最も新しく更新されたプロファイルを優先して更新する。
* 外部IDが存在しない場合、Brazeは一致するメールを持つ最新の更新プロファイルを優先する。
* 提供されたメールのプロファイルが存在しない場合、Brazeは新しいプロファイルを作成し、新しいエイリアスユーザープロファイルを作成する。新しく作成されたエイリアス・ユーザー・プロファイルを識別するには、[`/users/identify` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)使用する。

{% alert note %}
これらのフィールドが利用可能で、統合に必要な主要識別子であれば、Brazeへのリクエストの一部として電話番号や外部IDを使用することもできる。そのためには、[`/users/track` のエンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)示されているように、リクエストのペイロードを修正する。
{% endalert %}

## トラブルシューティング

{% details I tested the Trigger and Action successfully, so why am I unable to publish my Zapier Zap? %}
この統合を使用するには、プレミアムアプリをサポートする<a href="https://zapier.com/app/pricing/" target="_blank">Zapierプランを持って</a>いる必要がある。
{% enddetails %}

{% details Why aren’t Facebook leads syncing to Braze? %}
1. Facebookページ、広告アカウント、リードの管理者アクセス権を持っていることを確認する。その後、Zapierでアカウントを再接続する。
2. Facebookで作成したインスタントフォームが、トリガーステップで選択したフォームにマッピングされていることを確認する。 
3. **Facebook Business Manager**>**Integrations**>**Lead Accessに**アクセスして、ZapierをLeads Accessに割り当てたことを確認する。
{% enddetails %}

{% details Why am I seeing duplicate user profiles with the same email? %}
ユーザープロファイルの[ライフサイクルに]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle)基づき、Brazeでユーザープロファイルを作成・管理する独自の方法がある。

内部プロセスやBraze内で顧客作成のトリガーとなるタイミングによっては、統合によって作成されるユーザープロファイルと、お客様のシステムから作成されるユーザープロファイルの競合により、ユーザープロファイルが重複する場合がある。Brazeで[ユーザープロファイルを統合]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)できる。
{% enddetails %}

{% details I don’t have a Zapier account. How can I trigger Facebook Lead Ads webhooks into Braze? %}
Zapierを使用しておらず、使用する予定もない場合は、FacebookからBrazeに直接統合を構築することができる。詳しくは<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">Lead Adsのドキュメントを</a>参照のこと。

Facebookからリードを取得するには、<a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">Webhookを</a>使用する。FacebookでWebhookを使い始めるには、<a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">Webhooksドキュメントを</a>参照のこと。

FacebookでWebhooks URLを確立した後、チームと協力してデータを[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に転送する最適なパスを決定する。Zapierのアプローチと同様に、`users/track` エンドポイントを通して[メールでリクエスト]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-phone-number)することをお勧めする。
{% enddetails %}

{% alert tip %}
トラブルシューティングのヒントについては、Zapierの<a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Facebookリードのトラブルシューティングガイドを</a>参照のこと。
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