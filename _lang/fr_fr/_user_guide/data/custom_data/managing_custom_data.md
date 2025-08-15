---
nav_title: Gestion des données personnalisées
article_title: Gestion des données personnalisées
page_order: 20
page_type: reference
description: "Cet article de référence explique comment gérer les données personnalisées, par exemple en pré-remplissant les campagnes et les segments ou en bloquant et en supprimant des données."
---

# Gestion des données personnalisées

> Cette page explique comment pré-remplir les données personnalisées dans vos campagnes et vos segments, mettre en liste de blocage les données qui ne sont plus utiles et gérer les événements et attributs personnalisés ainsi que les propriétés.<br><br>Pour savoir comment gérer les attributs personnalisés en particulier, reportez-vous à la section [Gestion des attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).

## Pré-remplissage des données personnalisées

Il peut arriver que vous souhaitiez implémenter des campagnes et des segments à l'aide de données personnalisées avant que votre équipe de développement n'ait intégré ces données. Braze vous permet de pré-renseigner des événements et des attributs personnalisés sur le tableau de bord avant que ne commence le suivi de ces données, pour que ces événements et attributs soient disponibles dans les menus déroulants et durant le processus de création de campagnes.

Pour pré-remplir les événements et attributs personnalisés, procédez comme suit :

1. Allez dans **Paramètres des données** > **Événements personnalisés** ou **Attributs personnalisés** ou **Produits**.

![Naviguez vers les attributs personnalisés ou les événements personnalisés ou les produits.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2\. Pour ajouter un attribut personnalisé, un événement ou un produit, accédez à la page correspondante et sélectionnez **Ajouter des attributs personnalisés** ou **Ajouter des événements personnalisés** ou **Ajouter des produits**.<br><br>Pour les attributs personnalisés, sélectionnez un [type de données]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) pour cet attribut (par exemple, booléen ou chaîne de caractères). Le type de données d’un attribut détermine les filtres de segmentation disponibles pour cet attribut. <br><br>![Ajouter un nouvel attribut ou événement]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3\. Sélectionnez **Enregistrer**.

### Attribution de noms aux événements et attributs personnalisés

Les événements personnalisés et les attributs personnalisés sont sensibles à la casse. Gardez cela à l'esprit lorsque votre équipe de développement intégrera ultérieurement ces événements et attributs personnalisés. Ils doivent nommer les événements et attributs personnalisés exactement comme vous les avez nommés ici, sinon Braze générera un événement ou un attribut personnalisé différent.

## Gestion des propriétés

Après avoir créé un événement personnalisé ou un produit, sélectionnez **Gérer les propriétés de** cet événement ou de ce produit pour ajouter de nouvelles propriétés, dresser une liste de blocage des propriétés existantes et afficher les campagnes ou les toiles qui utilisent cette propriété dans un [événement déclencheur]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

![Propriétés d'un événement personnalisé.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Pour assurer la traçabilité des attributs personnalisés, événements, produits ou propriétés d'événement ajoutés, vous devez demander à votre équipe de développement de les créer dans le SDK en utilisant le nom exact que vous avez utilisé pour les ajouter précédemment. Vous pouvez également utiliser l'[API]({{site.baseurl}}/api/basics/) de Braze pour importer des données sur cet attribut. Ensuite, l'attribut personnalisé, l'événement ou autre sera exploitable et s'appliquera à vos utilisateurs.

{% alert note %}
Toutes les données des profils utilisateurs (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs.
{% endalert %}

## Ajout à la liste de blocage des données personnalisées

Vous pouvez occasionnellement identifier des attributs personnalisés, des événements personnalisés ou des événements d'achat qui soit consomment trop de points de données, soit ne sont plus utiles à votre stratégie de marketing, soit ont été enregistrés par erreur. 

Pour empêcher l’envoi de ces données à Braze, vous pouvez bloquer un objet Données personnalisées pendant que votre équipe d’ingénierie travaille à le supprimer du backend de votre application ou de votre site Web. La mise en liste bloquée empêche un objet de données personnalisé particulier d'être enregistré par Braze à l'avenir, ce qui signifie qu'il n'apparaîtra pas lors de la recherche d'un utilisateur spécifique.

{% alert important %}
Pour mettre en liste de blocage des données personnalisées, vous devez disposer des [autorisations du client]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) pour accéder et modifier les campagnes, les Canvases et les segments.
{% endalert %}

Les données en liste de blocage ne seront pas envoyées par le SDK et le tableau de bord de Braze ne traitera pas les données en liste de blocage provenant d'autres sources (par exemple, l'API). Cependant, le blocage ne supprime pas les données des profils utilisateurs et ne diminue pas rétroactivement le nombre de points de données encourus pour cet objet personnalisé.

### Bloquer des attributs personnalisés, des événements personnalisés et des produits

{% alert important %}
Lorsqu'un événement ou un attribut est mis sur liste de blocage, tout segment, campagne ou canvas utilisant cet événement ou cet attribut sera archivé.
{% endalert %}

Pour arrêter le suivi d'un attribut personnalisé, d'un événement ou d'un produit spécifique, procédez comme suit :

1. Recherchez-la dans les pages **Attributs personnalisés**, **Événements personnalisés** ou **Produits**.
2. Sélectionnez l'attribut personnalisé, l'événement ou le produit. Pour les attributs et les events personnalisés, vous pouvez en sélectionner jusqu'à 100 à la fois.
3. Sélectionnez **Liste de blocage**.

![Plusieurs attributs personnalisés sélectionnés qui sont mis en liste de blocage sur la page Attributs personnalisés.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Vous pouvez placer en liste de blocage jusqu'à 300 attributs personnalisés et 300 événements personnalisés. Pour empêcher la collecte de certains attributs d'appareils, consultez notre [guide SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection). 

{% alert important %}
Les événements et attributs personnalisés dont le statut est **"à la poubelle** " sont pris en compte dans le calcul de la limite de blocage jusqu'à ce qu'ils soient supprimés.
{% endalert %}

Lorsqu'un événement ou un attribut personnalisé est placé en liste de blocage, les règles suivantes s'appliquent :

- Aucune donnée envoyée à Braze ne sera traitée, et les événements et attributs inscrits sur la liste de blocage ne compteront plus comme des points de données
- Les données existantes seront indisponibles, à moins qu'elles ne soient réactivées
- Les événements et attributs mis en liste bloquée n'apparaîtront pas dans les filtres ou les graphiques.
- Les références aux données de la liste de blocage dans les brouillons des toiles actives seront chargées en tant que valeurs non valides, ce qui peut entraîner des erreurs.
- Tout ce qui utilise l'événement ou l'attribut figurant sur la liste de blocage sera archivé.

Pour ce faire, Braze envoie les informations de blocage à chaque appareil. Ceci est important lorsque vous envisagez de mettre sur liste de blocage un grand nombre d'événements et d'attributs (des centaines de milliers ou des millions), car l'opération serait très gourmande en données.

### Considérations relatives à l'inscription sur la liste de blocage

Il est possible de bloquer un grand nombre d'événements et d'attributs, mais ce n'est pas conseillé. En effet, chaque fois qu’un événement est exécuté ou qu’un attribut est (potentiellement) envoyé à Braze, cet événement ou cet attribut doit être vérifié par rapport à l’ensemble de la liste de blocage.

Jusqu'à 300 éléments sont envoyés au SDK pour la mise en liste de blocage. Si vous mettez en liste de blocage plus de 300 éléments, ces données seront envoyées par le SDK. Si vous n'avez pas besoin d'utiliser l'événement ou l'attribut à l'avenir, envisagez de le supprimer du code de votre application lors de votre prochaine mise à jour. Les modifications apportées à la liste de blocage peuvent prendre quelques minutes pour se propager. Vous pouvez réactiver n'importe quel événement ou attribut de la liste de blocage à tout moment.

## Suppression de données personnalisées

Au fur et à mesure que vous créez des campagnes et des segments ciblés, vous constaterez peut-être que vous n'avez plus besoin d'un événement personnalisé ou d'un attribut personnalisé. Par exemple, si vous avez utilisé un attribut personnalisé spécifique dans le cadre d'une campagne ponctuelle, vous pouvez supprimer cette donnée après l'avoir [mise en liste bloquée](#blocklisting-custom-attributes-custom-events-and-products) et supprimer ses références de votre application. Vous pouvez supprimer tous les types de données (tels que les chaînes de caractères, les nombres et les attributs personnalisés imbriqués).

{% alert important %}
Vous devez être un [administrateur de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) pour supprimer des données personnalisées.
{% endalert %}

Pour supprimer un événement personnalisé et un attribut personnalisé, procédez comme suit :

1. Allez dans **Paramètres des données** > **Attributs personnalisés** ou **Événements personnalisés**, selon le type de données que vous souhaitez supprimer.
2. Accédez aux données personnalisées et sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i> **Actions** > **Blocklist**.
3. Après que vos données personnalisées ont été bloquées pendant 7 jours, sélectionnez <i class="fa-solid fa-ellipsis-vertical"></i> **Actions** > **Supprimer.**

### Comment fonctionne la suppression

Lorsque vous supprimez des données personnalisées, le phénomène suivant se produit : 

- **Pour les attributs personnalisés :** Supprime définitivement les données d'attributs du profil de chaque utilisateur.
- **Pour les événements personnalisés :** Supprime définitivement les métadonnées de l'événement du profil de chaque utilisateur.

Lorsqu'un attribut ou un événement est sélectionné pour être supprimé, son statut passe à la **corbeille**. Pendant les sept jours suivants, il est possible de restaurer l'attribut ou l'événement. Si vous ne le restaurez pas au bout de sept jours, les données seront définitivement supprimées. Si vous restaurez l'attribut ou l'événement, il reviendra à l'état de liste bloquée.

La suppression n'empêche pas l'enregistrement des objets de données personnalisées sur les profils d'utilisateurs. Assurez-vous donc que les données personnalisées ne sont plus enregistrées avant de supprimer les événements et les attributs.

### Choses à savoir

Lorsque vous supprimez des données personnalisées, gardez à l'esprit les détails suivants :

* **La suppression est permanente**. Les données ne peuvent pas être récupérées.
* Les données sont supprimées de la plateforme Braze et des profils utilisateurs.
* Vous pouvez "réutiliser" le nom de l'attribut personnalisé ou de l'événement personnalisé après sa suppression. Cela signifie que si vous remarquez que des données personnalisées "réapparaissent" dans Braze après avoir été supprimées, cela peut être dû à une intégration qui n'a pas été arrêtée et qui envoie des données avec le même nom de données personnalisées.
* Il se peut que vous deviez à nouveau placer un élément sur liste de blocage si votre suppression entraîne la réapparition de données personnalisées. Le statut de liste de blocage n'est pas préservé car les données personnalisées sont supprimées.
* La suppression de données personnalisées ne consomme aucun [point de données]({{site.baseurl}}/user_guide/data/data_points) et ne génère pas non plus de nouveaux points de données à utiliser.

## Forcer les comparaisons de type de données

Braze reconnaît automatiquement les types de données pour les données d’attribut qui nous sont envoyées. Cependant, dans l’éventualité où plusieurs types de données sont appliqués à un seul attribut, vous pouvez forcer le type de données de n’importe quel attribut pour nous faire savoir ce qu’il est réellement. Sélectionnez dans la liste déroulante de la colonne **Type de données**.

{% alert note %}
Forcer les types de données ne s’applique pas aux propriétés de l’événement ou aux propriétés d’achat.
{% endalert %}

![Attributs personnalisés, type de données, liste déroulante]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Si vous choisissez de forcer le type de données d'un attribut, toute donnée entrante qui n'est pas du type spécifié sera contrainte dans ce type. Si une telle coercition est impossible (par exemple, une chaîne de caractères transformée en un nombre), les données seront ignorées. Toutes les données ingérées avant le changement de type continueront d'être stockées sous l'ancien type (et ne pourront donc pas être segmentées), et un avertissement apparaîtra à côté de l'attribut sur les profils des utilisateurs concernés.
{% endalert %}

### Contrainte de type de données

| Type de données forcées | Description |
|------------------|-------------|
| Valeur booléenne | Les entrées de `1`, `true`, `t` (non sensibles à la casse) seront conservées comme `true` |
| Valeur booléenne | Les entrées de `0`, `false`, `f` (non sensibles à la casse) seront conservées comme `false` |
| Nombre | Les nombres entiers ou flottants (tels que `1`, `1.5`) seront stockés en tant que nombres. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'informations sur les options de filtrage spécifiques exposées par les différentes comparaisons de types de données, consultez le [rapport de configuration.]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting) Pour plus d'informations sur les différents types de données disponibles, reportez-vous à la section [Types de données d'attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).

{% alert note %}
Les données envoyées à Braze sont immuables et ne peuvent être supprimées ou modifiées après leur réception. Cependant, vous pouvez recourir à l’une des méthodes énumérées dans les sections précédentes pour exercer un contrôle sur ce que vous suivez dans votre tableau de bord.
{% endalert %}


