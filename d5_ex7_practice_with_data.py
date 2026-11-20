import requests

resp = requests.get("https://google.com")
print(resp.text[:100])

# dacă avem de downloadat o pagină web, folosim
resp.text
# ^^ este str, s-a aplicat deja .decode() pe el
#    cu encoding-ul (charset-ul) pe care l-a prezentat
#    serverul

# dacă avem de downloadat un fișier, folosim
resp.content # este bytes


TODOS_URL = 'https://jsonplaceholder.typicode.com/todos'
resp = requests.get(TODOS_URL)

# dacă avem de-a face cu json,
# accesăm metoda .json()


# ne creăm un modul în care să păstrăm
# configurarea generală a aplicației

# și ne mutăm într-un alt fișier
# care să fie fișierul nostru de proiect

#from todos import save_todos, load_todos
#todos = load_todos()
#save_todos(todos)