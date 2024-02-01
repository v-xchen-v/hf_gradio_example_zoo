import gradio as gr

def handle_switching(is_check):
    if is_check:
        return gr.Button.update(visible=True), gr.Button.update(visible=False)
    else:
        return gr.Button.update(visible=False), gr.Button.update(visible=True)
        
with gr.Blocks() as demo:
    # create a checkbox, default as checked
    switch = gr.Checkbox(label='Use mock data?', value=True)
    
    # create two button which stands for two conflict condition, when one button shows the other should hide.
    button1 = gr.Button(value='Click to Mock Data')
    button2 = gr.Button(value='Click to Upload Real Data', visible=False)
    
    # connect checkbox changes event to button visibility changing
    switch.change(fn=handle_switching, inputs=switch, outputs=[button1, button2])
    
    demo.launch()