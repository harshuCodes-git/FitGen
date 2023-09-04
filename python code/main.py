import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Hello, I'm the Exercise Helper. I can help you with your exercise."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Exercise Helper")

demo.launch(share=True)