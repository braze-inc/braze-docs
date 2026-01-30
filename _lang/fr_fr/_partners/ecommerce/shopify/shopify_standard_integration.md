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
4\. Après avoir installé l'appli Braze, vous serez redirigé vers Braze pour confirmer l'espace de travail que vous souhaitez connecter à Shopify. Une boutique Shopify ne peut se connecter qu'à un seul espace de travail. Si vous devez changer d'espace de travail, sélectionnez le bon espace de travail.<br><br>![Une fenêtre vous demande de confirmer que vous êtes dans le bon espace de travail.]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\. Sélectionnez **Commencer la configuration**.<br><br>!["Paramètres d'intégration" avec un champ pour entrer le domaine et un bouton pour commencer la configuration.]({% image_buster /assets/img/Shopify/choose_account.png %})

## Étape 2 : Activer les SDK Web de Braze

Pour les boutiques en ligne Shopify, vous pouvez sélectionner la configuration standard pour mettre en œuvre automatiquement le SDK Web et le SDK JavaScript de Braze.

![L'étape "Activer le SDK Web" avec des options de mise en œuvre via une configuration standard ou personnalisée.]({% image_buster /assets/img/Shopify/sdk_setup.png %})

Après avoir sélectionné la configuration standard de l'onboarding, vous devrez choisir le moment où Braze doit s'initialiser et charger les SDK à partir de l'une des options suivantes : 
- Lors de la visite du site, par exemple au début de la session
    - Trace les utilisateurs identifiés et anonymes
- Lors de l'ouverture d'un compte, par exemple lors de l'identifiant du compte
    - Suivre uniquement les utilisateurs identifiés
    - Commence à suivre les données lorsque les visiteurs du site s'inscrivent ou se connectent à leur compte.

## Étape 3 : Configurez vos données Shopify

### Configuration standard des données

Vous allez maintenant sélectionner les données Shopify que vous souhaitez suivre.

!["Tracking Shopify data" section avec une case à cocher pour suivre les événements comportementaux et les attributs de l'utilisateur.]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

Les événements suivants sont activés par défaut dans l'intégration standard.

| Événements recommandés par Braze | Événements personnalisés de Shopify | Attributs personnalisés de Shopify |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Produit vu</li><li>Mise à jour du panier</li><li>L'encaissement a commencé</li><li>Commande passée</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

Pour plus d'informations sur les données suivies par l'intégration, consultez les [fonctionnalités des données de Shopify]({{site.baseurl}}/shopify_data_features/).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

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

Le suivi des données personnalisées permet d'obtenir des informations plus approfondies sur le comportement des clients et favorise une personnalisation supplémentaire. Pour mettre en œuvre des événements personnalisés, vous devez modifier [le code du thème de votre vitrine](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) dans le fichier `theme.liquid`. Vous aurez peut-être besoin de l'aide de vos développeurs.

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

## Étape 4 : Configurer la façon dont vous gérez les utilisateurs {#step-4}

Sélectionnez votre type de `external_id` dans le menu déroulant. 

![Section "Recueillir les abonnés".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut simplifier la gestion des identités dans l'ensemble de vos sources de données. Toutefois, il est important de prendre en compte les risques potentiels pour la confidentialité des utilisateurs et la sécurité des données.<br><br>

- **Informations à deviner :** Les adresses e-mail sont facilement devinables, ce qui les rend vulnérables aux attaques.
- **Risque d'exploitation :** Si un utilisateur malveillant modifie son navigateur web pour envoyer l'adresse e-mail de quelqu'un d'autre comme ID externe, il pourrait potentiellement accéder à des messages sensibles ou à des informations de compte.
{% endalert %}

Par défaut, Braze convertit automatiquement les e-mails provenant de Shopify en minuscules avant de les utiliser comme ID externe. Si vous utilisez l'e-mail ou l'e-mail haché comme ID externe, vérifiez que vos adresses e-mail sont également converties en minuscules avant de les attribuer comme ID externe ou de les hacher à partir d'autres sources de données. Cela permet d'éviter les divergences dans les ID externes et de ne pas créer de profils utilisateurs en double dans Braze.

{% alert note %}
Les étapes suivantes dépendent de votre sélection d'ID externe :<br><br>
- **Si vous avez sélectionné un type d'ID externe personnalisé :** Effectuez les étapes 4.1-4.3 pour mettre en place votre configuration d'ID externe personnalisé.
- **Si vous avez sélectionné l'ID du client Shopify, l'e-mail ou l'e-mail haché :** Sautez les étapes 4.1-4.3 et passez directement à l'étape 4.4.
{% endalert %}

### Étape 4.1 : Créez le méta-champ `braze.external_id` 

1. Dans le panneau d'administration de Shopify, allez dans **Paramètres** > **Métafields et métaobjets**.
2. Sélectionnez **Clients** > **Ajouter une définition**.
3. Pour **Nom**, entrez `braze.external_id`. 
4. Sélectionnez l'espace de noms et la clé générés automatiquement (`custom.braze_external_id`) pour les modifier et les remplacer par `braze.external_id`.
5. Pour **Type**, sélectionnez **Type d'ID.**

Une fois le métafichier créé, remplissez-le pour vos clients. Nous recommandons les approches suivantes :

- **Écouter les webhooks de création de clients :** Mettez en place un webhook pour écouter les [événements`customer/create` ](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Cela vous permet d'écrire le méta-champ lors de la création d'un nouveau client.
- **Renforcer la clientèle existante :** Utilisez l'[API Admin](https://shopify.dev/docs/api/admin-graphql) ou l'[API Client](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour remplir le métafichier pour les clients précédemment créés.

### Étape 4.2 : Créer un endpoint pour récupérer votre ID externe

Vous devez créer un endpoint public que Braze peut appeler pour récupérer l'ID externe. Cela permet à Braze de récupérer l'ID dans des scénarios où Shopify ne peut pas fournir directement le métafield `braze.external_id`.

#### Spécifications des endpoints

**Méthode :** GET

Braze envoie les paramètres suivants à votre endpoint :

| Paramètre            | Requis | Type de données | Description                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | Oui      | Chaîne de caractères    | L'ID du client Shopify.                                         |
| shopify_storefront   | Oui      | Chaîne de caractères    | Le nom de la vitrine pour la demande. Ex : `<storefront_name>.myshopify.com` |
| email_address        | Non       | Chaîne de caractères    | L'adresse e-mail de l'utilisateur connecté. <br><br>Ce champ peut être manquant dans certains scénarios de webhook. Votre logique d'endpoint doit prendre en compte les valeurs nulles (par exemple, récupérer l'e-mail en utilisant shopify_customer_id si votre logique interne l'exige). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Exemple d'endpoint

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

#### Réponse attendue
Braze attend un code de statut `200` renvoyant le JSON de l'ID externe :
```json
{
  "external_id": "my_external_id"
}
```

#### Validation
Il est essentiel de valider que les adresses `shopify_customer_id` et `email_address` (le cas échéant) correspondent aux valeurs du client dans Shopify. Vous pouvez utiliser l'[API d'administration de Shopify](https://shopify.dev/docs/api/admin-graphql) ou l'[API client](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) pour valider ces paramètres et récupérer le métafichier `braze.external_id` correct.

#### Comportement en cas d'échec et fusion
Tout code d'état autre que `200` est considéré comme un échec.

- **Fusionner les implications :** Si l'endpoint échoue (retour non`200` ou dépassement de délai), Braze ne peut pas récupérer l'ID externe. Par conséquent, la fusion entre le profil utilisateur Shopify et le profil utilisateur Braze ne se fera pas à ce moment-là.
- **Logique de réessai :** Braze peut effectuer des tentatives immédiates standard sur le réseau, mais si l'échec persiste, la fusion sera reportée jusqu'au prochain événement admissible (par exemple, la prochaine fois que l'utilisateur mettra à jour son profil ou effectuera un paiement).
- **Possibilité de prise en charge :** Pour permettre la fusion des utilisateurs en temps voulu, assurez-vous que votre endpoint est hautement disponible et qu'il gère le champ facultatif `email_address` de manière gracieuse.

### Étape 4.3 : Saisissez votre ID externe

Répétez l'[étape 4](#step-4) et saisissez l'URL de votre endpoint après avoir sélectionné l'ID externe personnalisé comme type d'ID externe Braze.

#### Considérations

- Si votre ID externe n'est pas généré lorsque Braze envoie une requête à votre endpoint, l'intégration utilisera par défaut l'ID du client Shopify lorsque la fonction `changeUser` sera appelée. Cette étape est cruciale pour fusionner le profil de l'utilisateur anonyme avec le profil de l'utilisateur identifié. Par conséquent, il peut y avoir une période temporaire pendant laquelle différents types d'ID externes existent dans votre espace de travail.
- Lorsque l'ID externe est disponible dans le métafichier `braze.external_id`, l'intégration donnera la priorité à cet ID externe et l'attribuera. 
    - Si l'ID personnalisé de Shopify était précédemment défini comme l'ID externe de Braze, il sera remplacé par la valeur du métafield `braze.external_id`. 

### Étape 4.4 : Recueillir vos abonnements par e-mail ou SMS depuis Shopify (facultatif).

Vous avez la possibilité de collecter vos abonnements marketing par e-mail ou par SMS depuis Shopify. 

Si vous utilisez les canaux e-mail ou SMS, vous pouvez synchroniser vos états d'abonnement au marketing parketeur sms et e-mail dans Braze. Si vous synchronisez des abonnements de marketing par e-mail depuis Shopify, Braze créera automatiquement un groupe d'abonnement e-mail pour tous les utilisateurs associés à ce magasin spécifique. Vous devez créer un nom unique pour ce groupe d'abonnement.

![Section "Collecte des abonnés" avec option de collecte des opt-ins de marketing par e-mail ou SMS.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Comme indiqué dans l'[aperçu de Shopify]({{site.baseurl}}/shopify_overview/), si vous souhaitez utiliser un formulaire de capture tiers, vos développeurs doivent intégrer le code SDK de Braze. Cela vous permettra de capturer l'adresse e-mail et l'état global de l'abonnement à l'e-mail à partir des soumissions de formulaire. Plus précisément, vous devez mettre en œuvre et tester ces méthodes dans votre fichier `theme.liquid`:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Définit l'adresse e-mail dans le profil utilisateur.
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Mise à jour de l'état de l'abonnement global à l'e-mail
{% endalert %}

## Étape 5 : Synchroniser les produits (facultatif)

Vous pouvez synchroniser tous les produits de votre boutique Shopify avec un catalogue Braze pour une personnalisation plus poussée des messages. Les mises à jour automatiques s'effectuent quasiment en temps réel, de sorte que votre catalogue contient des informations actualisées sur les produits. Pour en savoir plus, consultez le site [Shopify product sync]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![Étape 4 du processus de configuration avec "Shopify Variant ID" comme "Catalog product identifier".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## Étape 6 : Activer les canaux (facultatif)

Vous pouvez activer les messages in-app sans faire appel à un développeur en les configurant dans votre configuration.

![Étape de configuration pour l'activation des canaux, l'option disponible étant l'envoi de messages dans le navigateur.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze recueille des informations sur les visiteurs, telles que les adresses e-mail et les numéros de téléphone, par le biais de messages dans le navigateur. Ces informations sont envoyées à Shopify. Ces données permettent aux commerçants de reconnaître les visiteurs de leur magasin et de créer une expérience d'achat plus personnalisée. Pour plus de détails, reportez-vous à l'[API visiteurs](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Prise en charge de canaux SDK supplémentaires

Les SDK de Braze permettent d'utiliser différents canaux de messages, notamment les cartes de contenu.

#### Cartes de contenu et drapeaux de fonctionnalité

Pour ajouter des cartes de contenu ou des drapeaux de fonctionnalité, vous devrez collaborer avec vos développeurs pour insérer le code SDK nécessaire directement dans votre fichier `theme.liquid`. Pour obtenir des instructions détaillées, reportez-vous à la section [Intégration SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Notifications push Web

Le Web push n'est actuellement pas pris en charge pour l'intégration Shopify. Pour demander de l'aide, soumettez une demande de produit via le [portail des produits de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Étape 7 : Terminer la configuration

1. Après avoir configuré votre intégration, sélectionnez **Terminer la configuration**.
2. Activez l'intégration de l'application Braze dans les paramètres de votre thème Shopify. Sélectionnez **Open Shopify** pour être redirigé vers votre compte Shopify afin d'activer l'intégration de l'application dans les paramètres du thème de votre boutique. 

![Bannière indiquant que vous devez activer l'intégration de l'application Braze dans Shopify et contenant un bouton pour ouvrir Shopify.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\. Après avoir activé l'intégration de l'app, votre configuration est terminée !
Confirmez vous pouvez consulter vos paramètres d'intégration, l'état de la synchronisation initiale des données et vos événements Shopify actifs. <br><br>![Page partenaire de Shopify affichant les paramètres d'intégration.]({% image_buster /assets/img/Shopify/install_complete.png %})