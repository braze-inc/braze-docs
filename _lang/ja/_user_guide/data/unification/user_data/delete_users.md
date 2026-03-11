---
nav_title: ユーザーを削除する
article_title: ユーザーを削除する
page_order: 4.2
toc_headers: h2
description: "Brazeのダッシュボードから直接、個々のユーザーまたはユーザーセグメントを削除する方法を学ぶ。"
alias: /delete_users/
hidden: true
---

# ユーザーを削除する

> Brazeのダッシュボードから直接、個々のユーザーまたはユーザーセグメントを削除する方法を学ぶ。

{% alert important %}
この機能の早期アクセスは一時的に閉鎖されている。詳細については顧客サクセスマネージャーに連絡せよ。
{% endalert %}

## 前提条件

ユーザーを削除するには管理者である必要がある。

## ユーザー削除について

ユーザー削除機能により、不要になったプロファイル、エラーで作成されたプロファイル、またはコンプライアンス（GDPRやCCPAなど）のために削除が必要なプロファイルを削除することで、データベースを管理できる。

| 検討 | 詳細 |
|---------------|---------|
| 最大サイズ | セグメントを削除する際、最大1億件のユーザープロファイルを削除できる。 |
| 待機期間 | すべてのセグメント削除には、7日間の待機期間に加えて、削除処理にかかる時間がかかる。 |
| 仕事の制限 | 一度に削除できるのは一つのセグメントのみであり、これには7日間の待機期間が含まれる。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## ユーザーを削除する

Brazeのダッシュボードから、[個々のユーザー](#delete-individual)または[ユーザーセグメント](#delete-segment)を削除できる。

### 個人を削除する {#delete-individual}

Brazeから個々のユーザーを削除するには、**オーディエンス**＞**ユーザー検索**に移動し、ユーザーを検索して選択する。重複したユーザープロファイルを削除する場合は、正しいものを選択したことを確認せよ。

![Brazeの「ユーザー検索」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
単一ユーザーの削除は永久的なものだ。プロファイルは削除後に復元できない。  
{% endalert %}

プロファイルページで、**[オプションを表示**] > **[ユーザー**<i class="fa-solid fa-ellipsis-vertical"></i>**を削除]** を選択する。覚えておいてほしいが、Brazeでユーザーが完全に削除されるまで数分かかる場合がある。

![Brazeのユーザーが縦の省略記号メニューを開いている状態。ユーザーを削除するオプションが表示されている。]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### セグメントを削除する {#delete-segment}

まだ作成していないなら、削除したいユーザープロファイルを含む[セグメントを作成せよ]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)。重複ユーザーを削除する場合は、必ず全てのユーザープロファイルを含めること。

Brazeで、**オーディエンス**＞**オーディエンス管理**に移動し、**ユーザー削除**タブを選択する。

![Brazeダッシュボードの「オーディエンス管理」セクションにある「ユーザー削除」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

**ユーザー削除**を選択し、削除したいセグメントを選び、次に**進む**を選択する。

![削除対象として選択されたセグメントを含むポップアップウィンドウ。]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

要求を確認するには**「DELETE」**と入力し、その後**「ユーザーを削除」**を選択する。

![確認ボックスに「削除」と入力された確認ページ。]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

このセグメントのユーザーはすぐに削除されない。代わりに、それらは今後7日間、削除待ちとしてマークされる。この期間を過ぎると、それらは削除される。その際はメールでお知らせする。

{% alert tip %}
これらの特定のユーザーがセグメントの変更に関係なく確実に削除されるように、自動的に「**削除待機」**というセグメントフィルターが作成される。[このフィルターを使って]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters)、保留中の削除のステータスを確認できる。
{% endalert %}

## セグメント削除の確認

Brazeは、削除待ちのプロファイル数を記載した確認メールを送信する。

削除を続行するには、Brazeにログインし、削除リクエストを確認する。

メールに記載された期間内に確認を行わない場合、削除リクエストは期限切れとなり、処理されない。

## セグメント削除のキャンセル {#cancel}

保留中のセグメント削除は、7日以内にキャンセルできる。キャンセルするには、**オーディエンス**＞**オーディエンス管理**に移動し、**ユーザー削除**タブを選択する。

![Brazeダッシュボードの「オーディエンス管理」セクションにある「ユーザー削除」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

保留中のセグメント削除の横で、削除記録の詳細を開くには<i class="fa-solid fa-eye"></i>を選択する。

![「ユーザー削除」タブで保留中のセグメント削除。]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

削除記録の詳細で、**削除をキャンセルする**を選択する。

![「ユーザー削除」タブの「削除記録の詳細」ウィンドウ。]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
一括ユーザー削除が進行中の場合、いつでもキャンセルできる。ただし、キャンセル前に既に削除されたユーザーは復元できない。
{% endalert %}

## 削除ステータスの確認 {#status}

削除のステータスは、[セグメントフィルター](#segment-filters)、[オーディエンス](#manage-audience)管理ページ、またはセキュリティイベントレポートで確認できる。

### セグメントフィルター

ユーザーセグメントの削除をリクエストすると、自動的に**「削除待機中」**という[セグメントフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters)が作成される。それを使ってできることは：

- 特定の削除実行日に関連付けられた正確なユーザーセットを確認する。
- それらのユーザーをキャンペーンから除外する。そうすれば、削除される前にメッセージを受け取らなくなる。
- コンプライアンスや記録保管のために必要なら、リストをエクスポートしろ。

### オーディエンスを管理する

{% alert note %}
削除される正確なユーザーの一覧を取得するには、代わりに[「保留中の削除」セグメント](#segment-filters)フィルターを使用する。
{% endalert %}

**オーディエンス**＞**オーディエンス管理**に移動し、**ユーザー削除**タブを選択する。

![Brazeダッシュボードの「オーディエンス管理」セクションにある「ユーザー削除」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

このページでは、現在進行中および保留中の全削除対象について、以下の一般的な情報を確認できる。

| フィールド | 説明 |
|-------|-------------|
| 依頼日 | その要求が最初に提出された日付。**削除待ち**フィルターと一緒に使えば、削除待ちのプロファイル一覧を取得できる。 |
| 要求者 | 削除リクエストを送信したユーザー。 |
| セグメント名 | 削除待ちのユーザーを選択するために使用されるセグメントの名前。 |
| ステータス | 削除リクエストが保留中か、進行中か、完了したかを示す。 |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

特定のリクエストの詳細については、削除記録の詳細を表示するために<i class="fa-solid fa-eye"></i>を選択する。ここでは[保留中のセグメント削除](#cancel)も[キャンセル](#cancel)できる。

![「ユーザー削除」タブで保留中のセグメント削除。]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### セキュリティイベントレポート

セキュリティイベントレポートをダウンロードすれば、過去の削除ステータスも確認できる。詳細については、[セキュリティ設定を]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report)参照せよ。

## よくある質問 {#faq}

### 1億人を超えるユーザーがいるセグメントを削除できるか？

いいや。1億人を超えるユーザーがいるセグメントは削除できない。このサイズのセグメントを削除する際に支援が必要な場合は、[support@](mailto:support@braze.com)に連絡[braze.com](mailto:support@braze.com)せよ。

### どうやら1億人のユーザーを削除できず、1000万人しか削除できないようだ。これはバグか？

いや、これはバグではない。一部の顧客は、早期アクセス（EA）プログラム期間中に削除できるユーザー数に制限がある。

EAプログラムが進むにつれ、この処理能力は向上するように設計されており、最終的には全ての顧客が最大1億ユーザーを削除できるようになる。

この容量を増やしたい場合は、Brazeのアカウントマネージャーに連絡せよ。リクエストは製品チームの裁量で許可される。

### オートメーションによるユーザー統合は、ユーザー削除に影響するだろうか？

スケジュールされたマージに削除待ちのユーザープロファイルが含まれている場合、Brazeはそれらのプロファイルをスキップし、マージしない。これらのプロファイルを統合するには、削除対象から除外する必要がある。

### 削除待ちの状態でユーザーに送信されたデータはどうなるのか？

外部システムやSDKから送信されたデータは引き続き受け付けるが、ユーザーの削除は活動の有無にかかわらずスケジュール通り行われる。

### キャンバスとキャンペーンは、削除待ちのユーザーに対してトリガーされるのか？

はい。ただし、セグメント包含フィルターを追加すれば、**削除待機中の**[セグメントフィルター](#segment-filters)を持つ全ユーザーを除外できる。

### 削除したユーザープロファイルを復元できるか？

個々のユーザーを削除すると、その操作は取り消せない。

[セグメントの削除は、](#cancel)削除後7日以内に[キャンセル](#cancel)できる。ただし、キャンセル前に既に削除されたユーザーは復元できない。
