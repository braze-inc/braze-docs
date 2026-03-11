---
nav_title: 配信センター
article_title: 配信センター
alias: "/deliverability_center/"
page_order: 4
description: "このリファレンス記事では、配信センターの設定方法について説明します。この機能を使用すると、マーケターはメール送信ドメインと IP の信頼度を表示して、メールの配信到達性を把握できます。"
channel:
  - email

---

# 配信センター

> 配信センターは、送信メールのデータを追跡して送信ドメインに関するデータを収集する [Google Postmaster Tools](https://www.gmail.com/postmaster/) をサポートすることにより、メールのパフォーマンスに関してより多くのインサイトを提供します。

メールの配信到達性はキャンペーン成功の中核です。Braze ダッシュボードの配信センターを使用すると、**IP の信頼度**または**配信エラー**別にドメインを表示し、メールの配信到達性に関する潜在的な問題を検出してトラブルシューティングを行うことができます。 

配信センターにアクセスするには、ワークスペースに対して「キャンペーン、キャンバス、カード、セグメント、メディアライブラリーへのアクセス」および「使用状況データの表示」[のレガシーユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions)、または以下のドロップダウンにある[詳細権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions)が必要だ。

{% details User permissions for the Deliverability Center %}

{% multi_lang_include deprecations/user_permissions.md %}

- キャンペーンを表示
- キャンペーンを編集
- キャンペーンをアーカイブ
- キャンバスを表示
- キャンバスを編集
-  個のキャンバス 
- フリークエンシーキャップルールを表示
- フリークエンシーキャップルールを編集
- メッセージの優先順位付けを表示
- メッセージの優先順位付けを編集
- コンテンツブロックを表示
- フィーチャーフラグを表示
- フィーチャーフラグを編集
- フィーチャーフラグをアーカイブ
- セグメントを表示
- セグメントの編集
- IAM テンプレートを表示
- IAM テンプレートを編集
- IAM テンプレートをアーカイブ
- メールテンプレートを表示
- メールテンプレートを編集
- メールテンプレートをアーカイブ
- Webhook テンプレートを表示
- Webhook テンプレートを編集
- Webhook テンプレートをアーカイブ
- リンクテンプレートを表示
- リンクテンプレートを編集
- メディアライブラリアセットを表示
- メディアライブラリアセットを編集
- メディアライブラリアセットを削除
- 場所を表示
- 場所を編集
- アーカイブ場所
- プロモーションコードを見る
- プロモーションコードを編集する
- 輸出促進コード
- ユーザー設定センターを表示
- ユーザー設定センターを編集
- レポートを見る
- レポートを編集する
- 利用状況データを表示

{% enddetails %}

## Google Postmaster アカウントの設定

配信センターに接続するには、Google Postmaster Tools のアカウントを設定する必要があります。仕事用または個人用のGmailアカウントを使って、Google Postmasterを設定できる。 

1. [Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1) ダッシュボードに移動します。
2. 右下の<i class="fas fa-plus-circle"></i> プラスアイコンを選択する。
3. ルートドメインまたはサブドメインを入力してメールを認証する。ルートドメインを追加して認証する場合、これにより認証がサブドメインにも適用される。例えば、を検証`braze.com`しておけば、後でやその他のサブドメイン`demo.braze.com`を追加する際、それらを個別に検証する必要がなくなる。

{% alert important %}
TXTレコードは、Braze経由で使用しているサブドメインではなく、親ドメインに関連付けられていることを確認せよ。
{% endalert %}

{: start="4"}
4. Googleは、ドメインのDNSに直接追加できるTXTレコードを生成する。これは通常、DNS の管理者が所有します。特定の DNS の更新方法に関する情報とガイダンスについては、「[ドメインの所有権を証明する （ドメインホスト別の手順）](https://support.google.com/a/topic/1409901)」を参照してください。
5. [**次へ**] を選択します。<br>![メール認証用の例示ドメイン「demo.braze.com」]({% image_buster /assets/img_archive/domain_authentication.png %})
6. TXT レコードが DNS に追加されたら、Google Postmaster Tools ダッシュボードに戻り、[**検証**] を選択します。このステップでドメインの所有権を確認する。これにより、PostmasterアカウントでGmailの配信状況指標にアクセスできるようになる。<br> ![ドメイン「demo.braze.com」の所有権を確認するためのプロンプト。]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert note %}
サブドメインが Google Postmaster の配信センターに含まれていない場合、親ドメインのみを Google Postmaster に追加したことが原因の可能性があります。親ドメインがGoogle Postmasterで確認された後、サブドメインを追加できる。サブドメインは自動的に確認される。このプロセスにより、Google はサブドメインレベルの指標をレポートできるようになり、その指標を Braze の配信センターに取り込むことができます。
{% endalert %}

## Google Postmaster を連携する

配信センターを設定する前に、ドメインが [Gmail Postmaster Tools に追加](https://support.google.com/mail/answer/9981691?hl=en)されていることを確認します。

次の手順に従って、Google Postmaster と連携し、配信センターを設定します。

1. [**分析**] > **[メールパフォーマンス**] に移動します。
2. [**配信センター**] タブを選択します。<br>![Google Postmasterと接続されていない配信センター。]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. [**Google Postmaster との接続**] を選択します。 
4. Google アカウントを選択し、[**許可**] を選択して、Postmaster Tools に登録されているドメインのメールトラフィック指標の表示を Braze に許可します。 

認証済みドメインは配信状況センターに表示される。 

![Google Postmaster向けに認証済みのドメインが2つある。評判は中程度と低程度だ。]({% image_buster /assets/img_archive/deliverability_center2.png %})

また、Braze ダッシュボードで [**パートナー連携**] > [**テクノロジーパートナー**] > [**Google Postmaster**] に移動して、Google Postmaster にアクセスすることもできます。連携後、Braze は過去 30 日間の信頼度とエラーのデータを取得します。データはすぐには利用できない場合があり、入力されるまで数分かかる場合があります。

### 指標と定義

次の指標と定義は、Google Postmaster Tools に適用されます。

#### IP の信頼度 

IP の信頼度の評価を解釈するには、次の表を参照してください。

| 評判評価 | 定義 |
| ----- | ---------- |
| 高 | スパムの苦情が少ない（ユーザーが「スパム」ボタンをクリックするなど）実績がある。 |
| 中/フェア | ポジティブなエンゲージメントを生み出すことで知られているが、時折スパムからの苦情も受ける。このドメインからのメールの大半は受信トレイに届く。ただし、スパム苦情が増加した場合は例外だ。 |
| 低 | 定期的にスパムの苦情が多いことで知られている。この差出人からのメールは、おそらくスパムフィルターによって迷惑メールフォルダに振り分けられるだろう。 |
| 悪い | スパムに関する苦情を高率で受信した履歴があります。このドメインからのメールは、ほぼ常に接続時に拒否されるか、スパムフィルターに振り分けられる。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### ドメイン信頼度 

次の表をドメイン信頼度の評価の監視と解釈に役立てて、フィルターによりスパムフォルダーに入れられることを回避してください。

| 評判評価 | 定義 |
| ----- | ---------- |
| 高 | スパムに関する苦情が非常に少ないという優れた実績があります。Gmail の送信者ガイドラインに準拠しています。メールがスパムフォルダに振り分けられることはめったにない。スパム率が非常に低いという優れた追跡レコードがあります。[Gmail の送信者ガイドライン](https://developers.google.com/gmail/markup/registering-with-google)に準拠しています。 |
| 中/フェア | 好意的なエンゲージメントを生み出すことで知られているが、時折、少量のスパム苦情が寄せられることがある。このドメインからのメールの大半は受信トレイに届く（スパムレベルが著しく上昇した場合を除く）。 |
| 低 | 定期的にスパムの苦情を受けることで知られている。この差出人からのメールは、おそらくスパムフィルターによって迷惑メールフォルダに振り分けられるだろう。 |
| 悪い | スパムに関する苦情を高率で受信した履歴があります。このドメインからのメールは、ほぼ常に接続時に拒否されるか、スパムフィルターに振り分けられる。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 認証

認証ダッシュボードを使用して、Sender Policy Framework (SPF)、DomainKeys Identified Mail (DKIM)、および Domain-based Message Authentication, Reporting and Conformance (DMARC) に適合したメールの割合を確認します。

| グラフの種類 | 定義 |
| ----- | ---------- |
| SPF | SPFを試みたドメインからの全メールに対して、SPFを通過したメールの割合を示す。これにより、なりすましメールが除外されます。 |
| DKIM | DKIMを試行したドメインからのすべてのメールに対して、DKIMを通過したメールの割合を示す。 |
| DMARC | SPFまたはDKIMのいずれかを通過したドメインから受信したすべてのメールに対して、DMARCアライメントを通過したメールの割合を示す。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 暗号化

暗号化されているインバウンドトラフィックとアウトバウンドトラフィックの割合を解釈するときには、次の表を参照してください。

| 用語 | 定義 |
| ----- | ---------- |
| TLSインバウンド | そのドメインから受信したすべてのメールに対して、TLSをパスした（Gmailへの）受信メールのパーセンテージを表示する。 |
| TLSアウトバウンド | そのドメインに送信されたすべてのメールに対して、TLS経由で受け入れられた（Gmailからの）送信メールのパーセンテージを示す。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

配信到達性を向上させるためのその他のアイデアについては、[配信到達性の落とし穴とスパムトラップ]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps)を参照してください。メールキャンペーンの送信前に確認する必要がある項目については、[メールのベスト プラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)を必ず参照してください。

## Microsoft Smart Network Data Services (SNDS) の設定

Microsoft がメインのメールボックスプロバイダーである場合、この連携を使用すると Microsoft の信頼度データにアクセスして表示できます。これにより、IP の健全性を監視し、メールの受信状況の判断に役立てることができます。

{% alert important %}
配信センターにデータが表示されない場合は、IP アドレスのリストを添えて[サポート]({{site.baseurl}}/user_guide/administrative/access_braze/support/)にお問い合わせください。
{% endalert %}

![Microsoft SNDSの結果例には、サンプルIP、受信者、RCPTコマンド、データコマンド、フィルター結果、苦情率、トラップメッセージ期間の開始と終了、スパムトラップヒットが含まれる。]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### 指標と定義

次の指標が Microsoft SNDS に適用されます。

#### 受信者

この指標は、IP によって送信されたメッセージの受信者の数を指します。

#### DATA コマンド

この指標は、IP によって送信された DATA コマンドの数を追跡します。DATA コマンドは、メールの送信に使用される SMTP プロトコルの一部です。

#### フィルターを適用した結果

フィルターを適用した結果を解釈するには、次の表を参照してください。 

| 結果: | 定義 |
| ----- | ---------- |
| グリーン | Microsoft のスパムフィルターにより、時間枠の最大 10% がスパムと判断されました。 |
| イエロー | Microsoftのスパムフィルターにより、時間枠の 10% ～ 90% がスパムと判断されました。 |
| 赤 | Microsoft のスパムフィルターにより、時間枠の最大 90% 超がスパムと判断されました。| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 苦情率

これは、アクティビティ期間中に、IP から受信したメッセージに対して Hotmail または Windows Live のユーザーから苦情が寄せられた時間の割合です。ユーザーは、Web ユーザーインターフェイスを介して、ほぼすべてのメッセージを迷惑メールとして報告するオプションを利用できます。 

苦情率を計算するには、苦情の数をメッセージ受信者の数で除算します。  

| 結果: | 定義 |
| ----- | ---------- |
| 0.3%未満 | 理想的な苦情率 |
| 0.3%以上 | サインアッププロセスを確認し、配信停止リンクが機能していることを確認してください。また、そのメールがオーディエンスによりパーソナライズされたかどうかを検討するといい。 |
| 100%以上 | SNDSは、苦情のあった郵便物が配達された日にさかのぼって表示するのではなく、苦情が報告された日のものを表示することに注意されたい。 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### スパムトラップのヒット数

スパムトラップヒットは、「トラップアカウント」に送られたメッセージの数である。トラップアカウントとは、Outlook.com 、いかなるメールも勧誘しないアカウントである。これらのトラップアカウントに送信されたメッセージはスパムとみなされる可能性が高いので、この指標を監視して、この指標が低いことを確認することが重要です。スパムトラップのヒット数が少ないということは、メッセージがこれらのアカウントに送信されず、代わりに実際のアカウントに送信されていることを意味しています。

{% alert tip %}
Brazeで認証済みドメインに関連する記録を探している場合、配信センターにはGoogle PostmasterまたはMicrosoft SNDSからのデータが表示されることに注意せよ。つまり、いずれかのプラットフォームがBrazeと共有できるデータを保持していない可能性が高い。あるいは、一貫したメール配信を維持することも、高い評価につながるのでお勧めする。
{% endalert %}


