---
nav_title: Foire aux questions
article_title: Exporter la FAQ
page_order: 11
page_type: Foire Aux Questions
description: "Cet article couvre certaines questions fréquemment posées pour les exportations API et CSV."
---

# Exporter la FAQ

> Cette page fournit des réponses à certaines questions fréquemment posées sur les exportations API et CSV.

### Pouvez-vous faire apparaître certaines exportations dans le compartiment S3 d'un client, et pas certaines exportations ?

Non. Si vous avez fourni les identifiants S3, tous vos exports apparaîtront dans votre compartiment S3 ; sinon, si aucun identifiant n'est fourni, toutes les exportations apparaîtront dans un segment S3 appartenant à Braze.

### Dois-je ajouter des informations d'identification S3 à Braze pour exporter des données ?

Non. Les clients qui n'ajouteront pas d'identifiants S3 verront toutes leurs exportations apparaître dans un seau S3 appartenant à Braze.

### Que se passe-t-il si vous avez configuré les identifiants S3 dans le tableau de bord, mais que vous ne sélectionnez pas « faire de cela la destination par défaut de l'exportation de données?»

Cette case à cocher aura un impact sur les exportations vers S3 ou Azure, en supposant que vous ayez ajouté des informations d'identification pour les deux.

### Pourquoi ai-je reçu plusieurs fichiers lors de l'exportation des profils d'utilisateurs vers S3 ?

Ce comportement est attendu pour les groupes d'applications avec beaucoup d'utilisateurs. Nous divisons votre exportation en plusieurs fichiers, en fonction du nombre d'utilisateurs dans votre groupe d'applications. En général, il y a une sortie de fichier par 5000 utilisateurs. Notez que si vous exportez un petit segment dans un grand groupe d'applications, vous pouvez toujours recevoir plusieurs fichiers.

### Pourquoi est-ce que je vois des doublons lorsque j'exporte des utilisateurs par segment via l'API de repos ?

C'est un cas très rare dû à l'architecture sous-jacente du fournisseur de bases de données. Les doublons sont nettoyés chaque semaine; cependant, la plupart des semaines, il n'y a pas de doublons effacés.
