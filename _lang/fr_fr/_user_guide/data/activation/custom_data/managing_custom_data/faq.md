---
nav_title: FAQ
article_title: Gestion des données personnalisées - FAQ
page_order: 1
page_type: FAQ
description: "Cette page fournit des réponses aux questions fréquemment posées concernant la gestion des données personnalisées dans Braze."
---

# Foire aux questions

> Cette page fournit des réponses à certaines questions fréquemment posées concernant la gestion des données personnalisées.

### Pourquoi mon attribut personnalisé est-il détecté comme un type de données différent en production par rapport au développement ?

Braze détecte automatiquement le type de données d'un attribut personnalisé en fonction de la première valeur qu'il reçoit. Si votre environnement de développement envoie une valeur numérique telle que « premier`100` », l'attribut est stocké sous forme de nombre. Si la première valeur de votre environnement de production est une chaîne de caractères (par exemple,`"100"`entre guillemets), l'attribut est stocké sous forme de chaîne de caractères.

Pour éviter cela, veuillez vous assurer que votre intégration envoie des types de données cohérents dans tous les environnements. Si le type incorrect est déjà défini, vous pouvez imposer le type de données correct dans **Paramètres de données** > **Attributs personnalisés** en utilisant le [menu déroulant des types de données]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#forcing-data-type-comparisons).

### Si je modifie de force le type de données d'un attribut personnalisé, les données existantes seront-elles converties ?

Non. Le fait d'imposer un changement de type de données n'affecte que les nouvelles données entrant dans Braze. Toutes les données ingérées avant le changement de type continuent d'être stockées sous l'ancien type et peuvent ne pas être segmentables avec les filtres du nouveau type. Un avertissement apparaît sur les profils utilisateurs concernés. Pour les nouvelles données entrantes, si une valeur ne correspond pas au type imposé, Braze peut la convertir en type imposé (par exemple, la chaîne`"100"`de caractères en nombre`100`) ; les valeurs qui ne peuvent pas être converties sont ignorées et ne mettent pas à jour l'attribut.

Si vous avez besoin que toutes les données utilisateur existantes correspondent au nouveau type, il est nécessaire de renvoyer les valeurs d'attribut pour ces utilisateurs via le SDK, l'API ou une importation CSV. Il n'existe pas de conversion automatique en masse pour les données existantes.

### Comment puis-je éviter les problèmes liés aux types de données lorsque j'utilise l'ingestion de données (CDI) ?

Lorsque vous utilisez CDI pour synchroniser des données provenant de sources externes (telles que Databricks ou Snowflake), veuillez vous assurer que les colonnes source utilisent les types de données appropriés avant la synchronisation. Les problèmes courants incluent :

- **Horodatages enregistrés sous forme de chaînes de caractères** : Veuillez vous assurer que vos colonnes de date utilisent un type horodatage ou date-heure dans votre base de données source, et non un type varchar ou chaîne de caractères.
- **Nombres stockés sous forme de chaînes de caractères** : Veuillez convertir les colonnes numériques en types entiers ou float dans votre requête source avant la synchronisation.
- **Types incohérents entre les synchronisations** : Si le type d'une colonne change entre deux synchronisations, Braze peut refuser les nouvelles données. Veuillez vérifier que votre schéma source reste cohérent.
