---
nav_title: SSL chez Braze
article_title: Aperçu SSL
page_order: 5
page_type: reference
description: "Le présent article de référence couvre le SSL, son utilité et la manière dont il est utilisé chez Braze."
channel: email

---

# SSL chez Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Le protocole SSL (Secure Socket Layer) chiffre une URL avec HTTPS au lieu de HTTP. HTTPS indique qu'un certificat SSL ou TLS (sécurité de la couche de transport) valide et fiable existe et que le site web peut être consulté en toute sécurité.

## Pourquoi le SSL est-il important ?

La plupart des domaines ne nécessitent pas de SSL, mais Braze recommande fortement de l'utiliser pour les raisons suivantes.

La sécurisation de votre site Internet et de vos liens avec SSL est une pratique courante, même pour les entreprises qui ne traitent pas directement des informations sensibles sur leurs clients. Les utilisateurs font davantage confiance aux liens sécurisés avec SSL, et la couche d'authentification supplémentaire permet de protéger vos données.

### Nécessaire pour le suivi des clics et des ouvertures

Braze transforme vos liens en utilisant votre sous-domaine de suivi de liens personnalisé afin de suivre les clics et les ouvertures. Par défaut, ces liens commencent par HTTP. Les utilisateurs disposant de navigateurs ou d'extensions qui restreignent le trafic non sécurisé peuvent rencontrer des difficultés pour passer par la redirection avant l'URL de destination, même si l'URL est sécurisée. Cela peut entraîner des images endommagées et un suivi inexact. Appliquez le protocole SSL au sous-domaine de suivi des liens afin de garantir la sécurité des redirections.

### Exigences du navigateur

Les principaux navigateurs, tels que Google Chrome, limitent le trafic via des URL non sécurisées afin de protéger les utilisateurs. L'utilisation du protocole SSL permet de confirmer la fiabilité du contenu et de minimiser les problèmes tels que les liens et les images brisés dans les e-mails.

### Exigences des domaines HSTS

Si vous disposez d'un domaine HTTP Strict Transport Security (HSTS), configurez SSL et configurez un réseau de diffusion de contenu pour envoyer les certificats de sécurité requis. Sans SSL, les liens vers les images et les sites web ne fonctionnent pas correctement.

## Acquisition d'un certificat SSL

Obtenez un certificat SSL par l'intermédiaire d'un tiers, généralement un réseau de diffusion de contenu (CDN). Un CDN héberge le certificat et le transmet au navigateur lorsqu'un utilisateur clique sur un lien, en redirigeant le trafic via le CDN afin d'appliquer les certificats avant de l'envoyer à Sendgrid ou SparkPost.

Pour commencer la configuration SSL, contactez votre Customer Success Manager Braze afin de lancer une configuration complète de l'e-mail Braze.

Une fois que Braze a lancé la configuration, suivez les étapes suivantes :
1. Braze fournit des enregistrements DNS à ajouter à votre registre de domaine.
2. Braze vérifie si les enregistrements ont été ajoutés correctement à votre registre.
3. Vous sélectionnez ensuite un CDN et obtenez des certificats SSL auprès d'un fournisseur tiers. 
4. À ce stade, vous configurez votre CDN. Notez que Braze ne sera pas en mesure de vous aider à résoudre les problèmes de configuration du CDN. Contactez votre fournisseur de CDN pour toute assistance supplémentaire.
5. Contactez votre Customer Success Manager pour activer le protocole SSL.

### Qu'est-ce qu'un CDN et pourquoi en ai-je besoin ?

Un réseau de diffusion de contenu (CDN) est une plateforme de serveurs qui contribue à garantir des temps de chargement rapides pour le contenu sur plusieurs supports, tout en gérant les certificats de sécurité. 

{% alert important %}
La configuration du CDN se fait toujours après la validation de vos enregistrements DNS par Braze. Si vous n'avez pas encore entrepris cette étape, contactez votre Customer Success Manager pour obtenir plus d'informations sur la manière de procéder.
{% endalert %}

Pour le suivi des clics et des ouvertures, les partenaires de distribution transforment les liens à l'aide d'un sous-domaine de marque et le CDN applique le certificat SSL à ces liens transformés. Les partenaires doivent fréquemment présenter des certificats valides au navigateur du destinataire pour que les liens et les images s'affichent correctement. Étant donné que Braze ne demande ni ne gère de certificats, vous devez effectuer cette configuration via un CDN. 

{% alert note %}
Si vous ne pouvez pas ou ne souhaitez pas utiliser les CDN répertoriés pour le suivi des clics et des ouvertures SSL, vous pouvez mettre en place une configuration SSL personnalisée. L'utilisation d'autres CDN ou de proxys personnalisés peut entraîner une configuration plus complexe. Consultez la documentation de [Sendgrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) et de [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

#### Ressources complémentaires

{% alert important %}
Pour la résolution des problèmes liés à la configuration de votre CDN, contactez votre fournisseur de CDN.
{% endalert %}

Consultez les ressources suivantes rédigées par des partenaires ESP sur la manière de configurer certains CDN. Même si votre CDN spécifique n'est pas répertorié, vous devez vous assurer qu'il a la capacité d'appliquer des certificats SSL.

**Sendgrid**

- [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)
- [CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)
- [Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)
- [KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn)

**SparkPost**
- [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)
- [CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)
- [Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)
- [Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)
- [Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) 

**Amazon SES :**
- Consultez [Configuring custom domains to handle open and click tracking](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) et indiquez le domaine de suivi AWS par région en fonction de votre cluster Braze :
    - **Clusters Braze aux États-Unis :** `r.us-east-1.awstrack.me`
    - **Clusters Braze dans l'UE :** `r.eu-central-1.awstrack.me`
- [AWS Cloudfront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html)
- [CloudFlare](https://developers.cloudflare.com/ssl/get-started/)
- [Fastly](https://www.fastly.com/documentation/guides/getting-started/domains/securing-domains/setting-up-tls-with-certificates-fastly-manages/)
- [KeyCDN](https://www.keycdn.com/support/how-to-setup-custom-ssl)
- [Google Cloud](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs)


{% alert important %}
Lorsque vous configurez le domaine de suivi des clics de votre CDN, activez l'en-tête `X-Forwarded-Host` pour prévenir d'éventuels problèmes de sécurité tels que les attaques par en-tête d'hôte. Consultez la documentation de votre CDN ou votre équipe d'assistance pour connaître la procédure à suivre.
{% endalert %}

#### Résolution des problèmes

Bien que la configuration du CDN, les certificats et les problèmes de proxy doivent être gérés avec votre fournisseur de CDN, utilisez ces conseils pour identifier les problèmes courants liés au suivi des clics SSL.

##### Problèmes liés au registre de domaine

Exécutez une commande dig pour vérifier que le suivi des liens pointe bien vers le CDN. Dans votre terminal, exécutez `dig CNAME link_tracking_subdomain`. Sous `ANSWER SECTION`, vous verrez où pointe votre CNAME. S'il pointe vers le fournisseur de services d'e-mailing (Sendgrid ou SparkPost) et non vers votre CDN, reconfigurez votre registre de domaine afin qu'il pointe vers votre CDN.

##### Problèmes liés au CDN

Si les liens e-mail en production ne fonctionnent plus pendant la configuration, il est probable que vous ayez redirigé le DNS vers votre CDN avant d'avoir correctement terminé la configuration. Cela peut apparaître comme une erreur de « mauvais lien ». Contactez votre fournisseur de CDN et consultez sa documentation afin de résoudre les problèmes de configuration.

##### État d'activation SSL

Si vous avez terminé la configuration SSL et que les liens apparaissent toujours en HTTP, contactez votre Customer Success Manager Braze afin de confirmer que Braze a bien activé SSL. Braze n'active SSL qu'une fois toutes les étapes de configuration terminées.