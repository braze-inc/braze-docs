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

> Les groupes d'abonnement constituent la base de l'envoi de messages SMS, MMS et RCS via Braze. Un groupe d'abonnement est un ensemble d'[entités d'envoi]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) (telles que des expéditeurs vérifiés RCS, des codes courts SMS, des codes longs SMS ou des ID d'expéditeur alphanumériques SMS) utilisées pour un type spécifique d'envoi de messages. Par exemple, si une marque prévoit d'envoyer à la fois des messages SMS transactionnels et promotionnels, deux groupes d'abonnement avec des pools distincts de numéros de téléphone d'envoi devront être configurés dans votre tableau de bord de Braze.

## États du groupe d'abonnement

Il existe deux états d'abonnement pour les utilisateurs SMS et RCS : `subscribed` et `unsubscribed`. L'état d'abonnement d'un utilisateur est défini au niveau du groupe d'abonnement et n'est pas partagé entre les groupes. Autrement dit, un utilisateur peut être `subscribed` à un groupe d'abonnement transactionnel tout en étant `unsubscribed` d'un groupe promotionnel. Pour les marques, cette séparation des états garantit la possibilité de continuer à envoyer des SMS et des messages RCS pertinents à leurs utilisateurs.

| État | Définition |
| --------- | ---------- |
| Abonné | L'utilisateur a explicitement confirmé qu'il souhaitait recevoir des SMS et des RCS d'un groupe d'abonnement spécifique. Un utilisateur peut s'abonner soit en faisant mettre à jour son état d'abonnement via l'API d'abonnement de Braze, soit en envoyant une réponse avec un mot-clé d'abonnement. Un utilisateur doit être abonné à un groupe d'abonnement SMS ou RCS pour pouvoir recevoir des SMS, du RCS ou les deux. |
| Désabonné | L'utilisateur a explicitement choisi de ne plus recevoir de messages de votre groupe d'abonnement SMS et RCS ni des numéros de téléphone d'envoi associés à ce groupe. Il peut se désabonner en envoyant une réponse avec un mot-clé de désabonnement, ou la marque peut désabonner des utilisateurs via l'[API d'abonnement de Braze]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/). Les utilisateurs désabonnés d'un groupe d'abonnement SMS et RCS ne recevront plus aucun SMS ou RCS provenant des numéros de téléphone d'envoi appartenant à ce groupe.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Définir l'état d'un utilisateur

Lorsqu'un numéro de téléphone est mis à jour dans un profil utilisateur, le nouveau numéro hérite du statut du groupe d'abonnement de l'utilisateur. Si le numéro de téléphone est remplacé par un numéro qui existe déjà dans Braze, c'est le statut d'abonnement de ce numéro existant qui est hérité.

Par exemple, si l'utilisateur A possède un numéro de téléphone abonné à plusieurs groupes d'abonnement et que ce numéro est ensuite ajouté à l'utilisateur B, l'utilisateur B sera abonné aux mêmes groupes d'abonnement. Pour éviter qu'un utilisateur n'hérite des abonnements existants, vous pouvez réinitialiser les groupes d'abonnement de l'ancien numéro via l'API REST de Braze chaque fois qu'un utilisateur change de numéro. Si plusieurs utilisateurs partagent ce numéro de téléphone, ils seront tous désabonnés.

De plus, l'état d'abonnement du numéro de téléphone d'un ancien utilisateur peut être hérité, même si ce numéro n'est actuellement associé à aucun profil utilisateur. Par exemple, si un utilisateur possède le numéro de téléphone `123-456-7890`, s'abonne à un groupe d'abonnement, puis voit son numéro de téléphone supprimé, l'état d'abonnement associé à `123-456-7890` persiste et sera appliqué lorsque le numéro sera de nouveau attribué ultérieurement.

Pour définir l'état du groupe d'abonnement d'un utilisateur, utilisez l'une des méthodes suivantes :

- **API REST :** Les profils utilisateur peuvent être configurés par programmation via l'[endpoint `/subscription/status/set`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) à l'aide de l'API REST de Braze.
- **Intégration SDK :** Les utilisateurs peuvent être ajoutés à un groupe d'abonnement e-mail, SMS ou RCS à l'aide de la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Traitement automatique lors de l'abonnement/désabonnement :** Lorsqu'un utilisateur envoie par SMS un [mot-clé]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) d'abonnement ou de désabonnement par défaut, Braze définit et met à jour automatiquement l'état d'abonnement de l'utilisateur.
- **Importation d'utilisateurs :** Les utilisateurs peuvent être ajoutés à des groupes d'abonnement e-mail, SMS ou RCS via l'**importation d'utilisateurs**. Si vous mettez à jour le statut du groupe d'abonnement, votre CSV doit contenir les deux colonnes suivantes : `subscription_group_id` et `subscription_state`. Consultez la section [Importation d'utilisateurs]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status) pour plus d'informations.

### Vérifier le groupe d'un utilisateur

Pour vérifier le groupe d'abonnement d'un utilisateur, utilisez l'une des méthodes suivantes :

- **Profil utilisateur :** Les profils utilisateur individuels sont accessibles via le tableau de bord de Braze en sélectionnant **Recherche d'utilisateurs** dans la barre latérale. Vous pouvez y rechercher des profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Dans un profil utilisateur, sous l'onglet Engagement, vous pouvez consulter les groupes d'abonnement SMS et RCS de l'utilisateur. 
- **API REST :** Le groupe d'abonnement d'un profil utilisateur individuel peut être consulté via l'[endpoint de liste des groupes d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou l'[endpoint de liste du statut du groupe d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) à l'aide de l'API REST de Braze. 

## Envoi de messages avec un groupe d'abonnement

Pour lancer une campagne SMS ou RCS via Braze, sélectionnez un groupe d'abonnement dans le menu déroulant **Variantes SMS/MMS/RCS**. Une fois la sélection effectuée, un filtre d'audience sera automatiquement ajouté à votre campagne ou Canvas, garantissant que seuls les utilisateurs `subscribed` au groupe d'abonnement sélectionné font partie de l'audience cible.

{% alert important %}
Conformément aux [réglementations et directives internationales en matière de télécommunications]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), Braze n'enverra jamais de SMS ou de RCS aux utilisateurs qui ne sont pas abonnés au groupe d'abonnement sélectionné.  
{% endalert %}

![Composeur de messages SMS avec le menu déroulant Groupe d'abonnement ouvert et « Service de messagerie A pour SMS » mis en surbrillance par l'utilisateur.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Activation des groupes d'abonnement

Pour activer les groupes d'abonnement pour les SMS, MMS ou RCS, reportez-vous aux informations suivantes :

{% tabs local %}
{% tab SMS %}
Au cours de votre processus d'onboarding SMS, un gestionnaire d'onboarding Braze configurera les groupes d'abonnement pour votre compte. Il déterminera avec vous le nombre de groupes d'abonnement nécessaires et ajoutera les numéros de téléphone d'envoi appropriés à vos groupes d'abonnement. Les délais de mise en place d'un groupe d'abonnement dépendent du type de numéros de téléphone que vous ajoutez. Par exemple, les demandes de code court peuvent prendre entre 8 et 12 semaines, tandis que les codes longs peuvent être configurés en une journée. Si vous avez des questions concernant la configuration de votre tableau de bord de Braze, contactez votre conseiller Braze pour obtenir de l'aide.  
{% endtab %}

{% tab MMS %}
Pour envoyer un message MMS, au moins un numéro de votre groupe d'abonnement doit être autorisé à envoyer des MMS. Ceci est indiqué par une étiquette située à côté du groupe d'abonnement. 

![Menu déroulant Groupe d'abonnement avec « Service de messagerie A pour SMS » mis en surbrillance. L'entrée est précédée de l'étiquette « MMS ».]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Un expéditeur vérifié RCS doit être présent dans votre groupe d'abonnement avant de pouvoir envoyer un message RCS. 

Il existe deux façons d'ajouter un expéditeur vérifié RCS :
- L'ajouter à un groupe d'abonnement existant
- Créer un nouveau groupe d'abonnement RCS
Le choix dépend largement des cas d'utilisation RCS qui vous intéressent. 

En fonction de votre intégration, Braze peut ajouter des expéditeurs vérifiés RCS à vos groupes d'abonnement SMS existants ou créer de nouveaux groupes d'abonnement pour vous. Dans les deux cas, votre Customer Success Manager vous guidera dans une mise à niveau fluide et efficace du trafic SMS.
{% endtab %}
{% endtabs %}

## Migration du trafic SMS vers le RCS

Si vous disposez de groupes d'abonnement SMS et RCS séparés, vous pouvez migrer les utilisateurs du SMS vers le RCS à l'aide d'un Canvas en une seule étape. 

Braze vous recommande de commencer par tester l'envoi de RCS sur de plus petits volumes d'utilisateurs, puis de migrer progressivement davantage d'utilisateurs vers le groupe d'abonnement RCS. Par exemple, si vous avez 1 000 000 d'utilisateurs abonnés à un groupe d'abonnement SMS, vous pourriez commencer par migrer tous les utilisateurs vers le nouveau groupe d'abonnement, puis segmenter une audience plus restreinte de 50 000 à 100 000 personnes (5 à 10 %) pour tester les messages RCS.

### Étape 1 : Créez un Canvas et remplissez la planification de l'entrée

Créez un Canvas et donnez-lui un nom facilement identifiable (par exemple « SMS-RCS Subscription Group User Transfer »). Ensuite, planifiez la campagne au moment qui vous convient le mieux.

### Étape 2 : Définissez votre audience

Définissez votre audience en utilisant l'une des méthodes suivantes. Ensuite, passez à l'étape **Paramètres d'envoi** et sélectionnez **Utilisateurs abonnés ou ayant opté pour l'envoi**.

| Méthode                          | Description                                                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Créer un segment**         | Créez un segment qui inclut tous les utilisateurs d'un groupe d'abonnement ou un sous-ensemble à l'aide de filtres de segmentation (par exemple, 5 à 10 % au hasard). Les segments sont mis à jour avant chaque envoi pour refléter votre base d'utilisateurs actuelle.        |
| **Appliquer des filtres de campagne ou de Canvas** | Affinez l'audience à l'étape du **ciblage de l'audience** de votre campagne ou de votre Canvas. Ajustez les options de ciblage sans quitter la page pour plus de flexibilité.                                         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Étape 3 : Configurer une étape de mise à jour de l'utilisateur

Ajoutez une étape de mise à jour de l'utilisateur à votre Canvas. Dans cette étape, ouvrez l'**éditeur JSON avancé** et saisissez le code suivant (pour le champ d'identifiant unique de l'utilisateur, nous vous recommandons d'utiliser le champ `braze_id`) :

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

![« Objet de mise à jour utilisateur » contenant le code JSON mentionné précédemment.]({% image_buster /assets/img/sms/user_update_object.png %})

### Étape 4 : Testez le Canvas

Nous vous recommandons vivement de [tester votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) pour vérifier qu'il fonctionne comme prévu avant de l'envoyer à votre audience élargie.

### Étape 5 : Lancez votre Canvas

Après avoir testé votre Canvas avec succès, lancez-le pour votre sous-ensemble d'utilisateurs !

Pour confirmer que la migration de vos utilisateurs s'est bien déroulée, nous vous recommandons de vérifier quelques profils utilisateur individuels qui ont été mis à jour. Dans l'onglet **Engagement**, recherchez **Paramètres de contact** et faites défiler pour afficher les groupes d'abonnement auxquels l'utilisateur est abonné. Le bouton du groupe d'abonnement RCS devrait maintenant être activé.