import re, csv,os

def digits(val):
    digits=re.sub("\D", "", val)
    if(digits):
        return int(digits)
    return 0 
def format_key(key):
    key = key.strip() 
    if key.startswith('"') and key.endswith('"'):
        key = key[1:-1]
    return key 


def generate_edgeList_csv (file_path, undirected=True):
    csv_file = csv.reader(open(file_path, 'r'), delimiter=',')
    data = [row for row in csv_file]
    nodes = list(set([format_key(row[0]) for row in data]+[format_key(row[2]) for row in data]))
    mapper=dict([(nodes[i],i) for i in range(len(nodes))]) #map node name to an ID 
    inv_mapper=dict([(i,nodes[i]) for i in range(len(nodes))]) # Inverse Map Id to nodes name
    edgeList=[]
    if(undirected): 
        for row in data: 
            edgeList.append(
                (
                    mapper[format_key(row[0])],
                    mapper[format_key(row[2])]
                )
                )
            edgeList.append(
                (
                    mapper[format_key(row[2])],
                    mapper[format_key(row[0])]
                )
                )
    else: 
        for row in data: 

            if digits(row[1]) >=  digits(row[3]):
                edgeList.append(
                    
                    (mapper[format_key(row[0])], 
                    mapper[format_key(row[2])]
                    )
                    )
            else:
                 edgeList.append(
                    (
                        mapper[format_key(row[2])],
                        mapper[format_key(row[0])]
                    )
                    )

    return(list(set(edgeList)),mapper,inv_mapper)


def generate_edgeList_file(file_path):
    with open(file_path,'r') as file:
        data=file.read()
    data=data.split()
    edgeList=[(int(data[i])-1,int(data[i+1])-1) for i in range(0,len(data),2)]
    nbrOfVertex=len(set([int(i) for i in data]))
    return(nbrOfVertex,edgeList)


def generate_edgeList_directory(dir_path):
    pages=[os.path.join(dir_path, page).split("/")[-1].split(".")[0] for page in os.listdir(dir_path)  if page.endswith(".html")  ]
    mapper=dict([(pages[i],i) for i in range(len(pages))]) #map page name to an ID 
    inv_mapper=dict([(i,pages[i]) for i in range(len(pages))]) # Inverse Map Id to Page name
    edgeList=[]
    for page in pages: 
        with open(dir_path+page+".html",'r') as html_file:
            html=html_file.read()
            links = re.findall(r'<a href="(.[^>]*).html"', html)
            for link in links:
                if(page!=link):
                    edgeList.append((mapper[page],mapper[link]))
    return(list(set(edgeList)),mapper,inv_mapper)