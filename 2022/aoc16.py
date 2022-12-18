from re import match
from collections import defaultdict
from heapq import *
from dataclasses import dataclass, field

# FILENAME = "aoc16-0.txt"
FILENAME = "aoc16-1.txt"

TIME = 30
TEACH = 4
START = 'AA'

@dataclass(frozen = True)
class Agent:
    position: str = field(default = START)
    journey: set[str] = field(default_factory = set, compare = False)

    def move(self, target: str):
        new_journey = {*self.journey, self.position}
        return Agent(position = target, journey = set() if target in new_journey else new_journey)

@dataclass(frozen = True)
class Vaultlist:
    useful: tuple[str] = field()
    opened: set[str] = field(default_factory = set, compare = False)

    @classmethod
    def create_sorted(cls, complete):
        return Vaultlist(useful = tuple(filter(rate, sorted(complete, key = rate, reverse = True))))

    def open(self, vault: str):
        if vault in self.opened:
            return self
        return Vaultlist(useful = self.useful, opened = self.opened | {vault})

    def open_if_equal(self, source: str, target: str):
        if source != target:
            return self
        return self.open(target)

@dataclass(frozen = True, order = True)
class Way:
    distance: int
    source: str
    first_step: str = field(compare = False)
    target: str

rates = defaultdict(int)
edges = defaultdict(list)
ways = defaultdict(dict)

def parse_graph():
    with open(FILENAME, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
    for line in lines:
        if m := match(r'Valve (\w+) .*?=(\d+);.*?((?:\w\w(?:, )?)*)$', line):
            v = m.group(1)
            rates[v] = int(m.group(2))
            edges[v] = m.group(3).split(', ')
            print(v, rates[v], edges[v])

def calculate_ways():
    for v in rates.keys():
        ways[v][v] = Way(0, v, v, v)
    queue = []
    for (v, w) in ((v, w) for (v, vw) in edges.items() for w in vw):
        heappush(queue, Way(1, v, w, w))
    print(queue)

    while queue:
        way = heappop(queue)
        old = ways[way.source].get(way.target)
        if old is not None and old.distance <= way.distance:
            continue
        ways[way.source][way.target] = way
        for way_out in ways[way.target].values():
            heappush(queue, Way(way.distance + way_out.distance, way.source, way.first_step, way_out.target))
        for way_in in [way_dict[way.source] for way_dict in ways.values() if way.source in way_dict]:
            heappush(queue, Way(way_in.distance + way.distance, way_in.source, way_in.first_step, way.target))
    print(ways)

def rate(vault: str) -> int:
    return rates[vault]

def current_steam(vaults: Vaultlist) -> int:
    return sum(rates[v] for v in vaults.opened)

def useful_moves(agent: Agent, vaults: Vaultlist, avoid: str = ''):
    used = set()
    for target in vaults.useful:
        if target not in vaults.opened and target != avoid:
            next_step = ways[agent.position][target].first_step
            if not next_step in agent.journey and not next_step in used:
                used.add(next_step)
                yield (next_step, target)
    if not used:
        yield (agent.position, agent.position)

def upper_bound(agents, time: int, vaults: Vaultlist) -> int:
    return current_steam(vaults) * time + sum((rate(target) * max(0, time - min(ways[agent.position][target].distance for agent in agents) - 1) for target in vaults.useful if not target in vaults.opened))

def steam1(agent: Agent, time: int, vaults: Vaultlist, steam: int, maximum: list[int]) -> int:
    if time >= 3:
        if steam + upper_bound((agent,), time, vaults) < maximum[0]:
            return 0
    steam += current_steam(vaults)
    if steam > maximum[0]:
        maximum[0] = steam
        print(1, steam)
    if time == 1:
        return steam
    return max(
        (steam1(agent.move(next_step),
                time - 1,
                vaults.open_if_equal(agent.position, next_step),
                steam,
                maximum)
         for (next_step, _) in useful_moves(agent, vaults)),
        default = 0)

def steam2(me: Agent, elephant: Agent, time: int, vaults: Vaultlist, steam: int, maximum: list[int]) -> int:
    if time >= 3:
        if steam + upper_bound((me, elephant), time, vaults) < maximum[0]:
            return 0
    steam += current_steam(vaults)
    if steam > maximum[0]:
        maximum[0] = steam
        print(2, steam)
    if time == 1:
        return steam
    return max(
        (steam2(me.move(my_step), elephant.move(eleph_step),
                time - 1,
                vaults.open_if_equal(me.position, my_step).open_if_equal(elephant.position, eleph_step),
                steam,
                maximum)
         for (my_step, my_vault) in useful_moves(me, vaults)
         for (eleph_step, _) in useful_moves(elephant, vaults, my_vault)),
        default = 0)

parse_graph()
calculate_ways()

print(1, steam1(Agent(START), TIME, Vaultlist.create_sorted(rates.keys()), 0, [0]))
print(2, steam2(Agent(START), Agent(START), TIME - TEACH, Vaultlist.create_sorted(rates.keys()), 0, [0]))
