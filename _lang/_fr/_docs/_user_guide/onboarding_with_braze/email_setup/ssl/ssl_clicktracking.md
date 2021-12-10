---
nav_title: Suivi des clics SSL
article_title: Suivi des clics SSL
page_order: 9
page_type: Référence
description: "Cet article de référence couvre le suivi des clics SSL, les meilleures pratiques et la façon de commencer."
channel: Email
---

# Suivi des clics SSL

Un Socket Layer (SSL) sécurisé crypte une URL avec HTTPS au lieu du HTTP moins sécurisé. Les clients de Braze peuvent configurer leurs liens et leurs domaines pour appliquer les certificats SSL. Ces certificats, similaires à SPM et DKIM pour l'authentification par e-mail, sont des assurances que des liens dans vos courriels envoient vos utilisateurs à des emplacements réputés, et non des sites Web malveillants. Bien que non requis, les certificats SSL deviennent rapidement la norme et sont fortement recommandés pour s'assurer que les liens et les images s'affichent correctement.

## Comment puis-je commencer ?

1. Vous devez contacter un COM ou un CSM pour lancer une configuration complète de l'e-mail Braze.
2. Braze fournira des enregistrements DNS à ajouter à votre registre de domaine.
3. Braze vérifiera si des enregistrements ont été ajoutés correctement à votre registre.
4. Vous allez ensuite sélectionner un CDN et obtenir des certificats SSL auprès d'un fournisseur tiers.
5. Vous allez configurer votre CDN. Veuillez noter que Braze ne sera pas en mesure de vous aider à résoudre les problèmes de configuration CDN. Veuillez contacter votre fournisseur CDN pour obtenir de l'aide.
6. Enfin, contactez votre COM ou CSM pour activer SSL.

## Qu'est-ce qu'un CDN, et pourquoi en ai-je besoin?

Un réseau de distribution de contenu (CDN) est une plate-forme de serveurs qui permet d'assurer des temps de chargement rapides de contenu de haute qualité sur plusieurs supports tout en gérant les certificats de sécurité.

Au Brésil, pour effectuer un clic et ouvrir le suivi, nos partenaires de livraison transforment les liens en utilisant un sous-domaine de marque, et le CDN applique le certificat SSL à ces liens nouvellement transformés. Souvent, nos partenaires de livraison sont tenus de présenter des certificats valides et fiables au navigateur de votre destinataire de courrier électronique pour que les liens et les images s'affichent correctement. Parce que Braze ne peut pas demander ou gérer de tels certificats, cela doit être configuré à votre fin via un CDN.

Ci-dessous nous avons décrit et lié à des ressources de partenaires du CDN pertinentes pour faciliter ce processus.

{% alert important %}
Veuillez noter que la configuration CDN suit toujours après avoir validé vos enregistrements DNS par Braze. Si vous n'avez pas encore initié cette étape, contactez votre COM ou votre CSM pour plus d'informations sur la façon de commencer.
{% endalert %}

{% alert note %}
Si vous ne pouvez pas ou ne souhaitez pas utiliser les CDN listés ci-dessus lors de la configuration de SSL pour cliquer et ouvrir le suivi, vous pouvez configurer une configuration SSL personnalisée. Notez que les CDN alternatifs ou mandataires personnalisés peuvent entraîner une configuration plus complexe et nuancée. Consultez la documentation [Sendgrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) et [Sparkpost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) sur ce sujet.
{% endalert %}

### Ressources CDN

Listé ci-dessous sont des guides étape par étape écrits par Sendgrid et Sparkpost sur la façon de configurer certains CDN. Bien que votre CDN spécifique ne soit pas listé ci-dessous, vous devez vous assurer que votre CDN a la possibilité d'appliquer des certificats SSL.

{% alert important %}
Braze ne pourra pas vous aider à résoudre votre configuration CDN. Vous devez contacter votre fournisseur de CDN pour aider à résoudre le problème de la configuration de votre CDN.
{% endalert %}

| Tutoriels pas à pas Sendgrid                                                                                                                                                                                                                                                                                                                                                                                                                                | Tutoriels pas à pas Sparkpost                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AWS Cloudfront](https://sendgrid.com/docs/ui/sending-email/universal-links/#setting-up-universal-links-using-cloudfront)<br>[Fusée nuageuse](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Rapidement](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#aws-create)<br>[CloudFlare](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Cloudfront](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/)<br>[Rapidement](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#gcp-create)<br>[Microsoft Azure](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#azure-create) |

### Dépannage CDN

Pendant que la configuration CDN, les certificats et les problèmes de proxy doivent être traités avec votre CDN sélectionné, nous offrons quelques conseils de dépannage de base pour identifier où votre configuration de suivi des clics SSL peut échouer.

{% tabs %}
{% tab Domain Registry %}

#### Vérifier les problèmes de registre de domaine

Une commande de fouille peut vous dire si vous pointez votre suivi de lien sur le CDN. Cela peut être fait via le terminal en exécutant `fouiller le domaine CNAME link_tracking_subdomain`.

Une fois que la commande est exécutée, sous `ANSWER SECTION` elle devrait lister où votre CNAME est pointé. Si cela pointe vers le fournisseur de service de messagerie (Sendgrid ou Sparkpost) et non vers votre CDN, vous devez reconfigurer votre registre de domaine pour qu'il pointe vers votre CDN.

{% endtab %}
{% tab CDN %}

#### Vérifier les problèmes de CDN

Si vos liens de courriel en direct commencent à se briser pendant l'installation, cela signifie souvent que vous avez pointé votre DNS vers votre CDN sans qu'il soit correctement configuré. Cela apparaît souvent comme une erreur de "Mauvais lien".

Veuillez contacter votre fournisseur de CDN et consulter leur documentation pour aider à résoudre votre configuration CDN.

{% endtab %}
{% tab HTTP Messages Persisting %}

#### Vérifier si SSL est activé par Braze

Si vous avez terminé votre configuration SSL et que vous voyez toujours vos liens apparaître comme HTTP et non HTTPS, contactez votre Braze COM ou CSM et assurez-vous que SSL a été activé par Braze. Le protocole SSL ne peut être activé par Braze qu'une fois que tous les aspects de votre configuration SSL sont terminés.

{% endtab %}
{% endtabs %}