---
nav_title: Exemplos de aplicativos
article_title: Exemplos de aplicativos para iOS
platform: Swift
page_order: 9
search_rank: 2
description: "Este artigo aborda os aplicativos de amostra do SDK do Swift para iOS."

---

# Exemplos de aplicativos

> Os SDKs da Braze vêm com aplicativos de amostra no repositório para sua conveniência. Cada um desses apps é totalmente compilável, portanto, você pode testar os recursos do Braze e implementá-los em seus próprios aplicativos. 

Testar o comportamento em seu próprio aplicativo em comparação com o comportamento esperado e os caminhos de código nos aplicativos de amostra é uma excelente maneira de depurar quaisquer problemas que você possa encontrar.

## Exemplos de navegação

Vários aplicativos de teste estão disponíveis na pasta `Examples` do [repositório GitHub do Swift SDK](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples). O README descreve todas as diferentes permutações de integrações de amostra, como:

1. Tipos de integração (Swift Package Manager, CocoaPods, Manual)
2. Linguagens de codificação (Swift e Objective C)
3. Plataformas (iOS, tvOS, Mac Catalyst, etc.)
4. Recursos (mensagens no app, cartões de conteúdo, localização, Rich Push, Push Stories, etc.)
5. Tipos de personalização (UI padrão, UI totalmente personalizada)

## Criação de aplicativos de teste

Siga estas instruções para criar e executar nossos aplicativos de teste.

1. Crie um novo [espaço de trabalho]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) e note a chave de API do identificador do app e o ponto de extremidade.
2. Com base em seu método de integração (Swift Package Manager, CocoaPods, Manual), selecione o arquivo `xcodeproj` apropriado para abrir.
3. Coloque sua chave de API e seu endpoint no campo apropriado no arquivo `Credentials`.

