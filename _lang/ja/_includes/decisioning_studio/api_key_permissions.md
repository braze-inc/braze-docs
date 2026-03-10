| 権限 | 目的 | 必須かどうか |
| :--- | ----- | :---: |
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | テスト送信を使用して一時的なユーザープロファイルを作成するだけでなく、ユーザープロファイルのカスタム属性を更新します。 | ✓ |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | テスト送信の使用中に作成された一時的なユーザープロファイルを削除します。 | テスト送信のみ |
| [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | 選択したセグメントからユーザーの一覧をエクスポートして、毎朝、利用可能なオーディエンスの通信を更新します。 | ✓ |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | セグメントの代わりに `external_id` を使用してユーザーをターゲットにする場合、識別子の一覧を取得します。Decisioning Studioは個人を特定できる情報（PII）を受け付けないため、パラメータ`fields_to_export`が非PIIフィールドのみを返すようにする必要がある。
 | `external_ids` を使用している場合のみ |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Decisioning Studioの実験者向けに設定されたAPIキャンペーンを使用し、推奨される時間に推奨されるバリアントを送信する。 | ✓ |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/#prerequisites) | アクティブなキャンペーンの一覧を取得し、使用可能なメールコンテンツを抽出して、実験に使用します。 | ✓ |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | キャンペーンデータを集計してエクスポートする。これにより、Decisioning Studioでのレポート作成、検証、トラブルシューティングが可能になる。レポート値を比較し、ベースラインのパフォーマンスを分析できる。<br><br>必須ではありませんが、この権限をお勧めします。 |  |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | HTML の内容、件名、および画像のリソースを、既存のキャンペーンから取得して、実験に使用します。 | ✓ |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | アクティブなキャンバスの一覧を取得し、使用可能なメールコンテンツを抽出して、実験に使用します。 | ✓ |
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | BAU がキャンバスでオーケストレーションされている場合は、集約されたキャンバスをエクスポートしてレポートと検証を行います。<br><br>必須ではありませんが、この権限をお勧めします。 |  |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/#prerequisites) | HTML の内容、件名、および画像のリソースを、既存のキャンバスから取得して、実験に使用します。 | ✓ |
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | 既存の全セグメントを、Decisioning Studioの実験担当者向けの潜在的なターゲットオーディエンスとして取得する。 | ✓ |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | オーディエンスを選択する際にDecisioning Studioに表示されるセグメントサイズ情報をエクスポートする。 | ✓ |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/#prerequisites) | オーディエンスのサイズやパフォーマンスの変化を理解するのに役立つ、エントリや終了の基準などのセグメント情報を取得します。 |  |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | [ダイナミックなプレースホルダー]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) (Braze Liquid タグ) を使用して選択した基本の HTML テンプレートのコピーを作成し、オリジナルの変更を回避します。 | ✓ |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | 実験条件（例えばコールトゥアクションなど）が変更された場合、Decisioning Studioで作成されたテンプレートのコピーに更新を反映させる。 | ✓ |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/#prerequisites) | Brazeインスタンス内でDecisioning Studioによって作成されたテンプレートの情報を取得する。 | ✓ |
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | テンプレートが Braze インスタンスに正常にコピーされたことを検証します。 | ✓ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }