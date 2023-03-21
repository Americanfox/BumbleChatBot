from google.cloud import dialogflow


# bumble-response-lnwq

LANGUAGE = "en"
PROJECT_ID = "chatting-bot-athena-mtgp"
SESSION_ID = "123"

class ChatBot:

    def __init__(self):
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path(PROJECT_ID, SESSION_ID)

    def convert_text(self, message_to_be_analyzed):
        self.text_to_be_analyzed = message_to_be_analyzed
        self.text_input = dialogflow.TextInput(text=self.text_to_be_analyzed, language_code=LANGUAGE)
        self.query_input = dialogflow.QueryInput(text=self.text_input)
        self.response = self.session_client.detect_intent(
            request={"session": self.session, "query_input": self.query_input}
        )
        print(self.text_input)
        print(self.query_input)
        print("=" * 20)
        print("Query text: {}".format(self.response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                self.response.query_result.intent.display_name,
                self.response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(self.response.query_result.fulfillment_text))
        return self.response.query_result.fulfillment_text


    def failed_to_send(self):
        pass
