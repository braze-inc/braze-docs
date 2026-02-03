## Sobre o SDK do Braze Vega

O SDK Braze Vega permite que você colete análises de dados e exiba mensagens ricas no app para seus usuários. A maioria dos métodos no Braze Vega SDK é assíncrona e retorna promessas que devem ser aguardadas ou resolvidas.

## Integração do SDK do Braze Vega

### Etapa 1: Instalar a biblioteca do Braze

Instale o Braze Vega SDK usando seu gerenciador de pacotes preferido.

{% tabs local %}
{% tab npm %}
Se seu projeto usa NPM, você pode adicionar o Braze Vega SDK como uma dependência.

```bash
npm install @braze/vega-sdk --save
```

Após a instalação, você pode importar os métodos necessários:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
Se seu projeto usa o Yarn, você pode adicionar o Braze Vega SDK como uma dependência.

```bash
yarn add @braze/vega-sdk
```

Após a instalação, você pode importar os métodos necessários:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### Etapa 2: Inicializar o SDK

Depois que o SDK do Braze Vega for adicionado ao seu projeto, inicialize a biblioteca com a chave de API e [o endpoint de SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) encontrados em **Settings** > **App Settings** em seu dashboard do Braze.

{% alert important %}
Você deve aguardar ou resolver a promessa `changeUser` antes de chamar outros métodos do Braze, ou eventos e atribuições poderão ser definidos no usuário incorreto.
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");
      
      // Start a session
      await openSession();
      
      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };
    
    initBraze();
  }, []);
  
  return (
    // Your app components
  );
};
```

{% alert important %}
Usuários anônimos podem ser contados para o seu [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). Como resultado, talvez seja necessário carregar ou inicializar condicionalmente o SDK para excluir esses usuários da sua contagem de MAU.
{% endalert %}

## Configurações opcionais

### Registro

É possível ativar o registro do SDK para ajudar na depuração e na solução de problemas. Há várias maneiras de ativar o registro.

#### Ativar o registro durante a inicialização

Passe `enableLogging: true` para `initialize()` para registrar mensagens de depuração no console:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
Os registros básicos são visíveis para todos os usuários, portanto, considere desativar o registro antes de liberar seu código para produção.
{% endalert %}

#### Ativar o registro após a inicialização

Use `toggleLogging()` para ativar ou desativar o registro do SDK após a inicialização:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### Registro personalizado

Use `setLogger()` para fornecer uma função de registro personalizada para ter mais controle sobre como os registros do SDK são tratados:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### Opções de configuração

Você pode passar opções de configuração adicionais para `initialize()` para personalizar o comportamento do SDK:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## Fazendo upgrade do SDK

Ao fazer referência ao Braze Vega SDK a partir do NPM ou do Yarn, você pode fazer o upgrade para a versão mais recente atualizando a dependência do pacote:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## Teste de sua integração

Para verificar se a integração do SDK está funcionando corretamente:

1. Inicialize o SDK com `enableLogging: true` para ver as mensagens de depuração no console
2. Certifique-se de acessar `await changeUser()` antes de chamar outros métodos do SDK
3. Ligue para `await openSession()` para iniciar uma sessão
4. Verifique seu dashboard do Braze em **Overview (Visão geral)** para verificar se os dados da sessão estão sendo registrados
5. Teste o registro de um evento personalizado e verifique se ele aparece no dashboard


