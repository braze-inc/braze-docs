---
nav_title: Abonnements utilisateur
article_title: Abonnements utilisateur
page_order: 4
description: "Le présent article de référence couvre les différents états d’abonnement des utilisateurs, la création et la gestion des groupes d’abonnement, et la façon de segmenter les utilisateurs en fonction de leurs abonnements."
channel:
  - E-mail

---

# Gérer les abonnements des utilisateurs

## États d’abonnement globaux {#subscription-states}

Braze dispose de trois états d’abonnement globaux pour les utilisateurs de courrier électronique (répertoriés dans le tableau suivant), qui sont le contrôleur final entre vos messages et vos utilisateurs. Par exemple, les utilisateurs considérés comme `unsubscribed` ne recevront pas de messages ciblés à l’état d’abonnement global de `subscribed` ou `opted-in`.

| État | Définition |
| ----- | ---------- |
| Abonné | L’utilisateur a explicitement confirmé qu’il souhaitait recevoir un e-mail. Nous recommandons un processus explicite d’abonnement pour obtenir le consentement des utilisateurs à l’envoi d’e-mails. |
| Abonné | L’utilisateur ne s’est pas désabonné et n’a pas accepté explicitement de recevoir des e-mails. Il s’agit de l’état d’abonnement par défaut lorsqu’un profil utilisateur est créé. |
| Non inscrit | L’utilisateur s’est explicitement désabonné de vos courriels. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Ces états d’abonnement globaux sont différents des [groupes d’abonnement](#subscription-groups), qui agissent comme des filtres qui peuvent affiner davantage votre audience des états d’abonnement globaux.
{% endalert %}

## Modification des abonnements {#changing-subscriptions}

{% alert note %}
Braze ne compte pas les changements d’état d’abonnement par rapport à vos points de données, globalement, et autour des groupes d’abonnement.
{% endalert %}

### Groupes d’abonnement

Les groupes d’abonnement sont des filtres de segments qui peuvent affiner davantage votre audience des [états d’abonnement globaux](#subscription-states). Vous pouvez ajouter jusqu’à 100 groupes d’abonnement par groupe d’apps. Ces groupes vous permettent de présenter des options d’abonnement plus granulaires aux utilisateurs finaux.

Par exemple, supposons que vous envoyez plusieurs catégories de campagnes par e-mail (promotion, newsletter, mises à jour de produits). Dans ce cas, vous pouvez utiliser des groupes d’abonnement pour permettre à vos clients de choisir les catégories de courriels auxquelles ils souhaitent s’abonner ou se désabonner en masse à partir d'une seule page, en utilisant notre [centre de préférences e-mail](#email-preference-center). 

Vous pouvez également utiliser des groupes d’abonnement pour permettre à vos clients de choisir la fréquence à laquelle ils souhaitent recevoir des e-mails de votre part, en créant des groupes d’abonnement pour les e-mails quotidiens, hebdomadaires ou mensuels.

Utilisez les [API REST du groupe d’abonnement][25] pour gérer par programmation les groupes d’abonnement que vous avez stockés sur le tableau de bord de Braze sur la page **Groupe d’abonnement**.

#### Créer un groupe

Pour créer un groupe d’abonnement, allez sur la page **Groupes d’abonnement**, puis cliquez sur **+ Créer un groupe d’abonnement par e-mail**. Donnez un nom et une description à votre groupe d’abonnement, puis cliquez sur **Enregistrer**. Tous les groupes d’abonnement sont automatiquement ajoutés à votre centre de préférences.

![Champs pour créer un groupe d’abonnement.][26]{: height="50%" width="50%"}

Lors de la création de vos segments, définissez le nom du groupe d’abonnement comme filtre. Cela garantira que les utilisateurs qui se sont abonnés à votre groupe recevront vos e-mails. C’est très pratique pour les bulletins d’information mensuels, les bons de réduction, les niveaux d’adhésion et bien plus encore !

![GIF d’un utilisateur définissant un nom de groupe d’abonnement comme filtre.][27]{: style="max-width:80%"}

#### Groupes d’archivage

Les groupes d’abonnement archivés ne peuvent pas être modifiés et n’apparaîtront plus dans les filtres de segments ou dans votre centre de préférences.  Si vous tentez d’archiver un groupe utilisé comme filtre de segment dans un e-mail, une campagne ou Canvas, vous recevrez un message d’erreur qui vous empêchera d’archiver le groupe jusqu’à ce que vous supprimiez toutes les utilisations de celui-ci.

Vous pouvez archiver votre groupe à partir de la page **Groupes d’abonnement**. Trouvez votre groupe dans la liste, puis cliquez sur l’engrenage et sélectionnez **Archiver** dans le menu déroulant.

Braze ne traitera aucun changement d’état pour les utilisateurs des groupes archivés. Par exemple, si vous archivez le « Groupe d’abonnement A », alors que Susie est considérée comme `subscribed`, elle restera « "`subscribed` » à ce groupe, même si elle clique sur un lien de désabonnement (cela ne devrait pas intéresser Susie, le « Groupe d’abonnement A » est archivé et vous ne pouvez envoyer aucun message avec).

#### Exporter les modifications d’état d’abonnement utilisateur

Vous pouvez exporter les modifications d’état d’abonnement de vos utilisateurs via un fichier CSV. Dans la page **Centre de préférences**, cliquez sur **Données d’abonnement utilisateur**, puis sélectionnez **Exportation CSV des données d’abonnement utilisateur** dans la liste déroulante.

![Option d’exportation des données d’état d’abonnement utilisateur en tant que fichier CSV.][29]

Par défaut, les 30 derniers jours de modifications d’état dans tous les groupes d’abonnement sont exportés.

#### Voir les groupes d’abonnement dans l’analyse de campagne

Vous pouvez voir le nombre d’utilisateurs qui ont modifié leur état d’abonnement (abonnement ou désabonnement) à partir d’une campagne d’e-mail spécifique sur la page d’analyse de cette campagne.

Sur la page **Analyse de campagne** de votre campagne, faites défiler vers le bas jusqu’à la section **Performances de l’e-mail** et cliquez sur la flèche sous **Groupes d’abonnement** pour voir le nombre total de changements d’état, tel que soumis par vos clients.

![Performance du sous-groupe][30]

### Centre de préférence des e-mails

Le centre de préférences des e-mails est un moyen facile de gérer les utilisateurs qui reçoivent certains groupes de bulletins d’information et qui se trouvent dans le tableau de bord sous **Groupes d’abonnement**. Chaque groupe d'abonnement que vous créez est ajouté à la liste du centre de préférences. Cliquez sur le nom du centre de préférences pour avoir un aperçu interactif.

Pour placer un lien vers le centre de préférence dans vos e-mails, utilisez la balise Liquid suivante du centre de préférences et ajoutez-la à l’emplacement souhaité dans votre e-mail, de la même façon que vous insérez des [URL de désabonnement](#custom-footer).

{% raw %}
```
{{${preference_center_url}}}
```
{% endraw %}

{% alert note %}
Le centre de préférences dispose d’une case à cocher permettant à vos utilisateurs de se désabonner de tous les e-mails. Tenez compte du fait que vous ne pourrez pas sauvegarder ces préférences si elles sont envoyées en tant que message de test.
{% endalert %}

Le centre de préférences est destiné à être utilisé uniquement dans le canal e-mail lui-même. Les liens du centre de préférences sont dynamiques, basés sur chaque utilisateur et ne peuvent pas être hébergés en externe. Vous pouvez toutefois créer et héberger votre propre centre de préférences personnalisé avec les [endpoints de centre de préférence]({{site.baseurl}}/api/endpoints/preference_center/) et utiliser les [API REST du groupe d’abonnement][25] pour conserver les données en synchronisation avec Braze. Reportez-vous à la section suivante pour plus d’informations.

#### Personnalisez votre centre de préférences

Vous pouvez créer et héberger sur votre serveur Web un centre de préférences HTML entièrement personnalisé et synchroniser avec Braze grâce à notre [API][28]. À ce stade, vous ne pouvez avoir qu’un seul centre de préférences qui répertorie tous vos groupes d’abonnement actuels.

**Option 1 : Lien avec paramètres de requête de chaîne de caractères**

Utilisez les paires champ-valeur de la chaîne de caractères dans le corps de l’URL pour transmettre l’ID d’utilisateur et la catégorie d’e-mail à la page, afin que les utilisateurs n’aient qu’à confirmer leur choix de désabonnement. Cette option est valable pour ceux qui stockent un identifiant utilisateur dans un format haché et n’ont pas déjà de centre d’abonnement.

Pour cette option, chaque catégorie de courrier électronique nécessitera son propre lien de désabonnement :<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Il est également possible de hacher les `external_id` utilisateur au point d’envoi à l’aide d’un filtre Liquid. Cela convertira le `user_id` à une valeur de hachage md5, par exemple :
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}

My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

**Option 2 : Jeton Web JSON**

Utilisez un [jeton Web JSON](https://auth0.com/learn/json-web-tokens/) pour authentifier les utilisateurs sur une partie de votre serveur Web (par exemple, préférences de compte) qui se trouve normalement derrière une couche d’authentification, comme la connexion par nom d'utilisateur et mot de passe. Cette approche ne nécessite pas de paires de valeur de chaîne de requête incorporées dans l’URL, car elles peuvent être transmises dans la charge utile du jeton Web JSON, par exemple :

```json
{
    “user_id”: "1234567890",
    "name": "John Doe",
    “category": offre
}
```

##### Logo

Vous pouvez modifier le logo de votre centre de préférences. Cliquez sur l’engrenage, puis sur **Modifier** dans le menu qui apparaît.

### Modification des abonnements aux e-mail {#changing-email-subscriptions}

Dans la plupart des cas, vos utilisateurs gèrent leur abonnement aux e-mails via des liens d’abonnement inclus dans les e-mails qu’ils reçoivent.

Vous devez insérer un pied de page légalement conforme avec un lien de désabonnement au bas de chaque e-mail que vous envoyez. Lorsque les utilisateurs cliquent sur l’URL de désabonnement dans votre pied de page, ils doivent être désabonnés et amenés à une page d’accueil qui confirme la modification de leur abonnement.

#### Pieds de page personnalisés {#custom-footer}

{% raw %}
Braze provides the ability to set an app group-wide custom email footer which you can template into every email using the ``{{${email_footer}}}`` Liquid attribute.
{% endraw %}

De cette façon, vous n’avez pas à créer un nouveau pied de page pour chaque modèle de courriel ou de campagne par e-mail que vous utilisez. Les modifications apportées à votre pied de page personnalisé seront reflétées dans toutes les campagnes par e-mail existantes et nouvelles. Rappelez-vous que la conformité avec la [Loi CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) exige que vous incluiez une adresse physique pour votre entreprise et un lien de désabonnement dans vos e-mails. 

{% alert warning %}
Il est de votre responsabilité de vous assurer que votre pied de page personnalisé répond à ces exigences.
{% endalert %}

Pour créer ou modifier votre pied de page personnalisé, allez sur **Gérer les paramètres** et sélectionnez l’onglet **Paramètres des e-mails**.

![Panneau Paramètres des e-mails sortants.][19]

Dans la section **Pied de page personnalisé**, vous pouvez choisir d’activer les pieds de page personnalisés. Une fois activés, une fenêtre s’affiche pour modifier votre pied de page et envoyer un message de test.

![Bouton bascule de pied de page personnalisé activé.][20]

{% raw %}
You will see the default footer, which uses the ``{{${set_user_to_unsubscribed_url}}}`` attribute and Braze's physical mailing address. To comply with CAN-SPAM regulations, your custom footer must include ``{{${set_user_to_unsubscribed_url}}}``. You won't be able to save a custom footer without this attribute.

If using the default footer, which uses the ``{{${set_user_to_unsubscribed_url}}}`` attribute, be sure to select **&#60;other&#62;** for the **Protocol**.

![Protocol and URL values needed for the custom footer.][24]{: style="max-width:50%;"}

![Example email composed without a footer.][21]

> Be very careful to use a template with the custom footer ``{{${email_footer}}}`` or ``{{${set_user_to_unsubscribed_url}}}``when composing an email campaign. A warning will pop up; however, the ultimate decision of whether to send an email without an unsubscribe link lies with you.

![No-footer campaign composition.][22]

When creating a custom footer, Braze suggests you use attributes for personalization. Here are a few you may find useful:

| Attribute | Tag |
| --------- | --- |
| User's Email Address | `{{${email_address}}}` |
| User's Custom Unsubscribe URL | `{{${set_user_to_unsubscribed_url}}}` |
| User's Custom Opt-In URL | `{{${set_user_to_opted_in_url}}}` |
| User's Custom Subscribe URL | `{{${set_user_to_subscribed_url}}}` |
{: .reset-td-br-1 .reset-td-br-2}

Of course, the full set of default and custom attributes are available to you. As a best practice, Braze recommends including both an unsubscribe link (i.e., ``{{${set_user_to_unsubscribed_url}}}``) and an opt-in link (i.e., ``{{${set_user_to_opted_in_url}}}``) in your custom footer. This way, users will be able to both unsubscribe or opt-in, and you can passively collect opt-in data for a portion of your users.

You can also choose to set a custom footer for plaintext emails from the **Email Settings** tab, which follows the same rules as the custom footer for HTML emails. If you choose not to write a plaintext footer, Braze will automatically build one from the HTML footer. When your custom footers are to your liking, click **Save** at the bottom of the page.

![Email with Set Custom Plaintext Footer option selected.][23]{: style="max-width:70%" }

#### Custom unsubscribe landing page

When a user clicks on an unsubscribe URL in an email, they are taken to a default landing page that confirms the change to their subscription.

Optionally, you may provide HTML for your custom landing page that users will be directed to (instead of the default page) upon unsubscribing. This feature is available on the **Email Settings** page.

We recommend including a resubscribe link (i.e., `{{${set_user_to_subscribed_url}}}` ) on this page so that users have the option to resubscribe in case they unsubscribed by accident.

![Custom unsubscribe email in the Custom Unsubscribe Page panel.][11]

{% endraw %}

### Modification des abonnements aux notifications push {#changing-push-subscriptions}

Les SDK de Braze fournissent des méthodes pour modifier l’abonnement aux notifications push d’un utilisateur. Consultez la documentation technique de Braze pour votre plateforme mobile pour des informations sur la configuration de ces méthodes :

- [iOS][12]
- [Android et FireOS][13]
- [Windows Universal][14]

### Modification manuelle des abonnements utilisateur {#manually-changing-subscriptions}

Vous pouvez modifier manuellement l’état de l’abonnement pour n’importe quel utilisateur dans son profil utilisateur. Vous pouvez trouver des profils utilisateur individuels en recherchant l’ID ou l’adresse e-mail d’un utilisateur sur la page **Recherche utilisateur**. Sous l’onglet **Engagement** du profil utilisateur, vous trouverez l’état de l’abonnement aux e-mails et aux notifications push des utilisateurs. 

Cliquez sur les boutons **Désabonné**, **Abonné**, ou **Abonné** pour modifier le statut de l’abonnement de cet utilisateur. Si disponible, le profil utilisateur affiche également un horodatage de la dernière modification de l’abonnement de l’utilisateur.

![Statut d’abonnement d’un profil utilisateur comme abonné aux e-mails et aux notifications push.][16]{: style="max-width:60%" }

## Ciblage des abonnements et des campagnes {#subscriptions-and-campaign-targeting}

Les campagnes avec des notifications push ou des e-mails ciblent les utilisateurs qui sont inscrits ou abonnés par défaut. Vous pouvez modifier cette préférence de ciblage lors de la modification d’une campagne en allant à l’étape **Utilisateurs cibles** et en cliquant sur **Options avancées**.

Braze prend en charge trois états de ciblage :

- Les utilisateurs qui sont inscrits ou abonnés (par défaut).
- Uniquement les utilisateurs qui sont abonnés.
- Tous les utilisateurs, y compris ceux qui se sont désabonnés.

{% alert important %}
Il est de votre responsabilité de vous conformer aux [lois anti-spam]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations) lorsque vous utilisez ces paramètres de ciblage.
{% endalert %}

![Exemple de ciblage d’audience pour des utilisateurs qui sont inscrits ou abonnés aux options avancées de l’étape Utilisateurs cibles.][17]

## Segmentation par des abonnements utilisateur {#segmenting by-user-subscriptions}

Les filtres `Email Subscription Status` et `Push Subscription Status` vous permettent de segmenter vos utilisateurs par leur statut d’abonnement.

Cela peut être utile si vous souhaitez cibler les utilisateurs qui n’ont ni accepté ni refusé l’abonnement et les encouragez à s’abonner explicitement aux e-mails et aux notifications push. Dans ce cas, vous créerez un segment avec un filtre pour « L’état d’abonnement aux e-mails/notifications push est Abonné » et les campagnes de ce segment seront envoyées aux utilisateurs abonnés, mais pas à ceux qui n’ont pas confirmé.

![Statut d’abonnement aux e-mails utilisé comme filtre de segment.][18]

[11]: {% image_buster /assets/img/custom_unsubscribe.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/#setting-up-user-subscriptions
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/#managing-notification-subscription-statuses
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
