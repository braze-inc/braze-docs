{% if include.alert == "Shopify deprecation" %}

{% alert important %}
A new version of the Shopify integration will be released in phases starting April, based on the type of Shopify store and the external ID used to set up the initial integration. <br><br>**The older version of the integration will be deprecated on August 28, 2025. You must update to the newer version of the integration before August 28, 2025.**<br><br>**New Braze customers:** Starting April 2025, Braze will be gradually rolling out the new Shopify connector for new onboardings and upgrading existing customers. To learn more about the new standard integration, refer to [Shopify standard integration]({{site.baseurl}}/shopify_standard_integration/).<br><br>**Existing Braze customers:** Starting in February 2025, we will contact you with an upgrade guide to help you transition to the newer Shopify integration.  We will organize customers into groups (cohorts) based on your Shopify store and how you use Braze external IDs to facilitate a smooth and personalized upgrade experience. You will be notified when your cohort is ready to upgrade.<br><br>**Upgrading to this newer version will cause breaking changes.** You will be guided through a review process on the Braze dashboard to help you and your development team address these changes before you upgrade.
{% endalert %}

{% endif %}

{% if include.alert == "Shopify deprecation short" %}

{% alert important %}
A new version of the Shopify integration will be released in phases starting April, based on the type of Shopify store and the external ID used to set up the initial integration. <br><br>**The older version of the integration will be deprecated on August 28, 2025. You must update to the newer version of the integration before August 28, 2025.**<br><br>**New Braze customers:** Starting April 2025, Braze will be gradually rolling out the new Shopify connector for new onboardings and upgrading existing customers. To learn more about the new standard integration, refer to [Shopify standard integration]({{site.baseurl}}/shopify_standard_integration/).<br><br>**Existing Braze customers:** Starting in February 2025, we will contact you with an upgrade guide to help you transition to the newer Shopify integration.
{% endalert %}

{% endif %}