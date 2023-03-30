---
nav_title: Paramètres de sécurité
article_title: Paramètres de sécurité
page_order: 2
page_type: reference
description: "Cet article de référence couvre les paramètres génériques de sécurité inter-entreprise, y compris les règles d’authentification, la whiteliste IP et l’authentification à deux facteurs (2FA)."

---

# Paramètres de sécurité

En tant qu’administrateur, la sécurité est une priorité absolue sur votre liste de préoccupations. Cette page peut vous aider à gérer les paramètres de sécurité génériques et interentreprises, y compris les règles d’authentification, whitelister l’adresse IP et l’authentification à deux facteurs.

## Règles d’authentification

### Longueur du mot de passe

La longueur minimale par défaut est de huit caractères.

### Complexité du mot de passe

Exigez que les mots de passe comprennent au moins l’un des éléments suivants : lettre majuscule, lettre minuscule, numéro et caractère spécial.

### Réutilisation du mot de passe

Détermine le nombre minimum de nouveaux mots de passe devant être définis avant qu’un utilisateur puisse réutiliser un mot de passe. La valeur par défaut est 3.

### Règles d’expiration du mot de passe

Utilisez ce champ pour définir quand vous souhaitez que les utilisateurs de votre compte Braze réinitialisent leur mot de passe.

### Règles de durée de session

Utilisez ce champ pour définir la durée pendant laquelle Braze gardera votre session active. Une fois que Braze considère que votre session est inactive (aucune activité pour le nombre défini de minutes), l’utilisateur sera déconnecté. Le nombre maximum de minutes que vous pouvez saisir est de 1 440 (égale à 24 heures).

### Restriction de l’authentification unique SSO

Vous pouvez restreindre vos utilisateurs à la connexion à l’aide d’un mot de passe ou d’une Authentification unique (SSO).

Pour l’[Authentification unique (SSO) SAML][15], les clients devront configurer leurs paramètres SAML avant de les appliquer. Si les clients utilisent l’authentification unique de Google, ils devront simplement faire appliquer la page des paramètres de sécurité sans charges supplémentaires.

## Whitelister les adresses IP du tableau de bord

Utilisez le champ affiché pour répertorier les adresses IP et sous-réseaux spécifiques à partir desquels les utilisateurs peuvent se connecter à votre compte (par exemple, à partir d’un réseau de l’entreprise ou d’un VPN). Spécifiez les adresses IP et les sous-réseaux CIDR dans une liste séparée par des virgules. Si cela n’est pas précisé, les utilisateurs pourront se connecter à partir de n’importe quelle adresse IP.

## Authentification à deux facteurs

L’authentification à deux facteurs ajoute un deuxième niveau de vérification d’identité à un journal de compte, ce qui le rend plus sûr qu’un nom d’utilisateur et un mot de passe. Basculer ce bouton sur **On (Activé)** réalisera une authentification à deux facteurs obligatoire pour tous les utilisateurs de compte Braze dans votre entreprise.

Lorsque l’authentification à deux facteurs est activée, en plus de saisir un mot de passe, les utilisateurs devront saisir un code de vérification envoyé à leur appareil mobile lors de la connexion à leur compte Braze.

{% alert tip %} Braze recommande de configurer une authentification à deux facteurs via l’application Authy plutôt que par SMS, au cas où vous rencontreriez des problèmes de réception de SMS à l’avenir. {% endalert %}

L’authentification à deux facteurs est facultative par défaut. Cependant, lorsqu’elle est activée, les utilisateurs qui ne configurent pas leur authentification à deux facteurs seront bloqués dans leur compte Braze. Les utilisateurs du compte Braze peuvent également configurer une authentification à deux facteurs par eux-mêmes dans **Account Settings (Paramètres du compte)**, même si cela n’est pas exigé par l’administrateur.

### Se souvenir de moi

![Case à cocher Remember this account for 30 days (Se souvenir de ce compte pendant 30 jours)][04]{: style="float:right;max-width:35%;margin-left:15px;"}
Lors de l’activation de l’authentification à deux facteurs pour votre entreprise, la case à cocher **Remember Me (Se souvenir de moi)** devient accessible aux utilisateurs. Cette fonctionnalité stocke un cookie sur votre appareil, ce qui vous oblige uniquement à vous connecter avec l’authentification à deux facteurs **une fois** au cours de 30 jours.

Les clients ayant plusieurs comptes sous un tableau de bord de l’entreprise peuvent rencontrer des problèmes en utilisant cette fonctionnalité en raison du cookie lié à un appareil spécifique. Si les utilisateurs utilisent le même appareil pour se connecter à plusieurs comptes, le cookie sera remplacé pour les comptes précédemment autorisés sur cet appareil. Braze prévoit qu’un seul appareil soit associé à un compte, et non pas un seul appareil pour plusieurs comptes.

Assurez-vous d’enregistrer vos modifications avant de quitter la page !

### Réinitialisation de l’authentification utilisateur

Les utilisateurs qui rencontrent des problèmes se connectant via une authentification à deux facteurs peuvent contacter les administrateurs de leur entreprise pour réinitialiser leur authentification à deux facteurs. Pour ce faire, demandez à un administrateur de naviguer vers **Manage Users (Gérer les utilisateurs)**, sélectionnez l’utilisateur dans la liste fournie, puis sélectionnez **Reset (Réinitialiser)** sous **Two-Factor Authentication (Authentification à deux facteurs)**. Une réinitialisation peut résoudre des problèmes d’authentification courants, tels que des problèmes avec Authy, une défaillance de connexion en raison d’interruptions de SMS ou d’erreurs de l’utilisateur, etc.

Application de l’authentification à deux facteurs :

- Si l’authentification à deux facteurs n’est pas appliquée au niveau de l’entreprise, une fois réinitialisée, l’utilisateur se connectera normalement et devra aller à **Account Settings (Paramètres du compte)** pour activer et configurer une authentification à deux facteurs.
- Si l’authentification à deux facteurs est appliquée au niveau de l’entreprise, la prochaine fois que l’utilisateur se connecte, il lui sera demandé de configurer son authentification à deux facteurs.

## Téléchargement des événements de sécurité

Le rapport d’événement de sécurité est un rapport CSV d’événements de sécurité tels que les invitations de compte, les retraits de compte, les échecs et réussites de connexion, les tentatives de connexion et autres activités. Pour télécharger ce rapport, cliquez sur le profil utilisateur en haut à droite de votre tableau de bord de Braze, sélectionnez **Company Settings (Paramètres de l’entreprise)**, puis l’onglet **Security Settings (Paramètres de sécurité)**. Descendez et sélectionnez **Download report (Télécharger le rapport)** dans la section **Security Event Download (Télécharger l’événement de sécurité)**. Ce rapport contient uniquement les 10 000 événements de sécurité les plus récents pour votre compte. Si vous avez besoin de données d’événements spécifiques, contactez l’assistance technique.

## Afficher les Informations personnellement identifiables

Cette section décrit une autorisation qui n’est disponible que pour quelques utilisateurs Braze sélectionnés. Pour les capacités d’autorisation d’équipe existantes, consultez [Définition des autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions).

Par défaut, tous les administrateurs peuvent utiliser la fonction **Afficher les informations personnellement identifiables**. Ceci signifie qu’ils peuvent voir les attributs personnalisés et standard sur tous les tableaux de bord. Lorsque cette autorisation est désactivée pour les utilisateurs dans les [permissions utilisateurs]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions), ceux-ci ne pourront pas voir cette information.

### Définir les informations personnellement identifiables

Braze vous autorise à définir quels champs sont définis comme étant des informations personnellement identifiables (PII) dans votre tableau de bord. Pour ce faire, rendez-vous sur **Company Settings > Security Settings (Paramètres de l’entreprise > Paramètres de sécurité)**.

Les champs suivants peuvent être cachés pour les utilisateurs Braze qui n’ont pas l’autorisation de **visualiser les informations personnellement identifiables**.

| Attributs standard | Attributs personnalisés |
| ------------------- | ----------------- |
| - Adresse e-mail<br>- Numéro de téléphone<br>- Prénom<br>- Nom<br>- Sexe<br>- Anniversaire<br>- ID de l’appareil<br>- Emplacement le plus récent | - Tous les attributs personnalisés |
{: .reset-td-br-1 .reset-td-br-2}

### Zones restreintes

Ce qui suit présuppose que tous les champs sont définis comme étant des informations personnellement identifiables et que les utilisateurs indiqués sont ceux qui utilisent la plateforme Braze.

| Navigation sur le tableau de bord | Résultat | Remarques |
| -------------------- | ------ | ----- |
| User Search | L’utilisateur qui se connecte ne peut pas rechercher par adresse e-mail, numéro de téléphone, prénom ou nom de famille :<br><br>• Ne verra pas le standard et les attributs personnalisés précédents lorsqu’il affiche un profil utilisateur.<br><br>• Ne pourra pas modifier les attributs standard précédents dans un profil utilisateur dans le tableau de bord de Braze.| L’accès à cette section nécessite toujours l’accès au profil utilisateur. |
| User Import | L’utilisateur ne peut pas télécharger les fichiers de la page **User Import (Importation d’utilisateurs)**. | |
| Segments<br>Campagnes<br>Canvas | Dans la liste déroulante **User Data (Données utilisateur)** :<br><br>• L’utilisateur n’aura pas accès à l’option **Exportation CSV des e-mails**.<br><br>• L’utilisateur n’obtiendra pas la norme et les attributs utilisateur précédents dans le fichier CSV lorsque vous sélectionnez **CSV Export User Data (Exportation CSV des données utilisateur)**. | |
| Groupe de test interne | L’utilisateur n’aura pas accès aux attributs standards précédents d’un utilisateur ajouté au groupe de test interne. | |
| Journal des activités du message | L’utilisateur n’aura pas accès aux attributs standards précédents pour les utilisateurs identifiés dans le journal d’activité de message. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Lorsque vous prévisualisez un message, la permission **Afficher les informations personnellement identifiables** n’est pas appliquée. Les utilisateurs peuvent voir les attributs standard précédents s’ils ont été référencés dans le message via Liquid.
{% endalert %}


[1]: {% image_buster /assets/img/user_profile_obfuscated1.png %} "user profile obfuscated1"
[2]: {% image_buster /assets/img/user_profile_obfuscated2.png %} "user profile obfuscated2"
[3]: {% image_buster /assets/img/user_profile_obfuscated3.png %} "user profile obfuscated3"

[04]: {% image_buster /assets/img/remember_me.png %}
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
