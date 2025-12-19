class ConversationMemory:
    def __init__(self, max_tokens=4096):
        self.messages = []
        self.max_tokens = max_tokens
    def add(self, role, content):
        self.messages.append({"role": role, "content": content})
    def get(self):
        return self.messages[-20:]
