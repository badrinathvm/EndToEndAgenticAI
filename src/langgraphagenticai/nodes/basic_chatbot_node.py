from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot Node
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Process the state and return the response.

        Args:
            state (State): The state.

        Returns:
            str: The response.
        """
        return {"messages":self.llm.invoke(state['messages'])}