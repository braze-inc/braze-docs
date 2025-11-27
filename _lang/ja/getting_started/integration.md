---
nav_title: 統合
article_title: オンボーディング統合の概要
page_order: 8
page_type: reference
description: "この参考記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"

---

# 統合

> Braze との統合は価値あるプロセスだ。でも、お客様は賢いです。お客様は**ここに**います。明らかに、お客様はすでにそれを知っています。しかし、おそらくお客様が知らないことは、お客様と開発者が一緒に旅に出ようとしているということだ。この旅には、技術的な専門知識、戦略的な計画、そして両者間の調整に役立つ一貫したコミュニケーションが必要です。

{% alert note %}
なお、この記事の内容はメールには当てはまりません。[メール設定]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/)のセクションで確認してください。
{% endalert %}

## 統合プロセスの技術的側面

こんなふうに思うかもしれません。「うちの開発者は魔法のようだ。彼らは何でもできるから、いつも任せているんだ！」。そして、彼らはおそらく実際にそうであり、おそらくそれができるでしょう!しかし、彼らが舞台裏で何をしているのか、あなたが知らない理由はありません。実際、彼らが「API キーと API エンドポイントを送ってもらえますか？」と言ったときに、いつ情報を持って飛び込むべきか、何を探すべきかを知っていれば、プロセス全体の助けになるでしょう。

では、Braze をお客様のアプリやサイトに統合するとき、彼らは何をしているのでしょうか？聞いていただけて嬉しいです！

### ステップ1: 彼らは Braze SDK を実装します。

Braze SDK (ソフトウェア開発キット) は、アプリまたはサイトとの間で情報を送受信するためのものです。お客様のエンジニアは、本質的に私たちのアプリを結びつけています。そのためには、いくつかの重要な情報が必要となります。

* [API キー]({{site.baseurl}}/api/api_key/)
* [SDK エンドポイント]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * Brazeはカスタムエンドポイントを提供しなくなったので、定義済みの SDK エンドポイントを使用します。既存のカスタムエンドポイントが与えられている場合は、こちらで [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup)、[iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift)、[Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk) 統合の設定ステップを確認できます。

この情報を直接相手に渡すか、そのユーザーのアカウントを作成して Braze にアクセスできるようにすることもできます。 

{% alert warning %}
お客様と開発者が Braze 上で会社の認証情報を知らずに、または意図せずに変更しないようにしてください。実装プロセス中に問題が発生したり、1人または複数のユーザーがアカウントをロックされたりする可能性があるためです。
{% endalert %}

### ステップ 2: ご希望のメッセージングチャネルを実装する

Braze にはユーザーと連絡を取るための多くのオプションがありますが、どのオプションも自分の望むように動作させるためには独自の設定や調整が必要です。ここでエンジニアとのコミュニケーションが重要になります。

実装が効率的かつ適切な順序で行われるように、どのチャネルを使いたいかを必ず開発者に伝えてください。

| Channel | 詳細 |
|---|---|
| アプリ内メッセージ | SDK の実装とチャネル固有のステップが必要である。 |
| プッシュ | メッセージング認証情報とプッシュトークンに関する適切な処理を提供するSDK実装が必要である。 |
| メール | これはまったく別のプロセスである。統合の詳細については、[Eメール設定]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/)セクションをチェックする。 |
| コンテンツカードによって促進された | [コンテンツカードを]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)始めるには、Brazeカスタマーサクセスマネージャーに連絡する。 |
| SMS/MMS | 統合の詳細については、[SMSセットアップの]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/)セクションを参照のこと。 |
| Webhook | SDKの実装とチャンネル固有のステップが必要である。 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Braze を使えば、各チャネルでアクセスしやすいメッセージングキャンペーンを作成できます。開発者と協力して、実装においてアクセシビリティ基準を満たすようにしてください。
{% endalert %}

### ステップ 3: データを設定する

Brazeは1つの機能しかないのではありません。これは、単にメールを送信したり、プッシュを送信したりするだけのものではありません。これは、すべてのユーザーと顧客にとってユニークで、パーソナライズされたカスタマージャーニーを創造するためのものです。カスタマージャーニーは、アプリやサイト内での行動に基づいており、その内容を定義することができます！開発者の次の仕事は、アプリやサイト内で行われたアクションが Braze によって検出されるようにすることです。

では、彼らにこの情報を提供するにはどうすればいいのでしょうか?

1. マーケティングチームと協力して、キャンペーン、目標、属性、追跡が必要なイベントを定義します。それらのユースケースを定義し、チームと共有します。
2. カスタムデータ要件 ([カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)、[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)など) を定義します。
3. そこから、そのデータがどのように追跡されるべきか (SDKを通じてトリガーされるなど) について議論します。
4. 必要な[ワークスペース]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)の数を定義します。エンジニアは、これらのワークスペースを[テストおよび設定する]({{site.baseurl}}/user_guide/getting_started/workspaces/)方法を知っておく必要があります。

これらの情報をすべて発見したら、エンジニアと共有します。彼らはその情報をもとに、あなたの[カスタムデータ]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/)を実装します。[ユーザーをインポートする]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/)必要さえある場合があります。また、[イベントの命名規則]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/)にも注意する必要があります。

### ステップ 4: 希望に応じてカスタマイズしてくれる

API トリガーによる起動や Connected Content などが必要な場合は、Braze の担当者と開発者の両方と話し合い、アプリや Braze の外部にあるデータをメッセージに取り込めるようにします。

### ステップ 5: 二人とも実装のQAを行う

エンジニアと協力して、すべてが機能していることを確認します。[テストメッセージ]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/)を送信し、[Android 用のテストアプリ]({{site.baseurl}}/developer_guide/references/?tab=android)と [iOS 用のテストアプリ]({{site.baseurl}}/developer_guide/references/?tab=swift)を使用して、送信を開始する前にすべてのボックスを確認します。

[Android や FireOS との統合をテスト]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration)したり、[iOS のプッシュ]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing/)をテストするための具体的なステップまでもあります。

## 実装後

実装のゴールラインは、1度に100万件のメッセージを送信するためのゴーサインでもないことに注意してください。100万件のプッシュを送信すると、すべての顧客が同じリンクを同時にクリックした場合、アプリが破損する可能性があります。[**送信**] ボタンをクリックする前に、Braze からのリクエストを処理するための内部設定のキャパシティについて話し合うことをお勧めします。そして、それに基づいて[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting)を設定できます。

![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Braze を使い慣れたら、Braze Firebrand になることを検討しましょう！Braze のカスタマーエンゲージメントコミュニティである Braze Firebrands では、カスタマーエクスペリエンスとマーケティングを近代化するために Braze を使用している有力者のコミュニティを構築しています。もっと詳しく知りたいですか？[今すぐ参加しましょう](https://brazefirebrands.splashthat.com/)。
