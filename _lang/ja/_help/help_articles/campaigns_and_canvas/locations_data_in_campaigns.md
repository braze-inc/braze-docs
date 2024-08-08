---
nav_title: 位置データの確認
article_title: 位置データの確認
page_order: 1
page_type: solution
description: "このヘルプ記事では、ユーザーが利用可能な場所を持っていない場合に役立つかもしれない簡単なチェックを説明します。"
tool: Location
---

# 位置データの確認

BrazeはデフォルトでSDKを介してユーザーの最新の位置情報を取得します。これは通常、「最近の場所」がユーザーが最も最近アプリを使用した場所であることを意味します。Brazeにバックグラウンド位置データを送信すると、より詳細なデータが利用できる場合があります。

ユーザーに利用可能な場所がない場合、2つの迅速なチェックでデータ収集と日付転送を確認できます。

## データ収集

アプリが位置データを収集していることを確認してください:

- iOSの場合、ユーザーはユーザージャーニーのある時点でプロンプトを介して位置データの共有にオプトインすることを意味します。 
- Androidの場合、インストール時にアプリが詳細または大まかな位置情報の許可を求めることを確認してください。

ユーザーの位置データがBrazeに送信されているかどうかを確認するには、**位置情報利用可能**フィルターを使用します。このフィルターを使用すると、「最新の場所」を持つユーザーの割合を確認できます。

![][25]

## データ転送

開発者がBrazeに位置データを渡していることを確認してください。通常、位置データの送信はユーザーが許可を与えた後、SDKによって自動的に処理されますが、開発者がBrazeで位置情報の追跡を無効にしている可能性があります。位置情報の追跡に関する詳細情報は次の場所で見つけることができます:
- \[Android][26]
- \[iOS][27]
- \[Web][28]

まだ助けが必要ですか？[サポートチケット]({{site.baseurl}}/braze_support/)を開封する。

_最終更新日: 2022年11月16日_

[25]: {% image_buster /assets/img_archive/trouble7.png %}
[26]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
