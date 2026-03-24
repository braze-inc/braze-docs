---
nav_title: Coordonnées
article_title: Coordonnées
page_order: 0
page_type: reference
description: "Cet article de référence contient des informations importantes pour les administrateurs sur la gestion des coordonnées et du fuseau horaire de votre entreprise à Braze."

---

# Coordonnées

> En tant qu'administrateur, vous pouvez utiliser la page **Informations de contact** pour gérer les coordonnées et le fuseau horaire de votre entreprise dans Braze.

Pour accéder à cette page, allez dans **Paramètres** > **Paramètres d'administration** > **Informations de contact**. Veuillez sélectionner **Enregistrer** pour appliquer les modifications avant de quitter la page.

## Conséquences du changement de fuseau horaire

{% alert warning %}
Le changement de fuseau horaire peut entraîner des divergences dans les données autour de la période où le fuseau horaire a été modifié. Si vous modifiez votre fuseau horaire, Braze s'efforce de convertir les données avec précision, mais ne garantit pas une conversion parfaite. Vous pouvez remarquer une discontinuité dans vos données, susceptibles de basculer entre les fuseaux horaires.
{% endalert %}

Si vous choisissez de changer de fuseau horaire, vous risquez de subir diverses conséquences, notamment :

- Bien que les campagnes programmées pour des heures spécifiques dans des lieux spécifiques (comme 21h heure de l'Est) se dérouleront correctement selon le calendrier jusqu'à leur modification, les analyses de campagne et les futurs calendriers de campagne seront affectés par le changement.
- Toute planification de carte qui n'est pas assignée à l'heure locale peut être affectée, avec des cartes actives pouvant apparaître comme terminées ou inversement.
- Les filtres de segmentation de la forme « A effectué X avant/après `Date`» verront leur heure ajustée, car la date initiale sera désormais localisée dans le fuseau horaire par défaut de votre espace de travail (par exemple, l'heure du Pacifique).
