---
nav_title: Configuration de Shopify
article_title: "Configuration de Shopify"
description: "Cet article explique comment configurer Shopify, une société de commerce international, qui vous permet de connecter de manière harmonieuse votre boutique Shopify à Braze pour faire passer certains webhooks Shopify dans Braze."
page_type: partner
search_tag: Partenaire
alias: "/setting_up_shopify/"
alias: "/shopify_subscription_states/"
page_order: 2
---

# Configuration de Shopify

### Étape 1 : Localiser Shopify dans le tableau de bord
Dans Braze, accédez à **Technology Partners (partenaires technologiques)** puis recherchez **Shopify**. Sur la page partenaire Shopify, sélectionnez **Begin Setup (Commencer la configuration)** pour démarrer le processus d’intégration.

![Section Importation de données et installation du SDK Web de la page partenaire Shopify dans Braze.][2]{: style="max-width:80%;"}

### Étape 2 : Assistant de configuration de Braze
Cette étape prévoit l’interaction avec l’assistant de configuration de Braze. Dans ce flux, vous devez saisir le nom de votre magasin Shopify. Veillez à saisir le nom du magasin, et pas votre domaine Shopify. Notez qu'actuellement, nous ne pouvons connecter qu'un seul magasin par groupe d'apps.

### Étape 3 : Sélection flexible des événements
Il y aura une étape expliquant quels événements nécessitent l'implémentation du Web SDK Braze à votre magasin et ce à quoi vous devez vous attendre lorsque celui-ci sera ajouté. Passez à la page suivante pour sélectionner les événements Shopify que vous souhaitez que Braze suive. En sélectionnant tous les événements avec un * à côté d'eux, vous activerez notre Web SDK. L'étape suivante vous demandera de confirmer les événements sélectionnés.

### Étape 4 : Activer le canal de messages dans le navigateur
Vous pouvez éventuellement débloquer un nouveau canal dans votre boutique Shopify pour les messages dans le navigateur. Cela vous permettra d'utiliser nos types de messages prêts à l'emploi tels que : à glissement vers le haut, modal, plein écran, enquêtes simples et HTML personnalisé. Notez qu'en activant cette option, vous implémenterez notre SDK Web dans votre boutique. Consultez notre [guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) sur la façon dont vous pouvez créer votre premier message dans le navigateur.

### Étape 5 : Collecter des utilisateurs abonnés par courriel ou par SMS

À cette étape, indiquez si vous souhaitez que les abonnements collectés par e-mail et par SMS sur votre boutique Shopify soient synchronisés avec Braze.

![][77]{: style="max-width:60%;"}

- **Collecter des utilisateurs abonnés par e-mail**<br>Si cette option est activée, Braze mettra à jour l'état de l'abonnement global à l'e-mail sur le profil sur `subscribed` afin que vous puissiez envoyer des e-mails à vos utilisateurs. Vous pouvez également ajouter, de manière facultative, un ou plusieurs [groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups) auxquels les utilisateurs abonnés par e-mail sont automatiquement affectés lorsqu'ils choisissent de s’abonner. 
- **Collecter des utilisateurs abonnés par SMS**<br>Si cette option est activée, Braze mettra à jour le [groupe d'abonnement par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) sélectionné sur le profil sur `subscribed` afin que vous puissiez envoyer des messages à vos utilisateurs. Si vous collectez des SMS d’abonnement, vous devez sélectionner un groupe d'abonnement. Si aucun groupe d'abonnement n'existe, ou si vous souhaitez créer un nouveau groupe d'abonnement, contactez votre conseiller Braze pour obtenir de l'aide. 

S'il existe un état d'abonnement global existant sur un profil d'utilisateur dans Braze qui est différent de celui de Shopify, nous vous recommandons d'activer l'option **Remplacer le statut d'abonnement global existant pour les utilisateurs**. Cela remplacera le statut de Braze pour s'assurer qu'il correspond à celui de Shopify.

{% alert important %}
Si vous ne remplacez pas les statuts d'abonnement globaux, les statuts des utilisateurs existants peuvent ne pas correspondre à ceux trouvés dans Shopify. Cela peut conduire à des messages non reçus et non intentionnels.
{% endalert %}

#### Attributs personnalisés hérités

Les anciens clients de Shopify peuvent disposer de l’ancienne méthode de collecte d’utilisateurs abonnés par courriels et SMS via les attributs personnalisés `shopify_accepts_marketing` et `shopify_sms_consent`. Si vous enregistrez les paramètres ci-dessus en activant le remplacement, Braze supprimera les attributs personnalisés des profils d’utilisateur et synchronisera ces valeurs avec leur groupe d’abonnement par courriel et leur groupe d’abonnement par SMS respectifs.

Si vous avez encore des campagnes ou des Canevas existants qui utilisent ces anciens attributs personnalisés, vous devez les supprimer et vous assurer que les campagnes ou les Canevas utilisent l’état d’abonnement approprié, le groupe, ou les deux."

### Étape 6 : Installer l’application Shopify de Braze
Vous serez ensuite redirigé vers votre boutique Shopify pour installer l'application Braze. Sélectionnez **Install Unlisted App** (Installer une application non répertoriée) pour accéder au Tableau de bord de Braze. 

### Étape 7 : Vérifier la fin du processus
Et voilà ! L’état de votre intégration apparaît dans la section **Data Import** (Importation de données) de la page partenaire de Shopify. Une fois que l'application Braze a été installée avec succès et que la création du webhook est terminée, vous en serez informé par e-mail et l'absorption commencera. En outre, l’état **Connection Pending (Connexion en attente)** sera mis à jour vers **Connected (Connecté)** et affichera l’horodatage du moment où la connexion a été établie.

### Configuration de Shopify dans Braze

<br>![Flux de travail de configuration de Shopify dans Braze ; saisi du nom de la boutique et accès à Shopify pour installer l’application Braze.][4]{: style="max-width:90%;"}

## Résolution des problèmes

{% details Pourquoi l’installation de mon application Shopify est-elle toujours en attente ? %}
Votre installation peut être en attente pour l’une des raisons suivantes : 
  - Lorsque Braze configure vos webhooks Shopify
  - Lorsque Braze communique avec Shopify

Si l’installation de votre application reste en attente pendant 1 heure, Braze arrête l’installation et vous serez invité à réessayer l’opération.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details Pourquoi l’installation de mon application Shopify a-t-elle échoué ? %}
Votre installation a échoué pour l’une des raisons suivantes : 
  - Braze n’a pas pu joindre Shopify
  - Échec de traitement de la demande par Braze 
  - Votre jeton d’accès à Shopify n’est pas valide 
  - L’application Braze Shopify a été supprimée de votre page d’administration Shopify

Si cela se produit, vous pourrez sélectionner **Retry Setup (Réessayer l’installation)** et recommencer le processus d’installation.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details Comment désinstaller l’application Braze de mon magasin Shopify ? %}
Accédez à votre page d’administration Shopify située sous **Apps (Applications)**. Vous verrez alors une option pour supprimer l’application Braze.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details J’ai du mal à rapprocher mes utilisateurs, quelle pourrait en être la raison ? %}

Si vous utilisez l'intégration ScriptTag et que votre boutique Shopify propose une option "Acheter maintenant" qui permet de sauter le panier, Braze peut avoir du mal à réconcilier les utilisateurs, car Shopify n'autorise pas les balises de script à récupérer un `device_id` pour mapper un événement à un utilisateur qui saute le panier.

{% enddetails %}


[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/scriptag.gif %} 
[77]: {% image_buster /assets/img/Shopify/shopify_integration77.jpg %}
[4]: {% image_buster /assets/img/Shopify/shopify_integration3-6.gif %}
