---
nav_title: 位置情報をチェックする
article_title: 位置情報をチェックする
page_order: 1
page_type: solution
description: "このヘルプ記事では、利用可能なロケーションを持つユーザーがいない場合に役立つクイックチェックを紹介する。"
tool: Location
---

# 位置情報をチェックする

Brazeは、SDKを通じてユーザーの最新の位置情報をデフォルトで取得する。これは通常、"最近の場所 "が、ユーザーが最も最近アプリを使用した場所であることを意味する。Brazeにバックグラウンドの位置情報を送信すれば、より詳細なデータを入手できるかもしれない。

利用可能なロケーションを持つユーザーがいない場合、2つの簡単なチェックでデータ収集と日付転送を確認することができる。

## データ収集

アプリが位置情報を収集していることを確認する：

- iOSの場合、これはユーザージャーニーのある時点で、ユーザがプロンプトを通じて位置情報の共有をオプトインすることを意味する。 
- アンドロイドの場合、アプリのインストール時に、位置情報の許可を細かく、または粗く要求されることを確認する。

ユーザーの位置情報がBrazeに送信されているかどうかを確認するには、**Location Available**フィルターを使用する。このフィルターによって、「最新の位置情報」を持つユーザーの割合を見ることができる。

![][25]

## データ転送

開発者が位置情報をBrazeに渡していることを確認する。通常、位置情報の受け渡しは、ユーザーが許可を与えた後にSDKによって自動的に処理されるが、開発者がBrazeで位置情報のトラッキングを無効にしている可能性がある。位置情報のトラッキングに関する詳細は、以下を参照されたい：
- \[Android][26]
- \[iOS][27]
- \[ウェブ][28]

まだ助けが必要か？[サポートチケットを]({{site.baseurl}}/braze_support/)開く。

_最終更新日：2022年11月16日_

[25]: {% image_buster /assets/img_archive/trouble7.png %}
[26]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/
[27]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/
