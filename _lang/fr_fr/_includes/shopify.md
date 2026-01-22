{% if include.section == "Integration Tabs" %}

{% tabs local %}
{% tab standard %}
L'intégration standard est adaptée aux boutiques en ligne Shopify, offrant un processus de configuration simple et transparent. Cette option vous permet de connecter rapidement votre boutique Shopify à Braze, vous donnant ainsi les moyens d'exploiter de puissants outils d'engagement client sans disposer d'une expertise technique approfondie. Grâce à cette option d'intégration, vous pouvez synchroniser les données de vos clients, automatiser l'envoi de messages personnalisés et améliorer vos efforts de marketing grâce à des fonctionnalités complètes de Braze.

Pour utiliser l'intégration standard de Shopify, reportez-vous à la [configuration de l'intégration standard de Shopify]({{site.baseurl}}/shopify_standard_integration/).
{% endtab %}

{% tab personnalisé %}
L'intégration personnalisée offre une solution plus flexible et composable si vous utilisez Shopify Hydrogen ou prenez en charge une boutique headless. Cette option vous donne les moyens d'implémenter les SDK de Braze directement dans votre environnement Shopify, ce qui permet une intégration plus poussée et des fonctionnalités sur mesure. Que vous cherchiez à créer des expériences client uniques ou à optimiser des flux de travail spécifiques, l'intégration personnalisée fournit les outils nécessaires pour exploiter pleinement les capacités de Braze dans une configuration sans tête.

Pour utiliser l'intégration personnalisée de Shopify, reportez-vous à la [configuration de l'intégration personnalisée de Shopify]({{site.baseurl}}/shopify_custom_integration/).
{% endtab %}
{% endtabs %}

{% endif %}

{% if include.section == "Liquid promotion codes with Currents" %}

Vous pouvez combiner [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) avec des [codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) pour envoyer des informations sur les codes de promotion à Currents. Utilisez l'étiquette `capture` pour stocker le code de promotion dans une variable, puis faites référence à cette variable dans `message_extras`:

{% raw %}
```liquid
{% capture code %}
{% promotion('puttshacktest2') %}
{% endcapture %}
Use {{code}} for an exclusive discount!
{% message_extras :key cardscode :value {{code}} %}
```
{% endraw %}

{% endif %}