---
nav_title: Solução de problemas
article_title: Solução de problemas para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "Este artigo de referência aborda tópicos de solução de problemas para a plataforma Unity."

---

# Solução de problemas

> Este artigo fornece vários cenários de solução de problemas do Unity.

## Erros "O arquivo não pôde ser lido"

Os erros semelhantes aos seguintes podem ser ignorados com segurança. O software da Apple usa uma extensão PNG proprietária chamada CgBI, que a Unity não reconhece. Esses erros não afetarão sua compilação do iOS nem a exibição adequada das imagens associadas no pacote Braze.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
