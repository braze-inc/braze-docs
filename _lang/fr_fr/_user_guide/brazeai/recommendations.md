---
nav_title: Recommandations de poste
article_title: "Recommandations d'articles en Braze"
page_order: 15
search_rank: 1
description: "Apprenez tout sur les moteurs de recommandation d'articles dans Braze."
---

# Recommandations de poste

> Améliorez votre jeu de recommandation avec Braze en créant un moteur de recommandation capable de suggérer à vos utilisateurs des articles et du contenu qu'ils souhaitent réellement. De la personnalisation des expériences avec l'intelligence artificielle à la création de vos propres moteurs avec Liquid ou Connected Content, vous trouverez tout ce dont vous avez besoin pour que chaque recommandation compte.

## Conditions préalables

Avant de pouvoir créer ou utiliser des recommandations d'articles dans Braze, vous devez [créer au moins un catalogue. Seuls les]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)articles de ce catalogue seront recommandés aux utilisateurs.

## Types et cas d'utilisation

### Intelligence artificielle personnalisée {#ai}

Dans le cadre de la fonctionnalité de [recommandations d'articles par l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/), les recommandations personnalisées par l'intelligence artificielle tirent parti de l'apprentissage profond pour prédire ce qui est le plus susceptible d'intéresser vos utilisateurs par la suite, en fonction de ce à quoi ils ont montré de l'intérêt par le passé. Cette méthode fournit un système de recommandation dynamique et personnalisé qui s'adapte au comportement de l'utilisateur.

Les recommandations personnalisées de l'intelligence artificielle utilisent les 6 derniers mois de données d'interaction avec les articles, comme les achats ou les événements personnalisés, pour créer le modèle de recommandation. Pour les utilisateurs qui ne disposent pas de suffisamment de données pour établir une liste personnalisée, les éléments les plus populaires servent de solution de repli afin que vos utilisateurs reçoivent toujours des suggestions pertinentes.

Grâce aux recommandations d'articles de l'intelligence artificielle, vous pouvez également filtrer davantage les articles disponibles avec les éléments suivants.
[sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/). Cependant, les sélections avec Liquid ne peuvent pas être utilisées dans les recommandations de l'intelligence artificielle. Gardez donc cela à l'esprit lorsque vous créez vos sélections dans le catalogue.

{% alert tip %}
Les recommandations personnalisées par intelligence artificielle fonctionnent mieux avec des centaines ou des milliers d'articles et généralement au moins 30 000 utilisateurs avec des données d'achat ou d'interaction. Il s'agit d'une indication approximative qui peut varier. Les autres types de recommandations peuvent fonctionner avec moins de données.
{% endalert %}

#### Cas d'utilisation

En fonction des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient être les suivants :

{% tabs local %}
{% tab Most likely to purchase next %}
Prédire et recommander les articles qu'un utilisateur est le plus susceptible d'acheter ensuite, en fonction des événements d'achat ou des événements personnalisés liés aux achats. Par exemple :

- Un site de voyage pourrait suggérer des forfaits vacances, des vols ou des séjours à l'hôtel en fonction de l'historique de navigation de l'utilisateur et de ses réservations précédentes, anticipant ainsi sa prochaine destination de voyage et facilitant l'organisation de son séjour.
- Une plateforme de streaming peut analyser les habitudes de visionnage pour recommander des émissions ou des films qu'un utilisateur est le plus susceptible de regarder ensuite, ce qui permet de maintenir son engagement et de réduire les taux d'attrition.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Une méthode de suivi des achats, soit un objet personnalisé, soit un événement personnalisé.
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur **Intelligence artificielle personnalisée**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez la manière dont vous suivez actuellement les propriétés d'achat et la propriété d'événement correspondante.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Article le plus populaire {#most-popular}

Le modèle de recommandation "Les plus populaires" présente les fonctionnalités les plus appréciées par les utilisateurs.

#### Cas d'utilisation

Sur la base des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation :

{% tabs local %}
{% tab most popular %}
Encouragez les utilisateurs à explorer les articles populaires de votre catalogue en fonction de leurs achats. Pour vous assurer que vous n'obtenez que du contenu pertinent, nous vous recommandons de filtrer à l'aide d'une sélection. Par exemple, un service de réception/distribution de nourriture pourrait mettre en avant les plats ou les restaurants les mieux notés dans la région d'un utilisateur, en fonction de la popularité des commandes sur la plateforme, encourageant ainsi l'essai et la découverte.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Un objet d'achat ou tout autre événement personnalisé
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur le **plus populaire**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents. Par exemple, le service de réception/distribution de nourriture peut proposer une sélection pour l'emplacement/localisation du restaurant ou le type de plat.
5. Choisissez la manière dont vous suivez actuellement les événements et la propriété d'événement correspondante.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab most liked %}
Encouragez les utilisateurs à explorer les articles qu'ils ont récemment aimés ou les articles qui sont populaires, sur la base d'un événement personnalisé pour les likes. Par exemple, une application de streaming musical pourrait créer des playlists personnalisées ou suggérer de nouvelles sorties d'albums en fonction des genres ou des artistes qu'un utilisateur a aimés par le passé, améliorant ainsi l'engagement de l'utilisateur et le temps passé sur l'application.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Événement personnalisé pour les likes
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez dans la liste votre événement personnalisé pour les likes.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab most viewed %}
Mettez en avant les articles qui ont attiré l'attention de votre base d'utilisateurs par le biais des vues afin d'encourager l'engagement ou les achats. Par exemple, un site web immobilier pourrait afficher les annonces les plus consultées dans la zone de recherche d'un utilisateur afin de mettre en évidence les propriétés qui attirent beaucoup d'attention, ce qui pourrait être le signe de bonnes affaires ou d'emplacements recherchés.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Événement personnalisé pour les vues
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur le **plus populaire**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez dans la liste votre événement personnalisé pour les vues.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab popular in cart %}
Mettez en avant les articles qui sont ajoutés au panier par de nombreux autres acheteurs, donnant ainsi aux utilisateurs un aperçu des tendances actuelles de votre offre.

Par exemple, un détaillant de mode pourrait promouvoir des vêtements et des accessoires qui sont à la mode en se basant sur les ajouts personnalisés au panier par d'autres clients. Ils peuvent ensuite créer une section dynamique "Trending Now" sur leur page d'accueil et leur application mobile, qui se met à jour en temps réel pour encourager les acheteurs à acheter avant que les articles ne soient épuisés.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Événement personnalisé pour l'ajout au panier
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur le **plus populaire**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Custom Event** et sélectionnez dans la liste l'événement personnalisé à ajouter au panier.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Article le plus récent {#most-recent}

Le modèle de recommandation "Les plus récents" présente les fonctionnalités avec lesquelles les utilisateurs s'engagent le plus. Utilisez ce modèle pour réduire le désabonnement en encourageant les utilisateurs désabonnés à se réengager avec un contenu pertinent.

#### Cas d'utilisation

Sur la base des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation :

{% tabs local %}
{% tab Recently clicked %}
Encouragez les utilisateurs à revenir sur les éléments sur lesquels ils ont récemment cliqué, en fonction d'un événement personnalisé pour les clics. Par exemple, un détaillant de mode en ligne pourrait créer une recommandation pour envoyer des e-mails de suivi ou des notifications push présentant des fonctionnalités pour lesquelles un utilisateur a montré de l'intérêt en cliquant dessus, encourageant ainsi l'utilisateur à revenir sur l'article et à effectuer un achat.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Événement personnalisé pour les clics
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les clics dans la liste.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}

{% endtab %}
{% tab Recently liked %}
Encouragez les utilisateurs à explorer les articles qu'ils ont récemment aimés ou les articles qui sont populaires, sur la base d'un événement personnalisé pour les likes. Par exemple, une application de streaming musical pourrait créer des playlists personnalisées ou suggérer de nouvelles sorties d'albums en fonction des genres ou des artistes qu'un utilisateur a aimés par le passé, améliorant ainsi l'engagement de l'utilisateur et le temps passé sur l'application.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Événement personnalisé pour les likes
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez dans la liste votre événement personnalisé pour les likes.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Recently engaged %}
Faites la promotion d'éléments avec lesquels les utilisateurs ont récemment interagi, qu'il s'agisse de vues, de clics ou d'achats. Cette approche permet de maintenir vos recommandations à jour et de les aligner sur les derniers centres d'intérêt de l'utilisateur.. Par exemple :

- **Éducation :** Une plateforme d'éducation en ligne pourrait encourager les utilisateurs qui ont récemment regardé une vidéo éducative mais ne se sont pas inscrits à un cours à consulter des cours similaires ou des sujets d'intérêt afin de maintenir l'engagement de l'utilisateur et de le motiver à commencer l'apprentissage.
- **La remise en forme :** Une application de fitness peut suggérer des entraînements ou des défis similaires à ceux que l'utilisateur a récemment effectués ou avec lesquels il a interagi, ce qui lui permet de varier son programme d'exercices et de s'y intéresser.
- **Détaillant de produits d'amélioration de l'habitat :** Après qu'un client a acheté un outil électrique, un retailing de rénovation peut lui recommander des accessoires connexes ou des engrenages de sécurité en fonction de son achat récent, améliorant ainsi l'expérience et la sécurité de l'utilisateur.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Un objet d'achat ou tout autre événement personnalisé pour une interaction d'engagement.
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Événement personnalisé** et sélectionnez votre événement personnalisé pour les clics dans la liste.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Recently added %}
Rappelez aux utilisateurs leur intérêt pour les articles qu'ils ont récemment ajoutés à leur panier, mais qu'ils n'ont pas encore achetés. Par exemple, un retailing en ligne pourrait envoyer des rappels ou proposer des réductions à durée limitée sur les articles dans leur panier, encourageant ainsi les utilisateurs à terminer leurs achats avant que les offres n'expirent.
{% details Requirements %}

- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Événement personnalisé pour l'ajout au panier
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/).
2. Réglez le **type** sur le **plus récent**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez **Custom Event** et sélectionnez dans la liste l'événement personnalisé à ajouter au panier.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Article en vogue {#trending}

Le modèle de recommandation "Trending" présente les fonctionnalités qui ont le plus progressé au cours des dernières interactions avec les utilisateurs. Nous calculons cela en utilisant une analyse pondérée d'environ 10 semaines d'historique d'événements, la pondération la plus forte étant appliquée aux 2 semaines les plus récentes. Pour éviter que de petites fluctuations n'affectent la qualité de la recommandation, nous appliquons un seuil d'activité et des techniques de lissage statistique.

Contrairement au modèle "le plus populaire", qui présente des fonctionnalités avec un taux d'interaction élevé et constant, ce modèle présente des fonctionnalités qui ont connu une augmentation des interactions. Vous pouvez l'utiliser pour recommander des produits qui ont le vent en poupe et qui bénéficient actuellement d'une traction accrue.

#### Cas d'utilisation

Sur la base des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation :

{% tabs local %}
{% tab Trending purchased %}
Mettez en évidence les articles que vos utilisateurs ont récemment achetés avec une fréquence accrue. Par exemple, une entreprise de commerce électronique pourrait recommander des articles saisonniers que les utilisateurs commencent à stocker au cours de leurs préparatifs pour la prochaine saison. 

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Une méthode de suivi des achats (soit un objet d'achat, soit un événement personnalisé).
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/ai_item_recommendations/).
2. Réglez le **Type** sur **Tendance**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez un événement d'achat ou un événement personnalisé qui suit les achats, ainsi que la propriété correspondante.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Trending liked %}
Mettez en évidence les éléments que vos utilisateurs ont récemment aimés, et ce de manière plus fréquente. Par exemple, une application musicale pourrait mettre en fonctionnalité des artistes en devenir qui ont connu une hausse récente du nombre de likes des utilisateurs.

{% details Requirements %}
- Recommandations sur les postes de l'intelligence artificielle
- Catalogue d'articles pertinents
- Événement personnalisé pour le suivi des mentions "J'aime".
{% enddetails %}

{% details Setting it up %}
1. Créez une [recommandation d'article d'intelligence artificielle]({{site.baseurl}}/ai_item_recommendations/).
2. Réglez le **Type** sur **Tendance**.
3. Sélectionnez votre catalogue.
4. (Facultatif) Ajoutez une sélection pour filtrer votre recommandation et ne retenir que les éléments pertinents.
5. Choisissez votre événement personnalisé pour le suivi des propriétés d'événement, ainsi que la propriété correspondante.
6. Former la recommandation.
7. [Utilisez la recommandation dans les messages.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging/)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Basé sur des sélections {#selections-based}

Les [sélections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) sont des groupes spécifiques de données du catalogue. Lorsque vous utilisez une sélection, vous configurez essentiellement des filtres personnalisés basés sur des colonnes spécifiques de votre catalogue. Il peut s'agir de filtres pour la marque, la taille, l'emplacement/localisation, la date d'ajout, etc. Il vous permet de contrôler ce que vous recommandez en définissant les critères auxquels les éléments doivent répondre pour être présentés aux utilisateurs.

Les trois types précédents impliquent tous la configuration et la formation d'un modèle de recommandation dans Braze. Bien que vous puissiez également utiliser des sélections dans ces modèles, vous pouvez également réaliser certains cas d'utilisation de la recommandation avec seulement des sélections de catalogue et une personnalisation liquide.

#### Cas d'utilisation

Sur la base des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient inclure la recommandation :

{% tabs local %}
{% tab New items %}
Ce scénario ne repose pas directement sur les actions de l'utilisateur mais plutôt sur les données du catalogue. Vous pouvez filtrer les nouveaux articles en fonction de leur date d'ajout au catalogue et les promouvoir par le biais de campagnes ciblées ou de Canvases sans avoir besoin d'entraîner un modèle de recommandation.

Par exemple, une plateforme d'e-commerce technologique pourrait alerter les passionnés de technologie sur les derniers gadgets ou les précommandes à venir, en utilisant des filtres pour cibler les articles qui ont été récemment ajoutés au catalogue.

{% details Requirements %}
- Catalogue d'articles pertinents avec un champ pour la date d'ajout
{% enddetails %}

{% details Setting it up %}
1. Créez une sélection à partir de votre catalogue. Assurez-vous que votre catalogue dispose d'un champ temporel (champ dont le **type de données** est défini sur **Temps**) qui correspond à la date à laquelle l'élément a été ajouté.
2. (Facultatif) Ajoutez des filtres si vous le souhaitez.
3. Assurez-vous que l'**option Randomiser l'ordre de tri** est désactivée.
4. Pour le champ **de tri**, sélectionnez votre champ de date ajoutée.
5. Définissez l'**ordre de tri** comme étant décroissant.
6. [Utilisez la sélection dans les messages.]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Random items %}
Pour une expérience utilisateur diversifiée, la recommandation d'articles aléatoires peut introduire de la variété et potentiellement susciter de l'intérêt pour les zones du catalogue les moins visitées. Cette méthode ne requiert pas de modèles ou d'événements spécifiques, mais utilise plutôt une sélection de catalogue pour s'assurer que les articles sont affichés de manière aléatoire.

Par exemple, une librairie en ligne pourrait proposer une fonctionnalité "Surprenez-moi", recommandant un livre au hasard en fonction des achats antérieurs de l'utilisateur ou de ses habitudes de navigation, encourageant ainsi l'exploration en dehors des genres de lecture habituels.

{% details Requirements %}
- Catalogue d'articles pertinents
- Sélection avec **ordre de tri aléatoire** activé
{% enddetails %}

{% details Setting it up %}
1. [Créez une sélection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#creating-a-selection) à partir de votre catalogue.
2. (Facultatif) Ajoutez des filtres si vous le souhaitez.
3. Activez l'option **Randomiser l'ordre de tri**.
4. [Utilisez la sélection dans les messages.]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging)
{% enddetails %}
{% endtab %}
{% endtabs %}

### Basé sur des règles {#rules-based}

Un moteur de [recommandation basé sur des règles]({{site.baseurl}}/rules_based_recommendations/) utilise les données des utilisateurs et les informations sur les produits pour suggérer des articles pertinents aux utilisateurs dans les messages. Il utilise Liquid et les catalogues de Braze ou le contenu connecté pour personnaliser dynamiquement le contenu en fonction du comportement et des attributs de l'utilisateur.

Les recommandations basées sur des règles sont fondées sur une logique fixe que vous devez définir manuellement. Cela signifie que vos recommandations ne s'adapteront pas à l'historique d'achat et aux goûts individuels d'un utilisateur à moins que vous ne mettiez à jour la logique, c'est pourquoi cette méthode est préférable pour les recommandations qui ne nécessitent pas de mises à jour fréquentes.

#### Cas d'utilisation

En fonction des données d'interaction suivies, les cas d'utilisation de ce modèle pourraient être les suivants :

- **Rappels de réapprovisionnement :** Envoi de prédictions de réapprovisionnement pour les articles dont le cycle d'utilisation est prévisible, comme les vitamines mensuelles ou les produits d'épicerie hebdomadaires, en fonction de leur dernière date d'achat.
- **Les primo-accédants :** Recommandez des kits de démarrage ou des offres de lancement aux premiers acheteurs afin de les encourager à effectuer un deuxième achat.
Programmes de fidélisation : Mettez en évidence les produits qui maximiseraient les points de fidélité ou les récompenses d'un client en fonction de son solde de points actuel.
- **Contenu éducatif :** Proposer de nouveaux cours ou contenus sur la base des thèmes abordés dans les documents déjà consommés ou achetés.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Questions fréquemment posées {#faq}

### Qu'est-ce qui fait que les articles les plus populaires sont mélangés aux recommandations d'autres modèles ?

Lorsque notre moteur de recommandation établit une liste pour vous, il donne d'abord la priorité aux sélections personnalisées en fonction du modèle spécifique que vous avez choisi, comme "Plus récent" ou "Personnalisé par l'intelligence artificielle". Si, pour une raison quelconque, ce modèle ne peut pas remplir la liste complète des 30 recommandations, certains de vos articles les plus populaires parmi tous les utilisateurs sont alors ajoutés afin de s'assurer que chaque utilisateur dispose toujours d'un ensemble complet de recommandations.

Cela se produit dans quelques conditions spécifiques :

- Le modèle trouve moins de 30 articles correspondant à vos critères.
- Les articles concernés ne sont plus disponibles ou en stock.
- Les articles ne répondent pas aux critères de sélection actuels, peut-être en raison d'un changement de stock ou des préférences de l'utilisateur.

### Les recommandations existantes font-elles l'objet d'une formation hebdomadaire après la mise à niveau vers Item Recommendations Pro ?

Oui, mais seulement après la prochaine mise à jour planifiée. Les recommandations existantes ne passent pas à l'entraînement hebdomadaire et aux prédictions quotidiennes immédiatement après la mise à niveau vers Item Recommendations Pro. Toutefois, ils adopteront automatiquement la nouvelle planification lors de leur prochain cycle de recyclage. Par exemple, si une recommandation a été formée pour la dernière fois le 1er février et qu'elle est configurée pour se recycler tous les 30 jours, elle adoptera la nouvelle planification hebdomadaire après sa prochaine mise à jour, le 2 mars.