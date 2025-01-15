---
title: Logs
slug: /workspace-logs
---


The **Logs** pane provides a detailed record of all component executions within a workspace. It is designed to help you track actions, debug issues, and understand the flow of data through various components.

1. To access the **Logs** pane, click your **Flow Name**, and then select **Logs**.

![](/img/logs.png)

2. All cells in the **Logs** view can be opened and inspected.

## Adding Custom Logs

If you are developing custom components, you can add your own logs that will appear in the Logs panel. This is useful for debugging and monitoring your components' execution.

### Using Component's log() Method

The simplest way to add logs that will appear in the Langflow UI is using the component's built-in `log()` method:

```python
def process_data(self):
    self.log("Starting data processing...")  # This will appear in the Logs panel
    # Your code here
    self.log("Processing completed")  # This will appear in the Logs panel
```

### Using Loguru (Terminal Only)

For debugging during development, you can use the Loguru logger. Note that these logs will only appear in the terminal where Langflow is running, not in the UI:

```python
from loguru import logger

def complex_operation(self):
    logger.info("Starting complex operation")  # Only visible in terminal
    try:
        # Your code here
        logger.success("Operation completed successfully")  # Only visible in terminal
    except Exception as e:
        logger.error(f"Operation failed: {str(e)}")  # Only visible in terminal
```

For more details on implementing logging in your components, see the [Custom Components](/components-custom-components#adding-logs-to-components) documentation.
