---
nav_title: パブリックAPI
article_title: コネクテッドコンテンツのパブリック API
page_order: 4
description: "この記事では、コネクテッド・コンテンツで使用できる、一般に公開されているAPIのリストを取り上げる。"
---

# パブリックAPI

> 一般に公開されていて、コネクテッドコンテンツに利用可能な API には、さまざまなものがあります。パブリックAPIを使えば、メッセージにカスタムデータを挿入することができる。コネクテッドコンテンツに使用できると思われるパブリック API のリストをまとめました。しかし、世の中にはさらに多くの API があり、コネクテッドコンテンツをさまざまに使用できる可能性があります。  

共有したいAPIがある場合は、[success@braze.com](mailto:success@braze.com)までご連絡を！

{% alert note %}
パブリック API は、使用上の制約およびレート制限の対象になる可能性があります。 必ず API ドキュメントを通読し、御社の使用目的について API プロバイダーに問い合わせてください。
{% endalert %}

## ニュースと情報

|	 API 	| 説明 |
| --------- | --- |
| [OpenWeatherMap][7] | 現在の気象データ、5 日間と 16 日間の予報、および過去のデータを提供します。 |
| [NYT Article Search][8] | 見出し、トピック、URL、日付、抄録などを含めて、NYT の記事データを提供します。 |
| [The Guardian API][9] | 見出し、トピック、URL、日付、抄録などを含めて、Guardian の記事データを提供します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## イベントとチケット

|	 API 	| 説明 |
| --------- | --- |
| [SeatGeek][11]| コンサート、スポーツ、演劇などのチケット情報を提供する。  |
| [OnConnect][12] | 米国とカナダの映画館の興行成績と上映時間を提供する。 |
| [Eventbrite][19] | 様々な公共イベントのデータを提供する。 |
| [Eventful][20] | 様々な公共イベントのデータを提供する |
| [Ticketmaster][38] | 公共イベント、会場、料金に関するデータを提供します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 飲食

|  API  | 説明 |
| --------- | --- |
| [BreweryDB][40] | 醸造所、ビール、ビールのイベントに関する情報を提供します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ファイナンス

|  API  | 記述 |
| --------- | --- |
| [Barchart OnDemand][36] | 株式、先物、外国為替の各種データを提供する。 |
| [CoinDesk][37] | 様々な暗号通貨のデータを提供する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 健康

|  API  | 記述 |
| --------- | --- |
| [AirVisual][42] | 大気質と気象データを提供します。 |
| [Nutritionix Worlds][43] | 検証済みの栄養データを提供します。 |
| [USDA Nutrients][45] | 国立栄養素データベースへのアクセスを提供する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 音楽

|	 API 	| 記述 |
| --------- | --- |
| [Last.fm][14] | アーティスト情報、おすすめアーティストなど、さまざまな音楽データを提供する。 |
| [iTunes][24] | iTunes、App Store、iBooksストアの様々なアイテムのデータを提供する。 |
| [Bandsintown][13] | 地元のコンサート情報を提供し、ライブ音楽イベントを推薦する。 |
| [Songkick][22] | アーティスト、会場、場所などのライブ音楽情報を提供する。 |
| [Discogs][21] | アーティスト、レーベル、レコーディング情報を提供する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 製品情報

|	 API 	| 説明 |
| --------- | --- |
| [eBay][15] | アイテムデータ、人気検索などのライブeBayデータを提供する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## その他

|	 API 	| 記述 |
| --------- | --- |
| [Numbers API][18] | ランダムに数字のトリビアを提供する。 |
| [Clearbit][27] | 企業ロゴの画像を提供する。 |
| [ロンドン統一][28] [鉄道とニューヨーク市交通局][29] | 路線状況や到着時間など、リアルタイムの公共交通データを提供します。 |
| [日の出と日没][39] | 指定した緯度と経度の日没時刻と日の出時刻を提供する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[7]: http://openweathermap.org/api
[8]: https://developer.nytimes.com/docs/articlesearch-product/1/overview
[9]: http://open-platform.theguardian.com/documentation/
[11]: http://platform.seatgeek.com/
[12]: http://developer.tmsapi.com/docs/read/data_v1_1/movies/movie_showtimes
[13]: http://www.bandsintown.com/api/overview
[14]: http://www.last.fm/api
[15]: http://developer.ebay.com/devzone/shopping/docs/concepts/shoppingapiguide.html
[16]: [success@braze.com](mailto:success@braze.com)
[18]: http://numbersapi.com/
[19]: http://developer.eventbrite.com/
[20]: http://api.eventful.com/
[21]: http://www.discogs.com/developers/
[22]: http://www.songkick.com/developer
[24]: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
[27]: http://blog.clearbit.com/logo
[28]: http://api.tfl.gov.uk/#Line
[29]: https://new.mta.info/developers
[36]: https://www.barchartondemand.com/free
[37]: https://www.coindesk.com/api/
[38]: http://developer.ticketmaster.com/products-and-docs/apis/getting-started/
[39]: https://sunrise-sunset.org/api
[40]: http://www.brewerydb.com/
[42]: https://airvisual.com/api
[43]: https://developer.nutritionix.com/
[44]: https://open.fda.gov/api/
[45]: https://fdc.nal.usda.gov/api-guide.html
