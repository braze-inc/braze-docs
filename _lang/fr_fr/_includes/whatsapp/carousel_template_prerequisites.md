Avant de [créer des modèles de carrousel]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/template_builder/whatsapp_carousel_templates/#create-a-carousel-template), vous avez besoin des éléments suivants :
- Un compte WhatsApp Business (WABA) actif connecté à Braze
- Des groupes d'abonnement appropriés configurés au sein de votre WABA
- Des ressources multimédias (images ou vidéos) prêtes à être importées
- Des autorisations Braze pour les utilisateurs non administrateurs
    - Pour que les utilisateurs puissent créer de nouveaux modèles dans le générateur de modèles :
        - « View WhatsApp Message Templates »
        - « Edit WhatsApp Message Templates »
    - Pour que les utilisateurs puissent rédiger des campagnes ou des Canvas avec des modèles de carrousel :
        - « View WhatsApp Message Templates »
- Une connaissance du langage de modèles Liquid (facultatif, pour le contenu dynamique)

{% alert important %}
Tous les numéros de téléphone et groupes d'abonnement au sein d'un même compte WhatsApp Business (WABA) partagent les mêmes modèles. Si vous disposez de plusieurs groupes d'abonnement au sein d'un même WABA, ils peuvent tous accéder aux mêmes modèles de carrousel. En revanche, les modèles ne sont pas partagés entre différents WABA.
{% endalert %}