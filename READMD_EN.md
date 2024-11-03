# FletFlow

[**日本語**](README.md)

- FletFlow is an easy-to-develop, stable real-time system using Flet's GUI for seamless progress tracking, updates, and error handling in business apps.

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

### Communication Flow in Data Transmission Mode

1. **Transition to Data Transmission Mode**:
   - Upon activation of an Execution Trigger element, the GUI sends the required data from the Dynamic Display elements to the backend. This data is formatted according to the above data table and transmitted via inter-process communication using `multiprocessing`.
   
2. **Backend Processing**:
   - The backend system receives the data, processes the command specified in the `command` field, and then sends multiple responses to update the frontend on the progress, partial results, or errors if any occur.

3. **Real-time Response Handling**:
   - The GUI continuously listens for incoming `response` messages from the backend, updating the relevant Dynamic Display elements or showing progress notifications as specified in the `status` and `data` fields.

4. **Completion of Data Transmission Mode**:
   - Once all responses have been received and the backend sends a `complete` message, the GUI exits Data Transmission Mode. User interaction with the interface is re-enabled, allowing the user to perform further actions.

This structured data flow ensures that FletFlow can handle complex processes with real-time updates and a stable, responsive user interface.
