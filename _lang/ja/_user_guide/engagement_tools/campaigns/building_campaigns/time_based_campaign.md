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
|特定の暦日の指定した時刻にメッセージを送信します。| 会社のタイムゾーン。|
{: .reset-td-br-1 .reset-td-br-2}

![2021 年 7 月 13 日午前 9 時から 1 回送信する、「指定した時刻に送信」オプションを選択したキャンペーン][2]

### インテリジェントタイミング

| 定義 | タイムゾーン |
| ---------- | --------- |
|ユーザーの最適な時間。各ユーザーは、エンゲージする可能性が最も高い時刻にキャンペーンを受け取ります。詳細については、 [インテリジェントタイミング]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/)をご覧ください。| [フォールバック]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/#fallback-options)として特定の時刻を選択した場合、ユーザーの現地時間で送信されます。|
{: .reset-td-br-1 .reset-td-br-2}

![2021 年 7 月 13 日の最適な時刻に 1 回送信するように [インテリジェントタイミング] オプションが選択されたキャンペーンで、最適な時刻を計算するのに十分なデータがプロファイルにないユーザーに対しては、カスタムフォールバック時刻を午前 9 時に設定します。[3]

### ユーザーのローカルタイムゾーンにあわせてキャンペーンを送信

| 定義 | タイムゾーン |
| ---------- | --------- |
|ユーザーの [個々のタイムゾーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery)に基づいてセグメントにメッセージを配信できます。|ユーザーの現地時間。ユーザーのタイムゾーンが設定されていない場合、会社のタイムゾーンに従います。|
{: .reset-td-br-1 .reset-td-br-2}

![「ローカルタイムゾーンのユーザーにキャンペーンを送信する」チェックボックスがオンにされ、2021 年 7 月 13 日午前 9 時から 1 回送信する「指定した時間に送信」オプションが選択されているキャンペーン。][4]

### ユーザーがキャンペーンを再度受信できるようにする

| 定義 | タイムゾーン |
| ---------- | --------- |
|このキャンペーンによってユーザーにメッセージが届いた後、そのユーザーが再びキャンペーンを受け取る資格を再び得ることができる時期を指定します。[詳細情報]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/#campaigns)。| 該当なし |
{: .reset-td-br-1 .reset-td-br-2}

![1週間後に「ユーザーがキャンペーンを再度受信できるようにする」のチェックボックスをオンにしたキャンペーン][5]

## アクションベースの配信

このセクションでは、 [アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/)キャンペーンのスケジュール、遅延、および配信オプションについて説明します。

### スケジュールの遅延

{% alert important %}
遅延時間を選択する際に、 [キャンペーン期間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-4-assign-duration)よりも長い遅延を設定すると、ユーザーはキャンペーンを受け取れないことに注意してください。
{% endalert %}

#### キャンペーンをすぐに送信

| 定義 | タイムゾーン |
| ---------- | --------- |
|ユーザーがトリガーアクションを実行した直後にメッセージを送信します。 | 該当なし |
{: .reset-td-br-1 .reset-td-br-2}

![トリガーイベントが発生したらすぐにキャンペーンを送信するように設定されたスケジュール遅延。][6]

#### X日後にキャンペーンを送信

| 定義 | タイムゾーン |
| ---------- | --------- |
| 遅延後にメッセージを送信します。遅延は、秒、分、時間、日、または週単位で指定できます。| 該当なし |
{: .reset-td-br-1 .reset-td-br-2}

![スケジュールの遅延は、トリガーイベントが発生してから 1 日後にキャンペーンを送信するように設定されています。][7]

#### 次の [曜日] の X 時にキャンペーンを送信する

| 定義 | タイムゾーン |
| ---------- | --------- |
| 次の指定した曜日、選択した時刻にメッセージを送信します。| **ユーザーの現地時間**または**会社の時間**を選択する |
{: .reset-td-br-1 .reset-td-br-2}

たとえば、「次の土曜日の午後 3 時 15 分に送信」を選択するとします。ユーザーが土曜日にトリガーイベントを実行すると、そのメッセージは 7 日後の次の土曜日に受信されます。金曜日に入ると、次の土曜日は 1 日後になります。

![][8]

#### X 暦日で Y 時間に送信する

| 定義 | タイムゾーン |
| ---------- | --------- |
|指定した時刻に特定の日数でメッセージを送信します。| **ユーザーの現地時間**または**会社の時間**を選択する |
{: .reset-td-br-1 .reset-td-br-2}

Braze は遅延を `day of the week` + `calendar days` として計算し、`time` を加算します。たとえば、ユーザーが月曜日の午後 9 時にトリガーイベントを実行し、スケジュールの遅延が「1 日後の午前 9 時にキャンペーンを送信する」に設定されているとします。このメッセージは火曜日の午前 9 時に配信されますが、これは Braze が遅延を `Monday` + `1 calendar day` として計算し、`9 am` に加算するためです。

![][9]

### サイレント時間

| 定義 | タイムゾーン |
| ---------- | --------- |
|指定した時間帯にメッセージが送信されないようにします。通知停止時間中にメッセージがトリガーされた場合は、メッセージをキャンセルするか、次に利用可能な時間 (通知停止時間終了時に送信するなど) に送信するかを選択できます。| ユーザーの現地時間。ユーザーのタイムゾーンが設定されていない場合、会社のタイムゾーンに従います。|
{: .reset-td-br-1 .reset-td-br-2}

![サイレント時間を有効にしたキャンペーン。この例では、ユーザーの現地時間の午前 12 時から午前 8 時まではメッセージは送信されません。メッセージがサイレント時間中にトリガーされた場合、メッセージは次に利用可能な時間に送信されます。[10]

### ユーザーがキャンペーンを再度受信できるようにする

| 定義 | タイムゾーン |
| ---------- | --------- |
|このキャンペーンによってユーザーにメッセージが届いた後、そのユーザーが再びキャンペーンを受け取れるように [再有効化]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/#campaigns)することができる時期を指定します。| 該当なし |
{: .reset-td-br-1 .reset-td-br-2}

![1週間後に「ユーザーがキャンペーンを再度受信できるようにする」のチェックボックスをオンにしたキャンペーン][5]

### グローバルフリークエンシーキャップ

| 定義 | タイムゾーン |
| ---------- | --------- |
| 各ユーザーが特定の期間内にキャンペーンを受け取る回数を制限し、分、日、週(7日)、月単位で測定できます。詳細については、[フリークエンシー キャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping)を参照してください。| ユーザーの現地時間。ユーザーのタイムゾーンが設定されていない場合、会社のタイムゾーンに従います。|
{: .reset-td-br-1 .reset-td-br-2}

デフォルトでは、フリークエンシーキャップは新しいキャンバスに対してはオフに切り替わります。フリークエンシーキャップは、キャンバスのエントリ レベルではなく、ステップレベルで適用されます。

フリークエンシーキャップは、24 時間ではなく暦日に基づきます。つまり、1 日に 1 回のみキャンペーンを送信するフリークエンシーキャップルールを設定できますが、ユーザーが現地時間の午後 11 時にメッセージを受信した場合、1 時間後 (翌暦日の深夜) に別のメッセージを受信できます。 

## コンバージョンの期限

| 定義 | タイムゾーン |
| ---------- | --------- |
| ユーザーがキャンペーンを受信してから、割り当てられたアクションを実行しコンバージョンと見なされるまでに経過する可能性のある最大時間。詳しくは、 [コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/)を参照してください。| 該当なし |
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
