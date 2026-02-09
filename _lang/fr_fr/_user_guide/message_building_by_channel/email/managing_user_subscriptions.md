---
nav_title: Abonnements e-mail
article_title: Abonnements aux e-mails
page_order: 6
description: "Le présent article de référence couvre les différents états d’abonnement des utilisateurs, la création et la gestion des groupes d’abonnement, et la façon de segmenter les utilisateurs en fonction de leurs abonnements."
channel:
  - email

---

# Abonnements e-mail

> Découvrez les états d'abonnement des utilisateurs, comment créer et gérer des subscription groups et comment segmenter les utilisateurs en fonction de leurs abonnements.

Ce document n'est fourni qu'à titre d'information. Il n'a pas pour but de fournir des conseils juridiques à quelque titre que ce soit et ne peut être considéré comme tel. L'envoi d'e-mails marketing et transactionnels peut être soumis à des exigences légales spécifiques. Pour vous assurer que vous le faites en conformité avec toutes les lois, règles et réglementations applicables spécifiques à votre entreprise, vous devriez demander l'avis de votre conseiller juridique et/ou de votre équipe de conformité réglementaire.

## Statuts d’abonnement {#subscription-states}

Braze propose trois états d'abonnement global pour les utilisateurs d'e-mail. Ces états servent de porte d'entrée à vos messages de la part des utilisateurs. Par exemple, les utilisateurs de l'état `unsubscribed` ne reçoivent pas les messages ciblés sur `subscribed` ou `opted-in`.

| État | Définition |
| ----- | ---------- |
| Abonné | Un utilisateur a explicitement confirmé qu'il souhaitait recevoir des e-mails. Nous recommandons un processus explicite d’abonnement pour obtenir le consentement des utilisateurs à l’envoi d’e-mails. |
| Abonné | Un utilisateur ne s'est pas désabonné et n'a pas explicitement choisi de recevoir des e-mails. Il s’agit de l’état d’abonnement par défaut lorsqu’un profil utilisateur est créé. |
| Désabonné | Un utilisateur s'est explicitement désabonné de vos e-mails. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Braze ne compte pas les changements d’état d’abonnement par rapport à vos points de données, globalement, et autour des groupes d’abonnement.
{% endalert %}

### Adresses e-mail désabonnées

Braze désabonne automatiquement tout utilisateur qui se désabonne manuellement via un [pied de page personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Si l'utilisateur met à jour son adresse e-mail et que l'option **Réinscrire les utilisateurs lorsqu'ils mettent à jour leur e-mail** est activée dans **Configuration de l'envoi**, l'envoi normal reprend.

Si un utilisateur marque un ou plusieurs de vos e-mails comme étant du spam, Braze ne lui envoie que des e-mails transactionnels. Les e-mails transactionnels font référence à l'option **Envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés**, dans **Audience cible.**

{% alert tip %}
Consultez nos bonnes pratiques en matière de [réchauffement d'adresses IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) pour savoir comment réengager efficacement vos utilisateurs.
{% endalert %}

### Adresses e-mails non valides et messages non délivrés

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} 

Lorsqu'une adresse e-mail fait l'objet d'un échec définitif, Braze ne définit pas automatiquement l'état de l'abonnement de l'utilisateur comme "désabonné". Si une adresse fait l'objet d'un échec d'envoi définitif (invalide ou inexistante), Braze la marque comme invalide et ne tente pas d'autres envois. Si l'utilisateur change d'adresse e-mail, Braze reprend l'envoi. Braze relance les échecs provisoires d'envois pendant 72 heures.

### Mettre à jour les états d’abonnement aux e-mails

Il existe quatre façons de mettre à jour l'état de l'abonnement à l'e-mail d'un utilisateur :

#### Intégration SDK

Utilisez le SDK de Braze pour mettre à jour le statut d’abonnement d’un utilisateur.

#### API REST

Utilisez l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour l'[attribut`email_subscribe` ]({{site.baseurl}}/api/objects_filters/user_attributes_object) d'un utilisateur.

#### Profil utilisateur

1. Trouvez l'utilisateur par le biais de la **recherche d'utilisateurs**. 
2. Sous **Engagement**, sélectionnez **Désabonné**, **Abonné** ou **Ouvert** pour modifier le statut d'abonnement de l'utilisateur. 

Si disponible, le profil utilisateur affiche également un horodatage de la dernière modification de l’abonnement de l’utilisateur.

#### Centre de préférences

Incluez le liquide du [centre de préférences](#email-preference-center) au bas de vos e-mails pour permettre aux utilisateurs d'accepter ou de refuser. Braze gère les abonnements à partir du centre de préférences.

### Vérification de l’état de l’abonnement aux e-mails

![Profil utilisateur de John Doe avec son état d'abonnement aux e-mails défini sur Abonné.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Vous pouvez vérifier l'état de l'abonnement à l'e-mail d'un utilisateur de la manière suivante :

1. **Exportation de l'API REST :** Utilisez les endpoints [Exporter les utilisateurs par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Exporter les utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour exporter des profils utilisateurs individuels au format JSON.
2. **Profil utilisateur :** Trouvez le profil de l'utilisateur sur la page [Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/), puis sélectionnez l'onglet **Engagement** pour afficher et mettre à jour manuellement l'état de l'abonnement d'un utilisateur.

Lorsqu'un utilisateur met à jour son adresse e-mail, l'état de son abonnement devient abonné, sauf si l'adresse e-mail mise à jour existe déjà ailleurs dans un espace de travail de Braze.

## Groupes d’abonnement

Les groupes d'abonnement sont des filtres de segmentation qui permettent de restreindre davantage votre audience à partir des [états d'abonnement globaux](#subscription-states). Vous pouvez ajouter jusqu'à 350 groupes d'abonnement par espace de travail. Ces groupes vous permettent de présenter des options d’abonnement plus granulaires aux utilisateurs finaux.

Supposons par exemple que vous envoyiez plusieurs catégories de campagnes d'e-mail (promotionnelles, bulletins d'information ou mises à jour de produits). Dans ce cas, vous pouvez utiliser les groupes d'abonnement pour permettre à vos clients de choisir les catégories d'e-mails auxquelles ils souhaitent s'abonner ou se désabonner en masse à partir d'une seule page, en utilisant un [centre de préférences pour les e-mails.](#email-preference-center) Vous pouvez également utiliser des groupes d’abonnement pour permettre à vos clients de choisir la fréquence à laquelle ils souhaitent recevoir des e-mails de votre part, en créant des groupes d’abonnement pour les e-mails quotidiens, hebdomadaires ou mensuels.

Utilisez les [endpoints Groupe d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) pour gérer de manière programmatique les groupes d'abonnement que vous avez stockés sur le tableau de bord de Braze vers la page **Groupe d'abonnement**.

### Création d'un groupe d'abonnement

1. Allez dans **Audience** > Gestion des groupes d'abonnements **.**
2. Sélectionnez **Créer un groupe d'abonnement e-mail**. 
3. Donnez un nom et une description à votre groupe d'abonnement.
4. Sélectionnez **Enregistrer**. 

Tous les groupes d’abonnement sont automatiquement ajoutés à votre centre de préférences.

![Champs pour créer un groupe d'abonnement.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentation à l'aide d'un groupe d'abonnement

Lors de la création de vos segments, définissez le nom du groupe d’abonnement comme filtre. Cela confirmera que les utilisateurs qui ont opté pour votre groupe recevront vos e-mails. C’est très pratique pour les bulletins d’information mensuels, les bons de réduction, les niveaux d’adhésion et bien plus encore.

![Exemple de ciblage des utilisateurs du segment "Utilisateurs déchus" avec le filtre pour les utilisateurs du groupe d'abonnement "Emails hebdomadaires".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivage des groupes d'abonnement

Les groupes d’abonnement archivés ne peuvent pas être modifiés et n’apparaîtront plus dans les filtres de segments ou dans votre centre de préférences. Si vous tentez d’archiver un groupe utilisé comme filtre de segment dans un e-mail, une campagne ou Canvas, vous recevrez un message d’erreur qui vous empêchera d’archiver le groupe jusqu’à ce que vous supprimiez toutes les utilisations de celui-ci.

Pour archiver votre groupe à partir de la page **Groupes d'abonnement**, procédez comme suit :

1. Recherchez votre groupe dans la liste des groupes d'abonnement. 
2. Sélectionnez **Archive** dans le menu déroulant <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze ne traite pas les changements d'état pour les utilisateurs des groupes archivés. Par exemple, si vous archivez le groupe d'abonnement 1 alors qu'Alex y est abonné, Alex reste "abonné" même s'il clique sur un lien de désabonnement. Cela n'a pas d'importance car le groupe d'abonnement 1 est archivé et vous ne pouvez pas envoyer de messages en l'utilisant.

#### Affichage de la taille des groupes d'abonnement

Vous pouvez faire référence au graphique de **la série chronologique du groupe d'** abonnement dans la page **Groupes d'abonnement** pour visualiser la taille du groupe d'abonnement en fonction du nombre d'utilisateurs sur une période donnée. Ces tailles de groupes d'abonnement sont également cohérentes avec d'autres aspects de Braze, tels que le calcul de la taille des segments.

![Un exemple de graphique de "groupe d'abonnement" daté du 2 au 11 décembre. Le graphique montre une augmentation d'environ 10 millions du nombre d'utilisateurs entre le 6e et le 7e jour.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Visualisation des groupes d'abonnement dans l'analyse/analytique des campagnes

Vous pouvez consulter le nombre d'utilisateurs qui ont modifié leur état d'abonnement (abonné ou désabonné) à partir d'une campagne e-mail spécifique sur la page d'analyse de cette campagne.

1. Sur la page **Analyse/analytique de** votre campagne, faites défiler la page jusqu'à la section **Performances des messages e-mail.** 
2. Sélectionnez la flèche située sous les **groupes d'abonnement** pour afficher le nombre total de changements d'état, tels qu'ils ont été soumis par vos clients.

![La page "Performance des messages e-mail" affiche le nombre total de changements d'état soumis par les clients.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

### Vérification du groupe d'abonnement e-mail d'un utilisateur

- **Profil utilisateur :** Les profils d'utilisateurs individuels peuvent être consultés via le tableau de bord Braze depuis la page [Rechercher des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Là, vous pouvez faire une recherche dans les profils utilisateur par adresse e-mail, numéro de téléphone ou ID utilisateur externe. Vous pouvez également consulter les groupes d'abonnement e-mail d'un utilisateur dans l'onglet **Engagement**.
- **API REST de Braze :** Utilisez le [point de terminaison Liste des groupes d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) ou [Statut du groupe d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) pour afficher les groupes d'abonnement d'un profil utilisateur individuel. 

## Centre de préférence des e-mails

Le centre de préférences e-mail vous permet de gérer les utilisateurs qui reçoivent les bulletins d'information des groupes d'abonnement. Vous le trouverez dans le tableau de bord sous **Groupes d'abonnement**. Chaque groupe d’abonnement que vous créez est ajouté à la liste du centre de préférences. 

Pour en savoir plus sur la manière d'ajouter ou de personnaliser un centre de préférences, reportez-vous à [Centre de préférences.]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/)

## Modifier des abonnements aux e-mails {#changing-email-subscriptions}

Dans la plupart des cas, les utilisateurs gèrent leurs abonnements aux e-mails par le biais de liens inclus dans les e-mails qu'ils reçoivent. Insérez un pied de page conforme à la loi avec un lien de désabonnement au bas de chaque e-mail. Lorsque les utilisateurs sélectionnent l'URL de désabonnement, Braze les désabonne et affiche une page d'atterrissage confirmant le changement. Inclure cette étiquette Liquid : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Lorsqu'un utilisateur sélectionne "Se désabonner de tous les types d'e-mails ci-dessus" dans le centre de préférences, Braze définit son statut d'abonnement global aux e-mails sur `unsubscribed` et le désabonne de tous les groupes.

### Création de pieds de page personnalisés {#custom-footer}

Si vous ne souhaitez pas utiliser le pied de page par défaut, créez un pied de page personnalisé pour l'ensemble de votre espace de travail et intégrez-le dans chaque e-mail à l'aide de {% raw %}`{{${email_footer}}}`{% endraw %}.

Cela vous permet d'éviter de créer un nouveau pied de page pour chaque modèle d'e-mail ou campagne d'e-mail. Pour la marche à suivre, voir [Pied de page personnalisé de l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/)

#### Gestion des abonnements pour les adresses IP chinoises

Si vous prévoyez des adresses IP chinoises, ne comptez pas uniquement sur un lien de désabonnement pour maintenir les listes `unsubscribed`. Proposez d'autres moyens de se désabonner, par exemple en envoyant un ticket d'assistance ou un e-mail à un conseiller clientèle. 

### Créer une page de désabonnement personnalisée

Lorsque les utilisateurs sélectionnent une URL de désinscription, Braze affiche une page d'atterrissage par défaut confirmant le changement.

Pour créer une page d'atterrissage personnalisée (au lieu de la page par défaut) qui s'affiche après l'abonnement :

1. Allez dans **Préférences e-mail** > **Pages et pieds de page d'abonnement.**
2. Fournissez le code HTML de votre page d'atterrissage personnalisée. 

Incluez un lien de réabonnement (tel que {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) afin que les utilisateurs puissent se réabonner s'ils se sont désabonnés par accident.

![Page de désabonnement personnalisée avec un aperçu "Désolé de vous voir partir !".]({% image_buster /assets/img/custom_unsubscribe.png %})

### Créer une page d'abonnement personnalisée

Utilisez une page d'abonnement personnalisée pour permettre aux utilisateurs de reconnaître et de contrôler leurs préférences en matière de notification avant de s'abonner. Cette communication supplémentaire peut aider les campagnes d'e-mail à ne pas tomber dans les dossiers de spam.

1. Allez dans **Paramètres** > **Préférences e-mail.**
2. Sélectionnez **Pages et pieds de page d'abonnement**.
3. Personnalisez le style dans la section **Page d'abonnement personnalisée** pour voir comment cela indique à vos utilisateurs qu'ils ont été abonnés.

Les utilisateurs accèdent à cette page par l'étiquette {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}.

{% alert tip %}
Utilisez un processus de double abonnement pour améliorer la sensibilisation. Braze envoie un e-mail de confirmation supplémentaire dans lequel l'utilisateur confirme ses préférences en matière de notification au moyen d'un lien. Après confirmation, l'utilisateur est abonné.
{% endalert %}

![Un e-mail d'abonnement personnalisé avec un message "Heureux de voir que vous voulez toujours entendre parler de nous".]({% image_buster /assets/img/custom_optin.png %})

## Abonnements et ciblage des campagnes {#subscriptions-and-campaign-targeting}

Par défaut, Braze cible les campagnes avec des messages push ou e-mail aux utilisateurs qui sont abonnés ou qui ont opté pour un abonnement. Modifiez ceci dans **Target Audience** en sélectionnant le menu déroulant à côté de **Send to these users :.**

Braze prend en charge trois états de ciblage :

- Les utilisateurs qui sont inscrits ou abonnés (par défaut).
- Uniquement les utilisateurs qui sont abonnés.
- Tous les utilisateurs, y compris ceux qui se sont désabonnés.

{% alert important %}
Il est de votre responsabilité de vous conformer aux [lois applicables en matière de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) lorsque vous utilisez ces paramètres de ciblage.
{% endalert %}

## Segmenter par abonnements de l’utilisateur {#segmenting-by-user-subscriptions}

Utilisez les filtres "Statut de l'abonnement par e-mail" et "Statut de l'abonnement par push" pour segmenter les utilisateurs en fonction du statut de l'abonnement.

Utilisez cette option pour cibler les utilisateurs qui n'ont pas choisi de s'abonner ou de se désabonner et encouragez-les à s'abonner explicitement. Créez un segment avec le filtre "Email/Push Subscription Status is Subscribed" et envoyez des campagnes aux utilisateurs qui sont abonnés mais qui n'ont pas opté pour l'abonnement.

![Statut d’abonnement aux e-mails utilisé comme filtre de segment.]({% image_buster /assets/img_archive/not_optin.png %})

