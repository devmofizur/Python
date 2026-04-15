
class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dictionary = {}
        
        for start,end in self.edges: # List to Dictionary to get same start node connections
            if start in self.graph_dictionary:
                self.graph_dictionary[start].append(end)
            else:
                self.graph_dictionary[start] = [end]
        print("Graph dict :" , self.graph_dictionary)
    
    def get_paths(self,start,end, path=[]): #Kind of linear search to find all paths
        path = path + [start]

        if start == end:
            return path
        if start not in self.graph_dictionary:
            return []
        
        paths =[]

        for node in self.graph_dictionary[start]:
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return path
        if start not in self.graph_dictionary:
            return None
        
        shortest_path = None
        for node in self.graph_dictionary[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Tokyo"),
        ("Mumbai", "Abu Dhabi"),
        ("Dhaka", "Tokyo"),
        ("Abu Dhabi", "Dhaka"),
        ("Dubai", "NY"),
        ("NY", "Bustan"),
        ("NY", "Abu Dhabi"),
        ("Abu Dhabi", "Bustan"),
        ("Tokyo", "Abu Dhabi"),
        ("Mumbai", "Dubai"),
        ("Dubai", "London"),
        ("London", "NY"),
        ("Dhaka", "Dubai"),
        ("Tokyo", "Berlin"),
        ("Berlin", "London"),
        ("London", "Paris"),
        ("Paris", "Bustan"),
        ("Sydney", "Mumbai"),
        ("Sydney", "Tokyo"),
        ("Abu Dhabi", "Paris"),
        ("Berlin", "Bustan")
    ]

    route_graph = Graph(routes)

    start = "Mumbai"
    end = "Bustan"
    print(f"Shortest path from {start} to {end}: ", route_graph.get_shortest_path(start, end))

    start_2 = "Dhaka"
    print(f"Shortest path from {start_2} to {end}: ", route_graph.get_shortest_path(start_2, end))