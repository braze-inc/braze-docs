## Relationship diagram

```mermaid
---
config:
  layout: elk
  elk:
    mergeEdges: true
    nodePlacementStrategy: LINEAR_SEGMENTS
---
erDiagram
    {% multi_lang_include snowflake_mermaid/FILENAME %}

    CHANGELOGS_CANVAS_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
        string conversion_behaviors
        string variations
    }
    SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {
        string Id FK
        string time
        string app_group_id
        string type
        string api_step_id
        string experiment_splits
        string conversion_behaviors
        string name
    }
    SNAPSHOTS_CANVAS_STEP_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
        string actions
    }
    SNAPSHOTS_CANVAS_VARIATION_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
    }
    SNAPSHOTS_EXPERIMENT_STEP_SHARED {
        string Id FK
        string time
        string app_group_id
        string type
        string api_step_id
        string experiment_splits
        string conversion_behaviors
        string name
    }

    CHANGELOGS_CAMPAIGN_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
        string conversion_behaviors
        string actions
    }
    SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
    }

    CAMPAIGN_ENROLLMENT_EVENT {
        string id PK
        string campaign_id FK
        string campaign_api_id FK
        string user_id FK
        string app_api_id
        string app_group_api_id
        string app_group_id
        string country
        string device_id
        string dispatch_id
        string external_user_id
        string gender
        string language
        string message_variation_api_id
        string send_id
        string sf_created_at
        string time
        string timezone
    }
    CAMPAIGN_CONVERSION_EVENT {
        string id PK
        string campaign_id FK
        string campaign_api_id FK
        string message_variation_api_id FK
        string user_id FK
        string app_api_id
        string app_group_api_id
        string app_group_id
        string conversion_behavior_index
        string country
        string device_id
        string dispatch_id
        string external_user_id
        string gender
        string language
        string send_id
        string sf_created_at
        string time
        string timezone
    }

    CANVAS_ENTRY_EVENT {
        string id PK
        string canvas_id FK
        string canvas_api_id FK
        string canvas_step_api_id FK
        string canvas_variation_api_id FK
        string user_id FK
        string app_group_api_id
        string app_group_id
        string country
        string device_id
        string external_user_id
        string gender
        string in_control_group
        string language
        string sf_created_at
        string time
        string timezone
    }
    CANVAS_EXPERIMENT_STEP_ENTRY_EVENT {
        string id PK
        string canvas_id FK
        string canvas_api_id FK
        string canvas_step_api_id FK
        string canvas_variation_api_id FK
        string user_id FK
        string app_group_id
        string experiment_split_api_id
        string experiment_step_api_id
        string external_user_id
        string in_control_group
        string sf_created_at
        string time
    }
    CANVAS_EXIT_EVENT {
        string id PK
        string canvas_id FK
        string canvas_api_id FK
        string canvas_step_api_id FK
        string canvas_variation_api_id FK
        string user_id FK
        string app_group_api_id
        string app_group_id
        string external_user_id
        string sf_created_at
        string time
    }

    CANVAS_EXPERIMENT_STEP_CONVERSION_EVENT {
        string id PK
        string canvas_id FK
        string canvas_api_id FK
        string canvas_step_api_id FK
        string canvas_variation_api_id FK
        string user_id FK
        string app_api_id
        string app_group_id
        string conversion_behavior_index
        string experiment_split_api_id
        string experiment_step_api_id
        string external_user_id
        string sf_created_at
        string time
    }
    CANVAS_CONVERSION_EVENT {
        string id PK
        string canvas_id FK
        string canvas_api_id FK
        string canvas_step_api_id FK
        string canvas_step_message_variation_api_id FK
        string canvas_variation_api_id FK
        string user_id FK
        string app_api_id
        string app_group_api_id
        string app_group_id
        string conversion_behavior_index
        string country
        string device_id
        string external_user_id
        string gender
        string language
        string sf_created_at
        string time
        string timezone
    }

    %% Relationships for Group Labels
    GROUP_1["Campaign Snapshots and Log"] { }
    CHANGELOGS_CAMPAIGN_SHARED ||--o{ GROUP_1 : joins
    SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED ||--o{ GROUP_1 : joins
    GROUP_1 ||--o{ EVENT : joins

    GROUP_2["Campaign Events"] { }
    CAMPAIGN_ENROLLMENT_EVENT ||--o{ GROUP_2 : joins
    CAMPAIGN_CONVERSION_EVENT ||--o{ GROUP_2 : joins
    GROUP_2 ||--o{ EVENT : joins

    GROUP_3["Canvas Events"] { }
    CANVAS_ENTRY_EVENT ||--o{ GROUP_3 : joins
    CANVAS_EXPERIMENT_STEP_ENTRY_EVENT ||--o{ GROUP_3 : joins
    CANVAS_EXIT_EVENT ||--o{ GROUP_3 : joins
    GROUP_3 ||--o{ EVENT : joins

    GROUP_4["Canvas Experiments"] { }
    CANVAS_EXPERIMENT_STEP_CONVERSION_EVENT ||--o{ GROUP_4 : joins
    CANVAS_CONVERSION_EVENT ||--o{ GROUP_4 : joins
    GROUP_4 ||--o{ EVENT : joins

    GROUP_5["Canvas Snapshots and Log"] { }
    CHANGELOGS_CANVAS_SHARED ||--o{ GROUP_5 : joins
    SNAPSHOTS_CANVAS_FLOW_STEP_SHARED ||--o{ GROUP_5 : joins
    SNAPSHOTS_CANVAS_STEP_SHARED ||--o{ GROUP_5 : joins
    SNAPSHOTS_CANVAS_VARIATION_SHARED ||--o{ GROUP_5 : joins
    SNAPSHOTS_EXPERIMENT_STEP_SHARED ||--o{ GROUP_5 : joins
    GROUP_5 ||--o{ EVENT : joins
```

- `PK` = primary key
- `FK` = foreign key
