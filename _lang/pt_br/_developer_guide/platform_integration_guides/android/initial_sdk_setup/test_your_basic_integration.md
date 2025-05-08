---
nav_title: Teste sua integração básica
article_title: Teste sua integração básica para Android e FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda como testar a integração básica de seu aplicativo Android ou FireOS."

---

# Teste sua integração básica

> Este artigo de referência aborda como testar a integração básica de seu aplicativo Android ou FireOS.

## Confirme se o rastreamento da sessão está funcionando

Neste ponto, o rastreamento de sessão deve estar funcionando em sua integração com a Braze. Para testar isso, acesse **Overview (Visão geral)**, selecione seu aplicativo no menu suspenso do nome do aplicativo selecionado (o padrão é "All Apps") e defina **Display Data For (Exibir dados para** ) como "Today" (Hoje). Em seguida, abra seu app e atualize a página. Todas as suas principais métricas devem ter aumentado em 1.

![]({% image_buster /assets/img_archive/android_sessions.png %})

Continue testando a integração navegando pelo app e conferindo se apenas uma sessão foi registrada. Em seguida, coloque o app em segundo plano por pelo menos 10 segundos e traga-o para o primeiro plano novamente. Por padrão, uma nova sessão é criada se o app for trazido para o primeiro plano depois de ficar em segundo plano ou fechado por mais de 10 segundos. Depois de fazer isso, confirme que outra sessão foi registrada.

## Rastreamento de sessões de depuração
Se o rastreamento de sessão estiver se comportando de forma inesperada, ative o [registro detalhado]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#enabling-logs) e observe o app enquanto reproduz as etapas de disparo da sessão. Observe as declarações da Braze no logcat para identificar onde as chamadas `openSession` e `closeSession` podem não ter sido registradas em suas atividades.

