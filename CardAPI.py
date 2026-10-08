import requests

deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1") 
print(deck.status_code)
print(deck.json())
print(deck.json().get("deck_id"))
deckID = deck.json().get("deck_id")

sampleDraw = requests.get(f"https://deckofcardsapi.com/api/deck/{deckID}/draw/?count=2")
print(sampleDraw.json())

playerHand = requests.get(f"https://deckofcardsapi.com/api/deck/{deckID}/draw/?count=2").json()["cards"]
print(playerHand)
print(f"{playerHand[0].get('value')} of {playerHand[0].get('suit')}")
print(f"{playerHand[1].get('value')} of {playerHand[1].get('suit')}")

playerHand.append(requests.get(f"https://deckofcardsapi.com/api/deck/{deckID}/draw/?count=1").json()["cards"][0])
print(f"{playerHand[2].get('value')} of {playerHand[2].get('suit')}")