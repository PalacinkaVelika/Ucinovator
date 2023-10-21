from bs4 import BeautifulSoup

class HtmControl:
    # dává data do html
    def __init__(self):
        ...
        
    # public funkce na odeslání
    def send_questions(self):
        ...

    #Napíšu text do elementu html souboru
    def add_to_ui(self, file, element_id, text):
        with open(file, 'r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
        target_element = soup.find(id=element_id)
        if target_element:
            target_element.string = text #input do elementu
            with open(file, 'w', encoding='utf-8') as html_file: #save
                html_file.write(str(soup))
        else:
            print(f"Element with id '{element_id}' not found in the HTML.")
