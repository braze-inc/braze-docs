---
nav_title: キャンペーンの検索
article_title: キャンペーンの検索
page_order: 10
page_type: reference
description: "この記事では、キャンペーンの検索を使用してキャンペーンを見つける方法について説明します。"
tool:
  - Campaigns

---

# キャンペーンの検索

> この記事では、キャンペーンリストの検索フィールドを使用して結果を絞り込む方法について説明します。

## フィルター

サイドメニューのフィルターを使用して、作成者、編集使用者、送信日、またはチャネル別に結果をグループ化するか、\[**自分のものだけを表示**] を選択して、自分が作成したキャンペーンだけを表示できます。また、ステータスと[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)でフィルタリングして、結果をさらに絞り込むこともできます。

![][2]

検索ドロップダウンを展開して、最後の編集者、ターゲットセグメント、メッセージングチャネル、または日付でフィルタリングします。

![][3]

## 検索構文

キャンペーンフィルターを選択すると、適切な構文が検索フィールドに自動的に追加されます。ただし、これらのフィルターを手動で入力することもできます。手動検索を使用する場合、シンタックスはフィルターの名前、コロン、入力の順になります。例えば、プッシュキャンペーンを検索するには、`channel:push` と入力します。

サポートされている検索フィルターのリストを次に示します。

| 検索 | フィルター | 入力 |
| --- | --- | --- |
| キャンペーンAPI 識別子 | `api_id` | 具体的な[キャンペーン API 識別子]({{site.baseurl}}/api/identifier_types#api-identifier-types) |
| キャンペーン目標を区分する | `segment` | セグメント名 |
| キャンペーンが対象とするメッセージチャネル | `channel` | 次のいずれかです。<br>-`content_cards`<br>- `email`<br>- `push`<br>- `sms` (SMS とMMS の両方を返します)<br>- `webhook`
| ステータスまたは配信タイプ | `status` | 次のいずれかです。<br>- `one-time`<br>- `recurring`<br>- `triggered`<br>- `multivariate`<br>- `transactional`<br> - `drafts`<br> - `stopped`<br> - `archived`<br> - `all` |
| タグ | `tag` | \- 単一のタグの名前 <br>\- カンマで区切られたタグの名前の一覧 |
| 最新のエディター | `edited_by` | ユーザーのメール住所 |
| キャンペーンの作成日 | `created` | \- 書式の単一の日付 `YYYY/MM/DD`<br> \- 書式の日付の範囲 `YYYY/MM/DD-YYYY/MM/DD` |
| キャンペーンの最終編集日 | `edited` | \- 書式の単一の日付 `YYYY/MM/DD`<br> \- 書式の日付の範囲 `YYYY/MM/DD-YYYY/MM/DD` |
| キャンペーンを最後に送信した日時 | `sent` | \- 書式の単一の日付 `YYYY/MM/DD`<br> \- 書式の日付の範囲 `YYYY/MM/DD-YYYY/MM/DD` |
| 作成したキャンペーン | `created_by_me` | `true` |


[1]: {% image_buster /assets/img_archive/campaign_search.png %}
[2]: {% image_buster /assets/img_archive/campaign_search2.png %}
[3]: {% image_buster /assets/img_archive/campaign_search3.png %}
