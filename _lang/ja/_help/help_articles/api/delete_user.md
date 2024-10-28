---
nav_title: API を使用したユーザーの削除
article_title: API を使用したユーザーの削除
page_order: 0

page_type: reference
description: "このヘルプ記事では、Braze REST API を使用してユーザープロファイルを削除した場合の影響について説明します。"
tool: Dashboard
platform: API
---

# API によるユーザーの削除

[Braze REST API][1]でユーザーを削除すると、以下のデータが削除(null)されます。
- ユーザーが持っていたすべての属性
- メールアドレス
- 電話番号
- 外部ユーザー ID 
- 性別
- 国
- 言語

[Braze REST API][1] を使用してユーザーを削除すると、以下の事象が発生します。
- ユーザープロファイルは匿名化される。
- [\[生涯ユーザー数]][2] が更新され、新たに匿名化されたユーザーが考慮されます。	
- 匿名化されたユーザーは、集計コンバージョン率のタグにカウントされます。匿名ユーザーの場合は、カスタムイベントカウントと購入回数は更新されません。

## メールアドレスを共有する複数のプロファイル

同じメールアドレスを共有する複数のユーザープロファイルを結合するとします。 

これらのユーザープロファイルを結合するには:

 1. 重複するメールアドレスを持つユーザーを特定します。 
 2. 単一プロファイルの属性をすべてエクスポートします。 
 3. これらの属性s をAPI またはCSV を介してユーザープロファイルに読み込みます。 
 4. API を介してユーザーを削除します。基本的には、これらの重複ユーザーと上記のデータを削除します。

_最終更新日2023年9月13日_

[1]: {{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users
