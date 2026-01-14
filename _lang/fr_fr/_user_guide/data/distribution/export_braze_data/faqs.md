---
nav_title: FAQ
article_title: "FAQ sur l'exportation"
page_order: 11
page_type: FAQ
description: "Cet article aborde certaines questions fréquemment posées concernant les exportations API et CSV."

---

# Questions fréquemment posées

> Cette page répond aux questions les plus fréquemment posées sur l'API et les exportations CSV.

### Pouvez-vous faire en sorte que certaines exportations apparaissent dans votre compartiment S3 et d'autres non ?

Non. Si vous avez fourni des identifiants S3, toutes vos exportations apparaîtront dans votre compartiment S3 ; sinon, si aucun identifiant n'est fourni, toutes les exportations apparaîtront dans un compartiment S3 appartenant à Braze.

### Dois-je ajouter des identifiants S3 à Braze pour exporter des données ?

Non. Si vous n'ajoutez pas d'identifiants S3, vos exportations apparaîtront dans un compartiment S3 appartenant à Braze.

### Que se passe-t-il si vous configurez des identifiants S3 dans le tableau de bord mais que vous ne sélectionnez pas "Faire de cette destination la destination d'exportation de données par défaut ?"

La case à cocher **Faire de cette destination la destination par défaut de l'exportation de données** a un impact sur le fait que les exportations vont vers S3 ou Azure, en supposant que vous ayez ajouté des identifiants pour les deux.

### Pourquoi ai-je reçu plusieurs fichiers lors de l'exportation de profils utilisateurs vers S3 ?

Il s'agit d'un comportement attendu pour les espaces de travail comptant un grand nombre d'utilisateurs. Braze divisera votre exportation en plusieurs fichiers en fonction du nombre d'utilisateurs dans votre espace de travail. En général, il y a une sortie de fichier pour 5 000 utilisateurs. Notez que si vous exportez un petit segment au sein d'un grand espace de travail, il se peut que vous receviez plusieurs fichiers.

### Pourquoi y a-t-il des doublons lorsque j'exporte des utilisateurs par segmentation via l'API REST ?

Il s'agit d'un cas très rare, dû à l'architecture sous-jacente du fournisseur de base de données. Les doublons sont éliminés chaque semaine ; cependant, la plupart des semaines, aucun doublon n'est éliminé.
