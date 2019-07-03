#Necessitau instalar scipy, numpy spacy i es modul de spacy "es_core_news_md"

from textAnalytics import TextAnalytics

exampleText = '''El juez de la Audiencia Nacional Manuel García Castellón ha dado un paso adelante en la investigación que lleva a cabo sobre las posibles irregularidades que pudieron cometerse como consecuencia de la contratación por parte de BBVA del excomisario de policía José Manuel Villarejo, hoy en prisión preventiva por la posible comisión de varios delitos, para que llevara a cabo tareas de inteligencia en defensa de la entidad. El juez ha citado a declarar como investigados, es decir asistidos por sus abogados, al ex consejero delegado del banco de Ángel Cano entre 2009 y 2015, que previamente fue el responsable de recursos humanos; al exresponsable de seguridad, Julio Corrochano, que dependía directamente de Cano, y a otros directivos de la entidad que pudieron tener relación con los hechos que investiga el juez.La investigación encargada en enero pasado por el banco a los bufetes Garrigues y Uría, complementados por PwC, que se encarga de llevar a cabo un análisis forensic de todo lo relacionado con la contratación de Villarejo, sigue su curso, según fuentes del banco, que afirman que no ha terminado porque "no lo hará mientras dure la investigación judicial", pero que puede haber ayudado a la que en paralelo desarrolla la Audiencia Nacional y la Fiscalía Anticorrupción, porque el banco "colabora y lo hará siempre con la Justicia" aportando la documentación que esta le solicite.'''

'''
	nota, no vos prengueu molt en serio es codi que el vaig fer per una classe i li he afegit coses a lo rapido
	i esta bastant fatal. Tot i aixi podreu agafar idees de com fer ses coses que comentavem
	A part de ses funcions rellevants per lo que xerravem hi ha mes pijadetes que igual vos serveixen d'algo
	
	i si va tant lent es per es proces de carrega des model i per com calcul es centroide de
	ses categories. Com basicament aso serà sempre es mateix, es pot tenir ja calculat i sudar de fer aso cada vegada
'''
iTA = TextAnalytics(exampleText)

'''
	agafa uns diccionaris de paraules per categoria 
	(des fitxers que hi ha a nes mateix directori) 
	i calcula frequencia per categoria
'''
print("Keyword frequency per category")
print(iTA.keywordMatch())


'''
	agafa es vectors de ses paraules des text que proporcionem
	que son noms, verbs, adjectius o adverbis, fa es vector mitja, o centroide
	i compara aso amb es centroide de ses paraules que hi ha a cada categoria.
	Aixi tenim distancia de es text a cada una de ses categories.
'''
print("Distances to each category")
print(iTA.computeCategorySimilarities())