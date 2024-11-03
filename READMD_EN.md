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

## Communication Flow in Data Transmission Mode

In FletFlow, the communication flow during Data Transmission Mode can be summarized in the following steps. This table outlines each step's purpose and its role in ensuring smooth and real-time interaction between the frontend and backend.

| Step                            | Description                                                                                                              | Purpose                                                                                   |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **1. Enter Data Transmission Mode** | When the user triggers the Execution Trigger, the GUI enters Data Transmission Mode and prepares data for transmission. | Prepares Dynamic Display data for backend processing and initiates communication.         |
| **2. Send Data to Backend**     | The GUI sends data to the backend process via `multiprocessing`, following the structured data table format.            | Ensures consistent data structure for reliable communication.                             |
| **3. Backend Processing**       | The backend receives data, processes the specified command, and sends multiple `response` messages as needed.           | Provides real-time updates, progress, or errors during processing.                        |
| **4. Real-time Response Handling** | The GUI continuously listens for `response` messages, updating UI elements based on `status` and `data`.                | Dynamically updates UI to reflect the latest status, progress, or errors.                 |
| **5. Complete Transmission Mode** | After receiving the `complete` message, the GUI exits Data Transmission Mode and re-enables user interactions.          | Finalizes the process, restores UI usability, and allows for new actions.                 |

This table outlines the communication flow that keeps FletFlow responsive, reliable, and capable of handling complex, real-time interactions.
