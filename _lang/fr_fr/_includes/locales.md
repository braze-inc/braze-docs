{% if include.section == "Prerequisites" %}
## Conditions préalables

Pour modifier et gérer la [prise en charge multilingue]({{site.baseurl}}/multi_language_support/), vous devez disposer de l’autorisation « Gérer les paramètres multilingues ». Pour ajouter le paramètre régional à un message, vous devez disposer des autorisations nécessaires pour modifier les campagnes.

{% alert important %}
La prise en charge du multilinguisme est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

{% endif %}

{% if include.section == "Preview" %}

## Prévisualiser vos paramètres régionaux

Dans la liste déroulante **Prévisualiser le message en tant qu'utilisateur** de l'onglet **Test**, sélectionnez **Utilisateur personnalisé** et entrez différentes langues pour prévisualiser le message afin de vérifier si votre message se traduit comme prévu.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Foire aux questions

#### Puis-je apporter une modification à la version traduite dans l'un de mes pays ?
Oui. Modifiez d'abord le fichier CSV, puis téléchargez à nouveau le fichier pour apporter une modification à la copie traduite.

#### Puis-je imbriquer des tags de traduction ?
Non.

#### Puis-je ajouter un style HTML dans les étiquettes de traduction ?
Oui, mais vérifiez que le style HTML n'est pas traduit avec le contenu.

#### Quelles sont les validations ou les vérifications supplémentaires effectuées par Braze ?

| Scénario                                                                                                                                                 | Validation en Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Il manque, dans un fichier de traduction, les paramètres régionaux associés au message en cours.                                                                               | Ce fichier de traduction ne sera pas téléchargé.                                                                       |
| Il manque, dans un fichier de traduction, des blocs de texte, par exemple un texte à l'intérieur des tags Liquid, provenant du message e-mail en cours.                                | Ce fichier de traduction ne sera pas téléchargé.                                                                       |
| Le fichier de traduction inclut le texte par défaut qui ne correspond pas aux blocs de texte du message e-mail actuel.                                          | Ce fichier de traduction ne sera pas téléchargé. Corrigez ce problème dans votre CSV avant d'essayer de le télécharger à nouveau.               |
| Le fichier de traduction inclut des langues qui n'existent pas dans les paramètres de **prise en charge multilingue**.                                                           | Ces paramètres régionaux ne seront pas enregistrés dans Braze.                                                                      |
| Le fichier de traduction comprend des blocs de texte qui n'existent pas dans le message actuel (comme le brouillon actuel au moment où les traductions sont chargées). | Les blocs de texte qui n'existent pas dans votre message actuel ne seront pas enregistrés du fichier de traduction vers Braze. |
| Suppression d'un paramètre régional du message alors que ce paramètre régional a déjà été chargé dans le message en tant que partie du fichier de traduction.                           | En supprimant le paramètre régional, vous supprimez toutes les traductions associées à celui-ci dans votre message.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}
