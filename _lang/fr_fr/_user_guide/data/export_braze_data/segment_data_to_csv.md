---
nav_title: Exporter les données du segment dans un CSV
article_title: Exporter les données du segment dans un CSV
page_order: 2
page_type: reference
description: "Cet article de référence explique comment exporter les données d’un segment dans un fichier CSV."

---

# Exporter les données du segment dans un CSV

> Cette page explique comment demander une exportation CSV des données utilisateur d'une segmentation, ainsi que les données incluses dans l'exportation.

Pour exporter les données d'un segment vers un fichier CSV, sélectionnez le menu déroulant **Données utilisateur** lorsque vous modifiez un segment et choisissez d'exporter soit les données utilisateur, soit les adresses e-mail pour le segment.

![La section Détails du segment avec la liste déroulante Données de l'utilisateur affichant les options d'exportation.]({% image_buster /assets/img_archive/csvexport.png %})

Vous pouvez également demander une exportation CSV à partir de la page principale **Segments** en sélectionnant le menu déroulant <i class="fas fa-gear"></i> **Settings** pour un segment :

![Liste déroulante des paramètres sur la page principale des segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Pour exporter les données de tous vos profils utilisateurs, créez une segmentation sans filtre, puis demandez une exportation CSV.
{% endalert %}

Le fichier CSV contient les données de chaque profil utilisateur capturé dans le segment au moment de l’exportation. Vous pouvez exporter n'importe quel segment en sélectionnant l'icône d'engrenage, puis Exportation CSV. Braze génère le rapport en arrière-plan et l’envoie par e-mail à l’utilisateur actuellement connecté.

{% alert important %}
En raison des limites de taille de fichier, votre exportation peut échouer si la taille estimée de votre segment fait plus de 500 000 utilisateurs. Notez que cette restriction est basée sur la taille estimée de votre segment, et non sur la taille exacte. Pour plus de détails, voir [Exporter des segments volumineux]({{site.baseurl}}/help/help_articles/segments/exporting_large_segments/).
{% endalert %}

Si vous avez lié vos [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) à Braze, le fichier CSV sera téléchargé dans votre compartiment S3 sous la clé `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Le lien qui vous est envoyé par e-mail expirera après un jour d'exportation et vous devrez être connecté au tableau de bord pour y accéder.

## Données incluses dans l'exportation

Les éléments suivants sont inclus dans votre exportation en fonction de votre sélection.

### Exporter les données utilisateur en CSV

| Nom du champ                  | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interne (non modifiable)                           |
| pays                     | Pays                                    |
| created_at                  | Date et heure de création du profil utilisateur                   |
| appareils                     | Informations sur l’appareil                           |
| date_de_naissance               | Date de naissance                                            |
| e-mail                       | Adresse e-mail                                            |
| unsubscribed_from_emails_at | Date de désabonnement aux e-mails                            |
| user_id                     | ID externe                                              |
| Prénom                  | Prénom                                               |
| first_session               | Date et heure de la première session                           |
| genre                      | Genre                                                   |
| google_ad_ids               | les ID publicitaires de Google associés à l'utilisateur                      |
| ville                        | Ville                                     |
| IDFA                       | Valeurs de l'identifiant pour la publicité (IDFA)                 |
| IDFV                       | Valeurs de l'identificateur du fournisseur (IDFV)                      |
| langue                    | Langue dans la norme ISO-639-1                                        |
| dernière_app_version_utilisée       | Dernière version de l'application utilisée                             |
| Nom                   | Nom                                                |
| last_session                | Date et heure de la dernière session                            |
| number_of_google_ad_ids     | Nombre d'ID de publicité Google associés               |
| number_of_IDFAs             | Nombre d'IDFA associés                                |
| number_of_IDFVs             | Nombre d'IDFV associées                                |
| number_of_push_tokens       | Nombre de jetons de notification push associés.             |
| nombre_de_roku_ad_ids       | Nombre d'ID publicitaires Roku associés                 |
| number_of_windows_ad_ids    | Nombre d'ID de publicité Windows associés              |
| phone_number                | Numéro de téléphone                                             |
| opted_into_push_at          | Date d'abonnement aux notifications push                       |
| désabonné_de_push_at   | Date de désabonnement aux notifications push                |
| random_bucket               | Numéro de compartiment aléatoire                                 |
| roku_ad_ids                 | ID publicitaires Roku                          |
| session_count               | Nombre total de sessions                                 |
| fuseau horaire                    | Fuseau horaire de l'utilisateur dans le même format que la base de données des fuseaux horaires de l'IANA                                         |
| in_app_purchase_total       | Montant total dépensé en achats in-app                   |
| user_aliases                | Alias de l'utilisateur, le cas échéant                                          |
| windows_ad_ids              | ID de publicité Windows                       |
| Événements personnalisés               | Sur la base de la sélection à l'exportation                             |
| Attributs personnalisés           | Sur la base de la sélection à l'exportation                             |
{: .reset-td-br-1 .reset-td-br-2 }

### Exporter les adresses e-mail en CSV

| Nom du champ                  | Description            |
| --------------------------- | ---------------------- |
| user_id                     | ID externe de l'utilisateur     |
| Prénom                  | Prénom             |
| Nom                   | Nom              |
| e-mail                       | E-mail                  |
| unsubscribed_from_emails_at | Date de désabonnement aux e-mails |
| opted_in_to_emails_at       | Date d'abonnement à l'e-mail      |
| user_aliases                | Alias de l'utilisateur, le cas échéant   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez notre article de [résolution des problèmes]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %} 

