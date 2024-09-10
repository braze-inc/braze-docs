---
nav_title: Export Troubleshooting
article_title: Export Troubleshooting
page_order: 10
page_type: reference
description: "This reference article covers some common troubleshooting scenarios for API and CSV exports."

---

# Export troubleshooting

> The following lists error messages you may encounter while exporting data via CSV or API from Braze.

## Common errors

### 'AccessDenied' 

**独自の S3 バケット**を使用している場合、次の理由が考えられます。
- 予期されたオブジェクトはS3バケットにもう存在しません。エンジニアに確認してください。
- Brazeダッシュボード内で設定されたS3資格情報に正しい権限がありません。チームと共に適切な資格情報を確認してください。

**Braze S3 バケット**を使用している場合、次の理由が考えられます。
- オブジェクトはもうそこにありません。これは、4 時間以上前に実行したエクスポートのリンクをクリックした場合に発生する可能性があります。このような場合は、エクスポートを再実行してください。
- すぐにダウンロードリンクをクリックしましたが、S3がオブジェクトを提供する準備ができていませんでした。数分後にもう一度やり直してください。通常、レポートのサイズが大きいほど時間がかかります。 
- エクスポートが大きすぎるため、サーバーがこのzipファイルを作成しようとしてメモリ不足になりました。このような場合は、このエクスポートを試みているユーザーにメールを自動的に送信します。If you consistently run into this issue, we recommend that you use your own S3 buckets in the future.

### 'ExpiredToken'

This will happen if the email was sent 4+ hours ago.Re-run the export and download it within 4 hours.
This could also be caused by Braze no longer having access to the S3 bucket you are downloading the data to.Make sure you've updated your S3 credentials using these steps.

### "Looks like the file doesn't exist anymore, please check to make sure nothing is deleting objects from your bucket"

There may be a slight lag between when Braze's email with the export gets sent, and when S3 is actually ready to serve the object.このエラーが表示された場合は、数分待ってからやり直してください。

### フィールドにアポストロフィが追加されました

Brazeは、フィールドが次のいずれかの文字で始まる場合、CSVエクスポートのフィールドに自動的にアポストロフィを追加します:

- -
- =
- +
- @

例えば、フィールド「-1943」は「'-1943」としてエクスポートされます。これは、[`/users/export/segment`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)によって返されるJSONエクスポートには適用されません。