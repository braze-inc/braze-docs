---
nav_title: Coordonnées
article_title: Coordonnées
page_order: 0
page_type: reference
description: "Cet article de référence contient des informations importantes pour les administrateurs sur la gestion des coordonnées et du fuseau horaire de votre entreprise à Braze."

---

# Coordonnées

<style>
.fa-crown {
  color: gold;
}
</style>

> Cette page couvre des informations importantes pour les administrateurs sur la gestion des informations de contact de votre entreprise et du fuseau horaire dans Braze.

Pour accéder à cette page, allez dans **Paramètres** > **Paramètres d'administration** > **Informations de contact**.

Cette page est l'endroit où vous pouvez gérer les informations de contact de votre entreprise et le fuseau horaire. Assurez-vous de cliquer sur **Enregistrer** avant de quitter la page !

## Conséquences du changement de fuseau horaire

{% alert warning %}

Les fuseaux horaires peuvent entraîner des écarts de données au moment où le fuseau horaire a été modifié. En cas de changement de fuseau horaire, nous nous efforçons de convertir les données avec précision, mais la conversion n’est pas toujours parfaite. Vous pouvez remarquer une discontinuité dans vos données, susceptibles de basculer entre les fuseaux horaires.

{% endalert %}

Si vous choisissez de changer de fuseau horaire, vous risquez de subir diverses conséquences, notamment :

- Bien que les campagnes programmées pour des heures spécifiques dans des lieux spécifiques (comme 21h heure de l'Est) se dérouleront correctement selon le calendrier jusqu'à leur modification, les analyses de campagne et les futurs calendriers de campagne seront affectés par le changement.
- Toute planification de carte qui n'est pas assignée à l'heure locale peut être affectée, avec des cartes actives pouvant apparaître comme terminées ou inversement.
- Les filtres de segmentation de la forme « A fait X avant/après `Date` » verront l’heure ajustée, car la date initiale sera désormais localisée en heure du Pacifique.