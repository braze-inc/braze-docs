---
nav_title: Judo
article_title: Judo
description: "Este artigo de referência descreve a parceria entre o Braze e o Judo, uma plataforma de interface do usuário sem código e orientada para o servidor que permite adicionar contexto e monitoramento de localização aos seus apps para iOS e Android."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [O Judo](https://judo.app) é uma plataforma de interface do usuário orientada por servidor que permite que os editores forneçam com eficiência experiências ricas e envolventes para o usuário no app, sem atualizações do app.

_Essa integração é mantida pelo Judo._

## Sobre a integração

A integração da Braze e da Judo proporciona experiências personalizadas em suas campanhas e canvas. Em vez de uma experiência de landing page simples e modelada, uma campanha do Braze pode incorporar conteúdo que inclua várias telas, modais, vídeo, fontes personalizadas e configurações de suporte, como modo escuro e acessibilidade, criadas sem código e implantadas sem atualizações de app. Os dados do Braze também podem ser usados para oferecer suporte a conteúdo personalizado em uma experiência do Judo. Eventos do usuário e dados da experiência podem ser retroalimentados na Braze para atribuição e direcionamento.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta de judô | É necessário ter uma conta [Judo](https://www.judo.app/) para aproveitar essa parceria. |
| SDK de judô | O SDK da Judo deve ser integrado aos seus apps [para iOS](https://github.com/judoapp/judo-ios/) e/ou [Android](https://github.com/judoapp/judo-android). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

**Integração**: Os editores de aplicativos que usam o Judo criam e implementam experiências de integração ricas e nativas. Essas experiências agora podem ser um elemento em uma jornada de integração personalizada entre canais, coordenada pelo Braze. As experiências podem ser personalizadas e atualizadas rapidamente sem nenhuma atualização do app para testar a eficácia de diferentes fluxos no app.

**Conversão**: Os editores de aplicativos podem usar os dados do Braze para criar uma experiência rica e personalizada no app para impulsionar compras no app, inscrições pagas ou merchandising contextual usando ganchos de integração no Judo. O acesso a essas experiências pode ser disparado por meio de campanhas de marketing de engajamento criadas no Braze.

**Conteúdo orientado por eventos**: Um dos principais usos do Judo em esportes e entretenimento é a criação de experiências ricas para prévia, promoção e recapitulação de eventos. Esse recurso tem amplas aplicações em outros verticais de conteúdo sazonal e voltado para notícias. O envio de mensagens para promover ou destacar eventos em tempo hábil para experiências ricas no app capacita os editores a impulsionar o engajamento com interações relevantes.

## Integração lado a lado de SDK

O Judo oferece bibliotecas adicionais que automatizam parte do esforço necessário para integrar os SDKs do Judo e do Braze lado a lado em seus aplicativos móveis. 

### Etapa 1: Instale a biblioteca de integração do Judo-Braze

Instale e configure a biblioteca de integração do Judo Braze em seus apps. Isso ativará automaticamente o rastreamento de eventos.

- [Instalação do iOS
instruções](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Instalação do Android
Instruções](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Etapa 2: configure o envio de mensagens no app

Essa etapa envolverá a criação de implementações personalizadas de `ABKInAppMessageControllerDelegate` e `IInAppMessageManagerListener` para iOS e Android.

Consulte a documentação de configuração de mensagens no app incluída em cada uma das bibliotecas de integração:

- [Envio de mensagens no app do iOS
Configuração](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Envio de mensagens no app do Android
](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Usando esta integração

Depois de concluir a integração lado a lado do app, você pode testá-la executando uma campanha de mensagens no app do Braze para uma experiência no Judo para verificar se ela funciona conforme o esperado.

### Etapa 1: Crie uma campanha de mensagens no app com código personalizado

Na plataforma Braze, crie uma campanha de mensagens no app com um tipo de mensagem de **código personalizado**. Em seguida, selecione **Upload de HTML** como o tipo personalizado. Certifique-se de preencher o conteúdo da mensagem com os campos básicos de envio de mensagens no app; esse conteúdo não será mostrado ao usuário.

![Uma imagem da aparência do dashboard ao selecionar o tipo de mensagem "Custom Code" (Código personalizado).]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

Em seguida, use o seguinte snippet de HTML mínimo para satisfazer a validação do formulário: 
```
<a href="appboy://close">X</a>
```

Note que isso não será exibido em produção em seu dispositivo, pois a Judo reescreverá e substituirá o snippet com uma Judo Experience.

![Uma imagem mostrando o código de validação de formulário adicionado à etapa de criação de sua campanha.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### Etapa 2: Defina um par de valores-chave para o Judo
![Esta imagem mostra o par chave-valor necessário para essa integração, com a "chave" sendo "judo-experience" e o "valor" sendo o seu link do Judo.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Defina um [par chave-valor personalizado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) na campanha com uma chave de `judo-experience`. Forneça o URL da experiência de judô que gostaria de mostrar aqui. A biblioteca de integração do Braze detectará esse par chave-valor no manipulador e o usará para injetar sua experiência do Judo no lugar da interface de usuário padrão de mensagens no app do Braze.
<br><br>
### Etapa 3: Finalização da campanha

Por fim, conclua a campanha, configurando um disparo para a campanha e selecionando usuários por meio de Segmentos nas seções **Entrega** e **Usuário-alvo**. Acesse nosso [artigo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) sobre mensagens no app para conhecer os diferentes componentes de uma mensagem no app do Braze.


