import openai
class Chatbot:
    def __init__(self, model="gpt-4"):
        self.model = model
        self.history = []
    def chat(self, message):
        self.history.append({"role": "user", "content": message})
        resp = openai.ChatCompletion.create(model=self.model, messages=self.history)
        reply = resp.choices[0].message.content
        self.history.append({"role": "assistant", "content": reply})
        return reply
streaming support
