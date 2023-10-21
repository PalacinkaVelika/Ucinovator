from controller.requester import Requester


'''
#   Otevře main html   <--- pokud by někdo v budoucnu přidělal html support
def open_html_file():
    index_html_path = os.path.join(os.getcwd(), 'view', 'index.html')
    #exist check
    if os.path.isfile(index_html_path):
        webbrowser.open(index_html_path)
    else:
        print("The 'index.html' file does not exist in the 'view' folder.")
'''

def start_test():
    Requester()

if __name__ == "__main__":
    start_test()
