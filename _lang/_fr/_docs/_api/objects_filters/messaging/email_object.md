---
nav_title: "Objet Email"
article_title: Objet de messagerie électronique
page_order: 5
page_type: Référence
channel: Email
description: "Cet article explique les différents composants de Braze Email Object."
---

# Spécification de l'objet e-mail

```json
{
  "app_id": (requis, chaîne) voir App Identifier ci-dessus,
  "subject": (optionnel, chaîne),
  "from": (requis, adresse email valide au format "Nom affiché <email@address.com>"),
  "reply_to": (facultatif, adresse e-mail valide au format "email@adresse. om" - par défaut à la réponse par défaut de votre groupe d'applications si elle n'est pas définie) - utilisez "NO_REPLY_TO" pour définir l'adresse de réponse à null,
  "bcc": (optionnel, une des adresses BCC définies dans les paramètres e-mail de votre groupe d'applications) Si fourni et la fonctionnalité BCC est activée pour votre compte, cette adresse sera ajoutée à votre message sortant en tant qu'adresse BCC.
  "body": (requis sauf si email_template_id est donné, HTML valide),
  "plaintext_body": (optionnel, plaintext valide, par défaut pour générer automatiquement le texte en clair à partir de "body" lorsque ce n'est pas défini),
  "preheader": (optionnel*, chaîne) Longueur recommandée de 50-100 caractères.
  "email_template_id": (optionnel, chaîne) Si fourni, nous utiliserons les valeurs objet/body/should_inline_css du modèle d'email donné UNIQUEMENT elles sont spécifiées ici, auquel cas nous remplacerons le modèle fourni,
  "message_variation_id": (optionnel, string) utilisée lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi,
  "extras": (optionnel, valeur de la clé hachée), hash supplémentaire - pour les clients de SendGrid, ceci sera passé à SendGrid en tant qu'Arguments Uniques,
  "en-têtes": (optionnel, hachage Key-Value valide), hachage des en-têtes d'extensions personnalisées. Actuellement, uniquement pris en charge par les clients de SendGrid,
  "should_inline_css": (optionnel, booléen), si vous voulez insérer du CSS sur le corps. Si non fourni, retourne à la valeur CSS par défaut pour le groupe d'applications,
  "pièces jointes": (optionnel, tableau), table d'objets JSON qui définissent les fichiers dont vous avez besoin, défini par "file_name" et "url" ci-dessous,
    "file_name": (requis, ) le nom du fichier que vous souhaitez joindre à votre email. Vous pouvez joindre n'importe quel nombre de fichiers jusqu'à 2 Mo. Ceci est requis si vous utilisez "pièces jointes",
    "url": (obligatoire, chaîne) l'URL correspondante du fichier que vous souhaitez joindre à votre email. L'extension du nom du fichier sera automatiquement détectée à partir de l'URL définie ci-dessous, qui devrait retourner le "Content-Type" approprié en tant qu'en-tête de réponse. Ceci est requis si vous utilisez des « pièces jointes ».
}
```

Pour plus d'informations et de meilleures pratiques sur les pré-en-têtes, voir [notre article d'aide sur le style du corps de l'e-mail][46].

Un `email_template_id` peut être récupéré à partir du bas de n'importe quel modèle d'e-mail créé avec l'éditeur HTML. Voici un exemple de ce à quoi ressemble cet ID:

!\[Section de l'identifiant de l'API d'un modèle d'e-mail HTML\]\[31\]
[31]: {% image_buster /assets/img_archive/email_template_id.png %}

[46]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
