import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


def main():
    # The url to the website to web scrap
    url="https://news.ycombinator.com/item?id=22665398"
    # Send HTTP request to the website. This returns a response object
    response=requests.get(url)
    # To get the response in a nice format allowing us to search for different parts
    soup=BeautifulSoup(response.content, "html.parser")
    # Find first level html element with indentation=0. We use class_ because class is a reserved word on py
    elements= soup.find_all(class_="ind", indent=0)
    # Get the comment from the elements list
    comments=[e.find_next(class_="comment") for e in elements]

    # List of programming languages we will check for
    languages={"python":0, "javascript":0, "c++":0, "typescript":0, "ruby":0, "rust":0, "java":0, "c#":0}

    # get the comment elements in to human readable text
    for comment in comments:
        comment_text=comment.get_text().lower()
        # split the comment text in to individual word
        words=comment_text.split(" ")
        # Remove any special characters. Store in set to remove duplicate words
        words={w.strip(",./;:'*!@#~`") for w in words}
        for language in languages:
            if language in words:
                languages[language]+=1

    print(languages)
    plt.bar(languages.keys(),languages.values())
    plt.xlabel("Language")
    plt.ylabel("jobs requiring language")
    plt.show()


if __name__=="__main__":
    main()
