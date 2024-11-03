# FletFlow

[**日本語**](README.md)

- FletFlow is an easy-to-develop, stable real-time system using Flet's GUI for seamless progress tracking, updates, and error handling in business apps.
- By deciding in advance the rules for interaction between the GUI side and the back-end side, development can be completely split.

## Interface Classification in FletFlow

In FletFlow, user interface (UI) elements are categorized into three main types. This classification clarifies each element's role, supporting a structured design and smooth data flow between frontend and backend.

| Type               | Description                                                            | Role                                                                                      | Examples                                              |
|--------------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-------------------------------------------------------|
| **Static Display** | Elements that show fixed content, unaffected by user input.            | Provides essential, non-interactive information like program name, static text, or logos. | Application title, copyright info, decorative images  |
| **Dynamic Display**| Elements that change based on user input or selections.                | Holds user inputs and selections, which may later be used for processing.                 | Calendar input, toggle/switch, counter, text field    |
| **Execution Trigger** | Elements that initiate processing based on the Dynamic Display inputs. | Acts as a trigger to send stored data from Dynamic Display elements to the backend.       | Execute button, reset button                          |

## Data Transmission Mode in FletFlow

In FletFlow, when the user activates an element in the Execution Trigger (such as pressing the Execute button), the system transitions to **Data Transmission Mode**. In this mode, data from the Dynamic Display elements are transmitted to the backend system, which operates as a separate process using Python's `multiprocessing` module. This ensures smooth and isolated data processing without blocking the user interface.

### Data Table for Transmission

To facilitate reliable communication between the GUI and the backend, FletFlow uses a structured data table. Each message sent between the GUI and backend follows a specific format, with fields that describe the type of message, command, status, data content, and additional details as needed.

| Field Name   | Description                                         | Example                                          |
|--------------|-----------------------------------------------------|--------------------------------------------------|
| `type`       | Specifies the message type                          | `"request"`, `"response"`, `"complete"`          |
| `command`    | Specifies the action or function to execute         | `"calculate"`, `"update_status"`                 |
| `status`     | Indicates the processing state or response status   | `"progress"`, `"success"`, `"error"`             |
| `data`       | Contains the core data for processing               | `{"operand1": 5, "operand2": 3, "operation": "multiply"}` |
| `details`    | Provides additional information or error messages   | `"Calculation completed."`, `"Invalid input"`    |

## Communication Flow in Data Transmission Mode

In Data Transmission Mode, FletFlow disables all GUI inputs to ensure a stable processing environment. Once the mode is complete, the GUI re-enables inputs. The table below outlines the step-by-step communication flow.

| Step                            | Description                                                                                                         | Purpose                                                                                     |
|---------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| **1. Enter Data Transmission Mode** | The GUI enters Data Transmission Mode when an Execution Trigger is activated and disables all input elements.       | Prevents user interactions during processing for stability.                                |
| **2. Send Data to Backend**         | The GUI sends data to the backend using `multiprocessing`, following the structured data table format.             | Ensures consistent data structure and reliable communication.                              |
| **3. Backend Processing**           | The backend processes the command specified in `command` and sends multiple `response` messages to update the GUI. | Provides real-time updates, progress, or errors during processing.                         |
| **4. Real-time Response Handling**  | The GUI listens for `response` messages from the backend, updating the UI based on `status` and `data`.            | Reflects the latest status, progress, or errors in the UI while keeping inputs disabled.    |
| **5. Complete Transmission Mode**   | After receiving a `complete` message, the GUI exits Data Transmission Mode and re-enables all input elements.      | Restores UI usability and allows the user to perform new actions.                          |

This table highlights each step's role in maintaining a responsive, stable interaction between the frontend and backend during Data Transmission Mode.
