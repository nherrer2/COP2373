#User enters email message and the program scans for spam words and phrases
#in the list of 30. Then, it will rate the likelihood that the message is
#spam.

# List of 30 common spam words as well as phrases.
SPAM_WORDS = ['free', 'act now', '', 'bonus', 'apply online',
              'free money', 'click here', 'double your', 'winner', 'win',
              'money back', 'earn', 'prize', 'cash', 'guaranteed',
              'save big', 'you won!', 'social security', 'giveaway',
              'amazing deal', 'no catch', 'risk-free', 'for you',
              'verify identity', 'jackpot', 'try for free', 'get rich',
              'offer', 'chance', 'join millions']

#Main func that calls out other func.
def main():

    #Getting user input.
    print('Enter the email message:')
    email_message = input()

    #Analyze email for spam email and rate the likelihood.
    score, matched_words = analyze_email(email_message)
    rating = rate_spam(score)

    #Display the results.
    print('\n Spam Results')
    print('Spam Score:', score)
    print('Likelihood of Spam:', rating)

    #If any spam words or phrases are found, list them.
    if matched_words:
        print('Words or phrases that triggered detection:')
        for word in matched_words:
            print('-', word)
    else:
        print('No spam words or phrases found.')

#Function to analyze email and calculate spam score.
def analyze_email(text):
    spam_score = 0
    matched = []
    text = text.lower()

    #Check each word.
    for word in SPAM_WORDS:
        if word in text:
            spam_score = spam_score + 1
            matched.append(word)

    return spam_score, matched

#Function indicate the likelihood of spam in the email
def rate_spam(score):
    if score == 0:
        return 'Not spam'
    elif score <= 3:
        return 'Unlikely spam'
    elif score <= 6:
        return 'Possible spam'
    elif score <= 10:
        return 'Likely spam'
    else:
        return 'Very likely spam'


#Run main function.
main()
