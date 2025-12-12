---
nav_title: Différence entre la liste d’exclusion et la suppression
article_title: Différence entre la liste d’exclusion et la suppression
page_order: 2

page_type: solution
description: "Cet article d’aide vous explique la différence entre la liste de blocage et la suppression d’attributs."
---

# Différence entre la liste d’exclusion et la suppression

Pour comprendre la différence entre placer des attributs dans une liste de blocage et les supprimer dans Braze, examinons les résultats de chaque action :

- **Liste de blocage :** Si des attributs personnalisés, des événements ou des achats sont bloqués, ils resteront sur le profil utilisateur, mais aucune nouvelle demande pour l’attribut ne sera traitée.
- **Suppression :** Si des attributs personnalisés, des événements ou des achats sont supprimés, les données seront supprimées. Cependant, Braze acceptera toujours les nouvelles requêtes entrantes pour cet attribut s'il est toujours suivi via le SDK ou chargé via l'API ou un fichier CSV.

## Comment choisir ?

Pour placer un attribut dans une liste de blocage, Braze devra envoyer les informations de mise en liste de blocage à l'appareil de chaque utilisateur, et il s'agira d'une opération gourmande en données, ce que nous essayons idéalement d'éviter. De plus, si la liste est trop importante (> 100 attributs, événements ou achats), votre application peut en être ralentie. 

Si vous prévoyez de ne plus d'envoyer un attribut spécifique à Braze, il est préférable de le supprimer.

Quel que soit votre itinéraire, les attributs personnalisés, les événements et les achats que vous souhaitez supprimer n'apparaîtront plus sur la page **Gérer l'espace de travail**, qui les supprime en tant que filtres de segmentation. Les données au niveau utilisateur resteront sur les profils. 