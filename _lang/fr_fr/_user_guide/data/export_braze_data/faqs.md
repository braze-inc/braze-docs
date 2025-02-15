---
nav_title: FAQ
article_title: FAQ sur les Exportations
page_order: 11
page_type: FAQ
description: "Cet article couvre quelques questions fréquemment posées sur les exportations API et CSV."

---

# Foire aux questions

> Cette page fournit des réponses à certaines questions fréquemment posées sur les exportations API et CSV.

### Est-il possible de faire appartenir certaines exportations dans votre compartiment S3 et pas d’autres ?

Non. Si vous avez fourni des informations d’identification S3, toutes vos exportations apparaîtront dans votre compartiment S3 ; sinon, si aucune information d’identification n’est fournie, toutes les exportations apparaîtront dans un compartiment S3 appartenant à Braze.

### Dois-je ajouter des informations d’identification S3 à Braze pour exporter des données ?

Non. Si vous n'ajoutez pas d'identifiants S3, vos exportations apparaîtront dans un compartiment S3 appartenant à Braze.

### Que se passe-t-il si vous configurez des identifiants S3 dans le tableau de bord mais que vous ne sélectionnez pas "Faire de cette destination la destination d'exportation de données par défaut ?"

La case à cocher **Faire de cette destination la destination par défaut de l'exportation de données** a un impact sur le fait que les exportations vont vers S3 ou Azure, en supposant que vous ayez ajouté des identifiants pour les deux.

### Pourquoi ai-je reçu plusieurs fichiers lors de l’exportation de profils d’utilisateurs vers S3 ?

C'est le comportement attendu pour les espaces de travail avec beaucoup d'utilisateurs. Braze va diviser votre exportation en plusieurs fichiers en fonction du nombre d'utilisateurs dans votre espace de travail. En général, un fichier de sortie est créé tous les 5 000 utilisateurs. Notez que si vous exportez un petit segment dans un grand espace de travail, vous pouvez toujours recevoir plusieurs fichiers.

### Pourquoi y a-t-il des doublons lorsque j'exporte des utilisateurs par segmentation via l'API REST ?

Il s'agit d'un cas très rare causé par l'architecture sous-jacente du fournisseur de base de données. Les doublons sont nettoyés toutes les semaines, mais la plupart des semaines, aucun doublon n’est supprimé.
