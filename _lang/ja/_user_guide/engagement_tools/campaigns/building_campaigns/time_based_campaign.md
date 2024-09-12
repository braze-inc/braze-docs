---
nav_title: キャンペーンの時間ベースの機能
article_title: キャンペーンの時間ベースの機能
page_order: 2
tool: Campaigns
page_type: reference
description: "この参考記事では、スケジュール配信、インテリジェントタイミング、アクションベースの配信など、キャンペーンの時間ベースの機能について説明します。"

---
# キャンペーンの時間ベースの機能

> キャンペーンを利用する際には、時間ベースのスケジュール設定オプションを使用してオーディエンスにリーチできます。これらの時間ベースの機能には、スケジュール配信とアクションベースの配信に設定されたキャンペーンが含まれます。

また、キャンペーン配信の詳細については、 [キャンペーン設定](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)の Braze ラーニングコースもご覧ください。 

## スケジュール配信

このセクションでは、 [スケジュール配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/) キャンペーンの時間ベースのスケジュール設定と配信オプションについて説明します。

### 指定した時刻に送信

| 定義 | タイムゾーン |
| ---------- | --------- |
| 指定した日付の指定した時間にメッセージを送信する。 | 会社のタイムゾーン |
{: .reset-td-br-1 .reset-td-br-2}

![2021年7月13日午前9時から1回送信する「指定時間に送信」オプションを選択したキャンペーン。][2]

### インテリジェントタイミング

| 定義 | タイムゾーン |
| ---------- | --------- |
| ユーザーの最適な時間各ユーザーは、エンゲージする可能性が最も高い時刻にキャンペーンを受け取ります。詳しくは[インテリジェント・タイミングを]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/)ご覧いただきたい。 | [フォールバックとして]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/#fallback-options)特定の時間を選択した場合、これはユーザーの現地時間で送信される。 |
{: .reset-td-br-1 .reset-td-br-2}

![2021年7月13日の最適な時刻に1回送信し、最適な時刻を計算するのに十分なデータがプロファイルにないユーザーのために午前9時のフォールバック時刻をカスタム設定する「インテリジェントタイミング」オプションを選択したキャンペーン。][3]

### ユーザーのローカルタイムゾーンにあわせてキャンペーンを送信

| 定義 | タイムゾーン |
| ---------- | --------- |
| ユーザーの[タイムゾーンに]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery)基づいたセグメントへのメッセージ配信を可能にする。 | ユーザーの現地時間。ユーザーのタイムゾーンが設定されていない場合、これは会社のタイムゾーンにフォールバックする。 |
{: .reset-td-br-1 .reset-td-br-2}

![指定時間に送信」オプションを選択したキャンペーンで、「ローカルタイムゾーンのユーザーにキャンペーンを送信」チェックボックスを選択し、2021年7月13日午前9時から1回送信する。][4]

### ユーザーがキャンペーンを再度受信できるようにする

| 定義 | タイムゾーン |
| ---------- | --------- |
| ユーザーがこのキャンペーンでメッセージを受け取った後、再びキャンペーンを受け取る資格を得るタイミングを指定する。[詳細はこちら]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/#campaigns)。 | 該当なし |
{: .reset-td-br-1 .reset-td-br-2}

![1週間後に「ユーザーがキャンペーンを受け取る再資格になることを許可する」チェックボックスが選択されたキャンペーン。][5]

## アクションベースの配信

このセクションでは、 [アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/)キャンペーンのスケジュール、遅延、および配信オプションについて説明します。

### スケジュールの遅延

{% alert important %}
遅延時間を選択する際に、 [キャンペーン期間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-4-assign-duration)よりも長い遅延を設定すると、ユーザーはキャンペーンを受け取れないことに注意してください。
{% endalert %}

#### キャンペーンをすぐに送信

| 定義 | タイムゾーン |
| ---------- | --------- |
| ユーザーがトリガーアクションを実行した直後にメッセージを送信する。 | 該当なし |
{: .reset-td-br-1 .reset-td-br-2}

![スケジュール遅延は、トリガーイベントが発生した直後にキャンペーンを送信するように設定される。][6]

#### X日後にキャンペーンを送信

| 定義 | タイムゾーン |
| ---------- | --------- |
| 遅延後にメッセージを送信する。遅延は秒、分、時間、日、週単位で指定できる。 | 該当なし |
{: .reset-td-br-1 .reset-td-br-2}

![スケジュール遅延は、トリガーイベントが発生してから1日後にキャンペーンを送信するように設定されている。][7]

#### 次の\[曜日] X時にキャンペーンを送る

| 定義 | タイムゾーン |
| ---------- | --------- |
| 指定した曜日の指定した時間にメッセージを送信する。 | **ユーザーの現地時間か** **会社時間かを**選択する**。** |
{: .reset-td-br-1 .reset-td-br-2}

たとえば、「次の土曜日の午後 3 時 15 分に送信」を選択するとします。ユーザーが土曜日にトリガーイベントを実行すると、そのメッセージは 7 日後の次の土曜日に受信されます。金曜日に入ると、次の土曜日は 1 日後になります。

![][8]

#### X 暦日で Y 時間に送信する

| 定義 | タイムゾーン |
| ---------- | --------- |
| 指定した日数、指定した時間にメッセージを送る。 | **ユーザーの現地時間か** **会社時間かを**選択する**。** |
{: .reset-td-br-1 .reset-td-br-2}

Braze は遅延を `day of the week` + `calendar days` として計算し、`time` を加算します。たとえば、ユーザーが月曜日の午後 9 時にトリガーイベントを実行し、スケジュールの遅延が「1 日後の午前 9 時にキャンペーンを送信する」に設定されているとします。このメッセージは火曜日の午前 9 時に配信されますが、これは Braze が遅延を `Monday` + `1 calendar day` として計算し、`9 am` に加算するためです。

![][9]

### サイレント時間

| 定義 | タイムゾーン |
| ---------- | --------- |
| 指定した時間帯にメッセージが送信されないようにする。クワイエットアワー中にメッセージがトリガーされた場合、メッセージをキャンセルするか、次の利用可能な時間（クワイエットアワーの終了時に送信するなど）に送信するかを選択できる。 | ユーザーの現地時間。ユーザーのタイムゾーンが設定されていない場合、これは会社のタイムゾーンにフォールバックする。 |
{: .reset-td-br-1 .reset-td-br-2}

![クワイエットアワーを有効にしたキャンペーン。この例では、ユーザーの現地時間の午前 12 時から午前 8 時まではメッセージは送信されません。もしメッセージがクワイエットアワー中にトリガーされた場合、メッセージは次の利用可能な時間に送信される。][10]

### ユーザーがキャンペーンを再度受信できるようにする

| 定義 | タイムゾーン |
| ---------- | --------- |
| |このキャンペーンによってユーザーにメッセージが届いた後、そのユーザーが再びキャンペーンを受け取れるように [再有効化]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/#campaigns)することができる時期を指定します。| 該当なし | | 該当なし |
{: .reset-td-br-1 .reset-td-br-2}

![1週間後に「ユーザーがキャンペーンを受け取る再資格になることを許可する」チェックボックスが選択されたキャンペーン。][5]

### グローバルフリークエンシーキャップ

| 定義 | タイムゾーン |
| ---------- | --------- |
| 分、日、週（7日）、月単位で、各ユーザーが一定の期間内にキャンペーンを受け取る回数を制限する。詳しくは、[周波数キャッピングを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping)参照のこと。 | ユーザーの現地時間。ユーザーのタイムゾーンが設定されていない場合、これは会社のタイムゾーンにフォールバックする。 |
{: .reset-td-br-1 .reset-td-br-2}

デフォルトでは、フリークエンシーキャップは新しいキャンバスに対してはオフに切り替わります。フリークエンシーキャップは、キャンバスのエントリ レベルではなく、ステップレベルで適用されます。

フリークエンシーキャップは、24 時間ではなく暦日に基づきます。つまり、1 日に 1 回のみキャンペーンを送信するフリークエンシーキャップルールを設定できますが、ユーザーが現地時間の午後 11 時にメッセージを受信した場合、1 時間後 (翌暦日の深夜) に別のメッセージを受信できます。 

## コンバージョンの期限

| 定義 | タイムゾーン |
| ---------- | --------- |
| ユーザーがキャンペーンを受け取ってから指定されたアクションを実行するまでに、コンバージョンとみなされるまでの最大時間。詳しくは、[コンバージョンイベントを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/)参照のこと。 | 該当なし |
{: .reset-td-br-1 .reset-td-br-2}



[2]: {% image_buster /assets/img_archive/time_designated.png %}
[3]: {% image_buster /assets/img_archive/time_intelligent_timing.png %}
[4]: {% image_buster /assets/img_archive/time_local.png %}
[5]: {% image_buster /assets/img_archive/time_reeligibility.png %}
[6]: {% image_buster /assets/img_archive/time_delay_immediately.png %}
[7]: {% image_buster /assets/img_archive/time_delay_after.png %}
[8]: {% image_buster /assets/img_archive/time_delay_on_the_next.png %}
[9]: {% image_buster /assets/img_archive/time_delay_in.png %}
[10]: {% image_buster /assets/img_archive/time_quiet_hours.png %}
