---
nav_title: Abonnements e-mail
article_title: Abonnements utilisateur
page_order: 4
description: "Le présent article de référence couvre les différents états d’abonnement des utilisateurs, la création et la gestion des groupes d’abonnement, et la façon de segmenter les utilisateurs en fonction de leurs abonnements."
channel:
  - e-mail

---

# Abonnements e-mail

## Statuts d’abonnement {#subscription-states}

Braze dispose de trois états d’abonnement globaux pour les utilisateurs de courrier électronique (répertoriés dans le tableau suivant), qui sont le contrôleur final entre vos messages et vos utilisateurs. Par exemple, les utilisateurs considérés comme `unsubscribed` ne recevront pas de messages ciblés à l’état d’abonnement global de `subscribed` ou `opted-in`.

| État | Définition |
| ----- | ---------- |
| Abonné | L’utilisateur a explicitement confirmé qu’il souhaitait recevoir un e-mail. Nous recommandons un processus explicite d’abonnement pour obtenir le consentement des utilisateurs à l’envoi d’e-mails. |
| Abonné | L’utilisateur ne s’est pas désabonné et n’a pas accepté explicitement de recevoir des e-mails. Il s’agit de l’état d’abonnement par défaut lorsqu’un profil utilisateur est créé. |
| Non inscrit | L’utilisateur s’est explicitement désabonné de vos courriels. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Braze ne compte pas les changements d’état d’abonnement par rapport à vos points de données, globalement, et autour des groupes d’abonnement.
{% endalert %}

### Mettre à jour les états d’abonnement aux e-mails

Il existe trois manières de mettre à jour le statut d’abonnement aux e-mail d’un utilisateur :

1. **Intégration SDK**<br>Utilisez le SDK de Braze pour mettre à jour le statut d’abonnement d’un utilisateur.<br><br>
2. **API REST**<br>Utilisez l’[endpoint `/users/track`][users-track] pour mettre à jour l’attribut [`email_subscribe`][user_attributes_object] pour un utilisateur donné.<br><br>
3. **Profil utilisateur**<br>Pour modifier manuellement le statut de l’abonnement, recherchez d’abord l’utilisateur via **User Search (Recherche d’utilisateur)**. Cliquez ensuite dans l’onglet **Engagement**, sur les boutons **Unsubscribed (Désabonné)**, **Subscribed (Abonné)** ou **Opted In (Abonné)** pour modifier le statut de l’abonnement de cet utilisateur. Si disponible, le profil utilisateur affiche également un horodatage de la dernière modification de l’abonnement de l’utilisateur.<br><br>
4. **Centre de préférences**<br>[Centre de préférences](#email-preference-center) Liquid peut être inclus au bas de vos e-mails, ce qui permet aux utilisateurs de s’abonner ou de se désabonner des e-mails. Braze gère les mises à jour du statut d’abonnement depuis le centre de préférences.

### Vérification de l’état de l’abonnement aux e-mails

![Profil utilisateur de John Doe avec son état d’abonnement aux notifications push défini sur Abonné.][3]{: style="float:right;max-width:35%;margin-left:15px;"}

Il existe deux façons de vérifier l’état de l’abonnement aux notifications push d’un utilisateur avec Braze :

1. **Profil utilisateur :** Vous pouvez accéder aux profils utilisateur individuels via le tableau de bord de Braze sur la page **[User Search (Recherche utilisateur)][5]**. Après avoir trouvé un profil utilisateur (par adresse e-mail, numéro de téléphone ou ID d’utilisateur externe), vous pouvez sélectionner l’onglet **Engagement** pour afficher et ajuster manuellement l’état d’abonnement de l’utilisateur. 
<br><br>
2. **Rest API Export (Exportation d’API Rest)** : Vous pouvez exporter des profils utilisateur individuels au format JSON en utilisant les endpoints d’exportation [Users by segment (Utilisateurs par segment)][segment] ou [Users by identifier (Utilisateurs par identifiant)][identifier]. 

<br><br>
## Groupes d’abonnement

Les groupes d’abonnement sont des filtres de segments qui peuvent affiner davantage votre audience depuis les [états d’abonnement globaux](#subscription-states). Vous pouvez ajouter jusqu’à 100 groupes d’abonnement par groupe d’apps. Ces groupes vous permettent de présenter des options d’abonnement plus granulaires aux utilisateurs finaux.

Par exemple, supposons que vous envoyez plusieurs catégories de campagnes par e-mail (promotion, newsletter, mises à jour de produits). Dans ce cas, vous pouvez utiliser des groupes d’abonnement pour permettre à vos clients de choisir les catégories de courriels auxquelles ils souhaitent s’abonner ou se désabonner en masse à partir d'une seule page, en utilisant notre [centre de préférences e-mail](#email-preference-center). 

Vous pouvez également utiliser des groupes d’abonnement pour permettre à vos clients de choisir la fréquence à laquelle ils souhaitent recevoir des e-mails de votre part, en créant des groupes d’abonnement pour les e-mails quotidiens, hebdomadaires ou mensuels.

Utilisez les [API REST du groupe d’abonnement][25] pour gérer par programmation les groupes d’abonnement que vous avez stockés sur le tableau de bord de Braze sur la page **Subscription Group (Groupe d’abonnement)**.

### Créer un groupe

Pour créer un groupe d’abonnement, allez sur la page **Groupes d’abonnement**, puis cliquez sur **+ Create Email Subscription Group (+ Créer un groupe d’abonnement par e-mail)**. Donnez un nom et une description à votre groupe d’abonnement, puis cliquez sur **Save (Enregistrer)**. Tous les groupes d’abonnement sont automatiquement ajoutés à votre centre de préférences.

![Champs pour créer un groupe d’abonnement.][26]{: height="50%" width="50%"}

Lors de la création de vos segments, définissez le nom du groupe d’abonnement comme filtre. Cela garantira que les utilisateurs qui se sont abonnés à votre groupe recevront vos e-mails. C’est très pratique pour les bulletins d’information mensuels, les bons de réduction, les niveaux d’adhésion et bien plus encore.

![GIF d’un utilisateur définissant un nom de groupe d’abonnement comme filtre.][27]{: style="max-width:80%"}

### Groupes d’archivage

Les groupes d’abonnement archivés ne peuvent pas être modifiés et n’apparaîtront plus dans les filtres de segments ou dans votre centre de préférences.  Si vous tentez d’archiver un groupe utilisé comme filtre de segment dans un e-mail, une campagne ou Canvas, vous recevrez un message d’erreur qui vous empêchera d’archiver le groupe jusqu’à ce que vous supprimiez toutes les utilisations de celui-ci.

Vous pouvez archiver votre groupe à partir de la page **Subscription Groups (Groupes d’abonnement)**. Trouvez votre groupe dans la liste, puis cliquez sur l’engrenage et sélectionnez **Archive (Archiver)** dans le menu déroulant.

Braze ne traitera aucun changement d’état pour les utilisateurs des groupes archivés. Par exemple, si vous archivez le « Groupe d’abonnement A », alors que Susie est considérée comme `subscribed`, elle restera « `subscribed` » à ce groupe, même si elle clique sur un lien de désabonnement (cela ne devrait pas intéresser Susie, le « Groupe d’abonnement A » est archivé et vous ne pouvez envoyer aucun message avec).

#### Voir les groupes d’abonnement dans l’analyse de campagne

Vous pouvez voir le nombre d’utilisateurs qui ont modifié leur état d’abonnement (abonnement ou désabonnement) à partir d’une campagne d’e-mail spécifique sur la page d’analyse de cette campagne.

Sur la page **Campaign Analytics (Analyse de campagne)** de votre campagne, faites défiler vers le bas jusqu’à la section **Email Message Performance (Performances de l’e-mail)** et cliquez sur la flèche sous **Subscription Groups (Groupes d’abonnement)** pour voir le nombre total de changements d’état, tel que soumis par vos clients.

![][30]

## Centre de préférence des e-mails

Le centre de préférences des e-mails est un moyen facile de gérer les utilisateurs qui reçoivent certains groupes de bulletins d’information et qui se trouvent dans le tableau de bord sous **Subscription Groups (Groupes d’abonnement)**. Chaque groupe d’abonnement que vous créez est ajouté à la liste du centre de préférences. Pour en apprendre plus sur la manière dont ajouter ou personnaliser un centre de préférence, référez-vous au [Centre de préférence]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/).

## Modifier des abonnements aux e-mails {#changing-email-subscriptions}

Dans la plupart des cas, vos utilisateurs gèrent leur abonnement aux e-mails via des liens d’abonnement inclus dans les e-mails qu’ils reçoivent. Vous devez insérer un pied de page légalement conforme avec un lien de désabonnement au bas de chaque e-mail que vous envoyez. Lorsque les utilisateurs cliquent sur l’URL de désabonnement dans votre pied de page, ils doivent être désabonnés et amenés à une page d’accueil qui confirme la modification de leur abonnement.

### Pieds de page personnalisé {#custom-footer}

{% raw %}
Braze offre la possibilité de définir un pied de page d’e-mail personnalisé à l’échelle du groupe d’apps que vous pouvez modéliser dans chaque e-mail à l’aide de l’attribut Liquid ``{{${email_footer}}}``.
{% endraw %}

De cette façon, vous n’avez pas à créer un nouveau pied de page pour chaque modèle de courriel ou de campagne par e-mail que vous utilisez. Les modifications apportées à votre pied de page personnalisé seront reflétées dans toutes les campagnes par e-mail existantes et nouvelles. Rappelez-vous que la conformité avec la [Loi CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) exige que vous incluiez une adresse physique pour votre entreprise et un lien de désabonnement dans vos e-mails. 

{% alert warning %}
Il est de votre responsabilité de vous assurer que votre pied de page personnalisé répond à ces exigences.
{% endalert %}

Pour créer ou modifier votre pied de page personnalisé, allez sur **Manage Settings (Gérer les paramètres)** et sélectionnez l’onglet **Email Settings (Paramètres des e-mails)**.

![][19]

Dans la section **Custom Footer (Pied de page personnalisé)**, vous pouvez choisir d’activer les pieds de page personnalisés. Une fois activés, une fenêtre s’affiche pour modifier votre pied de page et envoyer un message de test.

![][20]

{% raw %}
Vous verrez le pied de page par défaut qui utilise l’attribut ``{{${set_user_to_unsubscribed_url}}}`` et l’adresse physique de Braze. Pour respecter les réglementations CAN-SPAM, votre pied de page personnalisé doit inclure ``{{${set_user_to_unsubscribed_url}}}``. Vous ne pourrez pas enregistrer un pied de page personnalisé sans cet attribut.

Si vous utilisez le pied de page par défaut qui utilise l’attribut ``{{${set_user_to_unsubscribed_url}}}``, assurez-vous de sélectionner **&#60;other (autres)&#62;** pour le **Protocole**.

![Valeurs de protocole et d’URL requises pour le pied de page personnalisé.][24]{: style="max-width:50%;"}

![Exemple de courriel composé sans pied de page.][21]

> Veiller à utiliser un modèle avec le pied de page personnalisé ``{{${email_footer}}}`` ou ``{{${set_user_to_unsubscribed_url}}}``lors de la composition d’une campagne par e-mail. Un avertissement apparaîtra, mais vous pourrez choisir d’envoyer un e-mail avec ou sans lien de désabonnement.

![Composition de campagne sans pied de page.][22]

Lorsque vous créez un pied de page personnalisé, Braze suggère d’utiliser des attributs pour la personnalisation. L’ensemble complet des attributs personnalisés et par défaut est disponible, mais en voici quelques-uns que vous pourriez trouver utiles :

| Attribut | Balise |
| --------- | --- |
| Adresse e-mail de l’utilisateur | `{{${email_address}}}` |
| URL personnalisée de désabonnement de l’utilisateur | `{{${set_user_to_unsubscribed_url}}}` |
| URL personnalisée d’abonnement de l’utilisateur | `{{${set_user_to_opted_in_url}}}` |
| URL personnalisée d’abonnement de l’utilisateur | `{{${set_user_to_subscribed_url}}}` |
{: .reset-td-br-1 .reset-td-br-2}

En tant que meilleure pratique, Braze recommande d’avoir un lien de désabonnement (par ex. ``{{${set_user_to_unsubscribed_url}}}``) et un lien d’abonnement (par ex. ``{{${set_user_to_opted_in_url}}}``) dans votre pied de page personnalisé. De cette façon, les utilisateurs pourront s’abonner ou se désabonner, et vous pourrez collecter de façon passive les données d’abonnement pour une partie de vos utilisateurs.

Vous pouvez également choisir de définir un pied de page personnalisé pour les e-mails en texte brut dans l’onglet **Email Settings (Paramètres des e-mails)** qui suit les mêmes règles que le pied de page personnalisé pour les e-mails HTML. Si vous n’ajoutez pas de pied de page en texte brut, Braze en créera automatiquement un à partir du pied de page HTML. Lorsque vos pieds de page personnalisés vous conviennent, cliquez sur **Save (Enregistrer)** au bas de la page.

![E-mail avec l’option Définir le pied de page personnalisé en texte brut sélectionnée.][23]{: style="max-width:70%" }

### Page de désabonnement personnalisée

Lorsqu’un utilisateur clique sur une URL de désabonnement dans un e-mail, il est dirigé vers une page d’accueil par défaut qui confirme la modification de son abonnement.

Vous pouvez éventuellement fournir le code HTML de votre page d’accueil personnalisée vers laquelle les utilisateurs seront dirigés (au lieu de la page par défaut) lorsqu’ils se désinscrivent dans l’onglet **Subscription Pages and Footers (Pages et pieds de page d’abonnement)** de la page **Email Settings (Paramètres des e-mail)**. Nous vous recommandons d’inclure un lien de réabonnement (par ex. `{{${set_user_to_subscribed_url}}}` ) sur cette page afin que les utilisateurs puissent se réabonner au cas où ils seraient désabonnés par accident.

![E-mail de désabonnement personnalisé dans le panneau Page de désabonnement personnalisée.][11]

{% endraw %}

### Page d’abonnement personnalisée

Au lieu d’abonner immédiatement un utilisateur à vos campagnes par e-mail, la création d’une page d’abonnement personnalisée peut donner à vos utilisateurs la possibilité de reconnaître et de contrôler leurs préférences de notification. Cette communication supplémentaire peut également aider vos campagnes par e-mail à ne pas atterrir dans les courriers indésirables, car vos utilisateurs auront choisi de s’inscrire. Allez dans **Manage Settings > Email Settings > Subscription Pages and Footers (Gérer les paramètres > Paramètres d’e-mail > Pages et pieds de page d’abonnement)** et personnalisez le style dans la section **Custom Opt-In Page (Page d’abonnement personnalisée)** pour voir comment cela indique à vos utilisateurs qu’ils ont été abonnés.

{% alert tip %}
Braze recommande d’utiliser un processus d’abonnement double pour vous aider à diffuser vos e-mails. Ce processus implique l’envoi d’un e-mail de confirmation supplémentaire dans lequel un utilisateur confirmerait à nouveau ses préférences de notification via un lien dans l’e-mail. À ce stade, l’utilisateur serait considéré comme étant abonné.
{% endalert %}

## Abonnements et ciblage des campagnes {#subscriptions-and-campaign-targeting}

Les campagnes avec des notifications push ou des e-mails ciblent les utilisateurs qui sont inscrits ou abonnés par défaut. Vous pouvez modifier cette préférence de ciblage lors de la modification d’une campagne en allant à l’étape **Target Users (Utilisateurs cibles)** et en cliquant sur **Options avancées**.

Braze prend en charge trois états de ciblage :

- Les utilisateurs qui sont inscrits ou abonnés (par défaut).
- Uniquement les utilisateurs qui sont abonnés.
- Tous les utilisateurs, y compris ceux qui se sont désabonnés.

{% alert important %}
Il est de votre responsabilité de vous conformer aux [lois anti-spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) lorsque vous utilisez ces paramètres de ciblage.
{% endalert %}

![Exemple de ciblage d’audience pour des utilisateurs qui sont inscrits ou abonnés aux options avancées de l’étape Utilisateurs cibles.][17]

## Segmenter par abonnements de l’utilisateur {#segmenting-by-user-subscriptions}

Les filtres `Email Subscription Status` et `Push Subscription Status` vous permettent de segmenter vos utilisateurs par leur statut d’abonnement.

Cela peut être utile si vous souhaitez cibler les utilisateurs qui n’ont ni accepté ni refusé l’abonnement et les encouragez à s’abonner explicitement aux e-mails et aux notifications push. Dans ce cas, vous créerez un segment avec un filtre pour « L’état d’abonnement aux e-mails/notifications push est Abonné » et les campagnes de ce segment seront envoyées aux utilisateurs abonnés, mais pas à ceux qui n’ont pas confirmé.

![Statut d’abonnement aux e-mails utilisé comme filtre de segment.][18]

[11]: {% image_buster /assets/img/custom_unsubscribe.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[16]: {% image_buster /assets/img_archive/user-profile-subscription-ui.png %}
[17]: {% image_buster /assets/img_archive/campaign-targeting-subscription-ui.png %}
[18]: {% image_buster /assets/img_archive/not_optin.png %}
[19]: {% image_buster /assets/img_archive/email_settings.png %}
[20]: {% image_buster /assets/img_archive/custom_footer.png %}
[21]: {% image_buster /assets/img_archive/no_unsub_link_warning.png %}
[22]: {% image_buster /assets/img_archive/no_footer_test.png %}
[23]: {% image_buster /assets/img_archive/custom_footer_save_changes.png %}
[24]: {% image_buster /assets/img_archive/email_unsub_protocol.png %}
[25]: {{site.baseurl}}/developer_guide/rest_api/subscription_group_api/
[26]: {% image_buster /assets/img/sub_group_create.png %}
[27]: {% image_buster /assets/img/sub_group_use.gif %}
[28]: {{site.baseurl}}/api/endpoints/preference_center/
[29]: {% image_buster /assets/img/user-sub-state-export.png %}
[30]: {% image_buster /assets/img/campaign_analytics_sub_groups.png %}
[users-track]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[user_attributes_object]: {{site.baseurl}}/api/objects_filters/user_attributes_object
[3]: {% image_buster /assets/img/push_example.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/
[identifier]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[segment]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/