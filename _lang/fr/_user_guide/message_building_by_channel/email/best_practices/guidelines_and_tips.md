---
nav_title: Recommandations pour les e-mails
article_title: Recommandations pour les e-mails
page_order: 1
page_type: reference
description: "Le présent article couvre les conseils généraux et les astuces à garder en tête lorsque vous créez des campagnes par e-mail pour différents cas d’utilisation et différents sujets."
channel: E-mail

---

# Recommandations pour les e-mails

> Le présent article couvre les conseils généraux et les astuces à garder en tête lorsque vous créez des campagnes par e-mail  pour différents cas d’utilisation et différents sujets.

## Généralités

Lorsque vous créez votre campagne par e-mail, il est important de garder à l’esprit comment vos messages vont être reçus par vos divers utilisateurs et par les ESP (fournisseurs de services d'e-mail). Voici quelques conseils rapides à garder à l’esprit en construisant votre contenu :

- Lors du formatage de votre e-mail, utilisez les feuilles de style inline en tant que CSS.
- Pour utiliser un modèle d’e-mail sur mobile et PC en même temps, spécifiez une largeur inférieure à 500 pixels.
- Les images téléchargées sur le modèle d’e-mail doivent faire moins de 5 Mo. Les formats pris en charge incluent PNG, JPG et GIF.
- Ne définissez pas de hauteurs et de largeurs pour les images, car cela générera un espace blanc inutile dans un e-mail dégradé.
- `div` tags ne doivent pas être utilisées car la plupart des clients par e-mail ne les prennent pas en charge. Utilisez plutôt des tables imbriquées.
- Évitez d’utiliser Javascript parce qu’il ne fonctionne avec aucun fournisseur de services de courrier électronique.
- Braze améliore les temps de chargement en utilisant un CDN global pour héberger toutes les images des e-mails.

### Utiliser du texte alternatif

Comme les filtres anti-spam surveillent à la fois la version HTML et la version texte brut d’un message, l’utilisation d’alternatives en texte brut est un excellent moyen de réduire votre score de spam. De plus, le texte alternatif `(alt="")` peut compléter, voire remplacer les images incluses dans le corps de votre e-mail, qui peuvent avoir été filtrées et supprimées par le fournisseur d’e-mail d’un utilisateur. Les lecteurs d’écran dévoilent le texte alternatif pour expliquer les images. C’est donc l’occasion d’utiliser un langage simple pour fournir des informations clés sur une image.

### Validation de le-mail

Braze ajuste automatiquement les adresses e-mail insérées et va tronquer les éventuels espaces blancs. Les adresses e-mail ciblées via les serveurs Braze doivent être conformes aux normes [RFC 2822][24]. En plus de ces normes, Braze n’accepte pas les caractères suivants et les considère comme non valides. Si un e-mail est renvoyé, Braze marque l’adresse e-mail comme non valide et le statut d’abonnement n’est pas modifié.

{% details Unaccepted characters outside of RFC standards %}
- *
- /
- ?
- !
- $
- #
- %
- &#94;
- &
- (
- )
- {
- }
- [
- ]
- ~
- ,
{% enddetails %}

### Définir les adresses « De » et « Répondre à »

Lorsque vous définissez vos adresses d’expéditeur, assurez-vous que votre domaine d’e-mail «  De » correspond à votre domaine d’envoi (c.-à-d., `marketing.yourdomain.com`). Le non-respect de cette consigne peut entraîner un mauvais alignement SPF et DKIM. Tous les e-mails Reply-to peuvent être définies sur votre domaine racine.

### Vérification des détails HTML

N’oubliez pas que certains tags et attributs HTML ne sont pas autorisés car ils peuvent potentiellement permettre d’exécuter du code malveillant dans le navigateur.

Consultez les listes suivantes pour voir les tags et les attributs HTML qui ne sont pas autorisés dans vos e-mails :
{% details Expand for disallowed HTML tags %}
- `<!doctype>`
- `<applet>`
- `<bgsound>`
- `<embed>`
- `<frameset>`
- `<iframe>`
- `<ilayer>`
- `<layer>`
- `<link>`
- `<meta>`
- `<object>`
- `<script>`
- `<title>`
- `<xml>`
- `<svg>`
{% enddetails %}

{% details Expand for disallowed HTML attributes %}
- `<animationend>`
- `<animationiteration>`
- `<animationstart>`
- `<data-bind>`
- `<fscommand>`
- `<onabort>`
- `<onabort>`
- `<onactivate>`
- `<onafterprint>`
- `<onafterupdate>`
- `<onbeforeactivate>`
- `<onbeforecopy>`
- `<onbeforecut>`
- `<onbeforedeactivate>`
- `<onbeforeeditfocus>`
- `<onbeforepaste>`
- `<onbeforeprint>`
- `<onbeforeunload>`
- `<onbeforeupdate>`
- `<onbegin>`
- `<onblur>`
- `<onbounce>`
- `<oncanplay>`
- `<oncanplaythrough>`
- `<oncellchange>`
- `<onchange>`
- `<onclick>`
- `<oncontextmenu>`
- `<oncontrolselect>`
- `<oncopy>`
- `<oncut>`
- `<ondataavailable>`
- `<ondatasetchanged>`
- `<ondatasetcomplete>`
- `<ondblclick>`
- `<ondeactivate>`
- `<ondrag>`
- `<ondragdrop>`
- `<ondragend>`
- `<ondragenter>`
- `<ondragleave>`
- `<ondragover>`
- `<ondragstart>`
- `<ondrop>`
- `<ondurationchange>`
- `<onemptied>`
- `<onend>`
- `<onended>`
- `<onerror>`
- `<onerror>`
- `<onerrorupdate>`
- `<onfilterchange>`
- `<onfinish>`
- `<onfocus>`
- `<onfocusin>`
- `<onfocusout>`
- `<onhashchange>`
- `<onhelp>`
- `<oninput>`
- `<oninvalid>`
- `<onkeydown>`
- `<onkeypress>`
- `<onkeyup>`
- `<onlayoutcomplete>`
- `<onload>`
- `<onloadeddata>`
- `<onloadedmetadata>`
- `<onloadstart>`
- `<onlosecapture>`
- `<onmediacomplete>`
- `<onmediaerror>`
- `<onmessage>`
- `<onmousedown>`
- `<onmouseenter>`
- `<onmouseleave>`
- `<onmousemove>`
- `<onmouseout>`
- `<onmouseover>`
- `<onmouseup>`
- `<onmousewheel>`
- `<onmove>`
- `<onmoveend>`
- `<onmovestart>`
- `<onoffline>`
- `<ononline>`
- `<onopen>`
- `<onoutofsync>`
- `<onpagehide>`
- `<onpageshow>`
- `<onpaste>`
- `<onpause>`
- `<onplay>`
- `<onplaying>`
- `<onpopstate>`
- `<onprogress>`
- `<onpropertychange>`
- `<onratechange>`
- `<onreadystatechange>`
- `<onredo>`
- `<onrepeat>`
- `<onreset>`
- `<onresize>`
- `<onresizeend>`
- `<onresizestart>`
- `<onresume>`
- `<onreverse>`
- `<onrowdelete>`
- `<onrowexit>`
- `<onrowinserted>`
- `<onrowsenter>`
- `<onscroll>`
- `<onsearch>`
- `<onseek>`
- `<onseeked>`
- `<onseeking>`
- `<onselect>`
- `<onselectionchange>`
- `<onselectstart>`
- `<onshow>`
- `<onstalled>`
- `<onstart>`
- `<onstop>`
- `<onstorage>`
- `<onsubmit>`
- `<onsuspend>`
- `<onsyncrestored>`
- `<ontimeerror>`
- `<ontimeupdate>`
- `<ontoggle>`
- `<ontouchcancel>`
- `<ontouchend>`
- `<ontouchmove>`
- `<ontouchstart>`
- `<ontrackchange>`
- `<onundo>`
- `<onunload>`
- `<onurlflip>`
- `<onvolumechange>`
- `<onwaiting>`
- `<onwheel>`
- `<seeksegmenttime>`
- `<transitionend>`
{% enddetails %}


[24]: http://tools.ietf.org/html/rfc2822

