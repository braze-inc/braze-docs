---
nav_title: Modèles de lien
article_title: Modèles de lien
page_order: 4
description: "Cet article explique comment créer différents types de modèles de liens dans vos e-mails."
tool:
  - Templates
channel:
  - email

---

# Modèles de lien

> Avec les modèles de liens, vous pouvez créer des liens dynamiques et réutilisables pour vos campagnes d'e-mail en ajoutant des paramètres ou des URL. Cela permet d'assurer la cohérence des URL dans l'ensemble de vos campagnes et de vos messages. 

{% alert note %}
Les modèles de liens sont une fonctionnalité facultative. Si l'option **Modèles de liens e-mail** n'apparaît pas dans la section **Modèles**, contactez votre gestionnaire de compte pour activer cette fonctionnalité.
{% endalert %}

## Fonctionnement

Les modèles de liens sont le plus souvent utilisés dans les cas suivants :

- Ajouter des paramètres de requête Google Analytics à tous les liens dans un e-mail donné
- Ajouter une URL à tous les liens dans un e-mail donné

Imaginons que vous lanciez une campagne d'e-mails promotionnels pour le lancement d'un nouveau produit. Vous pouvez utiliser un modèle de lien qui dirige les utilisateurs vers la page du produit et personnaliser le lien pour y inclure le nom de votre utilisateur ou un code promotionnel spécifique. Vous pouvez ainsi savoir combien d'utilisateurs ont cliqué sur le lien et ont effectué un achat. De cette façon, vous pouvez créer une cohérence entre vos liens et mieux suivre vos analyses/analytiques.

## Création d’un modèle de lien

Vous pouvez créer un nombre illimité de modèles de liens pour répondre à vos différents besoins. Pour créer un modèle de lien, procédez comme suit :

1. Allez dans **Modèles** > **Modèles de liens d'e-mail.** 
2. Sélectionnez **Créer un modèle de lien d'e-mail**.
3. Donnez un nom à votre modèle de lien.
4. (Facultatif) Ajoutez une description, une équipe ou une étiquette pour ajouter des détails sur le modèle de lien.
5. (Facultatif) Cochez la bascule pour ajouter automatiquement le modèle de lien aux liens dans les campagnes d'e-mail et les canevas. Ceci s'applique à l'ajout d'un nouveau lien à tout e-mail nouveau ou existant.

Il existe deux types de modèles de liens que vous pouvez créer :

- [Modèle de lien qui s'insère avant un URL](#prepend-link-template)
- [Modèle de lien qui s'insère après un URL](#append-link-template)

Lors de l'utilisation de modèles de liens et de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), ce dernier ne doit être ajouté qu'à l'intérieur de l'étiquette "body" afin de garantir un rendu cohérent.

### Ajouter avant une URL : Créer un modèle de lien qui s’insère avant une URL {#prepend-link-template}

Pour ajouter une chaîne de caractères ou une URL avant les liens dans votre message e-mail, procédez comme suit :

1. Créez un nouveau modèle de lien.
2. Définissez la **position du modèle** sur **Avant l'URL.** 
3. Saisissez une chaîne de caractères qui sera toujours ajoutée à votre URL. 

L'**aperçu du** modèle est fourni pour vous donner un exemple de la façon dont le modèle de lien sera inséré avant une URL.

![Champs Position du modèle, Ajout avant l’URL et Aperçu du modèle pour le processus d’insertion du modèle de lien avant une URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Ajouter : Créer un modèle de lien qui s’insère après une URL {#append-link-template}

Si vous souhaitez ajouter des paramètres de requête après une URL dans votre message e-mail :

1. Créez un nouveau modèle de lien.
2. Définissez la **position du modèle** sur **Après l'URL**. 
3. Saisissez les paramètres de requête (`value=example`) à la fin de chaque URL. Vous pouvez avoir plusieurs paramètres ajoutés à la fin d’une URL.

![Les champs Position du modèle, Paramètres de la requête et Aperçu du modèle pour le processus d'insertion du modèle de lien après un URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Utilisation de modèles de liens dans les campagnes d'e-mailing

Une fois vos modèles de liens configurés, vous pouvez sélectionner le modèle à utiliser dans votre e-mail.

- **Editeur HTML :** Accédez à l'onglet **Gestion des liens** dans la section **Contenu**. Sélectionnez **Ajouter un modèle de lien**, choisissez votre modèle de lien et sélectionnez **Ajouter.**

{% alert important %}
Pour accéder à l'onglet **Gestion des liens** dans l'éditeur d'e-mails HTML mis à jour, vous devez activer l'aliasage de liens. Pour activer l'aliasage de lien, contactez votre gestionnaire de compte.
{% endalert %}

- **Éditeur par glisser-déposer :** Sélectionnez **Contenu** > onglet **Gestion des liens.** Sélectionnez ensuite **Ajouter un modèle de lien**. Pour accéder aux modèles de liens dans l'éditeur par glisser-déposer, vous devez activer l'[aliasage de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/).

![Onglet Gestion des liens dans l'éditeur par glisser-déposer avec un exemple de liste de modèles de liens.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Les modèles de liens ne s'appliquent pas au texte brut. Cela signifie que Currents peut afficher des clics qui n'incluent pas les paramètres des modèles de lien, car ces clics peuvent provenir de la version texte de l'e-mail.
{% endalert %}

Lorsque vous ajoutez des modèles de liens dans l'onglet **Gestion des liens**, faites défiler vers la droite pour afficher les modèles que vous avez ajoutés. Si les liens existants dans un e-mail ont déjà un modèle de lien ajouté, les liens nouvellement ajoutés auront également le modèle de lien ajouté par défaut.

## Gestion des modèles de lien

Vous pouvez également [dupliquer les]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modèles de liens. Pour en savoir plus sur la création et la gestion de modèles et de contenus créatifs, consultez la rubrique [Modèles et médias.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)

{% alert important %}
L'archivage des modèles n'est pas disponible actuellement pour les modèles de liens.
{% endalert %}

## Foire aux questions

Pour obtenir des réponses aux questions fréquemment posées sur les modèles de liens, consultez notre page [FAQ sur les modèles.]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/) 

