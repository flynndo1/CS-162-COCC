# Build three queues for Premium, Standard, and Economy
queue_premium = []
queue_standard = []
queue_economy = []

#Import input packets from text file
with open("input queue-1.txt") as packet_list:
    #Append packets to their respective queues
    for packet in packet_list:
        prefix, name = packet.split(" ", 1)
        name = name.strip()
        if prefix == 'P':
            queue_premium.append(name)
        elif prefix == 'S':
            queue_standard.append(name)
        elif prefix == 'E':
            queue_economy.append(name)

#Apply weighted fair queueing
def apply_wfq(queue_premium, queue_standard, queue_economy):
    """This function applies WFQ to manage the stream of packets."""
    weighting = ['P', 'P', 'P', 'S', 'S', 'E']
    output = []

    while queue_premium or queue_standard or queue_economy:
        for item in weighting:
            if item == 'P' and queue_premium:
                output.append(('P', queue_premium.pop(0)))
            elif item == 'S' and queue_standard:
                output.append(('S', queue_standard.pop(0)))
            elif item == 'E' and queue_economy:
                output.append(('E', queue_economy.pop(0)))
    return output

def dequeue():
    """Calls the apply_wfq function on each packet."""
    output = apply_wfq(queue_premium, queue_standard, queue_economy)
    print('Output:')
    for i, (item, name) in enumerate(output, start=1):
        print(f'{i}. {item} {name}')

#Run the function
dequeue()