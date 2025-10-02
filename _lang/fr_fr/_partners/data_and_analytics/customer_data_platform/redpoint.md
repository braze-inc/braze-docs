---
nav_title: Redpoint
article_title: Redpoint 
description: "L'intégration de Redpoint à Braze vous permet d'intégrer et d'enrichir les profils utilisateurs de Braze avec vos données first-party."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com) est une plateforme technologique qui offre aux marketeurs une plateforme d'orchestration de campagne entièrement intégrée. Tirez parti des capacités de segmentation, de planification et d'automatisation de Redpoint pour contrôler comment et quand les données CDP sont importées dans Braze.

_Cette intégration est maintenue par Redpoint._

## À propos de l'intégration

L'intégration de Braze et Redpoint vous permet de créer des segments Braze basés sur vos données CDP Redpoint. Redpoint permet de transmettre des données à Braze de deux manières : 

1. Mode d’**onboarding et de mise à jour** de Braze : « Mettre à jour/Insérer » un profil utilisateur de Redpoint dans Braze. Ce processus est destiné à être utilisé pour l'onboarding ou la mise à jour des enregistrements des utilisateurs lorsque les données ont changé. 
2. mode **Braze Append** : Met à jour un profil utilisateur si cet utilisateur existe déjà dans Braze. 

Vous configurerez un modèle d'exportation et un canal sortant pour chaque mode.

{% alert note %}
Dans ce cas, la mise à jour permet d’actualiser les données, mais aussi d’insérer des enregistrements. Il est utilisé lorsque vous souhaitez insérer un nouvel enregistrement dans une table de base de données s'il n'existe pas déjà ou mettre à jour l'enregistrement s'il existe. Essentiellement, cette opération de mise à jour/insertion vérifie si un enregistrement particulier est présent dans la base de données. Si l'enregistrement existe, il est mis à jour, et dans le cas contraire, un nouvel enregistrement est inséré.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br>Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Composants de gestion de données Redpoint | L'intégration Braze est prise en charge par un ensemble de composants de gestion de données Redpoint. Contactez le [service d’assistance de Redpoint](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us) pour demander les composants pour votre version de la fonction de gestion des données de Redpoint. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Attributs personnalisés de CDP Redpoint

Les attributs personnalisés Redpoint suivants peuvent être ajoutés à un profil utilisateur Braze.

| Champ               | Description                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | L'objet d'attribut de profil CDP Redpoint                                                                                  |
| `rpi_audience_outputs`| Tableau de balises de sortie d'audience où l'utilisateur est ciblé dans une exécution de canal de livraison sortante Redpoint vers Braze         |
| `rpi_offers`         | Tableau de balises d'offre où l'utilisateur est ciblé dans une exécution de canal Braze de distribution Redpoint Outbound                   |
| `rpi_contact_ids`    | Tableau des identifiants de contact de l'historique des offres où l'utilisateur est ciblé dans une exécution de canal Braze de distribution Redpoint Outbound     |
| `rpi_channel_exec_ids`| Tableau d'ID d'exécution de canal où l'utilisateur est ciblé dans une exécution de canal Braze de distribution Redpoint Outbound       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## Intégration

### Étape 1 : Configurer les modèles

#### Étape 1a: Créer le modèle d’onboarding et de mise à jour/insertion Braze

Dans Redpoint Interaction (RPI), créez un nouveau modèle d'exportation et nommez-le **Onboarding et mise à jour Braze**. Ce modèle définit les correspondances principales entre le CDP Redpoint et le profil utilisateur Braze, ainsi que tous les attributs personnalisés supplémentaires que vous souhaitez ajouter à vos profils utilisateur dans Braze.

Faites glisser les attributs CDP de Redpoint dans la colonne **Attribut**. Attribuez à chaque **valeur de ligne d'en-tête** l'[attribut utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) Braze correspondant. 

Le tableau suivant répertorie les attributs de Redpoint CDP et leurs attributs correspondants de Braze :

| Attribut de point rouge | Valeur de la ligne d'en-tête |
|--------------------|------------------|
| PID                | `external_id`    |
| Prénom          | `first_name`     |
| Nom de famille          | `last_name`      |
| E-mail principal      | `email`          |
| Pays principal    | `country`        |
| DATE DE NAISSANCE                | `dob`            |
| Sexe             | `gender`         |
| Ville principale       | `home_city`      |
| Téléphone principal      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ajoutez l'attribut **Nom de sortie** de la table **Historique des offres**. Enfin, ajoutez tous les autres attributs Redpoint personnalisés que vous souhaitez fusionner dans Braze. Par exemple, vous trouverez ci-après un modèle d'onboarding et de mise à jour/insertion avec le diplôme, le revenu et l'état civil comme attributs supplémentaires.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### Étape 1b : Créer le modèle d'ajout Braze

Créez un deuxième modèle d'exportation pour les opérations d’ajout uniquement intitulé **Ajout Braze**.

Vous ne définirez que deux attributs pour ce modèle. Pour **PID**, définissez la **valeur de la ligne d'en-tête** sur `external_id`. Pour **Output Name**, définissez la **Header Row** comme `output_name`.

![Un exemple de modèle d'exportation avec les attributs `external_id` et output name.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### Étape 1c: Définir le format de la date

Pour les deux modèles d'exportation, accédez à l'**Options** onglet et définissez le **Format de date** sur la valeur de **Format personnalisé**. Définir le format comme **yyyy-MM-dd**.

![L'onglet des options indique que le format de la date est défini sur aaaa-MM-jj.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### Étape 2 : Créer des canaux sortants

Dans RPI, créez deux nouveaux canaux. Réglez les deux canaux sur **Distribution sortante**. Nommez un canal **Braze Onboarding et Upsert**, et l'autre **Braze Append**.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
Après l'onboarding initial de vos enregistrements CDP vers Braze, vérifiez si les workflows Redpoint Interaction suivants qui utilisent le canal d'onboarding et de mise à jour de Braze sont conçus pour sélectionner uniquement les enregistrements qui ont changé depuis la synchronisation initiale de l'onboarding.
{% endalert %}

### Étape 3 : Configurer les canaux

#### Étape 3a: Définir le modèle et le format du chemin d'exportation

Naviguez vers l'onglet **Général** dans l'écran de **Configuration** des canaux. Définir le modèle d'exportation pour chaque canal respectif. 

Ensuite, définissez un **format de chemin d'exportation** sur les deux canaux qui pointent vers un emplacement de réseau partagé, un protocole de transfert de fichiers ou un emplacement de fournisseur de contenu externe accessible à la fois à Redpoint Interaction et à Redpoint Gestion des données. 

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

Le format du répertoire d'exportation sur les deux canaux sera identique et devrait se terminer par `\\[Channel]\\[Offer]\\[Workflow ID]`.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### Étape 3b : Configurer l'exécution post

Accédez à l'onglet **Exécution de la publication** dans l'écran de **configuration** des canaux. 

Cochez la case **Post-exécution** pour appeler une URL de service après l'exécution du canal. Entrez l'URL du service Web de gestion des données Redpoint. Cette entrée sera identique sur vos canaux d'onboarding et d’ajout.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### Étape 4 : Configurer les composants Braze dans la gestion des données Redpoint 

L'archive contenant les artefacts de gestion des données Redpoint (RPDM) pour prendre en charge l'intégration Braze contient un fichier README avec des instructions détaillées pour configurer les composants requis. Gardez à l'esprit les détails suivants lors de la configuration de votre intégration. 

#### Étape 4a: Mettre à jour le RPI vers l'automatisation Braze avec votre endpoint REST Braze et le répertoire de sortie de base RPI 

Après avoir importé les composants associés de Braze dans le composant de gestion des données Redpoint, ouvrez l'automatisation nommée **AUTO_Process_RPI_to_Braze** et mettez à jour les deux variables d'automatisation suivantes avec les valeurs de votre environnement :

* **BRAZE_API_URL**: L'endpoint REST de Braze
* **BASE_OUTPUT_DIRECTORY** : Le répertoire de sortie partagé entre la fonction d’interaction de Redpoint et la fonction de gestion des données de Redpoint

![]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### Étape 4b : Mettre à jour le RPI pour le projet d'ajout de Braze 

Le projet de gestion des données Redpoint nommé **PROJ_RPI_to_Braze_Append** contient le schéma de fichier d'exportation de distribution sortant et les mappages pour l'objet attribut personnalisé `rpi_cdp_attributes` dans Braze. 

Mettre à jour le schéma de fichier d'entrée et l'outil d'injection de document nommé **RPI to Braze Document Injector** avec tous les attributs CDP personnalisés supplémentaires définis dans votre modèle de fichier d'exportation. Cet exemple montre le mappage supplémentaire de l'éducation, des revenus et de l'état civil :

![]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## Utilisation de l'intégration

Le canal Braze de distribution sortante peut désormais être exploité dans les flux d’interaction Redpoint. Suivez les pratiques standard pour créer des règles de sélection et des audiences dans RPI, et pour créer des calendriers de workflow et des déclencheurs associés. 

Pour activer la synchronisation d'une audience RPI vers Braze, créez une offre de distribution sortante et associez-la soit au **onboarding et mise à jour de Braze**, soit au canal **ajout de Braze**. Ce choix dépend de si vous avez l’intention de créer ou de fusionner de nouveaux enregistrements dans Braze, ou seulement d'ajouter des données de campagne si l'enregistrement existe déjà dans Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

Une fois que le flux de travail a été exécuté avec succès dans RPI, l'orchestration et les données CDP provenant de RPI peuvent maintenant être utilisées pour créer des segments dans Braze.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

Vous pouvez voir les propriétés associées à Redpoint sur le profil utilisateur.

![]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}


