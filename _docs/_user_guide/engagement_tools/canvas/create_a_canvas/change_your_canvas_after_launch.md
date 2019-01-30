---
nav_title: Change Your Canvas After Launch
platform: Canvas
subplatform: Create a Canvas
page_order: 1
---

# Changing Your Canvas After Launch

## Initial Conditions

| **Editable**                         | **Not-Editable**      |
|----------------------------------|-------------------|
| Initial Condition                | Conversion Events |
| Target Audience                  |                   |
| Pause / Resume Initial Condition |                   |
| Workflow Name                    |                   |

## Canvas Graph

| **Editable**                                     | **Not-Editable**         |
|------------------------------------------------|----------------------|
| Pause / Resume Execution of All Workflow Steps | Deleting Steps       |
| Insert Workflow Steps                          | Deleting Variants    |
| Add New Connections                            | Deleting Connections |
| Add New Variants                               |                      |
| Variant Distribution                           |                      |

## Individual Step

| **Editable**                           | **Not-Editable**                                 |
|-------------------------------------|----------------------------------------------|
| Name                                | Schedule Type (change from delay to trigger) |
| Message Content                     |                                              |
| Step Message Platforms (add/delete) |                                              |
| Triggers                            |                                              |
| Audience                            |                                              |
| Exception Events                    |                                              |
| Delays / Windows                    |                                              |

There are a number of things to know if you plan to edit or add more steps to any other step in Canvas after launching:

- Users who have not yet entered the Canvas __will__ be eligible for newly created steps
- Users who have already passed newly created steps __will__ be eligible next time they re-enter if you have allowed users to re-enter the Canvas in Canvas Entry Settings
- Users who are currently in a Canvas, but have not reached the points where new steps are added __will__ be eligible to receive those new steps.
