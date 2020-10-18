
<h1 style="text-align:center">PageRank Algorithm</h1>
<img style="display: block; margin: auto;" alt="photo"  width="400" src="./images/pagerank.png">
An implementation of Google's [PageRank](https://en.wikipedia.org/wiki/PageRank) algorithm ans some use cases on real data..


## Includes
    - Implementation of PageRank Algorithm.
    - Implementation of Sparce Matrix Algorithm and Sparce Matrix operations.
    - Implementation of CSV to edgeList and Directory to edgeList  .

## Usage 

Open ```main.py```, set the path of directory or CSV file containing the graph.
Save ```main.py``` and run it.

```console
$ python3 main.py
```

## Data
- Some Graphs data is provided in ```./data```.You can use your own graphs too.
- Data specification is provided with each graph in a text file having the same file name.
- Toyset is directory of html files , from which we build a graph based on the links between page, to mimic the web-page ranking process that pagerank was made for.

## Exemple : 

- Subject : Les Miserable
- Graph : Network of coappearances of characters in Victor Hugo's novel "Les Miserables"
- Analysis: The main characters are ranked the highest, which is as expected .
```
    Valjean         : 0.07445226000296074                           
    Myriel          : 0.04427145271202669
    Gavroche        : 0.0343437542001953
    Marius          : 0.029587567869892313
    Javert          : 0.02926449485312639
    Thenardier      : 0.027086768579824064
    Fantine         : 0.02631548583961218
    Enjolras        : 0.020608234633067015
    Cosette         : 0.020195029504094377
    MmeThenardier   : 0.01897593101792316
```


