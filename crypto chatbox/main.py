print("👋 Hey! I'm CryptoBuddy – your AI-powered financial sidekick! 🚀")
print("I can help you choose the best crypto based on trends and sustainability.")

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def chatbot():
    while True:
        user_query = input("\nYou: ").lower()

        if "exit" in user_query or "bye" in user_query:
            print("CryptoBuddy: Goodbye! Remember, crypto is risky—do your own research! 💸")
            break

        elif "sustainable" in user_query:
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

        elif "trending" in user_query or "rising" in user_query:
            trending_cryptos = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
            print(f"CryptoBuddy: These coins are trending up: {', '.join(trending_cryptos)} 📈")

        elif "most profitable" in user_query or "growth" in user_query:
            for coin, data in crypto_db.items():
                if data["price_trend"] == "rising" and data["market_cap"] == "high":
                    print(f"CryptoBuddy: {coin} is a great choice for profit! 🚀 High cap and rising price!")
                    break
            else:
                print("CryptoBuddy: Hmm... no high-cap coins are rising right now.")

        else:
            print("CryptoBuddy: Sorry, I didn’t get that. Try asking about trends, sustainability, or profitability.")

# Run the bot
chatbot()
