---
nav_title: Hightouch
article_title: Importation de cohortes Hightouch
description: "Cet article de référence décrit la fonctionnalité d'importation de la cohorte de Hightouch, une plateforme permettant de synchroniser les données de vos clients depuis votre entrepôt avec les outils commerciaux."
page_type: partner
search_tag: Partner

---
# Importation de la cohorte Hightouch

> Cet article explique comment importer des cohortes d'utilisateurs de [Hightouch][1] vers Braze afin de pouvoir envoyer des campagnes ciblées en fonction de données qui n'existent peut-être que dans votre entrepôt. [Pour plus d'informations sur l'intégration de Hightouch et de ses autres fonctionnalités, consultez l'article principal sur Hightouch.]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/hightouch/)

## Intégration de l'importation de données

### Étape 1 : Obtenez la clé d'importation des données Braze
Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Hightouch**. 

Ici, vous trouverez votre endpoint REST et générerez la clé d'importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante.<br><br>![][6]{: style="max-width:90%;"} 

### Étape 2 : Ajoutez les cohortes de Braze en tant que destination dans Hightouch
Accédez à la page **Destination** de votre espace de travail Hightouch, recherchez l’entrée **Cohortes Braze** et cliquez sur **Continuer**. À partir de là, définissez votre endpoint REST et votre clé d'importation des données, puis cliquez sur **Continuer**.<br><br>![][7]{: style="max-width:90%;"}

### Étape 3 : Synchroniser un modèle (ou une audience) dans Braze Cohorts
Dans Hightouch, à l'aide du [modèle](https://hightouch.io/docs/getting-started/create-your-first-sync/#create-a-model) ou de l'[audience](https://hightouch.io/docs/audiences/usage/) que vous avez créé, créez une nouvelle synchronisation. Ensuite, sélectionnez la destination Braze Cohorts que vous avez créée à l'étape précédente. Enfin, dans la configuration de destination de Braze Cohorts, sélectionnez l'identifiant que vous souhaitez comparer et décidez si vous souhaitez que Hightouch crée une nouvelle cohorte Braze ou mette à jour une cohorte existante.<br><br>![][8]{: style="max-width:90%;"}

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

### Étape 4 : Créez un segment Braze à partir de l'audience personnalisée Hightouch
Dans Braze, accédez à **Segments**, créez un nouveau segment et sélectionnez **Hightouch Cohorts** comme filtre. À partir de là, vous pouvez choisir la cohorte Hightouch que vous souhaitez inclure. Une fois votre segment de cohorte Hightouch créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.<br><br>![][9]{: style="max-width:90%;"}

### Utilisation de cette intégration
Pour utiliser votre segment Hightouch, créez une campagne Braze ou Canvas et sélectionnez le segment comme audience cible.<br><br>![][10]{: style="max-width:90%;"}

## Correspondance entre les utilisateurs

Les utilisateurs identifiés peuvent être associés à leur adresse `external_id` ou `alias`. Les utilisateurs anonymes peuvent être mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id`, et doivent être identifiés par leur `external_id` ou `alias`.

[1]: https://hightouch.io
[6]: {% image_buster /assets/img/hightouch/data_import_key.png %}
[7]: {% image_buster /assets/img/hightouch/cohort1.png %}
[8]: {% image_buster /assets/img/hightouch/cohort2.png %}  
[9]: {% image_buster /assets/img/hightouch/cohort3.png %}  
[10]: {% image_buster /assets/img/hightouch/cohort4.png %}  