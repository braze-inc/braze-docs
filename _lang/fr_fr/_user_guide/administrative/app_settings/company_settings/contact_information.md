---
nav_title: Informations sur le contact
article_title: Informations sur le contact
page_order: 0
page_type: reference
description: "Cet article de référence couvre des informations importantes pour les administrateurs sur la gestion des informations de contact et du fuseau horaire de votre entreprise dans Braze."

---

# Informations sur le contact

<style>
.fa-crown {
  color: gold;
}
</style>

> Cette page couvre des informations importantes pour les administrateurs sur la gestion des informations de contact et du fuseau horaire de votre entreprise dans Braze.

Pour accéder à cette page, allez dans **Réglages** > **Réglages administratifs** > **Informations de contact.**

C'est sur cette page que vous pouvez gérer les coordonnées et le fuseau horaire de votre entreprise. Veillez à sélectionner **Enregistrer** avant de quitter la page !

## Conséquences du changement de fuseau horaire

{% alert warning %}

Le changement de fuseau horaire peut entraîner des divergences de données autour du point où le fuseau horaire a été modifié. Si quelqu'un change de fuseau horaire, nous nous efforçons de bonne foi de convertir les données avec précision, mais la conversion n'est pas toujours parfaite. Il se peut que vous remarquiez une discontinuité dans vos données, où elles passent d'un fuseau horaire à l'autre.

{% endalert %}

Si vous décidez de changer de fuseau horaire, vous risquez de subir diverses conséquences, notamment

- Bien que les campagnes programmées à des heures précises dans des emplacements spécifiques (comme 21 heures, heure de l'Est) se dérouleront correctement selon la planification jusqu'à ce qu'elles soient modifiées, l'analyse/analyse des campagnes et les planifications des campagnes futures seront affectées par le changement.
- Toute planification de carte qui n'est pas assignée à l'heure locale peut être affectée, les cartes actives pouvant apparaître comme terminées ou l'inverse.
- Les filtres de segmentation de la forme "A fait X avant/après `Date`" verront l'heure ajustée car la date initiale sera désormais localisée à l'heure du Pacifique.