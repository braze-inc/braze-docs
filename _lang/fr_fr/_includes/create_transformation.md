Dans le tableau de bord de Braze, sélectionnez **Paramètres des données** > **Transformation des données**.

Sélectionnez **Créer une transformation** pour nommer votre transformation, puis choisissez votre expérience de modification.

![Détails de la transformation avec la possibilité de choisir « Utiliser un modèle » ou « Démarrer de zéro » pour votre expérience de modification.]({% image_buster /assets/img/data_transformation/data_transformation10.png %})

Sélectionnez **Utiliser un modèle** pour parcourir une bibliothèque de modèles, y compris les cas d'utilisation de la transformation des données. Vous pouvez également choisir de **partir de zéro** pour charger un modèle de code par défaut. 

Si vous démarrez de zéro, choisissez une destination pour votre transformation. Vous pouvez toujours insérer un modèle de code à partir de la bibliothèque de modèles.

{% details En savoir plus sur les destinations %}
* **POST : Suivre les utilisateurs :** Transforme les webhooks d'une plateforme source en mises à jour du profil utilisateur, telles que les attributs, les événements ou les achats.
* **PUT : Mettez à jour plusieurs éléments du catalogue :** Transforme les webhooks d'une plateforme source en mises à jour d'éléments du catalogue.
* **DELETE : Supprimez plusieurs éléments du catalogue :** Transforme les webhooks d'une plateforme source en suppressions d'éléments du catalogue.
* **PATCH : Modifiez plusieurs éléments du catalogue :** Transforme les webhooks d'une plateforme source en modifications d'éléments de catalogue.
* **POST : Envoyez des messages immédiatement via l'API uniquement :** Transforme les webhooks d'une plateforme source pour envoyer des messages immédiats à des utilisateurs désignés.
{% enddetails %}

{% alert note %}
Vous souhaitez demander des modèles ou des destinations supplémentaires ? Pensez à donner votre [avis sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

Après avoir créé votre transformation, vous verrez la vue détaillée de la transformation. Ici, vous pouvez voir le webhook le plus récent reçu pour cette transformation sous **Détails du webhook** et un espace pour écrire votre code de transformation sous **Code de transformation.**

{% if include.location == "typeform" %}

![]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

Capturez l'**URL de votre webhook** pour l'utiliser à l'étape suivante.

{% endif %}
