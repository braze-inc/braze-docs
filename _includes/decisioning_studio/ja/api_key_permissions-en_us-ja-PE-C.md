| 許可 | 目的 | 必要か？ |
| :--- | ----- | :---: |
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | テストセンドを使用して一時ユーザープロファイルを作成するだけでなく、ユーザープロファイルs のカスタム属性をアップデートします。 | ✓ |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | テストセンドの使用中に作成された一時ユーザープロファイルを削除します。 | テストセンドのみ |
| [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | 選択したSegmentからユーザーの一覧をエクスポートして、毎朝利用可能なオーディエンス通信をアップデートします。 | ✓ |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | Segmentの代わりに`external_id` を使用してユーザーs をターゲットにする場合、識別子s の一覧を取得します。デシジョンスタジオは個人識別情報(PII) を受け入れないため、`fields_to_export` パラメータが非PII フィールドs のみを返すようにする必要があります。
 | 使用時のみ `external_ids` |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | スタジオの実験者を決定するために設定されたAPI キャンペーンを使用して、推奨された時刻に推奨バリアントを送信します。 | ✓ |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/#prerequisites) | 使用中のキャンペーンの一覧を取得し、使用可能なメール内容を抽出します。 | ✓ |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 集約されたキャンペーンデータをエクスポートして、デシジョンスタジオでのレポートの検証、検証、トラブルシューティングを可能にするため、レポートの値を比較したり、ベースラインパフォーマンスを分析したりできます。<br><br>必要ありませんが、この許可をお勧めします。 |  |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | HTMLの内容、件名、および"画像の資料を、現行のキャンペーンから取得して、実験に使用します。 | ✓ |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | 使用中のキャンバスの一覧を取得して、使用可能なメール内容を抽出して、実験に使用できます。 | ✓ |
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | BAU がキャンバス でオーケストレーションされている場合は、集約されたキャンバスをエクスポートしてレポートの検証と検証を行います。<br><br>必要ありませんが、この許可をお勧めします。 |  |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/#prerequisites) | HTMLの内容、件名、および"画像の情報を、既存のキャンバスから取得して、実験に使用します。 | ✓ |
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | デシジョンスタジオ実験者の潜在的な標的オーディエンスsとして、存在するすべてのSegmentsを取得します。 | ✓ |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | オーディエンスを選択したときに、デシジョンスタジオに表示されるSegmentサイズ情報をエクスポートします。 | ✓ |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/#prerequisites) | オーディエンスの大きさやパフォーマンスの変化を理解するのに役立つ、エントリや終了基準などのSegment情報を取得します。 |  |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | [ダイナミックなプレースホルダ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)(Braze Liquid タグ)を使用して選択した基本HTML テンプレートs のコピーを作成し、オリジナルへの変更を回避します。 | ✓ |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | アクション s などの実験条件が変更された場合、更新 をスタジオ作成のテンプレートコピーにプッシュします。 | ✓ |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/#prerequisites) | Brazeインスタンス内のスタジオ作成テンプレートの決定に関する情報を取得します。 | ✓ |
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | テンプレートがBrazeインスタンスに正常にコピーされたことを検証します。 | ✓ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }