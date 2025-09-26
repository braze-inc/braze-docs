---
nav_title: Perfis de cores e modelos CSS
article_title: Perfis de cores e modelos CSS para mensagens no app
page_order: 4
page_type: reference
description: "Este artigo fornece uma visão geral dos perfis de cores de mensagens no app e dos modelos CSS."
channel:
  - in-app messages
---

# Perfis de cores e modelos CSS {#reusable-color-profiles}

> Você pode salvar modelos de mensagens no app e no navegador no dashboard para criar rapidamente novas campanhas e mensagens usando seu estilo. 

Acesse **Modelos** > **Modelos de mensagens no app**.

Nessa página, você pode editar modelos existentes ou clicar em **\+ Criar** e escolher **Perfil de cor** ou **Modelo CSS** para criar novos modelos a serem usados em suas mensagens no app.

## Perfil de cores

Você pode personalizar o esquema de cores do modelo de mensagem inserindo um código de cor HEX ou clicando na caixa colorida e selecionando uma cor com o seletor de cores.

Clique em **Save Color Profile (Salvar perfil de cor** ) quando terminar.

### Gerenciamento de perfis de cores

Você também pode [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) e [arquivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modelos! Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos e mídias.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)

## Modelo CSS {#in-app-message-templates}

Você pode personalizar um modelo CSS completo para sua [mensagem no app modal da Internet](#web-modal-css).

Dê um nome e uma tag para seu modelo CSS e, em seguida, escolha se ele será ou não seu modelo padrão. Você pode escrever seu próprio CSS no espaço fornecido. Esse espaço já está pré-preenchido com o CSS mostrado na prévia da mensagem, e você deve se sentir à vontade para ajustá-lo ligeiramente para atender às suas necessidades.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Como você pode ver, é possível editar tudo, desde a cor do plano de fundo até o tamanho e o peso da fonte, e muito mais.

### Gerenciamento de modelos CSS

Você também pode [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) e [arquivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modelos! Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos e mídias.]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)

## Modal com CSS (somente na Web) {#web-modal-css}

Se optar por usar um Web Modal somente para a internet com mensagem CSS, você poderá aplicar seu próprio modelo ou escrever seu próprio CSS no espaço fornecido. Esse espaço já está pré-preenchido com o CSS mostrado na prévia de sua mensagem, mas fique à vontade para ajustá-lo ligeiramente para atender às suas necessidades.

Se você optar por aplicar seu próprio modelo, clique em **Aplicar modelo** e escolha na galeria de modelos de mensagens no app. Se não tiver nenhuma opção, você pode fazer upload de um [modelo CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css/#in-app-message-templates) usando o construtor de modelos CSS.


