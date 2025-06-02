import requests

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

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
        self.coin_ids = {
            "Bitcoin": "bitcoin",
            "Ethereum": "ethereum",
            "Cardano": "cardano"
        }

    def get_real_time_data(self, coin_name):
        coin_id = self.coin_ids.get(coin_name, coin_name.lower())
        try:
            # Fetch 7-day price trend
            url = f"{COINGECKO_API_URL}/coins/{coin_id}/market_chart?vs_currency=usd&days=7"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                prices = data['prices']
                start_price = prices[0][1]
                end_price = prices[-1][1]
                price_trend = "rising" if end_price > start_price else "falling" if end_price < start_price else "stable"
            else:
                price_trend = self.crypto_db[coin_name]["price_trend"]

            # Fetch market cap
            url = f"{COINGECKO_API_URL}/coins/markets?vs_currency=usd&ids={coin_id}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                market_cap = data[0]["market_cap"] if data else None
                market_cap_rank = "high" if market_cap > 100_000_000_000 else "medium" if market_cap > 10_000_000_000 else "low"
            else:
                market_cap_rank = self.crypto_db[coin_name]["market_cap"]

            return {"price_trend": price_trend, "market_cap": market_cap_rank}
        except:
            return {
                "price_trend": self.crypto_db.get(coin_name, {}).get("price_trend", "unknown"),
                "market_cap": self.crypto_db.get(coin_name, {}).get("market_cap", "unknown")
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
            print(f"🌱 {best} is the most eco-friendly choice with a sustainability score of {self.crypto_db[best]['sustainability_score']*10}/10!")

        elif "trending" in query:
            trending = []
            for coin in self.crypto_db:
                real_time_data = self.get_real_time_data(coin)
                if real_time_data["price_trend"] == "rising":
                    trending.append(coin)
            if trending:
                print("📈 These cryptos are trending up (based on real-time data): " + ", ".join(trending))
            else:
                print("📊 No coins are trending up right now.")

        elif "long-term" in query or "growth" in query:
            for coin in self.crypto_db:
                real_time_data = self.get_real_time_data(coin)
                if real_time_data["price_trend"] == "rising" and self.crypto_db[coin]["sustainability_score"] >= 0.7:
                    print(f"🚀 {coin} is trending up (real-time) and sustainable. Great for long-term growth!")
                    return
            print("🔍 No perfect match found, but Cardano looks promising.")

        elif "buy" in query or "recommend" in query:
            for coin in self.crypto_db:
                real_time_data = self.get_real_time_data(coin)
                if real_time_data["price_trend"] == "rising" and real_time_data["market_cap"] == "high":
                    print(f"💡 You might consider {coin}, it’s rising and has a strong market presence (real-time data).")
                    return
            print("📊 No high market cap coins are currently rising.")

        elif "compare" in query:
            names = [name for name in self.crypto_db if name.lower() in query]
            if len(names) == 2:
                a, b = names
                a_data = self.get_real_time_data(a)
                b_data = self.get_real_time_data(b)
                print(f"📊 Comparing {a} vs {b} (real-time data where available):")
                for key in ["price_trend", "market_cap"]:
                    print(f"  {key.title()}: {a}: {a_data[key]} | {b}: {b_data[key]}")
                for key in ["energy_use", "sustainability_score"]:
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
            print("📋 Crypto Overview (real-time data where available):")
            for coin in self.crypto_db:
                real_time_data = self.get_real_time_data(coin)
                print(f"- {coin}: Trend={real_time_data['price_trend']}, MarketCap={real_time_data['market_cap']}, Sustainability={self.crypto_db[coin]['sustainability_score']*10}/10")

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