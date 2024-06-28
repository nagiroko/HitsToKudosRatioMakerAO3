from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import time
from bs4 import BeautifulSoup


def main():
    Break = False
    print("Hello, this is the AO3 Hits and Kudos ratio display")
    print("The values calculated in this program is done with whole numbers")
    print("The average is calulated with this formula average = hits divided by (hits* 0.04)\n")

    while not Break:
        link = input("Enter an AO3 URL in this style https://archiveofourown.org/works/: ")
        if link.startswith("https://archiveofourown.org/works/"):
            # Set up the Edge driver options and service
            edge_options = EdgeOptions()
            edge_options.add_argument('--headless')  # Run in headless mode
            edge_options.add_argument('--disable-gpu')  # Disable GPU rendering

            driver = webdriver.Edge(options=edge_options)
            driver.get(link)

            # Wait for the page to load completely
            time.sleep(3)

            results = driver.page_source
            soup = BeautifulSoup(results, 'html.parser')
            driver.quit()

            title = soup.find("h2",class_= 'title heading')
            title = title.text.strip()
            T = str()
            count = 0
            for item in str(title):
                if count == 2 and item in "<>":
                    break
                elif item in "<>":
                    T = ""
                    count += 1
                else:
                    T += item




            # Find and print the kudos
            kudos = soup.find_all("dd",class_= 'kudos')
            K = str()
            for item in str(kudos):
                if item.isnumeric() == True:
                    K += item
            K = int(K)
            hits = soup.find_all("dd",class_= 'hits')
            H = str()
            for item in str(hits):
                if item.isnumeric() == True:
                    H += item
            H = int(H)
            average = int(H/(H *.04))

            if K == 0:
                print(f"\nTitle: {''.join(T.split())}")
                print(f"Hits:  {H}")
                print(f"Kudos: {K}\n")
                print("This fic has no kudos")
                print(f"The average of this fic should be {average} hits : 1 kudos\n")
            else:
                ratio = int(H / K)
                verdict = ""
                if ratio == average:
                    verdict = "at"
                elif ratio > average:
                    verdict = "above"
                else:
                    verdict = "bellow"
                print(f"\nTitle: {T}")
                print(f"Hits:  {H}")
                print(f"Kudos: {K}\n")
                print(f"Fic ratio is {ratio} hits : 1 kudos")
                print(f"Average ratio for this should be {average} hits : 1 kudos")
                print(f"This fic is {verdict} the average\n")

        else:
            print("Invalid URL. Please try again.")

        if input("Enter 0 if you want the program to end: ") == "0":
            Break = True
        else:
            print("")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#  https://archiveofourown.org/works/43801903/chapters/110145358