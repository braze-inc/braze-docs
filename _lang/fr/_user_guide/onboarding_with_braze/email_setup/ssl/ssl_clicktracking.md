---
nav_title: Tracking du clic SSL
article_title: Tracking du clic SSL
page_order: 9
page_type: reference
description: "Le présent article de référence couvre le suivi des clics SSL, les bonnes pratiques et vous explique comment démarrer."
channel: email

---

# Tracking du clic SSL

Un Secured Socket Layer (SSL) chiffre une URL avec HTTPS plutôt que le HTTP moins sécurisé. Les clients de Braze peuvent configurer leurs liens et domaines pour appliquer des certificats SSL. Ces certificats, similaires à ceux du SPM et de DKIM pour l’authentification par e-mail, sont des assurances qui font que les liens dans vos e-mails envoient vos utilisateurs vers des emplacements réputés et non pas sur sites Web malveillants. Bien que cela ne soit pas nécessaire, les certificats SSL deviennent rapidement la norme et sont fortement recommandés pour garantir que les liens et les images s’affichent correctement.

## Comment commencer ?

1. Vous devez contacter votre gestionnaire du succès des clients Braze pour lancer une configuration d’e-mail Braze complète.
2. Braze fournit des enregistrements DNS à ajouter à votre registre de domaine.
3. Braze vérifie si les enregistrements ont été ajoutés correctement à votre registre.
4. Vous allez ensuite sélectionner un CDN et obtenir des certificats SSL auprès d’un fournisseur tiers. 
5. Vous configurerez votre CDN. Veuillez remarquer que Braze ne sera pas en mesure de dépanner la configuration CDN. Contactez votre fournisseur CDN pour obtenir de l’aide.
6. Enfin, contactez votre gestionnaire du succès des clients Braze pour activer le SSL.

## Qu’est-ce qu’un CDN et pourquoi en ai-je besoin ?

Un réseau de diffusion de contenu (CDN) est une plateforme de serveurs qui permet de garantir des temps de chargement rapides de contenus de haute qualité sur plusieurs supports tout en gérant les certificats de sécurité. 

Chez Braze, pour effectuer le suivi d’ouvertures et de clics, nos partenaires de livraison transforment les liens en utilisant un sous-domaine de marque, et le CDN applique le certificat SSL à ces liens nouvellement transformés. Souvent, nos partenaires de livraison sont tenus de présenter des certificats valides et approuvés au navigateur de votre destinataire d’e-mail pour les liens et les images à afficher correctement. Étant donné que Braze ne peut pas demander ou gérer de tels certificats, cela doit être configuré de votre côté par le biais d’un CDN. 

Dans les chapitres suivants, nous présentons et relions les ressources partenaires CDN pertinentes pour faciliter ce processus. 

{% alert important %}
Veuillez remarquer que la configuration CDN se fait toujours lorsque Braze a obtenu et validé vos enregistrements DNS. Si vous n’avez pas encore commencé cette étape, contactez votre gestionnaire du succès des clients pour plus d’informations sur la façon de commencer.
{% endalert %}

{% alert note %}
Si vous n’êtes pas en mesure d’utiliser les CDN répertoriés lors de la configuration de SSL pour le tracking de clic et ouvert, vous pouvez configurer une configuration SSL personnalisée. Veuillez remarquer que les CDN alternatifs ou les proxys personnalisés peuvent entraîner une configuration plus complexe et nuancée. Consultez la documentation [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/ "Adding a Custom SSL configuration") et [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/ "Using a Reverse Proxy for HTTPS Tracking Domain") sur ce sujet.
{% endalert %}

### Ressources CDN

Le tableau suivant répertorie les guides étape par étape rédigés par SendGrid et SparkPost sur la configuration de certains CDN. Même si votre CDN spécifique n’a pas à être répertorié, vous devez vous assurer que votre CDN a la capacité d’appliquer des certificats SSL.

{% alert important %}
Braze ne sera pas en mesure de dépanner la configuration CDN. Vous devez contacter votre fournisseur CDN pour vous aider à dépanner votre configuration CDN.
{% endalert %}

| Guides SendGrid étape par étape | Guides SparkPost étape par étape |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#aws-create)<br>[CloudFlare](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Cloudfront](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/)<br>[Fastly](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Plateforme cloud de Google](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#gcp-create)<br>[Microsoft Azure](https://www.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#azure-create) |

### Résolution des problèmes de CDN

Bien que la configuration, les certificats et les problèmes de proxy CDN soient gérés avec votre CDN sélectionné, nous proposons quelques conseils de résolution des problèmes de base pour identifier l’endroit où votre configuration de suivi de clic SSL peut échouer.

{% tabs %}
{% tab Domain Registry %}

#### Vérifier les problèmes du registre de domaine

Une commande dig peut vous indiquer si vous pointez votre suivi de liens au CDN. Cela peut être effectué par le terminal en exécutant `dig CNAME link_tracking_subdomain`.

Une fois la commande exécutée, sous `ANSWER SECTION`, elle doit indiquer la direction de votre CNAME. Si vous êtes dirigé vers le fournisseur de services de courrier électronique (SendGrid ou SparkPost) que vous avez choisi, et non pas votre CDN, vous devez reconfigurer votre registre de domaine pour pointer vers votre CDN.

{% endtab %}
{% tab CDN %}

#### Vérifier les problèmes CDN

Si vos liens d’e-mail en direct commencent à se rompre pendant la configuration, cela signifie souvent que vous avez pointé votre DNS vers votre CDN sans qu’il soit correctement configuré. Cela s’affiche souvent comme une erreur « Mauvais lien ».

Contactez votre fournisseur CDN et consultez sa documentation pour vous aider à dépanner votre configuration CDN.

{% endtab %}
{% tab HTTP Messages Persisting %}

#### Vérifiez si le SSL est activé par Braze

Si vous avez terminé votre configuration SSL et que vous voyez que vos liens apparaissent en tant que HTTP et non HTTPS, contactez votre banque COM ou CSM Braze et assurez-vous que le SSL a été activé par Braze. Le SSL ne peut être activé par Braze que lorsque que tous les aspects de votre configuration SSL ont été terminés.

{% endtab %}
{% endtabs %}