# Bannières

> Avec les bannières, vous pouvez créer des envois de messages personnalisés pour vos utilisateurs, tout en étendant la portée de vos autres canaux, tels que l'e-mail ou les notifications push. Vous pouvez intégrer des bannières directement dans votre application ou votre site web, ce qui vous permet d'engager le dialogue avec les utilisateurs à travers une expérience qui semble naturelle.

![Exemple de bannière affichée sur un appareil.]({% image_buster /assets/img/banners/sample_banner.png %})

## Conditions préalables

La disponibilité des bannières dépend de votre forfait Braze. Pour commencer, contactez votre gestionnaire de compte ou votre gestionnaire du succès des clients.

## Pourquoi utiliser des bannières ?

Les bannières permettent aux équipes marketing et produit de personnaliser le contenu des applis ou des sites web de manière dynamique, en reflétant l'éligibilité et le comportement des utilisateurs en temps réel. Ils affichent en permanence des messages en ligne, offrant des expériences non intrusives et contextuellement pertinentes qui sont mises à jour automatiquement au début de chaque session d'utilisateur.

Après l'intégration des Bannières dans une application ou un site web, les marketeurs peuvent concevoir et lancer des Bannières à l'aide d'un simple éditeur glisser-déposer, ce qui élimine le besoin d'une assistance permanente de la part des développeurs, réduit la complexité et améliore l'efficacité.

| Cas d’utilisation | Explication |
| --- | --- |
| Annonces | Gardez les annonces comme les événements à venir ou les changements de politique au premier plan de votre expérience sur l'application. |
| Personnalisation des offres | Affichez des promotions et des incitations personnalisées en fonction de l'historique de navigation de chaque utilisateur, du contenu de son panier, de son niveau d'abonnement et de son statut de fidélité. |
| Ciblage de l'engagement des nouveaux utilisateurs | Guidez les nouveaux utilisateurs à travers les flux d'onboarding et la configuration du compte. |
| Soldes et promotions | Mettez en avant les fonctionnalités, les produits en vogue et les campagnes de marque en cours, de manière persistante et directement sur votre page d'accueil, sans perturber l'expérience utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fonctionnalités

Les fonctionnalités des bannières sont les suivantes :

- **Créer facilement du contenu :** Créez et prévisualisez votre bannière à l'aide d'un éditeur visuel par glisser-déposer prenant en charge les images, le texte, les boutons, les formulaires de capture d'e-mail, le code personnalisé, etc.
- **Placements flexibles :** Définissez plusieurs emplacements/localisations au sein de votre application ou de votre site web où les bannières peuvent apparaître, ce qui permet un ciblage précis en fonction de contextes ou d'expériences utilisateur spécifiques.
- **Personnalisation dynamique :** Les bannières s'actualisent dynamiquement à chaque nouvelle session d'utilisateur, garantissant que le contenu reste à jour et personnalisé grâce aux outils de personnalisation intégrés de Braze et à la logique Liquid.
- **Priorité aux autochtones :** Définissez la priorité d'affichage lorsque plusieurs bannières ciblent le même emplacement, afin que le bon message atteigne les utilisateurs au bon moment.
- **Support HTML personnalisé :** Incorporez des blocs HTML personnalisés pour une personnalisation avancée ou une intégration parfaite avec vos styles web existants.

## À propos des bannières {#about-banners}

### ID de placement {#placement-id}

Les emplacements/localisations de bannières sont des emplacements/localisations spécifiques dans votre application ou site web [que vous créez avec le SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) et qui désignent l'endroit où les bannières peuvent apparaître.

Les emplacements/localisations les plus courants sont la partie supérieure de votre page d'accueil, les pages de détail des produits et les flux de paiement. Une fois les placements créés, les bannières peuvent être [attribuées dans votre campagne de bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/).

Il n'y a pas de limite fixe au nombre de placements que vous pouvez créer par espace de travail, et vous pouvez créer autant d'ID de placement que votre expérience l'exige. Chaque placement doit être unique au sein d'un espace de travail. Un seul ID de placement peut être référencé par un maximum de 10 campagnes actives en même temps.

{% alert important %}
Évitez de modifier les ID de placement après avoir lancé une campagne de bannières.
{% endalert %}

### Priorité à la bannière {#priority}

Lorsque plusieurs campagnes référencent le même ID de placement, les bannières sont affichées par ordre de priorité : élevée, moyenne ou faible. Par défaut, les bannières nouvellement créées sont réglées sur moyenne, mais vous pouvez [définir manuellement la priorité]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/#set-priority) lorsque vous créez ou modifiez votre campagne de bannières. 

Si plusieurs bannières ont la même priorité, la bannière la plus récente à laquelle l'utilisateur a droit s'affiche en premier.

### Demandes de placement {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Réception/distribution des messages

Les messages des bannières sont envoyés à votre application ou à votre site web sous forme de contenu HTML, généralement rendu à l'intérieur d'une iframe. Cela garantit un rendu cohérent de vos bannières sur tous les appareils et vous permet de séparer leurs styles et leurs scripts du reste de votre code.

Les iframes permettent des mises à jour de contenu dynamiques et personnalisées qui ne nécessitent pas de modifications de votre base de code. Chaque iframe récupère et affiche le code HTML pour chaque session d'utilisateur à l'aide d'une logique de ciblage et de personnalisation de la campagne.

### Dimensions et taille

Voici ce que vous devez savoir sur les dimensions des bannières :

- Bien que le compositeur vous permette de prévisualiser les bannières dans différentes dimensions, cette information n'est pas enregistrée ou envoyée au SDK.
- Le code HTML occupera toute la largeur du conteneur dans lequel il est affiché.
- Nous vous recommandons de créer un élément de dimension fixe et de tester ces dimensions dans composer.

## Restrictions

Chaque espace de travail peut prendre en charge jusqu'à 200 campagnes Banner actives. Si cette limite est atteinte, vous devrez [archiver ou désactiver]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) une campagne existante avant d'en créer une nouvelle.

En outre, les messages de la bannière ne prennent pas en charge les fonctionnalités suivantes :

- Intégration de Canvas
- Campagnes déclenchées par API et par événement
- Contenu connecté
- Codes de promotion
- Licenciements contrôlés par l'utilisateur
- `catalog_items` en utilisant l'[étiquette`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)

{% alert tip %}
Vous voulez aider à établir des priorités pour les prochaines étapes ? Contactez [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}

## Étapes suivantes

Maintenant que vous savez ce qu'est une bannière, vous êtes prêt à passer aux étapes suivantes :

1. [Création de bannières dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements/)
2. [Créer des campagnes de bannières dans Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
3. [Tutoriel : Affichage d'une bannière par ID de placement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
