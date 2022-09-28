---
nav_title: FAQ
article_title: FAQ sur les Exportations
page_order: 11
page_type: FAQ
description: "Cet article couvre quelques questions fréquemment posées sur les exportations API et CSV."

---

# FAQ sur les Exportations

> Cette page fournit des réponses à certaines questions fréquemment posées sur les exportations API et CSV.

### Peut–on faire apparaître certaines exportations dans le compartiment S3  d’un client, et pas d’autres ?

Non. Si vous avez fourni des informations d’identification S3, toutes vos exportations apparaîtront dans votre compartiment S3 ; sinon, si aucune information d’identification n’est fournie, toutes les exportations apparaîtront dans un compartiment S3 appartenant à Braze.

### Dois-je ajouter des informations d'identification S3 à Braze pour exporter des données ?

Non. Les clients qui n’ajoutent pas d’informations d'identification S3 verront toutes leurs exportations apparaître dans un compartiment S3 appartenant à Braze.

### Que se passe-t-il si vous configurez des informations d'identification S3 dans le tableau de bord, sans sélectionner « destination par défaut pour l’exportation des données » ?

Cette case à cocher aura un impact sur les exportations vers S3 ou Azure, en supposant que vous ayez ajouté des identifiants pour les deux.

### Pourquoi ai-je reçu plusieurs fichiers lors de l’exportation de profils d’utilisateurs vers S3 ?

Il s’agit d’un comportement attendu pour les groupes d’apps avec beaucoup d’utilisateurs. Nous divisons votre exportation en plusieurs fichiers, en fonction du nombre d’utilisateurs dans votre groupe d’apps. En général, un fichier de sortie est créé tous les 5 000 utilisateurs. Notez que si vous exportez un petit segment dans un grand groupe d’apps, vous  recevrez peut-être quand même plusieurs fichiers.

### Pourquoi puis-je voir les doublons lorsque j’exporte des utilisateurs par segment via API Rest ?

C’est un cas très rare causé par l’architecture sous-jacente du fournisseur de base de données. Les doublons sont nettoyés toutes les semaines mais la plupart des semaines, il n’y a pas de doublons à supprimer.
