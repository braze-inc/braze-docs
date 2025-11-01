---
nav_title: Suivi des clics
article_title: Suivi des clics
page_order: 3
description: "Cet article de référence explique comment activer le suivi des clics dans vos messages WhatsApp, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Suivi des clics

> Cette page explique comment activer le suivi des clics dans vos messages WhatsApp, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, et plus encore.

Le suivi des clics vous permet de mesurer quand quelqu'un tape sur un lien dans votre message WhatsApp, ce qui vous donne une vision claire du contenu qui suscite l'engagement. Braze raccourcit vos URL, ajoute un suivi en coulisses et enregistre les clics au fur et à mesure qu'ils se produisent.

Vous pouvez activer le suivi des clics dans les messages de réponse et les messages types. Il fonctionne avec des liens dans les boutons et le corps du texte, et prend en charge les URL personnalisées et les domaines personnalisés. Une fois qu'il est activé, vous verrez les données relatives aux clics dans vos rapports de performance WhatsApp et pourrez segmenter les utilisateurs en fonction de qui a cliqué sur quoi.

{% alert note %}
Le suivi des clics ne fonctionne pas avec les liens profonds. Vous pouvez raccourcir les liens universels à partir de fournisseurs tels que Branch ou Appsflyer, mais Braze n'est pas en mesure de résoudre les problèmes qui peuvent survenir lors de cette opération (comme la rupture de l'attribution ou la cause d'une redirection).
{% endalert %}

## Comment cela fonctionne-t-il ?

### Messages d'envoi de messages 

Pour configurer le suivi des clics pour les messages de réponse :
1. Créez un message de réponse comprenant un bouton d'appel à l'action (CTA) avec l'URL d'un site web.
2. Activez le suivi des clics en cliquant sur le bouton prévu à cet effet dans l'interface.

Le lien sera raccourci au domaine Braze, ou au domaine personnalisé spécifié pour le groupe d'abonnement, et personnalisé pour l'utilisateur.

Tous les URL statiques commençant par `http://` ou `https://` seront raccourcis. Les URL raccourcis qui contiennent une personnalisation liquide (comme le ciblage de suivi au niveau de l'utilisateur) seront valables pendant deux mois.

Composez un message WhatsApp avec un corps de contenu et un bouton.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Messages types 

Pour les messages des modèles, l'URL de base doit être soumise correctement lors de la création du modèle pour activer le suivi des clics.

#### Étape 1 : Créer un modèle pris en charge par le suivi des clics dans WhatsApp

1. Dans votre gestionnaire WhatsApp, créez une URL de base qui est soit votre domaine personnalisé, soit `brz.ai`.
2. Assurez-vous que les liens inclus dans le modèle sont compatibles avec le suivi des clics.
3. Ne modifiez pas les variables du modèle une fois qu'il a été implémenté en tant que campagne dans Braze ; les modifications en aval ne peuvent pas être intégrées.
4. Pour les liens des boutons CTA, sélectionnez **Dynamique**, puis indiquez l'URL de base (`brz.ai` ou votre domaine personnalisé).<br><br>\![Section pour créer un appel à l'action.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. Pour les liens dans le corps du texte, lorsque vous rédigez le modèle dans votre gestionnaire WhatsApp, supprimez les espaces insérés pour les liens contenus dans le corps que vous souhaitez suivre.<br><br>\![Zone de texte pour saisir le corps du contenu de l'appel à l'action.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### Étape 2 : Complétez votre modèle dans Braze

Lors de la composition, Braze détectera automatiquement les modèles dont les domaines URL sont compatibles, tant dans le corps du texte que pour les boutons CTA. L'état est indiqué au bas du modèle. 

\!["Statut du lien" indiquant un statut actif pour le suivi des clics.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Liens pris en charge :** Le suivi des clics sera activé pour les liens soumis avec l'URL de base correspondante.
- **Liens partiellement soutenus :** Si certains liens d'un modèle sont soumis en tant qu'URL complètes, le suivi des clics **ne sera pas** appliqué à ces liens.
- **Liens non soutenus :** Les liens qui n'ont pas d'URL de base approuvée ne pourront **pas** faire l'objet d'un suivi des clics.

L'URL de destination devra être fournie pour tout lien dont l'URL de base correspond à `brz.ai` ou à votre domaine personnalisé. 

\![ Section "Boutons" avec des champs pour le nom du bouton, l'URL du site web et l'URL de suivi des clics.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## La personnalisation liquide dans les URL

Vous pouvez construire dynamiquement votre URL directement dans le compositeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (comme diriger les utilisateurs vers leur panier abandonné ou vers un produit spécifique qui est de nouveau en stock).
Les URL peuvent être générés dynamiquement par l'utilisation de n'importe quelle étiquette Liquid de personnalisation prise en charge.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Nous sommes également favorables à l'abrègement des variables Liquid personnalisées, comme dans ces exemples :

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Raccourcir les URL rendues par les variables Liquid

Braze raccourcit les URL qui sont rendues par Liquid, même celles qui sont incluses dans les propriétés de déclenchement de l'API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, nous raccourcirons et suivrons cette URL avant d'envoyer le message WhatsApp.

## Essais

Avant de lancer votre campagne ou votre Canvas, la meilleure pratique consiste à prévisualiser et à tester votre message. Pour ce faire, allez dans l'onglet **Test** pour prévisualiser et envoyer un WhatsApp à des groupes de test de contenu ou à un utilisateur individuel.

Cet aperçu sera mis à jour avec la personnalisation pertinente et l'URL raccourcie. 

{% alert important %}
Si un brouillon est créé dans un canvas actif, l'URL raccourcie ne sera pas générée. L'URL raccourci est généré lorsque le projet Canvas est rendu actif.
{% endalert %}

## Rapports

Lorsque le suivi des clics est activé ou utilisé avec des modèles pris en charge, le tableau des performances de WhatsApp comprend la colonne **Nombre total de clics** qui indique un nombre d'événements de clics par variante et un taux de clics associé. Pour plus de détails sur les indicateurs de WhatsApp, reportez-vous à la section [Performances des messages WhatsApp.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics)

!Étape du canvas de l'envoi de messages WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Les données relatives aux clics seront automatiquement reportées dans le tableau de bord analytique.

!Tableau de performance des envois de messages WhatsApp.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Reciblage des utilisateurs 

Vous pouvez utiliser le filtre `Clicked/Opened Step` et l'interaction `clicked tracked WhatsApp link` pour segmenter les utilisateurs en fonction de leurs interactions avec les liens.

\![Groupe de filtrage avec un filtre pour "clicked tracked WhatsApp link".]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ?

Oui. Lorsque le suivi des clics est activé (ou activé en fonction de la configuration du modèle), vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en exploitant les filtres de reciblage WhatsApp ou les événements de clics WhatsApp (`users.messages.whatsapp.Click`) envoyés par Currents.

### Les prévisualisations sur l'appareil WhatsApp comptent-elles comme des clics ? 

Non, ils ne contribuent pas au taux de clics des messages WhatsApp. 

