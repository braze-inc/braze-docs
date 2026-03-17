---
nav_title: Veuillez accéder à votre compte.
article_title: Accédez à votre compte
page_order: 0
page_type: reference
description: "Cet article explique comment obtenir votre compte Braze, comment vous connecter une fois l'accès accordé et comment réinitialiser votre mot de passe Braze."

---

# Veuillez accéder à votre compte.

> Cet article explique comment obtenir votre compte Braze, comment vous connecter après avoir obtenu un accès, et comment résoudre les problèmes d'accès à votre tableau de bord et de performance de votre tableau de bord.

Si vous êtes le premier utilisateur Braze de votre entreprise et vous connectez pour la première fois, vous recevrez un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre e-mail et de vous connecter le premier jour de votre contrat.

Après avoir confirmé votre compte, vous pouvez ajouter des utilisateurs supplémentaires à partir de la page [Utilisateurs de l'entreprise de]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) votre tableau de bord. Tous les utilisateurs recevront un e-mail leur demandant de confirmer leur compte après avoir été ajoutés.

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

## Accès à plusieurs tableaux de bord de Braze

Braze ne permet pas d'enregistrer la même adresse e-mail pour plusieurs utilisateurs du tableau de bord dans le même cluster (par exemple, si vous avez deux tableaux de bord sur US-01). Vous pouvez utiliser le même e-mail pour créer des comptes sur différents clusters (par exemple, si vous disposez d'un tableau de bord sur US-01 et d'un autre sur US-05). Si vous avez besoin d'accéder à plusieurs tableaux de bord de Braze dans le même cluster, vous pouvez procéder comme suit :

### Utiliser des alias d'e-mail

Si votre fournisseur de e-mail est Gmail, vous pouvez créer des alias en ajoutant le`+`signe @ suivi de n'importe quel texte à votre adresse e-mail. Par exemple :
- **E-mail original :** `rocky@gmail.com`
- **Adresse e-mail alias :** `rocky+1@gmail.com`

Les deux adresses d'e-mail dirigeront les courriels vers la même boîte de réception, mais Braze les reconnaîtra comme des comptes distincts lorsque vous vous connecterez.

### Veuillez créer des alias distincts auprès d'autres fournisseurs.

Si votre fournisseur d'e-mail ne prend pas en charge`+`les alias, vous pouvez tout de même créer des alias distincts, par exemple en configurant`rocky@braze.com`le transfert vers`rocky.lotito@braze.com` . Cela permet à plusieurs adresses d'être redirigées vers la même boîte de réception tout en étant reconnues comme des e-mails distincts par Braze.

### Faire appel à des développeurs multi-entreprises

La fonctionnalité multi-entreprises pour les développeurs permet le partage d'un seul compte utilisateur entre plusieurs entreprises. Les utilisateurs peuvent basculer entre différents tableaux de bord d'entreprise à partir du menu de leur profil utilisateur.

Si vous disposez d'un système SSO et souhaitez configurer des développeurs multi-entreprises, il est nécessaire d'activer un ID d'entité SAML personnalisé en configurant une intégration d'authentification unique (SSO) SAML personnalisée. Veuillez suivre les étapes décrites dans la [section Identifiant initié par le fournisseur de services (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), mais en appliquant les modifications suivantes :
- Veuillez modifier **l'ID d'entité** en`braze_dashboard_<companyID>`  pour chaque intégration de tableau de bord.
- Veuillez contacter votre gestionnaire de la satisfaction client ou votre gestionnaire de compte afin d'activer le `saml_sso_custom_entity_id`commutateur de fonctionnalités pour chaque tableau de bord.

### Considérations relatives à l'authentification unique (SSO)

Si vous utilisez l'authentification unique (SSO), veuillez noter que le fait d'avoir plusieurs adresses e-mail différentes peut entraîner des complications. Veuillez vérifier que vos paramètres SSO sont correctement configurés afin d'éviter tout problème d'accès.

## Résolution des problèmes

### Réinitialisation de votre mot de passe

Pour réinitialiser votre mot de passe, sélectionnez le lien **Mot de passe oublié ?** sur la page d'identification du tableau de bord. Vous serez invité à saisir votre e-mail pour recevoir un lien vous permettant de réinitialiser votre mot de passe.

![Identifiant au tableau de bord avec l'invite « Mot de passe oublié ? ».]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Effacer la mémoire cache de votre navigateur et les cookies

Si vous rencontrez des problèmes avec les performances du tableau de bord, par exemple si votre tableau de bord ou la liste des performances des segments ne se charge pas, essayez d'effacer le cache et les cookies de votre navigateur en suivant les étapes indiquées pour votre navigateur respectif.

{% alert important %}
En supprimant les cookies, vous vous déconnectez, ce qui entraîne la perte des travaux non sauvegardés.
{% endalert %}

- [Veuillez effacer le cache et& les cookies dans Chrome.](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Effacer les cookies dans Safari sur Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Effacer les cookies et les données de site dans Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Supprimer tous les cookies dans Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Si la suppression du cache et des cookies de votre navigateur ne résout pas vos problèmes, contactez l ['assistance.]({{site.baseurl}}/support_contact/)

### Accès à l'éditeur par glisser-déposer

Pour la plupart des utilisateurs professionnels, l'éditeur par glisser-déposer devrait se charger. Toutefois, si vous utilisez un VPN ou si vous êtes derrière un pare-feu, il se peut que vous deviez autoriser la liste d'un domaine. Contactez votre administrateur informatique pour vérifier que `*.bz-rndr.com` est bien sur la liste des autorisations.

L'éditeur peut rencontrer des problèmes de chargement pour les raisons suivantes :

- **Erreur transitoire :** Il s'agit de défaillances temporaires qui peuvent affecter la connectivité, la communication ou le transfert de données. Heureusement, ils se résolvent généralement d'eux-mêmes sans nécessiter d'intervention significative, car ils sont souvent causés par des conditions éphémères et n'indiquent pas de problèmes systémiques.
- **Erreur majeure :** Il peut s'agir d'un problème d'infrastructure ou de produit sous-jacent.  Vous pouvez consulter notre [page sur l'état du système Braze](https://braze.statuspage.io/), car nous sommes probablement au courant de la situation et travaillons activement à la résoudre.

{% alert important %}
Si vous rencontrez toujours des problèmes, [ouvrez un ticket d'assistance.]({{site.baseurl}}/user_guide/administrative/access_braze/support/) Avant de le faire, vérifiez que votre administrateur informatique a confirmé que `*.bz-rndr.com` est inscrit sur la liste d'autorisation de votre côté.
{% endalert %}

### Accéder à Braze Learning

Si vous rencontrez des difficultés pour vous connecter à Braze Learning et que vous êtes redirigé de manière répétée vers le tableau de bord de Braze, veuillez suivre les étapes suivantes :

1. Si vous disposez de plusieurs comptes Braze, une connexion incorrecte à deux reprises vous redirigera vers le tableau de bord de Braze. Veuillez vérifier que vous vous connectez au bon compte. 
2. Si vous utilisez un bloqueur de publicités, veuillez vérifier qu'il est désactivé. Cela pourrait bloquer les cookies nécessaires à la fonctionnalité d'authentification unique.
3. Veuillez vous rendre dans Paramètres de l'entreprise > Paramètres de sécurité et vérifier que l'authentification unique (SSO) est activée.
4. Veuillez vérifier que votre profil utilisateur du tableau de bord comprend à la fois votre prénom et votre nom. L'absence de nom de famille peut perturber le processus d'identifiant.
5. Accédez à Braze Learning depuis votre tableau de bord en vous rendant dans **Assistance** > **Braze Learning**. 
6. Si les problèmes persistent, veuillez envisager de recréer votre compte. Les utilisateurs qui ont accédé à Braze Learning pendant la phase d'essai gratuit pourraient rencontrer des difficultés pour y accéder actuellement.

### Problèmes liés à l'authentification à deux facteurs (2FA)

Si un utilisateur rencontre des difficultés avec l'authentification à deux facteurs (2FA) et ne parvient pas à accéder au tableau de bord de Braze, cela peut être dû à plusieurs raisons. Le plus souvent, ils n'ont plus accès au numéro de téléphone enregistré ou à l'appareil sur lequel l'application Authy est installée.

Un administrateur doit réinitialiser la 2FA pour l'utilisateur concerné en procédant comme suit : 

1. Veuillez vous rendre dans **la section Gestionnaire des utilisateurs**.
2. Veuillez sélectionner **Modifier l'utilisateur** pour l'utilisateur rencontrant des difficultés avec l'authentification à deux facteurs.
3. Veuillez sélectionner l'option permettant de réinitialiser la 2FA.
4. Veuillez confirmer la réinitialisation de la 2FA lorsque vous y êtes invité.
5. Si la réinitialisation ne résout pas immédiatement le problème, veuillez effacer vos cookies et votre cache.

Pour des raisons de sécurité, Braze ne peut pas réinitialiser la 2FA au nom des utilisateurs. Par conséquent, si l'administrateur n'est pas en mesure de réinitialiser la 2FA, veuillez créer un ticket d'assistance.

#### Considérations

- Si la 2FA est appliquée au niveau de l'entreprise : Après la réinitialisation, Braze invite l'utilisateur à reconfigurer son authentification à deux facteurs lors de sa prochaine connexion.
- Si la 2FA n'est pas appliquée au niveau de l'entreprise : L'utilisateur pourra se connecter au tableau de bord sans avoir à reconfigurer l'authentification à deux facteurs. Si vous souhaitez activer la 2FA, vous pouvez le faire dans les paramètres du compte.

{% alert note %}
Ce processus de réinitialisation s'applique également aux utilisateurs dont l'accès au compte a été bloqué en raison d'une demande excessive de jetons au cours de la dernière heure.
{% endalert %}