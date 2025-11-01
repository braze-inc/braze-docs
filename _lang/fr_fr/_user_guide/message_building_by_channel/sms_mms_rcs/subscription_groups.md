---
nav_title: "Groupes d'abonnement"
article_title: "Groupes d'abonnement SMS et RCS"
page_order: 1
description: "Cet article de référence traite des groupes d'abonnement, des états d'abonnement et du processus de configuration des groupes d'abonnement pour les canaux SMS, MMS et RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS
  
---

# Groupes d'abonnement SMS et RCS

> Les groupes d'abonnement constituent la base de l'envoi de messages SMS, MMS et RCS par l'intermédiaire de Braze. Un groupe d'abonnement est un ensemble d'[entités d'envoi]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (telles que des expéditeurs vérifiés par RCS, des codes courts SMS, des codes longs SMS ou des ID d'expéditeur alphanumériques SMS) qui sont utilisées pour un type spécifique d'envoi de messages. Par exemple, si une marque prévoit d'envoyer à la fois des messages SMS transactionnels et promotionnels, deux groupes d'abonnement avec des pools distincts de numéros de téléphone d'envoi devront être configurés dans votre tableau de bord de Braze.

## États du groupe d'abonnement

Il existe deux états d'abonnement pour les utilisateurs de SMS et de RCS : `subscribed` et `unsubscribed`. L'état de l'abonnement d'un utilisateur réside au niveau du groupe d'abonnement et n'est pas partagé entre les groupes d'abonnement, ce qui signifie qu'un utilisateur peut être `subscribed` dans un groupe d'abonnement transactionnel mais `unsubscribed` dans un groupe d'abonnement promotionnel. Pour les marques, cette séparation des états garantit qu'elles peuvent continuer à envoyer des SMS et des messages RCS pertinents à leurs utilisateurs.

| État | Définition |
| --------- | ---------- |
| Abonné | L'utilisateur a explicitement confirmé qu'il souhaitait recevoir des SMS et des RCS d'un groupe d'abonnement spécifique. Un utilisateur peut être abonné soit par la mise à jour de son état d'abonnement via l'API d'abonnement de Braze, soit par l'envoi par SMS d'une réponse par mot-clé d'abonnement. Un utilisateur doit être abonné à un groupe d'abonnement SMS ou RCS pour pouvoir recevoir des SMS, du RCS ou les deux. |
| Désabonné | L'utilisateur a explicitement choisi de ne plus recevoir de messages de votre groupe d'abonnement SMS et RCS et des numéros de téléphone de l'expéditeur dans le groupe d'abonnement. Ils peuvent se désabonner en envoyant par SMS une réponse par mot-clé de désabonnement ou une marque peut désabonner les utilisateurs via l'[API d'abonnement de Braze]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Les utilisateurs désabonnés d'un groupe d'abonnement SMS et RCS ne recevront plus de SMS ou de RCS provenant des numéros de téléphone d'envoi appartenant au groupe d'abonnement.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Définir l'état d'un utilisateur

Lorsqu'un numéro de téléphone est mis à jour dans un profil utilisateur, le nouveau numéro de téléphone hérite du statut du groupe d'abonnement de l'utilisateur. Si le numéro de téléphone est mis à jour vers un numéro qui existe déjà dans Braze, le statut d'abonnement de ce numéro de téléphone existant est hérité.

Par exemple, si l'utilisateur A a un numéro de téléphone abonné à plusieurs groupes d'abonnement et que ce numéro de téléphone est ensuite ajouté à l'utilisateur B, l'utilisateur B sera abonné aux mêmes groupes d'abonnement. Pour éviter qu'un utilisateur n'hérite des abonnements existants, vous pouvez réinitialiser les groupes d'abonnement de l'ancien numéro via l'API REST de Braze chaque fois qu'un utilisateur change de numéro. Si plusieurs utilisateurs partagent ce numéro de téléphone, ils seront tous désabonnés.

Pour définir l'état du groupe d'abonnement d'un utilisateur, utilisez l'une des méthodes suivantes :

- **API REST :** Les profils utilisateurs peuvent être définis de manière programmatique par l'endpoint [\`/subscription/status/set\`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) en utilisant l'API REST de Braze.
- **Intégration SDK** Les utilisateurs peuvent être ajoutés à un groupe d'abonnement par e-mail ou par SMS et RCS à l'aide de la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web.](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)
- **Traitement automatique en cas d'abonnement/de désabonnement de l'utilisateur :** En envoyant par SMS un [mot-clé d']({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)abonnement ou de désabonnement par défaut, Braze définit et met à jour automatiquement l'état de l'abonnement des utilisateurs.
- **Import d'utilisateurs**: Les utilisateurs peuvent être ajoutés à des groupes d'abonnement à l'e-mail, au SMS et au RCS par le biais de l'**importation d'utilisateurs**. Lors de la mise à jour du statut du groupe d'abonnement, vous devez avoir ces deux colonnes dans votre CSV : `subscription_group_id` et `subscription_state`. Reportez-vous à l'[importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) pour plus d'informations.

### Vérifier le groupe d'un utilisateur

Pour vérifier le groupe d'abonnement d'un utilisateur, utilisez l'une des méthodes suivantes :

- **Profil utilisateur :** Les profils utilisateurs individuels sont accessibles via le tableau de bord de Braze en sélectionnant **Recherche d'utilisateurs** dans la barre latérale. Vous pouvez y rechercher des profils utilisateurs par e-mail, numéro de téléphone ou ID externe. Dans un profil utilisateur, sous l'onglet Engagement, vous pouvez voir les groupes d'abonnement SMS et RCS d'un utilisateur. 
- **API REST :** Les profils utilisateur individuels groupe d'abonnement peuvent être consultés par l'[endpoint Liste des groupes d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou l'[endpoint Statut du groupe d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) en utilisant l'API REST de Braze. 

## Envoi de messages avec un groupe d'abonnement

Pour lancer une campagne SMS ou RCS via Braze, sélectionnez un groupe d'abonnement dans la liste déroulante **Variantes SMS/MMS/RCS**. Une fois sélectionné, un filtre d'audience sera automatiquement ajouté à votre campagne ou Canvas, garantissant que seuls les utilisateurs `subscribed` du subscription groups sélectionné font partie de l'audience cible.

{% alert important %}
Conformément à la [conformité et aux directives]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) internationales en matière [de télécommunications]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), Braze n'enverra jamais de SMS ou de RCS aux utilisateurs qui ne se sont pas abonnés au groupe d'abonnement sélectionné.  
{% endalert %}

!compositeur SMS avec le groupe d'abonnement déroulant ouvert et "Service d'envoi de messages A pour SMS" mis en évidence par l'utilisateur.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Activation des groupes d'abonnement

Pour activer les groupes d'abonnement pour les SMS, MMS ou RCS, reportez-vous à ce qui suit :

{% tabs local %}
{% tab SMS %}
Au cours de votre processus d'onboarding SMS, un gestionnaire de bord de Braze mettra en place des groupes d'abonnements pour votre compte onboarding. Ils détermineront avec vous le nombre de groupes d'abonnement dont vous avez besoin et ajouteront les numéros de téléphone d'envoi appropriés à vos groupes d'abonnement. Les délais de mise en place d'un groupe d'abonnement dépendent du type de numéros de téléphone que vous ajoutez. Par exemple, les demandes de codes courts peuvent prendre entre 8 et 12 semaines, alors que les codes longs peuvent être mis en place en une journée. Si vous avez des questions sur la configuration de votre tableau de bord de Braze, contactez votre conseiller Braze pour obtenir de l'aide.  
{% endtab %}

{% tab MMS %}
Pour envoyer un message MMS, au moins un numéro de votre groupe d'abonnement doit être autorisé à envoyer des MMS. Ceci est indiqué par une étiquette située à côté du groupe d'abonnement. 

!déroulant du groupe d'abonnement avec "Messaging Service A for SMS" en surbrillance. L'entrée est précédée de l'étiquette "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Un expéditeur vérifié par RCS doit être présent dans votre groupe d'abonnement pour que vous puissiez envoyer un message RCS. 

Il y a deux façons d'ajouter un expéditeur vérifié par RCS :
- L'ajouter à un groupe d'abonnement existant
- Créer un nouveau groupe d'abonnement RCS
Le choix dépend largement des cas d'utilisation du RCS qui vous intéressent. 

En fonction de votre intégration, Braze peut ajouter des expéditeurs vérifiés par RCS à vos groupes d'abonnement SMS existants ou créer de nouveaux groupes d'abonnement pour vous. Dans les deux cas, votre gestionnaire de la satisfaction client vous guidera dans la mise à niveau du trafic SMS de façon fluide et homogène.
{% endtab %}
{% endtabs %}

## Migration du trafic SMS vers le RCS

Si vous avez des groupes d'abonnement SMS et RCS séparés, vous pouvez migrer les utilisateurs de SMS vers RCS en utilisant une étape canvas. 

Braze vous recommande de tester l'envoi de RCS à de plus petits volumes d'utilisateurs dans un premier temps et de faire migrer davantage d'utilisateurs vers le groupe d'abonnement RCS au fil du temps. Par exemple, si vous avez 1 000 000 d'utilisateurs abonnés à un groupe d'abonnement SMS, vous pourriez commencer par migrer tous les utilisateurs vers le nouveau groupe d'abonnement, puis segmenter une audience plus restreinte de 50 000 à 100 000 personnes (5 à 10 %) pour tester les messages RCS.

### Étape 1 : Créez un canvas et remplissez la planification de l'entrée.

Créez un canvas et donnez-lui un nom facilement identifiable (tel que "SMS-RCS Subscription Group User Transfer"). Ensuite, planifiez la campagne au moment qui vous convient le mieux.

### Étape 2 : Définissez votre audience

Définissez votre audience en utilisant l'une des méthodes suivantes. Ensuite, passez à l'étape **Paramètres d'envoi** et sélectionnez **Utilisateurs abonnés ou ayant opté pour l'** **envoi**.

| Méthode                          | Description                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Créer une segmentation**         | Créez un segment qui inclut tous les utilisateurs d'un groupe d'abonnement ou un sous-ensemble utilisant des filtres de segmentation (e.g., un 5-10% aléatoire). Les segments sont mis à jour avant chaque envoi pour refléter votre base d'utilisateurs actuelle.        |
| **Appliquer des filtres de campagne ou de canvas** | Affinez l'audience à l'étape du **ciblage** de l'**audience de** votre campagne ou de votre canvas. Ajustez les options de ciblage sans quitter la page pour plus de flexibilité.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Étape 3 : Configurer une étape de mise à jour de l'utilisateur

Ajoutez une étape de mise à jour de l'utilisateur à votre canvas. Dans l'étape, ouvrez l'**éditeur JSON avancé** et saisissez ce qui suit (pour le champ de l'identifiant unique de l'utilisateur, nous vous recommandons d'utiliser le champ `braze_id` ) :

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

\!["Objet de mise à jour de l'utilisateur" qui contient le code JSON indiqué précédemment.]({% image_buster /assets/img/sms/user_update_object.png %})

### Étape 4 : Testez le canvas

Nous vous recommandons vivement de [tester votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) pour confirmer qu'il fonctionne comme prévu avant de l'envoyer à votre audience élargie.

### Étape 5 : Lancez votre Canvas

Après avoir testé avec succès votre Canvas, lancez-le pour votre sous-ensemble d'utilisateurs !

Pour confirmer que la migration de vos utilisateurs s'est bien déroulée, nous vous recommandons de vérifier quelques profils utilisateurs individuels qui ont été mis à jour. Dans l'onglet **Engagement**, recherchez **Paramètres de contact** et faites défiler pour afficher les groupes d'abonnement auxquels l'utilisateur est abonné. Le groupe d'abonnement RCS devrait maintenant être basculé.
