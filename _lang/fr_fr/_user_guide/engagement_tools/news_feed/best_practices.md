---
nav_title: Bonnes pratiques
article_title: Meilleures pratiques pour les fils d’actualité
page_order: 20
page_type: reference
description: "Cet article énonce les meilleures pratiques à suivre pour concevoir et personnaliser des cartes de fil d’actualité."
channel: news feed
hidden: true

---

# Meilleures pratiques pour les fils d’actualité

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Le fil d’actualité de Braze est un flux dynamique, ciblé et riche en contenu. C’est un excellent moyen de contacter vos utilisateurs en leur envoyant un contenu continuellement mis à jour qui n’exige aucun développement supplémentaire. Ce contenu peut cibler plusieurs segments et être programmé de la même manière que les autres messages de Braze. Chaque carte comprend un titre, un résumé, une image et une URL (facultatif). Le fil d’actualité permet également de créer un lien profond dans l’application pour rediriger les utilisateurs vers l’App Store, Google Play ou une page Web. Cet élément unique de l'interface utilisateur de Braze doit être activé lors de l'[intégration][1]. Pensez donc à en parler avec vos développeurs.

Pour en savoir plus sur les différents types de cartes de fil d'actualité, comment les créer, les cas d'utilisation, ainsi que les spécifications des cartes et des images, lisez notre page sur [la création d'éléments de fil d'actualité][4].

> Braze améliore les temps de chargement en utilisant un réseau de diffusion de contenu global pour héberger toutes les images des fils d’actualité.

## Bonnes pratiques {#news-feed-best-practices}

Chez Braze, nous apprécions les possibilités de personnalisation des fils d’actualités. Vous trouverez ci-dessous des astuces et meilleures pratiques à suivre pour tirer le meilleur parti de Braze.

### Créez un fil accrocheur

Plus votre fil d’actualités est visible, pertinent et intéressant, plus il y a de chances qu’il soit vu par des clients.  

- Utilisez le fil d’actualité pour rendre votre application plus dynamique et la mettre régulièrement à jour avec de nouveaux contenus.
- Diversifiez le type d’annonces sur vos modèles de cartes pour que votre fil d’actualité reste intéressant.
- Optimisez l’espace visuel en incorporant des images et des graphiques qui ressortent.

### Personnalisez votre fil d’actualité.

Les entreprises et leurs utilisateurs apprécient et valorisent les messages personnalisés.

- Personnalisez votre fil d’actualité pour refléter votre image de marque et créer une expérience transparente sur votre application.
- Gardez à l’esprit que les modules ciblés peuvent inciter les utilisateurs à effectuer une action immédiate dans l’application, et les URL du protocole peuvent attirer directement l’attention sur différentes sections de l’application, encourageant ainsi des comportements spécifiques comme laisser un avis, effectuer un achat et plus encore.
- Segmentez vos utilisateurs et adaptez certaines annonces pour les inciter à effectuer une action spécifique.

### Créez un fil d’actualité réellement utile

Le contenu que vous choisissez de montrer dans votre fil d’actualité peut être très varié et fonctionner en tandem avec vos campagnes.  

- Envoyez des annonces qui encouragent l’interaction, mettent en évidence les actualités et promeuvent les ventes.
- Élaborez un calendrier pour vos campagnes (par exemple vos campagnes d’onboarding), et déterminez la cadence et la fréquence appropriées pour vos messages.
- Renforcez vos campagnes en intégrant d’autres messages multicanaux dans le fil d’actualité.

## Exemple d’intégration

1-800-Flowers.com utilise le fil d'actualité pour fournir des informations pertinentes à ses utilisateurs. L’intégration SDK reste entièrement transparente : il n’y a aucune mention de Braze dans l’application elle-même et le module du Fil d’actualité est visuellement cohérent avec le reste de l’application.

![shapefeed][2]{: style="max-width:50%;"}

Vous pouvez voir plus d'exemples de flux d'actualités dans nos [Études de cas][3].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[2]: {% image_buster /assets/img_archive/18F_newsfeed.png %}
Il y a [3]: https://www.braze.com/customers
[4]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/
