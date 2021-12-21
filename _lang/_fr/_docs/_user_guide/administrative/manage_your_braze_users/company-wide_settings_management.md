---
nav_title: Paramètres de la société
article_title: Paramètres de la société
page_order: 5
page_type: Référence
description: "Cet article de référence couvre les paramètres de l'entreprise, comme le changement du nom de votre entreprise, la définition de votre fuseau horaire et la demande de suppression de votre entreprise."
---

# Paramètres de la société

## Gestion des paramètres de votre entreprise

La page [Paramètres de la société][1] vous permet de changer le nom de votre entreprise, de définir votre fuseau horaire et de demander la suppression de votre entreprise.

{% alert note %}
Seuls les administrateurs et les utilisateurs ayant des autorisations explicites pour gérer les paramètres de l'entreprise verront cette page.
{% endalert %}

### Conséquences du changement de fuseau horaire

Si vous choisissez de changer de fuseau horaire, vous pouvez avoir diverses conséquences, y compris :

- Pendant que les campagnes sont planifiées pour des heures spécifiques à des endroits spécifiques (i.e. 21h Heure de l'Est) sera correctement exécuté dans le calendrier jusqu'à ce qu'il soit modifié, à la fois l'analyse de la campagne et les futurs calendriers de la campagne seront affectés par le changement.
- Toute planification de carte qui n'est pas affectée à l'heure locale peut être affectée, les cartes actives pouvant apparaître comme terminées (ou vice versa).
- Les filtres de segmentation de la forme "A fait X avant/après `Date`auront l'heure ajustée parce que la date initiale sera maintenant localisée en heure du Pacifique.

### Préférences de notification

La page **Préférences de Notification** est l'endroit où vous pouvez configurer qui (s'il y en a) reçoit des notifications à propos de votre entreprise. Vous pouvez configurer qui doit recevoir des notifications concernant la diffusion de la campagne et de la carte de nouvelles ou des erreurs techniques. Vous pouvez également spécifier les destinataires pour le rapport analytique hebdomadaire. Pour la plupart des notifications, Braze prend en charge les canaux email et webhook.

!\[Préférences de notification\]\[61\]

Le tableau ci-dessous liste les notifications disponibles :

| Notification                                 | Libellé                                                                                                                                                                                                          | Support Webhook |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Erreurs d'identification AWS                 | Notifie les destinataires lorsque Braze reçoit une erreur en essayant d'utiliser vos identifiants Amazon Web Services pour une exportation de données.                                                           | Oui             |
| Campagne planifiée envoyé/non envoyée        | Notifie les destinataires quand des campagnes planifiées commencent à envoyer ou quand des campagnes planifiées tentaient d'envoyer mais n'avaient aucun utilisateur éligible à envoyer.                         | Oui             |
| Limite de la Campagne Planifiée Met          | Notifie les destinataires lorsqu'une campagne récurrente programmée n'est pas envoyée parce que la limite totale de la campagne a été atteinte.                                                                  | Oui             |
| Envoi de la campagne programmée terminé      | Notifie les destinataires quand une campagne planifiée a terminé l'envoi.                                                                                                                                        | Oui             |
| Délai d'attente du Webhook                   | Notifie les destinataires lorsqu'un webhook dépasse 300 fois en 5 minutes. Cette notification n'envoie pas plus d'une fois toutes les deux heures.                                                               | Oui             |
| Erreurs d'authentification push              | Notifie les destinataires quand les identifiants push d'une application sont invalides et quand les identifiants push d'une application expirent bientôt.                                                        | Oui             |
| Carte de flux d'actualités publiée/en direct | Notifie les destinataires lorsque les fiches de nouvelles sont planifiées ou publiées.                                                                                                                           | Oui             |
| Rapport hebdomadaire d'analyses              | Envoie un résumé de l'activité du groupe d'applications de la semaine dernière aux destinataires chaque lundi. Les destinataires reçoivent un résumé pour chaque groupe d'applications auquel ils appartiennent. | Non             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Intégration du webhook entrant Slack

Slack a une application de webhook entrante qui [permet de poster des messages de sources externes dans Slack][62]. Pour commencer, ouvrez l'application [webhook entrante][67].

1. Sélectionnez le canal Slack sur lequel vous souhaitez que les notifications aillent et cliquez sur **Ajouter l'intégration des Webhooks entrants**.<br><br> ! Ajouter une configuration][63]<br><br> Slack générera une URL que vous devrez entrer dans Braze pour les notifications que vous souhaitez recevoir.<br><br>
2. Copiez l'URL **Webhook**.<br><br> !\[Copier l'URL\]\[64\]<br><br>
3. Accédez à l'onglet **Préférences de notification** dans **Paramètres de la société**.<br><br>
4. Sélectionnez la notification que vous souhaitez activer pour Slack. Ou, si vous avez plusieurs notifications que vous voulez envoyer à ce canal Slack, Utilisez **Ajouter en bloc** pour ajouter le webhook à plusieurs notifications.<br><br> !\[Select Slack Notifications\]\[65\]{: style="max-width:80%;"}<br><br>
5. Entrez l'URL que Slack a générée pour vous.

Voilà! Vous devriez commencer à recevoir des notifications concernant votre entreprise sur ce canal Slack.

### Rapport d'analyse hebdomadaire

Braze envoie éventuellement un rapport hebdomadaire par courriel aux personnes que vous désignez au sein de votre entreprise tous les lundis à 5 h (HNE). Les événements personnalisés à inclure dans le rapport hebdomadaire sont sélectionnés dans l'onglet **Événements personnalisés** dans la page [Gérer les paramètres][19] du tableau de bord. Vous pouvez sélectionner jusqu'à 5 événements à inclure dans votre rapport hebdomadaire :

!\[Sélection de l'Événement Rapport Analytiques\]\[22\]

### Paramètres de messagerie supplémentaires

Vous pouvez également accéder à l'onglet [Paramètres de messagerie][8] pour modifier :

- Le nom qui sera affiché par défaut dans vos e-mails
- L'adresse de réponse par défaut pour vos e-mails
- Votre page de désinscription personnalisée
  - Si vous ne fournissez pas de page de désinscription personnalisée, Braze gérera automatiquement les désinscriptions

!\[paramètres de messagerie\]\[7\]

## Paramètres de désinscription de la liste

!\[Liste Unsubscribe\]\[57\]{: style="float:right;max-width:60%;margin-left:15px;"}

Bien que la plupart des marketeurs ajoutent un lien de désinscription en un clic à leur adresse e-mail, il est préférable de fournir un en-tête de courriel spécial (« Liste de désinscription ») qui permet aux fournisseurs de services de messagerie tels que Gmail et Windows Live Hotmail de fournir leur propre fonctionnalité de désinscription :

Pour plus d'informations sur la désinscription de la liste, reportez-vous à [Paramètres de messagerie][2]

## Paramètres de sécurité

La page des paramètres de sécurité est l'endroit où vous pouvez configurer les règles d'authentification, la liste blanche IP du tableau de bord et l'authentification à deux facteurs. Ces paramètres se trouvent dans l'onglet [Paramètres de sécurité][83] de la page **Paramètres de la société**.

!\[Paramètres de sécurité\]\[50\]

### Règles d'authentification

Les administrateurs de l'entreprise peuvent configurer les conditions d'authentification pour se connecter à Braze, y compris la configuration des exigences de mot de passe (longueur minimale du mot de passe, complexité du mot de passe, expiration du mot de passe) et l'application de l'authentification Google.  Si l'administrateur de l'entreprise décide de définir des règles d'authentification par mot de passe pour devenir plus strict, dès que ces règles seront définies, les utilisateurs du compte seront informés par e-mail pour changer leurs mots de passe en conséquence.

!\[Règles d'authentification\]\[51\]

### Tableau de bord IP whitelisting

Votre équipe peut ajouter une liste blanche d'adresses, de plages et de sous-réseaux spécifiques à partir desquels les utilisateurs peuvent se connecter au compte Braze de votre entreprise.

Pour marquer les adresses IP spécifiques et les sous-réseaux comme liste blanche, remplissez les adresses IP et les sous-réseaux à la liste blanche et appuyez sur Enregistrer les modifications en bas de la page. Les plages d'adresses IP et les sous-réseaux doivent être spécifiées dans la notation CIDR (Inter-Domain Routing) sans fil. Par exemple, la liste blanche `63.45.134.*` serait exprimée en notation CIDR comme `63.45.134.0/24`

Pour plus d'informations sur la notation CIDR, voir [RFC 4632][84].

!\[Tableau de bord IP liste blanche\]\[52\]

### Authentification à deux facteurs

L'authentification à deux facteurs ajoute une couche supplémentaire de vérification d'identité lors de la connexion. En activant l'authentification à deux facteurs, Braze demandera deux méthodes de vérification pour se connecter à votre compte Braze : votre mot de passe et votre téléphone mobile.  Braze utilise [Authy][56], un service d'authentification à deux facteurs pour vous aider à sécuriser votre compte.

#### Aperçu de la configuration de l'authentification à deux facteurs
1. Télécharger l'application Authy
2. Allez à **Authentification à deux facteurs** sous **Paramètres du compte** et entrez votre numéro de téléphone.
3. Il y aura une notification envoyée à l'appareil demandant d'ouvrir Authy pour obtenir le code pour le Brésil.
4. Ouvrez l'application Authy sur l'appareil lié pour obtenir le code.
5. Naviguez dans les paramètres de l' **authentification à deux facteurs** et entrez le code.

Si vous souhaitez imposer l'authentification à deux facteurs pour l'ensemble de la société, activez l'authentification à deux facteurs sous l'onglet **Paramètres de sécurité** et cliquez sur **Enregistrer les modifications** en bas de la page.

!\[Authentification à deux facteurs\]\[53\]

Lorsque votre entreprise met en œuvre l'authentification à deux facteurs, les utilisateurs du compte doivent configurer l'authentification à deux facteurs sur leur propre compte lors de la connexion, sinon ils seront bloqués. Les utilisateurs du compte peuvent également accéder à la page des paramètres de leur compte pour l'activer. Il y a une option pour changer votre numéro de téléphone mobile au cas où un utilisateur souhaiterait s'authentifier à l'aide d'un autre numéro de téléphone mobile.  De plus, si l'authentification à deux facteurs est facultative pour votre entreprise dans **Paramètres de sécurité**, les utilisateurs du compte auront la possibilité de désactiver l'authentification à deux facteurs. Si vous avez des difficultés à activer ou à vérifier avec l'authentification à deux facteurs, contactez l'administrateur de votre compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/).

Sous l'onglet **Gérer les utilisateurs** , il y aura une colonne supplémentaire qui indique quels utilisateurs du compte ont activé l'authentification à deux facteurs.

!\[Gérer les utilisateurs\]\[55\]
[7]: {% image_buster /assets/img_archive/email_settings_custom_new.png %} [22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %} [50]: {% image_buster /assets/img_archive/security_settings_new. ng %} [51]: {% image_buster /assets/img_archive/authentication_rules_new.png %} [52]: {% image_buster /assets/img_archive/dashboard_ip_whitelisting_new.png %} [53]: {% image_buster /assets/img_archive/two_factor_authentication_new. ng %} [55]: {% image_buster /assets/img_archive/two_factor_authentication_manage_users_new.png %} [57]: {% image_buster /assets/img_archive/list_unsub_img1.png %} [61]: {% image_buster /assets/img_archive/notification_preferences. ng %} [63]: {% image_buster /assets/img_archive/slack_f.png %} [64]: {% image_buster /assets/img_archive/copy_url. ng %} [65]: {% image_buster /assets/img_archive/click_edit_f.png %}

[1]: https://dashboard-01.braze.com/company_settings/company_settings/ "Company Settings Page"
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#include-a-list-unsubscribe-header
[8]: https://dashboard-01.braze.com/app_settings/app_settings/email/ "Email App Settings"
[19]: https://dashboard-01.braze.com/app_settings/app_settings/ "App Settings Page"
[56]: https://www.authy.com
[62]: https://api.slack.com/incoming-webhooks
[67]: https://my.slack.com/services/new/incoming-webhook/
[83]: https://dashboard-01.braze.com/company_settings/company_settings/security-management/
[84]: https://tools.ietf.org/html/rfc4632
