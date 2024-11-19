class Sourcemapper():
    def __init__(self):
        self.source_lower = []
        self.source_upper = []
        self.desination = []
    
    def source2dest(self, source, destination, range_len):
        self.source_lower.append(source)
        self.source_upper.append(source+range_len-1)
        self.desination.append(destination)

    def sort(self):
        indexes = sorted(range(len(self.source_lower)), key=self.source_lower.__getitem__)
        self.source_lower = [self.source_lower[i] for i in indexes]
        self.source_upper = [self.source_upper[i] for i in indexes]
        self.desination = [self.desination[i] for i in indexes]
    
    def map(self, x):
        if x < self.source_lower[0]:
            return x

        i = 0
        while i < len(self.source_lower) and x > self.source_lower[i]:
            i+=1
        i-=1

        if x < self.source_upper[i]:
            return self.desination[i]+(x-self.source_lower[i])

        return x

    

class AutoMapper():
    def __init__(self):
        self.seed_to_soil = Sourcemapper()
        self.soil_to_fertilizer = Sourcemapper()
        self.fertilizer_to_water = Sourcemapper()
        self.water_to_light = Sourcemapper()
        self.light_to_temperature = Sourcemapper()
        self.temperature_to_humidity = Sourcemapper()
        self.humidity_to_location = Sourcemapper()
        self.maps = [self.seed_to_soil, self.soil_to_fertilizer, self.fertilizer_to_water, self.water_to_light, self.light_to_temperature, self.temperature_to_humidity, self.humidity_to_location]
    
    def source2dest(self, source, destination, range_len, map_i):
        self.maps[map_i].source2dest(source, destination, range_len)
    
    def map_seed(self, seed):
        x = seed
        for seed_map in self.maps:
            x = seed_map.map(x)
        return x

    def sort_maps(self):
        for seed_map in self.maps:
            seed_map.sort()


mapper = AutoMapper()

with open("./Day5/almanac.txt") as f:
    seeds = next(f)
    next(f)
    map_i = -1
    for line in f:
        if line[0].isnumeric():
            dest, source, range_len = line.split("\n")[0].split(" ")
            mapper.source2dest(int(source), int(dest), int(range_len), map_i)
        elif line[0] != "\n":
            map_i += 1
    mapper.sort_maps()
    lowest_loc = 10**99
    for seed in seeds.split(" ")[1:]:
        loc = mapper.map_seed(int(seed))
        if loc<lowest_loc:
            lowest_loc = loc
print(lowest_loc)
