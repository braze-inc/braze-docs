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

Braze dispose de trois états d’abonnement globaux pour les utilisateurs de courrier électronique (répertoriés dans le tableau suivant), qui sont le contrôleur final entre vos messages et vos utilisateurs. Par exemple, les utilisateurs considérés comme `unsubscribed` ne recevront pas de messages ciblés à l’état d’abonnement global de `subscribed` ou `opted-in`.

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

Si un utilisateur a marqué un ou plusieurs de vos e-mails comme étant des spams, Braze ne lui enverra que des e-mails transactionnels. Dans ce cas, les e-mails transactionnels font référence à l'option sélectionnée **Envoyer à tous les utilisateurs, y compris les utilisateurs désabonnés**, dans l'étape **Audience cible.** 

{% alert tip %}
Consultez nos bonnes pratiques en matière de [réchauffement d'adresses IP]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming/) pour savoir comment réengager efficacement vos utilisateurs.
{% endalert %}

### Adresses e-mails non valides et messages non délivrés

{% multi_lang_include metrics.md metric='Hard Bounce' %} {% multi_lang_include metrics.md metric='Soft Bounce' %} 

Si l’utilisateur change son adresse e-mail, nous recommencerons à lui envoyer des e-mails puisque sa nouvelle adresse sera sans doute valide. Les « soft bounces » sont automatiquement réessayés pendant 72 heures.

### Mettre à jour les états d’abonnement aux e-mails

Il existe quatre façons de mettre à jour l'état de l'abonnement à l'e-mail d'un utilisateur :

#### Intégration SDK

Utilisez le SDK de Braze pour mettre à jour le statut d’abonnement d’un utilisateur.

#### API REST

Utilisez l'[endpoint `/users/track`][users-track] pour mettre à jour l'attribut [`email_subscribe`][user_attributes_object] d'un utilisateur donné.

#### Profil utilisateur

1. Trouvez l'utilisateur par le biais de la **recherche d'utilisateurs**. 
2. Sous l'onglet **Engagement**, cliquez sur les boutons **Désabonné**, **Abonné** ou **Ouvert pour** modifier le statut d'abonnement de cet utilisateur. 

Si disponible, le profil utilisateur affiche également un horodatage de la dernière modification de l’abonnement de l’utilisateur.

#### Centre de préférences

Le code Liquid du [centre de préférences](#email-preference-center) peut être inclus au bas de vos e-mails, ce qui permet aux utilisateurs de s’abonner ou de se désabonner des e-mails. Braze gère les mises à jour du statut d’abonnement depuis le centre de préférences.

### Vérification de l’état de l’abonnement aux e-mails

![Profil utilisateur de John Doe avec son état d'abonnement aux e-mails défini sur Abonné.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l'état de l'abonnement aux e-mails d'un utilisateur avec Braze :

1. **Exportation de l'API REST :** Utilisez les endpoints [Exporter les utilisateurs par segment][segment] ] ou [Exporter les utilisateurs par identifiant][identifiant] ] pour exporter des profils utilisateurs individuels au format JSON.
2. **Profil utilisateur :** Recherchez le profil de l'utilisateur sur la page [Recherche d'utilisateurs][5] ], puis sélectionnez l'onglet **Engagement** pour afficher et mettre à jour manuellement l'état de l'abonnement d'un utilisateur.

Lorsqu'un utilisateur met à jour son adresse e-mail, l'état de son abonnement devient abonné, sauf si l'adresse e-mail mise à jour existe déjà ailleurs dans un espace de travail de Braze. Vous pouvez exporter des profils utilisateurs individuels au format JSON en utilisant les endpoints [Exporter les utilisateurs par segment][segment] ] ou [Exporter les utilisateurs par identifiant][identifiant] ].

## Groupes d’abonnement

Les groupes d'abonnement sont des filtres de segmentation qui permettent de restreindre davantage votre audience à partir des [états d'abonnement globaux](#subscription-states). Vous pouvez ajouter jusqu'à 350 groupes d'abonnement par espace de travail. Ces groupes vous permettent de présenter des options d’abonnement plus granulaires aux utilisateurs finaux.

Supposons par exemple que vous envoyiez plusieurs catégories de campagnes d'e-mail (promotionnelles, bulletins d'information ou mises à jour de produits). Dans ce cas, vous pouvez utiliser les groupes d'abonnement pour permettre à vos clients de choisir les catégories d'e-mails auxquelles ils souhaitent s'abonner ou se désabonner en masse à partir d'une seule page, en utilisant un [centre de préférences pour les e-mails.](#email-preference-center) Vous pouvez également utiliser des groupes d’abonnement pour permettre à vos clients de choisir la fréquence à laquelle ils souhaitent recevoir des e-mails de votre part, en créant des groupes d’abonnement pour les e-mails quotidiens, hebdomadaires ou mensuels.

Utilisez les [endpoints du groupe d'abonnement][25] pour gérer de manière programmatique les groupes d'abonnement que vous avez enregistrés sur le tableau de bord de Braze vers la page **Groupe d'abonnement**.

### Création d'un groupe d'abonnement

1. Allez dans **Audience** > **Abonnements**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), cette page se trouve sous **Utilisateurs** > **Groupes d'abonnement**.
{% endalert %}

{: start="2"}
2\. Sélectionnez **\+ Créer un groupe d'abonnement e-mail**.
3\. Donnez un nom et une description à votre groupe d'abonnement, puis cliquez sur **Enregistrer.** 

Tous les groupes d’abonnement sont automatiquement ajoutés à votre centre de préférences.

![Champs pour créer un groupe d'abonnement.][26]{: height="50%" width="50%"}

### Segmentation à l'aide d'un groupe d'abonnement

Lors de la création de vos segments, définissez le nom du groupe d’abonnement comme filtre. Cela confirmera que les utilisateurs qui ont opté pour votre groupe recevront vos e-mails. C’est très pratique pour les bulletins d’information mensuels, les bons de réduction, les niveaux d’adhésion et bien plus encore.

![GIF d'un utilisateur définissant un nom de groupe d'abonnement comme filtre.][27]{: style="max-width:80%"}

### Archivage des groupes d'abonnement

Les groupes d’abonnement archivés ne peuvent pas être modifiés et n’apparaîtront plus dans les filtres de segments ou dans votre centre de préférences. Si vous tentez d’archiver un groupe utilisé comme filtre de segment dans un e-mail, une campagne ou Canvas, vous recevrez un message d’erreur qui vous empêchera d’archiver le groupe jusqu’à ce que vous supprimiez toutes les utilisations de celui-ci.

Vous pouvez archiver votre groupe à partir de la page **Groupes d'abonnement**. Trouvez votre groupe dans la liste, puis cliquez sur l’engrenage et sélectionnez **Archiver** dans le menu déroulant.

Braze ne traitera aucun changement d’état pour les utilisateurs des groupes archivés. Par exemple, si vous archivez le « Groupe d’abonnement A », alors que Susie est considérée comme `subscribed`, elle restera « `subscribed` » à ce groupe, même si elle clique sur un lien de désabonnement (cela ne devrait pas intéresser Susie, car le « Groupe d’abonnement A » est archivé et vous ne pouvez envoyer aucun message avec celui-ci).

#### Affichage de la taille des groupes d'abonnement

Vous pouvez consulter le graphique **Série temporelle des groupes d’abonnement** dans la page **Groupes d'abonnement** pour voir la taille du groupe d'abonnement en fonction du nombre d'utilisateurs sur une période donnée. Ces tailles de groupes d'abonnement sont également cohérentes avec d'autres aspects de Braze, tels que le calcul de la taille des segments.

![][10]

#### Visualisation des groupes d'abonnement dans l'analyse/analytique des campagnes

Vous pouvez voir le nombre d’utilisateurs qui ont modifié leur état d’abonnement (abonnement ou désabonnement) à partir d’une campagne d’e-mail spécifique sur la page d’analyse de cette campagne.

Sur la page **Analyse/analytique de** votre campagne, descendez jusqu'à la section **Performances des messages électroniques** et cliquez sur la flèche située sous **Groupes d'abonnement** pour afficher le décompte global des changements d'état, tels qu'ils ont été soumis par vos clients.

![][30]

## Centre de préférence des e-mails

Le centre de préférences e-mail est un moyen facile de gérer les utilisateurs qui reçoivent certains groupes de bulletins d'information. Il se trouve dans le tableau de bord sous **Groupes d'abonnement**. Chaque groupe d’abonnement que vous créez est ajouté à la liste du centre de préférences. Pour en savoir plus sur la manière d'ajouter ou de personnaliser un centre de préférences, reportez-vous à [Centre de préférences.]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/)

## Modifier des abonnements aux e-mails {#changing-email-subscriptions}

Dans la plupart des cas, vos utilisateurs gèrent leur abonnement aux e-mails via des liens d’abonnement inclus dans les e-mails qu’ils reçoivent. Vous devez insérer un pied de page légalement conforme avec un lien de désabonnement au bas de chaque e-mail que vous envoyez. Lorsque les utilisateurs cliquent sur l'URL de désabonnement dans votre pied de page, ils doivent être désabonnés et renvoyés vers une page de renvoi qui confirme la modification de leur abonnement. Nous vous recommandons d'inclure cette étiquette Liquid : {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}.

Notez que lorsqu'un utilisateur sélectionne "Se désabonner de tous les types d'e-mails ci-dessus" dans le centre de préférences e-mail, son statut d'abonnement global à l'e-mail est mis à jour à `unsubscribed` et il est désabonné de tous les groupes d'abonnement.

### Création de pieds de page personnalisés {#custom-footer}

Si vous ne souhaitez pas utiliser le pied de page par défaut de Braze dans vos e-mails, vous pouvez créer un pied de page personnalisé pour l'ensemble de votre espace de travail, que vous pouvez intégrer dans chaque e-mail à l'aide de l'attribut Liquid de {% raw %}`{{${email_footer}}}`{% endraw %}.

De cette façon, vous n’avez pas à créer un nouveau pied de page pour chaque modèle de courriel ou de campagne par e-mail que vous utilisez. Pour connaître la marche à suivre, reportez-vous à la section [Pied de page personnalisé de l'e-mail.]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/)

#### Gestion des abonnements pour les adresses IP chinoises

Si vous prévoyez que les destinataires de vos e-mails auront une adresse IP chinoise, vous ne devez pas compter uniquement sur un lien de désabonnement dans votre e-mail pour maintenir vos listes `unsubscribed`. Au lieu de cela, proposez aux utilisateurs d'autres moyens de se désabonner facilement, comme l'ouverture d'un ticket d'assistance sur votre portail d'assistance ou l'envoi d'un e-mail à un conseiller clientèle. 

### Créer une page de désabonnement personnalisée

Lorsque les utilisateurs cliquent sur une URL de désabonnement dans un e-mail, ils sont dirigés vers une page de destination par défaut qui confirme la modification de leur abonnement.

Pour créer une page de renvoi personnalisée vers laquelle les utilisateurs seront dirigés (au lieu de la page par défaut) lorsqu'ils s'abonneront, allez dans **Préférences e-mail** > **Pages et pieds de page d'abonnement** et indiquez le code HTML de votre page de renvoi personnalisée. Nous vous recommandons d'inclure un lien de réinscription (tel que {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}) sur la page de renvoi afin que les utilisateurs aient la possibilité de se réinscrire au cas où ils se seraient désinscrits par accident.

![E-mail de désabonnement personnalisé dans le panneau Page de désabonnement personnalisée.][11]

### Créer une page d'abonnement personnalisée

Au lieu d’abonner immédiatement un utilisateur à vos campagnes par e-mail, la création d’une page d’abonnement personnalisée peut donner à vos utilisateurs la possibilité de reconnaître et de contrôler leurs préférences de notification. Cette communication supplémentaire peut également aider vos campagnes par e-mail à ne pas atterrir dans les courriers indésirables, car vos utilisateurs auront choisi de s’inscrire. 

Allez dans **Préférences e-mail** > **Pages et pieds de page d'abonnement**, et personnalisez le style dans la section **Page d'abonnement personnalisée** pour voir comment cela indique à vos utilisateurs qu'ils ont été abonnés.

{% alert tip %}
Braze recommande d’utiliser un processus d’abonnement double pour vous aider à diffuser vos e-mails. Ce processus envoie un e-mail de confirmation supplémentaire dans lequel l'utilisateur confirme à nouveau ses préférences en matière de notification au moyen d'un lien figurant dans l'e-mail. À ce stade, l'utilisateur est considéré comme ayant donné son accord.
{% endalert %}

## Abonnements et ciblage des campagnes {#subscriptions-and-campaign-targeting}

Les campagnes avec des notifications push ou des e-mails ciblent les utilisateurs qui sont inscrits ou abonnés par défaut. Vous pouvez modifier cette préférence de ciblage lorsque vous modifiez une campagne en accédant à l'étape **Audience cible** et en cliquant sur le menu déroulant situé à côté de **Envoyer à ces utilisateurs :.**

Braze prend en charge trois états de ciblage :

- Les utilisateurs qui sont inscrits ou abonnés (par défaut).
- Uniquement les utilisateurs qui sont abonnés.
- Tous les utilisateurs, y compris ceux qui se sont désabonnés.

{% alert important %}
Il est de votre responsabilité de vous conformer aux [lois applicables en matière de spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) lorsque vous utilisez ces paramètres de ciblage.
{% endalert %}

![Exemple de ciblage d'audience pour les utilisateurs abonnés ou ayant opté pour la section Options de ciblage de l'étape Cibler l'audience.][17]

## Segmenter par abonnements de l’utilisateur {#segmenting-by-user-subscriptions}

Les filtres `Email Subscription Status` et `Push Subscription Status` vous permettent de segmenter vos utilisateurs par leur statut d’abonnement.

Cela peut être utile si vous souhaitez cibler les utilisateurs qui n’ont ni accepté ni refusé l’abonnement et les encouragez à s’abonner explicitement aux e-mails et aux notifications push. Dans ce cas, vous créerez un segment avec un filtre "L'état de l'abonnement à l'e-mail/push est abonné" et les campagnes destinées à ce segment iront aux utilisateurs qui sont abonnés, mais qui n'ont pas opté pour l'abonnement.

![Statut d’abonnement aux e-mails utilisé comme filtre de segment.][18]

[10]: {% image_buster /assets/img_archive/subscription_group_graph.png %}
[11]: {% image_buster /assets/img/custom_unsubscribe.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[16]: {% image_buster /assets/img_archive/user-profile-subscription-ui.png %}
[17]: {% image_buster /assets/img_archive/campaign-targeting-subscription-ui.png %}
[18]: {% image_buster /assets/img_archive/not_optin.png %}
[19]: {% image_buster /assets/img_archive/email_settings.png %}
[25]: {{site.baseurl}}/api/endpoints/subscription_groups
[26]: {% image_buster /assets/img/sub_group_create.png %}
[27]: {% image_buster /assets/img/sub_group_use.gif %}
[28]: {{site.baseurl}}/api/endpoints/preference_center/
[29]: {% image_buster /assets/img/user-sub-state-export.png %}
[30]: {% image_buster /assets/img/campaign_analytics_sub_groups.png %}
[users-track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[3]: {% image_buster /assets/img/push_example.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[identifiant] : {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segmentation] : {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/
