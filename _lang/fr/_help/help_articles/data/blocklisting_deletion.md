---
nav_title: Différence entre la liste d’exclusion et la suppression
article_title: Différence entre la liste d’exclusion et la suppression
page_order: 0

page_type: solution
description: "Cet article d’aide vous explique la différence entre la liste de blocage et la suppression d’attributs."
---

# Différence entre la liste d’exclusion et la suppression

La différence entre la liste d’exclusion et la suppression est la suivante :
- Liste de blocage : Si des attributs personnalisés, des événements ou des achats sont bloqués, ils resteront sur le profil utilisateur, mais aucune nouvelle demande pour l’attribut ne sera traitée.
- Suppression : Si des attributs personnalisés, des événements ou des achats sont supprimés, les données seront supprimées, mais Braze acceptera toujours les nouvelles demandes entrantes pour cet attribut s’il est toujours suivi via le SDK ou téléchargé via l’API ou CSV. 

## Comment choisir ?

Pour réaliser la liste de blocage, Braze devra envoyer les informations de la liste de blocage à l’appareil de chaque utilisateur et ce sera une opération gourmande en données, que nous essayons idéalement d’éviter. De plus, si la liste est trop longue (> 100 attributs, événements ou achats), votre application peut commencer à ralentir. Si vous ne prévoyez plus d’envoyer des attributs à Braze, la suppression serait l’approche recommandée.

Quel que soit votre itinéraire, les attributs personnalisés, les événements et les achats que vous souhaitez supprimer n’apparaîtront plus sur la page **Manage App Group** (Gérer le groupe d’apps), qui les supprime en tant que filtres de segment. Les données au niveau utilisateur resteront sur les profils. 

