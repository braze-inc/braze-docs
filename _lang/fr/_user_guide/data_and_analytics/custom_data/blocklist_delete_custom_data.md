---
nav_title: Liste d’interdiction ou suppression des données personnalisées
article_title: Liste d’interdiction ou suppression des données personnalisées
page_order: 2
page_type: reference
description: "Cet article de référence explique comment bloquer ou supprimer des événements personnalisés, des attributs personnalisés ou des événements d’achat."
---

# Liste d’interdiction ou suppression des données personnalisées

Vous pouvez occasionnellement identifier des attributs personnalisés, des événements personnalisés ou des événements d’achat qui consomment trop de points de données, sont devenus obsolètes pour votre stratégie marketing ou ont été enregistrés par erreur. Pour empêcher l’envoi de ces données à Braze, vous pouvez bloquer un objet Données personnalisées pendant que votre équipe d’ingénierie travaille à le supprimer du backend de votre application ou de votre site Web.

Le processus de retrait d’un objet Données personnalisées est semblable à cela :

1. Vous ajoutez l’objet Données personnalisées à une [liste de blocage](#blocklisting-custom-data) afin qu’il ne soit plus enregistré.
2. Vous supprimez le code de vos déploiements du SDK Braze, des configurations CDP ou d’autres sources de données (c.-à-d. les données envoyées de votre backend à Braze via l’API) qui enregistrent cet objet Données personnalisées.
3. Votre gestionnaire du succès des clients ou l’équipe d’assistance de Braze supprime l’objet Données personnalisées de la liste des attributs personnalisés, des événements personnalisés ou des événements d’achat.

## Ajout à la liste de blocage des données personnalisées

L’ajout à la liste de blocage empêche Braze d’enregistrer un objet Données personnalisées particulier à l’avenir.

{% alert important %}
L’ajout à la liste de blocage ne supprime pas les données des profils utilisateur et ne diminue pas rétroactivement le nombre de points de données encourus pour cet objet Données personnalisées.
{% endalert %}

Pour ajouter un objet Données personnalisées à une liste de blocage :

1. Dans Braze, allez dans **Manage Settings (Gérer les paramètres)**.
2. Sélectionnez la page appropriée pour l’objet Données personnalisées que vous souhaitez bloquer : **Attribut personnalisé**, **Événement personnalisé** ou **Produits**.
3. Trouvez l’objet Données personnalisées dans le tableau.
4. Sélectionnez **Liste de blocage**.

![Avertissement qui vous empêche de bloquer un objet Données personnalisées et indique où les données personnalisées sont actuellement référencées.][1]{: style="max-width:50%;float:right;margin-left:15px;"}

Si l’objet Données personnalisées est toujours utilisé, vous devez le supprimer des filtres de segmentation ou des déclencheurs de campagne dans lesquels il est référencé avant de pouvoir le bloquer. Vous pouvez voir où les données personnalisées sont actuellement utilisées lorsque vous essayez de les bloquer.

Si les données personnalisées sont référencées à trop d’endroits différents, ou si vous souhaitez bloquer plusieurs éléments à la fois, veuillez contacter l’assistance pour obtenir de l’aide.

## Suppression de données personnalisées

Après avoir bloqué l’objet Données personnalisées et supprimé les références à celui-ci de votre application ou de votre site Web, votre gestionnaire du succès des clients ou l’équipe d’assistance supprimera les données personnalisées.

La suppression de données personnalisées se fait de la manière suivante :

- Supprime l’attribut personnalisé, l’événement personnalisé ou l’événement d’achat des sélections de filtres de segmentation et des pages analytiques.
- Supprime l’attribut personnalisé, l’événement personnalisé ou l’événement d’achat de la page correspondante dans **Manage Settings (Gérer les paramètres)**.

{% alert important %}
La suppression ne supprime pas les données déjà enregistrées sur les profils utilisateur ni n’empêche l’enregistrement supplémentaire des objets Données personnalisées sur les profils utilisateur. Assurez-vous que les données personnalisées ne sont plus enregistrées avant de supprimer l’événement ou l’attribut.
{% endalert %}

[1]: {% image_buster/assets/img_archive/blocklist_warning.png %}