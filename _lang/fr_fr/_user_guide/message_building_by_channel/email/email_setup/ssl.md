---
nav_title: SSL chez Braze
article_title: Aperçu SSL
page_order: 5
page_type: reference
description: "Le présent article de référence couvre le SSL, ce pour quoi il est utilisé et comment il l’est chez Braze."
channel: email

---

# SSL chez Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Un Secured Socket Layer (SSL) chiffre une URL avec du HTTPS, plutôt que le HTTP moins sécurisé. L’HTTPS dans une URL indique qu’un certificat SSL ou TLS (sécurité de la couche de transport) valide et approuvé existe et que le site Internet est sans danger pour être consulté et non une source de logiciels malveillants dangereux.

## Pourquoi est-ce que le SSL est important ?

Bien que la plupart des domaines ne nécessitent pas de SSL, Braze recommande fortement le SSL à nos utilisateurs pour ces raisons centrales.

La sécurisation de votre site Internet et des liens avec SSL est une pratique courante, même pour les entreprises qui ne traitent pas directement des informations sensibles sur le client. Les utilisateurs sont plus à l’aise des liens sécurisés avec SSL, et la couche d’authentification supplémentaire permet de protéger vos données.

### Nécessaire pour le suivi des clics et des ouvertures

Chez Braze, lorsque nous envoyons des e-mails, nous transformons d’abord vos liens en utilisant votre sous-domaine de suivi de lien de marque pour suivre les clics et les ouvertures des utilisateurs. Par défaut, ces liens commenceront par HTTP. Cela signifie que les utilisateurs disposant d’un navigateur ou d’une extension limitant le trafic non sécurisé peuvent avoir des difficultés à passer par la redirection avant d’arriver à l’URL de destination, même si l’URL est sécurisée. Cela peut entraîner des images cassées et un suivi de clics et d’ouvertures inexact dans tous vos e-mails. C'est pourquoi la meilleure pratique consiste à appliquer une couche SSL au sous-domaine de suivi des liens afin de confirmer les redirections sécurisées dans vos e-mails. 

### Exigences du navigateur

Les protocoles SSL deviennent plus répandus aujourd’hui, car les navigateurs majeurs comme Google Chrome commencent à restreindre le trafic via des URL non sécurisées pour protéger leurs utilisateurs. Les entreprises dont le site web est doté du protocole SSL confirment à ces principaux navigateurs que leur contenu est fiable, ce qui réduit les problèmes de visualisation du contenu tels que les liens et les images brisés dans leurs e-mails.

### Exigences des domaines HSTS 

Quels que soient les navigateurs avec lesquels vos utilisateurs accèdent à vos e-mails, vous devez configurer le SSL si vous possédez un domaine HTTP Strict Transport Security (HSTS) et configurer un CDN pour envoyer les certificats de sécurité nécessaires. Si vous échouez à configurer le SSL, les liens d’image et de Web se décomposent.

## Acquisition d’un certificat SSL

Vous pouvez obtenir un certificat SSL en utilisant un tiers, généralement un réseau de diffusion de contenu (CDN). Un CDN peut héberger le certificat SSL et le servir au navigateur à chaque fois qu’un de vos liens est cliqué. Pour ce faire, il faut rediriger le trafic par le CDN pour appliquer les certificats nécessaires avant de l’envoyer à notre partenaire d’e-mail SendGrid ou SparkPost.

Pour commencer à configurer votre SSL, vous devez contacter votre gestionnaire du succès des clients Braze pour lancer une configuration d’e-mail Braze complète.

Une fois que Braze a lancé cette configuration, procédez comme suit :
1. Braze fournit des enregistrements DNS à ajouter à votre registre de domaine.
2. Braze vérifie si les enregistrements ont été ajoutés correctement à votre registre.
3. Vous allez ensuite sélectionner un CDN et obtenir des certificats SSL auprès d’un fournisseur tiers. 
4. À ce stade, vous allez configurer votre CDN. Veuillez remarquer que Braze ne sera pas en mesure de vous aider à résoudre les problèmes de configuration CDN. Contactez votre fournisseur CDN pour toute assistance supplémentaire.
5. Contactez votre gestionnaire du succès des clients Braze pour activer le SSL.

### Qu’est-ce qu’un CDN et pourquoi en ai-je besoin ?

Un réseau de diffusion de contenu (CDN) est une plateforme de serveurs qui permet de garantir des temps de chargement rapides de contenus de haute qualité sur plusieurs supports tout en gérant les certificats de sécurité. 

{% alert important %}
La configuration CDN se fait toujours lorsque Braze a obtenu et validé vos enregistrements DNS. Si vous n’avez pas encore commencé cette étape, contactez votre gestionnaire du succès des clients pour plus d’informations sur la façon de commencer.
{% endalert %}

Chez Braze, pour effectuer le suivi d’ouvertures et de clics, nos partenaires de livraison transforment les liens en utilisant un sous-domaine de marque, et le CDN applique le certificat SSL à ces liens nouvellement transformés. Souvent, nos partenaires de livraison sont tenus de présenter des certificats valides et approuvés au navigateur de votre destinataire d’e-mail pour les liens et les images à afficher correctement. Étant donné que Braze ne demande ni ne gère de tels certificats, cela doit être configuré de votre côté par le biais d’un CDN. 

{% alert note %}
Si vous n’êtes pas en mesure ou ne désirez pas utiliser les CDN répertoriés lors de la configuration de SSL pour le suivi des clics et des ouvertures, vous pouvez paramétrer une configuration SSL personnalisée. Veuillez remarquer que les CDN alternatifs ou les proxys personnalisés peuvent entraîner une configuration plus complexe et nuancée. Reportez-vous aux articles de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) et de [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) sur ce sujet.
{% endalert %}

#### Ressources complémentaires

{% alert important %}
Pour obtenir une aide supplémentaire concernant la résolution des problèmes de votre configuration CDN, vous devez contacter votre fournisseur CDN.
{% endalert %}

Le tableau suivant comprend des guides étape par étape rédigés par des partenaires ESP sur la manière de configurer certains CDN. Même si votre CDN spécifique n’a pas à être répertorié, vous devez vous assurer que votre CDN a la capacité d’appliquer des certificats SSL.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour Amazon SES, consultez [Option 2 : Configuration d'un domaine HTTPS](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) et spécifiez le domaine de suivi AWS par votre région en fonction de votre cluster Braze :

- **Clusters Braze aux États-Unis :** `r.us-east-1.awstrack.me`
- **Clusters Braze dans l’UE :** `r.eu-central-1.awstrack.me`

{% alert important %}
Lorsque vous configurez le domaine de diffusion de contenu de votre réseau de diffusion, veillez à activer l'en-tête `X-Forwarded-Host`. Cela permet d'éviter les problèmes de sécurité potentiels, tels que les attaques de l'en-tête de l'hôte. Reportez-vous à la documentation du réseau de diffusion de contenu ou à votre équipe d'assistance pour savoir comment procéder, car cela varie en fonction du réseau de diffusion de contenu.
{% endalert %}

#### Résolution des problèmes

Bien que la configuration, les certificats et les problèmes de proxy CDN soient gérés avec votre CDN, voici quelques conseils généraux de résolution des problèmes pour identifier les problèmes fréquents de la configuration du suivi de clic SSL.

##### Problèmes liés au registre des domaines

Une commande dig peut vous indiquer si vous pointez votre suivi de liens au CDN. Cela peut être effectué dans votre terminal en exécutant `dig CNAME link_tracking_subdomain`. Une fois la commande exécutée, sous `ANSWER SECTION`, vous devriez trouver l'endroit où pointe votre CNAME. Si vous êtes dirigé vers le fournisseur de services de courrier électronique (SendGrid ou SparkPost) que vous avez choisi, et non pas votre CDN, essayez de reconfigurer votre registre de domaine pour pointer vers votre CDN.

##### Problèmes liés au CDN

Si vos liens d’e-mail en direct commencent à se rompre pendant la configuration, cela signifie généralement que vous avez pointé votre DNS vers votre CDN sans qu’il soit correctement configuré. Cela peut apparaître comme une erreur de « mauvais lien ». Contactez votre fournisseur CDN et consultez sa documentation pour vous aider à dépanner votre configuration CDN.

##### Statut d’activation SSL

Si vous avez terminé votre configuration SSL et que vos liens apparaissent toujours en tant que HTTP et non HTTPS, contactez votre gestionnaire du succès des clients Braze et assurez-vous que le SSL a été activé par Braze. SSL ne peut être activé par Braze qu'une fois que tous les aspects de votre configuration SSL ont été complétés.

