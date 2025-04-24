---
nav_title: Paramètres de sécurité
article_title: Paramètres de sécurité
page_order: 2
page_type: reference
description: "Cet article de référence traite des paramètres génériques de sécurité inter-entreprises, y compris des règles d’authentification, de la liste des adresses IP autorisées, des données d'identification et de l’authentification à deux facteurs."

---

# Paramètres de sécurité

> En tant qu'administrateur, la sécurité est l'une de vos principales préoccupations. La page **Paramètres de sécurité** peut vous aider à gérer les paramètres de sécurité génériques et interentreprises, notamment les règles d'authentification, la liste des adresses IP autorisées et l'authentification à deux facteurs.

Pour accéder à cette page, allez dans **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité**.

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), sélectionnez le menu déroulant de votre compte et allez dans **Paramètres de l'entreprise** > **Paramètres de sécurité**.
{% endalert %}

## Règles d’authentification

### Longueur du mot de passe

Utilisez ce champ pour modifier la longueur minimale du mot de passe requis. Le minimum par défaut est de huit caractères.

### Complexité du mot de passe

Sélectionnez **Renforcer les mots de passe complexes** pour exiger que les mots de passe comprennent au moins un élément de chacun des éléments suivants : 
- Lettre majuscule
- Lettre minuscule
- Nombre
- Caractère spécial

### Réutilisation du mot de passe

Détermine le nombre minimum de nouveaux mots de passe devant être définis avant qu’un utilisateur puisse réutiliser un mot de passe. La valeur par défaut est trois.

### Règles d’expiration du mot de passe

Utilisez ce champ pour définir quand vous souhaitez que les utilisateurs de votre compte Braze réinitialisent leur mot de passe.

### Règles de durée de session

Utilisez ce champ pour définir la durée pendant laquelle Braze gardera votre session active. Après que Braze considère votre session comme inactive (aucune activité pendant le nombre de minutes défini), l'utilisateur sera déconnecté. Le nombre maximum de minutes que vous pouvez entrer est de 10 080 (équivalent à une semaine) si l'authentification à deux facteurs est appliquée pour votre entreprise, sinon la durée maximale de session sera de 1 440 minutes (équivalent à 24 heures).

### Authentification par authentification unique (SSO)

Vous pouvez restreindre vos utilisateurs à la connexion à l’aide d’un mot de passe ou d’une Authentification unique (SSO).

Pour [l’authentification unique SAML][15], les clients doivent configurer leurs paramètres SAML avant application. Si les clients utilisent l’authentification unique de Google, ils n'ont qu'à appliquer la page des paramètres de sécurité sans aucune action supplémentaire.

## Liste des IP autorisées du tableau de bord

Utilisez le champ affiché pour autoriser des adresses IP spécifiques et des sous-réseaux à partir desquels les utilisateurs peuvent se connecter à votre compte (par exemple, depuis un réseau d'entreprise ou un VPN). Spécifiez les adresses IP et les sous-réseaux CIDR dans une liste séparée par des virgules. Si cela n’est pas précisé, les utilisateurs pourront se connecter à partir de n’importe quelle adresse IP.

## Authentification à deux facteurs

L'authentification à deux facteurs est requise pour tous les utilisateurs de Braze. Il ajoute un deuxième niveau de vérification d'identité à une connexion de compte, la rendant plus sécurisée qu'un simple nom d'utilisateur et mot de passe. Si votre tableau de bord ne peut pas prendre en charge l'authentification à deux facteurs, contactez votre gestionnaire du succès des clients. 

Lorsque l'authentification à deux facteurs est activée, en plus de saisir un mot de passe, les utilisateurs devront entrer un code de vérification lors de la connexion à leur compte Braze. Le code peut être envoyé via une application d'authentification, un e-mail ou un SMS.

Les utilisateurs qui ne configurent pas leur authentification à deux facteurs seront exclus de leur compte Braze. Les utilisateurs de compte Braze peuvent également configurer l'authentification à deux facteurs eux-mêmes dans **Paramètres du compte**, même si cela n'est pas requis par l'administrateur.

### Se souvenir de moi

![Case à cocher Se souvenir de ce compte pendant 30 jours][04]{: style="float:right;max-width:40%;margin-left:15px;"}

Après avoir activé l'authentification à deux facteurs pour votre entreprise, la case à cocher **Se souvenir de moi** devient disponible pour les utilisateurs. Cette fonctionnalité stocke un cookie sur votre appareil, ne nécessitant que de vous connecter avec une authentification à deux facteurs une seule fois au cours de 30 jours.

Les clients ayant plusieurs comptes sous une entreprise de tableau de bord peuvent rencontrer des problèmes en utilisant cette fonctionnalité en raison du fait que le cookie est lié à un appareil spécifique. Si les utilisateurs utilisent le même appareil pour se connecter à plusieurs comptes, le cookie sera remplacé pour les comptes précédemment autorisés sur cet appareil. Braze prévoit qu’un seul appareil soit associé à un compte, et non pas un seul appareil pour plusieurs comptes.

Assurez-vous d’enregistrer vos modifications avant de quitter la page !

### Réinitialisation de l'authentification de l'utilisateur

Les utilisateurs qui rencontrent des problèmes de connexion avec l'authentification à deux facteurs peuvent contacter les administrateurs de leur entreprise pour réinitialiser leur authentification à deux facteurs. Pour ce faire, demandez à un administrateur d'effectuer les opérations suivantes :

1. Allez dans **Paramètres** > **Utilisateurs de l'entreprise**.
2. Sélectionnez l'utilisateur dans la liste fournie.
3. Sélectionnez **Réinitialiser** sous **Authentification à deux facteurs**.

Une réinitialisation peut résoudre des problèmes d'authentification courants tels que des difficultés avec les applications d'authentification, la non-réception de la vérification par e-mail, l'échec de la connexion en raison de pannes de SMS ou d'erreurs de l'utilisateur, et plus encore.

## Accès renforcé

L'accès renforcé ajoute une couche de sécurité supplémentaire pour les actions sensibles dans votre tableau de bord de Braze. Lorsqu'il est actif, l'utilisateur doit revérifier son compte avant d'exporter un segment ou de consulter une clé API. Pour utiliser l'accès renforcé, accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez sur cette option. 

Si un utilisateur ne peut pas revérifier, il sera redirigé à l'endroit où il s'est arrêté et ne pourra pas poursuivre l'action sensible. Une fois qu'ils ont réussi à s'identifier à nouveau, ils n'ont plus besoin de le faire pendant l'heure qui suit, à moins qu'ils ne se déconnectent avant.

![Basculer l'accès renforcé.][5]

## Téléchargement d'un rapport d'événement de sécurité

Le rapport d’événement de sécurité est un rapport CSV d’événements de sécurité tels que les invitations de compte, les retraits de compte, les échecs et réussites de connexion, les tentatives de connexion et autres activités. Vous pouvez l'utiliser pour réaliser des audits internes.

Pour télécharger ce rapport, procédez comme suit :

1. Allez dans **Paramètres** > **Paramètres d'administration**.
2. Sélectionnez l'onglet **Paramètres de sécurité** et accédez à la section **Téléchargement des événements de sécurité**.
2. Sélectionnez **Télécharger le rapport**. 

Ce rapport contient uniquement les 10 000 événements de sécurité les plus récents pour votre compte. Si vous avez besoin de données d’événements spécifiques, contactez l’assistance technique.

{% details Événements signalés en matière de sécurité %}
### Identifiant et compte 
- Développeur supprimé
- Ajout d'un développeur supplémentaire
- Signé en
- Échec de l'identifiant
- Configuration de l'authentification à deux facteurs terminée
- Réinitialisation de l'authentification à deux facteurs terminée
- Autorisé Développeur 2FA
- Suspension du développeur
- Développeur non suspendu

### Accès surélevé
- Début de l'accès en hauteur
- Achevé Flux d'accès surélevés
- Échec de la vérification 2FA pour l'accès élevé

### Campagne arrêtée
- Campagne ajoutée
- Campagne modifiée

### Canvas
- Ajout d'un voyage
- Parcours modifié

### Segment
- Segmentation ajoutée
- Segment modifié
- Données exportées au format CSV
- Segment exporté via API

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

### Paramètres de l’entreprise
- Ajout d'un groupe d'applications
- Ajout d'une application

### Modèle d'e-mail
- Ajout d'un modèle d'e-mail
- Modèle d'e-mail mis à jour

### Pousser la lettre de créance
- Mise à jour de l'identifiant Push
- Suppression de l'identifiant de poussée

### Outil de débogage du SDK
- Démarrage de la session du débogueur SDK
- Journal du débogueur SDK exporté
{% enddetails %}

## Affichage des données d'identification {#view-pii}

L'autorisation **Afficher les IIP** n'est accessible qu'à quelques utilisateurs Braze sélectionnés. Pour connaître les possibilités existantes en matière de droits d'équipe, reportez-vous à la section [Définition des droits d'utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

Par défaut, tous les administrateurs ont l'autorisation de **voir les informations confidentielles** activée dans les [permissions de l'utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). Ceci signifie qu’ils peuvent voir les attributs personnalisés et standard sur tous les tableaux de bord. Lorsque cette autorisation est désactivée pour des utilisateurs, ces derniers ne pourront pas voir ces informations.

### Définition des données d'identification

Vous pouvez définir quels champs sont désignés comme PII dans le tableau de bord. Pour ce faire, allez dans **Paramètres de l'entreprise** > **Paramètres de sécurité**.

Les champs suivants peuvent être masqués aux utilisateurs de Braze qui n'ont pas les autorisations **Voir les IIP**.

| Attributs standard | Attributs personnalisés |
| ------------------- | ----------------- |
| {::nomarkdown} <ul> <li>Adresse e-mail </li> <li> Numéro de téléphone </li> <li> Prénom </li> <li> Nom </li> <li> Genre </li> <li> Anniversaire </li> <li> ID de l’appareil </li> <li> Localisation la plus récente </li> </ul> {:/} | {::nomarkdown} <ul> <li> Tous les attributs personnalisés<ul><li>Les attributs personnalisés individuels peuvent être marqués comme PII si vous n'avez pas besoin de masquer tous les attributs.</li></ul></li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Zones restreintes

Le texte suivant suppose que tous les champs sont définis comme PII et que les utilisateurs mentionnés sont ceux qui utilisent la plateforme Braze.

| Navigation sur le tableau de bord | Résultat | Remarques |
| -------------------- | ------ | ----- |
| User Search | L'utilisateur qui se connecte ne peut pas rechercher par adresse e-mail, numéro de téléphone, prénom ou nom de famille : {::nomarkdown} <ul> <li> Les attributs standard et personnalisés précédents ne seront pas affichés lors de la consultation d'un profil utilisateur. </li> <li> Impossible de modifier les attributs standard précédents d'un profil utilisateur à partir du tableau de bord de Braze. </li> </ul> {:/} | L’accès à cette section nécessite toujours l’accès au profil utilisateur. |
| User Import | L'utilisateur ne peut pas télécharger de fichiers depuis la page **Importation d'utilisateur**. | |
| {::nomarkdown} <ul> <li> Segments </li> <li> Campagnes </li> <li> Canvas </li> </ul> {:/} | Dans le menu déroulant **Données utilisateur** : {::nomarkdown} <ul> <li> L’utilisateur n’aura pas accès à l’option <b>CSV Export Email Address (Exportation CSV des e-mails)</b>. </li> <li> L’utilisateur n’obtiendra pas la norme et les attributs utilisateur précédents dans le fichier CSV lorsque vous sélectionnez <b>CSV Export User Data (Exportation CSV des données utilisateur)</b>. </li> </ul> {:/} | |
| Groupe de test interne | L’utilisateur n’aura pas accès aux attributs standards précédents d’un utilisateur ajouté au groupe de test interne. | |
| Journal des activités du message | L’utilisateur n’aura pas accès aux attributs standards précédents pour les utilisateurs identifiés dans le journal d’activité de message. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Lors de la prévisualisation d'un message, l'autorisation **Voir les IIP** n'est pas appliquée, de sorte que les utilisateurs peuvent voir les attributs standard précédents s'ils ont été référencés dans le message par l'intermédiaire de Liquid.
{% endalert %}

## Préférences en matière de suppression des données 

Vous pouvez utiliser ce paramètre pour définir des préférences quant à la suppression de certains champs lors du processus de suppression d'un utilisateur pour les événements. Ces préférences n'affectent que les données des utilisateurs qui ont été supprimés de Braze. 

Lorsqu'un utilisateur est supprimé, Braze supprime toutes les informations personnelles des données d'événements mais conserve les données anonymisées à des fins d'analyse. Certains champs définis par l'utilisateur peuvent contenir des IIP si vous envoyez des informations sur les utilisateurs finaux à Braze. Si ces champs contiennent des informations personnelles (PII), vous pouvez choisir de supprimer les données lorsque les données d'événement sont anonymisées pour les utilisateurs supprimés ; si les champs ne contiennent pas de PII, ils peuvent être conservés pour l'analyse.

Vous êtes responsable de déterminer les préférences correctes pour votre espace de travail. La meilleure façon de déterminer les paramètres appropriés est de consulter les équipes internes envoyant des données d'événements à Braze et les équipes utilisant des extras de message dans Braze pour confirmer si les champs peuvent contenir des informations personnelles identifiables (PII).  

### Champs pertinents  

| Nom ou type d'événement | Champ | Remarques |
| -------------------- | ------ | ----- |
| Événement personnalisé | propriétés |  |
| Événement d’achat | propriétés |  |
| Message envoyé | suppléments_de_messages | Plusieurs types d'événements contiennent un champ message_extras. La préférence s'applique à tous les types d'événements d'envoi de message qui prennent en charge message_extras, y compris les types d'événements ajoutés à l'avenir. |

{% alert warning %}
**La suppression est permanente !** Si vous choisissez de supprimer des champs de Snowflake pour les utilisateurs supprimés, le paramètre s'appliquera à toutes les données historiques de vos espaces de travail et à tous les événements pour les utilisateurs supprimés à l'avenir. Après que Braze a exécuté le processus pour appliquer les paramètres aux données d'événements historiques pour les utilisateurs supprimés, les données **ne peuvent pas être restaurées**.
{% endalert %}

### Configurer les préférences

Définissez les préférences par défaut en cochant les cases pour tous les champs qui doivent être supprimés si un utilisateur est supprimé. Sélectionnez l'un des champs contenant des IIP. Cette préférence s'appliquera à tous les espaces de travail actuels et futurs, sauf si les espaces de travail sont explicitement ajoutés à un groupe de préférences.

Pour personnaliser les préférences par espace de travail, vous pouvez ajouter des groupes de préférences avec des paramètres différents de ceux par défaut. Nous appliquons les paramètres par défaut à tous les espaces de travail qui ne sont pas ajoutés à un groupe de préférences supplémentaire, y compris les espaces de travail créés à l'avenir.  

![La section Préférences de suppression des données est basculée pour personnaliser les préférences de suppression des données par espace de travail.]({% image_buster /assets/img/deletion_preferences_1.png %})


[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "profil utilisateur obfusqué1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "profil utilisateur obfusqué2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "profil utilisateur obfusqué3"
[5]: {% image_buster /assets/img/elevated_access.png %}
[04]: {% image_buster /assets/img/remember_me.png %}
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
