from openai import OpenAI
from config import Config

class AssistantService:
    """
    Service class for handling OpenAI Assistant API interactions.
    """
    
    def __init__(self):
        """Initialize OpenAI client and create necessary resources."""
        self.openAI = OpenAI(api_key=Config.OPENAI_KEY)
        self.assistant_id = Config.ASSISTANT_ID
        self.assistant = self.get_assistant()
        self.thread = self.get_or_create_thread()

    def get_assistant(self):
        """Retrieve the OpenAI Assistant instance."""
        return self.openAI.beta.assistants.retrieve(self.assistant_id)

    def get_or_create_thread(self):
        """Create a new conversation thread."""
        return self.openAI.beta.threads.create()

    def stream_assistant(self, message):
        """
        Stream the assistant's response.
        
        Args:
            message (str): User's input message
            
        Yields:
            str: Chunks of the assistant's response
        """
        self.openAI.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=message
        )
        
        with self.openAI.beta.threads.runs.stream(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id,
        ) as stream:
            for event in stream.text_deltas:
                yield(event) 