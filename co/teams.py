class CustomIterTeams(object):
    def __init__(self ,division,teams=[]):
        self._mbg=division
        self._teams=teams
        self._index=1
    def __iter__(self):
        return self
    def __next__(self):
        self._index+=1
        if self._index >=len(self._teams):
            self._index =-1
            raise StopIteration
        else:
            return self._teams[self._index]
prem_teams = CustomIterTeams('Premier League', ['Arsenal', 'Watford', 'Bournemouth', 'Man Utd', 'Liverpool'])
for t in prem_teams:
    print(t)



