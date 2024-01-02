from rich import print

from vabot.base import BaseVabot
from vabot.debug import VabotDebug


def main():
    vabot = BaseVabot(api_key="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", organization_id="org-5NqK4uMmbTOTcu7VYt8mXTBC")
    response = vabot.search_with_bing("facebook adalah")
    print(response)

def debug():
    vabot = VabotDebug()
    response = vabot.search_with_bing()
    print(response)

if __name__ == "__main__":
    main()