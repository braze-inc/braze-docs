---
nav_title: Rastrear sessões
article_title: Rastrear Sessões para Windows Universal
platform: Windows Universal
page_order: 0
description: "Este artigo de referência aborda como rastrear sessões na plataforma Windows Universal."
hidden: true
---

# Análise de dados
{% multi_lang_include archive/windows_deprecation.md %}

## Rastreamento de sessão

O SDK do Braze relata dados de sessão que são usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Com base na semântica de sessão a seguir, nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que contabilizam a duração da sessão e as contagens de sessão visíveis no dashboard do Braze.

### Ciclo de vida da sessão

Nossa sessão de registros de integração do Windows é aberta quando o app é iniciado e a sessão de registros é fechada quando o aplicativo é encerrado. O valor mínimo para `sessionTimeoutInSeconds` é 1 segundo. Se precisar forçar uma nova sessão, poderá fazê-lo mudando de usuário.

### Teste de rastreamento de sessão

Para detectar sessões por meio de seu usuário, localize-o no dashboard e navegue até "App Usage" (Uso do app) no perfil do usuário. Você pode confirmar que o rastreamento de sessão está funcionando verificando se a métrica "Sessões" aumenta quando você espera que isso aconteça.

![Um perfil de usuário mostrando o uso do app como 25 sessões, usado pela última vez há duas horas e usado pela primeira vez há vinte dias]({% image_buster /assets/img_archive/test_session.png %})


