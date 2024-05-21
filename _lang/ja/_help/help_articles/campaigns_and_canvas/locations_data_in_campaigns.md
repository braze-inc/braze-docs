---
nav_title: 位置情報を確認する
article_title: 位置情報を確認する
page_order: 1
page_type: solution
description: "このヘルプ記事では、利用可能な場所にユーザーがいない場合に役立つクイックチェックについて説明します。"
tool: Location
---

# 位置情報を確認する

Braze は、SDK を介してデフォルトでユーザの最新の場所をキャプチャします。これは、通常、"lanced location"が、ユーザーがアプリを最後に使用した場所であることを意味します。Brazeのバックグラウンドロケーションデータを送信すると、より詳細なデータが利用可能になる場合があります。

利用可能な場所にユーザーがいない場合は、2 つのクイックチェックでデータ収集と日付転送を確認できます。

## データ収集

アプリが位置データを収集していることを確認します。

- iOSの場合、これはユーザがユーザジャーニーのある時点でプロンプトを介して位置データを共有することをオプトインすることを意味します。 
- Android の場合は、インストール時に細かい場所または粗い場所の権限がアプリで要求されていることを確認します。

ユーザーロケーションデータがBraze に送信されているかどうかを確認するには、**Location Available** フィルタを使用します。このフィルタを使用すると、" が最新のlocation" のユーザの割合を表示できます。

![][25]

## データ転送

開発者がロケーションデータをBraze に渡していることを確認します。通常、ロケーションデータの受け渡しはユーザーが権限を付与した後にSDKによって自動的に処理されますが、開発者がBrazeでロケーショントラッキングを無効にした可能性があります。位置追跡の詳細については、以下を参照してください。
\- [Android][26]
\- [iOS][27]
\- [Web][28]

それでも助けが必要ですか?[サポートチケット]({{site.baseurl}}/braze_support/)を開きます。

_最終更新日2022年11月16日_

[25]: {% image_buster /assets/img_archive/trouble7.png %}
[26]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
