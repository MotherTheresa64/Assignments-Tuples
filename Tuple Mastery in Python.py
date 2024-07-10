# Task 1: Formatting Flight Itineraries

def format_itineraries(itineraries):
    return '\n'.join(f"{name} is traveling from {origin} to {destination}." 
        for name, origin, destination in itineraries)

# Example usage
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"), ("Noah", "Missouri", "Nebraska")]
formatted_itineraries = format_itineraries(itineraries)
print(formatted_itineraries)