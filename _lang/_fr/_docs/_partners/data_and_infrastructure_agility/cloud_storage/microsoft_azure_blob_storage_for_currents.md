---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
page_order: 3
alias: /fr/partners/microsoft_azure_blob_storage_for_currents/
description: "Cet article décrit le partenariat entre Braze Currents et Microsoft Azure Blog Storage, un stockage d'objets massivement évolutif pour des données non structurées."
page_type: partenaire
tool: Courants
search_tag: Partenaire
---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) est un stockage d'objets massivement évolutif pour des données non structurées offertes par Microsoft dans le cadre de la suite de produits Azure.

Après avoir transporté des données dans le local Azure Blob, vous pouvez utiliser les processus ETL (Extract, Transformation, Charge) pour transférer vos données vers d'autres emplacements.

## Intégration

L'intégration avec Microsoft Azure Blob Storage nécessite un compte de stockage et une chaîne de connexion pour permettre à Braze de se connecter à des données de flux de courants.

### Étape 1 : Créer un compte de stockage

Naviguez vers "Comptes de stockage" dans la barre latérale et cliquez sur le bouton **Ajouter** dans la colonne centrale pour créer un nouveau compte de stockage. Même si vous avez déjà un compte de stockage, nous vous recommandons d'en créer un nouveau pour vos données Braze.

Tout ce que vous devez faire est de donner un nom au compte de stockage. Vous n'avez pas besoin de modifier les valeurs par défaut.

![Azure Blob]({% image_buster /assets/img/azure-currents-step-1.png %})

### Étape 2 : Récupérer la chaîne de connexion

Une fois le compte de stockage déployé, accédez au menu Clés d'accès à partir de la colonne centrale. Prenez note de la chaîne de connexion. Microsoft fournit deux clés d'accès pour que vous puissiez maintenir les connexions en utilisant une clé tout en régénérant l'autre. Vous n'avez besoin que de la chaîne de connexion de l'un d'entre eux.

{% alert note %}
Les courants de Braze utilisent la chaîne de connexion de ce menu, pas la clé.
{% endalert %}

![Azure Blob]({% image_buster /assets/img/azure-currents-step-2.png %})

### Étape 3 : Créer un conteneur de service blob

Ensuite, accédez au menu "Blobs" dans la section "Blob Service" de la colonne centrale. Créez un conteneur de service Blob dans ce même compte de stockage que vous avez créé précédemment. Tout ce que vous avez à faire est de donner un nom au Blob Service Container. Vous n'avez pas besoin de modifier les valeurs par défaut. Prenez note du nom du conteneur.

![Azure Blob]({% image_buster /assets/img/azure-currents-step-3.png %})

### Étape 4 : Terminer

Ajoutez ces informations à la page des courants de Blob Azure sur le tableau de bord, et appuyez sur "Lancer le courant".

![Azure Blob]({% image_buster /assets/img_archive/currents-azure-blob-edit.png %})

{% alert important %}
Il est important de garder votre chaîne de connexion à jour ; si les informations d'identification de votre connecteur expient, le connecteur arrêtera d'envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

Vous pouvez également ajouter les personnalisations suivantes, en fonction de vos besoins :

-   Préfixe (par défaut à `courants`)

