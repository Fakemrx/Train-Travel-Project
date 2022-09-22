from trains.models import Train


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)
    return graph


def get_routes(request, form) -> dict:  # По хорошему разбить на
    # несколько функций с обработкой путей по отдельности
    # (по параметру время/включенные города и т.п.)
    qs = Train.objects.all().select_related('from_city', 'to_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    travelling_time = data['travelling_time']
    if type(travelling_time) != int:
        travelling_time = 9999
    cities = data['cities']
    all_ways = list(dfs_path(graph, from_city.id, to_city.id))
    context = {
        'form': form
    }
    if not len(list(all_ways)):
        raise ValueError('Нет маршрута с заданными условиями')
    elif cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if len(right_ways) == 0:
            raise ValueError(f'Маршрут через указанные города невозможен')
            # \n!{right_ways}!\n{route}')
    else:
        right_ways = all_ways
    routes = []
    all_trains = dict()
    min_time = 9999
    for q in qs:
        all_trains.setdefault((q.from_city_id, q.to_city_id), [])
        all_trains[(q.from_city_id, q.to_city_id)].append(q)
    for route in right_ways:
        tmp = dict()
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_trains[(route[i], route[i + 1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= travelling_time:
            routes.append(tmp)
            if total_time < min_time:
                min_time = total_time
    if not routes:
        raise ValueError('Нет маршрутов с временем меньше указанного')
    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)
        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)
    context['min_time'] = min_time
    context['routes'] = sorted_routes
    context['cities'] = {'from_city': from_city.name, 'to_city': to_city.name}
    return context
