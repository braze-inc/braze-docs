---
nav_title: Paramètres de sécurité
article_title: Paramètres de sécurité
page_order: 2
toc_headers: h2
page_type: reference
description: "Cet article de référence traite des paramètres génériques de sécurité inter-entreprises, y compris des règles d’authentification, de la liste des adresses IP autorisées, des données d'identification et de l’authentification à deux facteurs."

---

# Paramètres de sécurité

> En tant qu'administrateur, la sécurité est une priorité absolue dans votre liste de préoccupations. La page **Paramètres de** **sécurité** vous permet de gérer les paramètres de sécurité génériques et interentreprises, notamment les règles d'authentification, la liste blanche d'adresses IP et l'authentification à deux facteurs.

Pour accéder à cette page, allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité**.

## Règles d’authentification

### Longueur du mot de passe

Veuillez utiliser ce champ pour modifier la longueur minimale requise pour le mot de passe. Le nombre minimum par défaut est de huit caractères.

### Complexité du mot de passe

Sélectionnez **Appliquer des mots de passe complexes** pour exiger que les mots de passe comprennent au moins un élément de chacune des catégories suivantes : 
- Lettre majuscule
- Lettre minuscule
- Nombre
- Caractère spécial

### Réutilisation des mots de passe

Détermine le nombre minimum de nouveaux mots de passe devant être définis avant qu’un utilisateur puisse réutiliser un mot de passe. La valeur par défaut est trois.

### Règles d’expiration du mot de passe

Utilisez ce champ pour définir quand vous souhaitez que les utilisateurs de votre compte Braze réinitialisent leur mot de passe.

### Règles de durée de session

Utilisez ce champ pour définir la durée pendant laquelle Braze gardera votre session active. Une fois que Braze a déterminé que votre session est inactive (aucune activité pendant le nombre de minutes défini), Braze déconnecte l'utilisateur. Le nombre maximal de minutes que vous pouvez saisir est de 10 080 (équivalent à une semaine) si l'authentification à deux facteurs est appliquée dans votre entreprise. Dans le cas contraire, la durée maximale de session est de 1 440 minutes (équivalent à 24 heures).

### Authentification par authentification unique (SSO)

Vous pouvez restreindre vos utilisateurs à la connexion à l’aide d’un mot de passe ou d’une Authentification unique (SSO).

Pour l'[authentification unique (SSO) SAM]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/)L, les clients doivent configurer leurs paramètres SAML avant de procéder à l'application. Si les clients utilisent l’authentification unique de Google, ils n'ont qu'à appliquer la page des paramètres de sécurité sans aucune action supplémentaire.

## Liste des IP autorisées du tableau de bord

Utilisez le champ affiché pour autoriser des adresses IP spécifiques et des sous-réseaux à partir desquels les utilisateurs peuvent se connecter à votre compte (par exemple, depuis un réseau d'entreprise ou un VPN). Spécifiez les adresses IP et les sous-réseaux CIDR dans une liste séparée par des virgules. Si aucune restriction n'est spécifiée, les utilisateurs peuvent se connecter à partir de n'importe quelle adresse IP.

## Authentification à deux facteurs (2FA)

L'authentification à deux facteurs est obligatoire pour tous les utilisateurs de l'entreprise. Il ajoute un deuxième niveau de vérification d'identité à une connexion de compte, la rendant plus sécurisée qu'un simple nom d'utilisateur et mot de passe. Si votre tableau de bord ne peut pas prendre en charge l'authentification à deux facteurs, contactez votre gestionnaire du succès des clients. 

Lorsque l'authentification à deux facteurs est activée :

- En plus de saisir un mot de passe, les utilisateurs doivent entrer un code de vérification lorsqu'ils se connectent à leur compte Braze. Le code peut être envoyé par l'intermédiaire d'une appli d'authentification, d'un e-mail ou d'un SMS. 
- La case à cocher **Se souvenir de ce compte pendant 30 jours** devient disponible pour les utilisateurs.

Braze bloque les utilisateurs qui n'ont pas configuré l'authentification à deux facteurs depuis leur compte Braze. Les utilisateurs de compte Braze peuvent également configurer l'authentification à deux facteurs eux-mêmes dans **Paramètres du compte**, même si cela n'est pas requis par l'administrateur.

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

### Exigences relatives à la double authentification (2FA) au niveau de l'entreprise

Veuillez d'abord vérifier si l'authentification à deux facteurs (2FA) est activée pour votre tableau de bord en accédant à **Paramètres de l'entreprise** > **Paramètres de sécurité** > **Authentification à deux facteurs**. Si le bouton est gris, cela signifie que la 2FA n'a pas été activée pour votre entreprise et n'est pas obligatoire pour tous les utilisateurs de l'entreprise.

#### Options utilisateur lorsque la 2FA n'est pas obligatoire

Si la 2FA n'est pas appliquée au niveau de l'entreprise, les utilisateurs individuels peuvent configurer la 2FA pour eux-mêmes sur la page Paramètres du compte. Dans ce cas, les utilisateurs ne seront pas bloqués de leurs comptes s'ils ne procèdent pas à cette configuration. Vous pouvez identifier les utilisateurs qui ont choisi d'activer la 2FA en consultant la page Gérer les utilisateurs.

#### Exigences lorsque la 2FA est obligatoire

Si la 2FA est appliquée au niveau de l'entreprise, les utilisateurs qui ne la configurent pas sur leurs propres comptes lors de la connexion se verront refuser l'accès au tableau de bord. Les utilisateurs doivent effectuer la configuration de la 2FA pour conserver leur accès.

{% alert important %}
La double authentification (2FA) est requise pour tous les utilisateurs de l'entreprise uniquement si l'authentification unique (SSO) n'est pas activée. Si l'authentification unique (SSO) est utilisée, l'authentification à deux facteurs (2FA) n'a pas besoin d'être appliquée au niveau de l'entreprise.
{% endalert %}

## Configuration de l'authentification à deux facteurs (2FA)

### Configuration de la 2FA avec Authy

1. Veuillez télécharger l'application Authy depuis la boutique d'applications de votre appareil.
2. Dans Braze, veuillez saisir votre numéro de téléphone.
3. Veuillez appuyer sur la notification envoyée à votre appareil vous invitant à ouvrir l'application Authy.
4. Veuillez ouvrir l'application Authy sur votre appareil pour récupérer le code.
5. Dans Braze, veuillez saisir le code de vérification que vous avez reçu de la part d'Authy.

Si vous rencontrez des difficultés lors de la configuration et que vous êtes redirigé vers la page d'accueil ou l'écran d'identification de Braze, veuillez essayer les solutions suivantes :

- Veuillez utiliser le mode de navigation privée ou incognito : Veuillez réessayer la configuration à l'aide d'une fenêtre de navigation privée ou incognito. Cela permet de contourner les problèmes causés par les extensions ou les plugins du navigateur.
- Veuillez essayer un autre profil de navigateur : Si le problème persiste, envisagez d'utiliser un autre profil de navigateur afin d'éliminer les conflits avec les plugins installés.

### Configurer la 2FA lorsqu'elle n'est pas obligatoire

Pour activer manuellement l'authentification à deux facteurs (2FA) sur votre compte Braze lorsqu'elle n'est pas imposée, veuillez suivre les étapes suivantes :

1. Veuillez télécharger une application 2FA telle que Authy, Google Authenticator, Okta Verify ou similaire depuis l'App Store (iOS), le Google Play Store (Android) ou le Web. Ou, si vous préférez configurer la 2FA par e-mail ou SMS, veuillez passer à l'étape 2.
2. Dans Braze, veuillez vous rendre dans « Gérer le compte », faites défiler jusqu'à la section **« Authentification à deux facteurs** », puis sélectionnez **« Commencer la configuration** ».
3. Veuillez saisir votre mot de passe dans la fenêtre modale de connexion, puis sélectionner **Vérifier le mot de passe**.
4. Dans la boîte de dialogue modale **de configuration de l'authentification à deux facteurs**, veuillez saisir votre numéro de téléphone, puis sélectionner **Activer**.
5. Veuillez copier le code à sept chiffres généré à partir de votre application 2FA, de votre e-mail ou de votre SMS, puis retournez sur Braze et collez-le dans la fenêtre modale **de configuration de l'authentification à deux facteurs**. Veuillez sélectionner **Vérifier**.
6. (Facultatif) Afin d'éviter de saisir l'authentification à deux facteurs pendant les 30 prochains jours, veuillez activer l'option **« Mémoriser ce compte pendant 30 jours** ».

## Accès renforcé

L'accès renforcé ajoute une couche de sécurité supplémentaire pour les actions sensibles dans votre tableau de bord de Braze. Lorsqu'il est actif, l'utilisateur doit revérifier son compte avant d'exporter un segment ou de consulter une clé API. Pour utiliser l'accès renforcé, accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez sur cette option. 

Si un utilisateur ne peut pas revérifier, il sera redirigé à l'endroit où il s'est arrêté et ne pourra pas poursuivre l'action sensible. Une fois qu'ils ont réussi à s'identifier à nouveau, ils n'ont plus besoin de le faire pendant l'heure qui suit, à moins qu'ils ne se déconnectent avant.

![Basculer l'accès renforcé.]({% image_buster /assets/img/elevated_access.png %})

## Téléchargement d'un rapport sur les événements de sécurité {#security-event-report}

Le rapport d’événement de sécurité est un rapport CSV d’événements de sécurité tels que les invitations de compte, les retraits de compte, les échecs et réussites de connexion, les tentatives de connexion et autres activités. Vous pouvez l'utiliser pour réaliser des audits internes.

Pour télécharger ce rapport, procédez comme suit :

1. Allez dans **Paramètres** > **Paramètres d'administration**.
2. Sélectionnez l'onglet **Paramètres de sécurité** et accédez à la section **Téléchargement des événements de sécurité**.
3. Sélectionnez **Télécharger le rapport**. 

Ce rapport téléchargé manuellement ne contient que les 10 000 événements de sécurité les plus récents pour votre compte.

Pour exporter des événements de sécurité vers Amazon S3 sans cette limite de lignes, veuillez consulter [la section Exportation d'événements de sécurité avec Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/).

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
- Compte développeur mis à jour

### Accès surélevé
- Début de l'accès en hauteur
- Achevé Flux d'accès surélevés
- Échec de la vérification 2FA pour l'accès élevé
- Application de l'accès élevé activée
- Application des règles relatives à l'accès surélevé pour les personnes handicapées

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
- Utilisateurs du segment supprimés
- Cohorte autorisée

### Clé d'API REST
- Ajout d'une clé API REST
- Suppression de la clé API REST

### Informations d'authentification de base
- Ajout d'un identifiant Basic Auth
- Mise à jour de l'identifiant Basic Auth
- Suppression de l'identifiant Basic Auth

### Autorisation
- Autorisé Développeur 2FA
- Mise à jour de l'autorisation du compte
- Équipe ajoutée
- Équipe éditoriale
- Équipe archivée
- Équipe non archivée
- Ensemble d'autorisations du groupe d'applications créé
- Ensemble d'autorisations modifié pour le groupe d'applications
- Suppression de l'ensemble d'autorisations du groupe d'applications
- Création d'un rôle personnalisé
- Rôle personnalisé mis à jour
- Rôle personnalisé supprimé

### Paramètres de l’entreprise
- Ajout d'un groupe d'applications
- Ajout d'une application
- Modification des paramètres de l'entreprise
- Paramètres de sécurité de l'entreprise mis à jour
- Exportation des événements de sécurité vers le cloud mise à jour
- Ajout de pages de destination avec domaine personnalisé
- Suppression des pages de destination du domaine personnalisé
- Domaine personnalisé créé
- Domaine personnalisé supprimé
- Groupe de contrôle global activé
- Groupe de contrôle global désactivé
- Exclusions de contrôle global mises à jour
- Liste blanche des SMS du groupe d'abonnement mis à jour

### Modèle d'e-mail
- Ajout d'un modèle d'e-mail
- Modèle d'e-mail mis à jour

### Envoyer les informations d'identification
Mise à jour de l'identifiant Push
Suppression de l'identifiant de poussée

### Outil de débogage du SDK
- Démarrage de la session du débogueur SDK
- Journal du débogueur SDK exporté

### Utilisateurs
- Utilisateurs supprimés
- Utilisateurs consultés
- Importation d'utilisateurs en cours
- Statut du groupe d'abonnement utilisateur mis à jour
- Utilisateur supprimé
- Suppression d'un utilisateur unique annulée
- Suppression groupée d'utilisateurs annulée

### Catalogues
- Catalogue créé
- Catalogue supprimé

### Agents Braze
- Agent créé
- Agent modifié

### Opérateur BrazeAI 
- Réponse demandée à l'opérateur BrazeAI
- Réponse de l'opérateur BrazeAI
{% enddetails %}

## Affichage des données d'identification {#view-pii}

L'autorisation **d'affichage des informations personnelles identifiables** n'est accessible qu'à quelques utilisateurs sélectionnés de l'entreprise. Par défaut, tous les administrateurs ont l'autorisation de **voir les informations confidentielles** activée dans les permissions de l'utilisateur. Cela signifie qu'ils peuvent visualiser tous les attributs standard et personnalisés que votre entreprise a définis comme des informations personnelles identifiables dans l'ensemble du tableau de bord. Lorsque cette autorisation est désactivée pour les utilisateurs, ces derniers ne pourront visualiser aucun de ces attributs.

{% alert note %}
Vous devez disposer de l'autorisation **« Afficher les informations personnelles identifiables** » pour utiliser [le générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/building_queries/), car celui-ci permet d'accéder directement à certaines données clients.
{% endalert %}

Pour connaître les possibilités existantes en matière de droits d'équipe, reportez-vous à la section [Définition des droits d'utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

### Définition des données d'identification

{% alert important %}
La sélection et la définition de certains champs comme champs PII n'affectent que ce que les utilisateurs peuvent voir sur le tableau de bord de Braze et n'ont aucune incidence sur la manière dont les données des utilisateurs finaux dans ces champs PII sont traitées.<br><br>Veuillez consulter votre équipe juridique afin d'aligner les paramètres de votre tableau de bord sur les réglementations et politiques de confidentialité applicables à votre entreprise, y compris celles relatives à [la conservation des données]({{site.baseurl}}/data_retention/).
{% endalert %}

Vous pouvez sélectionner les champs que votre entreprise désigne comme des informations personnelles identifiables dans le tableau de bord. Pour ce faire, veuillez vous rendre dans **Paramètres de l'entreprise** > **Paramètres d'administration** > **Paramètres de sécurité**.

Les attributs suivants peuvent être désignés comme des informations personnelles identifiables et masqués aux utilisateurs de l'entreprise qui ne disposent pas des autorisations **nécessaires pour les consulter**.

#### Attributs potentiels des informations personnelles identifiables

| Attributs standard | Attributs personnalisés |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Adresse e-mail </li> <li> Numéro de téléphone </li> <li> Prénom </li> <li> Nom </li> <li> Genre </li> <li> Anniversaire </li> <li> ID de l’appareil </li> <li> Localisation la plus récente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Tous les attributs personnalisés<ul><li>Les attributs personnalisés individuels peuvent être marqués comme PII si vous n'avez pas besoin de masquer tous les attributs.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Zones restreintes

Ce qui suit suppose que tous les champs sont définis comme PII et que les utilisateurs mentionnés sont des utilisateurs professionnels qui utilisent la plateforme Braze. De plus, les attributs « précédents » renvoient à ceux figurant dans le tableau [des attributs PII potentiels](#potential-pii-attributes). La suppression des autorisations PII d'un utilisateur peut avoir un impact sur la facilité d'utilisation au-delà des domaines mentionnés.

| Navigation sur le tableau de bord | Résultat | Remarques |
| -------------------- | ------ | ----- |
| User Search | L'utilisateur qui se connecte ne peut pas rechercher par adresse e-mail, numéro de téléphone, prénom ou nom de famille : {::nomarkdown} <ul> <li> Les attributs standard et personnalisés précédents ne seront pas affichés lors de la consultation d'un profil utilisateur. </li> <li> Il n'est pas possible de modifier les attributs standard précédents d'un profil utilisateur à partir du tableau de bord de Braze. </li> <li> Il n'est pas possible de mettre à jour le statut de l'abonnement sur un profil utilisateur. </li></ul> {:/} | L'accès à cette section nécessite toujours l'autorisation de consulter un profil utilisateur. |
| User Import | L'utilisateur ne peut pas télécharger de fichiers depuis la page **Importation d'utilisateur**. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campagnes </li> <li> Canvas </li> </ul> {:/} | Dans le menu déroulant **Données utilisateur** : {::nomarkdown} <ul> <li> L’utilisateur n’aura pas accès à l’option <b>CSV Export Email Address (Exportation CSV des e-mails)</b>. </li> <li> Lorsque l'utilisateur sélectionne <b>l'option « Exporter les données utilisateur au format CSV</b> », les attributs standard et personnalisés précédents ne seront pas fournis dans le fichier CSV. </li> </ul> {:/} | |
| Groupe de test interne | L’utilisateur n’aura pas accès aux attributs standards précédents d’un utilisateur ajouté au groupe de test interne. | |
| Journal des activités du message | L’utilisateur n’aura pas accès aux attributs standards précédents pour les utilisateurs identifiés dans le journal d’activité de message. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Lors de la prévisualisation d'un message, l'autorisation **« Afficher les informations personnelles identifiables** » n'est pas appliquée. Par conséquent, les utilisateurs peuvent voir les [attributs standard précédents](#potential-pii-attributes) s'ils ont été référencés dans le message via Liquid.
{% endalert %}

## Préférences en matière de suppression des données 

Ce paramètre vous permet de définir vos préférences quant à la suppression de certains champs par Braze lors du processus de suppression d'utilisateurs pour les événements. Ces préférences n'affectent que les données des utilisateurs que Braze a supprimées. 

Lorsqu'un utilisateur est supprimé, Braze supprime toutes les IPI des données d'événement mais conserve les données anonymes à des fins d'analyse/analytique. Certains champs définis par l'utilisateur peuvent contenir des IIP si vous envoyez des informations sur les utilisateurs finaux à Braze. Si ces champs contiennent des informations personnelles identifiables, vous pouvez choisir de supprimer les données lorsque Braze anonymise les données d'événement pour les utilisateurs supprimés ; si les champs ne contiennent aucune information personnelle identifiable, vous pouvez les conserver à des fins d'analyse/analytique.

Vous êtes responsable de déterminer les préférences correctes pour votre espace de travail. La meilleure façon de déterminer les paramètres appropriés est de consulter les équipes internes envoyant des données d'événements à Braze et les équipes utilisant des extras de message dans Braze pour confirmer si les champs peuvent contenir des informations personnelles identifiables (PII).  

### Champs pertinents  

| Nom ou type d'événement | Champ | Remarques |
| -------------------- | ------ | ----- |
| Événement personnalisé | propriétés |  |
| Événement d’achat | propriétés |  |
| Message envoyé | message_extras | Plusieurs types d'événements contiennent un champ `message_extras`. La préférence s'applique à tous les types d'événements d'envoi de messages qui prennent en charge `message_extras`, y compris les types d'événements qui seront ajoutés à l'avenir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert warning %}
**La suppression est permanente !** Si vous choisissez de supprimer des champs de Snowflake pour les utilisateurs supprimés, ce paramètre s'applique à toutes les données historiques de vos espaces de travail et à tous les événements concernant les utilisateurs supprimés à l'avenir. Une fois que Braze a appliqué les paramètres aux données d'événements historiques des utilisateurs supprimés, il **n'est plus possible de restaurer** ces données.
{% endalert %}

### Configurer les préférences

Définissez les préférences par défaut en cochant les cases correspondant aux champs que Braze doit supprimer si un utilisateur est supprimé. Sélectionnez l'un des champs contenant des IIP. Cette préférence s'applique à tous les espaces de travail actuels et futurs, sauf si ceux-ci sont explicitement ajoutés à un groupe de préférences.

Pour personnaliser les préférences par espace de travail, vous pouvez ajouter des groupes de préférences avec des paramètres différents de ceux par défaut. Nous appliquons les paramètres par défaut à tous les espaces de travail qui ne sont pas ajoutés à un groupe de préférences supplémentaire, y compris les espaces de travail créés à l'avenir.  

![Section Préférences de suppression des données avec le bouton qui bascule pour personnaliser les préférences de suppression des données par espace de travail.]({% image_buster /assets/img/deletion_preferences_1.png %})

## Résolution des problèmes 

### Problèmes liés à la configuration de l'authentification à deux facteurs (2FA)

Si vous vous retrouvez dans une boucle après avoir saisi avec succès votre numéro de téléphone pour la 2FA et que vous êtes redirigé vers l'identifiant, cela est probablement dû à un échec de la vérification lors de la première tentative. Pour résoudre ce problème, veuillez suivre les étapes suivantes :

1. Veuillez désactiver tout bloqueur de publicités.
2. Veuillez activer les cookies dans les paramètres de votre navigateur.
3. Veuillez redémarrer votre ordinateur ou votre ordinateur portable.
4. Veuillez essayer de configurer à nouveau la 2FA.

Si le problème persiste après avoir suivi ces étapes, veuillez contacter [le service d'assistance]({{site.baseurl}}/braze_support/) pour obtenir de l'aide.

### Impossible d'activer l'authentification à deux facteurs (2FA)

Si la 2FA est activée mais que rien ne se produit lorsque vous sélectionnez le bouton **Activer**, cela peut être dû au fait que votre navigateur bloque la redirection nécessaire pour envoyer le code de vérification par SMS. Voici les étapes à suivre pour la résolution des problèmes :

1. Veuillez désactiver temporairement tout bloqueur de publicités que vous avez activé dans votre navigateur.
2. Veuillez vérifier que vous avez activé les cookies tiers dans les paramètres de votre navigateur.
3. Veuillez essayer de configurer l'authentification à deux facteurs.

### Le code de vérification n'est pas envoyé

Si vous rencontrez des difficultés lors de la saisie de votre numéro de téléphone sur la page Authy et que vous ne recevez pas de SMS, veuillez suivre les étapes suivantes :

1. Veuillez installer l'application Authy sur votre téléphone et vous connecter à l'authentificateur Authy.
2. Veuillez saisir votre numéro de téléphone et vérifier l'application Authy pour tout changement ou notification par SMS.
3. Si vous ne recevez toujours pas le SMS, veuillez essayer d'utiliser une autre connexion réseau, telle que votre réseau domestique ou un réseau Wi-Fi non professionnel. Les réseaux d'entreprise peuvent disposer de politiques de sécurité qui interfèrent avec la réception/distribution des SMS.

Si les problèmes persistent, veuillez supprimer l'ancien profil dans l'application Authy et scanner à nouveau le code QR pour configurer l'authentification à deux facteurs. Veuillez vous assurer que vous avez désactivé tous les bloqueurs de publicités, activé les cookies tiers ou utilisé un autre navigateur avant de réessayer la configuration.