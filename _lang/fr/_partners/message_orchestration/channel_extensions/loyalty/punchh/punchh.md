---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "Cet article présente le partenariat entre Braze et Punchh, une plateforme de fidélité et d’engagement, qui vous permet de synchroniser les données sur les deux plateformes. Les données utilisateur publiées dans Braze seront disponibles pour la segmentation et peuvent être synchronisées dans Punchh via des modèles de webhooks configurés dans Braze. "
page_type: partner
search_tag: Partenaire

---

# Punchh

> [Punchh](https://punchh.com/) est une plateforme de fidélité et d’engagement leader du secteur qui permet aux marques de proposer des programmes de fidélité omnicanal à la fois en magasin et en ligne. 

L’intégration de Braze et de Punchh vous permet de synchroniser les données à des fins de cadeaux et de fidélisation sur les deux plateformes. Les données publiées dans Braze seront disponibles pour la segmentation et peuvent synchroniser les données des utilisateurs dans Punchh via des webhooks dans Braze.

## Quels sont les avantages ?
- Intégrer les données de fidélité de Punchh dans Braze en temps réel. 
- Exploiter et superposer les puissantes données d’audience de Braze pour offrir des expériences cross-canal significatives et dynamiques (application, mobile, Web, courriel et SMS).
  - Les clients ont-ils ouvert les e-mails ? Les clients ont-ils ouvert l’app près d’un magasin ?
- Standardiser l’aspect et la convivialité des e-mails transactionnels envoyés par Braze.
- Créer des parcours qui permettent de réaliser des tests A/B et de les optimiser au fur et à mesure.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Punchh | Un compte Punchh est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé API REST Braze avec autorisations `users.track` (suivi des utilisateurs) <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][6]. Votre endpoint dépend de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Que dois-je savoir d’autre ?

#### Avant d’intégrer
- Si vous utilisez l’intégration Braze, deux campagnes seront nécessaires, l’une dans Punchh et la seconde dans Braze. Par exemple, si vous envoyez une campagne à laquelle est jointe une offre, la campagne de cadeaux sera configurée dans Punchh, et la notification pourra être envoyée depuis Braze.
- Les invités devraient déjà exister dans Punchh et Braze. Punchh filtrera tout client qui n’est pas déjà un client fidèle.

#### Choses importantes à noter
- Punchh a ajouté la possibilité de désactiver l’envoi d’attributs utilisateur par défaut à Braze, afin que le client ne subisse pas d’excédents de points de données. Cela est configuré lors du paramétrage de l’adaptateur.
- Si vous utilisez des segments personnalisés sur des campagnes récurrentes, le nom de la campagne doit être utilisé à la place de l’ID de la campagne, car les ID changent à chaque exécution de la campagne.
- Les canaux de communication disponibles dans le cadre de chaque campagne de cadeaux Punchh comprennent les messages enrichis, les notifications push, les SMS et les courriels.
- Une fois que les utilisateurs ont été envoyés vers un segment personnalisé Punchh à partir de Braze, ils ne peuvent plus être supprimés. Seuls de nouveaux invités peuvent être ajoutés à un segment personnalisé existant. Si les invités doivent être retirés d’un segment personnalisé Punchh existant, une nouvelle campagne de webhook devra être créée dans Braze pour envoyer les utilisateurs vers un nouveau segment personnalisé Punchh.

## Intégration

Punchh propose plusieurs endpoints aux clients de Braze pour les aider à ajouter des ID externes à la plateforme Punchh en utilisant les endpoints d’API Punchh suivants. Une fois les ID externes ajoutés, créez un adaptateur dans Punchh, fournissez vos identifiants Braze et sélectionnez les événements que vous souhaitez synchroniser. Ensuite, vous pouvez prendre l’ID de segment Punchh et l’utiliser pour créer un webhook Punchh pour déclencher la synchronisation du client dans un parcours Canvas.

Notez que le `user_id` Punchh devra être ajouté au profil d’utilisateur Braze en tant qu’attribut personnalisé « punchh_user_id » pour que l’intégration soit utilisée. De même, l’`external_id` utilisé dans Braze devra être inclus comme champ `external_source_id` dans le profil utilisateur de Punchh. 

### Étape 1 : Configurer les endpoints d’ingestion de l‘ID externe

Des ID externes de Braze peuvent être ajoutés en utilisant les critères d’évaluation suivants pour les utilisateurs de Punchh nouveaux et existants.

{% alert important %}
Les valeurs des champs `external_source` et `external_source_id` doivent être uniques dans Punchh et ne pas être associées à des profils existants.
{% endalert %}

1. Nouveaux utilisateurs de Punchh<br>
Créez de nouveaux utilisateurs dans Punchh avec un endpoint d’inscription à Punchh en utilisant les champs `external_source` et `external_source_id`. Punchh permet d’envoyer des identifiants externes avec un profil utilisateur via l’un des endpoints suivants d’inscription :
- [API d’inscription mobile](https://developers.punchh.com/mobile-apis/users/mobile-sign-up)
- [API d’authentification unique](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-signup)<br><br>
2. Utilisateurs Punchh existants <br>
Mettez à jour `external_source_id` pour les utilisateurs Punchh existants. Punchh permet d’ajouter des identifiants externes à un profil via un endpoint de mise à jour de l’API utilisateur : 
- [Mise à jour de l’utilisateur mobile](https://developers.punchh.com/mobile-apis/users/mobile-update-user-profile)
- [Mise à jour de l’utilisateur d’authentification unique](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-update-user-information)
- [Mise à jour de l’utilisateur de tableau de bord](https://developers.punchh.com/platform-functions-apis/users/dashboard-users-update)
<br><br>
{% tabs local %}
{% tab Exemple d’API d’inscription d’utilisateur %}
Cet exemple vous permet d’envoyer des identifiants externes avec un profil d’utilisateur au moment de l’inscription. Ceci est fait en envoyant `external_source` comme « customer_id » et `external_source_id` comme « 556644557788334412 » comme type de données string.

```json
curl --location --request POST 'https://sandbox.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: eac5b04cbf7362c5359a4c259cf8fc18941646bf2e11bfe46be0031ffaa1100b' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4a0e0024ae0d30b",
    "user" : {
      "email": "example@braze.com",
      "password": "p@ssw0rd",
      "first_name":"Amit",
      "last_name":"K",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"556644557788334412"
      }
}'
```
{% endtab %}
{% tab Exemple d’API de mise à jour d’utilisateur %}
Cet exemple vous permet d’envoyer des identifiants externes avec un profil d’utilisateur. Ceci est fait en envoyant `external_source` comme « customer_id » et `external_source_id` comme « 556644557788334412 » comme type de données string.

```json
curl --location --request PUT 'https://sandbox.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: 953d896eebfdb5a84aacb9d1b8eaae1fa0cd710b68bcd3b2324415ac40fee99c' \
--header 'Authorization: Bearer c90b819bf962db9882eeac6993b57c0a22816ecad0e5229b27320d63' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4a0e0024ae0d30b",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"556644557788334412"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
Configuration de la plateforme : Pour activer les identifiants externes dans Punchh, dans le tableau de bord Punchh, accédez à **Cockpit > Dashboard (Tableau de bord) > External User Identifier (Identifiant utilisateur externe)**.
{% endalert %}

### Étape 2 : Configuration de l’adaptateur Braze dans Punchh

#### Événements disponibles à synchroniser {#available-events-to-sync}

1. Invité - déclenché lors de toute inscription, mise à jour du profil invité, désactivation ou suppression, etc.
2. Enregistrement de fidélité - déclenché pour les transactions de fidélité ou les gains en scannant le code-barres du reçu
3. Enregistrement des cadeaux - déclenché pour les points offerts dans le cadre d’une campagne
4. Échange - déclenché en cas d’échange de récompense à l’exception des bons de réduction Punchh, car ceux-ci seront envoyés séparément en tant qu’événements de bon de réduction, y compris leur émission et leur échange
5. Récompenses - déclenchées par des récompenses offertes par des campagnes, des activités, la conversion de points en récompenses, des cadeaux de l’administration, etc.
6. Notifications de transaction - déclenchées lors de l’activité transactionnelle d’un utilisateur dans le système Punchh. Par exemple, l’expiration du point.
7. Notifications marketing - déclenchées en fonction de différentes configurations de campagne dans Punchh pour un segment d’utilisateurs associé

{% alert note %}
Consultez la documentation de Punchh sur les exemples de charges utiles pour ces événements disponibles. 
{% endalert %}

Travaillez avec votre gestionnaire d’implémentation Punchh pour configurer cet adaptateur.

Pour configurer l’intégration Punchh à Braze :

1. Dans le tableau de bord Punchh, accédez à **Cockpit > Dashboard (Tableau de bord) > Major Features (Fonctionnalités principales) > Enable Webhook Management (Activer la gestion du webhook)** et basculez à **Enable Webhook Management (Activer la gestion du webhook)**.<br><br>
2. Ensuite, activez les adaptateurs en accédant à **Settings (Paramètres) > Webhooks Manager (Gestionnaire des webhooks) > Configurations > Show Adapters Tab (Afficher l’onglet Adaptateurs) ** et basculez à **Show Adapters Tab (Afficher l’onglet Adaptateurs)**.<br><br>
3. Accédez à **Webhooks Manager (Gestionnaire des webhooks)** sous l’onglet **Settings (Paramètres)** sélectionnez l’onglet **Adapters (Adaptateurs)** et cliquez sur **Create Adapter (Créer un adaptateur)**. <br><br>![][1]<br><br>
4. Indiquez le nom de l’adaptateur, la description et l’e-mail d’administration. Sélectionnez **Braze** comme adaptateur et fournissez votre endpoint d’API REST et la clé d’API REST de Braze.<br><br>
5. Ensuite, sélectionnez les événements disponibles que vous souhaitez activer. Une liste de ces événements est disponible dans [Événements disponibles à synchroniser](#available-events-to-sync).<br><br>![][3]<br><br>
6. Cliquez sur **Submit (Envoyer)** pour activer le webhook.

## Créer un webhook Punchh dans Braze

Braze peut ajouter des utilisateurs à un segment Punchh via des webhooks utilisant les segments personnalisés Punchh.

1. Créez un segment personnalisé dans Punchh et notez le `custom_segment_id` présent dans l’URL du tableau de bord de segment Punchh comme illustré ci-dessous. Les élaborateurs de segments classiques ou bêta peuvent être utilisés. Cependant, la version bêta est recommandée, car la version classique finira par être obsolète.<br><br>Dans la plateforme Punchh, accédez à **Guest > Segment > Custom List > New Custom List (Invité > Segment > Liste personnalisée > Nouvelle liste personnalisée)**.<br><br>![][8]<br><br>

2. Créez une campagne de webhook dans Braze en utilisant l’endpoint Punchh pour ajouter un utilisateur à un segment personnalisé comme URL du webhook. Vous pouvez fournir `custom_segment_id` issu de l’URL et `user_id` comme paires clé-valeur.<br><br>![][4]<br><br>

3. Ce webhook peut être configuré comme une campagne Singular ou comme une étape dans un Canvas. Parallèlement, si le webhook ajoutant des utilisateurs à ce segment Punchh spécifique est utilisé dans plusieurs campagnes ou canevas, il peut être configuré comme [modèle]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template).<br><br>
La clé `user_id` dans le mappage du webhook qui correspond à l’ID utilisateur Punchh. Cet identifiant devra être ajouté à tous les webhooks créés dans Braze pour ajouter des utilisateurs à un segment personnalisé Punchh. L’attribut personnalisé `punch_user_id` peut être renseigné dynamiquement en tant que valeur de la clé `user_id` via [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables). Vous pouvez insérer la variable d’attribut personnalisé `punchh_user_id` à l’aide de l’icône bleue « plus » située en haut à droite de n’importe quel champ de texte basé sur un modèle.<br><br>![][10]{: style="max-width:65%;"}<br><br>![][11]{: style="max-width:65%;"}<br><br>

4. Une fois le webhook enregistré, il peut être utilisé pour synchroniser les utilisateurs, comme indiqué ci-dessous. Par exemple, 136 invités seraient ajoutés au segment personnalisé Punch lors du lancement de cette campagne de webhook Braze.<br><br>![Exemple de synchronisation des utilisateurs à l’aide du webhook enregistré suite à l’intégration de Braze et Punchh.][7]

Pour plus d’informations sur la façon dont les webhooks sont utilisés chez Braze, consultez la rubrique [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) (Créer un webhook). 

## Campagnes de cas d’utilisation

### Configuration de la campagne et de Canvas

#### Déclencheurs

Les cas d’utilisation d’envoi de messages Braze déclenchés par les événements Punchh envoyés à Braze, comme les événements de récompense ou les événements invités, peuvent être créés sous forme de [campagnes par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) ou de Canevas déclenchés par l’événement Punchh concerné.

L’ajout d’un déclencheur affichera la liste des événements créés dans Braze. Choisissez l’événement qui doit déclencher votre campagne ou Canvas à envoyer à l’utilisateur qui a enregistré l’événement.

![][12]

Des filtres de propriétés peuvent être ajoutés pour mieux filtrer l’événement déclencheur. Par exemple, le message ne doit être déclenché que lorsqu’un client déclenche l’événement « checkins_gift » où la propriété d’événement approuvée est `true`. Il s’agit d’une fonctionnalité facultative qui peut ne pas s’appliquer à tous les cas d’utilisation. 

#### Segmentation

Dans de nombreux cas, les campagnes Braze et les Canevas déclenchés par des événements Punchh peuvent être définis sur une audience « Tous les utilisateurs », car la segmentation des utilisateurs déclenchant ces événements sera déterminée dans Punchh. Toutefois, les clients qui cherchent à mieux cibler l’audience des utilisateurs qui recevront les messages Braze déclenchés par l’événement peuvent le faire en ajoutant des filtres et des segments supplémentaires dans la section **Target Audiences (Audiences cibles)** du composeur de campagne ou **Entry Audience (l’Audience d’entrée)** du composeur Canvas. 

### Exemple de cas d’utilisation

{% tabs local %}
{% tab Inscription %}
#### Campagne d’inscription

Lors de l’utilisation de la configuration Braze pour une campagne d’inscription avec une offre jointe, une campagne de cadeaux pour l’inscription devra être configurée dans Punchh ainsi qu’un message de bienvenue dans Braze. 

Punchh recommande d’ajouter un délai d’exécution à la campagne d’inscription, afin que Braze puisse d’abord déclencher le message de bienvenue en fonction de l’événement invité. Si vous souhaitez envoyer un message de suivi informant l’utilisateur qu’il a reçu un cadeau, vous pouvez le déclencher en fonction de l’événement de récompense.

Dans le cas d’une campagne d’inscription, tous les inscrits peuvent être utilisés pour le segment ; par conséquent, un segment Braze personnalisé ne sera pas nécessaire.

Configurations Punchh requises :
- Campagne : Inscription 
- Segment : Tous les inscrits
- Récompenses : Choix du client
Événements requis :
- Événement de récompense
- Événement invité
Considérations :
- Délai d’exécution, recommander au client d’ajouter un délai de 5 à 10 minutes

![Un segment d’utilisateur est configuré dans Punch, et les invités s’inscrivent à un programme de fidélité. Après cela, l’événement invité, s’il est déclenché, et la campagne de communication Braze sont déclenchés. Ensuite, la campagne de cadeaux d’inscription Punchh est déclenchée après 10 minutes, déclenchant l’événement de récompense et le message de suivi facultatif.]({% image_buster /assets/img/punchh/usecase3.png %})

{% endtab %}
{% tab Offre de masse %}

#### Campagne d’offre de masse

Lors de l’utilisation d’une campagne d’offre de masse pour les cadeaux, une campagne d’offre de masse devra être configurée dans Punchh et une campagne de communication dans Braze.

Si vous souhaitez utiliser un segment Braze pour votre campagne ou envoyer une communication depuis Braze avant d’offrir des cadeaux aux invités sur la plateforme Punchh, un [segment Punchh personnalisé]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) sera nécessaire pour la campagne de cadeaux Punchh. 

La création du segment d’utilisateurs pour recevoir cette offre dans Braze n’est recommandée que lors de l’utilisation d’attributs non disponibles dans Punchh. Sinon, la segmentation Punchh peut être utilisée et la campagne de communication Braze sera créée comme une campagne par événement déclenchée par les utilisateurs recevant leur récompense (l’événement de récompense déclenché par Punchh).

Configurations Punchh requises :
- Campagne : Offre de masse
- Segment : Liste personnalisée ou choix du client
- Récompenses : Choix du client

**Si vous utilisez Punchh pour la segmentation et les cadeaux, et Braze pour l’envoi de messages :**<br>
Par exemple, une récompense de 2 $ est envoyée à un segment configurable dans Punchh avec un envoi de message géré par Braze.<br>
![Un segment d’utilisateur peut être configuré dans Punchh, et les utilisateurs reçoivent un cadeau via une campagne d’offre de masse Punchh. Ensuite, l’événement de récompense, s’il est déclenché, et la campagne de communication Braze sont déclenchés.]({% image_buster /assets/img/punchh/usecase4.png %}){: style="max-width:125%;"}

**Si vous utilisez la segmentation et l’envoi de messages Braze, mais Punchh pour les cadeaux :**<br>
Par exemple, une récompense de 2 $ et un message envoyé à un segment avec des attributs non disponibles dans Punchh.<br>
![Un segment utilisateur peut être configuré dans Braze, puis un message peut être envoyé de Braze au segment Braze. Puis, les utilisateurs sont envoyés au segment personnalisé Punchh via un webhook Braze avec segment et ID utilisateur. Après cela, l’utilisateur reçoit un cadeau via la campagne d’offre de masse Punchh avec un segment personnalisé. Après cela, l’événement de récompense est déclenché.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:125%;"}

**Si vous utilisez la segmentation Braze et Punchh pour les cadeaux et/ou l’envoi de messages :**<br>
Par exemple, une récompense de 2 $ de réduction est envoyée à un segment avec des attributs non disponibles dans Punchh, mais aucun message n’est requis, ou l’envoi de messages peut être géré par Punchh (notez que tous les invités doivent être présents dans Punchh).<br>
![Un segment d’utilisateurs peut être configuré dans Braze, et les utilisateurs sont envoyés au segment personnalisé Punchh via un webhook Braze avec segment et ID utilisateur. Après cela, l’utilisateur reçoit un cadeau via la campagne d’offre de masse Punchh avec un segment personnalisé. Après cela, l’événement de récompense est déclenché.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:75%;"}


{% endtab %}
{% tab Offre de masse récurrente %}

#### Campagne d’offre de masse récurrente

Lors de l’utilisation d’une campagne d’offre de masse récurrente pour les cadeaux, une campagne d’offre de masse devra être configurée dans Punchh et une campagne de communication paramétrée dans Braze. Un segment personnalisé Punchh sera requis si le client souhaite utiliser la segmentation Braze (recommandé uniquement si vous utilisez des attributs non disponibles dans Punchh). Sinon, la segmentation Punchh peut être utilisée et la campagne de communication Braze sera déclenchée en fonction de l’événement de récompense.

Configurations Punchh requises :
- Campagne : Offre de masse récurrente
- Segment : Liste personnalisée ou choix du client
- Récompenses : Choix du client
Considérations :
- Les ID de campagne et les noms de campagne sont envoyés à Braze en tant que propriété de l’événement dans l’événement. Si vous souhaitez utiliser un identifiant de campagne Punchh dans Braze pour mieux filtrer l’audience cible de la campagne, le nom de la campagne doit être utilisé, car les identifiants de campagne changeront quotidiennement.

{% endtab %}
{% tab Offre post-enregistrement avec notification %}

### Campagne d’offre post-enregistrement avec notification

Lors de l’utilisation d’une campagne d’offre post-enregistrement, Braze enverra la notification concernant le cadeau, et une fois que l’invité aura effectué un enregistrement, il sera alors offert par la campagne Punchh post-enregistrement. Par conséquent, une campagne d’offre post-enregistrement devra être configurée dans Punchh et une campagne de communication dans Braze (si vous informez les clients de la campagne).

Configurations Punchh requises :
- Campagne : Offre post-enregistrement
- Segment : Liste personnalisée
- Récompenses : Choix du client

Par exemple, un courriel informant les invités de visiter ce week-end pour doubler les points d’un segment avec des attributs non disponibles dans Punchh. Punchh offrira des points à ce segment après un enregistrement qualifiant et un envoi de messages facultatif de Braze. 

![Un segment d’utilisateurs est configuré dans Braze et les messages sont envoyés à partir de la campagne de post-enregistrement de Braze. Puis, les utilisateurs éligibles sont envoyés au segment personnalisé Punchh via un webhook Braze avec segment et ID utilisateur. Enfin, l’utilisateur éligible dans le segment personnalisé s’enregistre et reçoit le cadeau ainsi que le message facultatif via une campagne post-enregistrement.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab Offre post-enregistrement sans notification %}

#### Campagne d’offre post-enregistrement sans notification

Lors de l’utilisation d’une campagne d’offre post-enregistrement qui n’informe pas d’abord les clients, la campagne offrira (envoi de messages facultatif) et déclenchera toute notification dans Braze. C’est pourquoi une campagne d’offre post-enregistrement doit être configurée dans Punchh ; cependant, une liste personnalisée n’est pas requise. Au lieu de cela, vous pouvez choisir le segment que vous souhaitez dans Punchh. 

Configurations Punchh requises :
- Campagne : Offre post-enregistrement
- Segment : Choix du client
- Récompenses : Choix du client

Par exemple, une campagne Braze surprise et ravissante est envoyée à un segment disponible à Punchh, remerciant les invités de leur visite et les récompensant avec 2 $ de réduction sur leur prochaine visite.

![Un segment d’utilisateur éligible peut être configuré dans Punchh, et un utilisateur éligible s’enregistre puis reçoit un cadeau via une campagne post-check-in Punchh. Après cela, un événement de récompense est déclenché et le message de rappel est envoyé pour informer les invités de la récompense envoyée par Braze.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab Anniversaire %}

#### Campagne d’anniversaire 

Lors de l’utilisation d’une campagne d’anniversaire, un utilisateur recevra d’abord un cadeau pour son anniversaire via la campagne Punchh. Ce cadeau (événement de récompense) déclenchera la campagne de communication dans Braze qui notifie l’utilisateur du cadeau. C’est pourquoi une liste personnalisée n’est pas nécessaire. Au lieu de cela, vous pouvez choisir le paramètre de segment et d’anniversaire dans Punchh.

Configurations Punchh requises :
- Campagne : Campagne d’anniversaire
- Segment : Choix du client
- Récompenses : Choix du client
Considérations :
- Offrir un mois d’inscription
- Longévité (Combien de temps la récompense d’anniversaire est-elle valide ?)
- Campagnes récurrentes, planification requise 

![Un segment facultatif peut être créé dans Punchh, et un utilisateur éligible reçoit une récompense via une campagne d’anniversaire Punchh. Après cela, un événement de récompense est déclenché et le message de rappel est envoyé pour informer les invités de la récompense envoyée par Braze.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab Rappel %}

#### Campagne de rappel

Lorsque vous ciblez des utilisateurs en fonction de leur inactivité, vous pouvez utiliser une campagne de rappel. Le client peut créer le segment et la campagne dans Punchh, mais utiliser Braze pour l’envoi de messages.

Si vous souhaitez utiliser la segmentation créée dans Braze, un [segment Punchh personnalisé]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze) basé sur l’inactivité peut être associé à une campagne d’offre de masse récurrente.

Configurations Punchh requises :
- Campagne : Campagne de rappel
- Segment : Choix du client
- Récompenses : Choix du client
Considérations :
- La campagne se déroule selon une planification

![Un segment facultatif peut être créé dans Punchh, et un utilisateur éligible reçoit une récompense via une campagne de rappel Punchh. Après cela, un événement de récompense est déclenché et le message de rappel est envoyé pour informer les invités de la récompense envoyée par Braze.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/punchh/punchh1.png %}
[2]: {% image_buster /assets/img/punchh/punchh2.png %}
[3]: {% image_buster /assets/img/punchh/punchh3.png %}
[4]: {% image_buster /assets/img/punchh/punchh4.png %}
[5]: {% image_buster /assets/img/punchh/punchh5.png %}
[7]: {% image_buster /assets/img/punchh/punchh6.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[8]: {% image_buster /assets/img/punchh/update1.png %}
[9]: {% image_buster /assets/img/punchh/update2.png %}
[10]: {% image_buster /assets/img/punchh/update3.png %}
[11]: {% image_buster /assets/img/punchh/update4.png %}
[12]: {% image_buster /assets/img/punchh/update5.png %}
[13]: {% image_buster /assets/img/punchh/update6.png %}
[14]: {% image_buster /assets/img/punchh/update7.png %}
