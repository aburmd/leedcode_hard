import collections
class Solution:                
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph=collections.defaultdict(set) #Part1...3,6
        for i,route in enumerate(routes): 
            for stop in route:
                graph[stop].add(i)
        ans=0
        queue=collections.deque([source]) #Part2...8
        seen_stops=set() #Part3...9..25
        seen_stops.add(source)
        seen_routes=set()
        while queue:
            for i in range(len(queue)):
                verifystop=queue.popleft()
                if verifystop==target:
                    return ans
                for routeId in graph[verifystop]:
                    if routeId not in seen_routes:
                        seen_routes.add(routeId)
                        for next_stop in routes[routeId]:
                            if next_stop not in seen_stops:
                                queue.append(next_stop)
                                seen_stops.add(next_stop)
            ans+=1
        return -1