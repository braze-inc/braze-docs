---
nav_title: "Tipos de notificações por push"
article_title: Tipos de notificações por push
page_order: 1
page_type: glossary
description: "Este glossário lista os diferentes tipos de notificações por push que você pode usar o Braze para enviar."
channel: push

layout: glossary_page
glossary_top_header: "Tipos de notificações por push"
glossary_top_text: "Há muitos tipos de notificações por push que você pode usar para interagir com seus clientes. Elas podem ser reduzidas por canal e usadas para atender às necessidades de muitos usuários diferentes. É possível definir a maioria dessas configurações em suas campanhas push, mas há notas nas descrições a seguir que indicarão se são necessárias configurações de back-end e quais são elas."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: Web
  - name: Android
  - name: iOS

glossaries:
  - name: "Push regular"
    description: "A mensagem Push abrangente. Elas aparecem no dispositivo do usuário com um som de notificação e uma mensagem que desliza ou aparece em uma barra ou pilha de notificações."
    tags:
      - Web
      - Android
      - iOS
  - name: "Push para a web"
    description: "Essas mensagens no navegador são exibidas em Web Apps ou navegadores. Eles ainda precisam de permissão para entrar em contato com o cliente. Note que o web push não funciona se o usuário estiver usando um navegador oculto."
    tags:
      - Web
  - name: "Campanhas Push Primer"
    description: "Campanhas de mensagens no app usadas para obter sinais explícitos de aceitação ou não dos usuários. Por meio do primer, é possível evitar o envio de notificações para usuários que provavelmente desativarão o push nas configurações do dispositivo. Para o iOS, as campanhas push são relevantes, pois as notificações push em primeiro plano (como as notificações que despertam o dispositivo) não são ativadas até que o usuário faça a aceitação explícita do pedido de aceitação do push nativo do iOS."
    tags:
      - Web
      - Android
      - iOS
  - name: "Stories por push"
    description: "As \"Push Stories\" são mensagens imersivas que levam o usuário a uma jornada visual na forma de um carrossel. Elas estão disponíveis apenas para dispositivos móveis."
    tags:
      - iOS
      - Android
  - name: "Botões de ação por push"
    description: "Os botões de ação por push são mensagens que permitem fornecer opções aos seus usuários e oferecer várias chamadas para ação."
    tags:
      - Web
      - Android
      - iOS
  - name: "Notificações por push avançadas"
    description: "As notificações por push Rich são notificações com imagens envolventes e conteúdo criativo que podem ir além de um simples ícone e texto de chamada para ação."
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
  - name: "Notificações por push em segundo plano ou silenciosas"
    description: "Notificações por push que não são renderizadas no dispositivo. Normalmente usado para enviar pacotes de informações para o app para processos em segundo plano e rastreamento de desinstalação. É necessário um token por push ativado em segundo plano para que um push em segundo plano ou silencioso seja enviado."
    tags:
      - Web
      - Android
      - iOS
  - name: "Notificações por push vestíveis"
    description: "Essas notificações por push permitem que as marcas enviem mensagens diretamente para dispositivos vestíveis, como o Apple Watch."
    tags:
      - iOS

---
