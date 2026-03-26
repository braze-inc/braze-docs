---
nav_title: Accéder à votre compte
article_title: Accéder à votre compte
page_order: 0
page_type: reference
description: "Cet article explique comment obtenir votre compte Braze, comment vous connecter une fois l'accès accordé et comment réinitialiser votre mot de passe Braze."

---

# Accéder à votre compte

> Cet article explique comment obtenir votre compte Braze, comment vous connecter après avoir obtenu un accès, et comment résoudre les problèmes d'accès et de performance de votre tableau de bord.

Si vous êtes le premier utilisateur Braze de votre entreprise et que vous vous connectez pour la première fois, vous recevrez un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre e-mail et de vous connecter le premier jour de votre contrat.

Après avoir confirmé votre compte, vous pouvez ajouter des utilisateurs supplémentaires à partir de la page [Utilisateurs de l'entreprise]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) de votre tableau de bord. Tous les utilisateurs recevront un e-mail leur demandant de confirmer leur compte après avoir été ajoutés.

Si vous n'êtes pas le premier utilisateur du compte Braze de votre entreprise, contactez l'administrateur du compte Braze de votre entreprise et demandez-lui de créer votre compte. Vous recevrez ensuite un e-mail de bienvenue de `@alerts.braze.com` vous demandant de confirmer votre e-mail et de vous connecter.

## Connexion

Voyons comment vous connecter, que ce soit la première ou la millionième fois ! Si vous êtes le premier utilisateur de votre entreprise, suivez les directives de la section précédente. Si ce n'est pas le cas, vous pouvez vous connecter après que l'administrateur Braze de votre entreprise a créé votre compte.

Vous pouvez soit vous connecter à partir du site d'accueil [Braze.com](https://www.braze.com), soit utiliser l'URL de votre tableau de bord correspondant à votre [instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) spécifique. Pour vous faciliter la tâche, Braze propose plusieurs options d'authentification unique (SSO), notamment :

* [Authentification unique (SSO) SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [Approvisionnement SAML juste-à-temps]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
Une fois connecté à Braze via SSO, vous ne pouvez plus utiliser votre mot de passe pour accéder au tableau de bord.
{% endalert %}

## Navigateurs pris en charge

Le tableau de bord de Braze prend en charge les navigateurs suivants :
- Chrome (version 87 ou plus récente)
- Firefox (version 85 ou plus récente)
- Safari (version 15.4 ou plus récente)
- Edge (version 87 ou plus récente)

Si votre tableau de bord de Braze indique une erreur inattendue et que l'outil de console de votre navigateur affiche l'erreur `ReferenceError: structuredClone is not defined`, votre navigateur est obsolète. Si cette erreur se reproduit, désinstallez et réinstallez votre navigateur.

## Accéder à plusieurs tableaux de bord de Braze

Braze ne permet pas d'enregistrer la même adresse e-mail pour plusieurs utilisateurs du tableau de bord dans le même cluster (par exemple, si vous avez deux tableaux de bord sur US-01). Vous pouvez utiliser le même e-mail pour créer des comptes sur différents clusters (par exemple, si vous disposez d'un tableau de bord sur US-01 et d'un autre sur US-05). Si vous avez besoin d'accéder à plusieurs tableaux de bord de Braze dans le même cluster, voici les options possibles :

### Utiliser des alias d'e-mail

Si votre fournisseur d'e-mail est Gmail, vous pouvez créer des alias en ajoutant le signe `+` suivi de n'importe quel texte à votre adresse e-mail. Par exemple :
- **E-mail original :** `rocky@gmail.com`
- **E-mail alias :** `rocky+1@gmail.com`

Les deux adresses e-mail dirigeront les messages vers la même boîte de réception, mais Braze les reconnaîtra comme des comptes distincts lors de la connexion.

### Créer des alias distincts auprès d'autres fournisseurs

Si votre fournisseur d'e-mail ne prend pas en charge les alias avec `+`, vous pouvez tout de même créer des alias distincts, par exemple en configurant `rocky@braze.com` pour transférer les messages vers `rocky.lotito@braze.com`. Cela permet à plusieurs adresses d'être redirigées vers la même boîte de réception tout en étant reconnues comme des e-mails distincts par Braze.

### Utiliser la fonctionnalité développeurs multi-entreprises

La fonctionnalité développeurs multi-entreprises permet de partager un seul compte utilisateur entre plusieurs entreprises. Les utilisateurs peuvent basculer entre différents tableaux de bord d'entreprise à partir du menu de leur profil utilisateur.

Si vous disposez d'un système SSO et souhaitez configurer des développeurs multi-entreprises, vous devez activer un ID d'entité SAML personnalisé en configurant une intégration d'authentification unique (SSO) SAML personnalisée. Suivez les étapes décrites dans [Connexion initiée par le fournisseur de services (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), en appliquant les modifications suivantes :
- Modifiez l'**ID d'entité** en `braze_dashboard_<companyID>` pour chaque intégration de tableau de bord.
- Contactez votre Customer Success Manager ou Account Manager pour activer le commutateur de fonctionnalité `saml_sso_custom_entity_id` pour chaque tableau de bord.

### Considérations relatives à l'authentification unique (SSO)

Si vous utilisez l'authentification unique (SSO), sachez que le fait d'avoir plusieurs adresses e-mail différentes peut entraîner des complications. Vérifiez que vos paramètres SSO sont correctement configurés afin d'éviter tout problème d'accès.

## Résolution des problèmes

### Réinitialiser votre mot de passe

Pour réinitialiser votre mot de passe, sélectionnez le lien **Mot de passe oublié ?** sur la page de connexion du tableau de bord. Vous serez invité à saisir votre e-mail pour recevoir un lien de réinitialisation de votre mot de passe.

![Connexion au tableau de bord avec l'invite « Mot de passe oublié ? ».]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Vider le cache et les cookies de votre navigateur

Si vous rencontrez des problèmes de performance du tableau de bord, par exemple si votre tableau de bord ou la liste de performance des segments ne se charge pas, essayez de vider le cache et les cookies de votre navigateur en suivant les étapes correspondant à votre navigateur.

{% alert important %}
La suppression des cookies vous déconnectera, ce qui entraînera la perte des travaux non enregistrés.
{% endalert %}

- [Vider le cache et les cookies dans Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Effacer les cookies dans Safari sur Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Effacer les cookies et les données de site dans Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Supprimer tous les cookies dans Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

Si la suppression du cache et des cookies de votre navigateur ne résout pas vos problèmes, contactez l'[Assistance]({{site.baseurl}}/support_contact/).

### « Veuillez actualiser la page » ou « Erreur inattendue » lors de la navigation dans le tableau de bord

Cette erreur peut apparaître lorsqu'un utilisateur de l'entreprise n'appartient à aucun espace de travail. Pour résoudre ce problème :

1. Rendez-vous sur la page [Utilisateurs de l'entreprise]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/).
2. Vérifiez si l'utilisateur a été ajouté à un espace de travail.
3. S'il ne fait partie d'aucun espace de travail, ajoutez-le et affectez-lui les autorisations appropriées.
4. Demandez à l'utilisateur d'actualiser son tableau de bord.
5. Si le problème persiste, contactez l'[Assistance]({{site.baseurl}}/support_contact/).

### Accéder à l'éditeur par glisser-déposer

Pour la plupart des utilisateurs, l'éditeur par glisser-déposer devrait se charger sans problème. Toutefois, si vous utilisez un VPN ou êtes derrière un pare-feu, vous devrez peut-être ajouter un domaine à votre liste d'autorisation. Contactez votre administrateur informatique pour vérifier que `*.bz-rndr.com` est bien autorisé.

L'éditeur peut rencontrer des problèmes de chargement pour les raisons suivantes :

- **Erreur transitoire :** Il s'agit de défaillances temporaires pouvant affecter la connectivité, la communication ou le transfert de données. Elles se résolvent généralement d'elles-mêmes sans intervention particulière, car elles sont souvent causées par des conditions éphémères et n'indiquent pas de problèmes systémiques.
- **Erreur majeure :** Il peut s'agir d'un problème d'infrastructure ou de produit sous-jacent. Vous pouvez consulter notre [page d'état du système Braze](https://braze.statuspage.io/), car nous sommes probablement au courant de la situation et travaillons activement à la résoudre.

{% alert important %}
Si vous rencontrez toujours des problèmes, [ouvrez un ticket d'assistance]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Avant cela, vérifiez que votre administrateur informatique a confirmé que `*.bz-rndr.com` est bien autorisé de votre côté.
{% endalert %}

### Accéder à Braze Learning

Si vous rencontrez des difficultés pour vous connecter à Braze Learning et que vous êtes redirigé en boucle vers le tableau de bord, suivez les étapes ci-dessous :

1. Si vous disposez de plusieurs comptes Braze, une connexion avec le mauvais compte à deux reprises vous redirigera vers le tableau de bord de Braze. Vérifiez que vous vous connectez au bon compte.
2. Si vous utilisez un bloqueur de publicités, vérifiez qu'il est désactivé. Il pourrait bloquer les cookies nécessaires au fonctionnement de l'authentification unique.
3. Rendez-vous dans Paramètres de l'entreprise > Paramètres de sécurité et vérifiez que l'authentification unique (SSO) est activée.
4. Vérifiez que votre profil utilisateur du tableau de bord comprend à la fois un prénom et un nom. L'absence de nom de famille peut perturber le processus de connexion.
5. Accédez à Braze Learning depuis votre tableau de bord en vous rendant dans **Assistance** > **Braze Learning**.
6. Si les problèmes persistent, envisagez de recréer votre compte. Les utilisateurs ayant accédé à Braze Learning pendant la phase d'essai gratuit peuvent rencontrer des difficultés pour y accéder maintenant.

### Problèmes liés à l'authentification à deux facteurs (2FA)

Si un utilisateur rencontre des difficultés avec l'authentification à deux facteurs (2FA) et ne parvient pas à accéder au tableau de bord de Braze, cela peut être dû à plusieurs raisons. Le plus souvent, il n'a plus accès au numéro de téléphone enregistré ou à l'appareil sur lequel l'application Authy est installée.

Un administrateur doit réinitialiser la 2FA pour l'utilisateur concerné en procédant comme suit :

1. Rendez-vous dans **Gérer les utilisateurs**.
2. Sélectionnez **Modifier l'utilisateur** pour l'utilisateur rencontrant des difficultés avec la 2FA.
3. Choisissez l'option de réinitialisation de la 2FA.
4. Confirmez la réinitialisation de la 2FA lorsque vous y êtes invité.
5. Si la réinitialisation ne résout pas immédiatement le problème, videz vos cookies et votre cache.

Pour des raisons de sécurité, Braze ne peut pas réinitialiser la 2FA au nom des utilisateurs. Si l'administrateur n'est pas en mesure de réinitialiser la 2FA, créez un ticket d'assistance.

#### Considérations

- Si la 2FA est appliquée au niveau de l'entreprise : après la réinitialisation, Braze invite l'utilisateur à reconfigurer son authentification à deux facteurs lors de sa prochaine connexion.
- Si la 2FA n'est pas appliquée au niveau de l'entreprise : l'utilisateur pourra se connecter au tableau de bord sans avoir à reconfigurer la 2FA. S'il souhaite activer la 2FA, il peut le faire dans les paramètres du compte.

{% alert note %}
Ce processus de réinitialisation s'applique également aux utilisateurs dont l'accès au compte a été bloqué en raison d'un nombre excessif de demandes de jetons au cours de la dernière heure.
{% endalert %}