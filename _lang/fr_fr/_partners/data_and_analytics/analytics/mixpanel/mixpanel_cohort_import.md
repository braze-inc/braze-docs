---
nav_title: Mixpanel
article_title: Importation de la cohorte Mixpanel
description: "Cet article de référence présente la fonctionnalité d'importation de cohortes de Mixpanel, une plateforme d'analyse commerciale, vous permettant d'importer des cohortes Mixpanel dans Braze afin de créer des segments Braze qui peuvent être utilisés pour cibler les utilisateurs dans de futures campagnes ou canvas Braze."
page_type: partner
search_tag: Partner
---

# Importation de la cohorte Mixpanel

> Cet article décrit comment importer des cohortes d'utilisateurs de [Mixpanel](https://mixpanel.com/) vers Braze. Pour plus d'informations sur l'intégration de Mixpanel et de ses autres fonctionnalités, consultez l'article sur [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/).

## Intégration de l'importation de données

Toute intégration que vous mettez en place sera prise en compte dans le volume de points données de votre compte.

{% alert important %}
Conformément à la politique de conservation des données de Mixpanel, les événements envoyés avant le 1er janvier 2010 seront supprimés lors de l'importation.
{% endalert %}

### Étape 1 : Obtenez la clé d'importation des données Braze

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques** et sélectionnez **Mixpanel**. Ici, vous trouverez l’endpoint REST et générerez votre clé d'importation des données Braze. 

Une fois générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l’endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord de Mixpanel.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Étape 2 : Configurez l'intégration de Braze dans Mixpanel

Dans Mixpanel, accédez à **Gestion des données > Intégrations**. Ensuite, sélectionnez l'onglet de l'intégration Braze et cliquez sur **Connecter**. Dans l'invite qui s'affiche, indiquez la clé d'importation des données de Braze et l’endpoint REST, puis cliquez sur **Continuer**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Étape 3 : Exporter une cohorte Mixpanel vers Braze

Dans Mixpanel, accédez à **Gestion des données > Cohortes**. Sélectionnez la cohorte à envoyer à Braze, puis sélectionnez **Exporter vers Braze**. Enfin, sélectionnez une synchronisation unique ou une synchronisation dynamique. En sélectionnant la synchronisation dynamique, votre cohorte Braze sera synchronisée toutes les 15 minutes pour correspondre aux utilisateurs dans Mixpanel. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

### Étape 4 : Segmentation des utilisateurs à Braze

Dans Braze, pour créer un segment de ces utilisateurs, allez dans **Audience** > **Segments**, nommez votre segment et sélectionnez **Mixpanel_Cohorts** comme filtre. Ensuite, utilisez l'option "inclut" et choisissez la cohorte que vous avez créée dans Mixpanel. 

![Dans le générateur de segments Braze, le filtre d'attributs d’utilisateur "cohortes Mixpanel" est défini sur "inclut" et "cohorte Braze".]({% image_buster /assets/img_archive/mixpanel1.png %})

Après l'avoir enregistré, vous pouvez faire référence à ce segment lors de la création d'un canvas ou d'une campagne à l'étape du ciblage des utilisateurs.

## Correspondance entre les utilisateurs

Les utilisateurs identifiés peuvent être associés à leur adresse `external_id` ou `alias`. Les utilisateurs anonymes peuvent être mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id`, et doivent être identifiés par leur `external_id` ou `alias`.