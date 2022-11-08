import pandas

WC_DF = pandas.read_csv("worldcities.csv")


# Question 1a answer cell
def non_ascii_cities():
    non_ascii = {i for i in WC_DF["city"] if not i.isascii()}
    return non_ascii
    # TODO: Modify to return a set of all non-ascii city names in the world_cities data


# Question 1b answer cell
def num_cities_occurring_n_times(n):
    find_city = WC_DF["city"].value_counts() == n
    detect_true = find_city.value_counts(sort=False)
    return detect_true[True]
    # TODO: Modify to return a value according to the specification given above


# Question 1c answer cell
def country_num_cities_dict():
    find_country = WC_DF["country"].value_counts()  # <---counting rows
    return find_country.to_dict()
    # TODO: Write a function that returns a dictionary (a dict object), whose keys are all the country name strings
    #  that occur in the worldcities data and whose values are ints giving the number of cities of that country that
    #  are included in the dataset.


# Question 1d answer cell
def largest_cities_dataframe(n):
    WC_DF.sort_values(["population"], ascending=[False])
    return WC_DF[:n]
    # TODO: Modify to return a list of the n cities with the largest population


# Complete question 1e in this cell
def big_cities_in_country(country, population):  # country is a string argument
    big_cities_list = []
    ordered_df = WC_DF[WC_DF["country"] == country].sort_values(["population"], ascending=[True])
    for i, row in ordered_df.iterrows():
        if row["population"] >= population:
            # if row["population"] != row["population"]:#todo--- testing nan value
            #     print(row["population"], " ----- ", row["city"])#todo
            current_cities_tuple = ()
            current_cities_tuple += (row["city_ascii"],)
            current_cities_tuple += (row["population"],)
            big_cities_list.append(current_cities_tuple)
    return big_cities_list
    # TODO: Edit this function to return a list, as specified above


# Question 1f Answer Code Cell
def country_total_cities_population(country):
    big_cities_list = big_cities_in_country(country, 0)
    total_population = 0.0
    for i in big_cities_list:
        total_population = total_population + i[1]
    return int(total_population)
    # TODO: Create a function that given a country name, returns an int which is the total population of people living
    #  in all the cities of that country, as given in WC_DF.


print(non_ascii_cities())
print(num_cities_occurring_n_times(2))
print(country_num_cities_dict())
print(largest_cities_dataframe(5))
print(big_cities_in_country("India", 0))
# todo: change single to doubble inverted commas-------     <----DONE
# todo: manage missing data----------     <-----
print(country_total_cities_population("India"))




# ---------------------------------2---------------------------------------------------

