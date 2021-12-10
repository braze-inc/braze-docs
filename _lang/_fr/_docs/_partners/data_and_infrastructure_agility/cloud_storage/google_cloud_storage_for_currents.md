---
nav_title: Stockage Google Cloud
article_title: Stockage Google Cloud
page_order: 2
alias: /fr/partners/google_cloud_storage_for_currents/
description: "Cet article décrit le partenariat entre Braze et Google Cloud Storage, un stockage d'objets massivement évolutif pour des données non structurées."
page_type: partenaire
tool: Courants
search_tag: Partenaire
---

# Stockage Google Cloud

> [Google Cloud Storage](https://cloud.google.com/storage/) est un stockage d'objets massivement évolutif pour les données non structurées offertes par Google dans le cadre de la suite de produits Cloud Computing.

Après le streaming des données dans le stockage Google Cloud Store, vous pouvez utiliser les processus ETL (Extract, Transformer, Charger) pour transférer vos données à d'autres endroits, tels que Google Bigquery.

## Intégration

L'intégration avec Google Cloud Storage nécessite des informations d'identification qui permettent à Braze d'obtenir des informations sur le segment de stockage à écrire (`stockage. uckets.get`) ainsi que la possibilité de créer des objets dans ce bucket (`storage.objects.create`). Pour accorder ces autorisations dans la section IAM & Admin de la plate-forme Google Cloud, vous devez créer un rôle personnalisé, puis créer un compte de service qui utilise ce rôle. Cela générera une clé téléchargeable que vous pouvez ensuite télécharger dans Braze afin que les événements de Devises puissent être écrits dans votre compartiment GCS.

### Étape 1 : Créer un rôle

Créez un nouveau rôle dans la sous-section **Rôles** de la section **IAM & admin** de votre console **Google Cloud Platform**

!\[google_cloud_storage\]\[2\]

### Étape 2 : Accorder les autorisations de rôle

Donnez un nom au rôle, ajoutez les permissions `storage.buckets.get` et `storage.objects.create` au rôle, puis cliquez sur Créer.

!\[google_cloud_storage\]\[3\]

### Étape 3 : Créer un compte de service

Créez un nouveau **compte de service** pour votre projet dans la section **IAM & admin** de votre console **Google Cloud Platform**.

!\[google_cloud_storage\]\[4\]

### Étape 4 : Accorder l'accès

Donnez un nom au compte de service et accordez-lui l'accès à votre nouveau rôle personnalisé.

!\[google_cloud_storage\]\[5\]

### Étape 5 : Créer une clé

Crée une clé au format JSON. Une fois créée, cette clé sera téléchargée sur votre ordinateur.

!\[google_cloud_storage\]\[6\]

### Étape 6 : Télécharger la clé

Sur la page d'intégration **Braze Devises** , téléchargez ce fichier clé JSON en tant que votre **fichier d'identifiants**.

{% alert important %}
Il est important de garder à jour votre fichier d'identifiants; si les identifiants de votre connecteur expient, le connecteur arrêtera d'envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

### Étape 7 : Terminer

Inclure votre nom de segment GCS dans le champ approprié afin que nous sachions où diffuser les données des courants.

## Personnalisations

Vous pouvez également ajouter les personnalisations suivantes, en fonction de vos besoins :

-   Préfixe (par défaut à `courants`)

Ajoutez ces informations à la page Google Cloud Storage Currents de Braze, et appuyez sur **Enregistrer**.

!\[google_cloud_storage\]\[1\]
[1]: {% image_buster /assets/img/google_cloud_storage.png %} [2]: {% image_buster /assets/img/gcs1.png %} [3]: {% image_buster /assets/img/gcs2. ng %} [4]: {% image_buster /assets/img/gc<unk> png %} [5]: {% image_buster /assets/img/gcs4. ng %} [6]: {% image_buster /assets/img/gcs5.png %}
