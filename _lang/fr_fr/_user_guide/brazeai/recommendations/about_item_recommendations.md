---
nav_title: À propos des recommandations de produits
article_title: À propos des recommandations de produits
description: "Cet article de référence décrit différents cas d'utilisation pour recommander des produits aux clients à l'aide de Braze."
page_order: 10
---

# À propos des recommandations d'articles

Dans cet article, vous découvrirez les différentes façons de suggérer des articles qui intéressent vos clients, et vous vous inspirerez de cas d'utilisation courants pour créer des moteurs de recommandation à l'aide de Braze.

## Conditions préalables

Pour tous les types de recommandation, vous devez disposer d'au moins un [catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/), car c'est de là que proviennent les articles recommandés.

## Types de recommandations

Lorsque vous souhaitez recommander des produits à vos clients, vous pouvez adopter plusieurs approches :

- [Personnalisation par l’IA](#ai)
- [La plus populaire](#most-popular)
- [La plus récente](#most-recent)
- [Basée sur des sélections](#selections-based)
- [Basée sur des règles](#rules-based)
- [Tendances](#trending)

### Recommandations personnalisées avec l’IA {#ai}

Dans le cadre de la fonctionnalité de [recommandations d'articles par l'intelligence artificielle][1], les recommandations personnalisées par l'intelligence artificielle tirent parti de l'apprentissage profond pour prédire ce qui est le plus susceptible d'intéresser vos utilisateurs par la suite, en fonction de ce à quoi ils ont montré de l'intérêt par le passé. Cette méthode fournit un système de recommandation dynamique et personnalisé qui s'adapte au comportement de l'utilisateur.

Les recommandations personnalisées de l'intelligence artificielle utilisent les 6 derniers mois de données d'interaction avec les articles, comme les achats ou les événements personnalisés, pour créer le modèle de recommandation. Pour les utilisateurs qui ne disposent pas de suffisamment de données pour établir une liste personnalisée, les éléments les plus populaires servent de solution de repli afin que vos utilisateurs reçoivent toujours des suggestions pertinentes.

Grâce aux recommandations de produits avec l’IA, vous pouvez également filtrer davantage les produits disponibles avec les
[sélections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/). Cependant, les sélections avec Liquid ne peuvent pas être utilisées dans les recommandations de l'intelligence artificielle. Gardez donc cela à l'esprit lorsque vous créez vos sélections dans le catalogue.

Pour des exemples, consultez la section [Cas d'utilisation](#use-cases) de cet article.

{% alert tip %}
Les recommandations personnalisées par intelligence artificielle fonctionnent mieux avec des centaines ou des milliers d'articles et généralement au moins 30 000 utilisateurs avec des données d'achat ou d'interaction. Il s'agit d'une indication approximative qui peut varier. Les autres types de recommandations peuvent fonctionner avec moins de données.
{% endalert %}

### Recommandations des produits les plus populaires {#most-popular}

Outre le modèle « Personnalisé avec l’IA », la fonctionnalité [Recommandations de produits avec l’IA][1] inclut également un modèle de recommandation « Les plus populaires » qui présente les produits avec lesquels les utilisateurs interagissent le plus.

Sur la base des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation :

- [Produits les plus populaires](#most-popular-items)
- [Produits les plus appréciés](#liked-items)
- [Produits les plus consultés](#most-viewed-items)
- [Articles les plus populaires dans les paniers des utilisateurs](#popular-items-in-users-carts)

### Recommandations des produits les plus récents {#most-recent}

Outre le modèle « Personnalisé avec l’IA », la fonctionnalité [Recommandations de produits avec l’IA][1] inclut également un modèle de recommandation « Les plus récents » qui présente les produits avec lesquels les utilisateurs interagissent le plus. Utilisez ce modèle pour réduire l’attrition en encourageant les utilisateurs inactifs à se réengager avec le contenu pertinent.

Sur la base des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation :

- [Éléments récemment cliqués](#recently-clicked-items)
- [Produits aimés récemment](#liked-items)
- [Récemment interagi avec ou acheté des produits](#recently-engaged-with-or-purchased-items)
- [Articles récemment ajoutés au panier](#items-recently-added-to-cart)

### Recommandations de produits à la mode {#trending}

Outre le modèle "AI Personalized", la fonctionnalité de [recommandations d'articles par l'intelligence artificielle][1] comprend également un modèle de recommandation pour "Trending", qui présente les articles qui ont eu l'élan le plus positif en ce qui concerne les interactions récentes avec les utilisateurs. 

Contrairement au modèle "le plus populaire", qui présente des fonctionnalités avec un taux d'interaction élevé et constant, ce modèle présente des fonctionnalités qui ont connu une augmentation des interactions. Vous pouvez l'utiliser pour recommander des produits qui ont le vent en poupe et qui bénéficient actuellement d'une plus grande popularité.

Sur la base des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation :

- [Produits achetés à la mode](#trending-purchased-items)
- [Produits appréciés à la mode](#trending-liked-items)

### Recommandations basées sur des sélections {#selections-based}

Les [sélections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) sont des groupes spécifiques de données du catalogue. Lorsque vous utilisez une sélection, vous configurez essentiellement des filtres personnalisés basés sur des colonnes spécifiques de votre catalogue. Il peut s'agir de filtres pour la marque, la taille, l'emplacement, la date d'ajout, etc. Il vous permet de contrôler ce que vous recommandez en définissant les critères auxquels les éléments doivent répondre pour être présentés aux utilisateurs.

Les trois types précédents impliquent tous la configuration et l’entraînement d'un modèle de recommandation dans Braze. Bien que vous puissiez également utiliser des sélections dans ces modèles, vous pouvez également réaliser certains cas d'utilisation de la recommandation avec seulement des sélections de catalogue et une personnalisation liquide.

Parmi les cas d'utilisation, citons les recommandations :

- [Nouveaux produits](#new-items)
- [Produits aléatoires](#random-items)

### Recommandations basées sur des règles {#rules-based}

Un moteur de [recommandation basé sur des règles]({{site.baseurl}}/rules_based_recommendations/) utilise les données des utilisateurs et les informations sur les produits pour suggérer des articles pertinents aux utilisateurs dans les messages. Il utilise Liquid et les catalogues de Braze ou le contenu connecté pour personnaliser dynamiquement le contenu en fonction du comportement et des attributs de l'utilisateur.

Les recommandations basées sur des règles sont fondées sur une logique fixe que vous devez définir manuellement. Cela signifie que vos recommandations ne s'adapteront pas à l'historique d'achat et aux goûts individuels d'un utilisateur à moins que vous ne mettiez à jour la logique, c'est pourquoi cette méthode est préférable pour les recommandations qui ne nécessitent pas de mises à jour fréquentes.

Voici quelques exemples d'utilisation :

- **Rappels de réapprovisionnement :** Envoi de rappels de réapprovisionnement pour les produits dont le cycle d'utilisation est prévisible, comme les vitamines mensuelles ou les achats alimentaires hebdomadaires, en fonction de leur dernière date d'achat.
- **Premiers achats :** Recommandez des kits de démarrage ou des offres de lancement aux premiers acheteurs afin de les encourager à effectuer un deuxième achat.
Programmes de fidélisation : Mettez en évidence les produits qui maximiseraient les points de fidélité ou les récompenses d'un client en fonction de son solde de points actuel.
- **Contenu éducatif :** Proposer de nouveaux cours ou contenus basés sur les thèmes des documents déjà consommés ou achetés.

## Cas d’utilisation

### Articles qu'un utilisateur est le plus susceptible d'acheter ensuite

Prédire et recommander les articles qu'un utilisateur est le plus susceptible d'acheter ensuite, en fonction des événements d'achat ou des événements personnalisés liés aux achats. Par exemple :

- Un site de voyage pourrait suggérer des forfaits vacances, des vols ou des séjours à l'hôtel en fonction de l'historique de navigation de l'utilisateur et de ses réservations précédentes, anticipant ainsi sa prochaine destination de voyage et facilitant l'organisation de son séjour.
- Une plateforme de streaming peut analyser les habitudes de visionnage pour recommander des émissions ou des films qu'un utilisateur est le plus susceptible de regarder ensuite, ce qui permet de maintenir l'intérêt des utilisateurs et de réduire les taux d'attrition.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Méthode de suivi des achats, soit un objet d’achat, soit un événement personnalisé

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Réglez le **type** sur **Intelligence artificielle personnalisée**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez la manière dont vous suivez actuellement les propriétés d'achat et la propriété d'événement correspondante.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Articles récemment ajoutés au panier

Rappelez aux utilisateurs leur intérêt pour les articles qu'ils ont récemment ajoutés à leur panier, mais qu'ils n'ont pas encore achetés. Par exemple, un retailing en ligne pourrait envoyer des rappels ou proposer des réductions à durée limitée sur les articles dans leur panier, encourageant ainsi les utilisateurs à terminer leurs achats avant que les offres n'expirent.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Événement personnalisé pour l'ajout au panier

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Custom Event** et sélectionnez dans la liste l'événement personnalisé à ajouter au panier.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Produits appréciés

Encouragez les utilisateurs à explorer les produits qu'ils ont récemment aimés ou les produits populaires, sur la base d'un événement personnalisé pour les likes. Par exemple, une application de streaming musical pourrait créer des playlists personnalisées ou suggérer de nouvelles sorties d'albums en fonction des genres ou des artistes qu'un utilisateur a aimés par le passé, améliorant ainsi l'engagement de l'utilisateur et le temps passé sur l'application.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Événement personnalisé pour les likes

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez dans la liste votre événement personnalisé pour les likes.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Produits les plus populaires

Encouragez les utilisateurs à explorer les articles populaires de votre catalogue en fonction de leurs achats. Pour vous assurer que vous n'accédez qu'à des contenus pertinents, nous vous recommandons de les filtrer à l'aide d'une sélection. Par exemple, un service de réception/distribution de nourriture pourrait mettre en avant les plats ou les restaurants les mieux notés dans la région d'un utilisateur, en fonction de la popularité des commandes sur la plateforme, encourageant ainsi l'essai et la découverte.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Un objet d'achat ou tout autre événement personnalisé

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Réglez le **type** sur le **plus populaire**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents. Par exemple, le service de réception/distribution de nourriture peut proposer une sélection pour l'emplacement/localisation du restaurant ou le type de plat.
5. Choisissez la manière dont vous suivez actuellement les événements et la propriété d'événement correspondante.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Produits les plus consultés

Mettez en avant les articles qui ont attiré l'attention de votre base d'utilisateurs par le biais des vues afin d'encourager l'engagement ou les achats. Par exemple, un site Web immobilier pourrait afficher les annonces les plus consultées dans la zone de recherche d'un utilisateur afin de mettre en évidence les propriétés qui attirent beaucoup d'attention, ce qui pourrait indiquer les offres intéressantes ou les zones recherchées.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Événement personnalisé pour les vues

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Réglez le **type** sur le **plus populaire**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez dans la liste votre événement personnalisé pour les vues.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Nouveaux produits

Ce scénario ne repose pas directement sur les actions de l'utilisateur mais plutôt sur les données du catalogue. Vous pouvez filtrer les nouveaux articles en fonction de leur date d'ajout au catalogue et les promouvoir par le biais de campagnes ciblées ou de Canvases sans avoir besoin d'entraîner un modèle de recommandation.

Par exemple, une plateforme d'e-commerce technologique pourrait alerter les passionnés de technologie sur les derniers gadgets ou les précommandes à venir, en utilisant des filtres pour cibler les articles qui ont été récemment ajoutés au catalogue.

{% details Exigences %}

- Catalogue d'articles pertinents avec un champ pour la date d'ajout

{% enddetails %}

{% details Configuration %}

1. Créez une sélection à partir de votre catalogue. Assurez-vous que votre catalogue dispose d'un champ temporel (champ dont le **type de données** est défini sur **Temps**) correspondant à la date à laquelle l'élément a été ajouté.
2. (Facultatif) Ajoutez des filtres si vous le souhaitez.
3. Assurez-vous que l'**option Randomiser l'ordre de tri** est désactivée.
4. Pour **Trier le champ**, sélectionnez votre champ de date ajoutée.
5. Définissez l'**ordre de tri** comme étant décroissant.
6. [Utilisez la sélection dans les messages.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#using-selections-in-messaging)

{% enddetails %}

### Articles les plus populaires dans les paniers des utilisateurs

Mettez en avant les articles qui sont ajoutés au panier par de nombreux autres acheteurs, donnant ainsi aux utilisateurs un aperçu des tendances actuelles de votre offre.

Par exemple, un détaillant de mode pourrait promouvoir des vêtements et des accessoires à la mode en se basant sur les articles fréquemment ajoutés au panier par d'autres clients. Ils peuvent ensuite créer une section dynamique « À la mode en ce moment » sur leur page d'accueil et leur application mobile, qui se met à jour en temps réel pour encourager les utilisateurs à acheter avant que les articles ne soient épuisés.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Événement personnalisé pour l'ajout au panier

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Réglez le **type** sur le **plus populaire**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Custom Event** et sélectionnez dans la liste l'événement personnalisé à ajouter au panier.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Produits aléatoires

Pour une expérience utilisateur diversifiée, la recommandation de produits aléatoires peut favoriser la variété et potentiellement susciter de l'intérêt pour certaines parties du catalogue moins visitées. Cette méthode ne requiert pas de modèles ou d'événements spécifiques, mais utilise plutôt une sélection de catalogue pour s'assurer que les articles sont affichés de manière aléatoire.

Par exemple, une librairie en ligne pourrait proposer une fonctionnalité "Surprenez-moi", recommandant un livre au hasard en fonction des achats antérieurs de l'utilisateur ou de ses habitudes de navigation, encourageant ainsi l'exploration en dehors des genres de lecture habituels.

{% details Exigences %}

- Catalogue de produits pertinents
- Sélection avec **ordre de tri aléatoire** activé

{% enddetails %}

{% details Configuration %}

1. [Créez une sélection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#creating-a-selection) à partir de votre catalogue.
2. (Facultatif) Ajoutez des filtres si vous le souhaitez.
3. Activez l'option **Randomiser l'ordre de tri**.
4. [Utilisez la sélection dans les messages.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#using-selections-in-messaging)

{% enddetails %}

### Éléments récemment cliqués

Encouragez les utilisateurs à revenir sur les éléments sur lesquels ils ont récemment cliqué, en fonction d'un événement personnalisé pour les clics. Par exemple, un détaillant de mode en ligne pourrait créer une recommandation pour envoyer des e-mails de suivi ou des notifications push présentant des fonctionnalités pour lesquelles un utilisateur a montré de l'intérêt en cliquant dessus, encourageant ainsi l'utilisateur à revenir sur l'article et à effectuer un achat.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Événement personnalisé pour les clics

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les clics dans la liste.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Récemment interagi avec ou acheté des produits

Faites la promotion d'éléments avec lesquels les utilisateurs ont récemment interagi, qu'il s'agisse de vues, de clics ou d'achats. Cette approche permet de maintenir vos recommandations à jour et de les aligner sur les derniers centres d'intérêt de l'utilisateur.. Par exemple :

- **Éducation :** Une plateforme d'éducation en ligne pourrait encourager les utilisateurs qui ont récemment regardé une vidéo éducative mais ne se sont pas inscrits à un cours à consulter des cours similaires ou des sujets d'intérêt afin de maintenir l'engagement de l'utilisateur et de le motiver à commencer l'apprentissage.
- **Remise en forme :** Une application de fitness peut suggérer des entraînements ou des défis similaires à ceux que l'utilisateur a récemment effectués ou avec lesquels il a interagi, ce qui lui permet de varier son programme d'exercices et de s'y intéresser.
- **Produits de bricolage et décoration :** Après l'achat d'un outil électrique par un client, un retailing de rénovation peut lui recommander des accessoires connexes ou des engrenages de sécurité en fonction de son achat récent, améliorant ainsi l'expérience et la sécurité de l'utilisateur.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Un objet d'achat ou tout autre événement personnalisé pour une interaction d'engagement.

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les clics dans la liste.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Produits achetés à la mode

Mettez en évidence les articles que vos utilisateurs ont récemment achetés avec une fréquence accrue. Par exemple, une entreprise de commerce électronique pourrait recommander des articles saisonniers que les utilisateurs commencent à stocker au cours de leurs préparatifs pour la prochaine saison. 

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Une méthode de suivi des achats (soit un objet d'achat, soit un événement personnalisé).

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/ai_item_recommendations/).
2. Réglez le **Type** sur **Tendance**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez un événement d'achat ou un événement personnalisé qui suit les achats, ainsi que la propriété correspondante.
6. Former la recommandation.
7. [Utilisez la recommandation dans les communications.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Produits appréciés à la mode

Mettez en évidence les éléments que vos utilisateurs ont récemment aimés, et ce de manière plus fréquente. Par exemple, une application musicale pourrait mettre en fonctionnalité des artistes en devenir qui ont connu une hausse récente du nombre de likes des utilisateurs.

{% details Exigences %}

- Recommandations de produits basées sur l’IA
- Catalogue de produits pertinents
- Événement personnalisé pour le suivi des mentions "J'aime".

{% enddetails %}

{% details Configuration %}

1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/ai_item_recommendations/).
2. Réglez le **Type** sur **Tendance**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez votre événement personnalisé pour le suivi des likes avec la propriété correspondante.
6. Former la recommandation.
7. [Utilisez la recommandation dans les communications.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging/)

{% enddetails %}

[1]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/
