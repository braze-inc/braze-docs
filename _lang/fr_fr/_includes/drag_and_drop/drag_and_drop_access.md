{% if include.variable_name == "dnd editors" %}

{% alert important %}
Pour accéder à l'éditeur par glisser-déposer, contactez votre administrateur informatique pour vérifier que votre pare-feu a bien inscrit `*.bz-rndr.com` sur sa liste d'autorisation.
{% endalert %}

{% elsif include.variable_name == "email html editor" %}

{% alert important %}
Pour accéder à l'éditeur HTML, contactez votre administrateur informatique pour vérifier que votre pare-feu a bien inscrit `*.bz-rndr.com` sur sa liste d'autorisation.
{% endalert %}

{% endif %}