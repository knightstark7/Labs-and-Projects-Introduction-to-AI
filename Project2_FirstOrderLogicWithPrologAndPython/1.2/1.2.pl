region(east_asia, asia).
region(south_asia, asia).
region(southeast_asia, asia).
region(north_america, america).
region(central_america, america).
region(south_america, america).
region(western_europe, europe).
region(eastern_europe, europe).
region(north_africa, africa).
region(central_africa, africa).

country(vietnam, southeast_asia).
country(laos, southeast_asia).
country(china, east_asia).
country(japan, east_asia).
country(south_korea, east_asia).
country(russia, eastern_europe).
country(france, western_europe).
country(germany, western_europe).
country(poland, eastern_europe).
country(usa, north_america).
country(canada, north_america).
country(mexico, central_america).
country(brazil, south_america).
country(peru, south_america).
country(egypt, north_africa).
country(sudan, north_africa).
country(india, south_asia).

city(hanoi, vietnam).
city(vientiane, laos).
city(beijing, china).
city(tokyo, japan).
city(seoul, south_korea).
city(moscow, russia).
city(paris, france).
city(berlin, germany).
city(warsaw, poland).
city(washington_dc, usa).
city(ottawa, canada).
city(mexico_city, mexico).
city(brasilia, brazil).
city(lima, peru).
city(cairo,egypt). 
city(khartoum,sudan). 
city(new_delhi ,india).

capital(hanoi,vietnam). 
capital(vientiane ,laos). 
capital(beijing ,china). 
capital(tokyo ,japan). 
capital(seoul ,south_korea). 
capital(moscow ,russia). 
capital(paris ,france). 
capital(berlin ,germany). 
capital(warsaw ,poland). 
capital(washington_dc ,usa). 
capital(ottawa ,canada). 
capital(mexico_city ,mexico). 
capital(brasilia ,brazil). 
capital(lima ,peru). 
capital(cairo,egypt). 
capital(khartoum,sudan). 
capital(new_delhi ,india).

neighbor(vietnam,china).
neighbor(china,vietnam).
neighbor(vietnam ,laos).
neighbor(laos,vietnam).
neighbor(laos,china).
neighbor(china,laos).
neighbor(china,russia).
neighbor(russia,china).
neighbor(china,japan).
neighbor(japan,china).
neighbor(china,south_korea).
neighbor(south_korea,china).
neighbor(china,india).
neighbor(india,china).
neighbor(japan,south_korea).
neighbor(south_korea,japan).
neighbor(russia,poland).
neighbor(poland,russia).
neighbor(russia,germany).
neighbor(germany,russia).
neighbor(france,germany).
neighbor(germany,france).
neighbor(france,poland).
neighbor(poland,france).
neighbor(poland,germany).
neighbor(germany,poland).
neighbor(usa,mexico).
neighbor(mexico,usa).
neighbor(usa,canada).
neighbor(canada,usa).
neighbor(canada,mexico).
neighbor(mexico,canada).
neighbor(brazil,mexico).
neighbor(mexico,brazil).
neighbor(brazil,peru).
neighbor(peru,brazil).
neighbor(peru,mexico).
neighbor(mexico,peru).
neighbor(egypt,surdan).
neighbor(surdan,egypt).

neighbor(Country1, Country2, Country3) :- neighbor(Country1, Country2), neighbor(Country1, Country3).
city_region(City, Region) :- city(City, Country), country(Country, Region).
continent(Country, Continent) :- country(Country, Region), region(Region, Continent).
in_continent(City, Continent) :- city(City, Country), country(Country, Region), region(Region, Continent).
in_same_continent(City1, City2) :- in_continent(City1, Continent), in_continent(City2, Continent).
capital_continent(Capital, Continent) :- capital(Capital, Country), continent(Country, Continent).









