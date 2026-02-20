---
nav_title: 「カレンダーに追加」リンク
article_title: 「カレンダーに追加」リンク
page_order: 1
page_type: tutorial
description: "この記事では、メールキャンペーンに「カレンダーに追加」リンクを含める方法について説明します。"
channel: email

---

# 「カレンダーに追加」リンク

> イベント、セール、または予約を宣伝する場合、メールに「カレンダーに追加」リンクを追加すると、ユーザーが簡単にイベントをカレンダーに保存できるようになります。

そのためには、メールの下書きを作成し、リンクをどこに配置するかを決めます。次に、2 つのオプションを追加します。1 つは Google カレンダー用、もう 1 つは他のカレンダー (iCal や Outlook など) 用です。たとえば、「Google カレンダーに追加」や「iCal または Outlook に追加」などとします。

![ダッシュボードにリンクを追加する際のリンクダイアログ。「リンク情報」タブが選択され、テキストが「Googleカレンダーに追加」に設定されています。]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## URL フォーマット

プレースホルダーを置き換えて、次の URL をリンクに追加します。これら 2 つの URL の唯一の違いは、Google カレンダーには `&format=gcal` パラメーターが必要な点です。

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

以下を置き換えます。

- `EVENT_SUBJECT`: イベントのタイトル
- `EVENT_LOCATION`: イベントの場所
- `START_TIME`: ISO 8601 形式 (YYYY-MM-DDTHH: MM: SSZ) の UTC 時刻で表したイベント開始時刻
- `END_TIME`: ISO 8601 形式 (YYYY-MM-DDTHH: MM: SSZ) の UTC 時刻で表したイベント終了時刻
- `EVENT_DESCRIPTION`: イベントの説明

すべてのスペースを HTML エスケープコード「`%20`」に置き換えます。たとえば、「Meet Braze」という件名は「Meet%20Braze」になります。

「Google カレンダーに追加」のURL の例は次のとおりです。

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### その他のパラメーター

以下のパラメーターはオプションで、イベントのその他の要素を定義するために使用できます。

- **主催者名:** `&organizer=name`
- **イベントに関連するURLを添付:** `&attach=http://www.example.com/`
- **期間:** `duration=30M`イベント終了時刻 (dtend) の代わりに、1 時間や 30 分などの期間を指定
- **リマインダーアラームの時間（分）:** `&reminder=15`
- **終日イベント:** `&allday=1`
- **UID:** イベントの一意の識別子をハードコーディングするオプションのパラメーターで、一部のカレンダーアプリでは時間の経過とともにイベントを更新できるようにします。文字列 @ics.agical.io は自動的に値に追加されます。

繰り返し発生するイベントには、以下のようなパラメーターを追加することもできます。
- **毎週のイベント:** `&recur=weekly`
- **毎月のイベント:** `&recur=monthly`
- **再発の終了:** `&recuruntil=END_DATE`、ここで `END_DATE` は再発がUTCで終了するISO 8601形式（YYYY-MM-DDTHH:MM:SSZ）の日付と時刻です

## リンクの動作

ユーザーがリンクをクリックすると、カレンダーは URL の UTC タイムスタンプを、カレンダーに設定されているユーザーのタイムゾーンに合わせて自動的に変換します。

たとえば、[Google カレンダーに追加] リンクを開いたときにカレンダーが CST に設定されている場合、イベントの時間は UTC の午後 3 時に相当する ＣＳＴ 時刻 (午前 10 時) を使って事前入力されます。

### Google カレンダー

クリックすると、Google カレンダーが新しいタブまたはウィンドウで開き、イベントの詳細が招待状に事前入力され、ユーザーが保存できるようになります。これはモバイルとデスクトップの両方で発生します。

![イベントを追加する Google カレンダーダイアログ。イベントの詳細が追加されて保存できる状態です。]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal と Outlook

デスクトップでは、クリックすると ICS ファイルがダウンロードされます。次に、ユーザーは ICS ファイルを開く必要があります。これにより iCal または Outlook が開き、カレンダーにイベントを追加するよう求められます。

![iCalカレンダーに新しいイベントを追加するためのダイアログが表示され、ユーザーにカレンダーの選択と確認を促します。]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![イベントが追加されたiCalカレンダーです。]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

モバイルでは、ユーザーはリンクを長押しする必要があります。これにより、カレンダーに追加するよう求められます。

![カレンダーリンクを長押しすると表示されるiOSのポップアップで、「カレンダーに追加」ボタンが含まれています。]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

詳細については、参照してください。
* [Google カレンダーのイベントを作成する](https://developers.google.com/calendar/api/guides/create-events)
* [メールメッセージにカレンダーに追加リンクを作成する](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)


