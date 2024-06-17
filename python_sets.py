#1. Python Sets Adventure
#Task 1. Flight Route Comparison

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_destinations = our_routes.intersection(competitor_routes)
print("Common destinations:", common_destinations)

unique_to_our_airline = our_routes.difference(competitor_routes)
print("Unique to our airline:", unique_to_our_airline)

neither_shared_destinations = our_routes.symmetric_difference(competitor_routes)
print("Neither shared destinations:", neither_shared_destinations)

#2 Set Operations in Data Analysis
#Task 1: Duplicate Entries Cleanup
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_customer_ids = set(customer_ids)

print("Unique customer IDs: ", unique_customer_ids)

#3 Music Festival Playlist Organization
#Task 1: Artist Lineup Compilation

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

for artist in artist_names:
    unique_artists.add(artist)

duplicate_playlists_found = len(artist_names) != len(unique_artists)
print("Duplicate playlists found:", duplicate_playlists_found)