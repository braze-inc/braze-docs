---
nav_title: Accéder à votre compte
article_title: Accéder à votre compte
page_order: 2
page_type: reference
description: "Cet article explique comment obtenir votre compte Braze, comment vous connecter une fois l'accès accordé et comment réinitialiser votre mot de passe Braze."

---

# Accéder à votre compte

> Cet article explique comment obtenir votre compte Braze, comment vous connecter après avoir obtenu un accès, et comment résoudre les problèmes d'accès à votre tableau de bord et de performance de votre tableau de bord.

Si vous êtes le premier utilisateur de Braze au sein de votre entreprise et que vous vous connectez pour la première fois, vous recevrez un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre e-mail et de vous connecter le premier jour de votre contrat.

Après avoir confirmé votre compte, vous pouvez ajouter des utilisateurs supplémentaires à partir de la page [Utilisateurs de l'entreprise de]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) votre tableau de bord. Tous les utilisateurs recevront un e-mail leur demandant de confirmer leur compte après avoir été ajoutés.

Si vous n'êtes pas le premier utilisateur du compte Braze de votre entreprise, contactez l'administrateur du compte Braze de votre entreprise et demandez-lui de créer votre compte. Vous recevrez alors un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre e-mail et de vous connecter.

## Connexion

Voyons comment vous connecter, que ce soit la première ou la millionième fois ! Si vous êtes le premier utilisateur de votre entreprise, suivez les conseils de la section précédente. Si ce n'est pas le cas, vous pouvez vous connecter après que l'administrateur Braze de votre entreprise a créé votre compte.

Vous pouvez soit vous connecter à partir du site d'accueil, soit utiliser l'URL de votre tableau de bord correspondant à votre instance Braze spécifique. [Braze.com](https://www.braze.com) ou utiliser l'URL de votre tableau de bord correspondant à votre [instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Pour vous faciliter la tâche, Braze propose plusieurs options d'authentification unique (SSO), notamment :

* [AUTHENTIFICATION UNIQUE (SSO) SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [Approvisionnement SAML juste à temps]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
Après vous être connecté à Braze avec SSO, vous ne pouvez plus utiliser votre mot de passe pour vous connecter au tableau de bord.
{% endalert %}

## Navigateurs pris en charge

Le tableau de bord de Braze prend en charge les navigateurs suivants :
- Chrome (version 87 ou plus récente)
- Firefox (version 85 ou plus récente)
- Safari (version 15.4 ou plus récente)
- Edge (version 87 ou plus récente)

Si votre tableau de bord de Braze indique que vous avez une erreur inattendue et que l'outil de console de votre navigateur affiche l'erreur `ReferenceError: structuredClone is not defined`, votre navigateur est obsolète. Si cette erreur se reproduit, désinstallez et réinstallez votre navigateur.

## Accéder à plusieurs tableaux de bord de Braze

Braze ne vous permet pas d'enregistrer la même adresse e-mail pour plusieurs utilisateurs de tableaux de bord dans le même cluster (par exemple, si vous avez deux tableaux de bord sur US-01). Vous pouvez utiliser le même e-mail pour créer des comptes sur différents clusters (par exemple, si vous avez un tableau de bord sur US-01 et un sur US-05). Si vous devez accéder à plusieurs tableaux de bord de Braze dans le même cluster, vous pouvez procéder comme suit :

### Utilisez des alias d'e-mail

Si votre fournisseur d'e-mail est Gmail, vous pouvez créer des alias en ajoutant un signe `+` suivi d'un texte quelconque à votre adresse e-mail. Par exemple :
- **E-mail original :** `rocky@gmail.com`
- **Alias e-mail :** `rocky+1@gmail.com`

Les deux adresses e-mail dirigeront les e-mails vers la même boîte de réception, mais Braze les reconnaîtra comme des comptes distincts lorsque vous vous connecterez.

### Créez des alias distincts avec d'autres fournisseurs

Si votre fournisseur d'e-mail ne prend pas en charge l'alias `+`, vous pouvez toujours créer des alias distincts, par exemple en configurant `rocky@braze.com` pour qu'il soit transféré à `rocky.lotito@braze.com`. Cela permet à plusieurs adresses d'être entonnées dans la même boîte de réception tout en étant reconnues comme des e-mails différents par Braze.

### Utiliser des développeurs multi-entreprises

La fonctionnalité "développeurs multi-entreprises" permet de partager un même compte utilisateur entre plusieurs entreprises. Les utilisateurs peuvent basculer entre les différents tableaux de bord de l'entreprise à partir du menu de leur profil utilisateur.

Si vous disposez d'une authentification unique (SSO) et que vous souhaitez mettre en place des développeurs multi-entreprises, vous devez activer un ID d'entité personnalisé SAML en mettant en place une intégration SSO personnalisée (SAML SSO). Suivez les étapes de l'[identification initiée par le fournisseur de services (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), mais appliquez ces changements :
- Modifiez l'**ID de l'entité** à `braze_dashboard_<companyID>` pour chaque intégration de tableau de bord.
- Contactez votre gestionnaire de satisfaction client ou votre gestionnaire de compte pour activer la bascule de fonctionnalité `saml_sso_custom_entity_id` pour chaque tableau de bord.

### Considérations relatives à l'authentification unique (SSO)

Si vous utilisez l'authentification unique (SSO), sachez que le fait d'avoir plusieurs adresses e-mail différentes pourrait entraîner des complications. Confirmez que vos paramètres SSO sont correctement configurés pour éviter les problèmes d'accès.

## Résolution des problèmes

### Réinitialisation de votre mot passe

Pour réinitialiser votre mot de passe, sélectionnez le lien **Mot de passe oublié ?** sur la page d'identification du tableau de bord. Vous serez invité à saisir votre e-mail pour recevoir un lien vous permettant de réinitialiser votre mot de passe.

Identifiant du tableau de bord avec l'invite "Mot de passe oublié".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Effacer la mémoire cache de votre navigateur et les cookies

Si vous rencontrez des problèmes avec les performances du tableau de bord, par exemple si votre tableau de bord ou la liste des performances des segments ne se charge pas, essayez d'effacer le cache et les cookies de votre navigateur en suivant les étapes indiquées pour votre navigateur respectif.

{% alert important %}
En supprimant les cookies, vous vous déconnectez, ce qui entraîne la perte des travaux non sauvegardés.
{% endalert %}

- [Effacer le cache & cookies dans Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Effacer les cookies dans Safari sur Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Effacer les cookies et les données de site dans Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Supprimer tous les cookies dans Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Si la suppression du cache et des cookies de votre navigateur ne résout pas vos problèmes, contactez l ['assistance.]({{site.baseurl}}/support_contact/)

### Accès à l'éditeur par glisser-déposer

Pour la plupart des utilisateurs de Braze, l'éditeur par glisser-déposer devrait se charger. Toutefois, si vous utilisez un VPN ou si vous êtes derrière un pare-feu, il se peut que vous deviez autoriser la liste d'un domaine. Contactez votre administrateur informatique pour vérifier que `*.bz-rndr.com` est bien sur la liste des autorisations.

L'éditeur peut rencontrer des problèmes de chargement pour les raisons suivantes :

- **Erreur transitoire :** Il s'agit de défaillances temporaires qui peuvent affecter la connectivité, la communication ou le transfert de données. Heureusement, ils se résolvent généralement d'eux-mêmes sans nécessiter d'intervention significative, car ils sont souvent causés par des conditions éphémères et n'indiquent pas de problèmes systémiques.
- **Erreur majeure :** Il peut s'agir d'un problème d'infrastructure ou de produit sous-jacent.  Vous pouvez consulter notre [page sur l'état du système Braze](https://braze.statuspage.io/), car nous sommes probablement au courant de la situation et travaillons activement à la résoudre.

{% alert important %}
Si vous rencontrez toujours des problèmes, [ouvrez un ticket d'assistance.]({{site.baseurl}}/user_guide/administrative/access_braze/support/) Avant de le faire, vérifiez que votre administrateur informatique a confirmé que `*.bz-rndr.com` est inscrit sur la liste d'autorisation de votre côté.
{% endalert %}

### Accéder à l'apprentissage de Braze

Si vous rencontrez des problèmes pour vous connecter à Braze Learning et que vous vous retrouvez bloqué dans une boucle qui vous redirige vers le tableau de bord, procédez comme suit :

1. Si vous avez plusieurs comptes Braze, le fait de vous connecter deux fois avec le mauvais compte vous renverra au tableau de bord de Braze. Confirmez que vous vous connectez au bon compte. 
2. Si vous avez un bloqueur de publicité, vérifiez qu'il est désactivé. Il peut bloquer les cookies nécessaires à la fonctionnalité d'authentification unique.
3. Allez dans Paramètres de l'entreprise > Paramètres de sécurité et vérifiez que l'authentification unique (SSO) est activée.
4. Confirmez que le profil utilisateur de votre tableau de bord comprend un nom et un prénom. L'absence de nom de famille peut perturber le processus d'identification.
5. Accédez à la formation Braze à partir de votre tableau de bord en allant dans **Support** > **Formation Braze**. 
6. Si le problème persiste, envisagez de recréer votre compte. Les utilisateurs qui ont accédé à Braze Learning pendant la phase d'essai gratuite peuvent avoir des difficultés à y accéder maintenant.

### Problèmes d'authentification à deux facteurs (2FA)

Si un utilisateur rencontre des problèmes avec l'authentification à deux facteurs (2FA) et ne peut pas accéder au tableau de bord de Braze, cela peut être dû à plusieurs raisons. Le plus souvent, ils peuvent ne plus avoir accès au numéro de téléphone enregistré ou à l'appareil sur lequel l'appli Authy est installée.

Un administrateur doit réinitialiser le 2FA pour l'utilisateur concerné en procédant comme suit : 

1. Allez dans **Gérer les utilisateurs**.
2. Sélectionnez **Modifier l** 'utilisateur pour l'utilisateur qui rencontre des problèmes avec 2FA.
3. Choisissez l'option Réinitialiser 2FA.
4. Confirmez la réinitialisation 2FA lorsque vous y êtes invité.
5. Si la réinitialisation ne résout pas immédiatement le problème, effacez vos cookies et votre cache.

Braze ne peut pas réinitialiser 2FA au nom des utilisateurs pour des raisons de sécurité, donc si l'administrateur n'est pas en mesure de réinitialiser 2FA, un ticket d'assistance doit être créé.

#### Considérations

- Si le 2FA est appliqué au niveau de l'entreprise : Après la réinitialisation, l'utilisateur sera invité à configurer à nouveau son 2FA lors de sa prochaine connexion.
- Si le 2FA n'est pas appliqué au niveau de l'entreprise : L'utilisateur se connectera au tableau de bord sans avoir besoin de configurer à nouveau 2FA. S'ils souhaitent activer la fonction 2FA, ils peuvent le faire dans les paramètres du compte.

{% alert note %}
Ce processus de réinitialisation s'applique également aux utilisateurs dont le compte a été verrouillé parce qu'ils ont demandé trop de jetons au cours de la dernière heure.
{% endalert %}