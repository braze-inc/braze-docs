---
nav_title: "Groupes d’abonnement"
article_title: Groupes d’abonnement WhatsApp
page_order: 2
description: "Cet article décrit les groupes d’abonnement WhatsApp, quels statuts d’abonnement sont proposés et comment les groupes d’abonnement sont définis."
page_type: reference
channel:
  - WhatsApp
hidden: true  
---

# Groupes d’abonnement WhatsApp

Les groupes d’abonnement WhatsApp sont créés lorsque vous intégrez WhatsApp avec votre application via le **portail Technology Partner**.

{% alert important %}
La prise en charge du canal WhatsApp est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Statuts d’abonnement WhatsApp

Il existe deux statuts d’abonnement pour les utilisateurs WhatsApp : `abonné` et `désabonné`. WhatsApp a un groupe d’abonnement par groupe d’apps.

| État | Définition |
| --- | --- |
| Abonné | L’utilisateur a explicitement confirmé qu’il souhaite recevoir des messages WhatsApp de la part d’une société spécifique. Les utilisateurs peuvent souscrire en faisant mettre à jour leur état d’abonnement par l’API d’abonnement de Braze ou en déployant une stratégie d’abonnement, conformément aux directives de WhatsApp. |
| Non inscrit | L’utilisateur s’est explicitement désabonné des envois de message de votre groupe d’abonnement WhatsApp. Il peut se désabonner en envoyant une réponse avec un mot-clé de désabonnement si un Canvas correspondant a été mis en place, ou une marque peut désabonner des utilisateurs au moyen de l’API d’abonnement de Braze. Les utilisateurs désabonnés d’un groupe d’abonnement WhatsApp ne recevront plus les communications. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Comment les groupes d’abonnement WhatsApp d’utilisateurs sont mis en place 

- **API Rest :** Des profils d’utilisateur peuvent être définis en programmation par l’endpoint [/subscription/status/set][4] au moyen de l’API REST de Braze.
- **SDK Web :** Les utilisateurs peuvent être ajoutés à un groupe d’abonnement e-mail, SMS ou WhatsApp à l’aide de la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) ou [Web][11].
- **User Import** : Les utilisateurs peuvent être ajoutés dans des groupes d’abonnement E-mail ou SMS via User Import. Lorsque vous mettez à jour le statut du groupe d’abonnement, vous devez avoir ces deux colonnes dans votre CSV : `subscription_group_id` et `subscription_state`. Pour plus d’informations, consultez [User Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Comment vérifier le groupe d’abonnement WhatsApp d’un utilisateur

- **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze en sélectionnant User Search dans la barre latérale. Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Une fois dans un profil utilisateur, sous l’onglet Engagement, vous pouvez afficher les groupes d’abonnement SMS d’un utilisateur. 
- **API Rest :** Le groupe d’abonnement de profils d’utilisateurs individuels peut être consulté par l’endpoint [Obtenir un groupe d’abonnement][9] ou l’endpoint [Statut du groupe d’abonnement][8] au moyen de l’API REST de Braze. 

## Processus d’abonnement WhatsApp

Actuellement, les utilisateurs peuvent s’abonner et s’inscrire de plusieurs façons aux envois de messagesWhatsApp, y compris par [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), un site Internet, une discussion WhatsApp, téléphone ou en personne. Les mots clés d’abonnement ne sont pas actuellement pris en charge pour le canal WhatsApp, donc il vous appartient de maintenir une liste d’utilisateurs. WhatsApp a une approche rétrospective des abonnements et des limites de taux où, si les utilisateurs commencent à vous signaler ou vous bloquer, votre limite de débit sera réduite. 


[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
