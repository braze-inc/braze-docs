---
nav_title: API経由でユーザーを削除する
article_title: API経由でユーザーを削除する
page_order: 0

page_type: reference
description: "このヘルプ記事では、Braze REST API経由でユーザープロファイルを削除する意味について説明する。"
tool: Dashboard
platform: API
---

# API経由でユーザーを削除する

[Braze REST APIでユーザーを削除][1]すると、以下のデータが削除（NULL化）される：
- ユーザーが持っていたすべての属性
- メールアドレス
- 電話番号
- 外部ユーザー ID 
- 性別
- 国
- 言語

[Braze REST API経由でユーザーを削除][1]すると、以下のイベントが発生する：
- ユーザープロファイルは匿名化される。
- [生涯ユーザー][2]数は、新たに匿名化されたユーザーを考慮して更新される。	
- 匿名化されたユーザーは、集計されたコンバージョン率にカウントされる。カスタムイベントのカウントと購入カウントは、匿名化されたユーザーには更新されない。

## メールアドレスを共有する複数のプロファイル

同じメールアドレスを共有する複数のユーザープロファイルを統合したいとしよう。 

これらのユーザープロファイルを統合する：

 1. メールアドレスが重複しているユーザーを識別子で特定する。 
 2. 単一のプロファイルのすべての属性をエクスポートする。 
 3. これらの属性をAPIまたはCSV経由でユーザープロファイルにインポートする。 
 4. API経由でユーザーを削除し、重複ユーザーと上記のデータを削除する。

_最終更新日：2023年9月13日_

[1]: {{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users
