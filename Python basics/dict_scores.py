def check_result(table):
    teams = {}
    for games in table:
        for team in games[::2]:
            if team not in teams:
                teams[team] = {'games': 1, 'win': 0, 'draw': 0, 'loss': 0, 'scores': 0}
            else:
                teams[team]['games'] += 1

        # 0 - выиграл, 2 - проиграл
        if int(games[1]) > int(games[3]):
            teams[games[0]]['win'] += 1
            teams[games[0]]['scores'] += 3
            teams[games[2]]['loss'] += 1

        # ничья
        elif int(games[1]) == int(games[3]):
            teams[games[0]]['draw'] += 1
            teams[games[2]]['draw'] += 1
            teams[games[0]]['scores'] += 1
            teams[games[2]]['scores'] += 1

        # 2 - выиграл, 0 - проиграл
        else:
            teams[games[2]]['win'] += 1
            teams[games[2]]['scores'] += 3
            teams[games[0]]['loss'] += 1

    return teams


def main():
    games_result = []  # [['Спартак', '8', 'Зенит', '9'], ['Зенит', '4', 'Локомотив', '1']]
    count = int(input())
    for _ in range(count):
        games_result.append(input().split(';'))

    teams = check_result(games_result)
    for teams, scores in teams.items():
        print(f'{teams}:', end='')
        for item, score in scores.items():
            print(score, end=' ')
        print('')


if __name__ == '__main__':
    main()
