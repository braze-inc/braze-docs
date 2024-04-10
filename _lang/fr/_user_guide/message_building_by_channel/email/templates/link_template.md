---
nav_title: Modèles de liens
article_title: Modèles de liens
page_order: 5
description: "Cet article explique comment créer différents types de modèles de liens dans vos e-mails."
tool:
  - Templates
channel:
  - e-mail

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/creating-link-templates){: style="float:right;width:120px;border:0;" class="noimgborder"}Modèles de lien

> Les modèles de liens vous permettent d’ajouter des paramètres ou des URL à tous les liens dans un courrier électronique. Ceci est le plus souvent utilisé dans les cas suivants :

1. Ajouter des paramètres de requête Google Analytics à tous les liens dans un e-mail donné
2. Ajouter une URL à tous les liens dans un e-mail donné

{% alert note %}
Lorsque vous utilisez des modèles de liens et [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), le code Liquid ne doit être ajouté que dans la balise du corps pour garantir un rendu cohérent.
{% endalert %}

## Création d’un modèle de lien

![][11]{: style="float:right;max-width:20%;"}

Pour créer un modèle de lien, accédez à **Templates & Media (Modèles et médias)** et sélectionnez l’onglet **Link Templates (Modèles de liens)**. Vous pouvez créer un nombre illimité de modèles de liens pour répondre à vos différents besoins. Cliquez sur **Create Link Template (Créer un modèle de lien)** pour commencer.

{% alert note %}
Les modèles de liens sont une fonctionnalité facultative. Si l’onglet **Modèles de liens** n’apparaît pas dans votre page **Templates & Media (Modèles et médias)**, contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la fonctionnalité de bascule Oui/Non pour les modèles de liens.
{% endalert %}

Il existe deux types de modèles de liens que vous pouvez créer :

- [Le modèle de lien qui s’insère avant une URL](#prepend-link-template)
- [Le modèle de lien qui s’insère après une URL](#append-link-template)

### Ajouter avant une URL : Créer un modèle de lien qui s’insère avant une URL {#prepend-link-template}

Si vous souhaitez ajouter une chaîne de caractères ou une URL avant les liens de votre e-mail, créez un nouveau modèle de lien et définissez la **position du modèle** sur **Avant l’URL**.  Cela vous permettra de saisir une chaîne de caractères qui précèdera toujours votre URL. 

Une section d’aperçu est fournie pour vous donner un exemple de processus d’insertion.

![Champs Position du modèle, Ajout avant l’URL et Aperçu du modèle pour le processus d’insertion du modèle de lien avant une URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Ajouter : Créer un modèle de lien qui s’insère après une URL {#append-link-template}

Si vous souhaitez ajouter des paramètres de requête après une URL dans votre e-mail, créez un nouveau modèle de lien et définissez la **position du modèle** sur **Après l’URL**.  Vous pourrez ainsi saisir les paramètres de requête (`value=something`) à la fin de chaque URL.  

Vous pouvez avoir plusieurs paramètres ajoutés à la fin d’une URL.

![Champs Position du modèle, Paramètres de requête et Aperçu du modèle pour le processus d’insertion du modèle de lien après une URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Utilisation de vos modèles dans des campagnes par e-mail

Une fois que vos modèles sont configurés, vous pouvez sélectionner le modèle que vous souhaitez utiliser dans votre e-mail depuis l’éditeur de courrier électronique.

- **Éditeur d’e-mail HTML :** Sélectionnez votre modèle depuis l’onglet **Link Management (Gestion des liens)**. 
- **Éditeur Drag & Drop :** Sélectionnez **Content (Contenu)** puis **Link Management (Gestion des liens)**. Vous verrez tous les liens présents dans votre e-mail et pourrez ajouter le modèle à partir de là. Pour accéder aux modèles de lien dans l’éditeur Drag & Drop, votre [aliasage de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) doit être activé. 

![Onglet Gestion des liens dans l’éditeur Drag & Drop avec une liste d’exemples de modèles de lien.][1]

## Gestion des modèles de lien

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) les modèles de lien ! Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la section [Templates & Media (Modèles et médias)]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
Les modèles d’archivage ne sont actuellement pas disponible pour les [modèles de liens]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

## Foire aux questions

Pour obtenir des réponses aux questions fréquemment posées sur les modèles de liens, consultez notre page [FAQ sur les modèles][10].

[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[11]: {% image_buster /assets/img_archive/create_link_template.png %}
