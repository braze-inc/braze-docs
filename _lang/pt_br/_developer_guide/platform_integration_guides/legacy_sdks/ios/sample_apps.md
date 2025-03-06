---
nav_title: Exemplos de aplicativos
article_title: Exemplos de aplicativos para iOS
platform: iOS
page_order: 9
description: "Este artigo de referência aborda os apps de amostra do iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Exemplos de aplicativos

Os SDKs da Braze vêm com aplicativos de amostra no repositório para sua conveniência. Cada um desses apps é totalmente compilável, portanto, você pode testar os recursos do Braze e implementá-los em seus próprios aplicativos. Testar o comportamento em seu próprio aplicativo em comparação com o comportamento esperado e os caminhos de código nos aplicativos de amostra é uma excelente maneira de depurar quaisquer problemas que você possa encontrar.

## Criação de aplicativos de teste
Vários aplicativos de teste estão disponíveis no [repositório do GitHub do SDK do iOS ](https://github.com/appboy/appboy-ios-sdk "Appboy iOS GitHub Repository"). Siga estas instruções para criar e executar nossos aplicativos de teste.

1. Crie um novo [espaço de trabalho]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) e note a chave de API do identificador do app.
2. Coloque sua chave de API no campo apropriado do arquivo `AppDelegate.m`.

As notificações por push para o aplicativo de teste iOS exigem configuração adicional. Consulte nossa [integração com o iOS Push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) para obter detalhes.

