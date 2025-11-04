---
nav_title: 位置情報をチェックする
article_title: 位置情報をチェックする
page_order: 1
page_type: solution
description: "このヘルプ記事では、利用可能な位置情報があるユーザーが存在しない場合に役立つ簡単なチェックについて説明します。"
tool: Location
---

# 位置情報をチェックする

Brazeは、SDKを通じてユーザーの最新の位置情報をデフォルトで取得する。これは通常、「最新の位置情報」が、ユーザーがアプリを最後に使用した場所であることを意味します。Braze のバックグラウンド位置情報データを送信する場合は、より詳細なデータを使用できる場合があります。

利用可能なロケーションを持つユーザーがいない場合、2つの簡単なチェックでデータ収集と日付転送を確認することができる。

## データ収集

アプリが位置情報を収集していることを確認する：

- iOS の場合、これは、ユーザーがユーザージャーニーのどこかの時点でプロンプトを介して位置情報データの共有を選択することを意味します。 
- Androidについては、設置時にアプリが細かい場所または粗い場所の許可を要求していることを確認してください。

ユーザーの位置情報がBrazeに送信されているかどうかを確認するには、**Location Available**フィルターを使用する。このフィルターによって、「最新の位置情報」を持つユーザーの割合を見ることができる。

![]({% image_buster /assets/img_archive/trouble7.png %})

## データ転送

開発者が位置情報をBrazeに渡していることを確認する。通常、位置データの受け渡しは、ユーザーが権限を付与した後に SDK によって自動的に処理されますが、開発者が Braze での位置情報の追跡を無効にしている可能性があります。位置情報のトラッキングに関する詳細は、以下を参照されたい：
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/)

それでもサポートが必要な場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)を登録してください。

_最終更新日: 2022年11月16日_

