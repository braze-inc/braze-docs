The `properties` values must be an object up to 50&nbsp;KB where the keys are the property names and the values are the property values. Property names must be strings, 255 characters or fewer, with no leading dollar signs (`$`).

Property values can be any of the following data types:

| Data type | Description |
| --- | --- |
| Number | Integer or float |
| Boolean | Value `true` or `false` |
| Datetime | String in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) or `yyyy-MM-dd'T'HH:mm:ss:SSSZ` format. Not supported within arrays. |
| String | 255 characters or fewer |
| Array | Supported; datetimes are not supported within arrays. |
| Object | Ingested as strings (not nested objects). For nested data, use a string value (for example, JSON serialized). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The following keys are reserved and cannot be used as property names: `time`, `product_id`, `quantity`, `event_name`, `price`, and `currency`. Using a reserved key in the `properties` object returns the error "Invalid 'properties' field".
