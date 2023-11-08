# It's important to note that the session state is unique to each user. This means that different users can interact with the same Gradio app simultaneously without affecting each other's session states.
# Here’s a simple example of how you might use the session state in a Gradio app to keep track of the number of times a button has been clicked
# docs: https://www.gradio.app/guides/interface-state
# docs: https://www.gradio.app/guides/state-in-blocks

import gradio as gr

def update_counter(counter): # Step 1: Pass in an extra parameter into your function, which represents the state of interface.
    counter += 1
    
    # Step 2: At the end of the function, return the updated value of the state as extra return value (so that the state could update by the function, otherwise, keep as input by mistake)
    return counter, counter

demo = gr.Blocks()
with demo:
    # Step 0: Create a variable which represents the state of interface inside the block(or interface)
    counter = gr.Number(value=0)
    
    button = gr.Button("Click me")
    output = gr.Textbox()
    
    # Step 3: Add the 'state' input and 'state' output component when create your interface
    button.click(update_counter, inputs=counter, outputs=[output, counter])

demo.launch()