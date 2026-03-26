# Bannières : Foire aux questions

> Voici les réponses aux questions fréquemment posées sur les bannières en Braze. Pour obtenir des informations générales, veuillez consulter [À propos des bannières]]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Quand les mises à jour des bannières apparaissent-elles pour les utilisateurs ?

Les bannières sont actualisées avec leurs dernières données chaque fois que vous appelez la méthode d'actualisation. Il n'est pas nécessaire de renvoyer ou de mettre à jour votre campagne de bannières.

## Combien de placements puis-je demander au cours d'une session ?

Dans une seule requête pour actualiser, vous pouvez demander un maximum de 10 emplacements. Pour chaque demande, Braze renverra la bannière ayant la priorité la plus élevée à laquelle l'utilisateur est éligible. Toute demande supplémentaire entraînera une erreur.

Pour plus d'informations, veuillez consulter [Demandes de placement]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %})].

## Combien de campagnes publicitaires peuvent être actives simultanément ?

Chaque espace de travail peut prendre en charge jusqu'à 200 campagnes publicitaires actives. Si cette limite est atteinte, il sera nécessaire d'[archiver ou]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) de [désactiver]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) une campagne existante avant d'en créer une nouvelle.

## Pour les campagnes partageant un emplacement, quelle bannière est affichée en premier ?

Si un utilisateur est éligible à plusieurs campagnes publicitaires partageant le même emplacement, la publicité ayant la priorité la plus élevée sera affichée. Pour plus d'informations, veuillez consulter [Priorité des ]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})bannières].

## Puis-je utiliser des bannières dans mon flux de cartes de contenu existant ?

Les bannières diffèrent des cartes de contenu, ce qui signifie qu'il n'est pas possible d'utiliser à la fois des bannières et des cartes de contenu dans le même flux. Pour remplacer les flux de cartes de contenu existants par des bannières, il est nécessaire de [créer des emplacements dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements/).

## Puis-je déclencher l'affichage d'une bannière en fonction des actions de l'utilisateur ?

Bien que les bannières ne prennent pas en charge [la livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery), il est possible de cibler les utilisateurs en fonction de leurs actions passées à l'aide de la segmentation et de la priorité.

Par exemple, pour afficher une bannière spéciale uniquement aux utilisateurs ayant terminé un`purchase`événement :
1. **Ciblage :** Dans votre campagne, ciblez un segment d'utilisateurs ayant effectué l'événement personnalisé`purchase` au moins une fois.
2. **Priorité :** Si vous disposez d'une bannière générale pour tous les utilisateurs et d'une bannière spécifique pour les acheteurs avec un ciblage sur le même emplacement, veuillez définir la priorité de la bannière spécifique sur **Élevée** et celle de la bannière générale sur **Moyenne** ou **Faible**.

Lorsque l'utilisateur commence une nouvelle session ou actualise les bannières après avoir effectué l'action, Braze évalue son éligibilité. Si elles correspondent au segment « Achat », la bannière à priorité élevée sera affichée.


## Les utilisateurs peuvent-ils fermer manuellement une bannière ?

Non. Les utilisateurs ne peuvent pas fermer manuellement les bannières. Cependant, vous pouvez contrôler la visibilité des bannières en gérant l'éligibilité des segments d'utilisateurs. Lorsqu'un utilisateur ne répond plus aux critères de ciblage d'une campagne publicitaire, il ne la verra plus lors de sa prochaine session.

Par exemple, si vous affichez une bannière promotionnelle jusqu'à ce qu'un utilisateur effectue un achat, l'enregistrement d'un événement tel que`purchase_completed`  peut retirer cet utilisateur du segment ciblé, masquant ainsi efficacement la bannière lors des sessions suivantes.

## Est-il possible d'exporter les analyses des campagnes Banners à l'aide de l'API Braze ?

Oui. Vous pouvez utiliser [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)l'[endpoint]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) pour obtenir des données sur le nombre de campagnes Banner qui ont été consultées, cliquées ou converties.

## Quand la segmentation des utilisateurs est-elle effectuée ?

Les utilisateurs sont segmentés au début de la session. Si les segments ciblés d'une campagne dépendent d'attributs personnalisés, d'événements personnalisés ou d'autres attributs de ciblage, ceux-ci doivent être présents chez l'utilisateur au début de la session.

## Comment puis-je créer des bannières afin de garantir la latence la plus faible possible ?

Plus le message de votre bannière est simple, plus son affichage sera rapide. Il est recommandé de tester votre campagne publicitaire en fonction de la latence prévue pour votre cas d'utilisation. Par exemple, veuillez vous assurer de tester les attributs Liquid tels que `catalog_items`.

## Toutes les étiquettes Liquid sont-elles prises en charge ?

Non. Cependant, la plupart des étiquettes Liquid sont prises en charge pour les messages Banner, à l'exception de`catalog_items`celles qui sont réaffichées à l'aide de la[`:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)[balise]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Puis-je enregistrer les événements de clic ?

Oui. La manière dont les événements de clic sont capturés dépend de la façon dont votre bannière est affichée :

- **Composants standard de l'éditeur :** Si votre bannière utilise des composants d'éditeur standard (images, boutons, texte), les clics sont automatiquement suivis lorsque vous utilisez les méthodes d'insertion du SDK.
- **Blocs de code personnalisés :** Si vous souhaitez suivre les clics sur les éléments d'un bloc éditeur de code personnalisé, vous devez appeler`brazeBridge.logClick()`  à partir de votre code HTML personnalisé pour suivre les clics. Cela s'applique également lorsque vous utilisez les méthodes SDK pour insérer et afficher la bannière. Pour obtenir la référence complète, veuillez consulter [le code personnalisé et le pont JavaScript pour les bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge).
- **Interface utilisateur personnalisée (sans affichage) :** Si vous créez une interface utilisateur entièrement personnalisée à l'aide des propriétés personnalisées de la bannière au lieu d'afficher le code HTML de la bannière, veuillez`logClick()`appeler l'objet Banner à partir du code de votre application.

Pour plus d'informations, veuillez consulter [la section Enregistrement des clics]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks).
