# Fundamental structure
# CORE
# used it and reused it

empty_dict = {}         # Main pythonic way
empty_dict2 = dict()    # less pythonic
grades = {'jesus': 80, 'gabriel':95}

# Lookup by key
jesus_grade = grades['jesus']

try:
    pedros_grade = grades['pedro']
except KeyError:
    print('no grande for pedro!')

'jesus' in grades
'pedro' in grades

# Default when cant find value to return
jesus_grade = grades.get('jesus', 'oh no')    # Should return the grade
pedros_grade = grades.get('pedro', 'oh no')    # Should return 'oh no'
no_ones_grade = grades.get('no one')    # Should return 'oh no'

# Al parecer se puede devolver un tipo de dato totalmente diferente para
# cada excepcion de ejecucion usando get

# print(jesus_grade)
# print(pedros_grade)
# print(no_ones_grade)

# Asigning values to dictionary
grades['quino'] = 99
grades['alex'] = 100
num_students = len(grades)
# print(num_students)

# Structured data representation
tweet = {
        "user" : "joelgrus",
        "text" : "Data Science is Awesome",
        "retweet_count" : 100,
        "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()

# print(tweet_keys)
# print(tweet_values)
# print(tweet_items)

"user" in tweet_keys    # True, but not Pythonic
"user" in tweet         # Pythonic way of checking for keys
"joelgrus" in tweet_values # True (slow but the only way to check)

# Para poder hacer uso de algunas teclas rápidas de VIM, hoy aprendimos 
# lo siguiente

# :wq       Salir y escribir (write+quit)
# :x        Salir y escribir solo si hay cambios (:q! + :w)
# ZZ        Forma alternativa de salir

# ^+Y       Scroll down
# ^+E       Scroll up
# zz        Posicionar la linea actual en la MITAD de la pantalla
#           (Particularmente siento que este es el más útil que encontré hoy,
#           me recuerda al ctrl+F de cadence
