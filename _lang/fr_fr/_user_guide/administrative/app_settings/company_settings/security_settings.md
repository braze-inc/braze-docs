---
nav_title: Paramètres de sécurité
article_title: Paramètres de sécurité
page_order: 2
toc_headers: h2
page_type: reference
description: "Cet article de référence traite des paramètres génériques de sécurité inter-entreprises, y compris des règles d’authentification, de la liste des adresses IP autorisées, des données d'identification et de l’authentification à deux facteurs."

---

# Paramètres de sécurité

> En tant qu'administrateur, la sécurité est l'une de vos principales préoccupations. La page **Paramètres de sécurité** peut vous aider à gérer les paramètres de sécurité génériques et inter-entreprises, notamment les règles d'authentification, la liste des adresses IP autorisées et l'authentification à deux facteurs.

Pour accéder à cette page, allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité**.

## Règles d’authentification

### Longueur du mot de passe

Utilisez ce champ pour modifier la longueur minimale du mot de passe requis. Le minimum par défaut est de huit caractères.

### Complexité du mot de passe

Sélectionnez **Renforcer les mots de passe complexes** pour exiger que les mots de passe comprennent au moins un élément de chacun des éléments suivants : 
- Lettre majuscule
- Lettre minuscule
- Nombre
- Caractère spécial

### Réutilisation des mots de passe

Détermine le nombre minimum de nouveaux mots de passe devant être définis avant qu’un utilisateur puisse réutiliser un mot de passe. La valeur par défaut est trois.

### Règles d’expiration du mot de passe

Utilisez ce champ pour définir quand vous souhaitez que les utilisateurs de votre compte Braze réinitialisent leur mot de passe.

### Règles de durée de session

Utilisez ce champ pour définir la durée pendant laquelle Braze gardera votre session active. Lorsque Braze considère que votre session est inactive (aucune activité pendant le nombre de minutes défini), Braze déconnecte l'utilisateur. Le nombre maximal de minutes que vous pouvez saisir est de 10 080 (soit une semaine) si l'authentification à deux facteurs est appliquée dans votre entreprise. Dans le cas contraire, la durée maximale de la session est de 1 440 minutes (soit 24 heures).

### Authentification par authentification unique (SSO)

Vous pouvez restreindre vos utilisateurs à la connexion à l’aide d’un mot de passe ou d’une Authentification unique (SSO).

Pour l'[authentification unique (SSO) SAM]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/)L, les clients doivent configurer leurs paramètres SAML avant de procéder à l'application. Si les clients utilisent l’authentification unique de Google, ils n'ont qu'à appliquer la page des paramètres de sécurité sans aucune action supplémentaire.

## Liste des IP autorisées du tableau de bord

Utilisez le champ affiché pour autoriser des adresses IP spécifiques et des sous-réseaux à partir desquels les utilisateurs peuvent se connecter à votre compte (par exemple, depuis un réseau d'entreprise ou un VPN). Spécifiez les adresses IP et les sous-réseaux CIDR dans une liste séparée par des virgules. Si elle n'est pas spécifiée, les utilisateurs peuvent se connecter à partir de n'importe quelle adresse IP.

## Authentification à deux facteurs (2FA)

L'authentification à deux facteurs est requise pour tous les utilisateurs de Braze. Il ajoute un deuxième niveau de vérification d'identité à une connexion de compte, la rendant plus sécurisée qu'un simple nom d'utilisateur et mot de passe. Si votre tableau de bord ne peut pas prendre en charge l'authentification à deux facteurs, contactez votre gestionnaire du succès des clients. 

Lorsque l'authentification à deux facteurs est activée :

- Outre la saisie d'un mot de passe, les utilisateurs doivent saisir un code de vérification lorsqu'ils se connectent à leur compte Braze. Le code peut être envoyé par l'intermédiaire d'une appli d'authentification, d'un e-mail ou d'un SMS. 
- La case à cocher **Se souvenir de ce compte pendant 30 jours** devient disponible pour les utilisateurs.

Braze verrouille les utilisateurs qui ne configurent pas leur authentification à deux facteurs depuis leur compte Braze. Les utilisateurs de compte Braze peuvent également configurer l'authentification à deux facteurs eux-mêmes dans **Paramètres du compte**, même si cela n'est pas requis par l'administrateur.

Assurez-vous d’enregistrer vos modifications avant de quitter la page !

### Gardez ce compte en mémoire pendant 30 jours {#remember-me}

Cette fonctionnalité est disponible lorsque l'authentification à deux facteurs est activée.

Lorsque vous sélectionnez **Se souvenir de ce compte pendant 30 jours**, un cookie est stocké sur votre appareil, ne vous demandant de vous connecter avec l'authentification à deux facteurs qu'une seule fois sur une période de 30 jours. 

![Case à cocher Se souvenir de ce compte pendant 30 jours]({% image_buster /assets/img/remember_me.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Les clients ayant plusieurs comptes sous une entreprise de tableau de bord peuvent rencontrer des problèmes en utilisant cette fonctionnalité en raison du fait que le cookie est lié à un appareil spécifique. Si les utilisateurs utilisent le même appareil pour se connecter à plusieurs comptes, le cookie sera remplacé pour les comptes précédemment autorisés sur cet appareil. Braze prévoit qu’un seul appareil soit associé à un compte, et non pas un seul appareil pour plusieurs comptes.

### Réinitialisation de l'authentification de l'utilisateur

Si vous rencontrez des problèmes pour vous connecter avec l'authentification à deux facteurs, contactez les administrateurs de votre entreprise pour réinitialiser votre authentification à deux facteurs. Les administrateurs peuvent effectuer les opérations suivantes :

1. Allez dans **Paramètres** > **Utilisateurs de l'entreprise**.
2. Sélectionnez l'utilisateur dans la liste fournie.
3. Sélectionnez **Réinitialiser** sous **Authentification à deux facteurs**.

Une réinitialisation peut résoudre des problèmes d'authentification courants tels que des difficultés avec les applications d'authentification, la non-réception de la vérification par e-mail, l'échec de la connexion en raison de pannes de SMS ou d'erreurs de l'utilisateur, et plus encore.

### Exigences pour le 2FA au niveau de l'entreprise

Tout d'abord, vérifiez si l'authentification **à deux facteurs** est activée pour votre tableau de bord en vous rendant dans **Paramètres de l'entreprise** > **Paramètres de sécurité** > **Authentification à deux facteurs**. Si le basculeur est gris, l'option 2FA n'a pas été activée pour votre entreprise et n'est pas obligatoire pour tous les utilisateurs du tableau de bord.

#### Options pour l'utilisateur lorsque le 2FA n'est pas obligatoire

Si le 2FA n'est pas appliqué au niveau de l'entreprise, les utilisateurs individuels peuvent configurer le 2FA pour eux-mêmes sur leur page Paramètres du compte. Dans ce cas, les utilisateurs ne seront pas bloqués dans leur compte s'ils ne l'ont pas configuré. Vous pouvez identifier les utilisateurs qui ont choisi d'activer l'option 2FA en consultant la page Gérer les utilisateurs.

#### Exigences lorsque 2FA est obligatoire

Si le 2FA est appliqué au niveau de l'entreprise, les utilisateurs qui ne le configurent pas sur leurs propres comptes lors de la connexion seront bloqués hors du tableau de bord. Les utilisateurs doivent terminer la configuration de 2FA pour conserver l'accès.

{% alert important %}
Le 2FA est requis pour tous les utilisateurs de Braze uniquement si l'authentification unique (SSO) n'est pas activée. Si le SSO est utilisé, il n'est pas nécessaire d'appliquer le 2FA au niveau de l'entreprise.
{% endalert %}

## Mise en place de l'authentification à deux facteurs (2FA)

### Configurer 2FA avec Authy

1. Téléchargez l'application Authy dans la boutique d'applications de votre appareil.
2. Dans Braze, saisissez votre numéro de téléphone.
3. Appuyez sur la notification envoyée à votre appareil vous invitant à ouvrir l'appli Authy.
4. Lancez l'appli Authy sur votre appareil pour récupérer le code.
5. Dans Braze, saisissez le code de vérification que vous avez reçu d'Authy.

Si vous rencontrez des problèmes lors de la configuration et que vous êtes redirigé vers la page d'accueil ou l'écran d'identification de Braze, essayez ce qui suit :

- Utilisez le mode de navigation incognito ou privé : Réessayez la configuration avec une fenêtre de navigation incognito ou privée. Cela permet de contourner les problèmes causés par les extensions de navigateur ou les plugins.
- Essayez un autre profil de navigateur : Si le problème persiste, envisagez d'utiliser un autre profil de navigateur pour éliminer les conflits avec les plugins installés.

### Mettre en place le 2FA alors qu'il n'est pas appliqué

Pour activer manuellement l'authentification à deux facteurs (2FA) sur votre compte Braze lorsqu'elle n'est pas appliquée, procédez comme suit :

1. Téléchargez une application 2FA telle que Authy, Google Authenticator, Okta Verify ou une application similaire sur l'App Store (iOS), le Google Play Store (Android) ou sur le web. Ou, si vous préférez configurer 2FA par e-mail ou SMS, passez à l'étape 2.
2. Dans Braze, allez dans Gestion de compte, faites défiler jusqu'à la section **Authentification à deux facteurs**, puis sélectionnez **Démarrer la configuration**.
3. Saisissez votre mot de passe dans la fenêtre modale/boîte de dialogue, puis sélectionnez **Vérifier le mot de passe**.
4. Dans la fenêtre modale/boîte de dialogue **de configuration de l'authentification à deux facteurs**, entrez votre numéro de téléphone, puis sélectionnez **Activer**.
5. Copiez le code à sept chiffres généré à partir de votre appli 2FA, de votre e-mail ou de votre message SMS, puis retournez sur Braze et collez-le dans la fenêtre modale de **configuration de l'authentification à deux facteurs**. Sélectionnez **Vérifier**.
6. (Facultatif) Pour éviter d'avoir à saisir des données 2FA au cours des 30 prochains jours, activez l'option **Se souvenir de ce compte pendant 30 jours.** 

## Accès renforcé

L'accès renforcé ajoute une couche de sécurité supplémentaire pour les actions sensibles dans votre tableau de bord de Braze. Lorsqu'il est actif, l'utilisateur doit revérifier son compte avant d'exporter un segment ou de consulter une clé API. Pour utiliser l'accès renforcé, accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez sur cette option. 

Si un utilisateur ne peut pas revérifier, il sera redirigé à l'endroit où il s'est arrêté et ne pourra pas poursuivre l'action sensible. Une fois qu'ils ont réussi à s'identifier à nouveau, ils n'ont plus besoin de le faire pendant l'heure qui suit, à moins qu'ils ne se déconnectent avant.

![Basculer l'accès renforcé.]({% image_buster /assets/img/elevated_access.png %})

## Télécharger un rapport d'événement de sécurité {#security-event-report}

Le rapport d’événement de sécurité est un rapport CSV d’événements de sécurité tels que les invitations de compte, les retraits de compte, les échecs et réussites de connexion, les tentatives de connexion et autres activités. Vous pouvez l'utiliser pour réaliser des audits internes.

Pour télécharger ce rapport, procédez comme suit :

1. Allez dans **Paramètres** > **Paramètres d'administration**.
2. Sélectionnez l'onglet **Paramètres de sécurité** et accédez à la section **Téléchargement des événements de sécurité**.
2. Sélectionnez **Télécharger le rapport**. 

Ce rapport contient uniquement les 10 000 événements de sécurité les plus récents pour votre compte. Si vous avez besoin de données d’événements spécifiques, contactez l’assistance technique.

{% details Reported security events %}
### Identifiant et compte
- Signé en
- Échec de l'identifiant
- Configuration de l'authentification à deux facteurs terminée
- Réinitialisation de l'authentification à deux facteurs terminée
- Autorisé Développeur 2FA
- Ajout d'un développeur supplémentaire
- Compte ajouté
- Suspension du développeur
- Développeur non suspendu
- Développeur mis à jour
- Développeur supprimé
- Compte supprimé
- Mise à jour de l'état de l'abonnement des utilisateurs
- Utilisateur mis à jour
- Compte de développeur mis à jour

### Accès surélevé
- Début de l'accès en hauteur
- Achevé Flux d'accès surélevés
- Échec de la vérification 2FA pour l'accès élevé
- Activation de la mise en œuvre de l'accès en hauteur
- Application de l'accès surélevé pour les personnes handicapées

Campagne arrêtée
- Campagne ajoutée
- Campagne modifiée

Canvas
- Ajout d'un voyage
- Parcours modifié

### Segment
- Segmentation ajoutée
- Segment modifié
- Données exportées au format CSV
- Segment exporté via API
- Segmentation des utilisateurs supprimés
- Cohorte autorisée

### Clé d'API REST
- Ajout d'une clé API REST
- Suppression de la clé API REST

### Certificat d'authentification de base
- Ajout d'un identifiant Basic Auth
- Mise à jour de l'identifiant Basic Auth
- Suppression de l'identifiant Basic Auth

### Autorisation
- Autorisé Développeur 2FA
- Mise à jour de l'autorisation du compte
- Ajout d'une équipe
- Teams modifiée
- Teams archivé
- Teams non archivés
- Groupe d'applications créé Jeu de permissions
- Groupe d'applications modifié (App Group Permission Set)
- Suppression des autorisations du groupe d'applications
- Rôle personnalisé créé
- Mise à jour du rôle personnalisé
- Rôle personnalisé supprimé

### Paramètres de l’entreprise
- Ajout d'un groupe d'applications
- Ajout d'une application
- Modification des paramètres de l'entreprise
- Mise à jour des paramètres de sécurité de l'entreprise
- Mise à jour de l'exportation des événements de sécurité dans le nuage
- Ajout d'un domaine personnalisé pour les pages d'atterrissage
- Suppression du domaine personnalisé des pages d'atterrissage
- Création d'un domaine personnalisé
- Domaine personnalisé supprimé
- Activé Groupe de contrôle global
- Groupe de contrôle global désactivé
- Mise à jour des exclusions du contrôle global
- Mise à jour de la liste des autorisations de SMS du groupe d'abonnement

### Modèle d'e-mail
- Ajout d'un modèle d'e-mail
- Modèle d'e-mail mis à jour

### Pousser la lettre de créance
Mise à jour de l'identifiant Push
Suppression de l'identifiant de poussée

### Outil de débogage du SDK
- Démarrage de la session du débogueur SDK
- Journal du débogueur SDK exporté

### Utilisateurs
- Utilisateurs supprimés
- Utilisateurs consultés
- L'importation d'utilisateurs a commencé
- Statut du groupe d'abonnement d'un utilisateur mis à jour
- Utilisateur supprimé
- Suppression d'un utilisateur unique annulée
- Suppression en bloc d'un utilisateur annulée

### Catalogues
- Catalogue Créé
- Catalogue supprimé

### Agents Braze
- Agent créé
- Agent modifié

### Opérateur BrazeAI 
- Réponse demandée à l'opérateur BrazeAI
- L'opérateur BrazeAI a répondu
{% enddetails %}

## Affichage des données d'identification {#view-pii}

L'autorisation **Afficher les IIP** n'est accessible qu'à quelques utilisateurs Braze sélectionnés. Par défaut, tous les administrateurs ont l'autorisation de **voir les informations confidentielles** activée dans les permissions de l'utilisateur. Cela signifie qu'ils peuvent voir tous les attributs standard et personnalisés que votre entreprise a définis comme étant des IIP dans l'ensemble du tableau de bord. Lorsque cette autorisation est désactivée pour les utilisateurs, ces derniers ne pourront voir aucun de ces attributs.

{% alert note %}
Vous avez besoin de l'autorisation **Voir les DPI** pour utiliser le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), car il permet d'accéder directement à certaines données des clients.
{% endalert %}

Pour connaître les possibilités existantes en matière de droits d'équipe, reportez-vous à la section [Définition des droits d'utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### Définition des données d'identification

{% alert important %}
La sélection et la définition de certains champs en tant que champs PII affectent uniquement ce que les utilisateurs peuvent voir sur le tableau de bord de Braze et n'ont pas d'impact sur la manière dont les données de l'utilisateur final dans ces champs PII sont traitées.<br><br>Consultez votre équipe juridique pour aligner les paramètres de votre tableau de bord sur les réglementations et politiques de confidentialité applicables à votre entreprise, y compris celles relatives à la [conservation des données]({{site.baseurl}}/data_retention/).
{% endalert %}

Vous pouvez sélectionner les champs que votre entreprise désigne comme IIP dans le tableau de bord. Pour ce faire, allez dans **Paramètres de l'entreprise** > **Paramètres administratifs** > **Paramètres de sécurité**.

Les attributs suivants peuvent être désignés comme DPI et cachés aux utilisateurs de Braze qui ne disposent pas des autorisations **Afficher les DPI**.

#### Attributs potentiels des IIP

| Attributs standard | Attributs personnalisés |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Adresse e-mail </li> <li> Numéro de téléphone </li> <li> Prénom </li> <li> Nom </li> <li> Genre </li> <li> Anniversaire </li> <li> ID de l’appareil </li> <li> Localisation la plus récente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Tous les attributs personnalisés<ul><li>Les attributs personnalisés individuels peuvent être marqués comme PII si vous n'avez pas besoin de masquer tous les attributs.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Zones restreintes

Ce qui suit suppose que tous les champs sont définis comme des IIP et que les utilisateurs mentionnés sont ceux qui utilisent la plateforme de Braze. En outre, les attributs "précédents" sont ceux qui figurent dans le tableau des [attributs des IIP potentielles](#potential-pii-attributes). Le fait de retirer à un utilisateur les autorisations relatives aux IPI peut avoir un impact sur la facilité d'utilisation au-delà des domaines énumérés ci-dessus.

| Navigation sur le tableau de bord | Résultat | Remarques |
| -------------------- | ------ | ----- |
| User Search | L'utilisateur qui se connecte ne peut pas rechercher par adresse e-mail, numéro de téléphone, prénom ou nom de famille : {::nomarkdown} <ul> <li> Les attributs standard et personnalisés précédents ne seront pas affichés lors de la consultation d'un profil utilisateur. </li> <li> Impossible de modifier les attributs standard précédents d'un profil utilisateur à partir du tableau de bord de Braze. </li> <li> Impossible de mettre à jour l'état de l'abonnement sur un profil utilisateur. </li></ul> {:/} | L'accès à cette section nécessite toujours l'accès à la visualisation d'un profil utilisateur. |
| User Import | L'utilisateur ne peut pas télécharger de fichiers depuis la page **Importation d'utilisateur**. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campagnes </li> <li> Canvas </li> </ul> {:/} | Dans le menu déroulant **Données utilisateur** : {::nomarkdown} <ul> <li> L’utilisateur n’aura pas accès à l’option <b>CSV Export Email Address (Exportation CSV des e-mails)</b>. </li> <li> L'utilisateur ne recevra pas les attributs standard et personnalisés précédents dans le fichier CSV lorsque vous sélectionnez l'option <b>Exporter les données de l'utilisateur au format CSV</b>. </li> </ul> {:/} | |
| Groupe de test interne | L’utilisateur n’aura pas accès aux attributs standards précédents d’un utilisateur ajouté au groupe de test interne. | |
| Journal des activités du message | L’utilisateur n’aura pas accès aux attributs standards précédents pour les utilisateurs identifiés dans le journal d’activité de message. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Lors de la prévisualisation d'un message, l'autorisation **Voir les IIP** n'est pas appliquée, de sorte que les utilisateurs peuvent voir les [attributs standard précédents](#potential-pii-attributes) s'ils ont été référencés dans le message par l'intermédiaire de Liquid.
{% endalert %}

## Préférences en matière de suppression des données 

Ce paramètre vous permet de définir des préférences pour que Braze supprime certains champs lors du processus de suppression d'un utilisateur dans le cadre d'un événement. Ces préférences n'ont d'impact que sur les données des utilisateurs que Braze a supprimés. 

Lorsqu'un utilisateur est supprimé, Braze supprime toutes les IPI des données d'événement mais conserve les données anonymes à des fins d'analyse/analytique. Certains champs définis par l'utilisateur peuvent contenir des IIP si vous envoyez des informations sur les utilisateurs finaux à Braze. Si ces champs contiennent des IPI, vous pouvez opter pour la suppression des données lorsque Braze rend anonymes les données d'événement pour les utilisateurs supprimés ; si les champs ne contiennent pas d'IPI, vous pouvez les conserver à des fins d'analyse.

Vous êtes responsable de déterminer les préférences correctes pour votre espace de travail. La meilleure façon de déterminer les paramètres appropriés est de consulter les équipes internes envoyant des données d'événements à Braze et les équipes utilisant des extras de message dans Braze pour confirmer si les champs peuvent contenir des informations personnelles identifiables (PII).  

### Champs pertinents  

| Nom ou type d'événement | Champ | Remarques |
| -------------------- | ------ | ----- |
| Événement personnalisé | propriétés |  |
| Événement d’achat | propriétés |  |
| Message envoyé | message_extras | Plusieurs types d'événements contiennent un champ `message_extras`. La préférence s'applique à tous les types d'événements d'envoi de messages qui prennent en charge `message_extras`, y compris les types d'événements qui seront ajoutés à l'avenir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**La suppression est permanente !** Si vous optez pour la suppression de tous les champs de Snowflake pour les utilisateurs supprimés, le paramètre s'applique à toutes les données historiques dans vos espaces de travail et à tous les événements pour les utilisateurs supprimés à l'avenir. Une fois que Braze a exécuté le processus d'application des paramètres aux données d'événements historiques pour les utilisateurs supprimés, vous **ne pouvez pas restaurer les** données.
{% endalert %}

### Configurer les préférences

Définissez des préférences par défaut en cochant les cases des champs que Braze doit supprimer en cas de suppression d'un utilisateur. Sélectionnez l'un des champs contenant des IIP. Cette préférence s'applique à tous les espaces de travail actuels et futurs, sauf si les espaces de travail sont explicitement ajoutés à un groupe de préférences.

Pour personnaliser les préférences par espace de travail, vous pouvez ajouter des groupes de préférences avec des paramètres différents de ceux par défaut. Nous appliquons les paramètres par défaut à tous les espaces de travail qui ne sont pas ajoutés à un groupe de préférences supplémentaire, y compris les espaces de travail créés à l'avenir.  

![La section Préférences de suppression des données a été basculée pour personnaliser les préférences de suppression des données par espace de travail.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Résolution des problèmes 

### Problèmes de configuration de la boucle d'authentification à deux facteurs (2FA)

Si vous êtes pris dans une boucle après avoir saisi avec succès votre numéro de téléphone pour le 2FA et que vous êtes redirigé vers la page d'identifiant, cela est probablement dû à l'échec de la vérification lors de la première tentative. Pour résoudre ce problème, suivez les étapes suivantes :

1. Désactivez les bloqueurs de publicité.
2. Activez les cookies dans les paramètres de votre navigateur.
3. Redémarrez votre PC ou votre ordinateur portable.
4. Essayez à nouveau de configurer 2FA.

Si le problème persiste après ces étapes, contactez le [service d'assistance]({{site.baseurl}}/braze_support/) pour obtenir de l'aide.

### Impossible d'activer l'authentification à deux facteurs (2FA)

Si l'option 2FA est activée mais que rien ne se passe lorsque vous sélectionnez le bouton **Activer**, cela peut être dû au fait que votre navigateur bloque la redirection nécessaire à l'envoi du code de vérification par SMS. Voici les étapes à suivre pour résoudre ce problème :

1. Suspendez temporairement les bloqueurs de publicité que vous avez activés dans votre navigateur.
2. Confirmez que vous avez activé les cookies tiers dans les paramètres de votre navigateur.
3. Essayez de mettre en place le 2FA.

### Le code de vérification n'est pas envoyé

Si vous rencontrez des problèmes lorsque vous saisissez votre numéro de téléphone sur la page Authy et que vous ne recevez pas de SMS, procédez comme suit :

1. Installez l'application Authy sur votre téléphone et connectez-vous à l'authentificateur Authy.
2. Entrez votre numéro de téléphone et vérifiez l'application Authy pour tout changement ou notification par SMS.
3. Si vous ne recevez toujours pas le SMS, essayez d'utiliser une autre connexion réseau, par exemple votre réseau domestique ou un réseau Wi-Fi non professionnel. Les réseaux d'entreprise peuvent avoir des politiques de sécurité qui interfèrent avec la réception/distribution des SMS.

Si les problèmes persistent, supprimez l'ancien profil dans l'appli Authy et scannez à nouveau le code QR pour configurer 2FA. Assurez-vous que vous avez désactivé les bloqueurs de publicité, activé les cookies tiers ou utilisé un autre navigateur avant de tenter à nouveau la configuration.