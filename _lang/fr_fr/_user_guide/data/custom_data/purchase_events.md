---
nav_title: Événements d’achat
article_title: Événements d’achat
page_order: 8
page_type: reference
description: "Cet article de référence décrit les événements et propriétés d’achat, leur utilisation, leur segmentation, où voir les analyses qui s’y rapportent, etc."
search_rank: 3
---

# Événements d’achat

> Cette page traite des propriétés d'achat et des événements, de leur utilisation, de la segmentation, de l'affichage des analyses pertinentes, etc.

Les événements d'achat sont des actions d'achat effectuées par vos utilisateurs, et sont utilisés pour enregistrer les achats in-app et établir la valeur vie (LTV) pour chaque profil utilisateur. Ces événements doivent être mis en place par votre équipe. L'enregistrement des événements d'achat vous permet d'ajouter des propriétés telles que la quantité et le type, ce qui vous aide à mieux cibler vos utilisateurs en fonction de ces propriétés.

## Enregistrement des événements d’achat

Vous pouvez enregistrer les achats en transmettant un [objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/) par l'intermédiaire de l'[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

La liste suivante énumère les méthodes utilisées pour enregistrer les achats sur les différentes plateformes. Dans ces pages, vous trouverez également de la documentation sur la manière d'ajouter des propriétés et des quantités à votre événement d'achat. Vous pouvez ensuite cibler vos utilisateurs en fonction de ces propriétés.

- [Android et FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

## Consultation des données d'achat

Une fois que vous avez configuré et commencé à enregistrer les événements utilisateurs, vous pouvez consulter ces données sur le profil d'un utilisateur dans l' [onglet Aperçu.]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab)

## Utilisation des données d'achat

Vous pouvez utiliser les données d'achat de plusieurs façons dans Braze :

- **[Segmentation](#purchase-event-segmentation):** Utilisez les données comportementales pour créer des segments d'utilisateurs en fonction de leur comportement d'achat.
- **[Personnalisation](#personalization):** Utilisez les données relatives aux achats pour personnaliser les messages adressés aux utilisateurs.
- **[Déclencher des messages](#trigger-messages) :** Configurez les messages pour qu'ils se déclenchent en fonction des événements d'achat.
- **[Analyses](#analytics) :** Analysez vos données d'achat pour obtenir des informations sur le comportement des utilisateurs et l'efficacité de vos campagnes marketing.

### Segmentation {#purchase-event-segmentation}

Vous pouvez déclencher n'importe quel nombre ou type de campagnes de suivi sur la base des événements d'achat enregistrés. Par exemple, vous pouvez créer un segment d'utilisateurs ayant effectué un achat au cours des 30 derniers jours, ou un segment d'utilisateurs ayant dépensé plus d'un certain montant.

Les filtres de segmentation suivants sont disponibles pour le ciblage des utilisateurs :

- Premier achat
- Premier achat pour l'application
- Dernier produit acheté
- Argent dépensé
- Produit acheté
- Nombre total d’achats
- X argent dépensé en Y jours
- X produits achetés en Y jours
- X propriétés d’achat en Y jours
- X achats dans les Y derniers jours

Pour plus de détails sur chaque filtre, consultez le glossaire des [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) et filtrez par "comportement d'achat".

![Filtrage des utilisateurs ayant effectué exactement trois achats]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Pour segmenter le nombre de fois qu'un achat spécifique a été effectué, enregistrez cet achat individuellement en tant qu'[attribut personnalisé incrémentiel]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

### Personnalisation

Comme tout autre type de données que vous collectez auprès de vos utilisateurs, vous pouvez utiliser les données d'achat pour personnaliser votre envoi de messages grâce à Liquid. Par exemple, vous pouvez envoyer un e-mail personnalisé à un utilisateur en lui recommandant des produits similaires à ceux qu'il vient d'acheter.

Supposons que vous disposiez d'une propriété d'événement d'achat appelée `last_purchased_product` qui stocke le nom du dernier produit acheté par un utilisateur. Vous pouvez utiliser cette propriété pour personnaliser un message e-mail comme suit :

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

Dans cet exemple, le message est personnalisé en fonction de la propriété `last_purchased_product`. Si le dernier produit acheté par l'utilisateur était "Chaussures de course", il reçoit un message lui recommandant des shorts de course et des bouteilles d'eau. Si le dernier produit était un « tapis de yoga », il reçoit un message recommandant des blocs et des sangles de yoga. Si le `last_purchased_product` est autre chose, il reçoit un message de remerciement générique.

### Déclencher des messages

Un cas d'utilisation courant consiste à envoyer automatiquement un message, par exemple un e-mail, lorsqu'un utilisateur effectue un achat. Vous pouvez par exemple envoyer un message de remerciement ou un code de réduction pour un prochain achat.

Pour ce faire, créez une campagne ou un Canvas basé sur une action, puis définissez l'action de déclenchement sur **Effectuer un achat**. Vous pouvez également spécifier des conditions supplémentaires pour le déclencheur, telles que le produit acheté ou le montant de l'achat.

Vous pouvez également personnaliser votre message déclenché avec Liquid. Dans l'exemple suivant, `${purchase_product_name}` est un attribut personnalisé que vous remplacerez par le nom de l'attribut qui stocke le nom du produit acheté dans votre configuration Braze.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Analyse

En plus du suivi des indicateurs d'achat pour la segmentation, Braze note également le nombre d'achats pour chaque produit et le chiffre d'affaires généré au fil du temps. Cela peut être utile pour identifier les produits les plus populaires ou mesurer l'impact d'une campagne promotionnelle sur les ventes.

Vous trouverez ces données sur la page du [rapport sur les recettes.]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) 

### Calcul du chiffre d'affaires

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Revenus à vie</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valeur vie client par utilisateur</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Chiffre d'affaires quotidien moyen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">Achats quotidiens</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Revenus quotidiens par utilisateur</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Calcul du chiffre d'affaires à vie

Braze utilise les événements d'achat pour calculer le chiffre d'affaires à vie (également appelé valeur vie ou LTV) d'un utilisateur, qui est une prédiction du bénéfice net attribué à l'ensemble de la relation future avec un client. Ceci peut vous aider à prendre des décisions éclairées sur les stratégies d'acquisition et de rétention des clients.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Il y a deux endroits principaux dans Braze auxquels vous pouvez vous référer pour comprendre la LTV de vos utilisateurs :

- Pour obtenir des indicateurs globaux tels que le *chiffre d'affaires à vie* et la *valeur vie client par utilisateur* pour chaque appli et chaque site, consultez votre [rapport de chiffre d’affaires]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- Pour comprendre le chiffre d'affaires à vie d'un utilisateur spécifique, reportez-vous à son [profil utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Impact des remboursements sur les revenus à vie

Lorsque vous utilisez des événements d'achat pour suivre les données d'achat, vous devez suivre les remboursements en enregistrant un événement d'achat Braze avec une propriété d'achat négative `price`. Cette approche permet de maintenir un chiffre d'affaires précis pour toute la durée de vie du produit.

Toutefois, n'oubliez pas que le remboursement sera considéré comme un événement d'achat supplémentaire. Prenons l'exemple suivant. Sam effectue son premier achat pour 12 $ mais retourne une partie de l'achat pour un remboursement de 5 $. Le profil de Sam enregistrera :

- 1 achat de 12 $
- 1 achat de -5 $
- Revenu à vie de 7 $

Alors que le profil de Sam présente deux événements d'achat, il n'a en réalité effectué qu'un seul achat. Il est important d'en tenir compte si vous avez des segments ou des cas d'utilisation créés autour du nombre d'achats effectués par un utilisateur. Les remboursements constants gonflent le nombre d'achats sur le profil utilisateur.

## Propriétés de l’événement d’achat {#purchase-properties}

Avec les propriétés de l'événement d’achat, vous pouvez définir des propriétés sur les achats pour qualifier plus précisément les conditions de déclenchement, améliorer la personnalisation des messages et générer des analyses plus sophistiquées via l’exportation de données brutes. Les types de valeurs des propriétés (chaîne de caractères, numérique, booléenne, date) varient selon la plate-forme et sont souvent attribués sous forme de paires clé-valeur.

Par exemple, si vous avez une application de commerce électronique et que vous souhaitez envoyer un message à un utilisateur après avoir effectué un achat, vous pourriez en outre améliorer votre audience cible et permettre une personnalisation accrue de la campagne en ajoutant une propriété d'événement d'achat de `brand_name`.

**Exemple de déclenchement basé sur les propriétés d'un événement d'achat :**

![Paramètres de réception/distribution par événement pour envoyer une campagne aux utilisateurs qui achètent des écouteurs d'une marque égale à HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Pour en savoir plus, reportez-vous à l'[objet propriétés d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object).

### Segmentation des propriétés de l’événement

La segmentation des propriétés d'événements vous permet de cibler les utilisateurs en fonction non seulement des événements personnalisés pris, mais aussi des propriétés associées à ces événements. Cette fonctionnalité ajoute des options de filtrage supplémentaires lors de la segmentation des achats et des événements personnalisés.

![]({% image_buster /assets/img/nested_object3.png %}){: style="max-width:80%;margin-left:15px;"}

Ces filtres de segmentation comprennent :
- A effectué l'événement personnalisé avec la propriété Y et la valeur V X fois au cours des Y derniers jours.
- A effectué des achats avec le bien Y d'une valeur V X fois au cours des Y derniers jours
- Ajoute une segmentation de 1 à 30 jours sur tous les achats, les événements et les propriétés d'achats et d'événements.

Contrairement aux [extensions de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), les segments utilisés sont mis à jour en temps réel, prennent en charge un nombre illimité de segments, offrent un historique de 30 jours au maximum et encourent des points de données. En raison des frais liés aux points de données supplémentaires, vous devez contacter votre gestionnaire de satisfaction client Braze pour activer les propriétés d'événement pour vos événements personnalisés.

Une fois approuvées, des propriétés supplémentaires peuvent être ajoutées dans le tableau de bord sous **Paramètres des données** > **Événements personnalisés** en sélectionnant **Gérer les propriétés.** Vous pouvez ensuite utiliser ces propriétés d'événement dans l'étape cible de la campagne ou du générateur de canvas.

### Propriétés d’entrée et propriétés de l’événement Canvas

{% multi_lang_include canvas_entry_event_properties.md %}

### Journaliser les achats au niveau de la commande

Pour enregistrer les achats au niveau de la commande plutôt qu'au niveau du produit, utilisez le nom ou la catégorie de la commande comme `product_id`. Pour en savoir plus, reportez-vous aux [spécifications de l'objet de l'achat]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Conventions de nommage des ID de produit

Chez Braze, nous proposons des conventions générales de nommage pour l’objet Achat `product_id`. Lorsque vous choisissez `product_id`, Braze suggère d’utiliser des noms simples tels que le nom du produit ou la catégorie de produit (au lieu des unités de gestion des stocks) dans l’intention de regrouper tous les éléments enregistrés par ce `product_id`.

Cela permet de faciliter l’identification des produits pour la segmentation et le déclenchement. 

## Exclure des événements d’achat

Vous pouvez occasionnellement identifier des événements d'achat qui soit consomment trop de points de données, soit ne sont plus utiles à votre stratégie marketing, soit ont été enregistrés par erreur. Pour empêcher l'envoi de ces données à Braze, vous pouvez mettre l'objet de données personnalisé sur liste de blocage pendant que votre équipe d'ingénieurs travaille à sa suppression du backend de votre appli ou de votre site web.

Dans le tableau de bord de Braze, vous pouvez gérer la mise en liste de blocage à partir de **Paramètres des données** > **Produits**. Pour en savoir plus, consultez la rubrique [Gérer les données personnalisées]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/).

