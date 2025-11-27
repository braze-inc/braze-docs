---
nav_title: ユーザーの削除
article_title: ユーザーの削除
page_order: 4.2
toc_headers: h2
description: "個々のユーザーまたはユーザーのSegmentをBraze ダッシュボードから直接削除する方法について説明します。" 
---

# ユーザーの削除

> 個々のユーザーまたはユーザーのSegmentをBraze ダッシュボードから直接削除する方法について説明します。

{% alert important %}
この機能は現在早期アクセス段階です。参加したい場合は、顧客のサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

ユーザーを削除するには、管理者であるか、**Delete ユーザー**権限が必要です。

## ユーザー削除について

ユーザ削除を使用すると、不要になった、エラー で作成された、または準拠のために削除する必要があるプロファイル(GDPR やCCPA など) を削除して、データベースを管理できます。

| 検討 | 詳細 |
|---------------|---------|
| 最大サイズ | Segmentを削除すると、最大1億件のユーザープロファイルを削除できます。 |
| 待ち時間 | すべてのSegmentの削除には、7 日間の待機時間と、削除の処理にかかる時間が必要です。 |
| ジョブ制限 | 一度に削除できるSegmentは1 つだけです。これには7 日間の待機期間が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## ユーザーの削除

[ 個々のユーザー](#delete-individual) または[ ユーザーのSegments](#delete-segment) をBraze ダッシュボードから削除できます。

### 個人を削除する {#delete-individual}

個々のユーザーをBrazeから削除するには、**Audience**> **検索ユーザーs**に移動し、ユーザーを検索して選択します。重複するユーザープロファイルを削除する場合は、正しいものを選択したことを確認します。

![Brazeの「ユーザの検索」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
単一ユーザーの削除は永続的です。プロファイルは削除後に復元できません。  
{% endalert %}

プロファイル画面で、<i class="fa-solid fa-ellipsis-vertical"></i>**オプション**>**ユーザ**を削除を選択します。Braze でユーザーが完全に削除されるまでに数分かかる場合があります。

![ユーザーを削除するための選択肢を示す、縦長楕円メニュー開封とBrazeしたユーザー。]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Segmentの削除 {#delete-segment}

まだ使用していない場合は、[削除するユーザープロファイルを含むSegment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)を作成します。重複するユーザーを削除する場合は、必ずすべてのユーザープロファイルを含めてください。

Brazeで、**Audience**> **Audience**を管理し、**Delete Users**タブを選択します。

![Braze ダッシュボードの「視聴者の管理」セクションの「ユーザの削除」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

**Delete ユーザー s**を選択し、削除するSegmentを選択し、**Next**を選択します。

![削除対象として選択されたSegmentを含むポップアップウィンドウ。]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

**DELETE**と入力してリクエストを確認し、**Delete ユーザー s**を選択します。

![確認ボックスに「DELETE」と入力された確認ページ。]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

このSegmentのユーザーはすぐには削除されません。代わりに、次の7 日間は削除保留としてマークされます。この後、削除され、お知らせするようにメールさせていただきます。

{% alert tip %}
これらの厳密なユーザーs がSegmentの変更に関係なく削除されるように、**Pending Deletion** というSegment フィルターが自動的に作成されます。[このフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters)を使用して、保留中の削除のステータスを確認できます。
{% endalert %}

## Segment削除のキャンセル {#cancel}

保留中のSegment削除をキャンセルするには、7 日間かかります。キャンセルするには、**Audience**> **Manage Audience**に移動し、**Delete Users**タブを選択します。

![Braze ダッシュボードの「視聴者の管理」セクションの「ユーザの削除」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

保留中のSegment削除の横にある<i class="fa-solid fa-eye"></i>を選択して、削除レコードの詳細を開封します。

![「ユーザの削除」タブで保留中のSegmentの削除。]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

削除レコードの詳細で、**削除のキャンセル**を選択します。

![「Delete Users」タブの「Deletion Record Details」ウィンドウ。]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
一括ユーザー削除が進行中の場合は、いつでもキャンセルできます。ただし、すでに削除されているユーザーは、キャンセルリレーションを復元できません。
{% endalert %}

## 削除ステータスの確認 {#status}

削除のステータスは、[Segment フィルターs](#segment-filters)、[管理オーディエンス](#manage-audience)ページ、または[セキュリティイベントレポートs](#security-event-report)を使用して確認できます。

### セグメントフィルター

削除するユーザーのSegmentをリクエストすると、[Segment フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) **Pending Deletion** という名前の[が自動的に作成されます。これを使用すると、次のことができます。

- 指定した削除実行日に関連付けられたユーザーの厳密な集合を参照してください。
- これらのユーザーをキャンペーンから除外して、削除前に受信しないようにします。
- 遵守または記録のために必要な場合は、リストをエクスポートします。

### オーディエンスを管理

{% alert note %}
削除されるユーザーの一覧を取得するには、代わりに[Pending Deletion Segment フィルター](#segment-filters)を使用します。
{% endalert %}

**Audience**> **Manage Audience**に進み、**Delete Users**タブを選択します。

![Braze ダッシュボードの「視聴者の管理」セクションの「ユーザの削除」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

このページでは、現在および保留中のすべての削除に関する次の一般情報を確認できます。

| フィールド | 説明 |
|-------|-------------|
| リクエスト日 | リクエストが最初に行われた日付。**Pending Deletion**フィルターと一緒に使用して、プロファイルの削除保留中の一覧を取得します。 |
| 要求者 | 削除リクエストを開始したユーザー。 |
| セグメント名 | 削除保留中のユーザーを選択するために使用するSegmentの名前。 |
| ステータス | 削除要求が保留中か、進行中か、完了かを示します。 |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

特定のリクエストの詳細については、<i class="fa-solid fa-eye"></i>を選択して削除レコードの詳細を表示します。ここでは、[キャンセルの保留中のSegment削除](#cancel) も実行できます。

![「ユーザの削除」タブで保留中のSegmentの削除。]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### セキュリティイベントレポート

また、セキュリティイベントレポートをダウン読み込むすることで、以前の削除のステータスを確認することもできます。詳細については、[セキュリティー設定s]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report) を参照してください。

## よくある質問 {#faq}

### 1億 ユーザー s 以上のSegment s を削除できますか?

いいえ。1億 ユーザー s を超えるSegment s は消去できません。このサイズのSegmentを削除する際にヘルプが必要な場合は、[support@braze.com](mailto:support@braze.com) までご連絡ください。

### 自動ユーザーマージはユーザーの削除に影響しますか?

スケジュールされたマージにユーザープロファイルsの保留中の削除が含まれている場合、Brazeはそれらのプロファイルsをスキップし、それらをマージしません。これらのプロファイルs を結合するには、削除から削除する必要があります。

### h ユーザー s に送信され、削除が保留されているデータへのアプリは?

外部システムまたはSDK s から送信されたデータはまだ受け入れられますが、ユーザーs はアクティビティーに関係なくスケジュールされたとして削除されます。

### キャンバスとキャンペーン s がユーザー s の削除をトリガーしますか?

はい。ただし、**Pending Deletion** [Segment フィルター](#segment-filters) ですべてのユーザーを除外するSegmentインクルードフィルターを追加できます。

### 削除されたユーザープロファイルs を復元できますか?

個々のユーザーの削除は永続的です。

[ キャンセル Segment削除](#cancel) は、7 日後までに実行できます。ただし、すでに削除されているユーザーは、キャンセルリングを元に戻すことはできません。
