# Variablen erlauben uns Daten zu speichern.
# Diese können dann zu einem späteren Zeitpunkt, mit einem zuvor gewählten Ausdruck, wieder aufrufen werden.
# Mit dem erstellen einer Variablen reservieren wir quasi einen teil des physischen Speichers.
# Bsp. wie wenn ich mir auf ein Kärtchen meine Adresse notieren würde.
# Wenn ich dann später meine Adresse brauche, kann ich einfach auf das Kärtchen schauen.

x = 5
x = 10
y = 7

x = "Hello World" # Zeilen dublizieren mit Alt + Umschalt(Shift) + Pfeil Oben/Unten
xx = "Hello World"
xxx = "Hello World"

# print(x)
# print(xx)
# print(xxx)

# Ein paar regeln für Variablen:
# Enthalten können sie die Zeichen A-Z, a-z, 0-9 und _(Unterstrich)
# Der erste Buchstabe muss klein sein, (sie können auch mit einem "_" beginnen, was in der Praxis für spezielle Fälle genutzt wird)
# Sie dürfen auch nicht mit einer Zahl beginnen
# Variablen sidn "case-sensitive", man muss genau auf Groß- und Kleinscheibung achten.


first_name = "Tony" # snake case
firstName = "Steve" # camel case
# Es haben sich im Laufe der Zeit gewisse Konventionen für Variablen gebildet mit denen wir vertraut sein sollten.
# Generel gilt es als best practice, selbsterklärende Namen für Variablen zu wählen.
# Oft reicht ein Wort nicht aus um dem gerecht zu werden, daher gibt es zwei etablierte Wege Worte zu verketten.
# snake_case: Es wird ein Unterstrich zwischen jedes Wort gesetzt und alle Buchstaben werden klein geschrieben.
# camelCase: Mit ausnahme des ersten Buchstaben, wird jedes neue Wort mit einem Großbuchstaben begonnen.

last_name = "Stark"
country = "USA"
profession = "Engineer"

print(first_name, last_name)
print("From " + country)
print("Profession " + profession)