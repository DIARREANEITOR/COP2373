def calculate_spam_score(message, keywords):
    #scan the message
    score = 0
    found_keywords = []
    message_lower = message.lower()

    for word in keywords:
        # Count occurrences of each keyword/phrase
        count = message_lower.count(word.lower())
        if count > 0:
            score += count
            found_keywords.append(word)

    return score, found_keywords


def get_spam_likelihood(score):

    if score == 0:
        return "Not Spam (Safe)"
    elif 1 <= score <= 2:
        return "Low Likelihood"
    elif 3 <= score <= 5:
        return "Moderate Likelihood"
    else:
        return "High Likelihood (Likely Spam)"


def main():
    # List of 30 common spam keywords and phrases
    spam_keywords = [
        "free", "winner", "urgent", "offer", "money", "click here",
        "congratulations", "no cost", "act now", "limited time",
        "investment", "invoice", "refund", "casino", "bitcoin",
        "discount", "awarded", "password", "verification", "benefit",
        "eliminate debt", "extra income", "work from home", "guaranteed",
        "buy now", "gift", "millions", "subscribe", "lottery", "prize"
    ]

    print("AI Spam Detector Tool")
    user_message = input("Paste the email message content here: \n")

    # Processing
    score, detected = calculate_spam_score(user_message, spam_keywords)
    likelihood = get_spam_likelihood(score)

    # Display Results
    print("\n" + "=" * 30)
    print(f"SPAM SCORE: {score}")
    print(f"LIKELIHOOD: {likelihood}")

    if detected:
        # Using set() to avoid duplicates in the display list
        print(f"KEYWORDS TRIGGERED: {', '.join(set(detected))}")
    print("=" * 30)


if __name__ == "__main__":
    main()