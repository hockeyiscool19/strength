from dataclasses import dataclass
import json

with open("server/app/fixtures/state.json", "r") as s:
    state = json.load(s)


@dataclass
class Context:
    username: str = state["username"]
    oauth_token: str = state["oauth_token"]
    name: str = state["name"]

context = Context(state)

if __name__=="__main__":
    context = Context(state)
    print(context.username)