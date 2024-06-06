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

サイドメニューのフィルターを使用して、作成者、編集使用者、送信日、またはチャネル別に結果をグループ化するか、[**自分のものだけを表示**] を選択して、自分が作成したキャンペーンだけを表示できます。また、ステータスと[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)でフィルタリングして、結果をさらに絞り込むこともできます。

![][2]

検索ドロップダウンを展開して、最後の編集者、ターゲットセグメント、メッセージングチャネル、または日付でフィルタリングします。

![][3]

## 検索構文

キャンペーンフィルターを選択すると、適切な構文が検索フィールドに自動的に追加されます。ただし、これらのフィルターを手動で入力することもできます。手動検索を使用する場合、構文はフィルター名、セミコロン、入力の順になります。例えば、プッシュキャンペーンを検索するには、`channel:push` と入力します。

サポートされている検索フィルターのリストを次に示します。

| 検索内容 | フィルター | 入力 |
| --- | --- | --- |
| キャンペーン API ID | `api_id` | 特定の[キャンペーン API ID]({{site.baseurl}}/api/identifier_types#api-identifier-types) |
| キャンペーンターゲットをセグメント化する | `segment` | セグメント名 |
| メッセージングチャネルとキャンペーンターゲット | `channel` | 次のいずれか: <br>- `content_cards`<br>- `email`<br>- `push`<br>- `sms` (SMS とMMS の両方を返します)<br>- `webhook`
| ステータスまたは配信タイプ | `status` | 次のいずれか: <br>- `one-time`<br>- `recurring`<br>- `triggered`<br>- `multivariate`<br>- `transactional`<br> - `drafts`<br> - `stopped`<br> - `archived`<br> - `all` |
| タグ | `tag` | - 単一のタグ名 <br>\- コンマで区切られたタグ名のリスト |
| 最後の編集者 | `edited_by` | ユーザーのメールアドレス |
| キャンペーンの作成日付 | `created` | - `YYYY/MM/DD` フォーマットの単一の日付<br> - `YYYY/MM/DD-YYYY/MM/DD` 形式の日付の範囲 |
| キャンペーンが最後に編集された日付 | `edited` | - `YYYY/MM/DD` フォーマットの単一の日付<br> - `YYYY/MM/DD-YYYY/MM/DD` 形式の日付の範囲 |
| キャンペーンが最後に送信された日付 | `sent` | - `YYYY/MM/DD` フォーマットの単一の日付<br> - `YYYY/MM/DD-YYYY/MM/DD` 形式の日付の範囲 |
| 自分が作成したキャンペーン | `created_by_me` | `true` |


[1]: {% image_buster /assets/img_archive/campaign_search.png %}
[2]: {% image_buster /assets/img_archive/campaign_search2.png %}
[3]: {% image_buster /assets/img_archive/campaign_search3.png %}
