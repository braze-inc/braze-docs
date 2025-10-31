---
nav_title: "Configuration de l'intégration standard de Shopify"
article_title: "Configuration de l'intégration standard de Shopify"
description: "Cet article de référence explique comment mettre en place l'intégration standard de Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Configuration de l'intégration standard de Shopify

> Cette page vous explique comment intégrer Braze à Shopify à l'aide de notre intégration standard pour les utilisateurs disposant d'une boutique en ligne Shopify. Si vous utilisez un site Shopify headless ou si vous cherchez à mettre en place des solutions plus personnalisées, reportez-vous à la [configuration de l'intégration personnalisée de Shopify]({{site.baseurl}}/shopify_custom_integration/).

## Étape 1 : Connectez votre boutique Shopify

1. Dans Braze, allez à **Intégrations de partenaires** > **Partenaires technologiques**, puis recherchez Shopify.

{% alert note %}
Si vous utilisez l'ancienne navigation, vous trouverez les **partenaires technologiques** sous la rubrique **Intégrations**.
{% endalert %}

{: start="2"}
2\. Sur la page partenaire de Shopify, sélectionnez **Commencer la configuration** pour lancer le processus d'intégration.<br><br>![Page d'intégration de Shopify avec bouton pour commencer la configuration.]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3\. Dans la boutique d'applications de Shopify, installez l'application Braze.<br><br>![La page du magasin d'applications de Braze avec un bouton pour installer l'application.]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Si votre compte Shopify est associé à plusieurs boutiques, vous pouvez changer la boutique à laquelle vous êtes connecté en sélectionnant l'icône de la boutique en haut à droite de la page et en sélectionnant **Changer de boutique.**
{% endalert %}

{: start="4"}
4\. Après avoir installé l'appli Braze, vous serez redirigé vers Braze pour confirmer l'espace de travail que vous souhaitez connecter à Shopify. Une boutique Shopify ne peut se connecter qu'à un seul espace de travail. Si vous devez changer d'espace de travail, sélectionnez le bon espace de travail.<br><br>![Une fenêtre vous demandant de confirmer que vous êtes dans le bon espace de travail.]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\. Sélectionnez **Commencer la configuration**.<br><br>!["Paramètres d'intégration" avec un champ pour entrer le domaine et un bouton pour commencer la configuration.]({% image_buster /assets/img/Shopify/choose_account.png %})

## Étape 2 : Activer les SDK Web de Braze

Pour les boutiques en ligne Shopify, vous pouvez sélectionner la configuration standard pour mettre en œuvre automatiquement le SDK Web et le SDK JavaScript de Braze.

![Étape "Activer le SDK Web" avec des options de mise en œuvre par le biais d'une configuration standard ou personnalisée.]({% image_buster /assets/img/Shopify/sdk_setup.png %})

Après avoir sélectionné la configuration standard de l'onboarding, vous devrez choisir le moment où Braze doit s'initialiser et charger les SDK à partir de l'une des options suivantes : 
- Lors de la visite du site, par exemple au début de la session
    - Trace les utilisateurs identifiés et anonymes
- Lors de l'ouverture d'un compte, par exemple lors de l'identifiant du compte
    - Suivre uniquement les utilisateurs identifiés
    - Commence à suivre les données lorsque les visiteurs du site s'inscrivent ou se connectent à leur compte.

## Étape 3 : Configurez vos données Shopify

### Configuration standard des données

Vous allez maintenant sélectionner les données Shopify que vous souhaitez suivre.

![Section "Suivi des données Shopify" avec une case à cocher pour suivre les événements comportementaux et les attributs de l'utilisateur.]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

Les événements suivants sont activés par défaut dans l'intégration standard.

| Événements recommandés par Braze | Événements personnalisés de Shopify | Attributs personnalisés de Shopify |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Produit vu</li><li>Mise à jour du panier</li><li>L'encaissement a commencé</li><li>Commande passée</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

Pour plus d'informations sur les données suivies par l'intégration, consultez les [fonctionnalités des données de Shopify]({{site.baseurl}}/shopify_data_features/).

### Configuration du remblayage historique

Grâce à la configuration standard, vous avez la possibilité d'effectuer un chargement initial de vos clients et commandes Shopify des 90 derniers jours précédant votre connexion à l'intégration Shopify. Pour ce faire, cochez la case pour inclure le chargement initial des données dans votre intégration. 

![Données historiques basculer.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

Cette table contient les données qui seront initialement chargées par le biais du remblai.

| Événements recommandés par Braze | Événements personnalisés de Shopify | Attributs standard de Braze | État des abonnements à Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Commande passée</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Prénom</li><li>Nom de famille</li><li>Téléphone</li><li>Ville</li><li>Pays</li></ul>{:/} | {::nomarkdown}<ul><li>Abonnements au marketing par e-mail associés à cette boutique Shopify.</li><li>Abonnements au marketing parms associés à cette boutique Shopify.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

Lorsque vos enregistrements de clients Shopify sont chargés dans Braze, l'ID client Shopify sera utilisé comme ID externe de Braze. 

{% alert note %}
Si vous êtes un client existant de Braze avec des campagnes actives ou des Canvas, consultez les [fonctionnalités de données de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) pour plus de détails.
{% endalert %}

### (Avancé) Configuration personnalisée du suivi des données

Avec les SDK de Braze, vous pouvez suivre des événements personnalisés ou des attributs personnalisés qui vont au-delà des événements standard pour cette intégration. Les événements personnalisés capturent les interactions uniques dans votre magasin, comme par exemple :

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

Le suivi des données personnalisées vous permet d'obtenir des informations plus approfondies sur le comportement des utilisateurs et de personnaliser encore davantage leur expérience. Pour mettre en œuvre des événements personnalisés, vous devez modifier [le code du thème de votre vitrine](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) dans le fichier `theme.liquid`. Vous aurez peut-être besoin de l'aide de vos développeurs.

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

Le SDK doit être initialisé (à l'écoute de l'activité) sur l'appareil d'un utilisateur pour enregistrer des événements et des attributs personnalisés. Pour en savoir plus sur l'enregistrement des données personnalisées, reportez-vous à l'[objet User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) et à l'[objet logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## Étape 4 : Configurer la façon dont vous gérez les utilisateurs

Sélectionnez votre type de `external_id` dans le menu déroulant. 

![Section "Collecte des abonnés".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut contribuer à simplifier la gestion des identités dans l'ensemble de vos sources de données. Toutefois, il est important de prendre en compte les risques potentiels pour la confidentialité des utilisateurs et la sécurité des données.<br><br>

- **Informations à deviner :** Les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
- **Risque d'exploitation :** Si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail de quelqu'un d'autre comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.
{% endalert %}

Si vous avez sélectionné un type d'ID externe personnalisé, passez aux étapes 4.1 et 4.2. Sinon, passez à l'étape 4.3.

### Étape 4.1 : Créez un fichier personnalisé `external_id`

Tout d'abord, allez sur Shopify et créez le méta-champ `braze.external_id`. Nous vous recommandons de suivre les étapes de la section [Création de méta-champs personnalisés](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions). Pour l'**espace de noms et la clé**, entrez `braze.external_id`. Pour le **type**, nous vous recommandons de choisir un type d'ID.

Après avoir créé le métafichier, écoutez les [webhooks`customer/create` ](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) afin de pouvoir écrire le métafichier lorsqu'un nouveau client est créé. Ensuite, utilisez l'[API Admin](https://shopify.dev/docs/api/admin-graphql) ou l'[API Client](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour ajouter ce méta-champ à tous les clients que vous avez créés précédemment.

### Étape 4.2 : Créer un endpoint

Vous avez besoin d'un endpoint GET public pour récupérer votre ID externe. Si Shopify ne peut pas fournir le métafield, Braze appellera ce endpoint pour récupérer l'ID externe.

Voici un exemple d'endpoint : `https://mystore.com/custom_id?shopify_customer_id=1234&email_address=raghav.narain@braze.com&shopify_storefront=dev-store.myshopify.com`

#### Réponse

Braze attend un code de statut `200`. Tout autre code est considéré comme une défaillance de l'endpoint. La réponse devrait être :

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

Validez le site `shopify_customer_id` et l'adresse e-mail en utilisant l'API Admin ou l'API Client pour confirmer que les valeurs des paramètres correspondent aux valeurs du client dans Shopify. Après validation, vous pouvez également utiliser les API pour récupérer le métafichier `braze.external_id` et renvoyer la valeur de l'ID externe.

### Étape 4.3 : Recueillir vos abonnements par e-mail ou SMS depuis Shopify (facultatif).

Vous avez la possibilité de collecter vos abonnements marketing par e-mail ou par SMS depuis Shopify. 

Si vous utilisez les canaux e-mail ou SMS, vous pouvez synchroniser vos états d'abonnement au marketing parketeur sms et e-mail dans Braze. Si vous synchronisez des abonnements de marketing par e-mail depuis Shopify, Braze créera automatiquement un groupe d'abonnement e-mail pour tous les utilisateurs associés à ce magasin spécifique. Vous devez créer un nom unique pour ce groupe d'abonnement.

![Section "Collecte des abonnés" avec option de collecte des abonnements au marketing par e-mail ou par SMS.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Comme indiqué dans l'[aperçu de Shopify]({{site.baseurl}}/shopify_overview/), si vous souhaitez utiliser un formulaire de capture tiers, vos développeurs doivent intégrer le code SDK de Braze. Cela vous permettra de capturer l'adresse e-mail et l'état global de l'abonnement à l'e-mail à partir des soumissions de formulaire. Plus précisément, vous devez mettre en œuvre et tester ces méthodes dans votre fichier `theme.liquid`:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Définit l'adresse e-mail dans le profil utilisateur.
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Mise à jour de l'état de l'abonnement global à l'e-mail
{% endalert %}

## Étape 5 : Synchroniser les produits (facultatif)

Vous pouvez synchroniser tous les produits de votre boutique Shopify avec un catalogue Braze pour une personnalisation plus poussée des messages. Les mises à jour automatiques s'effectuent quasiment en temps réel, de sorte que votre catalogue reflète toujours les détails les plus récents sur les produits. Pour en savoir plus, consultez le site [Shopify product sync]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![Étape 4 du processus de configuration avec "Shopify Variant ID" comme "Catalog product identifier".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## Étape 6 : Activer les canaux (facultatif)

Vous pouvez activer les messages in-app sans faire appel à un développeur en les configurant dans votre configuration.

![Étape de configuration pour l'activation des canaux, l'option disponible étant l'envoi de messages dans le navigateur.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze recueille des informations sur les visiteurs, telles que les adresses e-mail et les numéros de téléphone, par le biais de messages dans le navigateur. Ces informations sont ensuite envoyées à Shopify. Ces données aident les commerçants à reconnaître les visiteurs de leur magasin et à créer une expérience d'achat plus personnalisée. Pour plus de détails, reportez-vous à l'[API visiteurs](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Prise en charge de canaux SDK supplémentaires

Les SDK de Braze permettent d'utiliser différents canaux de messages, notamment les cartes de contenu.

#### Cartes de contenu et drapeaux de fonctionnalité

Pour ajouter des cartes de contenu ou des drapeaux de fonctionnalité, vous devrez collaborer avec vos développeurs pour insérer le code SDK nécessaire directement dans votre fichier `theme.liquid`. Pour obtenir des instructions détaillées, reportez-vous à la section [Intégration SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Notifications push Web

L'intégration de Shopify ne prend actuellement pas en charge le Web Push. Si vous souhaitez que ce produit soit pris en charge à l'avenir, soumettez une demande de produit via le [portail des produits de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

Si vous souhaitez qu'il soit pris en charge à l'avenir, soumettez une demande de produit via le [portail des produits de]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) Braze.

## Étape 7 : Terminer la configuration

1. Après avoir configuré votre intégration, sélectionnez **Terminer la configuration**.
2. Activez l'intégration de l'application Braze dans les paramètres de votre thème Shopify. Sélectionnez **Open Shopify** pour être redirigé vers votre compte Shopify afin d'activer l'intégration de l'application dans les paramètres du thème de votre boutique. 

![Bannière indiquant que vous devez activer l'application Braze dans Shopify et contenant un bouton pour ouvrir Shopify.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\. Après avoir activé l'intégration de l'app, votre configuration est terminée !
Confirmez vous pouvez consulter vos paramètres d'intégration, l'état de la synchronisation initiale des données et vos événements Shopify actifs. <br><br>![Page partenaire de Shopify affichant les paramètres d'intégration.]({% image_buster /assets/img/Shopify/install_complete.png %})