---
nav_title: Abonnements aux e-mails
article_title: Abonnements aux e-mails
page_order: 6
description: "Le présent article de référence couvre les différents états d’abonnement des utilisateurs, la création et la gestion des groupes d’abonnement, et la façon de segmenter les utilisateurs en fonction de leurs abonnements."
channel:
  - email

---

# Abonnements e-mail

> Découvrez les différents états d'abonnement des utilisateurs, comment créer et gérer des groupes d'abonnements et comment segmenter les utilisateurs en fonction de leurs abonnements.

Ce document n'est fourni qu'à titre d'information. Il n'a pas pour but de fournir des conseils juridiques à quelque titre que ce soit et ne peut être considéré comme tel. L'envoi d'e-mails marketing et transactionnels peut être soumis à des exigences légales spécifiques. Pour vous assurer que vous le faites en conformité avec toutes les lois, règles et réglementations applicables spécifiques à votre entreprise, vous devriez demander l'avis de votre conseiller juridique et/ou de votre équipe de conformité réglementaire.

## Statuts d’abonnement {#subscription-states}

Braze dispose de trois états d'abonnement globaux pour les utilisateurs d'e-mail (énumérés dans le tableau suivant), qui sont les gardiens finaux entre vos messages et vos utilisateurs. Par exemple, les utilisateurs considérés comme `unsubscribed` ne recevront pas de messages ciblés à l’état d’abonnement global de `subscribed` ou `opted-in`.

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

Braze désabonnera automatiquement tout utilisateur qui se désabonne manuellement de votre e-mail par le biais d'un [pied de page personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer). Si l'utilisateur met à jour son adresse e-mail et que l'option **Réinscrire les utilisateurs lorsqu'ils mettent à jour leur adresse e-mail** est activée dans vos paramètres de **configuration de l'envoi**, l'envoi normal d'e-mails reprendra.

Si un utilisateur a marqué un ou plusieurs de vos e-mails comme étant des spams, Braze ne lui enverra que des e-mails transactionnels. Dans ce cas, les e-mails transactionnels se réfèrent à l'option sélectionnée **Envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés**, dans l'étape **Audience cible.** 

{% alert tip %}
Consultez nos bonnes pratiques en matière de [réchauffement d'adresses IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) pour savoir comment réengager efficacement vos utilisateurs.
{% endalert %}

### Adresses e-mails non valides et messages non délivrés

{% multi_lang_include metrics.md metric='Hard Bounce' %} {% multi_lang_include metrics.md metric='Soft Bounce' %} 

Lorsqu'une adresse e-mail fait l'objet d'un échec d'envoi définitif, l'état de l'abonnement de l'utilisateur n'est pas automatiquement défini comme "désabonné". En cas d'échec d'envoi définitif (par exemple lorsqu'un e-mail n'est pas valide ou n'existe pas), nous marquerons l'adresse e-mail de l'utilisateur comme invalide et n'essaierons pas d'envoyer d'autres e-mails à cette adresse. Si l’utilisateur change son adresse e-mail, nous recommencerons à lui envoyer des e-mails puisque sa nouvelle adresse sera sans doute valide. Les « soft bounces » sont automatiquement réessayés pendant 72 heures.

### Mettre à jour les états d’abonnement aux e-mails

Il existe quatre façons de mettre à jour l'état de l'abonnement à l'e-mail d'un utilisateur :

#### Intégration SDK

Utilisez le SDK de Braze pour mettre à jour le statut d’abonnement d’un utilisateur.

#### API REST

Utilisez l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour mettre à jour l'[attribut`email_subscribe` ]({{site.baseurl}}/api/objects_filters/user_attributes_object) pour un utilisateur donné.

#### Profil utilisateur

1. Trouvez l'utilisateur par le biais de la **recherche d'utilisateurs**. 
2. Sous l'onglet **Engagement**, sélectionnez les boutons **Désabonné**, **Abonné** ou **Ouvert pour** modifier l'état de l'abonnement de cet utilisateur. 

Si disponible, le profil utilisateur affiche également un horodatage de la dernière modification de l’abonnement de l’utilisateur.

#### Centre de préférences

Le code Liquid du [centre de préférences](#email-preference-center) peut être inclus au bas de vos e-mails, ce qui permet aux utilisateurs de s’abonner ou de se désabonner des e-mails. Braze gère les mises à jour du statut d’abonnement depuis le centre de préférences.

### Vérification de l’état de l’abonnement aux e-mails

![Profil utilisateur de John Doe dont l'état de l'abonnement à l'e-mail est réglé sur Abonné.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l'état de l'abonnement aux e-mails d'un utilisateur avec Braze :

1. **Exportation de l'API REST :** Utilisez les endpoints [Exporter les utilisateurs par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) ou [Exporter les utilisateurs par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour exporter des profils utilisateurs individuels au format JSON.
2. **Profil utilisateur :** Trouvez le profil de l'utilisateur sur la page [Recherche d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/), puis sélectionnez l'onglet **Engagement** pour afficher et mettre à jour manuellement l'état de l'abonnement d'un utilisateur. 

Lorsqu'un utilisateur met à jour son adresse e-mail, l'état de son abonnement devient abonné, sauf si l'adresse e-mail mise à jour existe déjà ailleurs dans un espace de travail de Braze.

## Groupes d’abonnement

Les groupes d'abonnement sont des filtres de segmentation qui permettent de restreindre davantage votre audience à partir des [états d'abonnement globaux](#subscription-states). Vous pouvez ajouter jusqu'à 350 groupes d'abonnement par espace de travail. Ces groupes vous permettent de présenter des options d’abonnement plus granulaires aux utilisateurs finaux.

Supposons par exemple que vous envoyiez plusieurs catégories de campagnes d'e-mail (promotionnelles, bulletins d'information ou mises à jour de produits). Dans ce cas, vous pouvez utiliser les groupes d'abonnement pour permettre à vos clients de choisir les catégories d'e-mails auxquelles ils souhaitent s'abonner ou se désabonner en masse à partir d'une seule page, en utilisant un [centre de préférences pour les e-mails.](#email-preference-center) Vous pouvez également utiliser des groupes d’abonnement pour permettre à vos clients de choisir la fréquence à laquelle ils souhaitent recevoir des e-mails de votre part, en créant des groupes d’abonnement pour les e-mails quotidiens, hebdomadaires ou mensuels.

Utilisez les [endpoints Groupe d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups) pour gérer de manière programmatique les groupes d'abonnement que vous avez stockés sur le tableau de bord de Braze vers la page **Groupe d'abonnement**.

### Création d'un groupe d'abonnement

1. Allez dans **Audience** > **Abonnements**.
2. Sélectionnez **Créer un groupe d'abonnement e-mail**. 
3. Donnez un nom et une description à votre groupe d'abonnement.
4. Sélectionnez **Enregistrer**. 

Tous les groupes d’abonnement sont automatiquement ajoutés à votre centre de préférences.

![Champs permettant de créer un groupe d'abonnement.]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

### Segmentation à l'aide d'un groupe d'abonnement

Lors de la création de vos segments, définissez le nom du groupe d’abonnement comme filtre. Cela confirmera que les utilisateurs qui ont opté pour votre groupe recevront vos e-mails. C’est très pratique pour les bulletins d’information mensuels, les bons de réduction, les niveaux d’adhésion et bien plus encore.

![Exemple de ciblage des utilisateurs du segment "Utilisateurs déchus" à l'aide du filtre pour les utilisateurs du groupe d'abonnement "Alertes stables".]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

### Archivage des groupes d'abonnement

Les groupes d’abonnement archivés ne peuvent pas être modifiés et n’apparaîtront plus dans les filtres de segments ou dans votre centre de préférences. Si vous tentez d’archiver un groupe utilisé comme filtre de segment dans un e-mail, une campagne ou Canvas, vous recevrez un message d’erreur qui vous empêchera d’archiver le groupe jusqu’à ce que vous supprimiez toutes les utilisations de celui-ci.

Pour archiver votre groupe à partir de la page **Groupes d'abonnement**, procédez comme suit :

1. Recherchez votre groupe dans la liste des groupes d'abonnement. 
2. Sélectionnez **Archive** dans le menu déroulant <i class="fa-solid fa-ellipsis-vertical"></i>.

Braze ne traitera aucun changement d’état pour les utilisateurs des groupes archivés. Par exemple, si vous archivez le "Groupe d'abonnement A" alors que Susie y est abonnée, elle restera "abonnée" à ce groupe, même si elle clique sur un lien de désabonnement (cela ne devrait pas avoir d'importance pour Susie car le "Groupe d'abonnement A" est archivé et vous ne pouvez pas envoyer de messages en l'utilisant).

#### Affichage de la taille des groupes d'abonnement

Vous pouvez faire référence au graphique de **la série chronologique du groupe d'** abonnement dans la page **Groupes d'abonnement** pour visualiser la taille du groupe d'abonnement en fonction du nombre d'utilisateurs sur une période donnée. Ces tailles de groupes d'abonnement sont également cohérentes avec d'autres aspects de Braze, tels que le calcul de la taille des segments.

![Un exemple de graphique de "groupe d'abonnement" daté du 2 au 11 décembre. Le graphique montre une augmentation d'environ 10 millions d'utilisateurs entre le 6e et le 7e jour.]({% image_buster /assets/img_archive/subscription_group_graph.png %})

#### Visualisation des groupes d'abonnement dans l'analyse/analytique des campagnes

Vous pouvez voir le nombre d’utilisateurs qui ont modifié leur état d’abonnement (abonnement ou désabonnement) à partir d’une campagne d’e-mail spécifique sur la page d’analyse de cette campagne.

1. Sur la page **Analyse/analytique de** votre campagne, faites défiler la page jusqu'à la section **Performances des messages e-mail.** 
2. Sélectionnez la flèche située sous les **groupes d'abonnement** pour afficher le nombre total de changements d'état, tels qu'ils ont été soumis par vos clients.

![La page "Performance des messages e-mail" affiche le nombre total de changements d'état soumis par les clients.]({% image_buster /assets/img/campaign_analytics_sub_groups.png %})

## Centre de préférence des e-mails

Le centre de préférences e-mail est un moyen facile de gérer les utilisateurs qui reçoivent certains groupes de bulletins d'information. Il se trouve dans le tableau de bord sous **Groupes d'abonnement**. Chaque groupe d’abonnement que vous créez est ajouté à la liste du centre de préférences. 

Pour en savoir plus sur la manière d'ajouter ou de personnaliser un centre de préférences, reportez-vous à [Centre de préférences.]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/)

## Modifier des abonnements aux e-mails {#changing-email-subscriptions}

Dans la plupart des cas, vos utilisateurs gèrent leur abonnement aux e-mails via des liens d’abonnement inclus dans les e-mails qu’ils reçoivent. Vous devez insérer un pied de page légalement conforme avec un lien de désabonnement au bas de chaque e-mail que vous envoyez. Lorsque les utilisateurs sélectionnent l'URL de désabonnement dans votre pied de page, ils doivent être désabonnés et renvoyés vers une page de renvoi qui confirme la modification de leur abonnement. Nous vous recommandons d'inclure cette étiquette Liquid : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Notez que lorsqu'un utilisateur sélectionne "Se désabonner de tous les types d'e-mails ci-dessus" dans le centre de préférences e-mail, son statut d'abonnement global à l'e-mail est mis à jour à `unsubscribed` et il est désabonné de tous les groupes d'abonnement.

### Création de pieds de page personnalisés {#custom-footer}

Si vous ne souhaitez pas utiliser le pied de page par défaut de Braze dans vos e-mails, vous pouvez créer un pied de page personnalisé pour l'ensemble de votre espace de travail, que vous pouvez intégrer dans chaque e-mail à l'aide de l'attribut Liquid de {% raw %}`{{${email_footer}}}`{% endraw %}.

De cette façon, vous n’avez pas à créer un nouveau pied de page pour chaque modèle de courriel ou de campagne par e-mail que vous utilisez. Pour connaître la marche à suivre, reportez-vous à la section [Pied de page personnalisé de l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/)

#### Gestion des abonnements pour les adresses IP chinoises

Si vous prévoyez que les destinataires de vos e-mails auront une adresse IP chinoise, vous ne devez pas compter uniquement sur un lien de désabonnement dans votre e-mail pour maintenir vos listes `unsubscribed`. Au lieu de cela, proposez aux utilisateurs d'autres moyens de se désabonner facilement, comme l'ouverture d'un ticket d'assistance sur votre portail d'assistance ou l'envoi d'un e-mail à un conseiller clientèle. 

### Créer une page de désabonnement personnalisée

Lorsque les utilisateurs sélectionnent une URL de désabonnement dans un e-mail, ils sont dirigés vers une page de destination par défaut qui confirme la modification de leur abonnement.

Pour créer une page d'atterrissage personnalisée vers laquelle les utilisateurs seront dirigés (au lieu de la page par défaut) lorsqu'ils s'abonneront :

1. Allez dans **Préférences e-mail** > **Pages et pieds de page d'abonnement.**
2. Fournissez le code HTML de votre page d'atterrissage personnalisée. 

Nous vous recommandons d'inclure un lien de réinscription (tel que {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) sur la page de renvoi afin que les utilisateurs aient la possibilité de se réinscrire au cas où ils se seraient désinscrits par accident.

![E-mail de désabonnement personnalisé dans le panneau Page de désabonnement personnalisée.]({% image_buster /assets/img/custom_unsubscribe.png %})

### Créer une page d'abonnement personnalisée

Au lieu d’abonner immédiatement un utilisateur à vos campagnes par e-mail, la création d’une page d’abonnement personnalisée peut donner à vos utilisateurs la possibilité de reconnaître et de contrôler leurs préférences de notification. Cette communication supplémentaire peut également aider vos campagnes par e-mail à ne pas atterrir dans les courriers indésirables, car vos utilisateurs auront choisi de s’inscrire. 

1. Allez dans **Paramètres** > **Préférences e-mail.**
2. Sélectionnez **Pages et pieds de page d'abonnement**.
3. Personnalisez le style dans la section **Page d'abonnement personnalisée** pour voir comment cela indique à vos utilisateurs qu'ils ont été abonnés.

{% alert tip %}
Braze recommande d’utiliser un processus d’abonnement double pour vous aider à diffuser vos e-mails. Ce processus envoie un e-mail de confirmation supplémentaire dans lequel l'utilisateur confirme à nouveau ses préférences en matière de notification au moyen d'un lien figurant dans l'e-mail. À ce stade, l'utilisateur est considéré comme ayant donné son accord.
{% endalert %}

## Abonnements et ciblage des campagnes {#subscriptions-and-campaign-targeting}

Par défaut, les campagnes avec des messages push ou e-mail sont ciblées sur les utilisateurs qui sont abonnés ou opt-in par défaut. Vous pouvez modifier cette préférence de ciblage lorsque vous modifiez une campagne en accédant à l'étape **Audience cible** et en sélectionnant la liste déroulante en regard de **Envoyer à ces utilisateurs :.**

Braze prend en charge trois états de ciblage :

- Les utilisateurs qui sont inscrits ou abonnés (par défaut).
- Uniquement les utilisateurs qui sont abonnés.
- Tous les utilisateurs, y compris ceux qui se sont désabonnés.

{% alert important %}
Il est de votre responsabilité de vous conformer aux [lois applicables en matière de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) lorsque vous utilisez ces paramètres de ciblage.
{% endalert %}

## Segmenter par abonnements de l’utilisateur {#segmenting-by-user-subscriptions}

Les filtres "Statut de l'abonnement par e-mail" et "Statut de l'abonnement par Push" vous permettent de segmenter vos utilisateurs en fonction de leur statut d'abonnement.

Cela peut être utile si vous souhaitez cibler des utilisateurs qui n'ont ni opté pour l'inclusion ni pour l'exclusion et les encourager à s'abonner explicitement à l'e-mail ou au push. Dans ce cas, vous créerez un segment avec un filtre "L'état de l'abonnement à l'e-mail/push est abonné" et les campagnes destinées à ce segment iront aux utilisateurs qui sont abonnés, mais qui n'ont pas opté pour l'abonnement.

![Statut de l'abonnement à l'e-mail utilisé comme filtre de segmentation.]({% image_buster /assets/img_archive/not_optin.png %})

