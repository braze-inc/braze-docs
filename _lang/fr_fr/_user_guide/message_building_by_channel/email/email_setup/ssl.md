---
nav_title: SSL à Braze
article_title: Aperçu du SSL
page_order: 5
page_type: reference
description: "Cet article de référence traite de SSL, de son utilité et de la manière dont il est utilisé à Braze."
channel: email

---

# SSL à Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Une couche de socket sécurisée (SSL) permet de crypter une URL avec HTTPS, au lieu de HTTP, moins sûr. HTTPS dans une URL indique qu'il existe un certificat SSL ou TLS valide et fiable, et que le site web peut être visité en toute sécurité et n'est pas une source de logiciels malveillants dangereux.

## Pourquoi SSL est-il important ?

Bien que la plupart des domaines ne nécessitent pas de SSL, Braze recommande vivement l'utilisation de SSL pour les raisons suivantes.

Sécuriser votre site web et vos liens à l'aide du protocole SSL est une pratique courante, même pour les entreprises qui ne traitent pas directement d'informations sensibles sur leurs clients. Les utilisateurs font davantage confiance aux liens sécurisés par SSL, et la couche supplémentaire d'authentification contribue à protéger vos données.

### Nécessaire pour le suivi des clics et des ouvertures

Chez Braze, lorsque nous envoyons des e-mails, nous transformons d'abord vos liens en utilisant le sous-domaine de suivi des liens de votre marque pour suivre les clics et les ouvertures des utilisateurs. Par défaut, ces liens commencent par HTTP. Cela signifie que les utilisateurs disposant d'un navigateur ou d'une extension qui restreint le trafic non sécurisé peuvent avoir des difficultés à passer la redirection avant d'arriver à l'URL de destination, même si l'URL est sécurisée. Cela peut conduire à des images cassées et à un suivi inexact des clics et des ouvertures dans vos e-mails. C'est pourquoi la meilleure pratique consiste à appliquer une couche SSL au sous-domaine de suivi des liens afin de confirmer les redirections sécurisées dans vos e-mails. 

### Navigateur requis

Les protocoles SSL sont de plus en plus répandus aujourd'hui, car les principaux navigateurs, comme Google Chrome, commencent à restreindre le trafic via des URL non sécurisées afin de protéger leurs utilisateurs. Les entreprises dont le site web est doté du protocole SSL confirment à ces principaux navigateurs que leur contenu est fiable, ce qui réduit les problèmes de visualisation du contenu tels que les liens et les images brisés dans leurs e-mails.

### Exigences en matière de domaines HSTS 

Quels que soient les navigateurs à partir desquels vos utilisateurs accèdent à vos e-mails, vous devez configurer SSL si vous disposez d'un domaine HTTP Strict Transport Security (HSTS) et configurer un réseau de diffusion contenu pour qu'il envoie les certificats de sécurité nécessaires. Si le protocole SSL n'est pas mis en place, les images et les liens web ne fonctionneront pas.

## Acquérir un certificat SSL

Vous pouvez acquérir un certificat SSL en faisant appel à un tiers, généralement un réseau de diffusion contenu (CDN). Un réseau de diffusion contenu peut héberger le certificat SSL et le transmettre au navigateur chaque fois qu'il clique sur l'un de vos liens. Pour ce faire, le trafic est redirigé via le réseau de diffusion contenu afin d'appliquer les certificats nécessaires avant de l'envoyer à nos partenaires d'e-mail SendGrid ou SparkPost.

Pour commencer votre configuration SSL, contactez votre gestionnaire satisfaction client de Braze afin d'initier une configuration complète de l'e-mail Braze.

Une fois que Braze a lancé cette configuration, suivez les étapes suivantes :
1. Braze vous fournira des enregistrements DNS à ajouter à votre registre de domaine.
2. Braze vérifiera si les enregistrements ont été correctement ajoutés à votre registre.
3. Ensuite, vous sélectionnerez un réseau de diffusion de contenu et obtiendrez des certificats SSL auprès d'un fournisseur tiers. 
4. À ce stade, vous allez configurer votre réseau de diffusion de contenu. Notez que Braze ne pourra pas vous aider à résoudre les problèmes liés à la configuration du réseau de diffusion de contenu. Contactez votre fournisseur de diffusion contenu pour toute assistance supplémentaire.
5. Contactez votre gestionnaire de satisfaction client pour activer SSL.

### Qu'est-ce qu'un réseau de diffusion de contenu et pourquoi en ai-je besoin ?

Un réseau de réception/distribution de contenu (CDN) est une plateforme de serveurs qui permet de garantir des temps de chargement rapides de contenus de haute qualité sur plusieurs supports, tout en gérant les certificats de sécurité. 

{% alert important %}
La configuration du réseau de diffusion de contenu se fait toujours après la validation de vos DNS par Braze. Si vous n'avez pas encore entamé cette étape, contactez votre gestionnaire de satisfaction client pour obtenir plus d'informations sur la marche à suivre.
{% endalert %}

Chez Braze, pour assurer le suivi des clics et des ouvertures, nos partenaires de réception/distribution transforment les liens en utilisant un sous-domaine de marque, et le réseau de diffusion de contenu applique le certificat SSL à ces liens nouvellement transformés. Souvent, nos partenaires de réception/distribution doivent présenter des certificats valides et fiables au navigateur du destinataire de votre e-mail pour que les liens et les images s'affichent correctement. Braze ne demandant ni ne gérant ces certificats, vous devez les configurer de votre côté par l'intermédiaire d'un réseau de diffusion de contenu. 

{% alert note %}
Si vous ne pouvez pas ou ne souhaitez pas utiliser les CDN répertoriés lors de la configuration de SSL pour le suivi des clics et des ouvertures, vous pouvez mettre en place une configuration SSL personnalisée. Notez que des CDN alternatifs ou des proxys personnalisés peuvent donner lieu à une configuration plus complexe et plus nuancée. Reportez-vous aux articles de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) et de [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) sur ce sujet.
{% endalert %}

#### Ressources complémentaires

{% alert important %}
Pour obtenir de l'aide sur la résolution des problèmes de votre configuration de réseau de diffusion contenu, vous devez contacter votre fournisseur de réseau de diffusion contenu.
{% endalert %}

Le tableau suivant comprend des guides étape par étape rédigés par des partenaires ESP sur la manière de configurer certains CDN. Même si votre réseau de diffusion contenu ne figure pas dans la liste, vous devez vous assurer qu'il est en mesure d'appliquer des certificats SSL.

| Sendgrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Rapidement](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Rapidement](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour Amazon SES, consultez [Option 2 : Configuration d'un domaine HTTPS](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) et spécifiez le domaine de suivi AWS par votre région en fonction de votre cluster Braze :

- **Clusters américains de Braze :** `r.us-east-1.awstrack.me`
- **Brazez les grappes de l'UE :** `r.eu-central-1.awstrack.me`

{% alert important %}
Lorsque vous configurez le domaine de diffusion de contenu de votre réseau de diffusion, veillez à activer l'en-tête `X-Forwarded-Host`. Cela permet d'éviter les problèmes de sécurité potentiels, tels que les attaques de l'en-tête de l'hôte. Reportez-vous à la documentation du réseau de diffusion de contenu ou à votre équipe d'assistance pour savoir comment procéder, car cela varie en fonction du réseau de diffusion de contenu.
{% endalert %}

#### Résolution des problèmes

Bien que la configuration du réseau de diffusion, les certificats et les problèmes de proxy doivent être traités avec votre réseau de diffusion, voici quelques conseils généraux de résolution des problèmes pour vous aider à identifier les problèmes courants liés à la configuration du suivi des clics SSL.

##### Questions relatives au registre des domaines

Une commande dig peut vous indiquer si vous faites pointer votre suivi de lien vers le réseau de diffusion de contenu. Vous pouvez le faire dans votre terminal en lançant `dig CNAME link_tracking_subdomain`. Une fois la commande exécutée, sous `ANSWER SECTION`, vous devriez trouver la liste de l'endroit où pointe votre CNAME. S'il pointe vers le fournisseur de services e-mail que vous avez choisi (SendGrid ou SparkPost) et non vers votre réseau de diffusion contenu, essayez de reconfigurer le registre de votre domaine pour qu'il pointe vers votre réseau de diffusion contenu.

##### Réseau de diffusion de contenu

Si les liens de votre ligne/en production/instantanée d'e-mail commencent à se briser pendant la configuration, cela signifie généralement que vous avez orienté votre DNS vers votre CDN sans qu'il soit correctement configuré. Cela peut apparaître comme une erreur de "mauvais lien". Contactez votre fournisseur de réseau de diffusion de contenu et consultez sa documentation pour résoudre les problèmes liés à votre configuration de réseau de diffusion de contenu.

##### État de l'activation du SSL

Si vous avez terminé votre configuration SSL et que vos liens apparaissent toujours comme HTTP et non HTTPS, contactez votre gestionnaire satisfaction client de Braze pour vous assurer que SSL a été activé par Braze. SSL ne peut être activé par Braze qu'une fois que tous les aspects de votre configuration SSL ont été complétés.

