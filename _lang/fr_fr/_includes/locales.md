{% if include.section == "Prerequisites" %}
## Conditions préalables

Pour modifier et gérer [la prise en charge multilingue]({{site.baseurl}}/multi_language_support/), vous devez disposer des [autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) suivantes pour votre espace de travail :

- Afficher les paramètres de localisation
- Modifier les paramètres de localisation
- Supprimer les paramètres de localisation

Pour ajouter la locale à un message, vous devez disposer de l'autorisation « Modifier les campagnes ».

{% alert important %}
La prise en charge multilingue est actuellement en accès anticipé. Contactez votre Account Manager Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

{% endif %}

{% if include.section == "Preview" %}

## Prévisualiser vos locales

Dans la liste déroulante **Prévisualiser le message en tant qu'utilisateur** de l'onglet **Test**, sélectionnez **Utilisateur personnalisé** et saisissez différentes langues pour prévisualiser le message et vérifier que la traduction s'affiche comme prévu.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Foire aux questions

#### Puis-je modifier la version traduite dans l'une de mes locales ?
Oui. Modifiez d'abord le fichier CSV, puis importez-le à nouveau pour mettre à jour la traduction.

#### Puis-je imbriquer des étiquettes de traduction ?
Non.

#### Puis-je ajouter du style HTML dans les étiquettes de traduction ?
Oui, mais vérifiez que le style HTML n'est pas traduit avec le contenu.

#### Quelles validations ou vérifications supplémentaires Braze effectue-t-il ?

| Scénario                                                                                                                                                 | Validation dans Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Il manque dans le fichier de traduction des locales associées au message en cours.                                                                               | Ce fichier de traduction ne sera pas importé.                                                                       |
| Il manque dans le fichier de traduction des blocs de texte, par exemple un texte contenu dans des étiquettes de traduction Liquid, provenant du message e-mail en cours.                                | Ce fichier de traduction ne sera pas importé.                                                                       |
| Le fichier de traduction contient le texte par défaut qui ne correspond pas aux blocs de texte du message e-mail actuel.                                          | Ce fichier de traduction ne sera pas importé. Corrigez ce problème dans votre CSV avant de réessayer l'import.               |
| Le fichier de traduction contient des locales qui n'existent pas dans les paramètres de **prise en charge multilingue**.                                                           | Ces locales ne seront pas enregistrées dans Braze.                                                                      |
| Le fichier de traduction contient des blocs de texte qui n'existent pas dans le message actuel (par exemple le brouillon en cours au moment de l'import des traductions). | Les blocs de texte absents de votre message actuel ne seront pas enregistrés depuis le fichier de traduction vers Braze. |
| Suppression d'une locale du message alors que celle-ci a déjà été importée dans le message via le fichier de traduction.                           | La suppression de la locale entraîne la suppression de toutes les traductions qui lui sont associées dans votre message.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}