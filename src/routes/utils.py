from trains.models import Train


def get_routes(request, form) -> dict:
    qs = Train.objects.all()
    graph = get_graph(qs)


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


'''
from trains.models import Train
from routes.utils import get_graph
qs = Train.objects.all()
graph = get_graph(qs)
graph
'''
