---
nav_title: Synchronisation des journaux et observabilité
article_title: Synchronisation des journaux et observabilité
page_order: 10
page_type: reference
description: "Cette page fournit un aperçu des fonctionnalités d'observabilité disponibles dans CDI."
---

# Synchronisation des journaux et observabilité

> Le tableau de bord Cloud Data Ingestion (CDI) **Sync Log** vous permet de surveiller toutes les données traitées par CDI, de vérifier si les données ont été synchronisées avec succès et de diagnostiquer tout problème lié à des données « incorrectes » ou manquantes.

Pour accéder aux journaux de synchronisation, veuillez vous rendre dans **Paramètres des données** > **Ingestion de données dans le cloud** et sélectionner l'onglet **Journal de synchronisation**.

## Comprendre le tableau de bord du journal de synchronisation

La page principale **du journal de synchronisation** fournit un aperçu de toutes vos synchronisations, y compris un aperçu des synchronisations récentes par statut actuel ou final.

* **Course à pied :** Veuillez synchroniser les tâches actuellement en cours.  
* **Réussite :** Les tâches de synchronisation ont été achevées et toutes les lignes ont été traitées avec succès.  
* **Succès partiel :** Synchroniser les tâches qui ont été achevées, mais pour lesquelles une ou plusieurs lignes ont rencontré une erreur.  
* **Erreur :** Synchroniser les tâches qui n'ont pas abouti.  
* **Limite dépassée :** Veuillez synchroniser les tâches dont le traitement a été interrompu en raison du dépassement d'une limite de données.

![Exemple de journaux de synchronisation avec un total de 6 576 réussites.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Les journaux de synchronisation fournissent également les détails suivants pour chaque synchronisation :

* **Nom de synchronisation :** Le nom de la configuration de synchronisation.  
* **ID de la course :** Identifiant unique pour une exécution spécifique de la synchronisation. Veuillez sélectionner cet ID pour obtenir plus de détails. Cela peut également être utilisé dans les [endpoints de l'API CDI]({{site.baseurl}}/api/endpoints/cdi) ou pour faire référence à une synchronisation effectuée avec l'assistance Braze.   
* **État :** Le statut de l'exécution (réussite, réussite partielle, erreur, en cours d'exécution).  
* **Nouvelles lignes lues à partir de la source :** Le nombre de nouvelles lignes extraites de votre entrepôt de données pour cette exécution.  
* **Résultats :** Une ventilation du nombre de lignes qui ont réussi ou échoué au cours de l'exécution.  
* **Dernier"UPDATED_AT": ** Horodatage de l'enregistrement le plus récent traité lors de cette synchronisation.  
* **Heure de début de la course :** Quand la tâche de synchronisation a-t-elle commencé ?  
* **Durée de l'exécution :** Durée totale nécessaire à la synchronisation.

![Détails relatifs au journal de synchronisation.]({% image_buster /assets/img/cloud_ingestion/sync_logs3.png %}){: style="max-width:80%"}

### Conservation des données

Les données du journal de synchronisation, y compris toutes les charges utiles au niveau des lignes et les détails des erreurs, sont conservées pendant une période maximale de **30 jours**. Les journaux datant de plus de 30 jours seront automatiquement supprimés.

Les métadonnées de synchronisation, telles que le nombre de lignes traitées, sont conservées pendant au moins 12 mois.

### Filtrage des journaux de synchronisation

Vous pouvez filtrer le tableau des journaux de synchronisation afin de trouver des exécutions spécifiques. Les filtres disponibles sont les suivants :

* **Date de début de l'emploi :** Veuillez sélectionner une plage prédéfinie (telle que « 30 derniers jours ») ou une plage de dates personnalisée.  
* **État :** Filtrez selon un ou plusieurs statuts de synchronisation (par exemple, affichez uniquement les statuts **« Erreur** » et **« Succès partiel** »).  
* **Nom de synchronisation :** Recherchez une synchronisation spécifique par son nom.

Pour examiner une synchronisation spécifique, veuillez sélectionner l'**ID d'exécution** pertinent dans le tableau des journaux de synchronisation. Dans la page **Détails de l'exécution**, vous trouverez un journal détaillé, ligne par ligne, de la synchronisation.

### Aperçu de la course

Cette section résume l'exécution sélectionnée, y compris son heure de début, son heure de fin, sa durée et le nombre total de lignes lues à partir de la source. Il fournit également un décompte du nombre de lignes traitées avec succès et du nombre de lignes ayant généré une erreur.

### Lignes traitées dans ce cycle

Ce tableau offre une visibilité au niveau des lignes sur les données traitées pendant la synchronisation, vous permettant ainsi de valider chaque enregistrement individuellement.

* **Recherche :** Vous pouvez rechercher un utilisateur spécifique dans les résultats de l'exécution à l'aide de la barre **Rechercher par ID utilisateur**.  
* **Informations disponibles :**   
  * **UPDATED_AT:** L'horodatage de la`UPDATED_AT`colonne pour cette ligne spécifique.  
  * **ID :** Les identifiants utilisateur (tels que `external_id`, `email`, ou `alias_name`) utilisés pour associer l'enregistrement à un profil utilisateur Braze.  
  * **État :** Le statut de traitement individuel pour cette ligne (**Succès** ou **Erreur**).  
  * **Charge utile source :** Un lien pour consulter les données transmises.  
  * **Motif de l'erreur :** Si le statut est **Erreur**, cette colonne affiche un message expliquant pourquoi la ligne n'a pas pu être synchronisée.

#### Affichage des charges utiles

Pour afficher les données exactes envoyées à Braze pour une ligne spécifique, veuillez sélectionner **Afficher la charge utile** dans la colonne Charge utile **source**. Cela affiche la charge utile JSON brute qui a été traitée pour cet utilisateur.

![Exemple de charge utile pour une ligne spécifique dans un journal de synchronisation.]({% image_buster /assets/img/cloud_ingestion/sync_logs2.png %}){: style="max-width:80%"}

#### Exportation des journaux de synchronisation

Veuillez sélectionner **Exporter les lignes** pour exporter les journaux au niveau des lignes pour une exécution de synchronisation. Ensuite, veuillez sélectionner l'option d'exportation suivante :

* **Lignes contenant des erreurs :** Télécharge un fichier contenant uniquement les lignes qui présentaient un statut **d'erreur**.
* **Toutes les lignes :** Télécharge un fichier contenant toutes les lignes traitées lors de l'exécution.

{% multi_lang_include early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Les journaux ne peuvent pas être exportés directement depuis le tableau de bord. Une fois l'exportation générée, vous recevrez un e-mail contenant un lien pour télécharger le fichier d'exportation du journal. 

## Notifications

Vous pouvez configurer des notifications par e-mail pour rester informé de l'état de vos synchronisations CDI. Ces paramètres sont configurés lors de la création d'une synchronisation et peuvent être mis à jour à tout moment.

### Notifications d'erreur

Au moins une adresse e-mail est requise pour recevoir les notifications relatives aux erreurs de synchronisation. Ces alertes sont envoyées lorsqu'une tâche de synchronisation échoue ou ne parvient pas à se terminer, ou si la synchronisation rencontre une erreur nécessitant l'intervention de l'utilisateur pour être corrigée, telle que des informations d'identification expirées ou une table source manquante.

Les notifications supplémentaires comprennent :

- **Erreur de ligne :** Recevez des alertes lorsqu'un certain pourcentage de lignes ne parvient pas à se mettre à jour lors d'une synchronisation.
- **Seuil de défaillance (%) :** Veuillez indiquer le pourcentage d'échecs de lignes qui devrait être le déclencheur d'une alerte. Par exemple, en définissant cette valeur sur **1,** une notification sera envoyée si 1 % ou plus des lignes d'une synchronisation génèrent une erreur.
- **Synchronisation réussie :** Recevez une notification lorsque la synchronisation est terminée.
- **Alerte même si aucune ligne n'a été modifiée :** Recevez une notification même lorsqu'une synchronisation réussie ne traite aucune ligne nouvelle ou mise à jour.