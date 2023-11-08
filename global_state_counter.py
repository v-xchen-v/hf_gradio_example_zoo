# Here’s a simple example of how you might use the global state in a Gradio app to keep track of the number of times a button has been clicked

import gradio as gr

# Your function may use data that persists beyond a single function call. If the data is something accessible to all function calls and all users, you can create a variable outside the function call and access it inside the function
counter = 0

def update_counter():
    global counter
    counter += 1
    return counter

demo = gr.Blocks()
with demo:
    button = gr.Button("Click me")
    output = gr.Textbox()
    button.click(update_counter, outputs=output)

demo.launch()