---
nav_title: Abonnements e-mail
article_title: Abonnements aux e-mails
page_order: 6
description: "Le présent article de référence couvre les différents états d'abonnement des utilisateurs, la création et la gestion des groupes d'abonnement, et la façon de segmenter les utilisateurs en fonction de leurs abonnements."
channel:
  - email

---

# Abonnements e-mail

> Découvrez les statuts d'abonnement des utilisateurs, comment créer et gérer des groupes d'abonnement, et comment segmenter les utilisateurs en fonction de leurs abonnements.

Ce document n'est fourni qu'à titre d'information. Il n'a pas pour but de fournir des conseils juridiques à quelque titre que ce soit et ne peut être considéré comme tel. L'envoi d'e-mails marketing et transactionnels peut être soumis à des exigences légales spécifiques. Pour vous assurer que vous le faites en conformité avec toutes les lois, règles et réglementations applicables spécifiques à votre entreprise, vous devriez demander l'avis de votre conseiller juridique et/ou de votre équipe de conformité réglementaire.

## Statuts d'abonnement {#subscription-states}

Braze propose trois statuts d'abonnement globaux pour les utilisateurs d'e-mail. Ces statuts contrôlent la réception de vos messages par les utilisateurs. Par exemple, les utilisateurs ayant le statut `unsubscribed` ne reçoivent pas les messages ciblant les utilisateurs `subscribed` ou `opted-in`.

| État | Définition |
| ----- | ---------- |
| Abonné (opted-in) | Un utilisateur a explicitement confirmé qu'il souhaitait recevoir des e-mails. Nous recommandons un processus explicite d'abonnement pour obtenir le consentement des utilisateurs à l'envoi d'e-mails. |
| Abonné (subscribed) | Un utilisateur ne s'est pas désabonné et n'a pas explicitement choisi de recevoir des e-mails. Il s'agit du statut d'abonnement par défaut lorsqu'un profil utilisateur est créé. |
| Désabonné | Un utilisateur s'est explicitement désabonné de vos e-mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Braze ne compte pas les changements de statut d'abonnement dans vos points de données, que ce soit au niveau global ou au niveau des groupes d'abonnement.
{% endalert %}

### Adresses e-mail désabonnées

Braze désabonne automatiquement tout utilisateur qui se désabonne manuellement via un [pied de page personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Si l'utilisateur met à jour son adresse e-mail et que l'option **Réinscrire les utilisateurs lorsqu'ils mettent à jour leur adresse e-mail** est activée dans **Configuration d'envoi**, l'envoi normal reprend.

Si un utilisateur marque un ou plusieurs de vos e-mails comme spam, Braze n'enverra plus que des e-mails transactionnels à cet utilisateur. Les e-mails transactionnels font référence à l'option **Envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés** dans **Audience cible**.

{% alert tip %}
Consultez nos bonnes pratiques en matière de [réchauffement d'adresses IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) pour savoir comment réengager efficacement vos utilisateurs.
{% endalert %}

### Adresses e-mail non valides et messages non délivrés

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Lorsqu'un e-mail provoque un échec d'envoi définitif, Braze ne définit pas automatiquement le statut d'abonnement de l'utilisateur sur « désabonné ». Si une adresse provoque un échec d'envoi définitif (invalide ou inexistante), Braze la marque comme invalide et ne tente plus d'envoyer de messages. Si l'utilisateur modifie son adresse e-mail, Braze reprend l'envoi. Braze effectue des tentatives de renvoi pour les échecs provisoires d'envoi pendant 72 heures.

### Mettre à jour les statuts d'abonnement aux e-mails

Il existe quatre façons de mettre à jour le statut d'abonnement aux e-mails d'un utilisateur :

#### Intégration SDK

Utilisez le SDK de Braze pour mettre à jour le statut d'abonnement d'un utilisateur.

#### API REST

Utilisez l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour l'[attribut `email_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object) d'un utilisateur. Par exemple, pour définir le statut d'abonnement aux e-mails d'un utilisateur sur « désabonné » lorsqu'il utilise un lien de désabonnement personnalisé, incluez `email_subscribe: "unsubscribed"` dans les attributs utilisateur de votre requête.

#### Profil utilisateur

1. Trouvez l'utilisateur via **Rechercher des utilisateurs**. 
2. Sous **Engagement**, sélectionnez **Désabonné**, **Abonné** ou **Abonnement confirmé** pour modifier le statut d'abonnement de l'utilisateur. 

Si disponible, le profil utilisateur affiche également un horodatage de la dernière modification du statut d'abonnement de l'utilisateur.

#### Centre de préférences

Incluez le [centre de préférences](#email-preference-center) Liquid au bas de vos e-mails afin de permettre aux utilisateurs de s'abonner ou de se désabonner. Braze gère les mises à jour du statut d'abonnement à partir du centre de préférences.

### Vérifier le statut d'abonnement aux e-mails

![Profil utilisateur de John Doe avec son statut d'abonnement aux e-mails défini sur Abonné.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez vérifier le statut d'abonnement aux e-mails d'un utilisateur de différentes manières :

1. **Exportation via l'API REST :** Utilisez les endpoints [Exporter les utilisateurs par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Exporter les utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour exporter des profils utilisateurs individuels au format JSON.
2. **Profil utilisateur :** Trouvez le profil de l'utilisateur sur la page [Rechercher des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/), puis sélectionnez l'onglet **Engagement** pour afficher et mettre à jour manuellement le statut d'abonnement d'un utilisateur.

Lorsqu'un utilisateur met à jour son adresse e-mail, son statut d'abonnement est défini sur « abonné », sauf si l'adresse e-mail mise à jour existe déjà ailleurs dans un espace de travail Braze.

## Groupes d'abonnement

Les groupes d'abonnement sont des filtres de segmentation qui permettent de restreindre davantage votre audience à partir des [statuts d'abonnement globaux](#subscription-states). Vous pouvez ajouter jusqu'à 350 groupes d'abonnement par espace de travail. Ces groupes vous permettent de présenter des options d'abonnement plus granulaires aux utilisateurs finaux.

Supposons par exemple que vous envoyiez plusieurs catégories de campagnes d'e-mail (promotionnelles, newsletters ou mises à jour de produits). Dans ce cas, vous pouvez utiliser les groupes d'abonnement pour permettre à vos clients de choisir les catégories d'e-mails auxquelles ils souhaitent s'abonner ou se désabonner en masse à partir d'une seule page, en utilisant un [centre de préférences pour les e-mails](#email-preference-center). Vous pouvez également utiliser des groupes d'abonnement pour permettre à vos clients de choisir la fréquence à laquelle ils souhaitent recevoir des e-mails de votre part, en créant des groupes d'abonnement pour les e-mails quotidiens, hebdomadaires ou mensuels.

Utilisez les [endpoints Groupe d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) pour gérer de manière programmatique les groupes d'abonnement que vous avez stockés sur le tableau de bord de Braze via la page **Groupe d'abonnement**.

### Créer un groupe d'abonnement

1. Rendez-vous dans **Audience** > **Gestion des groupes d'abonnement**.
2. Sélectionnez **Créer un groupe d'abonnement e-mail**. 
3. Donnez un nom et une description à votre groupe d'abonnement.
4. Sélectionnez **Enregistrer**. 

Tous les groupes d'abonnement sont automatiquement ajoutés à votre centre de préférences.

![Champs pour créer un groupe d'abonnement.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmenter avec un groupe d'abonnement

Lors de la création de vos segments, définissez le nom du groupe d'abonnement comme filtre. Cela garantit que les utilisateurs qui ont opté pour votre groupe recevront vos e-mails. C'est très pratique pour les newsletters mensuelles, les bons de réduction, les niveaux d'adhésion et bien plus encore.

![Exemple de ciblage des utilisateurs du segment « Utilisateurs inactifs » avec le filtre pour les utilisateurs du groupe d'abonnement « E-mails hebdomadaires ».]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archiver des groupes d'abonnement

Les groupes d'abonnement archivés ne peuvent pas être modifiés et n'apparaîtront plus dans les filtres de segments ni dans votre centre de préférences. Si vous tentez d'archiver un groupe utilisé comme filtre de segment dans un e-mail, une campagne ou un Canvas, vous recevrez un message d'erreur qui vous empêchera d'archiver le groupe tant que vous n'aurez pas supprimé toutes ses utilisations.

Pour archiver votre groupe à partir de la page **Groupes d'abonnement**, procédez comme suit :

1. Recherchez votre groupe dans la liste des groupes d'abonnement. 
2. Sélectionnez **Archiver** dans le menu déroulant <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze ne traite pas les changements de statut pour les utilisateurs des groupes archivés. Par exemple, si vous archivez le groupe d'abonnement 1 alors qu'Alex y est abonné, Alex reste « abonné » même s'il clique sur un lien de désabonnement. Cela n'a pas d'importance, car le groupe d'abonnement 1 est archivé et vous ne pouvez pas envoyer de messages via ce groupe.

#### Consulter la taille des groupes d'abonnement

Vous pouvez consulter le graphique **Série chronologique du groupe d'abonnement** sur la page **Groupes d'abonnement** pour visualiser la taille du groupe d'abonnement en fonction du nombre d'utilisateurs sur une période donnée. Ces tailles de groupes d'abonnement sont également cohérentes avec d'autres aspects de Braze, tels que le calcul de la taille des segments.

![Un exemple de graphique « Série chronologique du groupe d'abonnement » daté du 2 au 11 décembre. Le graphique montre une augmentation d'environ 10 millions du nombre d'utilisateurs entre le 6 et le 7.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Consulter les groupes d'abonnement dans l'analytique des campagnes

Vous pouvez consulter le nombre d'utilisateurs ayant modifié leur statut d'abonnement (abonnés ou désabonnés) à partir d'une campagne d'e-mails spécifique sur la page d'analytique de cette campagne.

1. Sur la page **Analytique de la campagne**, faites défiler la page jusqu'à la section **Performance des messages e-mail**. 
2. Sélectionnez la flèche sous **Groupes d'abonnement** pour afficher le nombre total de changements de statut soumis par vos clients.

![La page « Performance des messages e-mail » affichant le nombre total de changements de statut soumis par les clients.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Vérifier le groupe d'abonnement aux e-mails d'un utilisateur

- **Profil utilisateur :** Les profils utilisateurs individuels sont accessibles via le tableau de bord de Braze depuis la page [Rechercher des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Vous pouvez y rechercher des profils utilisateurs par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Vous pouvez également consulter les groupes d'abonnement aux e-mails d'un utilisateur dans l'onglet **Engagement**.
- **API REST Braze :** Utilisez l'[endpoint Lister les groupes d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou l'[endpoint Lister le statut du groupe d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) pour afficher les groupes d'abonnement du profil utilisateur. 

## Centre de préférences des e-mails

Le centre de préférences des e-mails vous permet de gérer les utilisateurs qui reçoivent les newsletters des groupes d'abonnement. Vous le trouverez dans le tableau de bord sous **Groupes d'abonnement**. Chaque groupe d'abonnement que vous créez est ajouté à la liste du centre de préférences. 

Pour en savoir plus sur la manière d'ajouter ou de personnaliser un centre de préférences, consultez [Centre de préférences]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/).

## Modifier les abonnements aux e-mails {#changing-email-subscriptions}

Dans la plupart des cas, les utilisateurs gèrent leur abonnement aux e-mails via les liens inclus dans les e-mails qu'ils reçoivent. Insérez un pied de page conforme à la législation avec un lien de désabonnement au bas de chaque e-mail. Lorsque les utilisateurs cliquent sur l'URL de désabonnement, Braze procède à leur désabonnement et affiche une page de confirmation de la modification. Incluez cette étiquette Liquid : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Lorsqu'un utilisateur sélectionne « Se désabonner de tous les types d'e-mails ci-dessus » dans le centre de préférences, Braze définit son statut d'abonnement global aux e-mails sur `unsubscribed` et le désabonne de tous les groupes.

### Créer des pieds de page personnalisés {#custom-footer}

Si vous ne souhaitez pas utiliser le pied de page par défaut, créez un pied de page personnalisé pour l'ensemble de l'espace de travail et intégrez-le à chaque e-mail à l'aide de {% raw %}`{{${email_footer}}}`{% endraw %}.

Cela vous évite de devoir créer un nouveau pied de page pour chaque modèle d'e-mail ou campagne d'e-mail. Pour connaître la procédure à suivre, consultez [Pied de page personnalisé pour les e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/).

#### Gérer les abonnements pour les adresses IP chinoises

Si vous prévoyez de recevoir des connexions depuis des adresses IP chinoises, ne vous fiez pas uniquement à un lien de désabonnement pour gérer vos listes `unsubscribed`. Proposez d'autres moyens de se désabonner, tels qu'un ticket d'assistance ou l'adresse e-mail d'un conseiller du service clientèle. 

### Créer une page de désabonnement personnalisée

Lorsque les utilisateurs cliquent sur un lien de désabonnement, Braze affiche une page par défaut confirmant la modification.

Pour créer une page personnalisée (au lieu de la page par défaut) qui s'affiche après l'abonnement :

1. Allez dans **Préférences e-mail** > **Pages et pieds de page d'abonnement**.
2. Fournissez le code HTML de votre page personnalisée. 

Incluez un lien de réinscription (tel que {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) afin que les utilisateurs puissent se réinscrire s'ils se sont désabonnés par inadvertance.

![Page de désabonnement personnalisée avec un aperçu « Nous regrettons votre départ ! ».]({% image_buster /assets/img/custom_unsubscribe.png %})

### Créer une page d'abonnement personnalisée

Utilisez une page d'abonnement personnalisée pour permettre aux utilisateurs de confirmer et de contrôler leurs préférences de notification avant de s'abonner. Cette communication supplémentaire peut contribuer à éviter que vos campagnes d'e-mail ne soient classées dans les dossiers de courrier indésirable.

1. Allez dans **Paramètres** > **Préférences e-mail**.
2. Sélectionnez **Pages et pieds de page d'abonnement**.
3. Personnalisez le style dans la section **Page d'abonnement personnalisée** pour indiquer à vos utilisateurs qu'ils ont bien été abonnés.

Les utilisateurs accèdent à cette page via l'étiquette {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}.

{% alert tip %}
Utilisez un processus de double abonnement pour améliorer la portée de vos communications. Braze envoie un e-mail de confirmation supplémentaire dans lequel l'utilisateur confirme ses préférences de notification via un lien. Après confirmation, l'utilisateur bénéficie d'un abonnement confirmé.
{% endalert %}

![E-mail d'abonnement personnalisé avec le message « Nous sommes ravis de constater que vous souhaitez toujours recevoir nos communications ».]({% image_buster /assets/img/custom_optin.png %})

## Abonnements et ciblage des campagnes {#subscriptions-and-campaign-targeting}

Par défaut, Braze cible les campagnes avec des messages push ou des e-mails vers les utilisateurs abonnés ou ayant donné leur consentement. Modifiez ce paramètre dans **Audience cible** en sélectionnant le menu déroulant à côté de **Envoyer à ces utilisateurs :**.

Braze prend en charge trois états de ciblage :

- Les utilisateurs qui sont abonnés ou ont donné leur consentement (par défaut).
- Uniquement les utilisateurs qui ont donné leur consentement.
- Tous les utilisateurs, y compris ceux qui se sont désabonnés.

{% alert important %}
Il est de votre responsabilité de vous conformer aux [lois applicables en matière de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) lorsque vous utilisez ces paramètres de ciblage.
{% endalert %}

## Segmenter par abonnements des utilisateurs {#segmenting-by-user-subscriptions}

Utilisez les filtres « Statut d'abonnement aux e-mails » et « Statut d'abonnement push » pour segmenter les utilisateurs en fonction de leur statut d'abonnement.

Utilisez cette option pour cibler les utilisateurs qui n'ont ni accepté ni refusé un abonnement et les encourager à donner leur consentement explicite. Créez un segment avec le filtre « Statut d'abonnement aux e-mails/notifications push : abonné » et envoyez des campagnes aux utilisateurs abonnés mais qui n'ont pas donné leur consentement.

![Statut d'abonnement aux e-mails utilisé comme filtre de segment.]({% image_buster /assets/img_archive/not_optin.png %})