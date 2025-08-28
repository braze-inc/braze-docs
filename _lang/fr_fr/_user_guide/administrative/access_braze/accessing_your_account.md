---
nav_title: Accéder à votre compte
article_title: Accéder à votre compte
page_order: 2
page_type: reference
description: "Cet article explique comment obtenir votre compte Braze, comment vous connecter une fois l'accès accordé et comment réinitialiser votre mot de passe Braze."

---

# Accéder à votre compte

> Cet article explique comment obtenir votre compte Braze, comment vous connecter après avoir obtenu un accès, et comment résoudre les problèmes d'accès à votre tableau de bord et de performance de votre tableau de bord.

Si vous êtes le premier utilisateur Braze de votre entreprise et vous connectez pour la première fois, vous recevrez un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre e-mail et de vous connecter le premier jour de votre contrat.

Après avoir confirmé votre compte, vous pouvez ajouter des utilisateurs supplémentaires à partir de la page [Utilisateurs de l'entreprise de]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) votre tableau de bord. Tous les utilisateurs recevront un e-mail leur demandant de confirmer leur compte après avoir été ajoutés.

Si vous n'êtes pas le premier utilisateur du compte Braze de votre entreprise, contactez l'administrateur du compte Braze de votre entreprise et demandez-lui de créer votre compte. Vous recevrez ensuite un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre e-mail et de vous connecter.

## Connexion

Voyons comment vous connecter, que ce soit la première ou la millionième fois ! Si vous êtes le premier utilisateur de votre entreprise, suivez les directives de la section précédente. Si ce n'est pas le cas, vous pouvez vous connecter après que l'administrateur Braze de votre entreprise a créé votre compte.

Vous pouvez soit vous connecter à partir du site d'accueil [Braze.com](https://www.braze.com), soit utiliser l'URL de votre tableau de bord qui correspond à votre [instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) spécifique. Pour vous faciliter la tâche, Braze propose plusieurs options d'authentification unique (SSO), notamment :

* [AUTHENTIFICATION UNIQUE (SSO) SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [Approvisionnement SAML juste-à-temps]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
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

## Résolution des problèmes

### Réinitialisation de votre mot de passe

Pour réinitialiser votre mot de passe, sélectionnez le lien **Mot de passe oublié ?** sur la page d'identification du tableau de bord. Vous serez invité à saisir votre e-mail pour recevoir un lien vous permettant de réinitialiser votre mot de passe.

![Tableau de bord identifiant avec l'invite "Mot de passe oublié".]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Effacer la mémoire cache de votre navigateur et les cookies

Si vous rencontrez des problèmes avec les performances du tableau de bord, par exemple si votre tableau de bord ou la liste des performances des segments ne se charge pas, essayez d'effacer le cache et les cookies de votre navigateur en suivant les étapes indiquées pour votre navigateur respectif.

{% alert important %}
En supprimant les cookies, vous vous déconnectez, ce qui entraîne la perte des travaux non sauvegardés.
{% endalert %}

- [Effacer le cache et les cookies dans Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
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

