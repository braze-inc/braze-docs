---
nav_title: Aperçu SSL
article_title: Aperçu SSL
page_order: 9
page_type: reference
description: "Le présent article de référence couvre SSL, ce pour quoi il est utilisé et comment il l’est chez Braze."
channel: email

---

# SSL chez Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Un Secured Socket Layer (SSL) chiffre une URL avec HTTPS plutôt que le HTTP moins sécurisé. Les URL avec HTTPS indiquent qu’un certificat SSL ou TLS (sécurité de la couche de transport) est valide et approuvé et que le site est sans danger pour visiter et non une arnaque ou la source de logiciels malveillants dangereux.

## Pourquoi est-ce que le SSL est important ?

Bien que la plupart des domaines ne nécessitent pas de SSL, voici les raisons pour lesquelles nous recommandons fortement le SSL à nos utilisateurs :
1. **Requis par certains navigateurs majeurs**: Les protocoles SSL deviennent plus répandus aujourd’hui, car les navigateurs majeurs comme Google Chrome commencent à restreindre le trafic via des URL non sécurisées pour protéger leurs utilisateurs. Les entreprises avec un SSL sur leur site Internet garantissent à ces navigateurs majeurs que leur contenu est fiable, minimisant ainsi les problèmes de visualisation du contenu tels que les liens cassés et les images dans leurs e-mails.<br><br>
2. **Nécessaire pour le suivi de clics et d’ouverture** : Chez Braze, lorsque nous envoyons des e-mails, nous transformons d’abord vos liens en utilisant votre sous-domaine de suivi de lien de marque pour suivre les clics et les ouvertures des utilisateurs. Par défaut, ces liens commenceront par HTTP. Cela signifie que les utilisateurs disposant d’un navigateur ou d’une extension limitant le trafic non sécurisé peuvent avoir des difficultés à passer par la redirection avant d’arriver à l’URL de destination, même si l’URL est sécurisée. Cela peut entraîner des images cassées et un suivi de clics et d’ouvertures inexact dans tous vos e-mails. C’est pourquoi il est recommandé d’appliquer une couche SSL au sous-domaine de suivi des liens afin de garantir la sécurité des redirections dans vos e-mails. <br><br>
3. **Les Domaines HSTS exigent le SSL** : Quels que soient les navigateurs avec lesquels vos utilisateurs accèdent à vos e-mails, vous devez configurer le SSL si vous possédez un domaine HTTP Strict Transport Security (HSTS) et configurer un CDN pour envoyer les certificats de sécurité nécessaires. Si vous échouez à configurer le SSL, les liens d’image et de Web se décomposent.<br><br>
4. **Bonnes pratiques générales** : La sécurisation de votre site Internet et des liens avec SSL est une pratique courante, même pour les entreprises qui ne traitent pas directement des informations sensibles sur le client. Les utilisateurs sont plus à l’aise des liens sécurisés avec SSL, et la couche d’authentification supplémentaire permet de protéger vos données.

## Acquisition d’un certificat SSL

L’acquisition d’un certificat SSL peut être effectuée en utilisant un tiers, généralement un réseau de diffusion de contenu (CDN). Un CDN peut héberger le certificat SSL et le servir au navigateur à chaque fois qu’un de vos liens est cliqué. Pour ce faire, il faut rediriger le trafic par le CDN pour appliquer les certificats nécessaires avant de l’envoyer à notre partenaire d’e-mail SendGrid ou SparkPost.

Prêt à démarrer votre configuration SSL ? Reportez-vous à l’article suivant sur le [Suivi du clic SSL]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ssl/ssl_clicktracking/). 