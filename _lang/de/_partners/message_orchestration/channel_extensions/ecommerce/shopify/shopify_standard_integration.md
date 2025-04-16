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

## Schritt 1: 

1. 

{% alert note %}

{% endalert %}

{: start="2"}
2\. <br><br><br><br> 
3\. <br><br>

{% alert note %}

{% endalert %}

{: start="4"}
4\.   <br><br>

{: start="5"}
5\. <br><br>

## Schritt 2: 





 
- 
    - 
- 
    - Nur identifizierte Nutzer:innen verfolgen
    - 

## Schritt 3: 

### 







|  |  | Angepasste Shopify-Attribute |
| --- | --- | --- |
| {::nomarkdown}<ul><li></li><li></li><li></li><li></li></ul>{:/}  | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li></ul>{:/} | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}



### 

  





|  |  |  |  |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li></li></ul>{:/}  | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li></li></ul>{:/} | {::nomarkdown}<ul><li>E-Mail</li><li>Vorname</li><li>Nachname</li><li>Telefon</li><li>Ort</li><li>Land</li></ul>{:/} | {::nomarkdown}<ul><li></li><li></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

 

{% alert note %}

{% endalert %}

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
      <th style="width: 50%;">Angepasste Events</th>
      <th style="width: 50%;">Angepasste Attribute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Einen angepassten Rabattcode verwenden</li>
          <li>Mit personalisierter Produktempfehlung interagiert</li>
          <li>Der Bestellung eine Geschenkbotschaft beifügen</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Bevorzugte Marken oder Produkte</li>
          <li>Bevorzugte Einkaufskategorien</li>
          <li>Zugehörigkeit oder Treuestatus</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

  

Das folgende JavaScript-Snippet verfolgt zum Beispiel, ob der:die aktuelle Nutzer:in einen Newsletter abonniert hat, und protokolliert dies als angepasstes Event im individuellen Nutzerprofil in Braze:

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

 

## Schritt 4: 

 



{% alert important %}
 <br><br>

-  
-  
{% endalert %}

 

  



{% alert note %}
  <br><br>
-  
-  
{% endalert %}

## Schritt 5: 

  



## Schritt 6: 





### 



#### 

  

#### 

 



## Schritt 7: Einrichtung abschließen

1. 
2.   



{: start="3"}
3\. 
 <br><br>

[1]: {% image_buster /assets/img/Shopify/begin_setup.png %}
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