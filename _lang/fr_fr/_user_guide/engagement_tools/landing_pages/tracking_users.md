---
nav_title: Suivi des utilisateurs
article_title: "Suivi des utilisateurs par le biais d'un formulaire"
description: "Découvrez comment identifier les utilisateurs qui soumettent un formulaire via votre page de destination en ajoutant une étiquette Liquid à vos messages."
page_order: 2
---

# Suivi des utilisateurs par le biais d'un formulaire

> Découvrez comment suivre les utilisateurs qui soumettent un formulaire via votre page d'atterrissage en ajoutant une étiquette Liquid de page d'atterrissage à vos messages. Cette étiquette Liquid est prise en charge sur tous les canaux d'envoi de messages de Braze, y compris les e-mails, les SMS, les messages in-app, et plus encore. Pour en savoir plus sur les données de suivi, voir [À propos des données de suivi des pages d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data).

## Comment cela fonctionne-t-il ?

Vous pouvez ajouter une étiquette Liquid {% raw %}`{% landing_page_url %}`{% endraw %} à n'importe lequel de vos messages à canal unique ou multiple dans Braze. Lorsqu'un utilisateur visite cette page de renvoi et soumet le formulaire, Braze relie automatiquement ces données à son profil existant, au lieu de créer un nouveau profil pour cet utilisateur. Dans l'exemple suivant, une étiquette Liquid de la page d'atterrissage est utilisée pour renvoyer les clients à une enquête :

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
Vous pouvez également utiliser les pages d'atterrissage pour générer des leads en intégrant l'URL de la page dans vos canaux externes. Après avoir créé une page d'atterrissage, allez dans **Détails de la page d'atterrissage** pour obtenir l'URL unique de votre page d'atterrissage.
{% endalert %}

## Utiliser les étiquettes Liquid des pages d'atterrissage

### Conditions préalables

Avant de commencer, vous devrez créer une [page de destination]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) et une [campagne.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)

### Étape 1 : Vérifiez l'URL de la page {#page-url}

Braze utilisera l'URL de votre page de destination pour générer son étiquette Liquid unique. Si vous souhaitez modifier l'URL de la page actuelle, allez dans **Messagerie** > **Pages d'atterrissage**, puis ouvrez votre page d'atterrissage. Sous **URL** de la page, vous pouvez saisir une nouvelle URL de page.

{% alert warning %}
Si vous modifiez l'URL de la page après l'envoi de votre message, tout utilisateur qui tente de visiter votre page d'atterrissage à l'aide de l'ancienne URL sera envoyé sur une page `404`.
{% endalert %}

Un exemple d'URL pour une page d'atterrissage dans Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Étape 2 : Générer l'étiquette Liquid

Allez dans **Messagerie** > **Campagnes**, puis choisissez une campagne. Dans l'éditeur de messages, sélectionnez **Personnalisation**.

Le bouton "Ajouter une personnalisation" de l'éditeur par glisser-déposer.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze génère automatiquement une étiquette Liquid à l'aide de l'[URL de](#page-url) votre [page d'atterrissage](#page-url). Reportez-vous au tableau suivant pour générer votre étiquette :

\|**Type de** personnalisation Choisissez la **page d'atterrissage**.
\|**Choisissez** la page d'atterrissage que [vous avez créée précédemment](#prerequisites).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour ajouter l'étiquette Liquid à votre message, vous pouvez soit sélectionner **Insérer**, soit copier l'extrait de code dans votre presse-papiers et l'ajouter manuellement.

Une étiquette Liquid générée automatiquement pour la page d'atterrissage sélectionnée.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Votre extrait de code sera similaire à ce qui suit :

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### Étape 3 : Finaliser et envoyer votre message

Incorporez l'extrait de code liquid dans votre message, puis finalisez le reste de votre message. Par exemple :

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

Lorsque vous êtes prêt, vous pouvez envoyer le message pour commencer à suivre les utilisateurs via votre page d'atterrissage.
