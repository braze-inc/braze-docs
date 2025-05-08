---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Cet article de référence décrit le partenariat entre Braze et Punchh, une plateforme de fidélisation et d'engagement, qui vous permet de synchroniser les données entre les deux plateformes. Les données publiées dans Braze seront disponibles pour la segmentation et pourront être synchronisées avec Punchh via la configuration de modèles de webhooks dans Braze."
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/) est une plateforme de fidélisation et d'engagement de pointe qui permet aux marques de proposer des programmes de fidélité omnicanaux à la fois en magasin et en ligne. 

_Cette intégration est maintenue par Punchh._

## À propos de l'intégration

L'intégration de Braze et Punchh vous permet de synchroniser les données à des fins de cadeaux et de fidélité sur les deux plateformes. Les données publiées dans Braze seront disponibles pour la segmentation et pourront être synchronisées avec Punchh via les webhooks de Braze.

## Quels en sont les avantages ?

- Ingérez les données de fidélité de Punchh à Braze en temps réel. 
- Tirez parti des puissantes données d'audience de Braze pour proposer des expériences cross-canal significatives et dynamiques (applications, mobile, Web, e-mail et SMS)
  - Les clients ont-ils ouvert leurs e-mails ? Les clients ont-ils ouvert l'application à proximité d'un magasin ?
- Standardisez l'apparence des e-mails transactionnels envoyés via Braze.
- Créez des parcours qui permettent de réaliser des tests A/B et de les optimiser au fur et à mesure.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Punchh | Vous devez disposer d'un compte Punchh actif pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze | [URL de votre endpoint REST][6]. Votre endpoint dépend de l'URL Braze de votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Que dois-je savoir d'autre ?

#### Avant l'intégration

- Lors de l'utilisation de l'intégration de Braze, deux campagnes seront nécessaires, l'une à Punchh et la seconde à Braze. Par exemple, si vous envoyez une campagne avec une offre en pièce jointe, la campagne de cadeaux sera configurée dans Punchh et la notification pourra être envoyée depuis Braze.
- Des invités devraient déjà exister à Punchh et Braze. Punchh filtrera tous les clients qui ne sont pas encore des clients du programme de fidélité.

#### Points importants à noter

- Punchh a ajouté la possibilité de désactiver l'envoi des attributs utilisateur par défaut à Braze, afin que le client ne subisse pas de dépassement de point de données. Ceci est configuré lors de la configuration de l'adaptateur.
- Si vous utilisez des segments personnalisés dans des campagnes récurrentes, le nom de la campagne doit être utilisé à la place de l'ID de campagne, car les identifiants changent à chaque fois que la campagne est lancée.
- Les canaux de communication disponibles dans le cadre de chaque campagne de cadeaux Punchh incluent les messages enrichis, les notifications push, les SMS et les e-mails.
- Une fois que les utilisateurs ont été redirigés vers un segment personnalisé Punchh depuis Braze, ils ne peuvent pas être supprimés. Seuls les nouveaux invités peuvent être ajoutés à un segment personnalisé existant. Si des invités doivent être retirés d'un segment personnalisé Punchh existant, une nouvelle campagne de webhook devra être créée dans Braze pour rediriger les utilisateurs vers un nouveau segment personnalisé Punchh.

## Intégration

Punchh propose plusieurs points de terminaison aux clients de Braze pour les aider à ajouter des identifiants externes à la plateforme Punchh à l'aide des points de terminaison de l'API Punchh suivants. Une fois les identifiants externes ajoutés, créez un adaptateur dans Punchh, fournissez vos informations d'identification Braze et sélectionnez les événements que vous souhaitez synchroniser. Ensuite, vous pouvez utiliser l'ID de segment Punchh pour créer un webhook Punchh afin de déclencher la synchronisation des clients dans un parcours Canvas.

Notez que les sites Punchh `user_id` et Braze `external_id` doivent être disponibles dans l'une ou l'autre plateforme pour que l'intégration se synchronise correctement. 
- Les événements envoyés de Punchh à Braze comprendront l'identifiant Braze `external_id`. Si Punchh est configuré pour utiliser `external_source_id`, cette valeur sera définie comme la valeur de Braze `external_id`. Dans le cas contraire, l'intégration se fera par défaut en définissant le Punchh `user_id` comme étant le Braze `external_id`.
- Pour envoyer des webhooks de Braze à Punchh, le profil utilisateur de Braze doit disposer de Punchh `user_id`. Si Punchh `user_id` n'est pas utilisé comme Braze `external_id`, il doit être défini comme attribut personnalisé "punchh_user_id". 

### Étape 1 : Configurer les endpoints d'ingestion d'ID externes (facultatif)

Les identifiants externes de Braze peuvent être ajoutés à l'aide des points de terminaison suivants pour les nouveaux utilisateurs et les utilisateurs existants de Punchh.

{% alert important %}
Les champs de valeur `external_source` et `external_source_id` doivent être uniques dans Punchh et ne pas être associées à des profils existants.
{% endalert %}

1. Nouveaux utilisateurs de Punchh<br>
Créez de nouveaux utilisateurs dans Punchh avec un endpoint d'inscription Punchh à l'aide des champs et. `external_source` `external_source_id` Punchh permet d'envoyer des identifiants externes avec un profil utilisateur via l'un des points d'inscription suivants :
- [API d'inscription mobile](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [API d'authentification unique](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. Utilisateurs existants de Punchh <br>
Mise à jour `external_source_id` pour les utilisateurs existants de Punchh. Punchh permet d'ajouter des identifiants externes à un profil via un endpoint de mise à jour de l'API utilisateur : 
- [Mise à jour pour les utilisateurs mobiles](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [Mise à jour de l’authentification unique des utilisateurs](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [Mise à jour du tableau de bord](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs local %}
{% tab Exemple d'API d'inscription utilisateur %}
Cet exemple vous permet d'envoyer des identifiants externes associés à un profil utilisateur au moment de l'inscription. Pour ce faire, envoyez `external_source` en tant que « customer_id » et « 11111111111111111111111111 » `external_source_id` en tant que type de données de chaîne de caractères.

```json
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab Exemple d'API de mise à jour utilisateur %}
Cet exemple vous permet de mettre à jour les identifiants externes avec un profil utilisateur. Pour ce faire, envoyez `external_source` en tant que « customer_id » et « 11111111111111111111111111 » `external_source_id` en tant que type de données de chaîne de caractères.

```json
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**Configuration de la plateforme :** Pour activer les identifiants externes dans Punchh, depuis le tableau de bord Punchh, **accédez** à **Cockpit** > Tableau de **bord** > Identifiant utilisateur externe.
{% endalert %}

### Étape 2 : Configuration de l'adaptateur Braze dans Punchh

#### Événements disponibles à synchroniser {#available-events-to-sync}

1. **Invité :** Déclenché lors de toute inscription, mise à jour du profil d'invité, désactivé ou supprimé
2. **Enregistrement des programmes de fidélité :** Déclenché pour les transactions de fidélité ou les gains en scannant le code-barres du reçu
3. **Enregistrement des cadeaux :** Déclenché pour les points offerts lors d'une campagne
4. **Remboursement :** Déclenché en cas d'échange de récompenses, à l'exception des coupons Punchh, car ceux-ci seraient envoyés séparément en tant qu'événements liés aux coupons, y compris l'émission et le remboursement
5. **Récompenses :** Déclenché par des récompenses offertes lors de campagnes, d'activités, de conversions de points en récompenses ou de cadeaux d'administrateur
6. **Notifications de transactions :** Déclenché lors d'une activité transactionnelle pour un utilisateur dans le système Punchh (par exemple, expiration de points)
7. **Notifications marketing :** Déclenché en fonction de différentes configurations de campagne dans Punchh pour un segment d'utilisateurs associé

{% alert note %}
Consultez la documentation Punchh pour savoir à quoi peuvent ressembler des exemples de charges utiles pour ces événements disponibles.
{% endalert %}

Travaillez avec votre responsable de l'implémentation Punchh pour configurer cet adaptateur.

Pour configurer l'intégration de Braze et Punchh, procédez comme suit :

1. Dans le tableau de bord Punchh, accédez à **Cockpit** > **Tableau de bord** > **Principales fonctionnalités** > **Activer la gestion des webhooks** et basculer sur **Activer la gestion des webhooks**.<br><br>
2. Activez ensuite les adaptateurs en accédant à **Paramètres** > **Gestionnaire de webhooks** > **Configurations** > **Afficher l'onglet Adaptateurs** et en basculant sur l'onglet **Afficher les adaptateurs**.<br><br>
3. Accédez au **gestionnaire Webhooks** sous l'onglet **Paramètres**, sélectionnez l'onglet **Adaptateurs**, puis cliquez sur **Créer un adaptateur**. <br><br>![][1]<br><br>
4. Entrez le nom, la description et l'e-mail de l'administrateur de l'adaptateur. Sélectionnez **Braze** comme adaptateur et fournissez votre endpoint d'API Braze REST et votre clé d'API Braze.<br><br>
5. Sélectionnez ensuite les événements disponibles que vous souhaitez activer. Une liste de ces événements se trouve dans [Événements disponibles à synchroniser](#available-events-to-sync).<br><br>![][3]<br><br>
6. Cliquez sur **Soumettre** pour activer le webhook.

## Créer un webhook Punchh dans Braze

Braze peut ajouter des utilisateurs à un segment Punchh via des webhooks utilisant des segments personnalisés Punchh.

1. Créez un segment personnalisé dans Punchh et notez le contenu dans l'URL du `custom_segment_id` tableau de bord des segments Punchh, comme indiqué ci-dessous. Les constructeurs de segments classiques ou bêta peuvent être utilisés. Cependant, la version bêta est recommandée car la version classique finira par devenir obsolète.<br><br>Sur la plateforme Punchh, accédez à **Invité** > **Segment** > **Liste personnalisée > Nouvelle liste** **personnalisée**.<br><br>![][8]<br><br>

2. Créez une campagne de webhook dans Braze à l'aide de l’endpoint Punchh pour ajouter un utilisateur à un segment personnalisé en tant qu'URL du webhook. Ici, vous pouvez fournir les données `custom_segment_id` extraites de l'URL et `user_id` sous forme de paires clé-valeur.<br><br>![][4]<br><br>

3. Ce webhook peut être configuré en tant que campagne individuelle ou en tant qu'étape d'un Canvas. [Sinon, si le webhook qui ajoute des utilisateurs à ce segment Punchh spécifique est utilisé dans plusieurs campagnes ou Canvases, il peut être configuré comme modèle.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template)<br><br>
La clé `user_id` du webhook correspond à l'ID utilisateur Punchh. Cet identifiant devra être ajouté à tous les webhooks créés dans Braze pour ajouter des utilisateurs à un segment personnalisé Punchh. L'attribut `punch_user_id` personnalisé peut être renseigné dynamiquement en tant que valeur de la clé `user_id` à l'aide de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables). Vous pouvez insérer la variable d'attribut `punchh_user_id` personnalisée à l'aide de l'icône bleue « plus » située en haut à droite de tout champ de texte modélisé.<br><br>![][10]{: style="max-width:65%;"}<br><br>![][11]{: style="max-width:65%;"}<br><br>

4. Une fois le webhook enregistré, il peut être utilisé pour synchroniser les utilisateurs, comme indiqué ci-dessous. Par exemple, 136 invités seraient ajoutés au segment personnalisé Punch lors du lancement de cette campagne de webhook Braze.<br><br>![Exemple de synchronisation d'utilisateurs à l'aide du webhook enregistré grâce à l'intégration de Braze et Punchh.][7]

Pour plus d'informations sur la façon dont les webhooks sont utilisés dans Braze, consultez la section [Création d'un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 

## Campagnes de cas d'utilisation

### Configuration de la campagne et du canevas

#### Déclenchement

Les cas d'utilisation des messages Braze déclenchés par l'envoi d'événements Punchh à Braze, tels que les événements de récompense ou les événements réservés aux invités, peuvent être créés sous forme de [campagnes basées sur l'action]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) ou de canvas déclenchés par l'événement Punchh concerné.

L'ajout d'un déclencheur affichera la liste des événements créés dans Braze. Choisissez l'événement qui doit déclencher votre campagne ou Canvas à envoyer à l'utilisateur qui a enregistré l'événement.

![][12]

Des filtres de propriétés peuvent être ajoutés pour filtrer davantage l'événement déclencheur. Par exemple, le message ne doit être déclenché que lorsqu'un client déclenche l'événement « checkins_gift » pour lequel la propriété de l'événement approuvé est définie sur `true`. Il s'agit d'une fonctionnalité optionnelle qui peut ne pas être applicable à tous les cas d'utilisation. 

#### Segmentation

Dans de nombreux cas, les campagnes Braze et Canvases déclenchées par des événements Punchh peuvent être définies pour une audience « Tous les utilisateurs », car la segmentation des utilisateurs déclenchant ces événements sera déterminée dans Punchh. Cependant, les clients qui souhaitent affiner davantage l'audience des utilisateurs qui recevront l'envoi de messages Braze déclenché par l'événement peuvent le faire en ajoutant des filtres et des segments supplémentaires dans la section **Audiences cibles** du compositeur de campagne ou dans la section **Entry Audience** du compositeur Canvas. 

### Cas d'utilisation

{% tabs local %}
{% tab S'inscrire %}
#### Campagne d'inscription

Lorsque vous utilisez la configuration Braze pour une campagne d'inscription accompagnée d'une offre, une campagne d'inscription et de cadeaux doivent être configurées dans Punchh et un message de bienvenue dans Braze. 

Punchh recommande d'ajouter un délai d'exécution à la campagne d'inscription, afin que Braze puisse d'abord déclencher le message de bienvenue en fonction de l'événement invité. Si vous souhaitez envoyer un message de suivi informant l'utilisateur qu'il a reçu un cadeau, vous pouvez le déclencher en fonction de l'événement de récompense.

Dans le cas d'une campagne d'inscription, toutes les personnes inscrites peuvent être utilisées pour le segment ; par conséquent, aucun segment Braze personnalisé ne sera requis.

Configurations Punchh requises :
- Campagne : S'inscrire 
- Segment : Tous se sont inscrits
- Récompense : Choix du client
Événements requis :
- Événement de récompense
- Événement invité
Considérations :
- Délai d'exécution, recommandez à l'invité d'ajouter un délai de 5 à 10 minutes

![Un segment d'utilisateurs est configuré dans Punch et les clients s'inscrivent à un programme de fidélité. Ensuite, l'événement invité, s'il est déclenché, et la campagne de communication Braze sont déclenchés. Ensuite, la campagne d'inscription de Punchh est déclenchée au bout de 10 minutes, déclenchant l'événement de récompense et un message de suivi facultatif. ]({% image_buster /assets/img/punchh/usecase3.png %})

{% endtab %}
{% tab Offre de masse %}
#### campagne d'offres de masse

Lorsque vous utilisez une campagne d'offres de masse pour les cadeaux, une campagne d'offres de masse doit être configurée dans Punchh et une campagne de communication dans Braze.

Si vous souhaitez utiliser un segment Braze pour votre campagne ou envoyer des communications depuis Braze avant d'offrir un cadeau à des invités sur la plateforme Punchh, un [segment Punchh personnalisé sera requis pour la campagne de cadeaux Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze). 

La création du segment d'utilisateurs devant bénéficier de cette offre dans Braze n'est recommandée que si vous utilisez des attributs non disponibles dans Punchh. Sinon, la segmentation Punchh peut être utilisée et la campagne de communication Braze sera créée sous la forme d'une campagne basée sur l'action déclenchée par les utilisateurs recevant leur récompense (l'événement de récompense déclenché par Punchh).

Configurations Punchh requises :
- Campagne : Offre de masse
- Segment : Liste personnalisée ou choix du client
- Récompense : Choix du client

**En utilisant Punchh pour la segmentation et les cadeaux, et Braze pour l'envoi de messages :**<br>
Par exemple, une récompense de 2 € est envoyée à un segment configurable dans Punchh avec l'envoi de messages via Braze.<br>
![Un segment d'utilisateurs peut être configuré dans Punchh, et les utilisateurs reçoivent un cadeau dans le cadre d'une campagne d'offres groupées Punchh. Ensuite, un événement de récompense est déclenché, puis la campagne de communication Braze est déclenchée. ]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**En utilisant la segmentation et la fonction d'envoi de messages Braze et Punchh pour les cadeaux :**<br>
Par exemple, une récompense de 2 € et l'envoi de messages à un segment dont les attributs ne sont pas disponibles dans Punchh.<br>
![Un segment utilisateur peut être configuré dans Braze, puis un message peut être envoyé depuis un segment Braze vers Braze. Ensuite, les utilisateurs sont redirigés vers le segment personnalisé Punchh via un webhook Braze avec segment et ID utilisateur. Après cela, l'utilisateur reçoit un cadeau via la campagne d'offre de masse Punchh avec un segment personnalisé. L'événement de récompense est ensuite déclenché. ]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**En utilisant la segmentation Braze et Punchh pour les cadeaux ou l'envoi de messages, ou les deux :**<br>
Par exemple, une récompense de 2$ est envoyée à un segment dont les attributs ne sont pas disponibles dans Punchh, mais aucun message n'est requis, ou le message peut être envoyé via Punchh (notez que tous les invités doivent être présents dans Punchh).<br>
![Un segment utilisateur peut être configuré dans Braze, et les utilisateurs sont envoyés vers un segment personnalisé Punchh via un webhook Braze avec segment et ID utilisateur. Après cela, l'utilisateur reçoit un cadeau via la campagne d'offre de masse Punchh avec un segment personnalisé. Ensuite, l'événement de récompense est déclenché. ]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab Offre de masse récurrente %}
#### Campagne d'offres de masse récurrente

Lorsque vous utilisez une campagne d'offres de masse récurrente pour les cadeaux, une campagne d'offres de masse doit être configurée dans Punchh et une campagne de communication doit être configurée dans Braze. Un segment personnalisé Punchh sera requis si le client souhaite utiliser la segmentation Braze (recommandée uniquement si vous utilisez des attributs non disponibles dans Punchh). Sinon, la segmentation Punchh peut être utilisée et la campagne de communication Braze sera déclenchée en fonction de l'événement de récompense.

Configurations Punchh requises :
- Campagne : Offre de masse récurrente
- Segment : Liste personnalisée ou choix du client
- Récompense : Choix du client
Considérations :
- Les identifiants et les noms des campagnes sont envoyés à Braze en tant que propriété de l'événement. Si vous souhaitez utiliser un identifiant de campagne Punchh dans Braze pour filtrer davantage l'audience qui reçoit la campagne, le nom de la campagne doit être utilisé car les identifiants de campagne changeront tous les jours.

{% endtab %}
{% tab Offre après l'enregistrement avec notification %}
#### Campagne d'offres après l'enregistrement avec notification

Lors de l'utilisation d'une campagne d'offre après l'enregistrement, Braze enverra la notification concernant le cadeau et, lorsque le client effectuera son enregistrement, il recevra un cadeau dans le cadre de la campagne Punchh après l'enregistrement. Par conséquent, une campagne d'offres après l'enregistrement devra être configurée dans Punchh et une campagne de communication dans Braze (si vous informez les clients de la campagne).

Configurations Punchh requises :
- Campagne : Offre après l'enregistrement
- Segment : Liste personnalisée
- Récompense : Choix du client

Par exemple, un e-mail invitant les clients à se rendre ce week-end pour doubler leurs points sur un segment dont les attributs ne sont pas disponibles dans Punchh. Punchh offrira des points à ce segment après un enregistrement qualifiant et l'envoi de messages facultatifs depuis Braze. 

![Un segment d'utilisateurs est configuré dans Braze et les messages sont envoyés depuis Braze après la campagne d’enregistrement. Ensuite, les utilisateurs éligibles sont envoyés vers le segment personnalisé Punchh via le webhook Braze avec un segment et un ID utilisateur. Enfin, l'utilisateur éligible du segment personnalisé s'enregistre et reçoit le cadeau et le message facultatif dans le cadre de la campagne post-enregistrement ] ({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Offre après l'enregistrement sans notification %}
#### Campagne d'offres post-enregistrement sans notification

Lors de l'utilisation d'une campagne d'offre post-enregistrement qui ne notifie pas d'abord les clients, la campagne offrira un cadeau (messagerie facultative) et déclenchera toute notification au sein de Braze. Par conséquent, une campagne d'offres post-enregistrement doit être configurée dans Punchh ; toutefois, aucune liste personnalisée n'est requise. Vous pouvez plutôt choisir le segment que vous souhaitez dans Punchh. 

Configurations Punchh requises :
- Campagne : Offre après l'enregistrement
- Segment : Choix du client
- Récompense : Choix du client

Par exemple, une campagne Braze, une surprise et un plaisir, est envoyée à un segment disponible dans Punchh, pour remercier les clients de leur visite et les récompenser en leur offrant 2$ de réduction sur leur prochaine visite.

![Un segment d'utilisateurs éligibles peut être configuré dans Punchh et les utilisateur éligibles s'enregistrent et reçoivent un cadeau dans le cadre d'une campagne Punchh post-enregistrement. Ensuite, un événement de récompense est déclenché et un message de rappel est envoyé pour informer les invités de la récompense envoyée par Braze. ]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab anniversaire %}
#### campagne d'anniversaire 

Lors de l'utilisation d'une campagne d'anniversaire, un utilisateur recevra d'abord un cadeau pour son anniversaire dans le cadre de la campagne Punchh. Ce cadeau (événement de récompense) déclenchera la campagne de communication au sein de Braze qui informera l'utilisateur du cadeau. Par conséquent, aucune liste personnalisée n'est requise. Vous pouvez plutôt choisir le segment et le paramètre d'anniversaire dans Punchh.

Configurations Punchh requises :
- Campagne : campagne d'anniversaire
- Segment : Choix du client
- Récompense : Choix du client
Considérations :
- Récompense le mois de l'inscription
- Durée de vie (Quelle est la durée de validité de la récompense anniversaire ?)
- Campagnes récurrentes, planification requise 

![Un segment facultatif peut être créé dans Punchh, et un utilisateur éligible reçoit une récompense dans le cadre d'une campagne anniversaire de Punchh. Ensuite, un événement de récompense est déclenché et un message de rappel est envoyé pour informer les invités de la récompense envoyée par Braze. ]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Rappel %}
#### campagne de rappel

Lors du ciblage des utilisateurs en fonction de leur inactivité, une campagne de rappel peut être utilisée. Le client peut créer le segment et la campagne dans Punchh, mais utiliser Braze pour l'envoi de messages.

Si vous souhaitez utiliser la segmentation créée dans Braze, un [segment Punchh personnalisé]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) basé sur l'inactivité peut être associé à une campagne d'offres de masse récurrente.

Configurations Punchh requises :
- Campagne : campagne de rappel
- Segment : Choix du client
- Récompense : Choix du client
Considérations :
- La campagne se déroule selon une planification

![Un segment facultatif peut être créé dans Punchh, et un utilisateur éligible reçoit une récompense dans le cadre d'une campagne de rappel Punchh. Ensuite, un événement de récompense est déclenché et le message de rappel est envoyé pour informer les invités de la récompense envoyée par Braze. ]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/punchh/punchh1.png %}
[2]: {% image_buster /assets/img/punchh/punchh2.png %}
[3]: {% image_buster /assets/img/punchh/punchh3.png %}
[4]: {% image_buster /assets/img/punchh/punchh4.png %}
[5]: {% image_buster /assets/img/punchh/punchh5.png %}
[7]: {% image_buster /assets/img/punchh/punchh6.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints
[8]: {% image_buster /assets/img/punchh/update1.png %}
[9]: {% image_buster /assets/img/punchh/update2.png %}
[10]: {% image_buster /assets/img/punchh/update3.png %}
[11]: {% image_buster /assets/img/punchh/update4.png %}
[12]: {% image_buster /assets/img/punchh/update5.png %}
[13]: {% image_buster /assets/img/punchh/update6.png %}
[14]: {% image_buster /assets/img/punchh/update7.png %}
