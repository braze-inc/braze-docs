# Bannières

> Avec Banners, vous pouvez créer des messages personnalisés pour vos utilisateurs, tout en élargissant la portée de vos autres canaux, tels que les e-mails ou les notifications push. Vous pouvez intégrer des bannières directement dans votre application ou votre site web, ce qui vous permet d'engager le dialogue avec les utilisateurs à travers une expérience qui semble naturelle.

![Exemple de bannière affichée sur un appareil.]({% image_buster /assets/img/banners/sample_banner.png %})

## Conditions préalables

La disponibilité des bannières dépend de votre forfait Braze. Veuillez contacter votre gestionnaire de compte ou votre gestionnaire de la satisfaction client pour commencer.

## Pourquoi utiliser des bannières ?

Les bannières permettent aux équipes marketing et produit de réaliser la personnalisation du contenu des applications ou des sites Web de manière dynamique, en tenant compte en temps réel de l'éligibilité et du comportement des utilisateurs. Ils affichent de manière persistante des messages en ligne, offrant des expériences non intrusives et pertinentes dans leur contexte, qui se mettent à jour automatiquement au début de chaque session utilisateur.

Une fois les bannières intégrées à une application ou à un site Web, les marketeurs peuvent concevoir et lancer des bannières à l'aide d'un éditeur par glisser-déposer, ce qui élimine le besoin d'une assistance continue de la part des développeurs, réduit la complexité et améliore l'efficacité.

| Cas d’utilisation | Explication |
| --- | --- |
| Annonces | Veuillez mettre en avant les annonces telles que les événements à venir ou les changements de politique dans votre expérience sur l'application. |
| Personnalisation des offres | Présentez des promotions et des incitations personnalisées en fonction de l'historique de navigation, du contenu du panier, du niveau d'abonnement et du statut de fidélité de chaque utilisateur. |
| Ciblage de l'engagement des nouveaux utilisateurs | Accompagnez les nouveaux utilisateurs tout au long du processus d'onboarding et de la configuration de leur compte. |
| Soldes et promotions | Mettez en avant le contenu phare, les produits tendance et les campagnes de marque en cours de manière persistante et directe sur votre page d'accueil sans perturber l'expérience utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fonctionnalités

Les fonctionnalités pour les bannières comprennent :

- **Création de contenu simplifiée :** Créez et prévisualisez votre bannière à l'aide d'un éditeur visuel par glisser-déposer prenant en charge les images, le texte, les boutons, les formulaires de saisie d'adresse e-mail, le code personnalisé, etc.
- **Placements flexibles :** Définissez plusieurs localisations au sein de votre application ou site web où les bannières peuvent apparaître, ce qui permet un ciblage précis en fonction de contextes ou d'expériences utilisateur spécifiques.
- **Personnalisation dynamique :** Les bannières sont actualisées de manière dynamique à chaque nouvelle session utilisateur, garantissant ainsi que le contenu reste à jour et personnalisé grâce aux outils de personnalisation intégrés de Braze et à la logique Liquid.
- **Priorisation native :** Définissez la priorité d'affichage lorsque plusieurs bannières effectuent le ciblage du même emplacement, afin de garantir que le message approprié parvienne aux utilisateurs au moment opportun.
- **Bloc éditeur de code personnalisé :** Veuillez utiliser le bloc Éditeur de code personnalisé pour ajouter du code HTML personnalisé afin de bénéficier d'une personnalisation avancée ou d'une intégration fluide avec vos styles Web existants.

## À propos des bannières {#about-banners}

### ID de placement {#placement-id}

Les emplacements de bannières sont des emplacements spécifiques dans votre application ou votre site Web que [vous créez à l'aide du SDK Braze]({{site.baseurl}}/developer_guide/banners/placements/) et qui désignent les endroits où les bannières peuvent apparaître.

Les localisations courantes incluent le haut de votre page d'accueil, les pages détaillées des produits et les processus de paiement. Une fois les emplacements créés, les bannières peuvent être [attribuées dans votre campagne publicitaire]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/).

Il n'y a pas de limite fixe au nombre de placements que vous pouvez créer par espace de travail, et vous pouvez créer autant d'ID de placement que votre expérience l'exige. Chaque emplacement doit être unique au sein d'un espace de travail. Un seul ID de placement peut être référencé par jusqu'à 25 messages actifs simultanément.

{% alert important %}
Veuillez éviter de modifier les ID de placement après le lancement d'une campagne publicitaire.
{% endalert %}

### Priorité des bannières {#priority}

Lorsque plusieurs messages de bannière font référence au même ID de placement, les bannières sont affichées par ordre de priorité : élevée, moyenne ou faible. Par défaut, les bannières sont définies sur moyen, mais vous pouvez [définir manuellement la priorité]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#set-priority) lorsque vous créez ou modifiez votre campagne de bannières. 

Si plusieurs bannières sont définies avec la même priorité, la bannière la plus récente à laquelle l'utilisateur est éligible s'affiche en premier.

### Demandes de placement {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Réception/distribution des messages

Les messages publicitaires sont diffusés sur votre application ou votre site web sous forme de contenu HTML, généralement affiché dans un cadre iframe. Cela garantit que vos bannières s'affichent de manière cohérente sur tous les appareils et vous aide à séparer leurs styles et leurs scripts du reste de votre code.

Les iframes permettent des mises à jour dynamiques et personnalisées du contenu sans nécessiter de modifications de votre base de code. Chaque iframe récupère et affiche le code HTML pour chaque session utilisateur à l'aide d'une logique de ciblage et de personnalisation de campagne.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

### Dimensions et taille

Voici ce que vous devez savoir sur les dimensions des bannières :

- Bien que le compositeur vous permette de prévisualiser les bannières dans différentes dimensions, cette information n'est pas enregistrée ou envoyée au SDK.
- Le code HTML occupe toute la largeur du conteneur dans lequel il est affiché.
- Nous vous recommandons de créer un élément de dimension fixe et de tester ces dimensions dans composer.

## Restrictions

Chaque espace de travail peut prendre en charge jusqu'à 200 campagnes publicitaires actives. Si cette limite est atteinte, il sera nécessaire d'[archiver ou]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) de [désactiver]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) une campagne existante avant d'en créer une nouvelle.

De plus, les messages bannières ne prennent pas en charge les fonctionnalités suivantes :

- Campagnes déclenchées par API et par événement
- Contenu connecté
- Codes de promotion
- Licenciements à la demande de l'utilisateur
- `catalog_items` en utilisant [`:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)l'[étiquette]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)

{% alert tip %}
Souhaitez-vous contribuer à définir les priorités pour la suite ? Veuillez contacter [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}

## Étapes suivantes

Maintenant que vous connaissez les bannières, vous êtes prêt pour les étapes suivantes :

1. [Création d'emplacements de bannières dans votre application ou votre site Web]({{site.baseurl}}/developer_guide/banners/placements/)
2. [Créer des campagnes de bannières dans Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/)
3. [Tutoriel : Affichage d'une bannière par ID de placement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
