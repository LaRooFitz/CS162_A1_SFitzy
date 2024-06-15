# Shasta Fitzgerald
# Week 3
# Manage a Weighted Fair Queue

# Input stream file name
input_file = 'input_queue-1.txt'

# Read the input stream
with open(input_file, 'r') as file:
    input_stream = file.read().strip()

# Build the queues
premium_queue = []
standard_queue = []
economy_queue = []

# Populate the queues based on the input stream
for packet in input_stream:
    if packet == 'P':
        premium_queue.append(packet)
    elif packet == 'S':
        standard_queue.append(packet)
    elif packet == 'E':
        economy_queue.append(packet)

# Function for performing Weighted Fair Queuing
def weighted_fair_queuing(premium_queue, standard_queue, economy_queue):
    output = []
#Dequeue packets for each
    while premium_queue or standard_queue or economy_queue:
        for _ in range(3):
            if premium_queue:
                output.append(premium_queue.pop(0))

        for _ in range(2):
            if standard_queue:
                output.append(standard_queue.pop(0))

        if economy_queue:
            output.append(economy_queue.pop(0))

    return output

# Execut the WFQ function
output_packets = weighted_fair_queuing(premium_queue, standard_queue, economy_queue)

# Print the packets
print("Dequeued packets in the prioritized order: ")
print(''.join(output_packets))

