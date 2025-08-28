---
page_order: 0
nav_title: Accueil
article_title: Guide de l’API Braze
layout: api_glossary
glossary_top_header: "Braze API Guide"
glossary_top_text: "Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This page lists available Braze API endpoints and their uses."
page_type: glossary
description: "Cette page d’accueil répertorie les endpoints disponibles dans l’API Braze ainsi que leurs utilisations."
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: Overview API
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics/
  - name: Types d’identifiant API
    link: /docs/api/identifier_types/
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objets et filtres
    link: /docs/api/objects_filters/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Erreurs et réponses
    link: /docs/api/errors/
    image: /assets/img/braze_icons/list.svg
  - name: Conservation des données
    link: /docs/api/data_retention/
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Limites de débit
    link: /docs/api/api_limits/
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Campagnes
  - name: Canvas
  - name: Catalogues
  - name: Blocs de contenu
  - name: Événements personnalisés
  - name: Liste d’e-mails
  - name: Modèles d’e-mail
  - name: Indicateur clé de performance
  - name: Achats
  - name: Centre de préférences
  - name: Planifier les messages
  - name: SCIM
  - name: Authentification SDK
  - name: Segments
  - name: Envoyer les messages
  - name: SMS
  - name: Groupes d’abonnement
  - name: Données utilisateur
  - name: Activité en direct
  - name: Ingestion de données cloud

glossaries:
  - name: "<a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>"
    description: "Ajouter de nouveaux alias utilisateur pour les utilisateurs identifiés existants, ou pour créer de nouveaux utilisateurs non identifiés."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/users/alias/update</a>"
    description: Mettre à jour les noms d’alias d’utilisateur existants avec les nouveaux noms d’alias d’utilisateur.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>"
    description: Supprimer un profil utilisateur en spécifiant un identifiant utilisateur connu.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>"
    description: Exporter tous les utilisateurs d’un Groupe de contrôle global.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/users/export/ids</a>"
    description: Exporter des données à partir de n’importe quel profil utilisateur en spécifiant un identifiant utilisateur.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/users/export/segment</a>"
    description: Exporter tous les utilisateurs d’un segment.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>"
    description: Renommer les ID externes de vos utilisateurs.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>"
    description: Supprimer les anciens ID externes obsolètes de vos utilisateurs.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>"
    description: Identifier un utilisateur non identifié (alias uniquement).
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>"
    description: "Enregistrer des événements personnalisés, des achats et mettre à jour les attributs de profil utilisateur."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_merge/'>/users/merge</a>"
    description: Fusionner un profil utilisateur avec un autre.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>"
    description: "Envoyez des messages immédiats et ponctuels à des utilisateurs désignés grâce à la réception/distribution déclenchée par l'API. - Envoyer des messages"
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>"
    description: "Envoyez des messages canvas par le biais d'une réception/distribution déclenchée par l'API. - Envoyer des messages"
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/messages/send</a>"
    description: "Envoyez des messages immédiats et ponctuels à des utilisateurs désignés via l'API de Braze."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>"
    description: Pour créer des ID d’envoi pouvant être utilisés pour envoyer des messages et suivre leur performance de manière programmatique sans créer une campagne pour chaque envoi.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>"
    description: Envoyez des messages transactionnels immédiats et ponctuels à un utilisateur désigné.
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>"
    description: "Envoyez des messages de campagne créés dans le tableau de bord par le biais d'une réception/distribution déclenchée par l'API."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>"
    description: Annuler des messages de campagne déclenchés par API que vous avez déjà planifiés avant qu’ils ne soient envoyés.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>"
    description: Mettre à jour des campagnes déclenchées par API planifiées créées dans le tableau de bord.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>"
    description: Annuler un message Canvas que vous avez déjà planifié dans des campagnes déclenchées par API avant qu’il ne soit envoyé.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>"
    description: "Planifiez les messages Canvas par le biais d'une réception/distribution déclenchée par l'API."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>"
    description: Mettre à jour les messages planifiés. Cet endpoint accepte les mises à jour vers le <code>schedule</code> ou <code>messages</code> paramètre ou les deux.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>"
    description: Annuler un message que vous avez déjà planifié avant qu’il ne soit envoyé.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>"
    description: "Planifiez l'envoi d'une campagne, d'un canvas ou d'un autre message à un moment donné."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/trigger/schedule/update</a>"
    description: Mettre à jour des Canvas déclenchés par API planifiés qui ont été créés dans le tableau de bord.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>"
    description: Renvoyer une liste JSON d’informations sur les campagnes planifiées et les entrées Canvas entre maintenant et une date désignée <code>end_time</code> spécifié dans la demande.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>"
    description: Mettre à jour une activité iOS Live.
    tags:
      - Live Activity
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>"
    description: Mettre à jour des statuts d’abonnement par lots de 50 utilisateurs maximum sur le tableau de bord de Braze.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>"
    description: Mettre à jour des statuts d’abonnement par lots de 50 utilisateurs maximum sur le tableau de bord de Braze.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>"
    description: Obtenir le statut d’abonnement d’un utilisateur dans un groupe d’abonnement.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>"
    description: Répertorier et obtenir les groupes d’abonnement d’un certain utilisateur.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>"
    description: Désinscrire un utilisateur des e-mails et le marquer comme rejeté définitivement.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>"
    description: Supprimer les adresses e-mail de votre liste de rejets Braze.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>"
    description: Supprimer les adresses e-mail de votre liste de courriers indésirables de Braze.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>"
    description: Définir l’état de l’abonnement aux e-mails de vos utilisateurs.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>"
    description: Créer des modèles d’e-mail sur le tableau de bord de Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>"
    description: Mettre à jour des modèles d’e-mail sur le tableau de bord de Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>"
    description: "Extraire une liste d’adresses e-mail qui ont rejeté définitivement vos e-mails au cours d'une certaine période."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>"
    description: Renvoie les adresses mail qui se sont désabonnées entre  <code>start_date</code> to <code>end_date</code>.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>"
    description: Obtenir des informations sur vos modèles d’e-mail.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>"
    description: Obtenir une liste des e-mails disponibles sur votre compte Braze.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>"
    description: Récupérer une série quotidienne de diverses statistiques pour une campagne au fil du temps.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/campaigns/details</a>"
    description: Récupérer des informations pertinentes d’une campagne donnée.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>"
    description: "Exporter une liste de campagnes, comportant pour chacune son nom, s’il s’agit d’une campagne par API, son identifiant API éventuel et les balises qui lui sont associées."
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>"
    description: Récupérer une série quotidienne de diverses statistiques pour un suivi. <code>send_id</code>.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>"
    description: Exporter les données d’une série de dates pour un Canvas.
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/data_summary</a>"
    description: "Exporter des cumuls de données de série temporelles pour un Canvas, fournissant ainsi un résumé concis des résultats du Canvas."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>"
    description: "Exporter des métadonnées sur un Canvas, telles que le nom, l’heure de création, l’état actuel, etc."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>"
    description: "Exporter une liste de Canvas, y compris le nom, l’identifiant de l’API Canvas et les balises associées."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>"
    description: Récupérer une série quotidienne de la taille estimée d’un segment au fil du temps.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>"
    description: Récupérer les informations pertinentes sur un segment.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>"
    description: "Exporter une liste de segments, chacun incluant son nom, l’identifiant API du segment et s’il a un suivi des analyses activé."
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>"
    description: Récupérer une série du nombre de sessions de votre application sur une période donnée.
    tags:
      - Sessions
  - name: "<a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes/'>/custom_attributes</a>"
    description: "Exportez une liste d'attributs personnalisés comprenant le nom, la description, le type de données, la longueur du tableau (le cas échéant), l'état et les tags associés."
    tags:
      - Custom Attributes
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>"
    description: Récupérer une série du nombre d’occurrences d’un événement personnalisé dans votre application sur une période donnée.
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_data/'>/événements</a>"
    description: "Exportez une liste d'événements personnalisés comprenant le nom, la description, l'état, les tags associés et l'inclusion dans le rapport d'analyse."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>"
    description: "Exportez une liste de noms d'événements personnalisés qui ont été enregistrés pour votre appli."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>"
    description: Créer un bloc de contenu d’e-mail.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>"
    description: Mettre à jour un bloc de contenu d’e-mail.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>"
    description: Appeler les informations de vos blocs de contenu d’e-mail existants.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>"
    description: Répertorier les informations existantes de vos blocs de contenu.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>"
    description: Récupérer une série quotidienne du nombre total d’utilisateurs actifs uniques à chaque date.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>"
    description: Récupérer une série quotidienne du nombre total d’utilisateurs actifs uniques sur une période de 30 jours glissants.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>"
    description: Récupérer une série quotidienne du nombre total de nouveaux utilisateurs à chaque date.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>"
    description: Récupérer une série quotidienne du nombre total de désinstallations à chaque date.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>"
    description: "Supprimez les numéros de téléphone \"non valides\" de la liste des numéros non valides dans Braze. Cela peut être utilisé pour revalider les numéros de téléphone après avoir été marqués comme non valides."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>"
    description: Extraire une liste des numéros de téléphone considérés comme « non valides » dans un certain délai.
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>"
    description: Retourner des listes paginées des ID de produits.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/purchases/quantity_series</a>"
    description: "Renvoyez le nombre total d'achats effectués dans votre application sur une période donnée."
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/purchases/revenue_series</a>"
    description: Renvoyez le montant total dépensé dans votre application sur une période donnée.
    tags:
      - Purchases    
  - name: "<a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>"
    description: Créer une URL pour un centre de préférences.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/preference_center/v1/list</a>"
    description: Répertorie les centres de préférences disponibles.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: "Afficher les détails de vos centres de préférences, y compris la date de leur création et de leurs mises à jour."
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>"
    description: Créer un centre de préférences pour permettre aux utilisateurs de gérer leurs préférences de notification pour les campagnes par e-mail.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: Mettre à jour un centre de préférences.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>"
    description: Supprimer plusieurs objets dans votre catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Lister un produit du catalogue et ses détails.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Éditer plusieurs objets dans votre catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Créer plusieurs objets dans votre catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/catalogs/{catalog_name}</a>"
    description: Supprimer un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/catalogs</a>"
    description: Créer un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/catalogs</a>"
    description: "Lister les catalogues d'un espace de travail."
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Créer un produit dans un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Éditer un produit dans un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Retourner plusieurs produits du catalogue et leur contenu.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Supprimer un produit dans un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Remplacer un article dans un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/items/</a>"
    description: Remplacer plusieurs articles dans un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/'>/catalogs/{catalog_name}/fields/</a>"
    description: Créez plusieurs champs dans un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/'>/catalogs/{catalog_name}/fields/{field_name}</a>"
    description: "Supprimer un champ d'un catalogue."
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/'>/catalogs/{catalog_name}/selections</a>"
    description: Créer une sélection dans un catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/'>/catalogs/{catalog_name}/selections/{selection_name}</a>"
    description: Supprimer une sélection de catalogue.
    tags:
      - Catalogs
  - name: "<a href='/docs/post_create_user_account/'>/scim/v2/Users</a>"
    description: "Créez un nouveau compte utilisateur pour le tableau de bord en indiquant l'e-mail, les noms et prénoms, les autorisations (pour définir les autorisations au niveau de l'entreprise, de l'espace de travail et de l'équipe)."
    tags:
      - SCIM
  - name: "<a href='/docs/get_see_user_account_information/'>/scim/v2/Users/{id}</a>"
    description: Recherchez un compte utilisateur de tableau de bord existant en spécifiant son ID de ressource.
    tags:
      - SCIM
  - name: "<a href='/docs/post_update_existing_user_account/'>/scim/v2/Users/{id}</a>"
    description: "Mettez à jour un compte utilisateur de tableau de bord existant en spécifiant l'e-mail, les noms et prénoms, les autorisations (pour définir les autorisations au niveau de l'entreprise, de l'espace de travail et de l'équipe)."
    tags:
      - SCIM
  - name: "<a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Users/{id}</a>"
    description: Supprimer définitivement un utilisateur du tableau de bord existant.
    tags:
      - SCIM
  - name: "<a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Users?filter={userName@example.com}</a>"
    description: Rechercher un compte utilisateur du tableau de bord existant en spécifiant leur e-mail.
    tags:
      - SCIM
  - name: "<a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrations</a>"
    description: Renvoyez une liste des intégrations existantes.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrations/{integration_id}/sync</a>"
    description: Déclencher une synchronisation pour une intégration donnée.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrations/{integration_id}/job_sync_status</a>"
    description: Retourne une liste des états de synchronisation.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/'>/app_group/sdk_authentication/create</a>"
    description: "Créez une nouvelle clé d'authentification SDK pour votre application."
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys/'>/app_group/sdk_authentication/keys</a>"
    description: "Liste des clés d'authentification du SDK pour votre application."
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/'>/app_group/sdk_authentication/primary</a>"
    description: "Définissez une clé d'authentification SDK comme clé principale pour votre application."
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key/'>/app_group/sdk_authentication/delete</a>"
    description: "Supprimez une clé d'authentification SDK pour votre application."
    tags:
      - SDK Authentication  
---