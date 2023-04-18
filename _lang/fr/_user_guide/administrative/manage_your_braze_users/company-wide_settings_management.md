---
nav_title: Paramètres de l’entreprise
article_title: Paramètres de l’entreprise
page_order: 5
page_type: reference
description: "Cet article de référence couvre les paramètres à l’échelle de l’entreprise, tels que la modification du nom de votre entreprise, la définition de votre fuseau horaire, vos préférences de notification, vos paramètres de sécurité, etc."

---

# Paramètres de l’entreprise

> La page **Company Settings (Paramètres de l’entreprise)** vous permet de modifier le nom de votre entreprise, de définir votre fuseau horaire et de demander à supprimer votre entreprise.<br><br>Seuls les administrateurs et utilisateurs disposant d’autorisations explicites pour gérer les paramètres de l’entreprise verront cette page.

### Conséquences du changement de fuseau horaire

Si vous choisissez de changer de fuseau horaire, vous risquez de subir diverses conséquences, notamment :

- Bien que les campagnes prévues pour des horaires spécifiques dans des endroits spécifiques (c.-à-d. 21 h, heure de l’Est) fonctionnent correctement selon la planification jusqu’à ce qu’elles soient modifiées, l’analyse de campagne et les futures planifications de campagne seront affectées par le changement.
- Toute planification de carte non associée à l’heure locale peut être affectée, avec des cartes actives pouvant potentiellement apparaître comme terminées (ou vice versa).
- Les filtres de segmentation de la forme « A fait X avant/après `Date` » verront l’heure ajustée, car la date initiale sera désormais localisée en heure du Pacifique.

### Préférences de notification

La page **Notification Preferences (Préférences de notification)** permet de configurer qui (le cas échéant) reçoit des notifications concernant votre entreprise. Vous pouvez configurer qui doit recevoir des notifications sur la campagne et la diffusion de la carte de fil d’actualités ou des erreurs techniques. Vous pouvez également spécifier les destinataires du rapport d’analyse hebdomadaire. Pour la plupart des notifications, Braze prend en charge les canaux d’e-mail et de connexion Webhook.

![Page Notification Preferences (Préférences de notification) dans le tableau de bord de Braze][61]

Le tableau suivant répertorie les notifications disponibles :

| Notification | Description | Canaux de notification disponibles |
|--------------|-------------|-----------------|
| Erreurs d’identification AWS | Informe le destinataire lorsque Braze reçoit une erreur lors d’un essai d’utilisation de vos informations d’identification Amazon Web Services pour une exportation de données. | E-mail, Webhook |
| Campagne arrêtée automatiquement | Avertit les destinataires lorsque Braze a arrêté une campagne. | E-mail |
| Expiration de l’interaction avec la campagne | Informe les destinataires d’une campagne dont l’expiration des données d’interaction de campagne est prévue, ainsi que de toute information pertinente sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | E-mail |
| Campagne/Canvas mis(e) à jour | Informe les destinataires lorsqu’une campagne/un canvas actif(ve) est mis(e) à jour ou désactivé(e), ainsi qu’une campagne/un canvas inactif(ve) est réactivé(e) ou lorsque des projets sont lancés. | E-mail |
| Expiration de l’interaction avec le Canvas | Informe les destinataires d’un Canvas dont l’expiration des données d’interaction de Canvas est prévue, ainsi que de toute information pertinente sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | E-mail |
| Carte de fil d’actualités publiée/en direct | Informe les destinataires lorsque des cartes de fil d’actualités sont planifiées ou publiées. | E-mail, Webhook |
| Erreurs d’identification de notification push | Avertit les destinataires lorsque les notifications push d’identification de l’application sont invalides et lorsqu’elles sont bientôt expirées. | E-mail, Webhook |
| Campagne planifiée envoyée/non envoyée | Informe les destinataires lorsque les campagnes planifiées commencent à être envoyées ou lorsque des tentatives d’envoi sont effectuées, mais qu’aucun utilisateur éligible n’a été trouvé. | E-mail, Webhook |
| Limite de campagne planifiée atteinte | Informe les destinataires lorsque la limite d’une campagne planifiée récurrente a été atteinte. | E-mail, Webhook |
| Envoi terminé d’une campagne planifiée | Informe les destinataires lorsque l’envoi d’une campagne planifiée est terminé. | E-mail, Webhook |
| Rapport hebdomadaire d’analyse | Envoie un résumé de l’activité du groupe d’apps de la semaine précédente aux destinataires tous les lundis. Les destinataires reçoivent un résumé pour chaque groupe d’apps auquel ils appartiennent. | E-mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Intégration du Webhook entrant pour Slack

Slack a une [application de Webhook entrant][67] qui permet de publier des messages de sources externes dans Slack. Pour commencer, ouvrez le Webhook entrant de l’application. 

1. Sélectionnez le canal Slack vers lequel vous souhaitez que les notifications soient envoyées et cliquez sur **Add Incoming Webhooks Integration (Ajouter une intégration de Webhooks entrants)**.<br><br>
    ![Ajouter l’intégration des Webhook entrants dans Slack][63]<br><br>
  Slack génère une URL que vous devrez saisir dans Braze pour les notifications que vous souhaitez recevoir.<br><br>
2. Copier l’**URL du Webhook**.<br><br>
    ![Copier l’URL du Webhook][64]<br><br>
3. Naviguez jusqu’à l’onglet **Notification Preferences (Préférences de notification)** dans **Company Settings (Paramètres de l’entreprise)**.<br><br>
4. Sélectionnez la notification que vous souhaitez activer pour Slack. Ou, si vous avez plusieurs notifications à envoyer à ce canal Slack, utilisez **Bulk Add (Ajout groupé)** pour ajouter le Webhook à plusieurs notifications.<br><br>
    ![Sélectionnez Slack notifications to enable (Notifications Slack à activer)][65]{: style="max-width:60%;"}<br><br>
5. Saisissez l’URL que Slack a générée pour vous.

Et voilà ! Vous devez commencer à recevoir des notifications concernant votre entreprise dans ce canal Slack. Vous pouvez également consulter l’article d’aide Slack sur cette rubrique : [Envoi de messages à l’aide des Webhooks entrants][62].

### Rapports hebdomadaires d’analyse

Braze propose l’option d’envoi d’un rapport hebdomadaire par e-mail aux personnes que vous désignez dans votre entreprise tous les lundis à 5 h EST. Les événements personnalisés à inclure dans le rapport hebdomadaire sont sélectionnés sur l’onglet **Custom Events (Événements personnalisés)** de la page **Manage Settings (Gérer les paramètres)** du tableau de bord. Vous pouvez sélectionner jusqu’à cinq événements à inclure dans votre rapport hebdomadaire :

![Sélection des événements à inclure dans le rapport d’analyse][22]

### Paramètres d’e-mail supplémentaires

Vous pouvez également accéder à l’onglet **Email Settings (Paramètres d’e-mails)** pour modifier :

- Le nom qui sera affiché par défaut sur vos e-mails
- Adresse de réponse par défaut pour vos e-mails
- Votre page de désabonnement personnalisé
  - Si vous ne fournissez pas de page de désabonnement personnalisé, Braze traitera automatiquement les désabonnements

![Section Outbound Email Settings (Paramètres d’e-mails sortants) de l’onglet Email Settings (Paramètres d’e-mail)][7]

## Paramètres de liste-désabonnement

![Se désabonner de ce lien de liste d’adresses dans un en-tête d’e-mail][57]{: style="float:right;max-width:60%;margin-left:15px;"}

Bien que la plupart des marketeurs ajoutent un lien de désabonnement en un clic à leur e-mail, il est recommandé de fournir un en-tête de messagerie spécial (« Liste-désabonnement ») qui permet aux fournisseurs de services d’e-mail tels que Gmail et Windows Live Hotmail de fournir leur propre fonctionnalité de désabonnement :

Pour plus d’informations sur liste-désabonnement, consultez les [Paramètres des e-mails][2]

## Paramètres de sécurité

La page de paramètres de sécurité permet de configurer les règles d’authentification, la whiteliste IP du tableau de bord et l’authentification à deux facteurs. Ces paramètres sont situés dans l’onglet **Security Settings (Paramètres de sécurité)** de la page **Company Settings (Paramètres de l’entreprise)**.

![Onglet Security Settings (Paramètres de sécurité) de la page Company Settings (Paramètres de l’entreprise)][50]

### Règles d’authentification

Les administrateurs de l’entreprise peuvent configurer les exigences d’authentification pour la connexion à Braze, y compris la définition des exigences de mot de passe (longueur minimale du mot de passe, complexité du mot de passe, expiration du mot de passe) et l’application de l’authentification Google.  Si l’administrateur de l’entreprise décide de définir des règles d’authentification de mot de passe pour devenir plus strict, dès que ces règles sont définies, les utilisateurs du compte seront informés par e-mail pour qu’ils modifient leurs mots de passe en conséquence.

![Section Authentication Rules (Règles d’authentification) de l’onglet Security Settings (Paramètres de sécurité)][51]

### Whitelister les adresses IP du tableau de bord

Votre équipe peut ajouter une whiteliste d’adresses IP, des plages et des sous-réseaux spécifiques à partir desquels les utilisateurs peuvent se connecter au compte Braze de votre entreprise.

Pour whitelister des adresses IP et sous-réseaux spécifiques, renseignez les adresses IP et les sous-réseaux à whitelister et cliquez sur Enregistrer les modifications au bas de la page. Les plages et sous-réseaux IP doivent être spécifiés dans la notation CIDR (Classless Inter-Domain Routing). Par exemple, whitelister `63.45.134.*` serait exprimé en notation CIDR en tant que `63.45.134.0/24`

Pour plus d’informations sur la notation CIDR, voir [RFC 4632][84].

![Section Dashboard IP Whitelisting (Whitelister des adresses IP) du tableau de bord dans l’onglet Security Settings (Paramètres de sécurité)][52]

### Authentification à deux facteurs

L’authentification à deux facteurs ajoute une étape supplémentaire de vérification d’identité lors de la connexion. En autorisant l’authentification à deux facteurs, Braze nécessitera deux méthodes de vérification pour vous connecter à votre compte Braze : votre mot de passe et votre téléphone mobile.  Braze utilise [Authy][56], un service d’authentification à deux facteurs, pour sécuriser votre compte.

#### Présentation de la configuration de l’authentification à deux facteurs Authy

1. Téléchargez l’application Authy.
2. Naviguez vers **Two-Factor Authentication (Authentification à deux facteurs)** sous **Account Settings (Paramètres du compte)** et saisissez votre numéro de téléphone.
3. Une notification sera envoyée à l’appareil demandant à Authy d’obtenir le code pour Braze.
4. Ouvrez l’application Authy sur l’appareil lié pour obtenir le code. 
5. Naviguer vers les paramètres **Two-Factor Authentication (Authentification à deux facteurs)** et saisissez le code. 

Si vous souhaitez appliquer l’authentification à deux facteurs pour toute l’entreprise, activez l’authentification à deux facteurs sous l’onglet **Security Settings (Paramètres de sécurité)** et cliquez sur **Save Changes (Enregistrer les modifications)** au bas de la page.

![Section Two-Factor Authentication (Authentification à deux facteurs) de l’onglet Security Settings (Paramètres de sécurité)][53]

Lorsque votre entreprise active l’authentification à deux facteurs, les utilisateurs du compte doivent configurer une authentification à deux facteurs sur leur propre compte lors de leur connexion ou d’autres seront verrouillés. Les utilisateurs du compte peuvent également accéder à la page des paramètres de leur compte pour l’activer. Il est possible de modifier votre numéro de téléphone portable au cas où un utilisateur de compte souhaiterait s’authentifier à l’aide d’un numéro de téléphone mobile différent.  En outre, si l’authentification à deux facteurs est facultative pour votre entreprise sous **Security Settings (Paramètres de sécurité)**, les utilisateurs du compte auront la possibilité de désactiver l’authentification à deux facteurs.
Si vous avez des difficultés à activer ou à vérifier avec une authentification à deux facteurs, contactez votre administrateur de compte ou ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

Sous l’onglet **Manage Users (Gérer les utilisateurs)**, une colonne supplémentaire indique les utilisateurs du compte qui ont activé l’authentification à deux facteurs.

![Section Account Users (Utilisateurs de compte) sur la page Manage Users (Gérer les utilisateurs)][55]

[2]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#include-a-list-unsubscribe-header
[7]: {% image_buster /assets/img_archive/email_settings_custom_new.png %}
[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[50]: {% image_buster /assets/img_archive/security_settings_new.png %}
[51]: {% image_buster /assets/img_archive/authentication_rules_new.png %}
[52]: {% image_buster /assets/img_archive/dashboard_ip_whitelisting_new.png %}
[53]: {% image_buster /assets/img_archive/two_factor_authentication_new.png %}
[55]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %}
[56]: https://www.authy.com
[57]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
[62]: https://api.slack.com/incoming-webhooks
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.png %}
[67]: https://my.slack.com/services/new/incoming-webhook/
[84]: https://tools.ietf.org/html/rfc4632
