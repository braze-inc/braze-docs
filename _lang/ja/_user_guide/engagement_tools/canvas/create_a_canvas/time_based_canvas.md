---
nav_title: 時間ベースの機能
article_title: キャンバスの時間ベースの機能
page_order: 1
tools: Canvas
page_type: reference
description: "この記事では、キャンバスの定義、タイムゾーン、および時間ベースの機能の例について説明します。"

---

# キャンバスの時間ベースの機能

> この記事では、戦略やトラブルシューティング、よくある疑問を解決するために役立つ、キャンバスの時間ベースの機能について説明します。 

## スケジュールの遅延

{% alert important %}
2023 年 2 月 28 日以降、元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは、元のキャンバスワークフローを使用して作成された既存のキャンバスのスケジュールを編集するときの参考にしてください。キャンバスフローのワークフローの時間ベースの機能については、[遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)コンポーネントを確認してください。
{% endalert %}

### すぐに送信

| 定義 |  タイムゾーン |
| --- | --- |
| ユーザーが前のステップを受信した直後、またはこのステップが最初のステップの場合は、ユーザーがキャンバスに入った直後にメッセージを送信する。 | 該当なし |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][1]

### X 日後に送信

| 定義 |  タイムゾーン |
| --- | --- |
| 遅延後にメッセージを送信します。遅延は秒、分、時間、日、週単位で指定できる。  | 該当なし |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### 次の [曜日] の時刻 X に送信

| 定義 |  タイムゾーン |
| --- | --- |
| 次の指定した曜日、選択した時刻にメッセージを送信します。  | **ユーザーの現地時間**または**会社の時間**を選択します |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

たとえば、「次の土曜日の午後 3 時 15 分に送信」を選択するとします。ユーザーが土曜日にキャンバスに入った場合、そのメッセージは 7 日後の次の土曜日に届きます。金曜日に入ると、次の土曜日は 1 日後になります。

![][3]

### X 暦日で Y 時間に送信する

| 定義 |  タイムゾーン |
| --- | --- |
| 指定した日数の範囲で、指定時刻にメッセージを送信します。 | **ユーザーの現地時間**または**会社の時間**を選択します |

キャンバスは遅延を `day of the week` + `calendar days` として計算し、`time` を加算します。例えば、キャンバスコンポーネントが月曜日の午後 9 時に送信され、次のステップが「1 日後の午前 9 時に送信」するようにスケジュールされているとします。このメッセージは火曜日の午前 9 時に配信されます。これは、キャンバスが遅延を `Monday` + `1 calendar day` として計算し、`9 am` を加算するためです。

![][4]

### インテリジェントタイミング

| 定義 | タイムゾーン |
| ---------- | ----- |
| [インテリジェント・タイミングは]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)、ユーザーの過去のメッセージング（チャネル毎）やアプリとのインタラクションの統計分析に基づいて、最適な送信時間を計算する。 | [フォールバック]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options)として**特定の時刻**を選択した場合、ユーザーの現地時間で送信されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][5]

## グローバルフリークエンシーキャップ

| 定義 | タイムゾーン |
| --- | --- |
| 特定の期間内に、各ユーザーがキャンバスを受信する回数を制限します。これは、分、日、週 (7 日間)、および月単位で測定できます。 | ユーザーの現地時間。ユーザーのタイムゾーンが設定されていない場合、これは会社のタイムゾーンにフォールバックする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping)は、24 時間ではなく暦日に基づいています。したがって、1 日に送信できるキャンペーンは 1 つだけというフリークエンシーキャップルールを設定できますが、ユーザーが現地時間の午後 11 時にメッセージを受信した場合には、その 1 時間後 (翌日の午前 0 時) に別のメッセージを受け取ることができます。

![][6]

{% alert note %}
キャンバスを承認するための適切な[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)を持っている場合は、ワークフローに[**要約**ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_approval/#using-approvals)が表示されます。
{% endalert %}


[1]: {% image_buster /assets/img_archive/schedule_delay_immediately.png %}
[2]: {% image_buster /assets/img_archive/schedule_delay_after.png %}
[3]: {% image_buster /assets/img_archive/schedule_delay_next.png %}
[4]: {% image_buster /assets/img_archive/schedule_delay_in.png %}
[5]: {% image_buster /assets/img_archive/schedule_delay_intelligent.png %}
[6]: {% image_buster /assets/img_archive/schedule_frequency_capping.png %}
