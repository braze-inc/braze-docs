---
nav_title: Pour commencer
article_title: "Démarrer avec Shopify"
description: "Cet article de référence explique comment mettre en œuvre le SDK Web Braze sur votre site web Shopify."
page_type: partner
search_tag: Partner
alias: /getting_started_shopify/
page_order: 1
---

# Démarrer avec Shopify

> Cet article explique comment mettre en œuvre le SDK Web Braze sur votre site web Shopify. Après la mise en œuvre, consultez la rubrique [Paramétrage de Shopify]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify) pour savoir comment terminer le paramétrage de l'intégration de Shopify à Braze.

## Liste de contrôle de la configuration de l'intégration

1. [Mettre en œuvre le SDK Web de Braze](#implement-web-sdk)
2. [Configurer Shopify dans Braze]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)
3. Testez l'intégration de Shopify

## Mise en œuvre du SDK Web sur votre site Shopify {#implement-web-sdk}

Le [SDK Web de Braze]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/) est un outil puissant utilisé pour suivre le comportement des clients de votre boutique Shopify. Avec le SDK Web, vous pouvez collecter des données de session, identifier les utilisateurs et enregistrer des données comportementales à partir d'un navigateur web ou mobile. Vous pouvez également débloquer les canaux de communication natifs comme les messages dans le navigateur.

Bien que l'intégration de Shopify offre un ensemble robuste de fonctionnalités par défaut, gardez à l'esprit que si vous avez des cas d'utilisation pour ajouter un suivi sur site pour des [événements non pris en charge par l'intégration de Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_in_braze/) ou si vous souhaitez ajouter des canaux tels que des [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), vous devez déployer le SDK Web directement sur votre site Shopify.

Avant de commencer l'onboarding de l'intégration, veuillez examiner les points suivants avec votre équipe afin de déterminer la marche à suivre pour mettre en œuvre le SDK Web.

### Fonctionnalités prises en charge

|Icône| Définition 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="Soutenu"></i><span class="sr-only">Soutenu</span> | Soutenu
|<i aria-hidden="true" class="fas fa-times" title="Non pris en charge"></i><span class="sr-only">Supporté</span> | Non pris en charge
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| Fonctionnalités | SDK Web via Shopify ScriptTag | Intégration SDK web directe via theme.liquid | Intégration SDK web directe via Shopify Hydrogen
|-------------|-------------|-------------|------------
| Suivi sur site par défaut      | <i class="fas fa-check" title="Soutenu"></i> | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-times" title="Non pris en charge"></i>          
| Rapprochement des utilisateurs de formulaires de capture (peu de travaux d'ingénierie sont nécessaires)   | <i class="fas fa-check" title="Soutenu"></i> | <i class="fas fa-check" title="Soutenu"></i> | <i class="fas fa-times" title="Non pris en charge"></i> 
| Rapprochement des utilisateurs au moment du paiement     | <i class="fas fa-check" title="Soutenu"></i>  | <i class="fas fa-times" title="Non pris en charge"></i>   | <i class="fas fa-times" title="Non pris en charge"></i>                                        
| Produit vu<br> Produit cliqué<br> Panier abandonné   | <i class="fas fa-check" title="Soutenu"></i> |<i class="fas fa-check" title="Soutenu"></i> | <i class="fas fa-times" title="Non pris en charge"></i> 
| Paiement abandonné<br> Ordre créé<br> Achat Braze<br> Commande payée<br> Commande partiellement satisfaite<br> Commande exécutée<br> Commande annulée<br> Remboursement créé<br> Création et mise à jour de clients | <i class="fas fa-check" title="Soutenu"></i> | <i class="fas fa-check" title="Soutenu"></i> | <i class="fas fa-check" title="Soutenu"></i>
| Remblai historique | <i class="fas fa-check" title="Soutenu"></i>  | <i class="fas fa-check" title="Soutenu"></i>  | <i class="fas fa-check" title="Soutenu"></i>  
| Synchronisation du catalogue  |<i class="fas fa-check" title="Soutenu"></i> |<i class="fas fa-check" title="Soutenu"></i>  |<i class="fas fa-check" title="Soutenu"></i>
| Collecte d'abonnés par e-mail et SMS    | <i class="fas fa-check" title="Soutenu"></i>| <i class="fas fa-check" title="Soutenu"></i>  | <i class="fas fa-check" title="Soutenu"></i>     
| Prise en charge des messages in-app par défaut   | <i class="fas fa-check" title="Soutenu"></i>  | <i class="fas fa-check" title="Soutenu"></i>  | <i class="fas fa-times" title="Non pris en charge"></i>     
| Prise en charge des cartes contenu par défaut   | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-times" title="Non pris en charge"></i>   
| Prise en charge par défaut du web push     | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-times" title="Non pris en charge"></i> | <i class="fas fa-times" title="Non pris en charge"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}
{% tab Shopify ScriptTag %}

### Mise en œuvre du Braze Web SDK via Shopify ScriptTag

[Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) est un code JavaScript à distance chargé dans les pages de votre boutique ou la page de statut de la commande. Lorsqu'une page de boutique est chargée, Shopify vérifie si des étiquettes de script doivent être chargées sur la page du site. 

Si vous souhaitez démarrer rapidement avec Braze, vous avez la possibilité d'autoriser Braze à charger un script prédéfini pour le SDK Web de Braze directement sur le site de votre boutique Shopify.

{% alert important %}
Le script prédéfini du SDK Braze Web pour cette méthode d'intégration n'est pas personnalisable.
{% endalert %}

#### Fonctionnement de l'intégration avec Shopify

Lorsque votre site Shopify est chargé, Shopify vérifie si des balises de script doivent être chargées sur la page. Au cours du processus, les scripts du Braze Web SDK seront chargés sur les pages de votre boutique ou sur la page de statut de la commande. 

Nous ajouterons également des scripts prédéfinis si vous avez sélectionné des événements de produit consulté, de produit cliqué et de panier abandonné qui nécessitent Shopify ScriptTag ou un message in-app en tant que canal de communication.  

#### Comment activer

Pour activer automatiquement les scripts du SDK Braze Web dans le cadre de votre intégration, sélectionnez les événements Shopify ScriptTag pris en charge ou activez l'envoi de messages in-app en tant que canal lors de la [configuration de l’intégration Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/). 

Depuis le compositeur de configuration de Shopify, les événements signalés par un astérisque (\*) sont pris en charge par le SDK Web. Si vous sélectionnez ces événements ou incluez l'envoi de messages dans le navigateur, Braze ajoutera la mise en œuvre du SDK Web via Shopify ScriptTag à votre boutique Shopify dans le cadre de votre configuration.

#### Formulaires de capture d'e-mail Shopify et réconciliation des utilisateurs. 

Les formulaires de capture permettent d'obtenir des informations identifiables sur le client dès le début de son cycle de vie, en vue de l'envoi de messages et de l'engagement en aval. 

Le SDK Web suit le comportement des sites Shopify et des utilisateurs anonymes en utilisant le paramètre `device_id`. L'intégration de Braze Shopify ScriptTag attribue les e-mails provenant des formulaires de capture d'e-mails de Shopify, comme l'inscription à une newsletter, au paramètre `device_id` de l’utilisateur.

Les formulaires de capture d'e-mail les plus courants sont les suivants : 
- Formulaire de capture d'e-mail 
- Formulaire d'inscription à la lettre d'information

Il y a deux façons de rapprocher l'e-mail de l'utilisateur et `device_id` : 
- Utilisation du script de capture d'e-mail automatisé de Braze 
- Appel des méthodes `setEmail` ou `setPhoneNumber` 

##### Capturer les inscriptions par e-mail ou par téléphone

Avec Braze, vous pouvez utiliser nos formulaires d'inscription [par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) et par [SMS et WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) pour exploiter le SDK Web et les messages in-app. 

Si vous utilisez une capture par e-mail ou par numéro de téléphone de Shopify, ou un formulaire de capture tiers, vous pouvez être défini directement sur l'utilisateur qui est suivi par le SDK Web de Braze. Par exemple, si vous obtenez l'adresse e-mail du client, vous pouvez la définir sur son profil utilisateur comme suit :

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Pour plus de détails sur le paramétrage de ces valeurs, reportez-vous à ces ressources Javascript :

- Définition de l'[e-mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) de l'utilisateur
- Définition du [numéro de téléphone](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) de l'utilisateur

Vous pouvez également définir l'état de l'abonnement des utilisateurs lorsque vous recueillez leur e-mail ou leur numéro de téléphone, comme ceci :

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Pour plus de détails sur le paramétrage de ces valeurs, reportez-vous à ces ressources Javascript :

- Définition du [type d'abonnement aux notifications par e-mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) de l'utilisateur
- Ajout de l'utilisateur à un [groupe d'abonnement](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Exemple de déploiement d'un formulaire de capture tiers**

1. Dans `theme.liquid`, copiez l'extrait de code suivant dans `head tag` :

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. Nous appelons d'abord `setInterval` pour que le script soit chargé en premier
3\. Remplacez `{FORM_ID}` par l'ID de l'élément du formulaire que vous souhaitez capturer
(comme "ContactFooter").
4\. Remplacez `{INPUT_EMAIL_ID}` par l'ID de l'élément du champ d'entrée de l'e-mail dans le formulaire.
5\. Lorsque le formulaire est soumis, le script appelle `setEmail` avec la valeur de l'e-mail.
6\. Après le chargement du script, nous appelons `clearInterval` pour qu'il ne se charge qu'une seule fois

{% alert note %}
Pour l'instant, le formulaire de capture d'e-mail de Braze ne permet pas de créer un client Shopify. Par conséquent, vous pourriez avoir des profils utilisateurs Braze sans profils utilisateurs Shopify associés jusqu'à ce que le client paie ou crée un compte.
{% endalert %}

#### À quoi s'attendre après la mise en œuvre

**Initialisation du SDK Web de Braze**

Le SDK Web s'initialise au démarrage de la session. Braze devra collecter le paramètre `device_id` pour le suivi des données utilisateur anonymes, car d'autres identifiants tels que l'ID du client Shopify, l'e-mail ou le numéro de téléphone peuvent ne pas être facilement disponibles pour les visiteurs invités de votre boutique Shopify.

Le site `device_id` sera également utilisé pour rapprocher les données de l'utilisateur du profil utilisateur anonyme lorsqu'un client fournit des informations plus identifiables (telles qu'une adresse e-mail ou un numéro de téléphone) après le processus de paiement.

**Version du SDK Web Braze**

La version actuelle du SDK Braze Currents via l'intégration Shopify ScriptTag est la v4.2.

**Utilisateurs actifs mensuels (MAU)**

Le SDK Web assure le suivi des sessions de vos clients et invités Shopify. Par conséquent, ces données seront comptabilisées comme MAU dans votre tableau de bord de Braze et seront prises en compte dans vos attributions de MAU. Il est important de noter que les utilisateurs anonymes seront également pris en compte dans votre MAU. Pour les appareils mobiles, les utilisateurs anonymes dépendent de l'appareil. Pour les utilisateurs Web, les utilisateurs anonymes dépendent du cache du navigateur.

{% endtab %}

{% tab thème liquid %}

### Le déploiement du SDK Web directement sur le theme.liquid de votre site Shopify. 

Braze permet de déployer le SDK Web de plusieurs façons, notamment :
- Ajouter le SDK Web directement à votre fichier Shopify `theme.liquid` 
- Google Tag Manager 

Si le SDK Web est déjà installé sur votre boutique Shopify, vous pouvez toujours procéder à la configuration du Shopify ScriptTag dans le cadre du processus d'onboarding. 

Au cours du processus d'installation, Braze vérifie si des instances du SDK Web sont déjà disponibles sur votre boutique Shopify. S'il existe déjà un déploiement, Braze ne chargera pas les scripts prédéfinis pour activer le SDK Web. Nous ajouterons ensuite les scripts nécessaires pour que vous puissiez suivre les événements sélectionnés ou activer l'envoi de messages dans le navigateur.

#### Comment activer

Pour mettre en œuvre manuellement le SDK Web, consultez la rubrique [Configuration initiale du SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/). Pour mettre en œuvre le SDK Web via Google Tag Manager, consultez [Google Tag Manager pour le Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager). 

Quel que soit le mode de mise en œuvre, assurez-vous que l'intégration de votre SDK Web comprend les éléments suivants, faute de quoi l'intégration de Shopify ne sera pas prise en charge : 
- Version v4.0+ du SDK Web
- Le SDK Web s'initialise au démarrage de la session

#### Formulaires de capture d'e-mail Shopify et réconciliation des utilisateurs. 

Les formulaires de capture permettent d'obtenir des informations identifiables sur le client dès le début de son cycle de vie, en vue de l'envoi de messages et de l'engagement en aval. 

Le SDK Web suit le comportement des sites Shopify et des utilisateurs anonymes en utilisant le paramètre `device_id`. L'intégration de Braze Shopify ScriptTag attribue les e-mails provenant des formulaires de capture d'e-mails de Shopify, comme l'inscription à une newsletter, au paramètre `device_id` de l’utilisateur.

Les formulaires de capture d'e-mail les plus courants sont les suivants : 
- Formulaire de capture d'e-mail 
- Formulaire d'inscription à la lettre d'information

Il y a deux façons de rapprocher l'e-mail de l'utilisateur et `device_id` : 
- Utilisation du script de capture d'e-mail automatisé de Braze 
- Appel des méthodes `setEmail` ou `setPhoneNumber` 

##### Capturer les inscriptions par e-mail ou par téléphone

Avec Braze, vous pouvez utiliser nos formulaires d'inscription [par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) et par [SMS et WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) pour exploiter le SDK Web et les messages in-app. 

Si vous utilisez une capture par e-mail ou par numéro de téléphone de Shopify, ou un formulaire de capture tiers, vous pouvez être défini directement sur l'objet de l'utilisateur qui est suivi par le SDK Web de Braze. Par exemple, si vous obtenez l'adresse e-mail du client, vous pouvez la définir sur son profil utilisateur comme suit :

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Pour plus de détails sur le paramétrage de ces valeurs, reportez-vous à ces ressources Javascript :

- Définition de l'[e-mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) de l'utilisateur
- Définition du [numéro de téléphone](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) de l'utilisateur

Vous pouvez également définir l'état de l'abonnement des utilisateurs lorsque vous recueillez leur e-mail ou leur numéro de téléphone :

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Pour plus de détails sur le paramétrage de ces valeurs, reportez-vous à ces ressources Javascript :

- Définition du [type d'abonnement aux notifications par e-mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) de l'utilisateur
- Ajout de l'utilisateur à un [groupe d'abonnement](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Exemple de déploiement d'un formulaire de capture tiers**

1. Dans `theme.liquid`, copiez l'extrait de code suivant dans `head tag` :

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. Nous appelons d'abord `setInterval` pour que le script soit chargé en premier
3\. Remplacez `{FORM_ID}` par l'ID de l'élément du formulaire que vous souhaitez capturer
(comme "ContactFooter").
4\. Remplacez `{INPUT_EMAIL_ID}` par l'ID de l'élément du champ d'entrée de l'e-mail dans le formulaire.
5\. Lorsque le formulaire est soumis, le script appelle `setEmail` avec la valeur de l'e-mail.
6\. Après le chargement du script, nous appelons `clearInterval` pour qu'il ne se charge qu'une seule fois

{% alert note %}
Pour l'instant, le formulaire de capture d'e-mail de Braze ne permet pas de créer un client Shopify. Par conséquent, vous pourriez avoir des profils utilisateurs Braze sans profils utilisateurs Shopify associés jusqu'à ce que le client paie ou crée un compte.
{% endalert %}

#### À quoi s'attendre après l'intégration ?

**Initialisation du SDK Web de Braze**

Le SDK Web s'initialise au démarrage de la session. Braze devra collecter le paramètre `device_id` pour le suivi des données utilisateur anonymes, car d'autres identifiants tels que l'ID du client Shopify, l'e-mail ou le numéro de téléphone peuvent ne pas être facilement disponibles pour les visiteurs invités de votre boutique Shopify.

Le site `device_id` sera également utilisé pour rapprocher les données de l'utilisateur du profil utilisateur anonyme lorsqu'un client fournit des informations plus identifiables (telles que son e-mail ou son numéro de téléphone) pendant et après le processus de paiement.

**Version du SDK Web Braze**

La version actuelle du SDK Braze Currents doit être la v4.0+.

**Utilisateurs actifs mensuels (MAU)**

Le SDK Web assure le suivi des sessions de vos clients et invités Shopify. Par conséquent, ces données seront comptabilisées comme MAU dans votre tableau de bord de Braze et seront prises en compte dans vos attributions de MAU. Il est important de noter que les utilisateurs anonymes seront également pris en compte dans votre MAU. Pour les appareils mobiles, les utilisateurs anonymes dépendent de l'appareil. Pour les utilisateurs Web, les utilisateurs anonymes dépendent du cache du navigateur.

{% endtab %}
{% tab Site Shopify headless %}

### Mise en œuvre du SDK Web directement sur votre site Shopify headless. {#headless-site}

L'intégration de Braze Shopify ScriptTag est incompatible avec les sites Shopify sans tête. Par conséquent, vous ne pourrez pas obtenir une prise en charge par défaut des événements produit consulté, produit cliqué ou panier abandonné, ni activer l'envoi de messages in-app par le biais de nos scripts prédéfinis. 

#### Comment activer

Pour intégrer directement le SDK Web à votre site Shopify sans tête, reportez-vous à la section [Configuration du SDK Web.]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)

Assurez-vous que votre intégration SDK Web comprend les éléments suivants : 
- La version du SDK Web doit être v4.0+.
- Le SDK Web s'initialise au démarrage de la session

#### Mise en place de formulaires Shopify pour la réconciliation des utilisateurs

Les marques de commerce électronique ont probablement des expériences sur leur site Shopify conçues pour capturer des informations identifiables des clients avant le paiement, comme des formulaires de capture d'e-mail.

Le SDK Web suit le comportement sur site de Shopify et des utilisateurs anonymes avec le paramètre `device_id`. Pour confirmer que les adresses e-mail sont ajoutées au profil de l'utilisateur anonyme, ajoutez ce qui suit à une lettre d'information ou à un formulaire de capture d'e-mail : 
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - Pour la capture d'e-mail ou l'inscription à une lettre d'information
- [addAlias](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label" : "shopify_email" 
  - "alias_name" : "example@email.com"

Lorsque les utilisateurs s'inscrivent ou se connectent à leur compte, il se peut que vous souhaitiez [identifier le profil utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) à l'aide d'un ID externe. Après l'enregistrement et la connexion de l'utilisateur, ajoutez la méthode [changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) pour attribuer un ID externe si un utilisateur crée un compte ou se connecte. 

{% alert note %}
Si vous définissez un alias temporaire sur le profil utilisateur, vous pouvez effectuer une requête à l’[endpoint users/merge]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) pour identifier l'utilisateur ultérieurement.
{% endalert %}

#### Configuration du rapprochement des utilisateurs lors du paiement{#headless-checkout}

Lorsque vous activez l'événement de paiement abandonné, Braze reçoit le webhook Shopify checkouts/create. Braze tentera de correspondre à un profil utilisateur existant soit par l'adresse e-mail, le numéro de téléphone ou l'ID client Shopify. S'il n'y a pas de correspondance, Braze crée un profil alias. 

Pour vous assurer que le profil utilisateur suivi sur le site fusionne avec le profil utilisateur alias Shopify créé par les webhooks de Shopify, vous pouvez utiliser l'[endpoint`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) en suivant les étapes ci-dessous. 

{% alert tip %}
Vous pouvez enregistrer un événement personnalisé via le SDK ou un appel d’API effectué sur le fichier `theme.liquid` pour déclencher un Canvas qui inclut une requête à l'endpoint `users/merge`. Ces méthodes sont décrites ci-dessous.
{% endalert %}

Dès qu'un client visite votre site Shopify, un utilisateur anonyme est créé. Cet utilisateur se voit automatiquement attribuer un Braze `device_id`. 

1. Attribuez de manière aléatoire un [alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) unique aux visiteurs de votre site lors d'une nouvelle session.

2. Lorsque les utilisateurs effectuent des actions sur votre site, enregistrez-les en tant qu'[événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events) ou [capturez les attributs clients]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Lorsque l'utilisateur paie et saisit son e-mail dans un formulaire Shopify, un ID client Shopify est créé. Braze traitera les webhooks Shopify et créera un nouveau profil utilisateur si l'e-mail, le téléphone ou l'alias Shopify ne correspond pas à un utilisateur existant.

{% raw %}
```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```
{% endraw %}

{% subtabs %}
{% subtab API approach %}

{: start="3"}
3\. Pour éviter les profils d'utilisateur en double, vous devez fusionner le profil utilisateur contenant le site `device_id` de Braze avec le profil utilisateur contenant le profil d'alias Shopify. Vous pouvez créer un canevas déclenché par l'API qui définira un délai, mettra à jour votre utilisateur avec l'attribut `do_not_merge` et effectuera une requête auprès de l'[endpoint`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/). Vous pouvez également enregistrer un événement personnalisé tel que `merge_user` pour déclencher votre Canvas. 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\. Lorsque les utilisateurs quittent le flux ou terminent le paiement, vous pouvez enregistrer un événement personnalisé, comme `merge_user`, pour déclencher un Canvas qui fixera un délai, mettra à jour votre utilisateur avec l'attribut `do_not_merge` et enverra une requête à l'[endpoint`/users/merge`.]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\. Dans vos critères d'entrée dans Canvas, ne ciblez que les profils utilisateurs non identifiés, c'est-à-dire qu'ils n'ont pas d'ID externe et que `do_not_merge` n'est pas vrai. <br><br>![L'étape de saisie de l’audience dans le compositeur de Canvas avec `do_not_merge` comme filtre d'audience.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5\. Après avoir configuré les critères d'entrée de votre canvas, vous pouvez créer votre flux Canvas. Faites de la première étape de votre Canvas une étape de **retardement** pour éviter d'éventuelles conditions de concurrence pendant le traitement.<br><br>![Étape du canvas dans le compositeur.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6\. Vous pouvez créer une étape de **mise à jour de l'utilisateur** pour mettre à jour l'attribut personnalisé `do_not_merge` à "true", car ces utilisateurs seront fusionnés lors de l'étape suivante. <br><br>![L'utilisateur met à jour l'étape dans le compositeur de canvas avec `do_not_merge` sélectionné comme attribut.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7\. Ensuite, créez une étape **Message** avec un webhook.<br><br>![Étape du message dans le compositeur de canvas avec un canal d'envoi de messages Webhook.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

{% raw %}
```javascript
{
  "merge_updates": [
    {
      "identifier_to_merge": {
           "user_alias": {
                "alias_label": "temp_user_id",
                "alias_name": "{{canvas_entry_properties.${temp_user_id}}}"
            }
      },
      "identifier_to_keep": {
           "user_alias": {
                "alias_label": "shopify_customer_id",
                "alias_name": "{{canvas_entry_properties.${shopify_customer_id}}}"
            }
      }
    }
  ]
}
```
{% endraw %}

{% alert tip %}
Pour plus d'informations sur le comportement de `merge_users`, voir [POST : Fusionner les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).
{% endalert %}

{: start="8"}
8\. Lorsque les utilisateurs quittent le flux ou terminent le paiement, les webhooks Shopify suivants seront mis en correspondance par l'adresse e-mail ou le numéro de téléphone ou en utilisant l'alias Shopify.

{% endtab %}
{% endtabs %}
