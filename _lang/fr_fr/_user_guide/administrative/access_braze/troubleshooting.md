---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de Braze Access
page_order: 8
page_type: reference
description: "Cet article vous guide dans la résolution des problèmes que vous pouvez rencontrer lorsque vous essayez d'accéder à Braze."

---

# Résolution des problèmes d'accès à Braze

> Cet article vous aide à résoudre les problèmes que vous pouvez rencontrer lorsque vous essayez d'accéder à Braze.

## Verrouillage du compte

Vous n'avez plus accès à votre compte Braze ? Pas de panique ! Nous pouvons vous aider à vous réinsérer.	

Le message d'erreur que vous recevez vous permet de savoir quel type de blocage vous rencontrez :	

- [Je vois une erreur concernant mon mot de passe.](#password-error)	
- [Je ne vois pas d'erreur, mais Braze ne me laisse toujours pas entrer.](#instance-error)	
- [Je vois une erreur concernant la suspension du compte.](#account-suspension)	

### Erreur de mot passe

La sécurité de votre compte est importante pour nous, c'est pourquoi des mots passe sont nécessaires pour vous connecter à votre compte Braze.	
- Vérifiez que vous vous connectez à la bonne [instance du tableau de bord de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Vérifiez auprès de votre administrateur de compte ou de votre gestionnaire de compte Braze.	
- Votre mot de passe a peut-être expiré, vous devez donc [le réinitialiser]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	
- Si vous utilisez un service d'[authentification unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), vérifiez auprès de votre administrateur de compte que l'inscription a été effectuée correctement.	
- Si votre entreprise utilise plusieurs instances de Braze, il se peut que vous utilisiez un e-mail incorrect pour vous connecter.  	

En cas de doute, vous pouvez toujours [réinitialiser votre mot de passe]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	

### Erreur d'instance

Si vous utilisez la même machine que vous utilisez habituellement pour vous connecter, Braze devrait automatiquement détecter la bonne instance. Toutefois, si ce n'est pas le cas ou si vous vous connectez pour la première fois, nous vous recommandons de prendre en compte les éléments suivants :	

- Vérifiez que vous vous connectez à la bonne [instance du tableau de bord de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Vérifiez auprès de votre administrateur de compte ou de votre gestionnaire de compte Braze.
- Si votre entreprise utilise plusieurs instances de Braze, il se peut que vous utilisiez un e-mail incorrect pour vous connecter.	

### Suspension du compte	

Cela n'arrive pas très souvent, mais nous prenons très au sérieux les suspensions et les suppressions de comptes. Si vous rencontrez cette erreur, nous vous recommandons de contacter l'administrateur Braze de votre entreprise, le gestionnaire de compte Braze ou [Support][support].

## Le tableau de bord de Braze ne se charge pas ou ne fonctionne pas comme prévu

Testez d'abord si le tableau de bord se charge dans un autre navigateur. Si le problème ne persiste pas dans un autre navigateur, essayez ce qui suit :

- **Relancez le tableau de bord :** Déconnectez-vous, quittez votre navigateur, puis essayez de vous connecter à votre tableau de bord.
- **Actualisez votre navigateur local :** [Effacez vos cookies et le cache de votre navigateur]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies), puis essayez à nouveau de vous connecter à votre tableau de bord.
- **Utilisez des plugins compatibles ou des outils tiers :** Les bloqueurs de publicité ou les logiciels de sécurité peuvent empêcher le chargement du tableau de bord de Braze. Testez-le en désactivant un bloqueur de publicité, puis en vous connectant à votre tableau de bord de Braze.
        \- Vous pouvez également consulter les journaux de la console de votre navigateur. Les erreurs liées à `ERR_BLOCKED_BY_CLIENT` peuvent indiquer que le bloc de contenu est bloqué par un bloqueur de publicité.
- **Vérifiez la qualité de votre connexion :** Il se peut que la qualité de votre connexion soit mauvaise. Essayez de vous connecter à votre tableau de bord de Braze sur un autre appareil.
- **Confirmez que vous accédez au bon cluster :** Assurez-vous que vous vous connectez au cluster attribué à votre entreprise. Par exemple, vous pouvez être affecté à US-03, mais vous vous connectez à US-01.
- **Mettez à jour votre navigateur :** Mettez à jour votre navigateur avec le dernier [navigateur pris en charge]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers), puis essayez de vous connecter à votre tableau de bord.

Si le problème se produit dans tous les navigateurs, essayez les solutions suivantes :

- **Vérifiez votre connexion réseau :** Essayez de désactiver votre VPN, si possible, ou désactivez et réactivez votre connexion réseau.
- **Redémarrez votre appareil :** Essayez de vous connecter à votre tableau de bord de Braze après avoir redémarré votre appareil.

Si vous avez résolu les problèmes précédents et que votre tableau de bord ne se charge toujours pas ou ne fonctionne toujours pas comme prévu, contactez l ['assistance.]({{site.baseurl}}/braze_support/)

## L'utilisateur n'appartient à aucun espace de travail

Vérifiez-le en allant dans **Paramètres** > **Utilisateurs de l'entreprise** et en vérifiant les autorisations de l'utilisateur au niveau de l'espace de travail. Ajoutez les espaces de travail nécessaires à **Espaces de travail**.

## Résolution des problèmes en tant que nouvel utilisateur

Si vous êtes un nouvel utilisateur de Braze et que vous avez des difficultés à vous connecter ou à accéder à votre compte pour la première fois, suivez ces étapes pour résoudre les problèmes les plus courants :

### Je n'ai jamais reçu l'e-mail de bienvenue

- Vérifiez votre dossier spam : Confirmez que l'e-mail d'activation du compte n'a pas été filtré dans votre dossier spam ou courrier indésirable.
- Vérifiez votre adresse e-mail : Demandez à votre administrateur de vérifier l'adresse e-mail associée à votre nouveau compte Braze pour confirmer qu'elle est correcte.
- Politiques informatiques : Confirmez auprès de votre équipe informatique qu'il n'existe pas de politiques en place susceptibles d'empêcher la réception de l'e-mail d'activation.

### J'ai reçu l'e-mail, mais je ne parviens pas à configurer l'authentification à deux facteurs (2FA).

- Réinitialisez 2FA : Si vous avez des difficultés à configurer 2FA, votre administrateur peut réinitialiser 2FA pour votre compte utilisateur dans les paramètres.
- Ajoutez à nouveau l'utilisateur : Si les problèmes persistent, l'administrateur peut supprimer votre compte utilisateur du tableau de bord et vous réinscrire. Cela permet de créer un utilisateur avec les mêmes détails.

Si le problème persiste après ces étapes, contactez le [service d'assistance]({{site.baseurl}}/braze_support/) pour obtenir de l'aide.