---
nav_title: Gestion des abonnements aux utilisateurs
article_title: Gestion des abonnements aux utilisateurs
page_order: 1.9
description: "Cet article de référence couvre les différents états d'abonnement, comment créer et gérer des groupes d'abonnement, et comment segmenter les utilisateurs en fonction de leurs abonnements."
channel:
  - Email
---

# Gestion des abonnements aux utilisateurs

## État global de l'abonnement {#subscription-states}

Braze a trois états d'abonnement global pour les utilisateurs de courriels (listés dans le tableau ci-dessous), qui sont le gardien final entre vos messages et vos utilisateurs. Par exemple, les utilisateurs considérés comme `désabonnés` ne recevront pas de messages ciblant l'état d'abonnement global de `souscrit` ou `opté`.

| État      | Définition                                                                                                                                                                                                      |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Opted in  | L'utilisateur a explicitement confirmé qu'il souhaite recevoir un e-mail. Nous recommandons un processus explicite d'opt-in pour obtenir le consentement des utilisateurs pour envoyer des e-mails.             |
| Inscrit   | L'utilisateur n'a ni désabonné ni explicitement opté pour recevoir des e-mails. Un utilisateur est automatiquement défini comme `abonné` lorsqu'une adresse e-mail valide est ajoutée à son profil utilisateur. |
| Désabonné | L'utilisateur s'est désabonné explicitement de vos e-mails.                                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Ces états globaux d'abonnement sont différents des [groupes d'abonnement](#subscription-groups), qui agissent comme des filtres qui peuvent restreindre votre public des États d'abonnement globaux.
{% endalert %}

## Changement des abonnements {#changing-subscriptions}

{% alert note %}
Braze ne compte pas les changements d'état d'abonnement sur vos points de données, globalement et autour des groupes d'abonnement.
{% endalert %}

### Groupes d'abonnement

Les groupes d'abonnement sont des filtres de segment qui peuvent affiner davantage votre public des [états d'abonnement globaux](#subscription-states) ci-dessus. Vous pouvez ajouter jusqu'à 25 groupes d'abonnement par groupe d'applications. Ces groupes vous permettent de présenter plus d'options d'abonnement granulaires aux utilisateurs finaux.

Par exemple, supposons que vous envoyez plusieurs catégories de campagnes d'email (Promotionnel, Newsletter, Mises à jour de produits). Dans ce cas, vous pouvez utiliser des groupes d'abonnement pour permettre à vos clients de choisir les catégories d'e-mails qu'ils souhaitent s'abonner ou de se désabonner en vrac d'une seule page, en utilisant notre [Centre de Préférence de Courriel](#email-preference-center).

Vous pouvez également utiliser des groupes d'abonnement pour permettre à vos clients de choisir la fréquence à laquelle ils souhaitent recevoir des e-mails de votre part, en créant des groupes d'abonnement pour les courriels quotidiens, hebdomadaires ou mensuels.

Utilisez les [API REST du groupe d'abonnement][25] pour gérer programmatiquement les groupes d'abonnement que vous avez stockés sur le tableau de bord de Braze à la page **Groupe d'abonnement**.

#### Créer un groupe

Pour créer un groupe d'abonnement, allez à la page __Groupes d'abonnement__ , puis cliquez sur **+ Créer un groupe d'abonnement par courriel**. Donnez un nom et une description à votre groupe d'abonnement, puis cliquez sur **Enregistrer**. Tous les groupes d'abonnement sont automatiquement ajoutés à votre centre de préférences.

!\[Create a Subscription Group\]\[26\]{: height="50%" width="50%"}

Lors de la création de vos segments, définissez le nom du groupe comme un filtre. Ceci assurera que les utilisateurs qui ont choisi de rejoindre votre groupe recevront vos emails. Idéal pour recevoir des bulletins mensuels, des coupons, des abonnements et bien plus encore!

!\[Use a Subscription Group\]\[27\]{: style="max-width:80%"}

#### Groupes d'archivage

Les groupes d'abonnement archivés ne peuvent pas être édités et n'apparaîtront plus dans les filtres de segment ou dans votre centre de préférences.  Si vous essayez d'archiver un groupe qui est utilisé comme filtre de segment dans n'importe quel e-mail, campagne, ou Canvas, vous recevrez un message d'erreur qui vous empêchera d'archiver le groupe jusqu'à ce que vous supprimiez toutes les utilisations de celui-ci.

Vous pouvez archiver votre groupe à partir de la page **Groupes d'abonnement**. Trouvez votre groupe dans la liste, puis cliquez sur l'engrenage et sélectionnez **Archiver** dans le menu déroulant.

Braze ne traitera aucun changement d'état pour les utilisateurs des groupes archivés. Par exemple, si vous archivez le "Groupe d'abonnement A" alors que Susie est considérée comme `abonné` à celui-ci, ils resteront "`abonnés`" à ce groupe, même s'ils cliquent sur un lien de désinscription (cela ne devrait pas importe à Susie, le « Groupe d'abonnement A » est archivé et vous ne pouvez pas envoyer de messages en l'utilisant).

#### Exporter les modifications d'état de l'abonnement utilisateur

Vous pouvez exporter les modifications d'état d'abonnement de vos utilisateurs via un fichier CSV. À partir de la page **Centre de préférences** , cliquez sur **Données d'abonnement aux utilisateurs**, puis sélectionnez **CSV Export User Subscription Data** dans le menu déroulant.

!\[Export\]\[29\]

Par défaut, les 30 derniers jours de changements d'état pour tous les groupes d'abonnement sont exportés.

#### Voir les groupes d'abonnement dans l'analyse de campagne

Vous pouvez voir le nombre d'utilisateurs qui ont changé leur état d'abonnement (abonné ou désabonné) à partir d'une campagne d'email spécifique sur la page d'analyse de cette campagne.

À partir de la page **Analyses de campagne** pour votre campagne, faites défiler vers le bas jusqu'à la section **Performance de message d'e-mail** et cliquez sur la flèche sous __Groupes d'abonnement__ pour voir le nombre d'agrégats de changements d'état, tel que soumis par vos clients.

!\[Sub Group Performance\]\[30\]

### Centre de préférence de l'e-mail

Le Centre de Préférence de Courriel est un moyen facile de gérer les utilisateurs qui reçoivent certains groupes de newsletters. Chaque groupe d'abonnement que vous créez est ajouté à la liste Centre de préférences. Cliquez sur le nom du centre de préférences pour voir un aperçu interactif.

Pour placer un lien vers le centre de préférences dans vos e-mails, utilisez la balise Préférence Center Liquid (ci-dessous) et ajoutez-la à l'endroit désiré dans votre e-mail, similaire à la façon dont vous insérez [URL de désinscription](#custom-footer).

{% raw %}
```
{{${preference_center_url}}}
```
{% endraw %}

{% alert note %}
Le Centre de préférences a une case à cocher qui permettra à vos utilisateurs de se désabonner de tous les e-mails.
{% endalert %}

Le Centre de préférences est destiné à être utilisé strictement dans le canal de messagerie lui-même. Les liens du Centre de préférences sont dynamiques, basés sur chaque utilisateur, et ne peuvent pas être hébergés en externe. Vous pouvez cependant créez et hébergez votre propre centre de préférences personnalisé et utilisez les [API REST du groupe d'abonnement][25] pour garder les données en synchronisation avec Braze. Reportez-vous à la section suivante pour en savoir plus.

#### Personnalisez votre centre de préférences

Vous pouvez créer et héberger un centre de préférences HTML entièrement personnalisé et synchroniser avec Braze en utilisant nos [APIs][28].

{% alert note %}
Pour le moment, vous ne pouvez avoir qu'un seul centre de préférences, qui répertorie tous vos groupes d'abonnement actuels.
{% endalert %}

##### Logo

Vous pouvez modifier le logo et l'en-tête de votre centre de préférences. Cliquez sur l'engrenage, puis cliquez sur **Modifier** dans le menu qui apparaît.

### Changement des abonnements aux e-mails {#changing-email-subscriptions}

Dans la plupart des cas, vos utilisateurs géreront leur abonnement par courriel à l'aide de liens d'abonnement qui sont inclus dans les courriels qu'ils reçoivent.

Vous devez insérer un pied de page conforme à la loi avec un lien de désinscription au bas de chaque e-mail que vous envoyez. Lorsque les utilisateurs cliquent sur l'URL de désinscription dans votre pied de page, ils devraient être désabonnés et transférés sur une page d'accueil qui confirme la modification de leur abonnement.

#### Pied de page personnalisé {#custom-footer}

{% raw %}
Braze fournit la possibilité de définir un pied de page d'e-mail personnalisé à l'échelle du groupe d'applications, que vous pouvez modéliser dans chaque e-mail en utilisant l'attribut `{{${email_footer}}}` Liquid.
{% endraw %}

De cette façon, vous n'avez pas à créer un nouveau pied de page pour chaque modèle d'e-mail ou campagne d'email que vous utilisez. Les modifications que vous apportez à votre pied de page personnalisé seront reflétées dans toutes les campagnes de courrier électronique nouvelles et existantes. Rappelez-vous que la conformité avec la [loi CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) vous oblige à inclure une adresse physique pour votre entreprise et un lien de désinscription dans vos e-mails.

{% alert warning %}
Il est de votre responsabilité de vous assurer que votre pied de page personnalisé répond à ces exigences.
{% endalert %}

Pour créer ou modifier votre pied de page personnalisé, allez à la page **Gérer les paramètres** et sélectionnez l'onglet **Paramètres de messagerie**.

!\[Paramètres des e-mails\]\[19\]

Dans la section **Pied de page personnalisé** , vous pouvez choisir d'activer les pieds de page personnalisés. Une fois activé, vous verrez une fenêtre pour éditer votre pied de page et envoyer un message de test.

!\[Pied de page personnalisé\]\[20\]

{% raw %}
Vous verrez le pied de page par défaut, qui utilise l'attribut `{{${set_user_to_unsubscribed_url}}}` et l'adresse de diffusion physique de Braze. Pour se conformer à la réglementation CAN-SPAM, votre pied de page personnalisé doit inclure `{{${set_user_to_unsubscribed_url}}}`. Vous ne pourrez pas enregistrer un pied de page personnalisé sans cet attribut.

Si vous utilisez le pied de page par défaut, qui utilise l'attribut `{{${set_user_to_unsubscribed_url}}}` , assurez-vous de sélectionner **<autre>** pour le **Protocole**, comme indiqué ci-dessous.

!\[Default Unsub URL Protocol\]\[24\]{: style="max-width:50%;"}

!\[Aucun Footer-Email Settings\]\[21\]

> Faites très attention à utiliser un modèle avec le pied de page personnalisé `{{${email_footer}}}` ou `{{${set_user_to_unsubscribed_url}}}`lors de la rédaction d'une campagne d'e-mail. Un avertissement apparaîtra ; cependant, la décision ultime d’envoyer un courriel sans lien de désinscription vous appartient.

!\[No Footer-Campaign Composition\]\[22\]

Lors de la création d'un pied de page personnalisé, Braze vous suggère d'utiliser des attributs pour la personnalisation. Voici quelques exemples que vous pouvez trouver utiles:

| Attribut                                             | Étiquette                             |
| ---------------------------------------------------- | ------------------------------------- |
| Adresse e-mail de l'utilisateur                      | `{{${email_address}}}`                |
| URL de désinscription personnalisée de l'utilisateur | `{{${set_user_to_unsubscribed_url}}}` |
| URL d'opt-in personnalisée de l'utilisateur          | `{{${set_user_to_opted_in_url}}}`     |
| URL d'inscription personnalisée de l'utilisateur     | `{{${set_user_to_subscribed_url}}}`   |
{: .reset-td-br-1 .reset-td-br-2}

Bien sûr, l'ensemble complet des attributs par défaut et personnalisés sont disponibles pour vous. En tant que meilleure pratique, Braze recommande d'inclure à la fois un lien de désinscription (i.e. `{{${set_user_to_unsubscribed_url}}}`) et un lien opt-in (i.e. `{{${set_user_to_opted_in_url}}}`) dans votre pied de page personnalisé. De cette façon, les utilisateurs pourront à la fois se désabonner ou se désinscrire, et vous pourrez collecter passivement des données opt-in pour une partie de vos utilisateurs.

Vous pouvez également choisir de définir un pied de page personnalisé pour les e-mails en texte brut à partir de l'onglet **Paramètres de messagerie** , qui suit les mêmes règles que le pied de page personnalisé pour les courriels HTML. Si vous choisissez de ne pas écrire un pied de page en texte simple, Braze en construira automatiquement un à partir du pied de page HTML. Lorsque vos pieds de page personnalisés sont à votre goût, cliquez sur **Enregistrer** au bas de la page.

!\[Sauvegarder le pied de page personnalisé\]\[23\]{: style="max-width:70%" }

#### Page d'accueil de désinscription personnalisée

Lorsqu'un utilisateur clique sur une URL de désinscription dans un e-mail, ils sont redirigés vers une page de destination par défaut qui confirme la modification de leur abonnement.

En option, vous pouvez fournir du HTML pour votre page de destination personnalisée vers laquelle les utilisateurs seront dirigés (au lieu de la page par défaut) lors de la désinscription. Cette fonctionnalité est disponible sur la page [Paramètres de messagerie][10].

Nous vous recommandons d'inclure un lien de réinscription (i.e. `{{${set_user_to_subscribed_url}}}` ) sur cette page afin que les utilisateurs aient la possibilité de se réabonner en cas de désinscription accidentelle.

!\[Désinscription personnalisée\]\[11\]

{% endraw %}

### Changement des abonnements push {#changing-push-subscriptions}

Les SDK de Braze fournissent des méthodes pour changer l'abonnement aux messages push d'un utilisateur. Veuillez vous référer à la documentation technique de Braze pour votre plateforme mobile pour plus d'informations sur la configuration de ces méthodes :

- [iOS][12]
- [Android et FireOS][13]
- [Univers Windows][14]

### Changement manuel des abonnements des utilisateurs {#manually-changing-subscriptions}

Vous pouvez modifier manuellement le statut d'abonnement de n'importe quel utilisateur dans son profil utilisateur. Vous pouvez trouver des profils utilisateur individuels en recherchant l'ID ou l'adresse e-mail d'un utilisateur sur la page **Recherche d'utilisateur**. Sous l'onglet **Engagement** du profil de l'utilisateur, vous trouverez l'état actuel de l'abonnement push et email d'un utilisateur.

Cliquez sur les boutons **Désabonné**, **Abonné**, ou **Abonné** pour changer le statut d'abonnement de cet utilisateur. Si disponible, le profil de l'utilisateur affiche également un horodatage pour la date de dernière modification de l'abonnement de l'utilisateur.

!\[UI de profil utilisateur\]\[16\]{: style="max-width:60%" }

## Abonnements et campagnes ciblées {#subscriptions-and-campaign-targeting}

Les campagnes avec des messages push ou email sont destinées aux utilisateurs qui sont abonnés ou optés par défaut. Vous pouvez modifier cette préférence de ciblage lors de l'édition d'une campagne en allant à l'étape **Utilisateurs cibles** et en cliquant sur **Options Avancées**.

Braze prend en charge trois états ciblant :

- Utilisateurs qui sont abonnés ou optés (par défaut).
- Seuls les utilisateurs qui sont inscrits.
- Tous les utilisateurs, y compris ceux qui se sont désabonnés.

{% alert important %}
Il est de votre responsabilité de vous conformer à toute [loi anti-spam applicable]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) lors de l'utilisation de ces paramètres de ciblage.
{% endalert %}

!\[Campaign Targeting Subscription UI\]\[17\]

## Segmentation par abonnements aux utilisateurs {#segmenting-by-user-subscriptions}

Les filtres `Statut d'abonnement par e-mail` et `Statut d'abonnement` vous permettent de segmenter vos utilisateurs par leur statut d'abonnement.

Par exemple, ceci peut être utile si vous voulez cibler les utilisateurs qui n'ont pas opté pour ou ne l'ont pas choisi et les encourager à opter explicitement pour l'e-mail ou le push. Dans ce cas, vous créeriez un segment avec un filtre pour "Email/Push Subscription Status is Subscribed" et les campagnes vers ce segment iront aux utilisateurs qui sont abonnés, mais pas choisi.

!\[Filtre d'abonnement\]\[18\]
[11]: {% image_buster /assets/img/custom_unsubscribe.png %} [16]: {% image_buster /assets/img_archive/user-profile-subscription-ui.png %} [17]: {% image_buster /assets/img_archive/campaign-targeting-subscription-ui. ng %} [18]: {% image_buster /assets/img_archive/not_optin.png %} [19]: {% image_buster /assets/img_archive/email_settings. ng %} [20]: {% image_buster /assets/img_archive/custom_footer.png %} [21]: {% image_buster /assets/img_archive/no_unsub_link_warning. ng %} [22]: {% image_buster /assets/img_archive/no_footer_test.png %} [23]: {% image_buster /assets/img_archive/custom_footer_save_changes.png %} [24]: {% image_buster /assets/img_archive/email_unsub_protocol. ng %} [26]: {% image_buster /assets/img/sub_group_create.png %} [27]: {% image_buster /assets/img/sub_group_use. if %} [29]: {% image_buster /assets/img/user-sub-state-export.png %} [30]: {% image_buster /assets/img/campaign_analytics_sub_groups.png %}

[10]: https://dashboard-01.braze.com/app_settings/app_settings/email/ "Email App Settings"
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/#managing-notification-subscription-statuses
[25]: {{site.baseurl}}/developer_guide/rest_api/subscription_group_api/
[28]: {{site.baseurl}}/developer_guide/rest_api/subscription_group_api/
