| 権限 | 目的 | 必須かどうか |
| :--- | ----- | :---: |
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) | テスト送信を使用して一時的なユーザープロファイルを作成するだけでなく、ユーザープロファイルのカスタム属性を更新します。 | ✓ |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) | テスト送信の使用中に作成された一時的なユーザープロファイルを削除します。 | テスト送信のみ |
| [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) | 選択したセグメントからユーザーの一覧をエクスポートして、毎朝、利用可能なオーディエンスの通信を更新します。 | ✓ |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) | セグメントの代わりに `external_id` を使用してユーザーをターゲットにする場合、識別子の一覧を取得します。Decisioning Studio は個人識別情報 (PII) を受け入れないため、`fields_to_export` パラメーターが非 PII フィールドのみを返すようにする必要があります。
 | `external_ids` を使用している場合のみ |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | Decisioning Studio の実験者を決定するために設定された API キャンペーンを使用して、推奨された時刻に推奨バリアントを送信します。 | ✓ |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/#prerequisites) | アクティブなキャンペーンの一覧を取得し、使用可能なメールコンテンツを抽出して、実験に使用します。 | ✓ |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) | 集約されたキャンペーンデータをエクスポートして、Decisioning Studio でのレポート、検証、トラブルシューティングを可能にするため、レポートの値を比較したり、ベースラインパフォーマンスを分析したりできます。<br><br>必須ではありませんが、この権限をお勧めします。 |  |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details) | HTML の内容、件名、および画像のリソースを、既存のキャンペーンから取得して、実験に使用します。 | ✓ |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) | アクティブなキャンバスの一覧を取得し、使用可能なメールコンテンツを抽出して、実験に使用します。 | ✓ |
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics) | BAU がキャンバスでオーケストレーションされている場合は、集約されたキャンバスをエクスポートしてレポートと検証を行います。<br><br>必須ではありませんが、この権限をお勧めします。 |  |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/#prerequisites) | HTML の内容、件名、および画像のリソースを、既存のキャンバスから取得して、実験に使用します。 | ✓ |
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment) | Decisioning Studio の実験者の潜在的なターゲットオーディエンスとして、すべての既存のセグメントを取得します。 | ✓ |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics) | オーディエンスを選択したときに、Decisioning Studio に表示されるセグメントサイズ情報をエクスポートします。 | ✓ |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/#prerequisites) | オーディエンスのサイズやパフォーマンスの変化を理解するのに役立つ、エントリや終了の基準などのセグメント情報を取得します。 |  |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template) | [ダイナミックなプレースホルダー]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) (Braze Liquid タグ) を使用して選択した基本の HTML テンプレートのコピーを作成し、オリジナルの変更を回避します。 | ✓ |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template) | コールトゥアクションなどの実験条件が変更された場合、更新を Decisioning Studio で作成されたテンプレートコピーにプッシュします。 | ✓ |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/#prerequisites) | Braze インスタンス内の Decisioning Studio 作成テンプレートの決定に関する情報を取得します。 | ✓ |
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates) | テンプレートが Braze インスタンスに正常にコピーされたことを検証します。 | ✓ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }