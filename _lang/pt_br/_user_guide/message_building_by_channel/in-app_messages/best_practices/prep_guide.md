---
nav_title: Guia de preparação
article_title: Guia de preparação de mensagens no aplicativo
page_order: 0.5

page_type: reference
description: "Este artigo aborda algumas perguntas e práticas recomendadas que você deve considerar antes de criar suas mensagens in-app."
channel: in-app messages

---

# Guia de preparação de mensagens no aplicativo

> Antes de criar suas mensagens in-app, você deve considerar alguns dos tópicos a seguir para que a criação da mensagem seja rápida e fácil.

## Considerações gerais

- Se estiver criando uma campanha, quantas variantes dessa mensagem você gostaria de exibir? Para obter ideias de testes de variantes, consulte [Dicas para diferentes canais]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels).
- Se você estiver criando um Canvas, essa mensagem será combinada com outros canais de mensagens nessa etapa?
- Quando você gostaria que [sua mensagem expirasse]({{site.baseurl}}/canvas_in-app_messages/)?

## Considerações sobre o direcionamento

- As mensagens no aplicativo são melhores para os usuários que visitam seu aplicativo regularmente. Você está incluindo esse público?
- Onde você quer que seus usuários vejam sua mensagem? Em seu aplicativo da Web? Em seu aplicativo móvel?
- Qual evento deve acionar essa mensagem?
- Algum dos seus usuários está usando versões mais antigas do seu aplicativo? Se for o caso, talvez eles não consigam ver alguns elementos de sua mensagem.
- Para que tipo de dispositivo ou dispositivos você está criando essa mensagem? Lembre-se de que você pode visualizar sua mensagem usando a caixa **Preview (Visualização** ) ou a guia **Test (Teste** ). Consulte [Testes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) para obter mais informações.

## Considerações sobre o conteúdo

- Quais idiomas você usará nessa mensagem?
- Qual é o texto do cabeçalho e do corpo da página? Eles são atraentes e relevantes para o seu usuário?
- As mensagens no aplicativo são exibidas apenas por um determinado período de tempo. Seu texto é conciso e memorável?
- Você usará o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) para adicionar uma cópia personalizada?
- Para mensagens em tela cheia no aplicativo, sua imagem ou outra mídia está dentro da [zona de segurança]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)?
- Para mensagens in-app de pesquisa, você deseja registrar atributos ou envios? Você configurou sua página de confirmação?

## Considerações sobre a conversão

- Qual é o seu objetivo com essa mensagem? Como você pode representar isso em sua mensagem?
- Seus botões oferecem opções que fazem sentido para o usuário? Qual é sua [principal chamada para ação]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- Você está [fazendo deep linking para outros conteúdos no aplicativo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)? Você está usando essa mensagem in-app para enviar e aceitar uma [permissão ou]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) uma [solicitação de push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)?
- Você tem uma opção de saída de mensagem? Caso contrário, você sempre poderá copiar e colar esse trecho para criar um botão rápido:
    ```html
    <a href="appboy://close">X</a>
    ```


