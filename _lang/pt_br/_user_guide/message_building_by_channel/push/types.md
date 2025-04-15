---
nav_title: "Tipos de notificações por push"
article_title: Tipos de notificações por push
page_order: 1
page_type: glossary
description: "Este glossário lista os diferentes tipos de notificações por push que você pode usar o Braze para enviar."
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
  - name: "Push regular"
    description: "A mensagem Push abrangente. Elas aparecem no dispositivo do usuário com um som de notificação e uma mensagem que desliza ou aparece em uma barra ou pilha de notificações."
    tags:
      - iOS
      - Android
      - Web
  - name: "Push para a web"
    description: "Essas mensagens no navegador são exibidas em Web Apps ou navegadores. Eles ainda precisam de permissão para entrar em contato com o cliente. Note que o web push não funciona se o usuário estiver usando um navegador oculto."
    tags:
      - Web
  - name: "Campanhas Push Primer"
    description: "Campanhas de mensagens no app usadas para obter sinais explícitos de aceitação ou não dos usuários. Por meio do primer, é possível evitar o envio de notificações para usuários que provavelmente desativarão o push nas configurações do dispositivo. Para o iOS, as campanhas push são relevantes, pois as notificações push em primeiro plano (como as notificações que despertam o dispositivo) não são ativadas até que o usuário faça a aceitação explícita do pedido de aceitação do push nativo do iOS."
    tags:
      - iOS
      - Android
      - Web
  - name: "Stories por push"
    description: "As \"Push Stories\" são mensagens imersivas que levam o usuário a uma jornada visual na forma de um carrossel. Elas estão disponíveis apenas para dispositivos móveis."
    tags:
      - iOS
      - Android
  - name: "Botões de ação por push"
    description: "Os botões de ação por push são mensagens que permitem fornecer opções aos seus usuários e oferecer várias chamadas para ação."
    tags:
      - iOS
      - Android
      - Web
  - name: "Notificações por push avançadas"
    description: "As notificações por push Rich são notificações com imagens envolventes e conteúdo criativo que podem ir além de um simples ícone e texto de chamada para ação."
    tags:
      - iOS
      - Android
  - name: "Notificações por push silenciosas"
    description: "Uma notificação por push que não acorda o dispositivo ao ser renderizada no dispositivo. Em vez disso, a notificação será armazenada na bandeja de notificações do dispositivo."
    tags:
      - iOS
      - Android
  - name: "Notificações por push provisórias para iOS"
    description: "Introduzida pela Apple no iOS 12, a autorização provisória ocorre automaticamente na instalação de apps para iOS, permitindo que as marcas enviem notificações silenciosas sem exibir um prompt por push aos usuários. Quando o push silencioso for enviado e visualizado na bandeja de notificações do dispositivo, os usuários terão a opção de permitir ou descontinuar as notificações por push."
    tags:
      - iOS
  - name: "Notificações por push em HTML"
    description: "As notificações por push em HTML são mensagens por push codificadas em HTML e não usam os modelos por push predefinidos que a Braze fornece. Ter a opção de criar notificações por push em HTML permite que sua empresa tenha total liberdade criativa e uma marca consistente quando se trata da aparência dessas mensagens push."
    tags:
      - Android
  - name: "IDs de notificação e IDs de canal"
    description: "As IDs de notificação e as IDs de canal permitem substituir ou atualizar as notificações por push já recebidas, mas não abertas, pelo usuário."
    tags:
      - iOS
      - Android
  - name: "Notificações por push em segundo plano"
    description: "Notificações por push que não são renderizadas para o dispositivo. Normalmente usado para enviar pacotes de informações para o app para processos em segundo plano e rastreamento de desinstalação. É necessário um token por push ativado em segundo plano para que o push em segundo plano seja enviado."
    tags:
      - iOS
      - Android
      - Web
  - name: "Notificações por push vestíveis"
    description: "Essas notificações por push permitem que as marcas enviem mensagens diretamente para dispositivos vestíveis, como o Apple Watch."
    tags:
      - iOS

---
