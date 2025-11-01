# Bannières : Foire aux questions

> Voici les réponses aux questions fréquemment posées sur les bannières en Braze. Pour plus d'informations générales, voir [À propos des bannières]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %}).

## Quand les mises à jour de la bannière apparaissent-elles pour les utilisateurs ?

Les bannières sont actualisées avec les données les plus récentes chaque fois que vous appelez la méthode d'actualisation - il n'est pas nécessaire de renvoyer ou de mettre à jour votre campagne de bannières.

## Combien de placements puis-je demander lors d'une session ?

En une seule demande d'actualisation, vous pouvez demander un maximum de 10 placements. Pour chaque demande, Braze renverra la bannière la plus prioritaire à laquelle un utilisateur peut prétendre. Toute demande supplémentaire entraînera une erreur.

Pour plus d'informations, voir [Demandes de placement]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %}).

## Combien de campagnes de bannières peuvent être actives simultanément ?

Chaque espace de travail peut prendre en charge jusqu'à 200 campagnes Banner actives. Si cette limite est atteinte, vous devrez [archiver ou désactiver]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) une campagne existante avant d'en créer une nouvelle.

## Pour les campagnes partageant un emplacement, quelle bannière est affichée en premier ?

Si un utilisateur se qualifie pour plusieurs campagnes de bannières qui partagent le même emplacement, la bannière ayant la priorité la plus élevée sera affichée. Pour plus d'informations, voir [Banner priority]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %}).

## Puis-je utiliser des bannières dans mon flux de cartes de contenu de type bannière existant ?

Les bannières sont différentes des cartes de type bannière, ce qui signifie que vous ne pouvez pas utiliser des bannières et des cartes de type bannière dans le même flux. Pour remplacer les flux de cartes de contenu existants par des bannières, vous devrez [créer des placements dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/placements/).

## Les utilisateurs peuvent-ils supprimer manuellement une bannière ?

Non. Les utilisateurs ne peuvent pas supprimer manuellement les bannières. Cependant, vous pouvez contrôler la visibilité de la bannière en gérant l'éligibilité des segments d'utilisateurs. Lorsqu'un utilisateur ne répond plus aux critères de ciblage d'une campagne Banner, il ne la verra plus lors de sa prochaine session.

Par exemple, si vous affichez une bannière promotionnelle jusqu'à ce qu'un utilisateur effectue un achat, le journal des événements utilisateurs ( `purchase_completed` ) peut supprimer cet utilisateur du segment ciblé, masquant ainsi la bannière dans les sessions suivantes.

## Puis-je exporter l'analyse/analytique de la campagne Bannières à l'aide de l'API Braze ?

Oui. Vous pouvez utiliser l'[endpoint`/campaigns/data_series` ]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) pour obtenir des données sur le nombre de campagnes Banner qui ont été vues, cliquées ou converties.

## Quand les utilisateurs sont-ils segmentés ?

Les utilisateurs sont segmentés au début de la session. Si les segments ciblés d'une campagne dépendent d'attributs personnalisés, d'événements personnalisés ou d'autres attributs de ciblage, ils doivent être présents sur l'utilisateur au début de la session.

## Comment puis-je composer des bannières pour garantir la plus faible latence possible ?

Plus l'envoi de messages dans votre bannière est simple, plus le rendu sera rapide. Il est préférable de tester votre campagne Banner par rapport à la latence attendue pour votre cas d'utilisation. Par exemple, veillez à tester les attributs liquides tels que `catalog_items`.

## Toutes les étiquettes Liquid sont-elles prises en charge ?

Non. Cependant, la plupart des étiquettes Liquid sont prises en charge pour les messages Banner, à l'exception de `catalog_items` qui est recréé à l'aide de l'[étiquette`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).

## Puis-je capturer des événements de clics ?

Les événements de clic ne sont capturés que si une action sur le clic est définie sur un élément `logClick` et est appelée à l'aide de la [passerelle JS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge).
