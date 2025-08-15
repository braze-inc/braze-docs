---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "Cet article de référence présente le partenariat entre Braze et Optimizely qui vous permet de synchroniser vos segments personnalisés, événements et Currents de Braze avec Optimizely Data Platform."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/) est une plateforme d'expérience numérique de premier plan qui propose des outils d'expérimentation et de gestion de contenu pour les produits numériques et les campagnes marketing.

L'intégration entre Braze et Optimizely est une intégration bidirectionnelle qui vous permet de :

- Synchronisez chaque nuit vos segments et événements personnalisés de Braze vers Optimizely Data Platform (ODP) afin d'enrichir les profils, rapports et segmentations des clients d'Optimizely.
- Envoyez les événements de Braze Currents depuis Braze vers l'outil de reporting d'Optimizely.
- Synchronisez les données et événements personnalisés de l'ODP vers Braze pour enrichir vos données clients et déclencher l'envoi de messages Braze en fonction des événements clients dans l'ODP.

## Conditions préalables

| Condition                     | Description |
|----------------------------------|-------------|
| Compte Optimizely Data Platform | Un compte Optimizely Data Platform (ODP) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze               | Une clé API REST de Braze avec les autorisations suivantes : `users.track`,`users.export.segments`,`segments.list`,`campaigns.trigger.send`, et `canvas.trigger.send`. |
| Currents                         | Pour réexporter des données dans Optimizely, vous devez avoir configuré Braze Currents pour votre compte. |
| URL et jeton Optimizely         | Vous pouvez l'obtenir en naviguant dans votre tableau de bord Optimizely et en copiant l'URL d'ingestion et le jeton. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Configurer l'intégration

1. Dans le **répertoire d'applications** d'Optimizely Data Platform (ODP), sélectionnez l'application **Braze**, puis cliquez sur **Installer l'application**.
2. Accédez à l'onglet **Paramètres**. Dans la section **Autorisation**, procédez comme suit :
    1. Saisissez la **clé de l'API REST de** Braze.
    2. Sélectionnez l'**URL de** votre **instance** Braze.
    2. Sélectionnez **Vérifier la clé API.**
3. Dans Braze, allez à **[Courants]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)**.
4. Sélectionnez **Créer un nouveau courant** > **Exportation de courants personnalisés**.
5. Configurez le courant à l'aide de l'endpoint et du jeton fournis dans l'ODP. Cette opération est nécessaire pour synchroniser les événements de Braze avec l'ODP. 

![Autorisation Optimizely.][1]

{:start="6"}
6\. Dans ODP, développez la section **Segments** et sélectionnez des segments personnalisés dans la liste **Segments à synchroniser** ou sélectionnez **Importer tous les clients** pour synchroniser tous les segments.
7\. Ajoutez les [mappages de champs supplémentaires](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) que vous souhaitez entre Braze et l'ODP.
8\. Sélectionnez **Enregistrer**.

![Optimizely Braze segmentation sync.][2]

{% alert tip %}
Vous devez sélectionner des segments pour importer des profils de clients de Braze. Si vous ne sélectionnez aucun segment, l'intégration n'importera aucun profil de client.
{% endalert %}

### Étape 2 : Champs de données cartographiques

L'intégration a des mappages de champs de données par défaut entre Braze et l'ODP. Par exemple, le champ **E-mail** dans Braze est mappé au champ **E-mail de la dernière visite** dans l'ODP.

![Optimizely et Braze segmentent les champs de cartes.][3]

#### Mappez des champs supplémentaires (facultatif)

Si vous souhaitez mapper des champs de données supplémentaires dans Braze vers ODP, procédez comme suit dans ODP :

1. Dans la section **Segments** de l'appli, sélectionnez le champ Braze dans la liste déroulante **Champs de données utilisateur Braze**.
2. Sélectionnez le champ ODP dans la liste déroulante **Champs clients ODP**.
3. Sélectionnez **Enregistrer le mappage des champs**.

![Optimizely Braze Segmenter Enregistrer les mappages de terrain][4]

#### Supprimer les mappages de champs non requis (facultatif)

Vous pouvez également supprimer tous les mappages de champs de données qui ne sont pas nécessaires. Effectuez les opérations suivantes dans l'ODP :

1. Dans la section **Segments** de l'application, sélectionnez le mappage de champ que vous souhaitez supprimer dans la liste déroulante **Mappage de champ**.
2. Sélectionnez **Supprimer le mappage de champ**.

![Optimizely Braze Segmenter Supprimer les mappages de champs][5]

### Étape 3 : Synchroniser les données de la plateforme de données Optimizely (ODP) vers Braze.

Après avoir configuré l'intégration, vous pouvez configurer une activation dans ODP pour synchroniser vos données clients ODP avec Braze.

1. Allez dans **Activation** > **Engage** et sélectionnez **Créer une nouvelle campagne.**
2. Sélectionnez **Comportemental** pour mettre en place une synchronisation automatique et récurrente.
3. Sélectionnez **Créer à partir de zéro**, puis saisissez un nom pour votre activation qui conseille les données que vous synchronisez avec **Braze**(par exemple **Braze Data Sync**).
4. Dans la section **Inscription**, vous pouvez synchroniser les données des clients qui correspondent à un segment ou synchroniser les données des clients qui déclenchent un événement personnalisé (par exemple, lorsque l'ODP enregistre qu'un client ouvre un e-mail) :
   - **Les clients qui correspondent à un segment :** Sélectionnez le segment de votre choix, puis cliquez sur **Suivant.**<br><br>![Optimizely Select Segment][6]
   - **Les clients qui déclenchent un événement :** Développez la liste déroulante **Filtre** et sélectionnez l'événement ODP à utiliser comme déclencheur de cette synchronisation de données vers Braze. Développez ensuite les **règles d'automatisation** et ajustez-les comme vous le souhaitez. <br><br>![Événement déclencheur Optimizely][7]
5. Développez **Touchpoints**, sélectionnez pour modifier **Touchpoint 1**, puis sélectionnez **Braze**.
6. Développez la section **Ciblage**, puis sélectionnez l'**identifiant de la cible**.
7. Sélectionnez l'une des options suivantes pour **Ajouter des utilisateurs à dans** la section **Configurer**:
    - **Campagne :** Ajoutez des clients à une campagne spécifique dans Braze. Après avoir choisi cette option, vous devez sélectionner la campagne Braze.
    - **Canvas :** Ajoutez des personnalisés à une toile spécifique dans Braze. Après avoir choisi cette option, vous devez sélectionner la toile Braze.
    - **Mise à jour du profil uniquement :** Mettez à jour uniquement le profil du client de Braze.
8. (Facultatif) Sélectionnez le **nombre de champs supplémentaires** que vous souhaitez synchroniser avec Braze (jusqu'à 20).  
    Ensuite, sélectionnez les éléments suivants pour la liste déroulante et le champ de saisie de chaque champ supplémentaire :
    - Dans chaque liste déroulante **des** champs, sélectionnez le champ de Braze que vous souhaitez remplir. 
    - Dans chaque **valeur de champ** correspondante, entrez le champ ODP que vous souhaitez envoyer au champ Braze sélectionné. Par exemple, si vous avez sélectionné **Nom de l'entreprise** dans la liste déroulante du **champ #**, entrez `{{customer.company_name}}` pour la **valeur** correspondante **du champ #.**
9. Sélectionnez **Enregistrer**, puis choisissez votre nom d'activation dans le fil d'Ariane.
10. Sélectionnez **Sélectionner l'heure de début et la planification** dans la section **Points de contact** si vous avez sélectionné des **Clients correspondant à une segmentation** pour l'inscription.
11. Complétez les paramètres suivants :
    - **Récurrent ou continu :** Sélectionnez **Récurrent**.
    - **Date de début :** Saisissez la date à laquelle vous souhaitez envoyer les données à Braze.
    - **Fin :** La valeur par défaut est **Jamais**. Si vous souhaitez mettre fin à la synchronisation des données de Braze à une date précise, définissez-la ici.
    - **Se répète :** Régler sur **quotidien**.
    - **Répétez tous les** \- Réglez sur **1 jour**.
    - **Calendrier :** Saisissez l'heure à laquelle vous souhaitez envoyer les données à Braze.
    - **Fuseau horaire :** Sélectionnez le fuseau horaire dans lequel vous souhaitez envoyer ces données.
12. Sélectionnez **Appliquer**, **Enregistrer**, puis **Passer en ligne/instantané**. Votre synchronisation commence à la date et à l'heure de début que vous avez désignées (ou lorsque l'événement déclencheur se produit).

## Résolution des problèmes

### Inspecter les événements

Pour vérifier que les données sont correctement synchronisées entre l'ODP et Braze, vous pouvez inspecter les événements dans l'ODP.

1. Dans l'ODP, allez dans **Paramètres du compte** > **Inspecteur d'événements**.
2. Sélectionnez **Démarrer l'inspecteur**.
3. Lorsque des données sont disponibles dans l'inspecteur, un nombre s'affiche à côté d'**Actualiser**. Sélectionnez cette option pour afficher les données.
4. Les données brutes que l'ODP et Braze se renvoient s'affichent. Sélectionnez **Afficher les détails** pour voir la version formatée de ces données brutes.
5. Les champs de données renvoyés par Braze à l'ODP commencent par `_braze`.

### Vérifier les journaux d'activité

Chaque synchronisation de données est également enregistrée dans le [journal d'activité de l'ODP](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP):

1. Allez dans **Paramètres du compte** > **Journal d'activité.**
2. Filtrez les catégories par **Braze**.
3. Sélectionnez **Afficher les détails** pour obtenir une vue formatée des détails du journal, y compris le nombre de correspondances.

[1]: {% image_buster /assets/img/optimizely/image1_authorization.png %}
[2]: {% image_buster /assets/img/optimizely/image2_syncsegment.png %}
[3]: {% image_buster /assets/img/optimizely/image3_emailmapfield.png %}
[4]: {% image_buster /assets/img/optimizely/image4_mapfields.png %}
[5]: {% image_buster /assets/img/optimizely/image5_deletephonefield.png %}
[6]: {% image_buster /assets/img/optimizely/image6_segment.png %}
[7]: {% image_buster /assets/img/optimizely/image7_trigger.png %} 