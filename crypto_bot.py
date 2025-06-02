class CryptoBuddy:
    def __init__(self):
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10,
                "fact": "Bitcoin was the first cryptocurrency, launched in 2009 by Satoshi Nakamoto."
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10,
                "fact": "Ethereum introduced smart contracts and is the foundation of many Web3 apps."
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10,
                "fact": "Cardano uses a proof-of-stake model called Ouroboros, making it eco-friendly."
            }
        }


    def greet(self):
        print("👋 Hey there! I'm *CryptoBuddy*, your friendly crypto sidekick!")
        print("Ask me about trends, sustainability, coin comparisons, or cool crypto facts.")
        print("📢 Disclaimer: Crypto is risky—always do your own research!")

    def show_help(self):
        print("""
🤖 You can ask me:
- What's the most sustainable coin?
- Which crypto is trending?
- Tell me a fun fact about Bitcoin.
- Compare Bitcoin and Cardano.
- List all cryptos.
- Give me some motivation!
- Type 'exit' to quit.
""")

    def respond(self, user_query):
        query = user_query.lower()

        if "help" in query:
            self.show_help()

        elif "sustainable" in query:
            best = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            print(f"🌱 {best} is the most eco-friendly choice!")

        elif "trending" in query:
            trending = [k for k, v in self.crypto_db.items() if v["price_trend"] == "rising"]
            print("📈 These cryptos are trending up: " + ", ".join(trending))

        elif "long-term" in query or "growth" in query:
            for name, data in self.crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] >= 0.7:
                    print(f"🚀 {name} is trending and sustainable. Great for long-term growth!")
                    return
            print("🔍 No perfect match found, but Cardano looks promising.")

        elif "buy" in query or "recommend" in query:
            for name, data in self.crypto_db.items():
                if data["price_trend"] == "rising" and data["market_cap"] == "high":
                    print(f"💡 You might consider {name}, it’s rising and has a strong market presence.")
                    return
            print("📊 No high market cap coins are currently rising.")

        elif "compare" in query:
            names = [name for name in self.crypto_db if name.lower() in query]
            if len(names) == 2:
                a, b = names
                print(f"📊 Comparing {a} vs {b}:")
                for key in ["price_trend", "market_cap", "energy_use", "sustainability_score"]:
                    print(f"  {key.title()}: {a}: {self.crypto_db[a][key]} | {b}: {self.crypto_db[b][key]}")
            else:
                print("❗ Please mention two valid crypto names to compare.")

        elif "fact" in query or "tell me about" in query:
            for name in self.crypto_db:
                if name.lower() in query:
                    print(f"💡 Fun Fact about {name}: {self.crypto_db[name]['fact']}")
                    return
            print("🤷 I don't have a fact for that one. Try Bitcoin, Ethereum, or Cardano.")

        elif "list" in query or "all coins" in query:
            print("📋 Crypto Overview:")
            for name, data in self.crypto_db.items():
                print(f"- {name}: Trend={data['price_trend']}, MarketCap={data['market_cap']}, Sustainability={data['sustainability_score']*10}/10")

        elif "motivation" in query or "quote" in query:
            print("💬 'An investment in knowledge pays the best interest.' – Benjamin Franklin")

        else:
            print("🤖 I didn’t understand that. Try typing 'help' to see what I can do!")

if __name__ == "__main__":
    bot = CryptoBuddy()
    bot.greet()
    bot.show_help()

    while True:
        query = input("\nYou: ")
        if query.lower() in ["exit", "quit", "bye"]:
            print("👋 Bye for now! Stay smart with your investments!")
            break
        bot.respond(query)