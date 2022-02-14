import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

email = """Hello,

 

Attend IDP's U.S. Virtual Education Fairs where you can meet top US universities and colleges and discuss your queries related to courses, scholarships, intakes, visa and much more.


 

Please find below the artwork and registration link for your reference. We request you to kindly forward it to any of your friends/relatives who is interested to study in the USA for further study.


Hi vivek,

Welcome! We’re excited that you're exploring careers at Microsoft and that you've created your account. As a reminder, you created your profile using your Google account and email address vivekchary541@gmail.com. Please continue using this sign in option when visiting the site.

What's next?

We encourage you to complete your profile – it’s the first step in getting to know you! You can build your profile any way you’d like – you can import it from LinkedIn, manually update it, or import/attach a resume. The most important thing is that your profile tells your story!

We hope you’ll take some time to explore Microsoft Careers, save jobs that are of interest to you, apply for openings, and engage in the recruiting processes. Check back in to your Action Center regularly for updates.

Thank you,

Microsoft Recruiting

 

Please find below the artwork and registration link for your reference."""
               
               
sentences = nltk.sent_tokenize(email)
lemmatizer = WordNetLemmatizer()

# Lemmatization
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)      