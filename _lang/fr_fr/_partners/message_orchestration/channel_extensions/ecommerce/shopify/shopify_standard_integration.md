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

## Étape 1 : Connectez votre boutique Shopify

1. Dans Braze, allez à **Intégrations de partenaires** > **Partenaires technologiques**, puis recherchez Shopify.

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

## Étape 2 : 





 
- 
    - 
- 
    - Suivre uniquement les utilisateurs identifiés
    - 

## Étape 3 : 

### 







|  | Événements personnalisés de Shopify | Attributs personnalisés de Shopify |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Produit vu</li><li></li><li></li><li></li></ul>{:/}  | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li></ul>{:/} | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li><li></li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}



### 

  





|  | Événements personnalisés de Shopify | Attributs standard de Braze |  |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li></li></ul>{:/}  | {::nomarkdown}<ul><li></li><li></li><li></li><li></li><li></li><li></li></li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Prénom</li><li>Nom de famille</li><li>Téléphone</li><li>Ville</li><li>Pays</li></ul>{:/} | {::nomarkdown}<ul><li></li><li></li></ul>{:/} |
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
      <th style="width: 50%;">Événements personnalisés</th>
      <th style="width: 50%;">Attributs personnalisés</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Utilisation d’un code de réduction personnalisé</li>
          <li>Interagir avec une recommandation produit personnalisée</li>
          <li>Ajouter un message de cadeau à leur commande</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marques ou produits favoris</li>
          <li>Catégories d’achat préférées</li>
          <li>Statut d’adhésion ou de fidélité</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

  

Par exemple, l’extrait de code JavaScript suivant détermine si l'utilisateur actuel s'abonne à un bulletin d’information et consigne cet événement en tant qu’événement personnalisé sur son profil dans Braze :

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

 

## Étape 4 : 

 



{% alert important %}
 <br><br>

-  Les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
-  Si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail de quelqu'un d'autre comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.
{% endalert %}

 

  



{% alert note %}
  <br><br>
-  
-  
{% endalert %}

## Étape 5 : 

  



## Étape 6 : 





### 



#### 

  

#### Notifications push Web

 



## Étape 7 : Terminer la configuration

1. Après avoir configuré votre intégration, sélectionnez **Terminer la configuration**.
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