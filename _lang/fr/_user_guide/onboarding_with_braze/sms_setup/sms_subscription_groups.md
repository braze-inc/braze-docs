---
nav_title: "Groupes d’abonnement SMS"
article_title: Groupes d’abonnement SMS
page_order: 5
description: "Le présent article de référence couvre les groupes d’abonnement SMS, une collection d’envoi de numéros de téléphone qui sont utilisés pour un type de message spécifique."
page_type: reference
noindex: true
channel:
  - SMS

---

# Groupes d’abonnement SMS

> Les groupes d’abonnement sont la base pour envoyer des SMS et MMS au moyen de Braze. Un groupe d’abonnement est une collection de [numéros de téléphone expéditeurs][2] (c.-à-d. codes courts, codes longs et/ou identifiants alphanumériques d’expéditeurs) qui sont utilisés pour envoyer un type spécifique de message.

Par exemple, si une marque prévoit d’envoyer des messages SMS transactionnels et promotionnels, deux groupes d’abonnement avec des pools distincts de numéros de téléphone émetteurs devront être configurés dans votre tableau de bord de Braze.

## Notions de bases des Groupes d’abonnement SMS

Les groupes d’abonnement sont nécessaires pour tout message SMS envoyé par le biais de Braze. Un groupe d’abonnement est un groupe de nombres pour un cas d’utilisation de messagerie donné (par exemple, marketing ou messages transactionnels). Les utilisateurs de ce groupe d’abonnement peuvent être abonnés ou désabonnés au groupe indépendamment et, s’ils sont abonnés, ils recevront des messages envoyés à ce groupe.

1. **Groupes d’abonnement**
- Un groupe d’abonnement est requis pour chaque groupe d'apps Braze que vous prévoyez d’envoyer avec des SMS. 
- Les utilisateurs peuvent se désabonner des messages dans un SMS ou en utilisant d’autres types d’invites de désabonnement (par exemple, page de compte ou flux Web dans l’application). Votre équipe doit mettre à jour le statut de l’abonnement de tout utilisateur qui désabonne en dehors de la messagerie SMS.<br><br>
2. **Gestion des mises à jour utilisateur**
- Vous devez ajouter des utilisateurs à un groupe d’abonnement via REST API.
- Groupe d’abonnement des [filtres de reciblage]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) sont disponibles pour créer et cibler des campagnes et des Canvas.
- Il existe deux états d’abonnement pour les utilisateurs de SMS : `subscribed` et `unsubscribed`.

## États d’abonnement SMS

Il existe deux états d’abonnement pour les utilisateurs de SMS : `subscribed` et `unsubscribed`. L’état d’abonnement d’un utilisateur n’est pas partagé entre les groupes d’abonnement, ce qui signifie qu’un utilisateur peut être `subscribed` pour un groupe d’abonnement transactionnel, `unsubscribed` pour un groupe promotionnel. Pour les marques, cette séparation des états assure qu’ils peuvent continuer à envoyer des SMS pertinents à leurs utilisateurs.

| État | Définition |
| --------- | ---------- |
| Abonné | L’utilisateur a explicitement confirmé qu’il souhaite recevoir des SMS de la part d’un groupe d’abonnement spécifique. Un utilisateur peut souscrire soit en faisant mettre à jour son état d’abonnement par l’API d’abonnement de Braze, soit en envoyant une réponse avec un mot clé d’abonnement. Un utilisateur doit être abonné à un groupe d’abonnement SMS pour recevoir un SMS |
| Non inscrit | L’utilisateur s’est explicitement désabonné de la messagerie de votre groupe d’abonnement SMS et des numéros de téléphone d’envoi au sein du groupe d’abonnement. Il peut se désabonner en envoyant une réponse avec un mot clé de désabonnement ou une marque peut désabonner des utilisateurs au moyen de l’[API abonnement de Braze][4]. Les utilisateurs désabonnés d’un groupe d’abonnement SMS ne reçoivent plus de SMS des numéros de téléphone émetteurs appartenant au groupe d’abonnement.|
{: .reset-td-br-1 .reset-td-br-2}

### Comment les groupes d’abonnement SMS d’utilisateurs sont mis en place

- **Ensemble API Rest** : Des profils d’utilisateur peuvent être définis en programmation par l’endpoint [/subscription/status/set][4] en utilisant l’API REST de Braze.
- **Automatiquement géré lors de l’abonnement/désabonnement de l’utilisateur :** Lorsque les utilisateurs envoient un [mot-clé][7] d’abonnement ou de désabonnement par défaut, Braze configure et met à jour automatiquement l’état d’abonnement des utilisateurs.

### Comment vérifier le groupe d’abonnement SMS d’un utilisateur

- **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze en sélectionnant **User Search** dans la barre latérale. Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Une fois dans un profil utilisateur, sous l’onglet **Engagement**, vous pouvez afficher les groupes d’abonnement SMS d’un utilisateur. 
- **Ensemble API Get** : Le groupe d’abonnement de profils d’utilisateurs individuels peut être consulté par l’endpoint [/subscription/user/status][9] ou l’endpoint [/subscription/status/get][8] au moyen de l’API REST de Braze. 

## Envoi avec un groupe d’abonnement

Pour lancer une campagne SMS via Braze, un groupe d’abonnement doit être sélectionné dans la liste déroulante, comme illustré dans l’image suivante. Après la sélection, un filtre d’audience sera ajouté à votre campagne ou Canvas automatiquement, ce qui assure que seuls les utilisateurs `subscribed` au groupe d’abonnement sélectionné font partie de l’audience cible. Pour se conformer aux [lignes directrices internationales de conformité pour les télécommunications][3], Braze n’enverra jamais de SMS aux utilisateurs qui n’ont pas souscrit au groupe d’abonnement sélectionné.  

![Sélection d’un groupe d’abonnement lors de la composition d’un SMS sur le tableau de bord de Braze][6]

## Processus de configuration

Au cours de votre processus d’onboarding par SMS, un gestionnaire d’onboarding de Braze configurera les groupes d’abonnement pour votre compte de tableau de bord. Il ou elle travaillera avec vous pour déterminer le nombre de groupes d’abonnement dont vous avez besoin et ajouter les numéros de téléphone émetteurs appropriés pour vos groupes d’abonnement. Les délais de configuration d’un groupe d’abonnement dépendent du type de numéros de téléphone que vous ajoutez. 

Par exemple, les applications de code court peuvent prendre entre 8 et 12 semaines, tandis que les codes longs peuvent être configurés en une journée. Si vous avez des questions sur la configuration de votre tableau de bord de Braze, contactez votre conseiller Braze pour obtenir de l’aide.  

## Habilitation MMS du groupe d’abonnement

Pour envoyer un message MMS, au moins un numéro au sein de votre groupe d’abonnement doit être activé pour envoyer MMS. Ceci est indiqué par une balise située à côté du groupe d’abonnement.

![Liste déroulante des groupes d’abonnement avec MMS et balises SMS pour chaque groupe][10]{: style="max-width:40%"}

[1]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[2]: {{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/
[3]: {{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_laws_and_regulations/
[4]: {{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[6]: {% image_buster /assets/img/sms/sms_subgroup_select.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[10]: {% image_buster /assets/img/sms/mms_sub_group_tag.png %}

