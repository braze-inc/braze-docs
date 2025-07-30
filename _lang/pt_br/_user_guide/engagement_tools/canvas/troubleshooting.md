---
nav_title: Solução de problemas
article_title: Solução de problemas com telas
page_order: 11
page_type: reference
description: "Esta página fornece etapas de solução de problemas para Canvas."
tool: Canvas
---

# Solução de problemas com telas

> Esta página o ajuda a solucionar problemas com suas Canvas.

## Por que um usuário não recebeu uma etapa do Canva disparada?

Primeiro, confirme se o evento personalizado está sendo passado para o Braze. Acesse **Análise de dados** > **Relatório de eventos personalizados** e, em seguida, selecione o respectivo evento personalizado e o intervalo de datas. Se o evento não for exibido, confirme se ele foi configurado corretamente e se o usuário executou a ação correta.

Se o evento personalizado for exibido, solucione o problema da seguinte forma:

- Verifique o download do perfil do usuário para confirmar se ele disparou o evento e quando o fez. Se o evento foi disparado, compare o registro de data e hora de quando o evento foi disparado com a hora em que o Canva foi TTL. O evento pode ter sido disparado antes da ativação do Canva.
- Revise os changelogs do Canva e de todos os segmentos usados no direcionamento para determinar se o usuário estava no segmento quando o evento personalizado foi disparado. Se não estivessem no segmento, não teriam recebido a etapa do canva.
- Verifique se o usuário foi inserido em um grupo de controle por meio de segmentação e, consequentemente, impedido de receber a etapa do Canva.
- Se houver uma postergação programada, verifique se o evento personalizado do usuário foi disparado antes da postergação. Se o evento fosse disparado antes da postergação, eles não teriam recebido a etapa do Canva.

{% alert note %}
As mensagens no app só podem ser disparadas por eventos enviados pelo SDK, não pela API REST.
{% endalert %}