
# 🤖 Lex Bot Creator (AWS Boto3 + Python)

A bThis project provides a Python script to **automate the creation of an Amazon Lex Bot** using the AWS SDK (`boto3`). It simplifies the process of deploying a Lex bot with intents like `BookHotel` and `OrderPizza`, including utterances, slots, and sample responses — all without needing to click through the AWS Console.


---

## 📌 Features

- ✅ Automatically creates an Amazon Lex v2 bot using Python
- ✅ Adds custom intents (`BookHotel`, `OrderPizza`)
- ✅ Includes utterances, sample slot types, and responses
- ✅ Fully customizable structure — easy to modify or scale
- ✅ Uses IAM Role ARN for permission management
- ✅ Ideal for demos, POCs, or learning AWS Lex

---

## 🛠️ Tech Stack

- **Language**: Python 3.7+
- **AWS SDK**: Boto3
- **Lex Version**: Amazon Lex v2
- **Cloud Platform**: AWS

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/SubuNayak/lex-bot-creator-python.git
cd lex-bot-creator-python
```

### 2. Set Up AWS Credentials

aws configure
Or use environment variables:
```bash
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_DEFAULT_REGION=your-region
```

### 3. Install Dependencies
```bash
pip install boto3
```
### 4. Update IAM Role ARN
In the script, update:
```bash
LEX_SERVICE_ROLE_ARN = "arn:aws:iam::<your-account-id>:role/YourLexBotRole"
```

### 5. Run the Script
```bash
python create_lex_bot.py
```
```bash
lex-bot-creator-python/
├── create_lex_bot.py       # Main script to create the Lex bot
├── README.md               # This file
└── ...
```

💡 Example Intents

**BookHotel :**
Utterances: "I want to book a hotel", "Reserve a room"

**OrderPizza :**
Utterances: "Order a pizza", "I want a pepperoni pizza"

🧠 Use Cases
Demos and prototypes

Automating bot creation across environments

Learning Lex programmatically

Reproducible bot deployments

🙋‍♂️ Author
Subhransu Nayak

🔗[GitHub](https://github.com/SubuNayak)

🔗 [LinkedIn](www.linkedin.com/in/subhransunayak29)

Feel free to connect or reach out if you have suggestions or questions!

📜 License
This project is licensed under the MIT License.

🌟 Show Your Support
If this helped you, please ⭐ the repo! Contributions and feedback are welcome.

---

Let me know if you’d like me to:
- Add a sample output of the script
- Link to an example bot on AWS
- Include a `requirements.txt`

Happy to help you make this repo 🔥!
