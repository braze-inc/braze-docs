---
nav_title: Accessibilité
article_title: Accessibilité
platform: Web
page_order: 22
page_type: reference
description: "Cet article décrit comment Braze prend en charge l'accessibilité."

---

# Accessibilité

> Cet article donne un aperçu de la manière dont Braze prend en charge l'accessibilité au sein de votre intégration.

Le Braze Web SDK prend en charge les normes fournies par les [directives d'accessibilité au contenu Web (WCAG 2.1).](https://www.w3.org/TR/WCAG21/) Nous maintenons un [score phare de 100/100](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) pour les cartes de contenu et les messages in-app sur tous nos nouveaux projets afin de respecter notre norme d'accessibilité.

## Conditions préalables

La version minimale du SDK qui satisfait aux WCAG 2.1 est proche de la v3.4.0. Toutefois, nous vous recommandons de passer au moins à la version 6.0.0 pour bénéficier des principales corrections apportées aux étiquettes d'images.

### Corrections notables en matière d'accessibilité

| Version | Type | Principaux changements |
|---------|------|-------------|
| **6.0.0** | **Principale** | Images en tant qu'étiquettes `<img>`, champs `imageAltText` ou `language`, améliorations générales de l'accessibilité de l'interface utilisateur |
| **3.5.0** | Mineur | Amélioration de l'accessibilité du texte défilant |
| **3.4.0** | Correctif | Cartes de contenu `article` Correction du rôle |
| **3.2.0** | Mineur | Cibles de ciblage minimales de 45x45px pour les boutons |
| **3.1.2** | Mineur | Texte alt par défaut pour les images |
| **2.4.1** | **Principale** | HTML sémantique (`h1` ou `button`), attributs ARIA, navigation au clavier, gestion du focus |
| **2.0.5** | Mineur | Gestion du focus, navigation au clavier, étiquettes |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Fonctionnalités d'accessibilité prises en charge

Nous prenons en charge ces fonctionnalités pour les cartes de contenu et les messages in-app :

- Rôles et labels ARIA
- Prise en charge de la navigation au clavier
- Gestion de l'attention
- Annonces concernant les lecteurs d'écran
- Prise en charge du texte Alt pour les images

## Lignes directrices en matière d'accessibilité pour les intégrations SDK

Reportez-vous à la section [Créer des messages accessibles dans Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) pour connaître les directives générales en matière d'accessibilité. Ce guide fournit des conseils et des bonnes pratiques pour une accessibilité maximale lors de l'intégration du SDK Braze Web dans votre application web.

### Cartes de contenu

#### Fixer une hauteur maximale

Pour éviter que les cartes de contenu n'occupent trop d'espace vertical et améliorer l'accessibilité, vous pouvez fixer une hauteur maximale au conteneur de flux, comme dans cet exemple :

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Considérations sur la fenêtre de visualisation

Pour les cartes de contenu affichées en ligne, tenez compte des contraintes de visualisation, comme dans cet exemple.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### in-app Messages

{% alert warning %}
Ne mettez pas d'informations importantes dans les messages in-app, car ils ne sont pas accessibles aux lecteurs d'écran.
{% endalert %}

### Considérations sur le mobile

#### Conception adaptée

Le SDK comprend des points d'arrêt réactifs. Confirmez que vos personnalisations fonctionnent sur toutes les tailles d'écran, comme dans cet exemple :

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }
  
  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Test d'accessibilité

#### Liste de contrôle des tests manuels

Testez manuellement votre accessibilité en effectuant les tâches suivantes :

- Naviguer dans les cartes de contenu et les messages in-app avec le clavier uniquement (onglet, entrée, espace).
- Test avec un lecteur d'écran (NVDA, JAWS, VoiceOver)
- Vérifiez que toutes les images comportent un texte alt
- Vérifiez les rapports de contraste des couleurs (utilisez des outils tels que WebAIM Contrast Checker).
- Test sur des appareils mobiles tactiles
- Vérifier que les indicateurs de focalisation sont visibles
- Test de l'envoi de messages modaux en mode dialogue, etc.
- Vérifiez que tous les éléments interactifs sont accessibles au moyen d'un clavier.

### Problèmes courants d'accessibilité

Pour éviter les problèmes d'accessibilité les plus courants, procédez comme suit :

1. **Gardez le cap sur les styles :** Les indicateurs de mise au point du SDK sont essentiels pour les utilisateurs de clavier.
2. **N'utilisez `display: none` que pour les éléments non interactifs :** Utilisez `visibility: hidden` ou `opacity: 0` pour masquer les éléments interactifs.
3. **Ne remplacez pas les attributs ARIA :** Le SDK définit les rôles et les étiquettes ARIA appropriés.
4. **Utilisez les attributs `tabindex`:** Ils contrôlent l'ordre de navigation du clavier.
5. **Fournissez un défilement si vous définissez `overflow: hidden`:** Confirmez que le contenu défilant reste accessible.
6. **N'interférez pas avec les gestionnaires de clavier intégrés :** Confirmez que la navigation au clavier existante fonctionne.