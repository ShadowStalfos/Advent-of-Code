class Sourcemapper():
    def __init__(self):
        self.source_lower = []
        self.source_upper = []
        self.desination = []
        self.desination_upper = []
    
    def source2dest(self, source, destination, range_len):
        self.source_lower.append(source)
        self.source_upper.append(source+range_len-1)
        self.desination.append(destination)
        self.desination_upper.append(destination+range_len-1)

    def sort(self):
        indexes = sorted(range(len(self.source_lower)), key=self.source_lower.__getitem__)
        self.source_lower = [self.source_lower[i] for i in indexes]
        self.source_upper = [self.source_upper[i] for i in indexes]
        self.desination = [self.desination[i] for i in indexes]
        self.desination_upper = [self.desination_upper[i] for i in indexes]

    def get_dest(self, source, i):
        return self.desination[i]+source-self.source_lower[i]
    
    def map_range(self, range_tup):
        lower, upper = range_tup
        ranges = []
        if lower == upper:
            for i in range(len(self.source_lower)):
                source_lower = self.source_lower[i]
                source_upper = self.source_upper[i]
                if lower < source_lower:
                    ranges.append((lower, min(upper, source_lower-1)))
                    return ranges
                elif source_lower <= lower <= source_upper and lower != upper:
                    ranges.append((self.get_dest(lower, i), self.get_dest(min(upper, source_upper), i)))
                    return ranges
            else:
                ranges.append((lower, upper))
                return ranges

        for i in range(len(self.source_lower)):
            source_lower = self.source_lower[i]
            source_upper = self.source_upper[i]
            if lower < source_lower:
                ranges.append((lower, min(upper, source_lower-1)))
                lower = min(source_lower, upper)
            if source_lower <= lower <= source_upper and lower != upper:
                ranges.append((self.get_dest(lower, i), self.get_dest(min(upper, source_upper), i)))
                lower = min(upper, source_upper)
            if lower == upper:
                return ranges
        else:
            ranges.append((lower, upper))
            return ranges

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
    
    def map_seed(self, lower, range_len):
        upper = lower+range_len-1
        ranges = (lower, upper)
        return self.recursive_map(ranges, 0)
    
    def recursive_map(self, range_tup, map_i):
        ranges = self.maps[map_i].map_range(range_tup)
        if map_i == len(self.maps)-1:
            return ranges[0][0]
        
        locs = []
        for r in ranges:
            locs.append(self.recursive_map(r, map_i+1))
        return min(locs)
        
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
    seeds = seeds.split(" ")[1:]
    for i in range(0,len(seeds), 2):
        loc = mapper.map_seed(int(seeds[i]), int(seeds[i+1]))
        if loc<lowest_loc:
            lowest_loc = loc
print(lowest_loc)