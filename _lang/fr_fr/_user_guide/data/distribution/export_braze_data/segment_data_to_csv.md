---
nav_title: Exporter les données de segmentation au format CSV
article_title: Exporter les données de segmentation au format CSV
page_order: 2
page_type: reference
description: "Cet article de référence explique comment exporter des données de segmentation au format CSV."

---

# Exportation des données de segmentation au format CSV

> Cette page explique comment demander une exportation CSV des données utilisateur d'une segmentation, ainsi que les données incluses dans l'exportation.

Pour exporter les données d'un segment vers un fichier CSV, sélectionnez le menu déroulant **Données utilisateur** lorsque vous modifiez un segment et choisissez d'exporter soit les données utilisateur, soit les adresses e-mail pour le segment.

Section Détails du segment avec le menu déroulant Données de l'utilisateur affichant les options d'exportation.]({% image_buster /assets/img_archive/csvexport.png %})

Vous pouvez également demander une exportation CSV à partir de la page principale **Segments** en sélectionnant le menu déroulant <i class="fas fa-gear"></i> **Settings** pour un segment :

!déroulant Paramètres sur la page principale des segments.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Pour exporter les données de tous vos profils utilisateurs, créez une segmentation sans filtre, puis demandez une exportation CSV.
{% endalert %}

Le fichier CSV contient les données de chaque profil utilisateur capturé dans le segment au moment de l'exportation. Vous pouvez exporter n'importe quel segment en sélectionnant l'icône d'engrenage et l'exportation CSV. Braze génère le rapport en arrière-plan et l'envoie par e-mail à l'utilisateur actuellement connecté.

{% alert important %}
En raison de restrictions sur la taille des fichiers, votre exportation risque d'échouer si la taille estimée de votre segmentation est supérieure à 500 000 utilisateurs. Notez que cette restriction utilise la taille estimée de votre segmentation, et non le calcul exact. Pour plus de détails, reportez-vous à la section [Exportation de segments de grande taille](#exporting-large-segments).
{% endalert %}

Si vous avez lié vos [identifiants Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) à Braze, le fichier CSV sera téléchargé dans votre compartiment S3 sous la clé `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. Vous devez être connecté au tableau de bord pour accéder au lien de téléchargement qui vous a été envoyé par e-mail.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Données incluses dans l'exportation

Les éléments suivants sont inclus dans votre exportation en fonction de votre sélection.

### Exportation des données de l'utilisateur au format CSV

| Nom du champ                  | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interne (non modifiable)                           |
| pays                     | Pays                                    |
| created_at                  | Date et heure de création du profil utilisateur                   |
| appareils                     | Informations sur l'appareil                           |
| date_of_birth               | Date de naissance                                            |
| e-mail                       | Adresse e-mail                                            |
| unsubscribed_from_emails_at | Date de désabonnement aux e-mails                            |
| user_id                     | ID externe                                              |
| first_name                  | Prénom                                               |
| first_session               | Date et heure de la première session                           |
| sexe                      | Genre                                                   |
| google_ad_ids               | les ID publicitaires de Google associés à l'utilisateur                      |
| ville                        | Ville                                     |
| IDFA                       | Valeurs de l'identifiant pour la publicité (IDFA)                 |
| IDFVs                       | Valeurs de l'identificateur du fournisseur (IDFV)                      |
| langue                    | Langue dans la norme ISO-639-1                                        |
| last_app_version_used       | Dernière version de l'application utilisée                             |
| last_name                   | Nom de famille                                                |
| last_session                | Date et heure de la dernière session                            |
| number_of_google_ad_ids     | Nombre d'ID de publicité Google associés               |
| number_of_IDFAs             | Nombre d'IDFA associés                                |
| number_of_IDFVs             | Nombre d'IDFV associées                                |
| number_of_push_tokens       | Nombre de jetons de notification push associés.             |
| number_of_roku_ad_ids       | Nombre d'ID publicitaires Roku associés                 |
| number_of_windows_ad_ids    | Nombre d'ID de publicité Windows associés              |
| phone_number                | Numéro de téléphone                                             |
| opted_into_push_at          | Date d'abonnement aux notifications push                       |
| unsubscribed_from_push_at   | Date de désabonnement aux notifications push                |
| random_bucket               | Numéro de compartiment aléatoire                                 |
| roku_ad_ids                 | ID publicitaires Roku                          |
| session_count               | Nombre total de sessions                                 |
| fuseau horaire                    | Fuseau horaire de l'utilisateur dans le même format que la base de données des fuseaux horaires de l'IANA                                         |
| in_app_purchase_total       | Montant total dépensé en achats in-app                   |
| user_aliases                | Aliasing de l'utilisateur, le cas échéant                                          |
| windows_ad_ids              | ID de publicité Windows                       |
| Événements personnalisés               | Sur la base de la sélection à l'exportation                             |
| Attributs personnalisés           | Sur la base de la sélection à l'exportation                             |
{: .reset-td-br-1 .reset-td-br-2 }

### Exportation des adresses e-mail au format CSV

| Nom du champ                  | Description            |
| --------------------------- | ---------------------- |
| user_id                     | ID externe de l'utilisateur     |
| first_name                  | Prénom             |
| last_name                   | Nom de famille              |
| e-mail                       | e-mail                  |
| unsubscribed_from_emails_at | Date de désinscription de l'e-mail |
| opted_in_to_emails_at       | Date d'abonnement à l'e-mail      |
| user_aliases                | Aliasing de l'utilisateur, le cas échéant   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez notre article de [résolution des problèmes.]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/) 
{% endalert %} 

## Exportation de segments importants

Il existe plusieurs méthodes pour exporter un segment d'utilisateurs important qui contient plus de 500 000 utilisateurs.

{% tabs %}
{% tab Multiple segments %}

Vous pouvez diviser un grand segment en segments plus petits, puis exporter chacun des segments plus petits à partir de Braze. 

{% endtab %}
{% tab Random bucket numbers %}

Vous pouvez également utiliser des [numéros de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) pour diviser votre base d'utilisateurs en plusieurs segments, puis les combiner après l'exportation. Par exemple, si vous devez diviser votre segment en deux segments différents, vous pouvez le faire avec les filtres suivants :
- Segmentation 1 : Le numéro de compartiment aléatoire est inférieur à 5000 (y compris 0-4999).
- Segmentation 2 : Le numéro de compartiment aléatoire est supérieur à 4999 (y compris 5000-9999).

{% endtab %}
{% tab Endpoints %}

Vous pouvez également utiliser les endpoints suivants pour exporter les données des utilisateurs pour une segmentation spécifique. Notez que ces endpoints sont soumis à des limites de données.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

{% endtab %}
{% endtabs %}
