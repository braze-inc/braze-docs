---
nav_title: Meilleures pratiques
article_title: Meilleures pratiques du flux d'actualités
page_order: 20
page_type: Référence
description: "Cet article fournit les meilleures pratiques pour la conception et la personnalisation des cartes de News Feed."
channel: fil d'actualité
---

# Meilleures pratiques du flux d'actualités

Le flux de nouvelles de Braze est un flux ciblé et dynamique de contenu riche. Il offre un moyen puissant d'atteindre les utilisateurs avec un contenu constamment mis à jour qui ne nécessite pas de travail de développement supplémentaire. Ce contenu peut être ciblé sur différents segments et planifié de la même manière que les autres messages de Braze. Chaque carte se compose d'un titre, d'un résumé, d'une image et, optionnellement, d'une URL. Le flux inclut également la possibilité de créer des liens profonds dans l'application, le lien directement vers l'App Store, Google Play, etc. ou diriger les utilisateurs vers une vue Web. Cet élément unique de l'interface utilisateur de Braze doit être activé pendant [l'intégration][1]. Assurez-vous d'en discuter avec vos développeurs.

Pour en savoir plus sur les différents types de cartes de flux de nouvelles, comment les créer, utiliser des cas, ainsi que les spécifications de la carte et de l'image, veuillez lire notre page [sur la création de fils d'actualité][4].

> Braze améliore les temps de chargement en utilisant un CDN global pour héberger toutes les images de flux d'actualités.

{% alert note %}
Braze recommande que les clients qui utilisent notre outil News Feed passent à notre canal de messagerie de cartes de contenu - il est plus flexible, personnalisable et fiable. Il est également plus facile à trouver et à utiliser dans le produit Braze. Contactez votre responsable de compte Braze pour plus d'informations.
{% endalert %}

## Meilleures pratiques {#news-feed-best-practices}

Chez Braze, nous apprécions la personnalisation que le fil de nouvelles apporte à la table. Voici quelques-unes de nos meilleures pratiques et conseils pour vous aider à tirer le meilleur parti du Brésil.

### Rendez-le attrayant

Plus votre fil de nouvelles est remarquable, plus pertinent et intéressant, plus il sera probablement vu par les autres.

- Utilisez le fil d'actualité pour rendre votre application dynamique et régulièrement mise à jour en présentant de nouveaux contenus.
- Diversifiez le type d'annonces de cartes modèles pour garder le flux d'actualités intéressant
- Profitez de l'espace visuel en incorporant des images et des graphismes qui se démarquent.

### Rendez-le personnel

Les entreprises et leurs utilisateurs aiment la personnalisation de la valeur.

- Personnalisez le fil d'actualités pour refléter l'identité de votre marque et créer une expérience transparente de l'application.
- Gardez à l'esprit que les modules ciblés peuvent immédiatement inspirer l'action dans l'application, et les URL de protocole peuvent attirer l'attention sur différentes sections de l'application, en encourageant un comportement spécifique comme les commentaires, les achats et plus encore.
- Utilisateurs du segment et adaptez certaines annonces pour inspirer une action spécifique.

### Rendre cela utile

Le contenu que vous choisissez de montrer à travers le flux de nouvelles peut être étendu et de travailler en tandem avec des campagnes.

- Fournir des annonces qui encouragent l'interaction, mettre en valeur les nouvelles et promouvoir les ventes.
- Élaborer un calendrier pour les campagnes comme l'intégration etc., et déterminer la cadence et la fréquence appropriées de la messagerie.
- Renforcer et renforcer les campagnes en intégrant d'autres messages multicanaux dans le flux d'actualités

## Exemple d'intégration

1-800-Flowers.com utilise le fil d'actualité pour fournir des informations pertinentes à ses utilisateurs. L'intégration du SDK reste entièrement transparente : il n'y a aucune mention de Braze dans l'application elle-même et le module News Feed a une esthétique de design qui est compatible avec le reste de l'application.

!\[shapefeed\]\[2\]{: style="max-width:50%;"}

Vous pouvez voir plus d'exemples de flux d'actualités dans notre [Études de cas][3].
[2]: {% image_buster /assets/img_archive/18F_newsfeed.png %}

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[3]: https://www.braze.com/customers
[4]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/
