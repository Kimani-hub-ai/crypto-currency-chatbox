# crypto-currency-chatbox
# 💸 CryptoBuddy – Your AI-Powered Financial Sidekick! 🌟

Welcome to **CryptoBuddy**, a beginner-friendly AI chatbot built with Python. This chatbot offers basic investment advice based on predefined cryptocurrency data, focusing on **profitability** and **sustainability**.

---

## 🚀 Project Overview

This chatbot was built as part of an AI Introduction assignment. The objective was to design a **rule-based AI chatbot** that helps users make simple cryptocurrency investment decisions using static logic and hardcoded data.

---

## 🎯 Features

- 🔍 **Trend Analysis:** Identifies which coins are currently rising in value.
- 🌱 **Sustainability Evaluation:** Recommends eco-friendly coins based on energy use and viability.
- 💰 **Profitability Logic:** Suggests high-potential coins using market cap and price trend.
- 🧠 **Conversational Flow:** Uses `if-else` logic for natural, friendly conversation.
- ⚠️ **Disclaimer Included:** Warns users about the risks of investing in cryptocurrencies.

---

## 🛠️ Tools & Technologies

- **Language:** Python 3.x
- **IDE:** Visual Studio Code
- **Data Type:** Static dictionary (simulated crypto dataset)
- **Libraries Used:** None (optional upgrade: NLTK, ChatterBot)

---

## 🧠 Sample Dataset

```python
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
