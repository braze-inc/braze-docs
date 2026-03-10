---
nav_title: "Tutorial: fast food"
article_title: Tutorial da Intelligence Suite
page_order: 10
search_rank: 12
description: "Novo na Braze Intelligence Suite? Comece com este tutorial."
tool:
  - Dashboard
---

# Tutorial da Intelligence Suite

> Novo na Braze Intelligence Suite? Comece com este tutorial. Para informações gerais, consulte [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/).

## Tutorial: fast food

Imagine que você trabalha no SandwichEmperor, uma rede de fast food com um novo item de menu por tempo limitado: o Royal Roast. Usamos dois recursos da Intelligence Suite para enviar ações personalizadas em um Canvas.

### Etapa 1: Usar Intelligent Timing para o momento das notificações

Usamos o Intelligent Timing para analisar as interações passadas dos usuários com o app e cada canal de mensagem e escolher automaticamente o melhor momento para promover o Royal Roast a cada usuário. Alguns usuários recebem a ação à tarde, outros à noite.

Para usuários sem interações passadas suficientes, definimos um horário de fallback: o horário de uso do app mais popular entre todos os usuários.

![Configurações de entrega do Intelligent Timing para um passo de mensagem.]({% image_buster /assets/img/intelligence_suite1.png %})

### Etapa 2: Usar Intelligent Selection para a escolha da mensagem

Para as mensagens promocionais em si, usamos o Intelligent Selection para testar três mensagens (push, e-mail e SMS) para o Royal Roast. O Intelligent Selection analisa o desempenho de todas as mensagens promocionais duas vezes por dia e envia gradualmente mais da melhor e menos das demais.

Quando o Intelligent Selection tiver dados suficientes para determinar a melhor mensagem, essa mensagem será usada em 100% dos envios futuros.

![Área de teste A/B de um Canvas com Intelligent Selection ativado.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Etapa 3: Iniciar o Canvas

Com Intelligent Timing e Intelligent Selection, otimizamos o momento e a mensagem das ações do Royal Roast. Podemos iniciar o Canvas e observar as entregas se adaptarem às preferências dos usuários.
