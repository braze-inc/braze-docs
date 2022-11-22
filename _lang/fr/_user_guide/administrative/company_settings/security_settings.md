---
nav_title: Paramètres de sécurité
article_title: Paramètres de sécurité
page_order: 2
page_type: reference
description: "Cet article de référence couvre les paramètres génériques de sécurité inter-entreprise, y compris les règles d’authentification, la whiteliste IP et l’authentification à deux facteurs (2FA)."

---

# Paramètres de sécurité

En tant qu’administrateur, la sécurité est une priorité absolue sur votre liste de préoccupations. Cette page peut vous aider à gérer les paramètres de sécurité génériques et interentreprises, y compris les règles d’authentification, la whiteliste IP et l’authentification à deux facteurs.

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

Utilisez ce champ pour définir la durée pendant laquelle Braze tiendra votre session active. Une fois que Braze considère que votre session est inactive (aucune activité pour le nombre défini de minutes), l’utilisateur sera déconnecté. Le nombre maximum de minutes que vous pouvez saisir est de 1 440 (égale à 24 heures).

### Restriction SSO

Vous pouvez restreindre vos utilisateurs à la connexion à l’aide d’un mot de passe ou d’une SSO.

Pour l’[Authentification unique (SSO) SAML][1], les clients devront configurer leurs paramètres SAML avant de les appliquer. Si les clients utilisent l’authentification unique de Google, ils devront simplement faire appliquer la page des paramètres de sécurité sans charges supplémentaires.

## Whitelister les adresses IP du tableau de bord

Utilisez le champ affiché pour répertorier les adresses IP et sous-réseaux spécifiques à partir desquels les utilisateurs peuvent se connecter à votre compte (par exemple, à partir d’un réseau de l’entreprise ou d’un VPN). Spécifiez les adresses IP et les sous-réseaux CIDR dans une liste séparée par des virgules. Si cela n’est pas précisé, les utilisateurs pourront se connecter à partir de n’importe quelle adresse IP.

## Authentification à deux facteurs

L’authentification à deux facteurs ajoute un deuxième niveau de vérification d’identité à un journal de compte, ce qui le rend plus sûr qu’un nom d’utilisateur et un mot de passe. Basculer ce bouton sur **On** (Activé) réalisera une authentification à deux facteurs obligatoire pour tous les utilisateurs de compte Braze dans votre entreprise.

Lorsque l’authentification à deux facteurs est activée, en plus de saisir un mot de passe, les utilisateurs devront saisir un code de vérification envoyé à leur appareil mobile lors de la connexion à leur compte Braze.

{% alert tip %} Braze recommande de configurer une authentification à deux facteurs via l’application Authy plutôt que par SMS, au cas où vous rencontreriez des problèmes de réception de SMS à l’avenir. {% endalert %}

L’authentification à deux facteurs est facultative par défaut. Cependant, lorsqu’elle est activée, les utilisateurs qui ne configurent pas leur authentification à deux facteurs seront bloqués dans leur compte Braze. Les utilisateurs du compte Braze peuvent également configurer une authentification à deux facteurs par eux-mêmes dans **Account Settings** (Paramètres du compte), même si cela n’est pas exigé par l’administrateur.

### Se souvenir de moi

![Case à cocher Remember this account for 30 days (Se souvenir de ce compte pendant 30 jours)][0]{: style="float:right;max-width:35%;margin-left:15px;"}
Lors de l’activation de l’authentification à deux facteurs pour votre entreprise, la case à cocher **Remember Me** (Se souvenir de moi) devient accessible aux utilisateurs. Cette fonctionnalité stocke un cookie sur votre appareil, ce qui vous oblige uniquement à vous connecter avec l’authentification à deux facteurs **une fois** au cours de 30 jours.

Les clients ayant plusieurs comptes sous un tableau de bord de l’entreprise peuvent rencontrer des problèmes en utilisant cette fonctionnalité en raison du cookie lié à un périphérique spécifique. Si les utilisateurs utilisent le même périphérique pour se connecter à plusieurs comptes, le cookie sera remplacé pour les comptes précédemment autorisés sur ce périphérique. Braze prévoit qu’un seul périphérique soit associé à un compte, et non pas un seul périphérique pour plusieurs comptes.

Assurez-vous d’enregistrer vos modifications avant de quitter la page !

### Réinitialisation de l’authentification utilisateur

Les utilisateurs qui rencontrent des problèmes se connectant via une authentification à deux facteurs peuvent contacter les administrateurs de leur entreprise pour réinitialiser leur authentification à deux facteurs. Pour ce faire, demandez à un administrateur de naviguer vers **Manage Users** (Gérer les utilisateurs), sélectionnez l’utilisateur dans la liste fournie, puis sélectionnez **Reset** (Réinitialiser) sous **Two-Factor Authentication** (Authentification à deux facteurs). Une réinitialisation peut résoudre des problèmes d’authentification courants, tels que des problèmes avec Authy, une défaillance de connexion en raison d’interruptions de SMS ou d’erreurs de l’utilisateur, etc.

Application de l’authentification à deux facteurs :

- Si l’authentification à deux facteurs n’est pas appliquée au niveau de l’entreprise, une fois réinitialisée, l’utilisateur se connectera normalement et devra aller à **Account Settings** (Paramètres du compte) pour activer et configurer une authentification à deux facteurs.
- Si l’authentification à deux facteurs est appliquée au niveau de l’entreprise, la prochaine fois que l’utilisateur se connecte, il lui sera demandé de configurer son authentification à deux facteurs.

## Téléchargement des événements de sécurité

Le rapport d’événement de sécurité est un rapport CSV d’événements de sécurité tels que les invitations de compte, les retraits de compte, les échecs et réussites de connexion, les tentatives de connexion et autres activités. Pour télécharger ce rapport, cliquez sur **Download report** (Télécharger le rapport) dans la section **Security Event Download** (Téléchargement des événements de sécurité). Ce rapport contient uniquement les 10 000 événements de sécurité les plus récents pour votre compte. Si vous avez besoin de données d’événements spécifiques, contactez l’assistance technique.

[0]: {% image_buster /assets/img/remember_me.png %}
[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
