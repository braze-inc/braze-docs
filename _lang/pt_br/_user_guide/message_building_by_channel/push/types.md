---
nav_title: "Tipos de notificações por push"
article_title: Tipos de notificações push
page_order: 1
page_type: glossary
description: "Este glossário lista os diferentes tipos de notificações push que você pode usar o Braze para enviar."
channel: push

layout: glossary_page
glossary_top_header: "Types of push notifications"
glossary_top_text: "There are many types of push notifications you can use to interact with your customers. These can be narrowed by channel and used to meet the needs of many different users. You can configure most of these settings in your Push campaigns, but there are notes in the following descriptions that will indicate whether any backend configurations are needed and what those might be."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: iOS
  - name: Android
  - name: Web

glossaries:
  - name: "Empurrar regularmente"
    description: "A mensagem Push abrangente. Elas aparecem no dispositivo do usuário com um som de notificação e uma mensagem que desliza ou aparece em uma barra ou pilha de notificações."
    tags:
      - iOS
      - Android
      - Web
  - name: "Web Push"
    description: "Essas mensagens push aparecem em aplicativos da Web ou navegadores. Eles ainda precisam de permissão para entrar em contato com o cliente. Observe que o Web Push não funciona se o usuário estiver usando um navegador oculto."
    tags:
      - Web
  - name: "Campanhas Push Primer"
    description: "Campanhas de mensagens no aplicativo usadas para obter um sinal explícito de opt-in ou opt-out dos usuários. Por meio do primer, é possível evitar o envio de notificações para usuários que provavelmente desativarão o push nas configurações do dispositivo. Para o iOS, as campanhas push são relevantes, pois as notificações push em primeiro plano (como as notificações que ativam o dispositivo) não são ativadas até que o usuário opte explicitamente pelo prompt push nativo do iOS."
    tags:
      - iOS
      - Android
      - Web
  - name: "Histórias de empurrar"
    description: "As Push Stories são mensagens imersivas que levam o usuário por uma jornada visual na forma de um carrossel. Eles estão disponíveis apenas para dispositivos móveis."
    tags:
      - iOS
      - Android
  - name: "Pressione com botões de ação"
    description: "Os botões de ação são mensagens que permitem fornecer opções aos usuários e oferecer várias chamadas para ação."
    tags:
      - iOS
      - Android
      - Web
  - name: "Notificações push avançadas"
    description: "As Rich Push Notifications são notificações com imagens envolventes e conteúdo criativo que podem ir além de um simples ícone e texto de chamada para ação."
    tags:
      - iOS
      - Android
  - name: "Notificações push provisórias para iOS"
    description: "Introduzida pela Apple no iOS 12, a autorização provisória ocorre automaticamente na instalação de aplicativos iOS, permitindo que as marcas enviem notificações silenciosas sem exibir um prompt de push para os usuários. Quando o push silencioso for enviado e visualizado na bandeja de notificações do dispositivo, os usuários terão a opção de permitir ou descontinuar as notificações push."
    tags:
      - iOS
  - name: "Notificações push em HTML"
    description: "As notificações HTML Push são mensagens push codificadas em HTML e não usam os modelos push predefinidos fornecidos pelo Braze. Ter a opção de criar notificações push em HTML permite que sua empresa tenha total liberdade criativa e uma marca consistente quando se trata da aparência dessas mensagens push."
    tags:
      - Android
  - name: "IDs de notificação e IDs de canal"
    description: "As IDs de notificação e as IDs de canal permitem substituir ou atualizar as notificações push já recebidas, mas não abertas, pelo usuário."
    tags:
      - iOS
      - Android
  - name: "Notificações push em segundo plano ou silenciosas"
    description: "Notificações por push que não são renderizadas no dispositivo. Normalmente usado para enviar pacotes de informações para o aplicativo para processos em segundo plano e rastreamento de desinstalação. Um token de push habilitado para segundo plano é necessário para que um push em segundo plano ou silencioso seja enviado."
    tags:
      - iOS
      - Android
      - Web
  - name: "Notificações push vestíveis"
    description: "Essas notificações push permitem que as marcas enviem mensagens diretamente para dispositivos vestíveis, como o Apple Watch."
    tags:
      - iOS

---
