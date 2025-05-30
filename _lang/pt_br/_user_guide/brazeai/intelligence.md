---
nav_title: Intelligence Suite
article_title: Intelligence Suite
page_order: 10
layout: dev_guide
search_rank: 12
guide_top_header: "Intelligence Suite"
guide_top_text: "O Intelligence Suite da Braze ajuda a automatizar a tomada de decisões com insights baseados em dados. Do tempo de entrega aos testes multivariantes, as marcas podem usar essas ferramentas e recursos para criar experiências dinâmicas e entre canais que otimizam em escala. <br> <br> O Intelligence Suite é composto por três recursos principais: Intelligent Timing, Canal Inteligente e Seleção Inteligente."
description: "O Intelligence Suite da Braze ajuda a automatizar a tomada de decisões com insights baseados em dados. Do tempo de entrega aos testes multivariantes, as marcas podem usar essas ferramentas e recursos para criar experiências dinâmicas e entre canais que otimizam em escala."

Tool:
  - Dashboard

guide_featured_title: "Ferramentas e recursos"
guide_featured_list:
- name: Intelligent Timing
  link: /docs/user_guide/brazeai/intelligence/intelligent_timing/
  image: /assets/img/braze_icons/clock.svg
- name: Canal Inteligente
  link: /docs/user_guide/brazeai/intelligence/intelligent_channel/
  image: /assets/img/braze_icons/mail-04.svg
- name: Seleção Inteligente
  link: /docs/user_guide/brazeai/intelligence/intelligent_selection/
  image: /assets/img/braze_icons/hearts.svg

guide_menu_title: "Additional resources"
guide_menu_list:
- name: Perguntas frequentes sobre inteligência
  link: /docs/user_guide/brazeai/intelligence/faqs/
  image: /assets/img/braze_icons/annotation-question.svg


---

## Casos de uso

O Intelligence Suite oferece recursos avançados para analisar o histórico do usuário e a performance da campanha e do Canva e, em seguida, fazer ajustes automáticos para aumentar o engajamento, a visualização e as conversões. Para obter alguns exemplos de como esses recursos podem beneficiar diferentes setores, veja os casos de uso abaixo.

### e-commerce

- **Promoções relâmpago:** Use o [filtro Intelligent Channel]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) para estudar o histórico do usuário e identificar os usuários que respondem mais às notificações por push do que aos e-mails e, em seguida, envie notificações por push e e-mails para os respectivos usuários. Opcionalmente, selecione um canal específico para usuários que não têm dados suficientes para determinar seu canal preferido.
- **Banners promocionais:** Use o [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) para analisar a performance de diferentes banners promocionais em uma campanha recorrente e, em seguida, selecione e envie automaticamente o banner que gera as maiores taxas de cliques.

### Viagens

- **Ofertas de pacotes:** Use a Seleção Inteligente para testar diferentes ofertas de pacotes de viagem em um Canva recorrente e mude gradualmente o tráfego do Canvas para a variante com melhor performance para aumentar as taxas de reserva.
- **Ofertas de viagens:** Use o filtro Intelligent Channel para enviar ofertas de viagens personalizadas por meio do canal mais ativo do usuário, como e-mail ou SMS, maximizando a probabilidade de engajamento com suas mensagens.

### entretenimento

- **Promoção de novos conteúdos:** Use o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) para enviar notificações sobre novos filmes, programas, músicas e outros tipos de conteúdo quando os usuários estiverem mais propensos a abrir o envio de mensagens.
- **Compras no jogo:** Use a Seleção Inteligente para testar diferentes mensagens promocionais para compras no jogo e selecionar automaticamente a que gera as maiores taxas de conversão.

### Restaurante de serviço rápido

Vamos imaginar que trabalhamos no SandwichEmperor, um restaurante de fast food que tem um novo item de menu por tempo limitado: o Royal Roast. Usaremos dois recursos do Intelligence Suite para enviar promoções personalizadas em um canva.

#### Use o Intelligent Timing para saber quando enviar notificações

Usaremos o Intelligent Timing para analisar as interações anteriores de nossos usuários com nosso app e cada canal de envio de mensagens e, em seguida, selecionaremos automaticamente o melhor momento para promover o Royal Roast para cada usuário. Alguns usuários podem receber a promoção à tarde, enquanto outros podem recebê-la à noite. 

Forneceremos um tempo de fallback para usuários que não têm interações anteriores suficientes para analisar: o tempo mais popular para usar o app entre todos os usuários.

![Configurações de envio de mensagens do Intelligent Timing para uma etapa de Mensagem.][1]

#### Use a Seleção Inteligente para selecionar a promoção

Para as mensagens promocionais reais, usaremos o Intelligent Selection para testar três mensagens diferentes (notificação por push, envio de e-mail e SMS) para o Royal Roast. A Intelligent Selection analisará a performance de todas as nossas mensagens promocionais duas vezes por dia e, em seguida, enviará gradualmente mais mensagens de melhor performance e menos mensagens de outras.

Depois que a Seleção Inteligente reunir dados suficientes para determinar a mensagem de melhor performance, ele usará essa mensagem em 100% dos envios futuros.

![Seção Testes A/B de um Canva com a Seleção Inteligente ativada.][3]

#### Iniciar o Canva

Com o Intelligent Timing e a Seleção Inteligente, configuramos nossas promoções Royal Roast para serem otimizadas em termos de tempo e envio de mensagens. Podemos lançar nosso canva e observar como nossos envios mudam para acomodar as preferências do usuário.

[1]: {% image_buster /assets/img/intelligence_suite1.png %}
[3]: {% image_buster /assets/img/intelligent_selection_canvas.png %}
