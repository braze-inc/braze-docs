---
nav_title: ""
article_title: ""
description: ""
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# 

> 

## ステップ1:Shopify ストアを接続する

1. Braze で、**Partner Integrations**> **Technology Partners** に移動し、"Shopify" を検索します。





{: start="2"}
2\.<br><br><br><br> 
3\.<br><br>





{: start="4"}
4\.<br><br>


5\.<br><br>

## ステップ2: 





 
- 
    - 
- 
    - 識別されたユーザーのみを追跡
    - 

## ステップ 3:

### 







|  | Shopify カスタムイベントs | Shopifyカスタム属性 |
| --- | --- | --- |
| <ul><li>製品の閲覧</li><li></li><li></li><li></li></ul>  | <ul><li></li><li></li><li></li><li></li><li></li><li></li></ul> | <ul><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul> |




### 

 





|  | Shopify カスタムイベントs | Braze の標準属性項目 |  |
| --- | --- | --- | --- |
| <ul><li></li></ul>  | <ul><li></li><li></li><li></li><li></li><li></li><li></li></li></ul> | <ul><li>メール</li><li>名</li><li>姓</li><li>電話</li><li>市区町村</li><li>国</li></ul>{:/} | <ul><li></li><li></li></ul> |


 





### 



<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">カスタムイベント</th>
      <th style="width: 50%;">カスタム属性</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>カスタム割引コードの使用</li>
          <li>パーソナライズされたおすすめ商品とのインタラクション</li>
          <li>注文へのギフトメッセージの追加</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>お気に入りのブランドまたは製品</li>
          <li>優先ショッピングカテゴリ</li>
          <li>メンバーシップまたはロイヤルティステータス</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>



たとえば、次の JavaScript スニペットは、現在のユーザーがニュースレターを購読しているかどうかを追跡し、その情報を Braze のプロファイルにカスタムイベントとして記録します。

```json
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```



## ステップ 4:

 




<br><br>

- メールアドレスは推測されやすく、攻撃されやすい。
- 悪意のあるユーザーがWebブラウザーを改ざんし、他人のメールアドレスを外部IDとして送信した場合、機密メッセージやアカウント情報にアクセスされる可能性がある。


 






<br><br>
- 
- 


## ステップ 5: 





## ステップ6: 





### 



#### 

 

#### 





## ステップ 7:設定完了

1. 設定後、**Finish Setup**を選択します。
2.  




3\.
<br><br>


[2]: {% image_buster /assets/img/Shopify/confirm_workspace1.png %}
[3]: {% image_buster /assets/img/Shopify/sdk_setup.png %}
[4]: {% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %}
[5]: {% image_buster /assets/img/Shopify/shopify_log_in.png %}
[6]: {% image_buster /assets/img/Shopify/tracking_shopify_data.png %}
[7]: {% image_buster /assets/img/Shopify/open_shopify.png %}
[8]: {% image_buster /assets/img/Shopify/install_complete.png %}
[9]: {% image_buster /assets/img/Shopify/choose_account.png %}
[10]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[11]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}
[12]: {% image_buster /assets/img/Shopify/configure_settings.png %}
[13]: {% image_buster /assets/img/Shopify/collect_email_subscribers_2.png %}