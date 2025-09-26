    EVENT["SMS_EVENT"] {
        string id PK
        string campaign_id FK
        string campaign_updated_at
        string canvas_id FK
        string canvas_updated_at
        string canvas_step_id FK
        string canvas_step_updated_at
        string canvas_variation_id FK
        string message_variation_id FK
        string message_variation_updated_at
        string canvas_step_message_variation_id FK
        string canvas_step_message_variation_updated_at
        string user_id FK
        string abort_log
        string abort_type
        string action
        string app_group_id
        string dispatch_id
        string error
        string external_user_id
        string from_phone_number
        string inbound_phone_number
        string message_body
        string message_extras
        string event_type
        string provider_error_code
        string short_url
        string subscription_group_id
        string subscription_group_api_id
        string to_phone_number
        string time
        string timezone
        string url
        string user_agent
        string user_phone_number
    }
