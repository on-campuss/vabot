from vabot.chatbot import Vabot
from vabot.config import BaseConfig as cfg


def main():
    vabot = Vabot(api_key="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", organization_id="org-5NqK4uMmbTOTcu7VYt8mXTBC")
    response = vabot.generate_response("apa itu python")
    print(response)

if __name__ == "__main__":
    main()