import sys
# Takes input
data = {}
while True:
    line = sys.stdin.readline()
    if len(line) < 3:
        break
    else:
        end1 = line.find(':')
        winner = line[:end1]
        new_line = line[end1+1:]
        end2 = new_line.find(':')
        looser = new_line[:end2]
        set_ = line.count('-')

        # Creating player profile in dictionary if not in dictionary
        try :
            data[winner]
        except KeyError:
            data[winner] = {'B5W':0, 'B3W':0, 'SW':0, 'GW':0, 'SL':0, 'GL':0}
        try:
            data[looser]
        except KeyError:
            data[looser] = {'B5W':0, 'B3W':0, 'SW':0, 'GW':0, 'SL':0, 'GL':0}

        # Won best of 5 and 3
        if line.count('-') < 4 :
            #increase B3W for winner
            data[winner]['B3W'] = data[winner]['B3W'] + 1
        elif line.count('-') > 3 :
            # increase B5W for winner
            data[winner]['B5W'] = data[winner]['B5W'] + 1

        # Totall set Won and lost
        if set_ == 5 :
            # Update winner
            data[winner]['SW'] = data[winner]['SW'] + 3 # Set won
            data[winner]['SL'] = data[winner]['SL'] + 2 # Set lost
            # Update looser
            data[looser]['SW'] = data[looser]['SW'] + 2 # Set won
            data [looser]['SL'] = data [looser]['SL'] + 3 # Set lost

        elif set_ == 4 :
            # Update winner
            data[winner]['SW'] = data[winner]['SW'] + 3 # Set won
            data[winner]['SL'] = data[winner]['SL'] + 1 # Set lost
            # Update looser
            data[looser]['SW'] = data[looser]['SW'] + 1 # Set won
            data [looser]['SL'] = data [looser]['SL'] + 3 # Set lost

        elif set_ == 3 :
            # Update winner
            data[winner]['SW'] = data[winner]['SW'] + 2 # Set won
            data[winner]['SL'] = data[winner]['SL'] + 1 # Set lost
            # Update looser
            data[looser]['SW'] = data[looser]['SW'] + 1 # Set won
            data [looser]['SL'] = data [looser]['SL'] + 2 # Set lost
        else:
            # Update winner
            data[winner]['SW'] = data[winner]['SW'] + 2 # Set won
            data[winner]['SL'] = data[winner]['SL'] + 0 # Set lost
            # Update looser
            data[looser]['SW'] = data[looser]['SW'] + 0 # Set won
            data [looser]['SL'] = data [looser]['SL'] + 2 # Set lost

        # Update Game won and lost
        winner_score = 0
        looser_score = 0
        score_board = line
        for s in range(set_):
            separator = score_board.find('-')
            winner_score += int(score_board[separator-1])
            looser_score += int(score_board[separator+1])
            score_board = score_board[score_board.find('-')+1:]
        # Update game won and lost in dictionary
        data[winner]['GW'] = data[winner]['GW'] + winner_score # Game won
        data[winner]['GL'] = data[winner]['GL'] + looser_score # Game Lost

        data[looser]['GW'] = data[looser]['GW'] + looser_score # Game won
        data[looser]['GL'] = data[looser]['GL'] + winner_score # Game lost

sorted_keys = sorted(data, key=lambda x: (data[x]["B5W"],data[x]['B3W'],data[x]["SW"],data[x]['GW']))
count = len(sorted_keys)-1
for keys in sorted_keys:
    i = sorted_keys[count]
    print(i,data[i]['B5W'],data[i]['B3W'],data[i]['SW'],data[i]['GW'],data[i]['SL'],data[i]['GL'])
    count -= 1
