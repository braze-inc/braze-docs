---
nav_title: Solução de problemas
article_title: Solução de problemas com telas
page_order: 11
page_type: reference
description: "Esta página fornece etapas de solução de problemas para Canvases."
tool: Canvas
---

# Solução de problemas com telas

> Esta página o ajuda a solucionar problemas com seus Canvases.

## Por que um usuário não recebeu uma etapa do Canvas acionada?

Primeiro, confirme se o evento personalizado está sendo passado para o Braze. Vá para **Analytics** > **Custom Events Report** e selecione o respectivo evento personalizado e o intervalo de datas. Se o evento não for exibido, confirme se ele foi configurado corretamente e se o usuário executou a ação correta.

Se o evento personalizado for exibido, solucione o problema da seguinte forma:

- Verifique o download do perfil do usuário para confirmar se ele acionou o evento e quando o fez. Se o evento foi acionado, compare o registro de data e hora de quando o evento foi acionado com a hora em que o Canvas foi ao ar. O evento pode ter sido acionado antes da ativação do Canvas.
- Revise os registros de alterações do Canvas e de todos os segmentos usados na segmentação para determinar se o usuário estava no segmento quando o evento personalizado foi acionado. Se eles não estivessem no segmento, não teriam recebido a etapa Canvas.
- Verifique se o usuário foi incluído em um grupo de controle por meio de segmentação e, consequentemente, impedido de receber a etapa do Canvas.
- Se houver um atraso programado, verifique se o evento personalizado do usuário foi acionado antes do atraso. Se o evento fosse acionado antes do atraso, eles não teriam recebido a etapa do Canvas.

{% alert note %}
As mensagens in-app só podem ser acionadas por eventos enviados pelo SDK, não pela API REST.
{% endalert %}