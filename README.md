#Présentation du code

Le code contenu dans ce dossier est un écrit en Python. Le code commenté contient 3 parties: <br/>
* **Question 1 (partie 1)** : celle-ci répond à la question 1, à savoir compter tout les 
éléments dont la valeur est supérieur au seuil (0.5)
  
* **Question 2 (partie 2)** : celle-ci répond à la question 2. Ici, nous établissons un 
modèle de vecteur. Le but est de tester les combinaisons pour chaque ligne et ensuite de compter
  les combinaisons de somme supérieure au seuil.
  
* **Question 3 (partie 3)** : celle-ci répond à la question 2, à savoir calculer la max, le min et la moyenne
des éléments dont la valeur est supérieur au seuil.
  


# Et Hadoop dans tout ceci ? 
Hadoop fonctionne avec Java non ? Pourquoi utilisons-nous Python ? <br/>
Hadoop nous offre la possibilité d'utiliser n'importe quel langage de programmation 
pour écrire le MapReduce. En effet, il existe une fonctionnalité qui s'appelle Hadoop Streaming
qui va nous permettre d'exécuter notre MapReduce comme si c'était du java.

#Etapes pour exécuter le code
Tout d'abord nous testons notre code en locale avec MRJOB pour un fichier de petite taille.

```shell
$ cd <CHEMIN_DU_REPERTOIRE_DU_FICHIER_PYTHON>
$ python3 mapper_reducer.py  <FICHIER_DENTREE>
```


<br/>
Puis On se place dans le répertoire d'installation Hadoop ($HADOOP_HOME). Puis on démarre notre
Cluster.
 	

```shell
$ cd $HADOOP_HOME
$ sbin/./start-dfs.sh
$ sbin/./start-yarn.sh
```

Ensuite, nous faisons un upload du fichier à traiter (fichier généré) vers le HDFS.

```shell
$ hdfs dfs -D dfs.blocksize=67108864 -put <CHEMIN_FICHIER_A_COPIER> <REPERTOIRE DARRIVEE>
```

Il nous reste à démarrer le streaming de notre Job (MapReduce). On se place dans le répertoire 
contenant notre fichier python "mapper_reducer.py" puis on exécute le streaming Hadoop.

```shell
$ cd <CHEMIN_DU_REPERTOIRE_DU_FICHIER_PYTHON>
$ python3 mapper_reducer.py -r hadoop hdfs://<CHEMIN_DU_FICHIER_DANS_HDFS>  >  <FICHIER_RESULTAT>
```
