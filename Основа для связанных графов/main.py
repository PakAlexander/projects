class Vertex:
    def __init__(self):
        self._links = []    # список связей с другими вершинами графа (список объектов класса Link).

    @property
    def links(self):
        return self._links

class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, dist):
        self._dist = dist

    @property
    def nodes(self):
        return self.v1, self.v2

class LinkedGraph:
    def __init__(self):
        self._links = []    # список из всех связей графа (из объектов класса Link)
        self._vertex = []   # список из всех вершин графа (из объектов класса Vertex)

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        t = tuple(filter(lambda x: (id(x.v1) == id(link.v1) and id(x.v2) == id(link.v2)) or \
                                   (id(x.v2) == id(link.v1) and id(x.v1) == id(link.v2)), self._links))

        if len(t) == 0:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def find_path(self, v_start, v_end):
        result_arr = []
        self.step_path(v_start, v_end, list(), list(), result_arr)
        result_arr.sort(key=lambda val: val[2])
        result_value = (result_arr[0][0], result_arr[0][1])
        return result_value

    def step_path(self, v_cur, v_end, node_list=None, link_list=None, result_arr=None):
        if node_list == None: node_list = []
        if link_list == None: link_list = []
        if result_arr == None: result_arr = []

        for link in self.get_links(v_cur, node_list):
            if v_end in link.nodes:
                node_list.append(v_cur)
                node_list.append(v_end)
                link_list.append(link)
                result_arr.append((node_list, link_list, sum([l.dist for l in link_list])))
            else:
                new_node_list = node_list.copy()
                new_node_list.append(v_cur)
                new_link_list = link_list.copy()
                new_link_list.append(link)
                v_next = link.v1 if link.v1 != v_cur else link.v2
                self.step_path(v_next, v_end, new_node_list, new_link_list, result_arr)

    def get_links(self, v_request, route_list=None):
        if route_list == None: route_list = []
        return list(filter(lambda x: v_request in x.nodes and x.v1 not in route_list and x.v2 not in route_list, self._links))

class  Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class  LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self.dist = dist




