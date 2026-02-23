---
nav_title: Tableau de bord des chiffres affaires du commerce électronique
article_title: Tableau de bord des chiffres affaires du commerce électronique
alias: "/ecommerce_revenue_dashboard/"
page_order: 6
description: "Cet article donne un aperçu du tableau de bord eCommerce Chiffre d'affaires - Attribution de la dernière touche."
---

# Tableau de bord des chiffres affaires du commerce électronique

> Le tableau de bord **eCommerce Revenue - Last Touch Attribution** permet de suivre le chiffre d'affaires attribué au dernier contact pour les campagnes et les canevas utilisant des [événements recommandés eCommerce]({{site.baseurl}}/ecommerce_events/). Utilisez ce tableau de bord pour comprendre quels sont les messages qui génèrent du chiffre d'affaires et pour suivre les performances globales du commerce électronique au fil du temps.

{% alert note %}
Les événements recommandés pour le commerce électronique sont actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client Braze si vous souhaitez participer à cet accès anticipé. <br><br>Si vous utilisez le nouveau [connecteur Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), ces événements recommandés seront automatiquement disponibles grâce à l'intégration. Dans le cas contraire, ces événements doivent être mis en œuvre avant que les données n'apparaissent dans ce tableau de bord.
{% endalert %}

Pour afficher votre tableau de bord des revenus du commerce électronique, allez dans **Analytics** > **Dashboard Builder (générateur de tableau de bord**), puis sélectionnez les **revenus du commerce électronique - Last Touch Attribution (attribution au dernier contact)**. Ce tableau de bord rend compte des chiffres d'affaires attribués à la dernière campagne ou Canvas avec laquelle un utilisateur a interagi avant de passer une commande, dans la fenêtre de conversion sélectionnée.

## Indicateurs disponibles

| Indicateurs | Définition |
| --- | --- |
| Revenu du commerce électronique | Total des chiffres d'affaires attribués au dernier contact en fonction de la plage de dates et de la fenêtre de conversion sélectionnées. |
| Commandes quotidiennes passées | Le nombre moyen de commandes distinctes passées par jour. |
| Revenu quotidien moyen du commerce électronique | Chiffre d'affaires moyen attribué par jour pour la période sélectionnée. |
| Revenus d’e-commerce – Au cours du temps | Une série chronologique des chiffres d'affaires attribués dans la plage de dates sélectionnée. |
| Revenu du commerce électronique par campagne | Chiffre d'affaires attribué ventilé par campagne. | 
| Revenu du commerce électronique par Canvas | Chiffre d'affaires attribué ventilé par Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Modèle d'attribution

Le tableau de bord **eCommerce chiffre d'affaires - Att** ribution au dernier contact utilise l'attribution au dernier contact. Cela signifie que les chiffres d'affaires sont attribués à la campagne la plus récente de Braze ou au Canvas avec lequel un utilisateur s'est engagé avant de passer une commande.

{% alert important %}
Les interactions entre les messages doivent avoir eu lieu dans la fenêtre de conversion sélectionnée. Les commandes qui n'ont pas fait l'objet d'un envoi de messages éligibles pendant la fenêtre de conversion ne sont pas attribuées.
{% endalert %}

## Données incluses

Le tableau de bord **eCommerce Revenue - Last Touch Attribution** extrait les données des événements recommandés pour l'eCommerce :

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

Le chiffre d'affaires et le nombre d'affaires sont calculés selon les normes de Braze.

| Indicateurs | Calcul |
| --- | --- |
| Total des revenus | Somme des valeurs des commandes passées - Somme des valeurs remboursées |
| Total des commandes | Ordres distincts passés - Ordres distincts annulés |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

### Données exclues

Les achats enregistrés à l'aide de l'événement d'achat hérité ne sont pas inclus. Le tableau de bord **eCommerce Revenue - Last Touch Attribution** ne prend actuellement pas en charge les fonctionnalités liées aux événements d'achat hérités, telles que les rapports sur la LTV ou le chiffre d'affaires au sein des campagnes ou des Canvases. 


## Traitement des devises

Tous les chiffres d'affaires sont affichés en USD. Les devises autres que l'USD sont converties en USD en utilisant le taux de change en vigueur à la date de l'événement. Pour éviter la conversion, indiquez en dur la devise à `USD` lors de l'envoi d'événements.
