---
nav_title: Journaux de synchronisation et observabilité
article_title: Journaux de synchronisation et observabilité
page_order: 10
page_type: reference
description: "Cette page donne un aperçu des fonctionnalités d'observabilité disponibles dans CDI."
---

# Journaux de synchronisation et observabilité

> Le tableau de bord Cloud Data Ingestion (CDI) **Sync Log** vous permet de surveiller toutes les données traitées par CDI, de vérifier si les données ont été synchronisées avec succès et de diagnostiquer tout problème lié à des données "incorrectes" ou manquantes.

Pour accéder aux journaux de synchronisation, accédez à **Paramètres des données** > **Ingestion de données dans le cloud** et sélectionnez l'onglet **Journal de synchronisation**.

## Comprendre le tableau de bord Sync Log

La page principale du **journal de synchronisation** fournit un aperçu de haut niveau de toutes vos synchronisations, y compris un aperçu des synchronisations récentes en fonction de leur état actuel ou final.

* **La course à pied :** Synchroniser les travaux en cours.  
* **Réussite :** Les tâches de synchronisation sont terminées et toutes les lignes ont été traitées avec succès.  
* **Succès partiel :** Tâches de synchronisation qui se sont terminées, mais une ou plusieurs lignes ont rencontré une erreur.  
* **Erreur :** Travaux de synchronisation qui n'ont pas abouti.  
* **Limite dépassée :** Travaux de synchronisation dont le traitement a été interrompu en raison du dépassement d'une limite de données.

![Exemple de journaux de synchronisation avec 6 576 succès au total.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Les journaux de synchronisation fournissent également les détails suivants pour chaque synchronisation :

* **Nom de la synchronisation :** Le nom de la configuration de synchronisation.  
* **Run ID :** Un identifiant unique pour une exécution spécifique de la synchronisation. Sélectionnez cet ID pour obtenir plus de détails. Ceci peut également être utilisé dans les [endpoints de l'API CDI]({{site.baseurl}}/api/endpoints/cdi), ou pour référencer une synchronisation exécutée avec Braze Support.   
* **État :** L'état de l'exécution (succès, succès partiel, erreur, en cours).  
* **Nouvelles lignes lues à partir de la source :** Le nombre de nouvelles lignes extraites de votre entrepôt de données pour cette exécution.  
* **Résultats :** Ventilation du nombre de lignes qui ont réussi ou échoué au cours de l'exécution.  
* **Last "UPDATED_AT":** Horodatage de l'enregistrement le plus récent traité dans ce cycle de synchronisation.  
* **Heure de début de la course :** Date de début du travail de synchronisation.  
* **Durée d'exécution :** Durée totale de la tâche de synchronisation.

![Détails d'un journal de synchronisation.]({% image_buster /assets/img/cloud_ingestion/sync_logs3.png %}){: style="max-width:80%"}

### Conservation des données

Les données du journal de synchronisation, y compris toutes les charges utiles au niveau des lignes et les détails des erreurs, sont conservées pendant **30 jours** maximum. Les journaux datant de plus de 30 jours seront automatiquement purgés.

Les métadonnées d'exécution de la synchronisation, telles que le nombre de lignes traitées, sont conservées pendant au moins 12 mois.

### Filtrer les journaux de synchronisation

Vous pouvez filtrer le tableau des journaux de synchronisation pour trouver des exécutions spécifiques. Les filtres disponibles sont les suivants :

* **Date de début de l'emploi :** Sélectionnez une plage prédéfinie (comme "30 derniers jours") ou une plage de dates personnalisée.  
* **État :** Filtrez sur un ou plusieurs statuts de synchronisation (par exemple en n'affichant que les statuts **Erreur** et **Succès partiel** ).  
* **Nom de la synchronisation :** Recherchez une synchronisation spécifique par son nom.

Pour enquêter sur une synchronisation spécifique, sélectionnez l'**ID d'exécution** correspondant dans le tableau des journaux de synchronisation. Dans la page **Détails de l'exécution**, vous trouverez un journal granulaire, ligne par ligne, de la synchronisation.

### Aperçu de l'exécution

Cette section résume l'exécution sélectionnée, y compris son heure de début, son heure de fin, sa durée et le nombre total de lignes lues à partir de la source. Il indique également le nombre de lignes qui ont abouti et le nombre de lignes qui ont donné lieu à une erreur.

### Lignes traitées dans ce cycle

Ce tableau offre une visibilité au niveau des lignes sur les données traitées pendant la synchronisation, ce qui vous permet de valider des enregistrements individuels.

* **Recherche :** Vous pouvez rechercher un utilisateur spécifique dans les résultats de l'exécution à l'aide de la barre **Recherche par ID utilisateur.**   
* **Détails disponibles :**   
  * **UPDATED_AT:** L'horodatage de la colonne `UPDATED_AT` pour cette ligne spécifique.  
  * **ID :** Les identifiants de l'utilisateur (tels que `external_id`, `email`, ou `alias_name`) utilisés pour faire correspondre l'enregistrement à un profil utilisateur Braze.  
  * **État :** Le statut de traitement individuel pour cette ligne**(succès** ou **erreur)**.  
  * **Source payload :** Un lien permettant de visualiser la charge utile des données.  
  * **Raison de l'erreur :** Si le statut est **Erreur**, cette colonne fournit un message expliquant pourquoi la ligne n'a pas été synchronisée.

#### Visualisation des charges utiles

Pour voir les données exactes envoyées à Braze pour une ligne spécifique, sélectionnez **View payload** dans la colonne **Source** payload. Ceci affiche la charge utile JSON brute qui a été traitée pour cet utilisateur.

![Exemple de charge utile pour une ligne spécifique dans un journal de synchronisation.]({% image_buster /assets/img/cloud_ingestion/sync_logs2.png %}){: style="max-width:80%"}

#### Exportation des journaux de synchronisation

Sélectionnez **Exporter les lignes** pour exporter les journaux au niveau des lignes pour un cycle de synchronisation. Ensuite, choisissez d'exporter par :

* **Lignes comportant des erreurs :** Télécharge un fichier contenant uniquement les lignes ayant un statut d'**erreur.** 
* **Tous les rangs :** Télécharge un fichier contenant toutes les lignes traitées au cours de l'exécution.

{% alert important %}
L'exportation des journaux de synchronisation pour toutes les lignes est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

Les journaux ne peuvent pas être exportés directement à partir du tableau de bord. Une fois l'exportation générée, vous recevrez un e-mail contenant un lien pour télécharger le fichier d'exportation du journal. 

## Notifications

Vous pouvez configurer des notifications par e-mail pour rester informé de l'état de vos synchronisations CDI. Ces paramètres sont configurés lorsque vous créez une synchronisation et peuvent être mis à jour à tout moment.

### Notifications d'erreurs

Au moins une adresse e-mail de contact est requise pour recevoir les notifications d'erreurs au niveau de la synchronisation. Ces alertes sont envoyées lorsqu'une tâche de synchronisation entière ne s'exécute pas ou ne se termine pas, ou si la synchronisation rencontre une erreur nécessitant l'intervention de l'utilisateur, comme des informations d'identification expirées ou une table source manquante.

Les notifications supplémentaires comprennent

- **Erreur de ligne :** Recevez des alertes lorsqu'un certain pourcentage de lignes n'est pas mis à jour au cours d'une synchronisation.
- **Seuil de défaillance (%) :** Indiquez le pourcentage d'échecs de lignes qui doit déclencher une alerte. Par exemple, si cette valeur est fixée à **1**, une notification sera envoyée si 1 % ou plus des lignes d'un cycle de synchronisation donnent lieu à une erreur.
- **Synchronisation réussie :** Recevez une notification lorsque la synchronisation a été effectuée avec succès.
- **Alerte même si aucune ligne n'est modifiée :** Recevez une notification même lorsqu'une synchronisation réussie ne traite aucune ligne nouvelle ou mise à jour.