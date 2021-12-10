---
nav_title: Paramètres de sécurité
article_title: Paramètres de sécurité
page_order: 2
page_type: Référence
description: "Cet article de référence couvre les paramètres génériques de sécurité entre les sociétés, y compris les règles d'authentification, la liste blanche IP et l'authentification à deux facteurs (2FA)."
---

# Paramètres de sécurité

En tant qu'administrateur, la sécurité est une priorité absolue sur votre liste de préoccupations. Cette page peut vous aider à gérer les paramètres de sécurité génériques et interentreprises, y compris les règles d'authentification, la liste blanche IP et l'authentification à deux facteurs.

## Règles d'authentification

### Longueur du mot de passe
La longueur minimale par défaut est de huit caractères.

### Complexité du mot de passe
Exiger que les mots de passe incluent au moins un des caractères suivants : une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial.

### Réutilisabilité du mot de passe
Détermine le nombre minimum de nouveaux mots de passe qui doivent être définis avant qu'un utilisateur puisse réutiliser un mot de passe. La valeur par défaut est 3.

### Règles d'expiration du mot de passe
Utilisez ce champ pour définir quand vous voulez que les utilisateurs de votre compte Braze réinitialisent leur mot de passe.

### Règles de durée de session
Utilisez ce champ pour définir combien de temps Braze gardera votre session active. Une fois que Braze jugera votre session inactive (aucune activité pour le nombre défini de minutes), l'utilisateur sera déconnecté. Le nombre maximum de minutes que vous pouvez entrer est de 1440 (égal à 24 heures).

### Restreindre SSO
Vous pouvez interdire à vos utilisateurs de se connecter en utilisant un mot de passe ou un SSO.

Pour [SAML SSO][1], les clients devront configurer leurs paramètres SAML avant de les appliquer. Si les clients utilisent Google SSO, ils devront simplement appliquer la page des paramètres de sécurité sans ascenseur supplémentaire.

## Tableau de bord IP whitelisting
Utilisez le champ montré pour mettre en liste blanche des adresses IP spécifiques et des sous-réseaux à partir desquels les utilisateurs peuvent se connecter à votre compte (par exemple, depuis un réseau d'entreprise ou un VPN). Spécifier les adresses IP et les sous-réseaux comme des plages CIDR dans une liste séparée par des virgules. Si non spécifié, les utilisateurs pourront se connecter à partir de n'importe quelle adresse IP.

## Authentification à deux facteurs
L'authentification à deux facteurs ajoute un deuxième niveau de vérification d'identité à un journal de compte, ce qui le rend plus sécurisé qu'un simple nom d'utilisateur et un mot de passe. Basculer ce commutateur sur __On__ rendra l'authentification à deux facteurs obligatoire pour tous les utilisateurs de votre compte Braze dans votre entreprise.

Lorsque l'authentification à deux facteurs est activée, en plus de la saisie d'un mot de passe, les utilisateurs devront entrer un code de vérification envoyé à leur appareil mobile lors de la connexion à leur compte Braze.

{% alert tip %} Braze recommande de configurer l'authentification à deux facteurs via l'application Authy plutôt que simplement SMS, au cas où vous rencontrez des problèmes pour recevoir des SMS dans le futur. {% endalert %}

L'authentification à deux facteurs est optionnelle par défaut. Cependant, lorsque cette option est activée, les utilisateurs qui ne parviennent pas à configurer leur authentification à deux facteurs seront exclus de leur compte Braze. Les utilisateurs du compte Braze peuvent également configurer l'authentification à deux facteurs seuls dans __Paramètres du compte__, même si ce n'est pas requis par l'administrateur.

### Se souvenir de moi
!\[Remember Me\]\[0\]{: style="float:right;max-width:30%;margin-left:15px;"} En basculant sur l'authentification à deux facteurs pour votre entreprise, la case à cocher __Remember Me__ devient disponible pour les utilisateurs. Cette fonctionnalité stocke un cookie sur votre appareil, vous demandant seulement de vous connecter avec l'authentification à deux facteurs __une fois__ au cours de 30 jours.

- Les clients ayant plusieurs comptes dans une société de tableau de bord peuvent rencontrer des problèmes en utilisant cette fonctionnalité en raison du fait que les cookies sont liés à un appareil spécifique. Si les utilisateurs utilisent le même appareil pour se connecter à plusieurs comptes, le cookie sera remplacé pour les comptes précédemment autorisés sur cet appareil. Braze s'attend à ce qu'un seul appareil soit associé à un compte, pas un seul appareil pour plusieurs comptes.

N'oubliez pas d'enregistrer vos modifications avant de quitter la page!

### Réinitialisation de l'authentification de l'utilisateur

Les utilisateurs rencontrant des problèmes de connexion via l'authentification à deux facteurs peuvent contacter les administrateurs de leur entreprise pour réinitialiser leur authentification à deux facteurs. Pour cela, demandez à un administrateur de naviguer vers __Gérer les utilisateurs__, sélectionnez l'utilisateur dans la liste fournie, et sélectionnez __Reset__ sous __Authentification à deux facteurs__. Une réinitialisation peut résoudre des problèmes d'authentification courants tels que des problèmes d'Autorisation, d'échec de connexion en raison de panne de SMS ou d'erreur de l'utilisateur, et plus encore.

Application de l'authentification à deux facteurs :
- Si l'authentification à deux facteurs n'est pas appliquée au niveau de la société, une fois réinitialisée, l'utilisateur se connectera normalement et devra aller dans __Paramètres du compte__ pour activer et configurer l'authentification à deux facteurs.
- Si l'authentification à deux facteurs est appliquée au niveau de la société, la prochaine fois que l'utilisateur se connecte, il lui sera demandé de configurer son authentification à deux facteurs.

## Téléchargement de l'événement de sécurité

Le rapport Événement Sécurité est un rapport CSV d'événements de sécurité tels que les invitations de compte, les suppressions de compte, les tentatives de connexion échouées et réussies, et d'autres activités. Pour télécharger ce rapport, cliquez sur **Télécharger le rapport** dans la section **Télécharger l'événement de sécurité**.
[0]: {% image_buster /assets/img/remember_me.png %}

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/
