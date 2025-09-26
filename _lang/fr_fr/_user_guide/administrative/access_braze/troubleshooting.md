---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de Braze Access
page_order: 8
page_type: reference
description: "Cet article vous guide dans la résolution des problèmes que vous pouvez rencontrer lorsque vous essayez d'accéder à Braze."

---

# Résolution des problèmes d'accès à Braze

> Cet article vous aide à résoudre les problèmes que vous pouvez rencontrer lorsque vous essayez d'accéder à Braze.

## Compte verrouillé

Donc vous n’arrivez plus à rentrer sur votre compte Braze mais pas soucis ! Nous sommes là pour vous aider.	

Le message d’erreur que vous recevez vous informe sur le type de verrouillage de compte que vous avez :	

- [Je vois une erreur concernant mon mot de passe.](#password-error)	
- [Je ne vois pas d'erreur, mais Braze ne me laisse toujours pas entrer.](#instance-error)	
- [Je vois une erreur concernant la suspension du compte.](#account-suspension)	

### Erreur de mot de passe

La sécurité de votre compte est importante pour nous, donc des mots de passe sont requis pour vous connecter à votre compte Braze.	
- Vérifiez que vous vous connectez à la bonne [instance du tableau de bord de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Demandez à votre administrateur de compte ou votre gestionnaire de compte Braze pour être sûr.	
- Votre mot de passe a peut-être expiré, vous devez donc [le réinitialiser]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	
- Si vous utilisez un service d'[authentification unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/), vérifiez auprès de votre administrateur de compte que l'inscription a été effectuée correctement.	
- Si votre entreprise se trouve sur plusieurs instances de Braze, vous utilisez peut-être une adresse e-mail incorrecte pour vous connecter.  	

En cas de doute, vous pouvez toujours [réinitialiser votre mot de passe]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password).	

### Erreur d’instance

Si vous utilisez la machine avec laquelle vous vous connectez habituellement, Braze devrait détecter automatiquement l’instance correcte. Cependant, si ce n’est pas le cas ou si vous connectez pour la première fois, veuillez suivre les conseils suivants :	

- Vérifiez que vous vous connectez à la bonne [instance du tableau de bord de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances). Demandez à votre administrateur de compte ou votre gestionnaire de compte Braze pour être sûr.
- Si votre entreprise se trouve sur plusieurs instances de Braze, vous utilisez peut-être une adresse e-mail incorrecte pour vous connecter.	

### Compte suspendu	

Cela n’arrive pas très souvent, mais nous prenons très au sérieux les suspensions et les suppressions de comptes. Si vous rencontrez cette erreur, nous vous recommandons de contacter l'administrateur Braze de votre entreprise, le gestionnaire de compte Braze ou [Support][support].

## Le tableau de bord de Braze ne se charge pas ou ne fonctionne pas comme prévu

Testez d'abord si le tableau de bord se charge dans un autre navigateur. Si le problème ne persiste pas dans un autre navigateur, essayez ce qui suit :

- **Relancez le tableau de bord :** Déconnectez-vous, quittez votre navigateur, puis essayez de vous connecter à votre tableau de bord.
- **Actualisez votre navigateur local :** [Effacez vos cookies et le cache de votre navigateur]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#browser-cache-and-cookies), puis essayez à nouveau de vous connecter à votre tableau de bord.
- **Utilisez des plugins compatibles ou des outils tiers :** Les bloqueurs de publicité ou les logiciels de sécurité peuvent empêcher le chargement du tableau de bord de Braze. Testez ceci en désactivant un bloqueur de publicité, puis en vous connectant à votre tableau de bord de Braze.
        \- Vous pouvez également consulter les journaux de la console de votre navigateur. Les erreurs liées à `ERR_BLOCKED_BY_CLIENT` peuvent indiquer que le bloc de contenu est bloqué par un bloqueur de publicité.
- **Vérifiez la qualité de votre connexion :** Il se peut que la qualité de votre connexion soit mauvaise. Essayez de vous connecter à votre tableau de bord de Braze sur un autre appareil.
- **Confirmez que vous accédez au bon cluster :** Assurez-vous que vous vous connectez au cluster attribué à votre entreprise. Par exemple, vous pouvez être affecté à US-03, mais vous vous connectez à US-01.
- **Mettez à jour votre navigateur :** Mettez à jour votre navigateur avec le dernier [navigateur pris en charge]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#supported-browsers), puis essayez de vous connecter à votre tableau de bord.

Si le problème se produit dans tous les navigateurs, essayez les solutions suivantes :

- **Vérifiez votre connexion réseau :** Essayez de désactiver votre VPN, si possible, ou désactivez et réactivez votre connexion réseau.
- **Redémarrez votre appareil :** Essayez de vous connecter à votre tableau de bord de Braze après avoir redémarré votre appareil.

Si vous avez résolu les problèmes précédents et que votre tableau de bord ne se charge toujours pas ou ne fonctionne toujours pas comme prévu, contactez l ['assistance.]({{site.baseurl}}/braze_support/)


