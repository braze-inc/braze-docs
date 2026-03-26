---
nav_title: FAQ
article_title: FAQ sur la bibliothèque multimédia
page_order: 5
page_type: FAQ
tool: Media
description: "Cet article apporte des réponses aux questions fréquemment posées sur la bibliothèque multimédia de Braze."

---

# Foire aux questions

> Cette page fournit des réponses aux questions fréquemment posées sur la bibliothèque multimédia de Braze.

### Existe-t-il des limites de stockage pour les images dans la bibliothèque multimédia ?

Non, il n'y a pas de limite de stockage pour les ressources de la bibliothèque multimédia. Toutefois, la taille des ressources est limitée (5 Mo maximum).

### Les ressources téléchargées ont-elles une date d'expiration ?

Non, les ressources téléchargées dans la bibliothèque multimédia sont conservées pendant toute la durée de votre contrat avec Braze.

### Puis-je télécharger des ressources vidéo ?

Non, la bibliothèque multimédia ne prend pas en charge les fichiers vidéo. Nous vous recommandons de les héberger en externe ou sur une plateforme telle que YouTube.

### Puis-je recadrer tous les types d'images ?

Non, la bibliothèque multimédia ne permet pas de recadrer les images GIF.

### Comment recadrer une image existante ?

Vous pouvez recadrer une image existante en la sélectionnant dans la bibliothèque multimédia et en cliquant sur **Crop & Save New Image**. 

![Aperçu de l'image de la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_crop1.png %}){: height="75%" width="75%"}

Vous serez ensuite redirigé vers un outil de recadrage où vous pourrez sélectionner votre type de proportions et modifier le nom de la nouvelle image. Lorsque vous cliquez sur **Save**, votre nouvelle image est prête à être utilisée.

![Fenêtre permettant de recadrer et d'enregistrer l'image de la bibliothèque multimédia.]({% image_buster /assets/img_archive/media_library_crop2.png %}){: height="75%" width="75%"}

### Le délai d'attente expire lorsque j'essaie de télécharger mon image. Que puis-je faire ?

Cela peut se produire pour diverses raisons. Une solution courante consiste à optimiser votre image avant de tenter de la télécharger, en la passant dans un optimiseur d'image tel qu'[ImageOptim](https://imageoptim.com/mac).

Par ailleurs, si votre image a été créée dans Photoshop (ou un logiciel similaire) et qu'elle comporte de nombreux calques, fusionner et réduire le nombre de calques peut également aider.

### Je vois une « Erreur inattendue » lors du téléchargement d'une image alors qu'elle fait moins de 5 Mo et qu'elle est dans un format pris en charge. Quel est le problème ?

Cela peut se produire pour deux raisons principales :

1. **Métadonnées invalides dans le fichier :** Le logiciel utilisé par Braze pour traiter les images peut rejeter les fichiers dont les métadonnées sont invalides ou incompatibles. Dans certains cas, le traitement du fichier peut aussi faire dépasser la limite de 5 Mo. Essayez d'utiliser une image différente (par exemple, réexportez ou réenregistrez l'image depuis votre éditeur d'images) ou une image provenant d'une autre source.
2. **Caractères spéciaux dans le nom du fichier :** Les noms de fichiers contenant des caractères spéciaux (tels que `&` ou `%`) peuvent provoquer l'échec du téléchargement. Renommez le fichier en utilisant uniquement des lettres, des chiffres, des tirets ou des underscores, puis réessayez.

### Comment se fait-il que je ne puisse pas télécharger n'importe quelle image dans les éditeurs de notifications push ?

La plupart des éditeurs imposent des restrictions sur les proportions d'image autorisées.