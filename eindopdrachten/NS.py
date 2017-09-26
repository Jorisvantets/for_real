def standaardprijs(afstandKM):
    km = 0
    if km > 50:
        return afstandKM * 0.6 + 15
    if afstandKM <= 0:
        return 0
    else:
        return afstandKM * 0.8

def ritprijs(leeftijd,weekendrit,afstandKM):
    kosten = standaardprijs(afstandKM)
    dag = input("welke dar reist u?")
    if dag == 'zaterdag' or dag == 'zondag':




