---
nav_title: Monitoramento de localização
article_title: Monitoramento de localização para Windows Universal
platform: Windows Universal
page_order: 6
description: "Este artigo de referência aborda como adicionar o monitoramento de localização ao seu app da Plataforma Universal do Windows."
tool: Location
hidden: true
---

# monitoramento de localização
{% multi_lang_include archive/windows_deprecation.md %}

1. Verifique se, em seu arquivo `Package.appxmanifest`, a opção `location` está marcada.
2. Se quiser desativar o monitoramento automático de localização, defina `<DisableLocationCollection>false</DisableLocationCollection>` como `true` em seu `AppboyConfiguration.xml`.
