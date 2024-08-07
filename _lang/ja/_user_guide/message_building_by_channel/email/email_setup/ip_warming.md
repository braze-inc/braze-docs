---
nav_title: IP ウォームアップ
article_title: IP ウォームアップ
page_order: 1
page_type: reference
description: "この参照記事では、IPの温暖化とベストプラクティスに関するトピックについて説明します。"
channel: email

---

# IP ウォームアップ

> IP ウォームアップは、専用 IP アドレスからのメッセージ受信に E メール受信プロバイダを使用する方法です。これは、E メールサービスプロバイダー(ESP) と標準的なプラクティスを含むE メール送信の非常に重要な部分であり、メッセージが一貫して高いレートで宛先の受信トレイに到達することを確認するために、Braze で実行されます。

IP ウォーミングは、インターネットサービスプロバイダ(ISP)との良好な評価を確立するために設計されています。新しい IP アドレスを使用して E メールを送信するたびに、ISP はプログラムでこれらの E メールを監視して、スパムの送信に使用されていないことを確認します。

## IPを温める時間がなければどうしますか?

**IPウォーミングが必要です。**IP を適切にウォームアップせず、メールのパターンが疑わしい場合は、メールの配信速度が大幅に遅くなったり遅くなったりすることがあります。ドメインまたはIP もISP によってブロックされる可能性があります。その結果、ユーザーのメールは代わりにユーザーの受信トレイのスパムフォルダーに直接送信されます。そのため、IP を適切に温めることが重要です。

ISPは、スパムの疑いが生じた場合、ユーザーを保護できるように電子メールの配信を制限します。たとえば、100,000 人のユーザーに送信する場合、ISP は最初の1 時間で5000 人のユーザーにのみメールを配信することができます。次に、ISPは、オープンレート、クリック率、登録解除、スパムレポートなどのエンゲージメントの測定を監視します。そのため、大量のスパムレポートが発生した場合、ユーザの受信トレイに送信するのではなく、その送信の残りの部分をスパムフォルダに送信することを選択する可能性があります。 

エンゲージメントが適度な場合は、メールをスロットリングして、より確実にメールがスパムであるかどうかを判断するために、より多くのエンゲージメントデータを収集することができます。Eメールのエンゲージメントメトリクスが非常に高い場合、Eメールのスロットリングが完全に停止することがあります。このデータを使用して、メールレピュテーションを作成し、最終的にメールが自動的にスパムにフィルタリングされるかどうかを決定します。

ドメインまたはIP がISP によってブロックされている場合、[Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) のメッセージログには、これらのISP にアピールし、これらのリストから除外するために訪問するWeb サイトに関する情報が含まれます。

## IP温暖化スケジュール

配信可能性をサポートするために、このIP ウォーミングスケジュールに厳密に従うことを強くお勧めします。また、一貫したスケーリングにより配信メトリクスが向上するため、日数をスキップしないことも重要です。

Day | 送信するメールの数
----|--------------------------|
1 | 50
2 | 100
3 | 500
4 | 1,000
5 | 5,000
6 | 10,000
7 | 20,000
8 | 40,000
9 | 70,000
10 | 100,000
11 | 150,000
12 | 250,000
13 | 400,000
14 | 600,000
15 | 1,000,000
16 | 2,000,000
17 | 4,000,000
18+ | 1 日2 回、希望するボリュームまで

送付ピークまでのウォーミングアップをお勧めします。つまり、通常は1日に200万通のメールを送信するが、季節的な期間に700万通を送信する予定の場合、その"peak"送信は、ウォームアップする必要があるものです。

ウォーミングが完了し、希望の1日の体積に達したら、その体積を毎日維持するようにします。ある程度の変動が予想されますが、望ましいボリュームに到達すると、週に1回大量送出を行うだけで、配信メトリクスと送信者の評判に悪影響を与える可能性があります。 

{% alert important %}
ほとんどのISP は、30 日間のみレピュテーションデータを保存します。メッセージを送信せずに1ヶ月経過した場合は、IPウォーミングプロセスを繰り返す必要があります。
{% endalert %}

## ウォーミング時の送信制限方法

組み込みのユーザー制限機能は、IP アドレスのウォームアップに役立つ便利なツールです。キャンペーンの作成時に必要なメッセージングセグメントを選択した後、[Target Users]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) ステップで**Advanced Options** ドロップダウンを選択してユーザーを制限します。温暖化スケジュールが続くと、この制限を徐々に引き上げて、送信するメールの量を増やすことができます。

![][18]

## サブドメインのセグメンテーション

多くのISPおよび電子メールアクセスプロバイダは、IPアドレスのレピュテーションによってのみフィルタリングされなくなりました。現在では、これらのフィルタリング技術は、ドメインベースのレピュテーションにも対応しています。つまり、フィルタは、送信者のドメインに関連付けられているすべてのデータを調べ、IP アドレスをシングルアウトするだけではありません。このため、メールIP のウォームアップに加えて、マーケティング、トランザクション、および企業メール用に別々のドメインまたはサブドメインを持つことをお勧めします。 

{% alert important %}
サブドメインのセグメンテーションは、大量の送信者にとって特に重要である。これらの送信者は、アカウントを設定してこの慣行を遵守していることを確認する際に、ブレーズ担当者と連携する必要があります。
{% endalert %}

企業メールが最上位ドメインを介して送信され、マーケティングメールとトランザクションメールが異なるドメインまたはサブドメインを介して送信されるように、ドメインをセグメンテーションすることをお勧めします。

## ベストプラクティス

IP温暖化ではない結果は、IP温暖化のベストプラクティスに従えば避けることができます。

### 少量のメール送信から始める

毎日送る金額を少しずつ増やしていきます。突然の大量メールキャンペーンは、ISPによる最も懐疑的なものと見なされている。そのため、まず少量のメールを送信し、最終的に送信する予定のメールの量に向けて徐々にスケールする必要があります。ボリュームに関係なく、IP を安全にウォーミングアップすることをお勧めします。[IPウォーミングスケジュール](#ip-warming-schedule)を参照してください。

### 導入コンテンツを持つ

最初のコンテンツが非常に魅力的であることを確認し、ユーザーがメールをクリック、開き、エンゲージする可能性を最大化します。IPを温めるときは、常に無差別の爆風よりも的を絞ったメールを好む。

### 一貫した送信ケイデンスを設定する

IP ウォームアップが完了したら、送信ケイデンスを作成し、1 日または数日間にわたってメールを分散させるようにします。できるだけ一貫したスケジュールを作成することで、IP のクールダウンを防ぐことができます。これは、送信ボリュームが数日以上停止したり大幅に減少したりした場合に発生する可能性があります。 

特定の時間に大量送出を送信するのではなく、送信をより長い時間枠に広げるには、私たちの[IPウォーミングスケジュール](#ip-warming-schedules)を参照してください。

### メールリストをクリーンアップする

メールリストがクリーンで、古いメールや未確認のメールがないことを確認します。[CASL-とCAN-SPAM-準拠][40]の両方であることを確認するのが理想的です。

### 送信者の評価を監視する

IP ウォーミングプロセスを実行する場合は、IP ウォーミングプロセスを実行する際に送信者のレピュテーションを注意深く監視してください。これらの特定のメトリクスは、以下を監視するために重要です。
- **バウンスレート:**キャンペーンが3～5%を超えてバウンドする場合は、[清潔に保つ]のガイドラインに従って、リストの清潔度を評価する必要があります。Eメールリスト衛生の重要性][43]の記事。さらに、[sunset policy][46] を実装して、電子メールの未送信または休止メールアドレスの電子メール送信を停止することを検討する必要があります。
- **スパムレポート:**いずれかのキャンペーンが0.08% を超える割合でスパムとして報告された場合は、送信中のコンテンツを再評価し、興味のあるユーザーを対象としていることを確認し、興味のあるユーザーの興味をそそるためにメールが適切に表現されていることを確認する必要があります。
- **送信者評価スコア:**ReturnPathの[SenderScore][44]とCiscoのIronPort[SenderBase][45]は、レピュテーションがどのように進んでいるかをチェックするのに役立つリソースです。

{% alert tip %}
IP を温めるために、[インテリジェントタイミング]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/) を使用しないことをお勧めします。IP ウォーミングキャンペーンは、最初に送信するキャンペーンの一部であるため、Braze は最適な送信時間を計算するのに十分な情報をユーザーに提供しません。この場合、インテリジェントタイミングを持つすべてのメッセージはデフォルトでフォールバック時間になり、同時に送信されます。
{% endalert %}

[18]: {% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %}
[40]: {{site.baseurl}}/user_guide/onboarding_with_braze/spam_regulations/
[43]: https://www.braze.com/blog/email-list-hygiene/
[44]: https://senderscore.org/
[45]: http://www.senderbase.org/
[46]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/
