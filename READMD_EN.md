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
