{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Definindo a última localização conhecida

Para definir manualmente a última localização conhecida de um usuário, use o método `setLastKnownLocation`. Isso é útil se você coletar dados de localização fora do SDK do Braze.

```javascript
Braze.setLastKnownLocation(LATITUDE, LONGITUDE, ALTITUDE, HORIZONTAL_ACCURACY, VERTICAL_ACCURACY);
```

- No Android, `latitude` e `longitude` são obrigatórios. `altitude`, `horizontalAccuracy` e `verticalAccuracy` são opcionais.
- No iOS, `latitude`, `longitude` e `horizontalAccuracy` são obrigatórios. `altitude` e `verticalAccuracy` são opcionais.

Para compatibilidade entre plataformas, forneça `latitude`, `longitude` e `horizontalAccuracy` no mínimo.

## Definindo um atributo de localização personalizado

Para definir um atributo de localização personalizado em um perfil de usuário, use o método `setLocationCustomAttribute`.

```javascript
Braze.setLocationCustomAttribute("favorite_restaurant", 40.7128, -74.0060, optionalCallback);
```

## Solicitando inicialização de localização (apenas Android)

Chame `requestLocationInitialization` após um usuário conceder permissões de localização para inicializar os recursos de localização do Braze no Android. Este método não é suportado no iOS e não é necessário para recursos de geofence ou localização no iOS.

```javascript
Braze.requestLocationInitialization();
```

## Geofences

Geofences são suportados tanto no iOS quanto no Android. Por padrão, o SDK do Braze pode solicitar e monitorar geofences automaticamente quando a localização está disponível. Você pode contar com essa configuração automática para a maioria das integrações.

### Solicitação manual de geofences

Para solicitar manualmente uma atualização de geofence para uma coordenada GPS específica, use `requestGeofences`. Isso está disponível tanto no iOS quanto no Android. Se você usar este método, desative as solicitações automáticas de geofence em sua configuração nativa para que o SDK não sobrescreva suas solicitações manuais.

```javascript
Braze.requestGeofences(LATITUDE, LONGITUDE);
```
