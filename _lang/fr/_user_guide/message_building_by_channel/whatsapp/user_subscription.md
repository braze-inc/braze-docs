---
nav_title: "Groupes d’abonnement"
article_title: Groupes d’abonnement WhatsApp
page_order: 3
description: "Cet article décrit les groupes d’abonnement WhatsApp, quels états d’abonnement sont proposés et comment les groupes d’abonnement sont définis."
page_type: reference
channel:
  - WhatsApp
 
---

# Groupes d’abonnement

> Les groupes d’abonnement WhatsApp sont créés lorsque vous intégrez WhatsApp avec votre application via le **Portail Technology Partner**.

## État d’abonnement WhatsApp

Il existe deux états d’abonnement pour les utilisateurs WhatsApp : `subscribed` et `unsubscribed`. WhatsApp a un groupe d’abonnement par groupe d’apps.

| État | Définition |
| --- | --- |
| Abonné | L’utilisateur a explicitement confirmé qu’il souhaite recevoir des messages WhatsApp de la part d’une société spécifique. Les utilisateurs peuvent souscrire en faisant mettre à jour leur état d’abonnement par l’API d’abonnement de Braze ou en déployant une stratégie d’abonnement, conformément aux directives de WhatsApp. |
| Non inscrit | Soit l’utilisateur n’a pas explicitement donné son consentement pour l’abonnement, soit son statut d’abonnement a été explicitement supprimé. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Comment les groupes d’abonnement WhatsApp d’utilisateurs sont-ils mis en place 

- **API Rest :** Des profils d’utilisateur peuvent être définis en programmation par l’endpoint [/subscription/status/set][4] au moyen de l’API REST de Braze.
- **SDK Web :** Les utilisateurs peuvent être ajoutés à un groupe d’abonnement e-mail, SMS ou WhatsApp à l’aide de la méthode `addToSubscriptionGroup` pour [Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-), [iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287) ou [Web][11].
- **User Import** : Les utilisateurs peuvent être ajoutés dans des groupes d’abonnement E-mail ou SMS via User Import. Lorsque vous mettez à jour le statut du groupe d’abonnement, vous devez avoir ces deux colonnes dans votre CSV : `subscription_group_id` et `subscription_state`. Pour plus d’informations, consultez [User Import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status).

### Comment vérifier le groupe d’abonnement WhatsApp d’un utilisateur

- **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze en sélectionnant **User Search** dans la barre latérale. Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Une fois dans un profil utilisateur, sous l’onglet **Engagement**, vous pouvez afficher les groupes d’abonnement WhatsApp d’un utilisateur et leurs statuts.
- **API Rest :** Le groupe d’abonnement de profils d’utilisateurs individuels peut être consulté par l’endpoint [Obtenir un groupe d’abonnement][9] ou l’endpoint [Statut du groupe d’abonnement][8] au moyen de l’API REST de Braze. 

## Processus d’abonnement WhatsApp

Actuellement, les utilisateurs peuvent s’inscrire et s’[abonner]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/#set-up-opt-ins-for-your-braze-whatsapp-channel) de plusieurs façons aux envois de messages WhatsApp, y compris par [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), un site Internet, une discussion WhatsApp, par téléphone ou en personne. Les mots-clés d’abonnement ne sont pas pris en charge actuellement pour le canal WhatsApp, vous aurez donc à entretenir vous-même votre liste d’utilisateurs. WhatsApp possède une approche rétroactive vis-à-vis des abonnements et des limites de débit, ce qui fait que si vos utilisateurs commencent à vous signaler et à vous bloquer, votre limite de débit sera abaissée. 


[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
