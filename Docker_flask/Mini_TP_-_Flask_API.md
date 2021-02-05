# Mini TP - Flask API

**Avant de commencer**
Faite des recherche sur la documentation [ici](https://flask.palletsprojects.com/en/1.1.x/) ainsi que sur le web sur Flask et essayez de comprendre les concepts/questions ci-dessous:  

1. Qu'est ce que flask et comment on lance une application. 

	Flask est un framework web, ou plutôt, un micro-framework. Ce “micro” signifie simplement que Flask ne fait pas tout. Cela signifie aussi que pour en faire plus que ce qu’il permet de base, il faudra installer des extensions. Heureusement, celles-ci sont nombreuses, de qualité, et très bien intégrées.

2. Comprendre ce qu'est un code HTTP, [wikipedia sur le sujet](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) 👀

	Un code qui permet de déterminer le résultat d'une requête ou d'indiquer une erreur au client.
	Les codes les plus courants sont :

		200 : succès de la requête ;
		301 et 302 : redirection, respectivement permanente et temporaire ;
		401 : utilisateur non authentifié ;
		403 : accès refusé ;
		404 : page non trouvée ;
		500 et 503 : erreur serveur ;
		504 : le serveur n'a pas répondu.

3. A quoi sert le `if __name__ = "__main__" ` ? 
	
	On lance notre application en mode debug, qui nous aidera à détecter les erreurs dans notre code. Le mode debug nous offre un second avantage : essayer de modifier ce fichier (par exemple, faites afficher “Coucou” au lieu de “Hello !”), sauvegardez le, et actualisez la page dans votre navigateur web : le site a été mis à jour sans besoin de relancer le programme avec python hello.py. Le mode debug est donc bien pratique pour développer, mais à ne surtout par laisser quand votre site sera disponible sur Internet.

4. Qu’est ce qu’une route ?

	@app.route qui permets de spécifier une URL d'accès à une vue, en filtrant les méthodes HTTP autorisées en prenant en paramètre une route .
	Cette route est celle par laquelle notre fonction sera accessible.
	La route ‘/’ est spéciale puisqu’elle représente la racine du site web. Il n’est donc pas besoin de la préciser dans l'adresse du navigateur.
	 

5. A quoi servent les fichiers statiques ? Qu’est ce qu’un template ?

	Un moteur de templates sert à insérer intelligemment et élégamment le contenu de nos variables dans des pages HTML.

6. A quoi sert le *Jinja2* ? 

	Jinja est un moteur de templates pour le langage de programmation Python.
	il permets de gérer des boucles, des tests logiques, des listes ou des variables, il permets de faire des développements avancés et sont indispensables pour la gestion de la fonctionnalité ZTP (Zero Touch Provisioning) des équipements réseau.

"Référence : http://sdz.tdct.org/sdz/creez-vos-applications-web-avec-flask.html#LeprotocoleHTTP"


**Quickstart** 

Ecrire une application flask suivant le modele ci-dessus avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello BG"
* une route qui renvoie "hello name", ou name est une variable string 
	* on devra donc trouver "hello name" à la route (http:localhost:5000/ma_route/name) avec la possibilité de changer la variable name. 
* refaite la meme chose en ajoutant un template 


**Contexte**

Vous avez répondu à l'appel d'offre d'une mairie qui consiste à digitaliser la bibliothèque de la commune. Il faudra pour cela proposer un "catalogue" en ligne de leur ressources et donner la possibilité au utilisateur du site de faire des recherches de livre. On supposera que la bibliothèque nous met à disposition ces livres via un fichier `.json` ci-dessous. 
Vous devez donc construire une api (application flask) avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello my app"
* instancier une variable `book` dans votre aopplication tel que : 
```
book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
```
* faite une route `/api/books` avec une méthode `GET` qui retourne cette variable sous forme de json 
* faite une route qui retourne un book selon son `id` 
* faite une route qui retourne un book selon son titre 
* chager le fichier [books.json](https://drive.google.com/file/d/1UdRCm5d5UAPnfjGes_rHZl2kDQ9NNAsG/view?usp=sharing) et faite de même avec ce fichier
* **(bonus 1)** écrire un template pour le résultat de la recherche
* **(bonus 2)** Coder un site type vitrine/portfolio en flask et le déployer avec github pages